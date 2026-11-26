# -*- coding: utf-8 -*-
from common import *
import os, json

def card(w, h, color=SKY):
    return RoundedRectangle(width=w, height=h, corner_radius=0.22,
                            fill_color=CARD, fill_opacity=0.92,
                            stroke_color=color, stroke_width=2.5)

def make_header(tag, title):
    t1 = fit(T(tag, 22, SUN), 7.6)
    t2 = fit(T(title, 32, WHITE), 7.8)
    return VGroup(t1, t2).arrange(DOWN, buff=0.14).move_to([0, 6.2, 0])

def setup_vo(scene):
    vo_durs = json.load(open(os.environ["VO_DUR_JSON"])) if os.environ.get("VO_DUR_JSON") else {}
    tl_path = os.environ.get("VO_TIMELINE_JSON")
    timeline = []
    def end_vo(sid, t0, fb):
        dur = vo_durs.get(sid)
        if dur is not None:
            rem = dur - (scene.time - t0) + 0.45
            if rem > 0.05:
                scene.wait(rem)
        else:
            scene.wait(fb)
    def save_tl():
        if tl_path:
            with open(tl_path, "w") as f:
                json.dump({"timeline": timeline, "total": float(scene.time)}, f)
    return timeline, end_vo, save_tl

class ConvexVsNonconvex(Scene):
    def construct(self):
        timeline, end_vo, save_tl = setup_vo(self)
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_header("BOYD & VANDENBERGHE (SLIDE 1.12)", "Ranh giới thực sự: Lồi vs. Không lồi")
        self.play(FadeIn(hdr), run_time=0.6)

        b1 = card(7.6, 2.5, PINK).move_to([0, 2.1, 0])
        t1 = VGroup(
            fit(T("Quan niệm CŨ (SAI): Tuyến tính dễ, Phi tuyến khó", 24, PINK), 7.0),
            fit(T("Thực tế: nhiều bài toán phi tuyến lồi giải cực nhanh!", 22, WHITE), 7.0),
        ).arrange(DOWN, buff=0.2).move_to(b1)

        b2 = card(7.6, 2.9, MINT).move_to([0, -1.5, 0])
        t2 = VGroup(
            fit(T("Quan niệm ĐÚNG: Lồi (lõm lên) dễ, Không lồi khó", 24, MINT), 7.0),
            fit(T("Với bài toán LỒI: Mọi cực tiểu địa phương", 23, WHITE), 7.0),
            fit(T("đều là CỰC TIỂU TOÀN CỤC!", 25, SUN), 7.0),
        ).arrange(DOWN, buff=0.18).move_to(b2)

        self.play(FadeIn(b1), FadeIn(t1), run_time=1.0)
        self.play(FadeIn(b2), FadeIn(t2), run_time=1.0)
        end_vo("s1", t0, 10.0)

        self.play(FadeOut(hdr), FadeOut(b1), FadeOut(t1), FadeOut(b2), FadeOut(t2), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_header("KIẾN TRÚC BÀI TOÁN LỒI", "minimize f₀(x)  s.t.  fᵢ(x) ≤ 0,  aⱼᵀx = bⱼ")
        self.play(FadeIn(hdr2), run_time=0.6)

        b3 = card(7.6, 3.6, SKY).move_to([0, 0.2, 0])
        t3 = VGroup(
            fit(T("• Hàm mục tiêu f₀(x) lồi", 24, SKY), 7.0),
            fit(T("• Ràng buộc bất đẳng thức fᵢ(x) ≤ 0 với fᵢ lồi", 23, MINT), 7.0),
            fit(T("• Ràng buộc đẳng thức hⱼ(x) = aⱼᵀx − bⱼ phải là AFIN!", 23, SUN), 7.0),
            fit(T("⇒ Tập khả thi là Tập Lồi & Giải được hiệu quả (20–80 bước IPM)", 21, WHITE), 7.0),
        ).arrange(DOWN, buff=0.28).move_to(b3)
        self.play(FadeIn(b3), FadeIn(t3), run_time=1.0)
        end_vo("s2", t0, 9.5)
        save_tl()
