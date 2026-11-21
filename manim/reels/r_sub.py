from rl import *
SLS = [(-2.0, -1.0), (0.5, 0.0), (2.0, -3.0)]
f = lambda x: max(a * x + b for a, b in SLS)
def g(x):
    v = [a * x + b for a, b in SLS]; return SLS[int(np.argmax(v))][0]
XS, FS = -0.4, -0.2
assert abs(f(XS) - FS) < 1e-12 and abs(f(2) - 1) < 1e-12
def sgm(x0, step, n):
    x = x0; xs = [x]; fb = [f(x)]
    for k in range(n):
        x = x - step(k) * g(x); xs.append(x); fb.append(min(fb[-1], f(x)))
    return xs, fb
DX, DB = sgm(2.9, lambda k: 1 / (k + 1), 400)
FX, FB = sgm(2.9, lambda k: 0.5, 400)
inc = [k for k in range(1, 25) if f(DX[k]) > f(DX[k - 1]) + 1e-12]
assert inc, "need a non-monotone step"
K1 = inc[0]
assert DB[-1] - FS < 2e-3 and FB[-1] - FS > 0.02
assert min(FB[100:]) == FB[100]   # fixed step: stuck
GAPF = FB[-1] - FS

class Sub(Reel):
    def construct(self):
        self.title(L("Gradient dưới: cả một chiếc quạt\nđường đỡ tại điểm gãy", "Subgradients: a whole fan of\nsupporting lines at a kink"))
        self.stage(1)
        ax = plain_axes([-3, 3.6], [-1.6, 5.6], 7.8, 6.2, [0, 1.1, 0])
        self.play(Create(ax), run_time=0.5)
        cols = [SKY, PINK, ORANGE]
        lines = VGroup(*[ax.plot(lambda x, a=a, b=b: a * x + b, x_range=[max(-3, (-1.6 - b) / a if a else -3), min(3.6, (5.6 - b) / a if a > 0 else 3.6)] if a > 0 else [max(-3, (5.6 - b) / a), min(3.6, (-1.6 - b) / a)], color=c, stroke_width=3, stroke_opacity=0.6) for (a, b), c in zip(SLS, cols)])
        self.play(Create(lines), run_time=1.2)
        self.say(L("Ba đường thẳng: −2x − 1,  0,5x,  2x − 3.", "Three lines: −2x − 1,  0.5x,  2x − 3."), hold=2.4)
        fg = ax.plot(f, x_range=[-3, 3.6, 0.01], color=SUN, stroke_width=7, use_smoothing=False)
        fg = VMobject(color=SUN, stroke_width=7).set_points_as_corners([ax.c2p(x, f(x)) for x in (-3, -0.4, 2, 3.3)])
        self.play(Create(fg), lines.animate.set_stroke(opacity=0.25), run_time=1.2)
        self.say(L("f(x) = max của ba đường: lồi, nhưng gãy tại x = −0,4 và x = 2. Ở đó không có đạo hàm.",
                   "f(x) = the max of the three: convex, but with kinks at x = −0.4 and x = 2. No derivative there."))
        # key idea
        self.stage(2)
        def sup(x0, s, col=MINT, w=4):
            return Line(ax.c2p(x0 - 1.4, f(x0) - 1.4 * s), ax.c2p(x0 + 1.4, f(x0) + 1.4 * s), color=col, stroke_width=w)
        p = Dot(ax.c2p(1, f(1)), radius=0.11, color=WHITE); tl = sup(1, 0.5)
        self.play(FadeIn(p), Create(tl), run_time=0.6)
        self.readout(["x = 1:   ∂f(1) = {" + nf(0.5, 1) + "}"], color=MINT, size=25)
        self.say(L("Ở điểm trơn x = 1 chỉ có một đường đỡ: tiếp tuyến, độ dốc 0,5.", "At the smooth point x = 1 there is one supporting line: the tangent, slope 0.5."))
        self.play(FadeOut(tl), p.animate.move_to(ax.c2p(2, 1)), run_time=0.5)
        s = ValueTracker(0.5); fan = always_redraw(lambda: sup(2, s.get_value())); self.add(fan)
        self.readout(["x = 2:   ∂f(2) = [" + nf(0.5, 1) + ", 2]"], color=MINT, size=25)
        self.say(L("Tại điểm gãy x = 2, mọi độ dốc từ 0,5 đến 2 đều cho một đường nằm dưới đồ thị.",
                   "At the kink x = 2, every slope from 0.5 to 2 gives a line that stays below the graph."), wait=False)
        self.play(s.animate.set_value(2), run_time=1.2); self.play(s.animate.set_value(0.5), run_time=1.2)
        ghost = VGroup(*[sup(2, v, MINT, 2).set_stroke(opacity=0.35) for v in np.linspace(0.5, 2, 7)]); self.add(ghost); self.remove(fan)
        self.wait(0.5)
        self.say(L("Tập các độ dốc đó gọi là vi phân dưới ∂f(2): một đoạn, không phải một số.", "That set of slopes is the subdifferential ∂f(2): an interval, not a number."))
        self.play(FadeOut(ghost), p.animate.move_to(ax.c2p(XS, FS)), run_time=0.5)
        s2 = ValueTracker(-2); fan2 = always_redraw(lambda: sup(XS, s2.get_value(), SKY)); self.add(fan2)
        self.readout(["x = −0,4:   ∂f = [−2, 0,5]  ∋ 0" if LANG == "vi" else "x = −0.4:   ∂f = [−2, 0.5]  ∋ 0"], color=SKY, size=25)
        self.play(s2.animate.set_value(0.5), run_time=1.8); self.play(s2.animate.set_value(0), run_time=0.9)
        self.say(L("Tại x = −0,4 chiếc quạt chứa độ dốc 0: đường nằm ngang đỡ cả đồ thị. 0 ∈ ∂f(x) nghĩa là x tối ưu.",
                   "At x = −0.4 the fan contains slope 0: a flat line supports the whole graph. 0 ∈ ∂f(x) means x is optimal."), hold=5.0)
        self.remove(fan2); self.play(FadeOut(p), FadeOut(VGroup(sup(XS, 0, SKY))), run_time=0.3)
        # algorithm
        self.stage(3)
        self.readout(["x⁺ = x − tₖ·g,   g ∈ ∂f(x)", "tₖ = 1/(k+1)"], color=SUN, size=25)
        self.say(L("Phương pháp gradient dưới: đi ngược một gradient dưới bất kỳ, với bước giảm dần tₖ = 1/(k+1). Bắt đầu x₀ = 2,9.",
                   "The subgradient method: step against any subgradient, with shrinking steps tₖ = 1/(k+1). Start at x₀ = 2.9."))
        dot = Dot(ax.c2p(DX[0], f(DX[0])), radius=0.13, color=SUN); self.play(FadeIn(dot), run_time=0.3)
        best = Dot(ax.c2p(DX[0], f(DX[0])), radius=0.09, color=MINT)
        for k in range(1, K1 + 4):
            self.play(dot.animate.move_to(ax.c2p(DX[k], f(DX[k]))), run_time=0.4 if k <= K1 + 1 else 0.3)
            up = f(DX[k]) > f(DX[k - 1]) + 1e-12
            self.readout(["k = %2d   x = %s   g = %s" % (k, nf(DX[k], 3), nf(g(DX[k - 1]), 1)),
                          ("f(x) = %s   %s" % (nf(f(DX[k]), 3), "↑" if up else "↓"), PINK if up else SUN), ("f_best = %s" % nf(DB[k], 3), MINT)], color=WHITE)
            if k == K1:
                self.say(L("Bước %d: f TĂNG. Gradient dưới không nhất thiết là hướng giảm, nên ta luôn giữ f_best." % K1,
                           "Step %d: f goes UP. A subgradient step need not be a descent step, so we keep track of f_best." % K1), hold=4.5)
        for k in (40, 100, 400):
            self.play(dot.animate.move_to(ax.c2p(DX[k], f(DX[k]))), run_time=0.6)
            self.readout(["k = %d   x = %s" % (k, nf(DX[k], 4)), ("f_best − f* = %s" % sci(DB[k] - FS), MINT)], color=WHITE)
            self.wait(0.6)
        self.say(L("Bước giảm dần (nhưng tổng vô hạn) đưa f_best về f* = −0,2, chậm nhưng chắc chắn.", "Shrinking steps (with an infinite sum) drive f_best to f* = −0.2: slowly, but surely."))
        # contrast
        self.stage(4)
        self.play(dot.animate.move_to(ax.c2p(FX[0], f(FX[0]))).set_color(PINK), run_time=0.5)
        self.say(L("Đối chiếu: bước cố định t = 0,5, cùng điểm xuất phát.", "Contrast: a fixed step t = 0.5 from the same start."), wait=False)
        for k in range(1, 9):
            self.play(dot.animate.move_to(ax.c2p(FX[k], f(FX[k]))), run_time=0.35)
            self.readout(["t = %s   k = %2d   x = %s" % (nf(0.5, 1), k, nf(FX[k], 3)), ("f_best − f* = %s" % nf(FB[k] - FS, 3), PINK)], color=WHITE)
        self.say(L("Gần đáy, các bước 0,25 và 1 cứ nảy qua lại quanh −0,4. Sau 400 bước f_best − f* vẫn là %s." % nf(GAPF, 3),
                   "Near the bottom, steps of 0.25 and 1 keep bouncing around −0.4. After 400 steps f_best − f* is still %s." % nf(GAPF, 3)), hold=5.0)
        self.takeaway([L("Tại điểm gãy, ∂f(x) là cả một tập độ dốc (một chiếc quạt).", "At a kink, ∂f(x) is a whole set of slopes (a fan)."),
                       L("Điều kiện tối ưu: 0 ∈ ∂f(x*).", "Optimality condition: 0 ∈ ∂f(x*)."),
                       L("Bước gradient dưới có thể làm f tăng: giữ f_best và cho bước giảm dần.", "A subgradient step can increase f: keep f_best and shrink the step.")])
