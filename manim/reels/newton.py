from common_b import *

TX = {
    "title": {"vi": "Newton: nhảy tới đáy của\nparabol xấp xỉ", "en": "Newton: jump to the bottom\nof the local parabola"},
    "fn": {"vi": "f(x) = eˣ − 2x", "en": "f(x) = eˣ − 2x"},
    "model": {"vi": "Parabola xấp xỉ bậc hai tại xₖ", "en": "Quadratic model at xₖ"},
    "step": {"vi": "xₖ₊₁ = xₖ − f′(xₖ) / f″(xₖ)", "en": "xₖ₊₁ = xₖ − f′(xₖ) / f″(xₖ)"},
    "err": {"vi": "Sai số |xₖ − x*|", "en": "Error |xₖ − x*|"},
    "dbl": {"vi": "Số chữ số đúng gần như nhân đôi mỗi bước", "en": "Correct digits roughly double each step"},
}
f = lambda x: np.exp(x) - 2 * x
d1 = lambda x: np.exp(x) - 2
d2 = lambda x: np.exp(x)
XS = np.log(2.0)
xs = [2.0]
for _ in range(5):
    x = xs[-1]; xs.append(x - d1(x) / d2(x))
err = [abs(x - XS) for x in xs]
assert all(err[i + 1] < err[i] for i in range(5)) and err[5] < 1e-8 and err[1] > 0.5 and err[2] < 0.15
assert all(err[i + 1] <= 0.5 * err[i] ** 2 + 1e-15 for i in range(1, 5)), [(err[i + 1], err[i] ** 2) for i in range(5)]
sci = lambda v: ("%.0e" % v).replace("e-0", "e-").replace(".", ",") if LANG == "vi" else ("%.0e" % v).replace("e-0", "e-")
num = lambda v: (("%.2f" % v).replace(".", ",") if LANG == "vi" else "%.2f" % v)


class Newton(Scene):
    def construct(self):
        self.add(line(TX["title"], 30, WHITE, 6.2))
        self.add(line(TX["fn"], 30, DIM, 5.0))
        ax = Axes(x_range=[-0.4, 2.1, 0.5], y_range=[0, 4, 1], x_length=7.2, y_length=4.6,
                  axis_config={"color": "#2c3350", "stroke_width": 2}, tips=False).move_to([0, 2.15, 0])
        self.play(Create(ax), run_time=0.7)
        g = ax.plot(f, x_range=[-0.4, 2.15], color=SKY, stroke_width=7); self.play(Create(g), run_time=1.0)
        mn = Dot(ax.c2p(XS, f(XS)), radius=0.11, color=MINT)
        self.add(mn)
        t1 = line(TX["model"], 28, SUN, -0.9); t2 = line(TX["step"], 28, WHITE, -1.7)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.6)
        hdr = line(TX["err"], 28, DIM, -2.8); self.play(FadeIn(hdr), run_time=0.4)
        cur = Dot(ax.c2p(xs[0], f(xs[0])), radius=0.13, color=PINK); self.play(FadeIn(cur), run_time=0.4)
        rows = VGroup(); y = -3.6
        for k in range(4):
            x = xs[k]
            q = lambda s, x=x: f(x) + d1(x) * (s - x) + 0.5 * d2(x) * (s - x) ** 2
            ss = np.linspace(-0.4, 2.1, 2000); ok = [u for u in ss if q(u) <= 3.95]
            lo, hi = min(ok), max(ok)
            par = ax.plot(lambda s, q=q: q(s), x_range=[lo, hi], color=SUN, stroke_width=5)
            self.play(Create(par), run_time=0.8)
            nx = xs[k + 1]
            tgt = Dot(ax.c2p(nx, q(nx)), radius=0.1, color=SUN)
            self.play(FadeIn(tgt), run_time=0.3)
            self.play(cur.animate.move_to(ax.c2p(nx, f(nx))), run_time=0.7)
            r = T("k = %d :   %s" % (k + 1, sci(err[k + 1]) if err[k + 1] < 0.01 else num(err[k + 1])), 30, WHITE).move_to([0, y, 0])
            self.play(FadeIn(r), FadeOut(par), FadeOut(tgt), run_time=0.5); rows.add(r); y -= 0.62
        d = line(TX["dbl"], 28, MINT, -6.2)
        self.play(FadeIn(d), run_time=0.6); self.wait(3.2)
