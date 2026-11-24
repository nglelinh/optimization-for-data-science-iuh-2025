from rl import *
# Bài 06-02-01: bước cố định; L-trơn, bổ đề giảm với t = 1/L, và thung lũng có số điều kiện lớn
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

# L-trơn: ‖∇f(x) − ∇f(y)‖ ≤ L‖x − y‖ với L = 10
gf = lambda p: A * p
_r = np.random.default_rng(0)
for _ in range(200):
    u_, v_ = _r.normal(size=2) * 3, _r.normal(size=2) * 3; assert np.linalg.norm(gf(u_) - gf(v_)) <= 10 * np.linalg.norm(u_ - v_) + 1e-12
# t = 1/L: f giảm ít nhất ‖∇f‖²/(2L) mỗi bước, và f_k − f* ≤ ‖x₀ − x*‖²/(2tk)
PT1, NT1 = R.setdefault(0.1, run(0.1))[:2]
DEC = [(f(PT1[k]) - f(PT1[k + 1]), gf(PT1[k]) @ gf(PT1[k]) / 20) for k in range(NT1)]
assert all(a >= b - 1e-15 for a, b in DEC) and NT1 == 66 and np.isclose(DEC[0][0], 1.305) and np.isclose(DEC[0][1], 0.9)
assert all(f(PT1[k]) <= (P0 @ P0) / (2 * 0.1 * k) for k in range(1, NT1 + 1))
# số điều kiện: κ = 10 so với κ = 100
def runA(Av, t, tol=1e-6):
    Av = np.array(Av); fA = lambda p: 0.5 * (Av * p * p).sum(); p = P0.copy(); f0 = fA(p); out = [1.0]
    while fA(p) >= tol * f0 and len(out) < 5000: p = p - t * Av * p; out.append(fA(p) / f0)
    return out
