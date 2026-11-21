from rl import *
A = np.array([10.0, 1.0]); P0 = np.array([0.3, 3.0]); f = lambda p: 0.5 * (A * p * p).sum()
def run(t, n=5000, tol=1e-6):
    p = P0.copy(); pts = [p.copy()]; f0 = f(p)
    for k in range(n):
        if f(p) < tol * f0: return pts, k, True
        p = p - t * A * p; pts.append(p.copy())
        if f(p) > 1e4 * f0: return pts, k + 1, False
    return pts, n, False
TB = 2 / 11
R = {t: run(t) for t in (0.18, 0.21, 0.02, TB)}
assert R[0.18][2] and not R[0.21][2] and R[0.02][2] and R[TB][2]
N18, N21, N02, NB = R[0.18][1], R[0.21][1], R[0.02][1], R[TB][1]
assert NB <= N18 < N02 and N02 > 8 * N18
rate = lambda t: max(abs(1 - 10 * t), abs(1 - t))
assert abs(rate(TB) - 9 / 11) < 1e-12

class GD(Reel):
    def construct(self):
        self.title(L("Gradient descent: kích thước bước\nquyết định tất cả", "Gradient descent: the step size\ndecides everything"))
        self.stage(1)
        ax = Axes(x_range=[-1.3, 1.3, 0.5], y_range=[-3.6, 3.6, 1], x_length=4.4, y_length=6.2, axis_config={"color": DIM, "stroke_width": 2}, tips=False).move_to([0, 1.05, 0])
        lv = [0.05, 0.3, 1, 2, 3.5, 5.4]
        cs = VGroup(*[ax.plot_parametric_curve(lambda s, c=c: np.array([np.sqrt(2 * c / 10) * np.cos(s), np.sqrt(2 * c) * np.sin(s)]), t_range=[0, TAU], color="#2c3350", stroke_width=3) for c in lv])
        self.play(Create(ax), run_time=0.6); self.play(Create(cs), run_time=1.2)
        star = Dot(ax.c2p(0, 0), radius=0.1, color=MINT); self.add(star)
        dot = Dot(ax.c2p(*P0), radius=0.13, color=SUN); self.play(FadeIn(dot, scale=1.5), run_time=0.4)
        self.say(L("f(x, y) = ½(10x² + y²): dốc theo x, thoải theo y. Cực tiểu ở gốc (chấm xanh).",
                   "f(x, y) = ½(10x² + y²): steep in x, flat in y. The minimum is at the origin (green dot)."))
        self.readout(["L = 10   (curvature along x)", "m = 1    (curvature along y)", "start (x, y) = " + vec(P0, 1) + "   f₀ = " + nf(f(P0), 3)], color=DIM)
        self.say(L("Độ cong lớn nhất L = 10, nhỏ nhất m = 1. Tỉ số κ = L/m = 10 sẽ quyết định tốc độ.",
                   "Largest curvature L = 10, smallest m = 1. Their ratio κ = L/m = 10 will set the speed."))
        # ---- key idea
        self.stage(2)
        self.readout(["x⁺ = x − t·∇f(x)", "x ← (1 − 10t)·x", "y ← (1 − t)·y"], color=SUN, size=26)
        self.say(L("Mỗi bước: đi ngược gradient một đoạn t. Ở đây mỗi tọa độ chỉ bị nhân với một hệ số cố định.",
                   "Each step moves against the gradient by t. Here every coordinate is just multiplied by a fixed factor."))
        rows = ["   t     1−10t    1−t"] + ["%5s  %7s  %6s" % (nf(t, 2), nf(1 - 10 * t, 2), nf(1 - t, 2)) for t in (0.02, 0.18, 0.21)]
        self.readout(rows, color=WHITE, size=25)
        self.say(L("Ổn định khi |1 − 10t| < 1, tức t < 2/L = 0,2. Với t = 0,21 hệ số theo x là −1,1: nó sẽ phình ra.",
                   "Stable only if |1 − 10t| < 1, i.e. t < 2/L = 0.2. At t = 0.21 the x-factor is −1.1: it will grow."), hold=4.2)
        # ---- algorithm t = 0.18
        self.stage(3)
        pts = R[0.18][0]
        self.say(L("Chạy với t = 0,18 (an toàn). Theo dõi tọa độ và f sau từng bước.", "Run with t = 0.18 (safe). Watch the coordinates and f after every step."), wait=False)
        def ro(k):
            self.readout(["t = " + nf(0.18), "k = %d   (x, y) = %s" % (k, vec(pts[k], 3)), "f = %s" % nf(f(pts[k]), 4)], color=SUN); self.wait(0.55)
        p1 = trail(self, ax, pts, dot, SUN, rt=0.75, ks=range(1, 9), cb=ro)
        self.say(L("x đổi dấu mỗi bước (hệ số −0,8) còn y co lại 0,82 lần: đường đi zig-zag nhưng hội tụ.",
                   "x flips sign every step (factor −0.8) while y shrinks by 0.82: a zig-zag that still converges."))
        p2 = trail(self, ax, [pts[8]] + pts[9:N18 + 1], dot, SUN, rt=0.12, width=3, rate=linear)
        self.remove(p1, p2); path = VGroup(p1, p2); self.add(path); self.bring_to_front(dot)
        self.readout(["t = " + nf(0.18), "k = %d   f = %s" % (N18, sci(f(pts[N18]))), "f/f₀ < 10⁻⁶  ✓"], color=MINT)
        self.say(L("Sau %d bước, f đã nhỏ hơn một phần triệu giá trị ban đầu." % N18, "After %d steps f is below one millionth of its starting value." % N18))
        # ---- contrast
        self.stage(4); self.play(FadeOut(path), dot.animate.move_to(ax.c2p(*P0)), run_time=0.5)
        pts = R[0.21][0]
        ok = lambda p: abs(p[0]) <= 1.3 and abs(p[1]) <= 3.6
        kx = max(k for k in range(N21 + 1) if all(ok(pts[j]) for j in range(k + 1)))
        rd = lambda k: self.readout(["t = " + nf(0.21), "k = %d   x = %s" % (k, nf(pts[k][0], 3)), "f = %s" % nf(f(pts[k]), 3)], color=PINK)
        path = trail(self, ax, pts[:kx + 1], dot, PINK, rt=lambda k: 0.6 if k <= 4 else 0.3, cb=rd)
        self.play(dot.animate.set_color(PINK).scale(1.3), run_time=0.3)
        self.readout(["t = " + nf(0.21), tr(L("x tăng ×%s mỗi bước" % nf(1.1, 1), "x grows ×1.1 each step")),
                      "k = %d: f > 10⁴·f₀  ✗" % N21], color=PINK)
        self.say(L("x rời khỏi khung sau %d bước; tới bước %d thì f đã gấp 10⁴ lần f₀. Phân kỳ." % (kx, N21),
                   "x leaves the frame after %d steps; by step %d f is 10⁴ times f₀. Divergence." % (kx, N21)))
        self.play(FadeOut(path), dot.animate.move_to(ax.c2p(*P0)).set_color(SUN).scale(1 / 1.3), run_time=0.5)
        pts = R[0.02][0]
        self.say(L("Còn t = 0,02 thì an toàn nhưng rất chậm: y chỉ co 0,98 lần mỗi bước.", "And t = 0.02 is safe but painfully slow: y only shrinks by 0.98 per step."), wait=False)
        path = trail(self, ax, pts, dot, SKY, rt=0.1, ks=range(5, N02 + 1, 5), rate=linear)
        self.wait(0.6)
        rows = ["   t       steps to f/f₀ < 10⁻⁶" if LANG == "en" else "   t       số bước tới f/f₀ < 10⁻⁶",
                ("%6s   %s" % (nf(0.02), N02), SKY), ("%6s   %s" % (nf(0.18), N18), SUN), ("%6s   %s" % (nf(TB, 3), NB), MINT), ("%6s   ∞ (%s)" % (nf(0.21), "phân kỳ" if LANG == "vi" else "diverges"), PINK)]
        self.readout(rows, color=WHITE, size=24)
        self.say(L("t = 0,02 cần %d bước. Bước tốt nhất t = 2/(L+m) ≈ 0,182 chỉ cần %d." % (N02, NB),
                   "t = 0.02 needs %d steps. The best fixed step t = 2/(L+m) ≈ 0.182 needs only %d." % (N02, NB)), hold=4.0)
        self.takeaway([L("t > 2/L: gradient descent phân kỳ.", "t > 2/L: gradient descent diverges."),
                       L("t quá nhỏ: an toàn nhưng chậm (%d bước thay vì %d)." % (N02, NB), "t too small: safe but slow (%d steps instead of %d)." % (N02, NB)),
                       L("Tốc độ do κ = L/m quyết định: tốt nhất (κ−1)/(κ+1) = 9/11 ≈ 0,82 mỗi bước.", "Speed is set by κ = L/m: at best the error shrinks by (κ−1)/(κ+1) = 9/11 ≈ 0.82 per step.")])
