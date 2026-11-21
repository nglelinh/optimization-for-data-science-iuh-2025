from rl import *
f = lambda x: np.exp(x) - 2 * x; d1 = lambda x: np.exp(x) - 2; d2 = lambda x: np.exp(x); XS = np.log(2.0)
xs = [2.0]
for _ in range(5): xs.append(xs[-1] - d1(xs[-1]) / d2(xs[-1]))
err = [abs(x - XS) for x in xs]
assert err[5] < 1e-8 and all(err[i + 1] <= 0.5 * err[i] ** 2 + 1e-15 for i in range(1, 5))
h = lambda x: np.sqrt(1 + x * x); h1 = lambda x: x / np.sqrt(1 + x * x); h2 = lambda x: (1 + x * x) ** -1.5
def pure(x0, n):
    out = [x0]
    for _ in range(n): x = out[-1]; out.append(x - h1(x) / h2(x))
    return out
BAD = pure(1.2, 3); GOOD = pure(0.5, 3)
assert all(abs(BAD[i] + BAD[i - 1] ** 3) < 1e-9 for i in range(1, 4)) and abs(BAD[3]) > 100 and abs(GOOD[3]) < 1e-6
def damped(x0, n):
    out = [x0]; ts = []
    for _ in range(n):
        x = out[-1]; d = -h1(x) / h2(x); t = 1.0
        while h(x + t * d) > h(x) + 0.25 * t * h1(x) * d: t *= 0.5
        out.append(x + t * d); ts.append(t)
    return out, ts
DMP, DTS = damped(1.2, 6)
assert abs(DMP[-1]) < 1e-8 and DTS[0] < 1 and DTS[-1] == 1.0

