from common_b import *

TX = {
    "title": {"vi": "Frank-Wolfe: đi về phía đỉnh\nmà không cần chiếu", "en": "Frank-Wolfe: step toward a vertex,\nno projection needed"},
    "fn": {"vi": "min ½‖x − p‖² trên tam giác", "en": "min ½‖x − p‖² over the triangle"},
    "lmo": {"vi": "Chọn đỉnh làm cực tiểu mô hình tuyến tính", "en": "Pick the vertex minimising the linear model"},
    "mix": {"vi": "xₖ₊₁ = (1 − γ)xₖ + γ·s", "en": "xₖ₊₁ = (1 − γ)xₖ + γ·s"},
    "end": {"vi": "Mọi điểm lặp là tổ hợp lồi của các đỉnh,\nnên luôn nằm trong tập", "en": "Every iterate is a convex combination of vertices,\nso it always stays inside the set"},
}
V = np.array([[-1.6, -1.0], [1.7, -0.9], [0.1, 1.8]]); PP = np.array([2.1, 1.0])


def run(n):
    x = V[0].copy(); out = [(x.copy(), None)]
    for k in range(n):
        g = x - PP; s = int(np.argmin(V @ g)); gm = 2 / (k + 2)
        out[-1] = (out[-1][0], s); x = (1 - gm) * x + gm * V[s]; out.append((x.copy(), None))
    return out


R = run(40)
tri = lambda p: all(((V[(i + 1) % 3][0] - V[i][0]) * (p[1] - V[i][1]) - (V[(i + 1) % 3][1] - V[i][1]) * (p[0] - V[i][0])) >= -1e-9 for i in range(3))
assert all(tri(r[0]) for r in R)
sv = [r[1] for r in R[:6]]
assert len(set(sv[:6])) >= 2, sv


class FW(Scene):
    def construct(self):
        self.add(line(TX["title"], 30, WHITE, 6.2))
        self.add(line(TX["fn"], 26, DIM, 4.85))
        ax = Axes(x_range=[-2.8, 3.2, 1], y_range=[-2.2, 2.6, 1], x_length=7.8, y_length=6.24, axis_config={"stroke_width": 0}, tips=False).move_to([0, 1.2, 0])
        P = lambda p: ax.c2p(p[0], p[1])
        tri_m = Polygon(*[P(v) for v in V], color=SKY, stroke_width=6, fill_color="#1d2540", fill_opacity=1)
        self.play(FadeIn(tri_m), run_time=0.8)
        vd = [Dot(P(v), radius=0.12, color=SKY) for v in V]; self.add(*vd)
        pd = Dot(P(PP), radius=0.15, color=ORANGE); pl = T("p", 30, ORANGE).next_to(pd, UR, buff=0.1); self.play(FadeIn(pd), FadeIn(pl), run_time=0.5)
        for r in (0.6, 1.8, 3.2):
            self.add(Circle(radius=r * (P((1, 0))[0] - P((0, 0))[0]), stroke_width=2, color="#2f3a5e").move_to(P(PP)))
        cur = Dot(P(R[0][0]), radius=0.15, color=PINK); self.add(cur)
        t1 = line(TX["lmo"], 26, MINT, -2.6); t2 = line(TX["mix"], 28, WHITE, -3.4)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.5)
        trail = VMobject(color=SUN, stroke_width=5); trail.set_points_as_corners([P(R[0][0]), P(R[0][0])]); self.add(trail)
        hl = None
        for k in range(8):
            s = R[k][1]
            if hl is not None: self.remove(hl)
            hl = DashedLine(P(R[k][0]), P(V[s]), color=MINT, stroke_width=4); self.add(hl)
            self.play(vd[s].animate.scale(1.9).set_color(MINT), run_time=0.35)
            trail.set_points_as_corners([P(r[0]) for r in R[:k + 2]])
            self.play(cur.animate.move_to(P(R[k + 1][0])), run_time=0.7)
            self.play(vd[s].animate.scale(1 / 1.9).set_color(SKY), run_time=0.2)
        self.remove(hl)
        for k in range(8, 40):
            trail.set_points_as_corners([P(r[0]) for r in R[:k + 2]]); cur.move_to(P(R[k + 1][0])); self.wait(0.07)
        e = line(TX["end"], 26, SUN, -5.0); self.play(FadeIn(e), run_time=0.6); self.wait(3.2)
