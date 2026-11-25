"""Lồng tiếng ElevenLabs cho reel tối ưu (giọng Trường U0vnF55XGy05G83azOfJ, model eleven_v3).

  python vo/vo_build_el.py texts <reel>   in lời dẫn đã đọc ra chữ (mỗi đoạn một dòng) và tổng số ký tự
  python vo/vo_build_el.py plan  <reel>   đọc .vo_cache/<reel>/el_NN.mp3, kiểm tra tràn mục, ghi pads vào vo/pads.json
  python vo/vo_build_el.py mux   <reel>   ghép vào public/videos/reels/<reel>_vi.mp4 (bản không tiếng lấy từ .vo_cache/<reel>/silent_vi.mp4)

Lời dẫn lấy từ narration_vi.py; chữ cái đơn đọc thành tên chữ (ích, ét, tê...), ISTA/FISTA/LP đọc ra chữ.
Mỗi đoạn mp3 tạo bằng creative_generate_speech và lưu thành .vo_cache/<reel>/el_NN.mp3 (NN = thứ tự đoạn, từ 00); cache không commit.
Mốc thời gian dùng lại timeline() của vo_build.py (timing_base.json không pads + vo/pads.json)."""
import json, math, os, re, shutil, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import vo_gemini as vg
import vo_build as vb
from narration_vi import REELS

LETTERS = {"x": "ích", "y": "i-grếch", "z": "dét", "t": "tê", "p": "pê", "d": "đê", "f": "ép", "g": "giê",
           "h": "hát", "s": "ét", "a": "a", "b": "bê", "c": "xê", "e": "e", "l": "e-lờ", "k": "ca", "n": "en", "m": "em"}
WORDS = [("FISTA", "Fít-ta"), ("ISTA", "Ít-ta"), ("LP", "quy hoạch tuyến tính")]


def spoken(t):
    for a, b in WORDS:
        t = t.replace(a, b)
    return re.sub(r"(?<![\w-])([A-Za-z])(?![\w-])", lambda m: LETTERS[m.group(1).lower()], t)


def texts(reel):
    return [(k, off, spoken(t)) for k, off, t in REELS[reel][2]]


def plan(reel, log=print):
    file, scene, _ = REELS[reel]
    segs = texts(reel)
    d = os.path.join(vb.CACHE, reel)
    allp = json.load(open(vb.PADS)) if os.path.exists(vb.PADS) else {}
    S, E = vb.timeline(reel, scene, allp.get(scene, {}))
    ends = S[1:] + [E]
    out, need, prev_end, prev_k = [], {}, 0.0, None
    for i, (k, off, text) in enumerate(segs):
        mp3 = os.path.join(d, f"el_{i:02d}.mp3"); wav = os.path.join(d, f"el_{i:02d}.wav")
        if not os.path.exists(wav):  # chỉ chỉnh âm lượng, không cắt khoảng lặng
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", mp3, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "24000", "-ac", "1", wav], check=True)
        dur = vg.probe_duration(wav)
        start = S[k - 1] + off
        if prev_k == k: start = max(start, prev_end + vb.GAP)
        end = start + dur; lim = ends[k - 1] - vb.TAIL; over = end - lim
        if over > 0 and (i + 1 == len(segs) or segs[i + 1][0] != k):
            need[str(k)] = need.get(str(k), 0) + math.ceil((over + 0.3) * 10) / 10
        out.append((wav, start, dur, k))
        prev_end, prev_k = end, k
        log(f"  seg {i} k={k} start={start:7.2f} dur={dur:6.2f} end={end:7.2f} limit={lim:7.2f} {'OVER %.2f' % over if over > 0 else ''}")
    return out, need, E, scene, allp


def main():
    mode, reel = sys.argv[1], sys.argv[2]
    if mode == "texts":
        ts = texts(reel); total = 0
        for i, (k, off, t) in enumerate(ts):
            print(i, k, len(t), t); total += len(t)
        print("TOTAL", total); return
    segs, need, E, scene, allp = plan(reel)
    if need:
        cur = allp.setdefault(scene, {})
        for k, v in need.items(): cur[k] = round(cur.get(k, 0) + v, 1)
        if mode == "plan":
            json.dump(allp, open(vb.PADS, "w"), indent=1, sort_keys=True)
        print(f"NEED PADS {need} -> {cur} (re-render VI, copy to public and silent_vi.mp4)"); sys.exit(4)
    if mode == "mux":
        d = os.path.join(vb.CACHE, reel); silent = os.path.join(d, "silent_vi.mp4"); pub = os.path.join(vb.PUB, f"{reel}_vi.mp4")
        if not os.path.exists(silent):
            assert not vb.has_audio(pub), "public video already has audio and no silent copy exists"
            shutil.copy(pub, silent)
        vd = vg.probe_duration(silent)
        assert abs(vd - E) < 0.08, f"silent video {vd:.3f}s != timeline {E:.3f}s (re-render needed?)"
        m4a = os.path.join(d, "vo_el.m4a")
        vg.build_vo_track([(w, s) for w, s, *_ in segs], vd, m4a)
        vg.mux(silent, m4a, pub)
        print(f"MUXED {pub} {vg.probe_duration(pub):.2f}s audio={vb.has_audio(pub)}")
    else:
        print("OK no pads needed")


if __name__ == "__main__":
    main()
