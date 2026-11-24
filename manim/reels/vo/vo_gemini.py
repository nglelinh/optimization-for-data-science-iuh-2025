"""Reusable Gemini TTS voiceover synthesis and FFmpeg timeline muxing helper.

Defaults follow Sample C (voice Algenib, simple conversational prompt, loudnorm only,
no internal silence cutting). Needs GEMINI_API_KEY in the environment.
"""
import base64
import json
import os
import re
import ssl
import subprocess
import time
import urllib.error
import urllib.request
import wave

DEFAULT_MODELS = (
    "gemini-3.8-flash-tts",
    "gemini-3.1-flash-tts-preview",
    "gemini-2.5-flash-preview-tts",
)
DEFAULT_VOICE = "Algenib"
DEFAULT_STYLE_PROMPT = (
    "Nói như đang trò chuyện với một sinh viên, thoải mái, tự nhiên, nhẹ nhàng, "
    "không đọc như đọc văn bản. Đọc đoạn sau: "
)
# Only trims silence at the very start and end of a clip (pauses inside speech are kept),
# then normalizes loudness like Sample C.
AUDIO_FILTER = (
    "silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.05,"
    "areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.15,areverse,"
    "loudnorm=I=-16:TP=-1.5:LRA=11"
)
RETRY_DELAYS = (5, 20, 45)  # seconds, backoff on HTTP 429 before trying the next model


class QuotaExhausted(RuntimeError):
    """Every model kept answering HTTP 429 (rate limit or daily quota)."""


def probe_duration(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
        text=True,
    ).strip()
    return float(out)


def _quota_info(body):
    """(retry_delay_sec or None, quota ids) from a 429 body."""
    try:
        err = json.loads(body)["error"]
    except Exception:
        return None, []
    delay, ids = None, []
    for d in err.get("details", []):
        if "retryDelay" in d:
            m = re.match(r"(\d+(?:\.\d+)?)s", d["retryDelay"])
            delay = float(m.group(1)) if m else None
        for v in d.get("violations", []):
            ids.append(v.get("quotaId", ""))
    return delay, ids


def _retry_delay(body, default):
    delay, _ = _quota_info(body)
    return min(delay + 1, 90) if delay is not None else default


def _is_daily(body):
    """Daily quota: every violated quota is a per-day one, or the server asks to wait > 5 min."""
    delay, ids = _quota_info(body)
    if ids and all("PerDay" in i for i in ids):
        return True
    return delay is not None and delay > 300


def synth_segment(text, out_wav, voice=DEFAULT_VOICE, models=DEFAULT_MODELS,
                  style_prompt=DEFAULT_STYLE_PROMPT, log=print):
    """Synthesize one segment to out_wav (cached). Returns (duration_sec, model_used)."""
    if os.path.exists(out_wav) and os.path.getsize(out_wav) > 1000:
        return probe_duration(out_wav), "cache"
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("Missing GEMINI_API_KEY in environment")

    cafile = "/etc/ssl/certs/ca-certificates.crt"
    ctx = ssl.create_default_context(cafile=cafile) if os.path.exists(cafile) else ssl.create_default_context()
    payload = {
        "contents": [{"parts": [{"text": style_prompt + text}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}},
        },
    }
    data = json.dumps(payload).encode("utf-8")

    res, used, errors = None, None, []
    for model in models:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        for attempt in range(len(RETRY_DELAYS) + 1):
            req = urllib.request.Request(
                url, data=data, method="POST",
                headers={"Content-Type": "application/json", "x-goog-api-key": key},
            )
            try:
                with urllib.request.urlopen(req, context=ctx, timeout=180) as resp:
                    res = json.loads(resp.read().decode("utf-8"))
                used = model
                break
            except urllib.error.HTTPError as e:
                body = e.read().decode("utf-8", "replace")
                if e.code == 429:
                    errors.append(f"{model}: 429 {body[:300]}")
                    if _is_daily(body) or attempt == len(RETRY_DELAYS):
                        log(f"  429 on {model} ({'daily quota' if _is_daily(body) else 'still limited'}), next model")
                        break
                    d = _retry_delay(body, RETRY_DELAYS[attempt])
                    log(f"  429 on {model}, retry in {d:.0f}s")
                    time.sleep(d)
                    continue
                if e.code in (500, 503) and attempt < len(RETRY_DELAYS):
                    time.sleep(RETRY_DELAYS[attempt])
                    continue
                if e.code == 404:  # model not available for this key
                    errors.append(f"{model}: 404")
                    break
                raise RuntimeError(f"{model}: HTTP {e.code} {body[:300]}")
            except (urllib.error.URLError, TimeoutError) as e:
                if attempt < len(RETRY_DELAYS):
                    time.sleep(RETRY_DELAYS[attempt])
                    continue
                raise
        if res is not None:
            break
    if res is None:
        raise QuotaExhausted("; ".join(errors))

    part = res["candidates"][0]["content"]["parts"][0]["inlineData"]
    rate = int((re.search(r"rate=(\d+)", part.get("mimeType", "")) or [None, 24000])[1])
    pcm = base64.b64decode(part["data"])
    raw_wav = out_wav + ".raw.wav"
    with wave.open(raw_wav, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(pcm)
    tmp = out_wav + ".tmp.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", raw_wav, "-af", AUDIO_FILTER,
                    "-ar", "24000", "-ac", "1", tmp], check=True)
    os.remove(raw_wav)
    os.replace(tmp, out_wav)
    return probe_duration(out_wav), used


def build_vo_track(segments_with_start_sec, total_duration, out_m4a):
    """Mix (wav_path, start_sec) pairs into one AAC track exactly total_duration long."""
    inputs = ["-f", "lavfi", "-t", f"{total_duration:.3f}", "-i", "anullsrc=r=24000:cl=mono"]
    filters = []
    mix_labels = ["[0:a]"]
    for idx, (wav_path, start_sec) in enumerate(segments_with_start_sec, start=1):
        inputs.extend(["-i", wav_path])
        ms = int(round(start_sec * 1000))
        filters.append(f"[{idx}:a]adelay={ms}|{ms}[a{idx}]")
        mix_labels.append(f"[a{idx}]")
    fc = ";".join(filters) + f";{''.join(mix_labels)}amix=inputs={len(mix_labels)}:duration=first:normalize=0[aout]"
    subprocess.run(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", fc, "-map", "[aout]",
                    "-t", f"{total_duration:.3f}", "-c:a", "aac", "-b:a", "128k", out_m4a], check=True)


def mux(video_in, audio_m4a, video_out):
    """Put the AAC track on the video (video stream copied if already H.264)."""
    tmp = video_out + ".tmp.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", video_in, "-i", audio_m4a,
                    "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "128k",
                    "-shortest", "-movflags", "+faststart", tmp], check=True)
    os.replace(tmp, video_out)
