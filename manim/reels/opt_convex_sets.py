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

class ConvexSetsHulls(Scene):
    def construct(self):
        timeline, end_vo, save_tl = setup_vo(self)
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_header("CHƯƠNG 2 · TẬP LỒI", "Định nghĩa hình học: Đoạn thẳng nằm trọn bên trong")
        self.play(FadeIn(hdr), run_time=0.6)

        c_shape = Circle(radius=1.7, color=MINT, fill_color=MINT, fill_opacity=0.18, stroke_width=4).move_to([0, 1.8, 0])
        p1 = Dot([-0.9, 2.2, 0], color=SUN, radius=0.11)
        p2 = Dot([0.9, 1.3, 0], color=SUN, radius=0.11)
        seg = Line(p1.get_center(), p2.get_center(), color=SUN, stroke_width=4)

        b1 = card(7.6, 2.7, SKY).move_to([0, -2.0, 0])
        t1 = VGroup(
            fit(T("∀ x₁, x₂ ∈ C, ∀ θ ∈ [0, 1]:", 25, SKY), 7.0),
            fit(T("θx₁ + (1 − θ)x₂ ∈ C", 28, SUN), 7.0),
            fit(T("Mọi đoạn thẳng nối 2 điểm thuộc C đều nằm trong C.", 22, WHITE), 7.0),
        ).arrange(DOWN, buff=0.2).move_to(b1)

        self.play(Create(c_shape), FadeIn(p1), FadeIn(p2), Create(seg), run_time=1.2)
        self.play(FadeIn(b1), FadeIn(t1), run_time=0.9)
        end_vo("s1", t0, 10.0)

        self.play(FadeOut(hdr), FadeOut(c_shape), FadeOut(p1), FadeOut(p2), FadeOut(seg), FadeOut(b1), FadeOut(t1), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_header("TỔ HỢP LỒI & BAO LỒI", "Mọi tập S đều có một Bao Lồi conv(S) nhỏ nhất")
        self.play(FadeIn(hdr2), run_time=0.6)

        b2 = card(7.6, 3.8, MINT).move_to([0, 0.2, 0])
        t2 = VGroup(
            fit(T("• Tổ hợp lồi: ∑ θᵢxᵢ  với θᵢ ≥ 0, ∑ θᵢ = 1", 23, SKY), 7.0),
            fit(T("• Bao lồi conv(S): giao của mọi tập lồi chứa S", 23, MINT), 7.0),
            fit(T("  (Hình ảnh: sợi dây thun căng quanh các đinh S)", 22, SUN), 7.0),
            fit(T("• Ví dụ chuẩn: Đa diện, Hình cầu chuẩn, Đơn hình (Simplex)", 21, WHITE), 7.0),
        ).arrange(DOWN, buff=0.28).move_to(b2)
        self.play(FadeIn(b2), FadeIn(t2), run_time=1.0)
        end_vo("s2", t0, 9.5)
        save_tl()
