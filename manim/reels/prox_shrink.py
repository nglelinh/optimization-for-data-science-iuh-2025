from common_b import *

TX = {
    "title": {"vi": "Co ngưỡng mềm:\nprox của λ|x|", "en": "Soft-thresholding:\nthe prox of λ|x|"},
    "fn": {"vi": "prox(y) = argmin ½(x − y)² + λ|x|,  λ = 1", "en": "prox(y) = argmin ½(x − y)² + λ|x|,  λ = 1"},
    "zero": {"vi": "|y| ≤ λ  →  đúng bằng 0", "en": "|y| ≤ λ  →  exactly 0"},
    "shr": {"vi": "|y| > λ  →  co về 0 một đoạn λ", "en": "|y| > λ  →  shrink toward 0 by λ"},
    "end": {"vi": "ISTA = bước gradient + co ngưỡng mềm\nnên nghiệm lasso có thành phần bằng 0", "en": "ISTA = gradient step + soft-thresholding,\nso lasso solutions have exact zeros"},
    "in": {"vi": "đầu vào y", "en": "input y"},
    "out": {"vi": "đầu ra prox(y)", "en": "output prox(y)"},
}
LAM = 1.0
soft = lambda y: np.sign(y) * max(abs(y) - LAM, 0.0)
# prox đúng là argmin: kiểm bằng lưới
for y in (-2.4, -0.7, 0.3, 1.0, 1.8):
    xs = np.linspace(-4, 4, 80001); v = 0.5 * (xs - y) ** 2 + LAM * np.abs(xs)
    assert abs(xs[np.argmin(v)] - soft(y)) < 2e-4, y


class Prox(Scene):
    def construct(self):
        self.add(line(TX["title"], 32, WHITE, 6.2))
        self.add(line(TX["fn"], 24, DIM, 4.85, max_w=8.0))
        ax = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=7.0, y_length=7.0,
                  axis_config={"color": "#2c3350", "stroke_width": 2}, tips=False).move_to([0, 0.4, 0])
        self.play(Create(ax), run_time=0.7)
        band = Rectangle(width=ax.c2p(1, 0)[0] - ax.c2p(-1, 0)[0], height=7.0, stroke_width=0, fill_color=PINK, fill_opacity=0.12).move_to(ax.c2p(0, 0))
        diag = DashedLine(ax.c2p(-3, -3), ax.c2p(3, 3), color=DIM, stroke_width=3)
        curve = VGroup(Line(ax.c2p(-3, -2), ax.c2p(-1, 0)), Line(ax.c2p(-1, 0), ax.c2p(1, 0)), Line(ax.c2p(1, 0), ax.c2p(3, 2))).set_color(SKY).set_stroke(width=7)
        self.play(Create(diag), run_time=0.6); self.play(Create(curve), FadeIn(band), run_time=1.2)
        tracker = ValueTracker(-2.6)
        d_in = always_redraw(lambda: Dot(ax.c2p(tracker.get_value(), tracker.get_value()), radius=0.12, color=SUN))
        d_out = always_redraw(lambda: Dot(ax.c2p(tracker.get_value(), soft(tracker.get_value())), radius=0.14, color=MINT))
        drop = always_redraw(lambda: DashedLine(ax.c2p(tracker.get_value(), tracker.get_value()), ax.c2p(tracker.get_value(), soft(tracker.get_value())), color=SUN, stroke_width=3))
        self.add(drop, d_in, d_out)
        t1 = line(TX["in"], 24, SUN, -3.55); t2 = line(TX["out"], 24, MINT, -4.15)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.4)
        c1 = line(TX["shr"], 28, WHITE, -5.2); self.play(FadeIn(c1), run_time=0.4)
        self.play(tracker.animate.set_value(-1.0), run_time=2.0, rate_func=linear)
        c2 = line(TX["zero"], 28, PINK, -5.2); self.play(FadeOut(c1), FadeIn(c2), run_time=0.4)
        self.play(tracker.animate.set_value(1.0), run_time=3.0, rate_func=linear)
        self.play(FadeOut(c2), FadeIn(c1), run_time=0.4)
        self.play(tracker.animate.set_value(2.6), run_time=2.0, rate_func=linear)
        e = line(TX["end"], 27, SUN, -6.2); self.play(FadeOut(c1), FadeIn(e), run_time=0.6); self.wait(3.0)
