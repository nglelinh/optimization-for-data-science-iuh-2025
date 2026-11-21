from common_b import *

TX = {
    "title": {"vi": "Cùng một hàm, ba kích thước bước", "en": "One function, three step sizes"},
    "fn": {"vi": "f(x) = (10x₁² + x₂²) / 2,  L = 10", "en": "f(x) = (10x₁² + x₂²) / 2,  L = 10"},
    "big": {"vi": "t = 0,21  (quá lớn)", "en": "t = 0.21  (too big)"},
    "small": {"vi": "t = 0,02  (quá nhỏ)", "en": "t = 0.02  (too small)"},
    "good": {"vi": "t = 0,18  (vừa phải)", "en": "t = 0.18  (about right)"},
    "div": {"vi": "Dao động ngày càng rộng: phân kỳ", "en": "The swings keep growing: divergence"},
    "slow": {"vi": "Đúng hướng nhưng rất chậm", "en": "Right direction, painfully slow"},
    "ok": {"vi": "Hội tụ sau %d bước", "en": "Converges in %d steps"},
    "rule": {"vi": "Ngưỡng an toàn: t < 2/L = 0,2", "en": "Safe zone: t < 2/L = 0.2"},
}
A = np.array([10.0, 1.0])
f = lambda p: 0.5 * (A * p * p).sum()
P0 = np.array([0.3, 3.0])
for t in (0.21, 0.02, 0.18):
    assert (abs(1 - t * 10) > 1) == (t == 0.21)           # chỉ t=0.21 > 2/L làm x₁ phân kỳ
    assert abs(1 - t * 10) < 1 or t == 0.21


def run(t, n=2000, tol=1e-6):
    p = P0.copy(); pts = [p.copy()]; f0 = f(p)
    for k in range(n):
        if f(p) < tol * f0:
            return pts, k, True
        p = p - t * A * p; pts.append(p.copy())
        if f(p) > 1e4 * f0:
            return pts, k + 1, False
    return pts, n, False


R = {t: run(t) for t in (0.21, 0.02, 0.18)}
assert not R[0.21][2] and R[0.18][2] and R[0.02][1] > 8 * R[0.18][1]
N_GOOD = R[0.18][1]
assert 20 <= N_GOOD <= 90, N_GOOD
inside = lambda p: abs(p[0]) <= 1.15 and abs(p[1]) <= 3.5


class GD(Scene):
    def construct(self):
        self.add(line(TX["title"], 34, WHITE, 6.3))
        self.add(line(TX["fn"], 28, DIM, 5.5))
        ax = Axes(x_range=[-1.2, 1.2, 1], y_range=[-3.6, 3.6, 1], x_length=6.6, y_length=7.6,
                  axis_config={"color": "#2c3350", "stroke_width": 2}, tips=False).move_to([0, 0.6, 0])
        self.play(Create(ax), run_time=0.7)
        f0 = f(P0)
        for c in (1, 0.5, 0.25, 0.1, 0.03, 0.008):
            lev = c * f0
            e = ParametricFunction(lambda s, lev=lev: ax.c2p(np.sqrt(2 * lev / 10) * np.cos(s), np.sqrt(2 * lev) * np.sin(s)),
                                   t_range=[0, 2 * np.pi], color="#46507a", stroke_width=2)
            self.add(e)
        st = Dot(ax.c2p(*P0), radius=0.11, color=PINK); self.play(FadeIn(st), run_time=0.4)
        cols = {0.21: PINK, 0.02: SKY, 0.18: MINT}
        lab = None; note = None
        for t, key, nk in ((0.21, "big", "div"), (0.02, "small", "slow"), (0.18, "good", "ok")):
            pts = [p for p in R[t][0][:200] if inside(p)]
            if t == 0.02:
                pts = pts[:90]
            path = VMobject(color=cols[t], stroke_width=4).set_points_as_corners([ax.c2p(*p) for p in pts])
            new_lab = line(TX[key], 32, cols[t], -4.2)
            if lab is None:
                self.play(FadeIn(new_lab), run_time=0.4)
            else:
                self.play(FadeOut(lab), FadeOut(note), FadeIn(new_lab), run_time=0.5)
            lab = new_lab
            self.play(Create(path), run_time=3.4 if t != 0.02 else 3.0, rate_func=linear)
            dots = VGroup(*[Dot(ax.c2p(*p), radius=0.05, color=cols[t]) for p in pts[:60]])
            self.add(dots)
            msg = tr(TX[nk]) % N_GOOD if nk == "ok" else tr(TX[nk])
            note = line({"vi": msg, "en": msg}, 30, WHITE, -5.0)
            self.play(FadeIn(note), run_time=0.5)
            self.wait(0.9)
            self.play(FadeOut(path), FadeOut(dots), run_time=0.4)
        r = line(TX["rule"], 30, SUN, -5.9)
        self.play(FadeIn(r), run_time=0.6)
        self.wait(3.0)
