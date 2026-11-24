"""Build the Vietnamese voiceover for the optimization reels.

  python vo/vo_build.py plan [reel ...]   synthesize (cached) + check timing, suggest stage pads
  python vo/vo_build.py mux  [reel ...]   mix + mux into public/videos/reels/<reel>_vi.mp4

Needs GEMINI_API_KEY (source ~/.config/gemini/tts.env). Cache: manim/reels/.vo_cache/<reel>/ (untracked).
Base timing: .vo_cache/<reel>/timing_base.json = VO_LOG of an unpadded VI dry run (stage/caption times).
Pads: vo/pads.json {"Scene": {"k": sec}} (read by rl.py for VI renders)."""
import hashlib, json, math, os, shutil, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import vo_gemini as vg
from narration_vi import REELS

ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CACHE = os.path.join(HERE, "..", ".vo_cache")
PUB = os.path.join(ROOT, "public", "videos", "reels")
PADS = os.path.join(HERE, "pads.json")
GAP, TAIL = 0.25, 0.35   # min gap between segments in a stage; silence kept before the next stage


def has_audio(p):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", p], text=True)
    return bool(out.strip())


def timeline(reel, scene, pads):
    ev = json.load(open(os.path.join(CACHE, reel, "timing_base.json")))
    S = [t for t, k, v in ev if k == "stage"]; E = ev[-1][0]
    add, S2 = 0.0, []
    for i, s in enumerate(S, start=1):
        S2.append(s + add); add += pads.get(str(i), 0)
    return S2, E + add


def plan(reel, log=print):
    file, scene, segs = REELS[reel]
    d = os.path.join(CACHE, reel); os.makedirs(d, exist_ok=True)
    allp = json.load(open(PADS)) if os.path.exists(PADS) else {}
    pads = allp.get(scene, {})
    S, E = timeline(reel, scene, pads)
    ends = S[1:] + [E]
    out, need, prev_end, prev_k = [], {}, 0.0, None
    for i, (k, off, text) in enumerate(segs):
        h = hashlib.sha1((vg.DEFAULT_VOICE + vg.DEFAULT_STYLE_PROMPT + text).encode()).hexdigest()[:8]
        wav = os.path.join(d, f"{i:02d}_{h}.wav")
        dur, model = vg.synth_segment(text, wav, models=("gemini-3.8-flash-tts",), log=log)
        start = S[k - 1] + off
        if prev_k == k: start = max(start, prev_end + GAP)
        end = start + dur; lim = ends[k - 1] - TAIL
        over = end - lim
        if over > 0 and (i + 1 == len(segs) or segs[i + 1][0] != k):
            need[str(k)] = need.get(str(k), 0) + math.ceil((over + 0.3) * 10) / 10
        elif over > 0:
            pass  # spills into the next segment of the same stage; checked there
        out.append((wav, start, dur, k, model))
        prev_end, prev_k = end, k
        log(f"  seg {i} k={k} start={start:7.2f} dur={dur:6.2f} end={end:7.2f} limit={lim:7.2f} {'OVER %.2f' % over if over > 0 else ''} [{model}]")
    return out, need, E, scene


def main():
    mode, names = sys.argv[1], (sys.argv[2:] or list(REELS))
    allp = json.load(open(PADS)) if os.path.exists(PADS) else {}
    bad = False
    for reel in names:
        print(f"== {reel}", flush=True)
        try:
            segs, need, E, scene = plan(reel)
        except vg.QuotaExhausted as e:
            print(f"QUOTA EXHAUSTED at {reel}: {e}", flush=True); sys.exit(3)
        if need:
            bad = True
            cur = allp.setdefault(scene, {})
            for k, v in need.items(): cur[k] = round(cur.get(k, 0) + v, 1)
            print(f"  NEED PADS {need} -> {cur} (re-render VI)")
            continue
        if mode == "mux":
            silent = os.path.join(CACHE, reel, "silent_vi.mp4"); pub = os.path.join(PUB, f"{reel}_vi.mp4")
            if not os.path.exists(silent):
                assert not has_audio(pub), "public video already has audio and no silent copy exists"
                shutil.copy(pub, silent)
            vd = vg.probe_duration(silent)
            assert abs(vd - E) < 0.08, f"silent video {vd:.3f}s != timeline {E:.3f}s (re-render needed?)"
            m4a = os.path.join(CACHE, reel, "vo.m4a")
            vg.build_vo_track([(w, s) for w, s, *_ in segs], vd, m4a)
            vg.mux(silent, m4a, pub)
            print(f"  MUXED {pub} {vg.probe_duration(pub):.2f}s")
    if mode == "plan" and any(allp.values()):
        json.dump(allp, open(PADS, "w"), indent=1, sort_keys=True)
    sys.exit(4 if bad else 0)


if __name__ == "__main__":
    main()
