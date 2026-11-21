from common_b import *
import math

TX = {
    "title": {"vi": "Đường trung tâm:\nt tăng, nghiệm rào cản đi tới đỉnh", "en": "Central path: as t grows,\nthe barrier solution reaches the vertex"},
    "fn": {"vi": "min t·cᵀx − Σ log(bᵢ − aᵢᵀx)", "en": "min t·cᵀx − Σ log(bᵢ − aᵢᵀx)"},
    "obj": {"vi": "hướng tối ưu: tăng x₁ + 0,7x₂", "en": "objective: increase x₁ + 0.7x₂"},
    "end": {"vi": "Rào cản đẩy nghiệm ra khỏi biên;\nt lớn thì nghiệm áp sát đỉnh tối ưu", "en": "The barrier keeps x*(t) off the boundary;\nlarge t lets it hug the optimal vertex"},
}
A = np.array([[-1, 0], [0, -1], [1, 1], [1, 0], [0, 1]], float); B = np.array([-0.2, -0.2, 4, 3, 2.6]); C = np.array([-1, -0.7])


def phi(x, t):
    s = B - A @ x
    return np.inf if (s <= 0).any() else t * C @ x - np.log(s).sum()


def center(t, x):
    for _ in range(80):
        s = B - A @ x; g = t * C + A.T @ (1 / s); H = A.T @ np.diag(1 / s ** 2) @ A
        d = -np.linalg.solve(H, g); dec = -g @ d
        if dec / 2 < 1e-12: break
        a = 1.0
        while phi(x + a * d, t) > phi(x, t) - 0.25 * a * dec: a *= 0.5
        x = x + a * d
    return x


x = np.array([1.5, 1.0]); path = []
TS = [10 ** (k / 20) for k in range(-10, 61)]
for t in TS:
    x = center(t, x); path.append(x.copy())
assert np.linalg.norm(path[-1] - np.array([3, 1])) < 5e-3 and abs(C @ path[-1] + 3.7) < 5 / 1000 + 1e-9
assert all((C @ p + 3.7) <= 5 / t + 1e-9 for p, t in zip(path, TS))


class Path(Scene):
    def construct(self):
        self.add(line(TX["title"], 30, WHITE, 6.2))
        self.add(line(TX["fn"], 26, DIM, 4.85))
        ax = Axes(x_range=[0, 3.5, 1], y_range=[0, 3, 1], x_length=7.4, y_length=6.3,
                  axis_config={"color": "#2c3350", "stroke_width": 2}, tips=False).move_to([0, 0.9, 0])
        P = lambda p: ax.c2p(p[0], p[1])
        poly = Polygon(*[P(p) for p in [(0.2, 0.2), (3, 0.2), (3, 1), (1.4, 2.6), (0.2, 2.6)]], color=SKY, stroke_width=6, fill_color="#1d2540", fill_opacity=1)
        self.play(FadeIn(poly), run_time=0.9)
        opt = Dot(P((3, 1)), radius=0.13, color=MINT); self.add(opt)
        arrow = Arrow(P((0.35, 2.3)), P((1.0, 2.3 + 0.65 * 0.7 / 1)), buff=0, color=ORANGE, stroke_width=6, max_tip_length_to_length_ratio=0.3)
        ol = line(TX["obj"], 24, ORANGE, -3.15); self.play(Create(arrow), FadeIn(ol), run_time=0.7)
        cur = Dot(P(path[0]), radius=0.15, color=PINK); self.add(cur)
        tl = T("t = %s" % nf(TS[0], 1), 34, SUN).move_to([0, -4.2, 0]); self.add(tl)
        trail = VMobject(color=SUN, stroke_width=6)
        trail.set_points_as_corners([P(p) for p in path[:2]])
        self.add(trail)
        marks = {0: "t = 1", 20: "t = 10", 40: "t = 100", 60: "t = 1000"}
        idx = list(range(1, len(path)))
        for k in idx:
            trail.set_points_as_corners([P(p) for p in path[:k + 1]])
            cur.move_to(P(path[k]))
            tl.become(T("t = %s" % (nf(TS[k], 1) if TS[k] < 100 else "%d" % round(TS[k])), 34, SUN).move_to([0, -4.2, 0]))
            self.wait(0.07)
        gp = T(("khoảng cách ≤ m/t = 5/1000" if LANG == "vi" else "gap ≤ m/t = 5/1000"), 28, MINT).move_to([0, -5.0, 0]); self.play(FadeIn(gp), run_time=0.5)
        e = line(TX["end"], 26, WHITE, -6.1); self.play(FadeIn(e), run_time=0.6); self.wait(3.0)
