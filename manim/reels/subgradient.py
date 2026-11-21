from common_b import *

TX = {
    "title": {"vi": "Gradient dưới: nhiều đường đỡ\ntại điểm gãy", "en": "Subgradients: many supporting\nlines at a kink"},
    "fn": {"vi": "f(x) = max{ −2x − 1,  x/2,  2x − 3 }", "en": "f(x) = max{ −2x − 1,  x/2,  2x − 3 }"},
    "kink1": {"vi": "Điểm gãy x = −0,4: mọi độ dốc g ∈ [−2 ; 0,5]\nđều cho một đường nằm dưới f", "en": "Kink at x = −0.4: every slope g ∈ [−2, 0.5]\ngives a line that stays below f"},
    "smooth": {"vi": "Điểm trơn x = 1:\nchỉ còn một độ dốc, g = 0,5", "en": "Smooth point x = 1:\nonly one slope, g = 0.5"},
    "kink2": {"vi": "Điểm gãy x = 2: g ∈ [0,5 ; 2]", "en": "Kink at x = 2: g ∈ [0.5, 2]"},
    "out": {"vi": "Độ dốc ngoài đoạn →\nđường cắt qua đồ thị", "en": "A slope outside the interval\ncuts through the graph"},
}
SLS = [(-2.0, -1.0), (0.5, 0.0), (2.0, -3.0)]
fS = lambda x: max(a * x + b for a, b in SLS)
assert abs(fS(-0.4) - (-2 * -0.4 - 1)) < 1e-12 and abs(fS(-0.4) - 0.5 * -0.4) < 1e-12
assert abs(fS(2) - 0.5 * 2) < 1e-12 and abs(fS(2) - (2 * 2 - 3)) < 1e-12 and abs(fS(1) - 0.5) < 1e-12
xs = np.linspace(-3, 3.5, 2000)


def below(x0, g):
    return all(fS(y) >= fS(x0) + g * (y - x0) - 1e-9 for y in xs)


for g in np.linspace(-2, 0.5, 26):
    assert below(-0.4, g)
for g in (-2.2, 0.7, 1.0):
    assert not below(-0.4, g)
for g in np.linspace(0.5, 2, 16):
    assert below(2, g)
assert below(1, 0.5) and not below(1, 0.6) and not below(1, 0.3)


class Sub(Scene):
    def construct(self):
        self.add(line(TX["title"], 30, WHITE, 6.2))
        self.add(line(TX["fn"], 28, DIM, 5.0))
        ax = Axes(x_range=[-3, 3.5, 1], y_range=[-1.5, 6, 1], x_length=7.2, y_length=6.2,
                  axis_config={"color": "#2c3350", "stroke_width": 2}, tips=False).move_to([0, 1.3, 0])
        self.play(Create(ax), run_time=0.7)
        graph = VMobject(color=SKY, stroke_width=7).set_points_as_corners([ax.c2p(x, fS(x)) for x in np.linspace(-3, 3.5, 300)])
        self.play(Create(graph), run_time=1.2)

        def L(x0, g, col):
            return Line(ax.c2p(-3, fS(x0) + g * (-3 - x0)), ax.c2p(3.5, fS(x0) + g * (3.5 - x0)), color=col, stroke_width=5)
        k = line(TX["kink1"], 30, SUN, -3.0)
        pt = Dot(ax.c2p(-0.4, fS(-0.4)), radius=0.14, color=SUN)
        g0 = ValueTracker(-2.0)
        ln = always_redraw(lambda: L(-0.4, g0.get_value(), MINT))
        self.play(FadeIn(pt), FadeIn(k), run_time=0.6)
        self.add(ln)
        self.play(g0.animate.set_value(0.5), run_time=3.2, rate_func=smooth)
        self.wait(0.5)
        o = line(TX["out"], 28, PINK, -4.5)
        self.play(g0.animate.set_value(1.1), run_time=1.0)
        ln.clear_updaters(); self.remove(ln)
        bad = L(-0.4, 1.1, PINK); self.add(bad)
        self.play(FadeIn(o), run_time=0.5); self.wait(1.2)
        self.play(FadeOut(bad), FadeOut(o), FadeOut(k), run_time=0.5)
        # điểm trơn
        s = line(TX["smooth"], 30, SUN, -3.0)
        self.play(pt.animate.move_to(ax.c2p(1, fS(1))), FadeIn(s), run_time=1.0)
        sm = L(1, 0.5, MINT); self.play(Create(sm), run_time=0.8); self.wait(1.4)
        self.play(FadeOut(sm), FadeOut(s), run_time=0.4)
        k2 = line(TX["kink2"], 30, SUN, -3.0)
        self.play(pt.animate.move_to(ax.c2p(2, fS(2))), FadeIn(k2), run_time=1.0)
        g1 = ValueTracker(0.5)
        ln2 = always_redraw(lambda: L(2, g1.get_value(), MINT)); self.add(ln2)
        self.play(g1.animate.set_value(2.0), run_time=2.4, rate_func=smooth)
        self.wait(3.0)