K10, K100 = runA([10, 1], 2 / 11), runA([100, 1], 2 / 101); K10b, K100b = runA([10, 1], 0.1), runA([100, 1], 0.01)
assert (len(K10) - 1, len(K100) - 1, len(K10b) - 1, len(K100b) - 1) == (35, 346, 66, 653)
assert abs(99 / 101 - 0.9802) < 1e-4
VI = LANG == "vi"

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
        self.say(L("Ví dụ của bài: f(x, y) = ½(10x² + y²), dốc theo x, thoải theo y. Cực tiểu ở gốc, chấm xanh lá.",
                   "The lesson's example: f(x, y) = ½(10x² + y²), steep in x, flat in y. The minimum is at the origin, the green dot."), hold=7.0)
        self.readout(["L = 10   (độ cong theo x)" if VI else "L = 10   (curvature along x)", "m = 1    (độ cong theo y)" if VI else "m = 1    (curvature along y)", ("điểm đầu (x, y) = " if VI else "start (x, y) = ") + vec(P0, 1) + "   f₀ = " + nf(f(P0), 3)], color=DIM)
        self.say(L("Độ cong lớn nhất L = 10, nhỏ nhất m = 1. Tỉ số κ = L/m = 10 gọi là số điều kiện, nó sẽ quyết định tốc độ.",
                   "Largest curvature L = 10, smallest m = 1. Their ratio κ = L/m = 10 is the condition number, and it will set the speed."), hold=7.5)
        # ---- key idea
        self.stage(2)
        self.readout(["x⁺ = x − t·∇f(x)", "x ← (1 − 10t)·x", "y ← (1 − t)·y"], color=SUN, size=26)
        self.say(L("Mỗi bước: đi ngược gradient một đoạn t. Với hàm này, mỗi tọa độ chỉ bị nhân với một hệ số cố định.",
                   "Each step moves against the gradient by t. For this function every coordinate is just multiplied by a fixed factor."), hold=7.5)
        rows = ["   t     1−10t    1−t"] + ["%5s  %7s  %6s" % (nf(t, 2), nf(1 - 10 * t, 2), nf(1 - t, 2)) for t in (0.02, 0.18, 0.21)]
        self.readout(rows, color=WHITE, size=25)
        self.say(L("Ổn định khi |1 − 10t| < 1, tức t < 2/L = 0,2. Với t = 0,21 hệ số theo x là −1,1: nó sẽ phình ra.",
                   "Stable only if |1 − 10t| < 1, i.e. t < 2/L = 0.2. At t = 0.21 the x-factor is −1.1: it will grow."), hold=8.0)
        self.readout([("L-trơn:  ‖∇f(x) − ∇f(y)‖ ≤ L‖x − y‖" if VI else "L-smooth:  ‖∇f(x) − ∇f(y)‖ ≤ L‖x − y‖", SUN), ("ở đây ∇f = (10x, y)  ⇒  L = 10" if VI else "here ∇f = (10x, y)  ⇒  L = 10", DIM)], color=WHITE, size=23)
        self.say(L("Tổng quát hơn: f là L-trơn nếu gradient không đổi nhanh hơn L lần khoảng cách. Với hàm bậc hai, L chính là trị riêng lớn nhất của Hessian, ở đây bằng 10.",
                   "More generally: f is L-smooth if its gradient changes at most L times as fast as the point moves. For a quadratic, L is the largest Hessian eigenvalue, here 10."), hold=10.5)
        self.readout(["f(y) ≤ f(x) + ∇f(x)ᵀ(y − x) + (L/2)‖y − x‖²", ("y = x − t∇f:  f(x⁺) ≤ f(x) − t(1 − Lt/2)‖∇f‖²", WHITE), ("t = 1/L:  f(x⁺) ≤ f(x) − ‖∇f(x)‖²/(2L)", MINT)], color=SUN, size=22)
        self.say(L("Hệ quả là bổ đề giảm: f nằm dưới một parabol. Thay bước GD vào, với t = 1/L ta được đảm bảo f giảm ít nhất ‖∇f‖²/(2L) mỗi bước, không cần biết gì thêm.",
                   "The consequence is the descent lemma: f lies below a parabola. Plug in the GD step, and with t = 1/L, f is guaranteed to drop by at least ‖∇f‖²/(2L) per step, nothing else needed."), hold=12.0)
        self.readout([("f lồi, t ≤ 1/L:" if VI else "f convex, t ≤ 1/L:", WHITE), ("f(xₖ) − f* ≤ ‖x₀ − x*‖² / (2tk)", MINT)], color=WHITE, size=25)
        self.say(L("Nếu f còn lồi, cộng dồn các bước giảm cho cận f(xₖ) − f* ≤ ‖x₀ − x*‖²/(2tk): sai số giảm ít nhất như 1/k.",
                   "If f is also convex, summing the decreases gives the bound f(xₖ) − f* ≤ ‖x₀ − x*‖²/(2tk): the error falls at least like 1/k."), hold=9.0)
        # ---- algorithm t = 0.18
        self.stage(3)
        pts = R[0.18][0]
        self.say(L("Chạy với t = 0,18 (an toàn). Theo dõi tọa độ và f sau từng bước.", "Run with t = 0.18 (safe). Watch the coordinates and f after every step."), wait=False)
        def ro(k):
            self.readout(["t = " + nf(0.18), "k = %d   (x, y) = %s" % (k, vec(pts[k], 3)), "f = %s" % nf(f(pts[k]), 4)], color=SUN); self.wait(0.55)
        p1 = trail(self, ax, pts, dot, SUN, rt=0.75, ks=range(1, 9), cb=ro)
        self.say(L("x đổi dấu mỗi bước (hệ số −0,8) còn y co lại 0,82 lần: đường đi zig-zag nhưng hội tụ.",
                   "x flips sign every step (factor −0.8) while y shrinks by 0.82: a zig-zag that still converges."), hold=7.0)
        p2 = trail(self, ax, [pts[8]] + pts[9:N18 + 1], dot, SUN, rt=0.12, width=3, rate=linear)
        self.remove(p1, p2); path = VGroup(p1, p2); self.add(path); self.bring_to_front(dot)
        self.readout(["t = " + nf(0.18), "k = %d   f = %s" % (N18, sci(f(pts[N18]))), "f/f₀ < 10⁻⁶  ✓"], color=MINT)
        self.say(L("Sau %d bước, f đã nhỏ hơn một phần triệu giá trị ban đầu." % N18, "After %d steps f is below one millionth of its starting value." % N18), hold=6.0)
        rows = [("t = 1/L = %s" % nf(0.1, 1), WHITE)] + [(("k = %d:  f giảm %s ≥ %s  ✓" if VI else "k = %d:  f drops %s ≥ %s  ✓") % (k, nf(DEC[k][0], 3), nf(DEC[k][1], 3)), MINT) for k in range(4)]
        self.readout(rows, size=22)
        self.say(L("Kiểm tra bổ đề giảm với t = 1/L = 0,1: bước đầu f giảm 1,305, nhiều hơn mức bảo đảm 0,9. Các bước sau cũng vậy.",
                   "Check the descent lemma with t = 1/L = 0.1: the first step lowers f by 1.305, more than the guaranteed 0.9. The same holds for every later step."), hold=9.5)
        self.readout([("t = 1/L: %d bước tới f/f₀ < 10⁻⁶" % NT1 if VI else "t = 1/L: %d steps to f/f₀ < 10⁻⁶" % NT1, MINT), ("cận 1/k: f(x₁₀) ≤ %s,  thực tế %s" % (nf((P0 @ P0) / 2, 2), sci(f(PT1[10]))) if VI else "1/k bound: f(x₁₀) ≤ %s,  actual %s" % (nf((P0 @ P0) / 2, 2), sci(f(PT1[10]))), DIM)], size=23)
        self.say(L("t = 1/L an toàn, cần %d bước. Cận 1/k rất dè dặt: ở bước 10 nó cho ≤ %s nhưng f thực tế đã nhỏ hơn nhiều, vì hàm này còn lồi mạnh." % (NT1, nf((P0 @ P0) / 2, 2)),
                   "t = 1/L is safe and needs %d steps. The 1/k bound is very cautious: at step 10 it allows %s, but f is already far smaller, because this function is also strongly convex." % (NT1, nf((P0 @ P0) / 2, 2))), hold=10.5)
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
                   "x leaves the frame after %d steps; by step %d f is 10⁴ times f₀. Divergence." % (kx, N21)), hold=7.0)
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
        self.say(L("Đối chiếu cuối: thung lũng hẹp hơn. Đổi 10x² thành 100x², tức κ = 100.", "A final contrast: a narrower valley. Change 10x² into 100x², so κ = 100."), hold=6.0)
        self.wipe()
        fx = plain_axes([0, 360], [0, 6.4], 7.4, 4.6, [0.25, 1.6, 0])
        yt = VGroup(*[Text(s_, font=MONO, font_size=17, color=DIM).next_to(fx.c2p(0, v + 6), LEFT, buff=0.1) for v, s_ in ((0, "1"), (-3, "10⁻³"), (-6, "10⁻⁶"))])
        xt = VGroup(*[Text(str(v), font=MONO, font_size=17, color=DIM).next_to(fx.c2p(v, 0), DOWN, buff=0.1) for v in (100, 200, 300)])
        cv = lambda Y, c: VMobject(color=c, stroke_width=4).set_points_as_corners([fx.c2p(k, max(np.log10(v), -6) + 6) for k, v in enumerate(Y)])
        self.play(Create(fx), FadeIn(yt), FadeIn(xt), run_time=0.5)
        c10, c100 = cv(K10, SUN), cv(K100, PINK)
        self.play(Create(c10), run_time=0.8); self.play(Create(c100), run_time=1.8)
        self.readout([("f/f₀ trên thang log, bước tốt nhất 2/(L+m)" if VI else "f/f₀ on a log scale, best step 2/(L+m)", WHITE), ("κ = 10:   hệ số 9/11 ≈ %s,  %d bước" % (nf(9 / 11, 3), len(K10) - 1) if VI else "κ = 10:   factor 9/11 ≈ %s,  %d steps" % (nf(9 / 11, 3), len(K10) - 1), SUN),
                      ("κ = 100:  hệ số 99/101 ≈ %s,  %d bước" % (nf(99 / 101, 3), len(K100) - 1) if VI else "κ = 100:  factor 99/101 ≈ %s,  %d steps" % (nf(99 / 101, 3), len(K100) - 1), PINK), ("với t = 1/L: %d và %d bước" % (len(K10b) - 1, len(K100b) - 1) if VI else "with t = 1/L: %d and %d steps" % (len(K10b) - 1, len(K100b) - 1), DIM)], size=22)
        self.say(L("Với κ = 100, ngay cả bước tốt nhất cũng chỉ co sai số 0,98 lần mỗi bước: cần %d bước thay vì %d. Số bước tăng gần tỉ lệ với κ." % (len(K100) - 1, len(K10) - 1),
                   "With κ = 100, even the best step only shrinks the error by 0.98 per step: %d steps instead of %d. The step count grows roughly in proportion to κ." % (len(K100) - 1, len(K10) - 1)), hold=11.0)
        self.say(L("Bước t bị khoá bởi hướng dốc nhất (t < 2/L), nên hướng thoải nhất đi rất chậm. Đó là lý do cần tiền điều kiện, momentum, hay Newton ở các chương sau.",
                   "The step t is capped by the steepest direction (t < 2/L), so the flattest direction moves very slowly. That is why later chapters bring preconditioning, momentum, or Newton."), hold=10.5)
        self.takeaway([L("t > 2/L: gradient descent phân kỳ.", "t > 2/L: gradient descent diverges."),
                       L("f L-trơn, t = 1/L: mỗi bước f giảm ít nhất ‖∇f‖²/(2L).", "f L-smooth, t = 1/L: each step lowers f by at least ‖∇f‖²/(2L)."),
                       L("t quá nhỏ: an toàn nhưng chậm (%d bước thay vì %d)." % (N02, NB), "t too small: safe but slow (%d steps instead of %d)." % (N02, NB)),
                       L("Tốc độ do κ = L/m quyết định: tốt nhất (κ−1)/(κ+1) mỗi bước; κ = 100 cần %d bước." % (len(K100) - 1), "Speed is set by κ = L/m: at best (κ−1)/(κ+1) per step; κ = 100 needs %d steps." % (len(K100) - 1))], tail=4.0)