class Newton(Reel):
    def construct(self):
        self.title(L("Phương pháp Newton: nhảy tới\nđáy của parabol xấp xỉ", "Newton's method: jump to\nthe bottom of the local parabola"))
        self.stage(1)
        ax = plain_axes([-1.2, 2.6], [0, 4.6], 7.6, 6.0, [0, 1.1, 0], ticks=True)
        G = ax.plot(f, x_range=[-1.2, 2.25], color=SKY, stroke_width=6)
        self.play(Create(ax), Create(G), run_time=1.0)
        st = Dot(ax.c2p(XS, f(XS)), radius=0.09, color=MINT); self.add(st)
        self.say(L("Cực tiểu hoá f(x) = eˣ − 2x. Đáp số đúng: x* = ln 2 ≈ 0,693 (chấm xanh).", "Minimize f(x) = eˣ − 2x. The true answer: x* = ln 2 ≈ 0.693 (green dot)."))
        self.readout(["f′(x) = eˣ − 2,   f″(x) = eˣ > 0"], color=DIM, size=25)
        self.say(L("Ta biết cả đạo hàm bậc một và bậc hai. Xuất phát từ x₀ = 2.", "We know both the first and second derivatives. Start at x₀ = 2."))
        # key idea
        self.stage(2)
        dot = Dot(ax.c2p(xs[0], f(xs[0])), radius=0.13, color=SUN); self.play(FadeIn(dot), run_time=0.3)
        def par(x0, col=SUN):
            q = lambda x: f(x0) + d1(x0) * (x - x0) + 0.5 * d2(x0) * (x - x0) ** 2
            lo, hi = x0 - 3, x0 + 3
            xsg = [x for x in np.linspace(lo, hi, 400) if -1.2 <= x <= 2.6 and 0 <= q(x) <= 4.6]
            return VMobject(color=col, stroke_width=4).set_points_smoothly([ax.c2p(x, q(x)) for x in xsg]), q
        P0, q0 = par(xs[0])
        self.readout(["m(x) = f(xₖ) + f′(xₖ)(x−xₖ) + ½f″(xₖ)(x−xₖ)²", "xₖ₊₁ = xₖ − f′(xₖ)/f″(xₖ)"], color=SUN, size=22)
        self.play(Create(P0), run_time=1.0)
        self.say(L("Tại xₖ, thay f bằng parabol m có cùng giá trị, độ dốc và độ cong. Nhảy thẳng tới đáy của parabol đó.",
                   "At xₖ, replace f by the parabola m with the same value, slope and curvature. Jump straight to its bottom."), hold=5.0)
        vtx = Dot(ax.c2p(xs[1], q0(xs[1])), radius=0.1, color=SUN)
        self.play(FadeIn(vtx), run_time=0.3); self.play(dot.animate.move_to(ax.c2p(xs[1], f(xs[1]))), run_time=0.8)
        self.play(FadeOut(vtx), FadeOut(P0), run_time=0.4)
        # algorithm
        self.stage(3)
        self.say(L("Lặp lại. Theo dõi sai số |xₖ − ln 2|.", "Repeat. Watch the error |xₖ − ln 2|."), wait=False)
        rows = ["k      xₖ              |xₖ − x*|"]
        rows.append("%d   %s   %s" % (0, nf(xs[0], 10), nf(err[0], 3)))
        rows.append("%d   %s   %s" % (1, nf(xs[1], 10), nf(err[1], 3)))
        self.readout(rows, color=WHITE, size=21, y=-3.0); self.wait(1.2)
        for k in range(1, 5):
            Pk, qk = par(xs[k]); self.play(Create(Pk), run_time=0.6)
            self.play(dot.animate.move_to(ax.c2p(xs[k + 1], f(xs[k + 1]))), run_time=0.6); self.play(FadeOut(Pk), run_time=0.3)
            rows.append(("%d   %s   %s" % (k + 1, nf(xs[k + 1], 10), sci(err[k + 1]) if err[k + 1] > 0 else "0"), MINT if k >= 2 else WHITE))
            self.readout(rows, color=WHITE, size=21, y=-3.0); self.wait(0.9)
        self.say(L("Gần nghiệm, số chữ số đúng gần như gấp đôi mỗi bước: sai số mới ≤ ½·(sai số cũ)². Đó là hội tụ bậc hai.",
                   "Near the answer the number of correct digits roughly doubles each step: new error ≤ ½·(old error)². That is quadratic convergence."), hold=5.5)
        # contrast
        self.stage(4); self.clear_ro()
        self.play(FadeOut(G), FadeOut(dot), FadeOut(st), FadeOut(ax), run_time=0.5)
        ax2 = plain_axes([-6, 6], [0, 6.5], 7.8, 6.0, [0, 1.1, 0], ticks=True)
        H = ax2.plot(h, x_range=[-6, 6], color=PINK, stroke_width=6)
        self.play(Create(ax2), Create(H), run_time=0.8)
        self.say(L("Hàm khác: h(x) = √(1 + x²), lồi, cực tiểu tại 0. Bước Newton thuần ở đây là x ↦ −x³.",
                   "Another function: h(x) = √(1 + x²), convex, minimum at 0. Here the pure Newton step is x ↦ −x³."))
        d = Dot(ax2.c2p(BAD[0], h(BAD[0])), radius=0.13, color=PINK); self.play(FadeIn(d), run_time=0.3)
        self.readout(["x₀ = %s" % nf(BAD[0], 1)], color=PINK)
        for k in range(1, 4):
            x = BAD[k]
            if abs(x) <= 6: self.play(d.animate.move_to(ax2.c2p(x, h(x))), run_time=0.7)
            else: self.play(d.animate.move_to(ax2.c2p(np.sign(x) * 6.3, 6.4)).set_opacity(0.3), run_time=0.7)
            self.readout(["x₀ = %s" % nf(BAD[0], 1)] + ["x%s = %s" % ("₁₂₃"[j - 1], nf(BAD[j], 3)) for j in range(1, k + 1)], color=PINK)
            self.wait(0.6)
        self.say(L("Từ x₀ = 1,2 các bước Newton thuần phóng ra xa: 1,2 → −1,728 → 5,16 → −137. Phân kỳ.",
                   "From x₀ = 1.2 pure Newton blows up: 1.2 → −1.728 → 5.16 → −137. It diverges."))
        self.play(FadeOut(d), run_time=0.2)
        d = Dot(ax2.c2p(DMP[0], h(DMP[0])), radius=0.13, color=MINT); self.play(FadeIn(d), run_time=0.3)
        self.say(L("Sửa: Newton tắt dần. Giữ hướng Newton nhưng chọn bước t bằng backtracking cho tới khi h giảm đủ.",
                   "The fix: damped Newton. Keep the Newton direction but backtrack on t until h decreases enough."), wait=False)
        for k in range(1, len(DMP)):
            self.play(d.animate.move_to(ax2.c2p(DMP[k], h(DMP[k]))), run_time=0.6)
            self.readout(["k = %d   t = %s   x = %s" % (k, nf(DTS[k - 1], 3), nf(DMP[k], 6) if abs(DMP[k]) > 1e-6 else sci(abs(DMP[k])))], color=MINT); self.wait(0.6)
        self.say(L("Bước đầu bị cắt còn t = %s; khi đã gần 0 thì t = 1 và hội tụ bậc hai quay lại." % nf(DTS[0], 3),
                   "The first step is cut to t = %s; once close to 0, t = 1 and quadratic convergence is back." % nf(DTS[0], 3)), hold=4.5)
        self.takeaway([L("Newton dùng cả độ cong: nhảy tới đáy parabol xấp xỉ.", "Newton uses curvature: jump to the bottom of the local parabola."),
                       L("Gần nghiệm: hội tụ bậc hai, số chữ số đúng gấp đôi mỗi bước.", "Near the answer: quadratic convergence, correct digits double each step."),
                       L("Xa nghiệm có thể phân kỳ: dùng Newton tắt dần (backtracking).", "Far away it can diverge: use damped Newton (backtracking).")])
