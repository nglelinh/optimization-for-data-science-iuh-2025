from rl import *
# Bài 14-01-01: bước Newton từ xấp xỉ bậc hai; 1D, 2D (ví dụ của bài) và trường hợp không lồi
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

# 2D: ví dụ của bài, f = (10x₁² + x₂²)/2 + 5 log(1 + e^(−x₁−x₂))
sg = lambda z: 1 / (1 + np.exp(-z))
F2 = lambda p: (10 * p[0] ** 2 + p[1] ** 2) / 2 + 5 * np.log1p(np.exp(-p[0] - p[1]))
def G2(p): s = sg(-p[0] - p[1]); return np.array([10 * p[0] - 5 * s, p[1] - 5 * s])
def H2(p): s = sg(-p[0] - p[1]); c = 5 * s * (1 - s); return np.array([[10 + c, c], [c, 1 + c]])
X2S = np.zeros(2)
for _ in range(50): X2S = X2S - np.linalg.solve(H2(X2S), G2(X2S))
F2S = F2(X2S); assert np.allclose(G2(X2S), 0, atol=1e-12) and np.allclose(X2S, [0.11247, 1.12467], atol=1e-5)
LL2 = 12.5
for p in np.random.default_rng(0).uniform(-3, 3, (200, 2)): assert np.linalg.eigvalsh(H2(p)).max() <= LL2 + 1e-12 and np.linalg.eigvalsh(H2(p)).min() > 0
S2 = np.array([1.0, 3.0])
def run2(kind):
    p = S2.copy(); pts = [p.copy()]
    while F2(p) - F2S > 1e-10 and len(pts) < 2000:
        p = p - (np.linalg.solve(H2(p), G2(p)) if kind == "nw" else G2(p) / LL2); pts.append(p.copy())
    return pts
NW2, GD2 = run2("nw"), run2("gd"); KN2, KG2 = len(NW2) - 1, len(GD2) - 1
assert KN2 == 4 and KG2 == 80
g1 = -G2(S2); dn1 = -np.linalg.solve(H2(S2), G2(S2)); toS = X2S - S2
cosang = lambda a, b_: a @ b_ / np.linalg.norm(a) / np.linalg.norm(b_)
ANG_N, ANG_G = [np.degrees(np.arccos(cosang(v_, toS))) for v_ in (dn1, g1)]
assert ANG_N < 6 and 45 < ANG_G < 50      # hướng Newton lệch ~5° khỏi hướng tới nghiệm, −∇f lệch ~48°
# không lồi: q(x) = x⁴/4 − x²/2, cực đại địa phương tại 0, cực tiểu tại ±1
q = lambda x: x ** 4 / 4 - x ** 2 / 2; q1 = lambda x: x ** 3 - x; q2 = lambda x: 3 * x * x - 1
QN = [0.4]
for _ in range(4): QN.append(QN[-1] - q1(QN[-1]) / q2(QN[-1]))
assert q2(0.4) < 0 and q1(0.4) < 0 and QN[1] < 0 and abs(QN[4]) < 1e-4 and all(q(QN[k + 1]) > q(QN[k]) for k in range(3))
assert np.isclose(QN[1], 0.4 - 0.336 / 0.52) and abs(QN[1] + 0.2462) < 1e-4
QG = [0.4]
for _ in range(30): QG.append(QG[-1] - 0.5 * q1(QG[-1]))
assert abs(QG[-1] - 1) < 1e-4 and all(q(QG[k + 1]) < q(QG[k]) for k in range(5))
VI = LANG == "vi"

class Newton(Reel):
    def construct(self):
        self.title(L("Phương pháp Newton: nhảy tới\nđáy của parabol xấp xỉ", "Newton's method: jump to\nthe bottom of the local parabola"))
        # ---- stage 1
        self.stage(1)
        ax = plain_axes([-1.2, 2.6], [0, 4.6], 7.6, 6.0, [0, 1.1, 0], ticks=True)
        G = ax.plot(f, x_range=[-1.2, 2.25], color=SKY, stroke_width=6)
        self.play(Create(ax), Create(G), run_time=1.0)
        st = Dot(ax.c2p(XS, f(XS)), radius=0.09, color=MINT); self.add(st)
        self.say(L("Cực tiểu hoá f(x) = eˣ − 2x. Đáp số đúng: x* = ln 2 ≈ 0,693, là chấm xanh lá.", "Minimize f(x) = eˣ − 2x. The true answer: x* = ln 2 ≈ 0.693, the green dot."), hold=5.6)
        self.readout(["f′(x) = eˣ − 2,   f″(x) = eˣ > 0"], color=DIM, size=25)
        self.say(L("Ta biết cả đạo hàm bậc một và bậc hai, và f″ luôn dương. Xuất phát từ x₀ = 2.", "We know both the first and second derivatives, and f″ is always positive. Start at x₀ = 2."), hold=6.3)
        # ---- stage 2
        self.stage(2)
        dot = Dot(ax.c2p(xs[0], f(xs[0])), radius=0.13, color=SUN); self.play(FadeIn(dot), run_time=0.3)
        def par(x0, col=SUN):
            qq = lambda x: f(x0) + d1(x0) * (x - x0) + 0.5 * d2(x0) * (x - x0) ** 2
            lo, hi = x0 - 3, x0 + 3
            xsg = [x for x in np.linspace(lo, hi, 400) if -1.2 <= x <= 2.6 and 0 <= qq(x) <= 4.6]
            return VMobject(color=col, stroke_width=4).set_points_smoothly([ax.c2p(x, qq(x)) for x in xsg]), qq
        P0, q0 = par(xs[0])
        self.readout(["m(x) = f(xₖ) + f′(xₖ)(x−xₖ) + ½f″(xₖ)(x−xₖ)²", "xₖ₊₁ = xₖ − f′(xₖ)/f″(xₖ)"], color=SUN, size=22)
        self.play(Create(P0), run_time=1.0)
        self.say(L("Tại xₖ, thay f bằng parabol m có cùng giá trị, cùng độ dốc và cùng độ cong. Rồi nhảy thẳng tới đáy của parabol đó.",
                   "At xₖ, replace f by the parabola m with the same value, slope and curvature. Then jump straight to its bottom."), hold=7.5)
        vtx = Dot(ax.c2p(xs[1], q0(xs[1])), radius=0.1, color=SUN)
        self.play(FadeIn(vtx), run_time=0.3); self.play(dot.animate.move_to(ax.c2p(xs[1], f(xs[1]))), run_time=0.8)
        self.play(FadeOut(vtx), FadeOut(P0), run_time=0.4)
        self.readout(["∇m(y) = ∇f(x) + ∇²f(x)(y − x) = 0", ("⇒  y = x − [∇²f(x)]⁻¹∇f(x)", SUN), ("GD: thay ∇²f bằng I/t  ⇒  y = x − t∇f(x)" if VI else "GD: replace ∇²f by I/t  ⇒  y = x − t∇f(x)", SKY)], color=WHITE, size=23)
        self.say(L("Nhiều chiều cũng vậy, như bài 14-01-01: cho gradient của mô hình bậc hai bằng 0 là ra bước Newton, y = x − [∇²f]⁻¹∇f.",
                   "Same in many dimensions, as in lesson 14-01-01: set the gradient of the quadratic model to 0 and out comes the Newton step, y = x − [∇²f]⁻¹∇f."), hold=9.0)
        self.say(L("Gradient descent là cùng công thức, nhưng thay Hessian bằng I/t: nó coi mọi hướng đều cong như nhau.",
                   "Gradient descent is the same recipe with the Hessian replaced by I/t: it pretends every direction curves the same."), hold=7.5)
        # ---- stage 3
        self.stage(3)
        self.say(L("Lặp lại trên eˣ − 2x. Theo dõi sai số |xₖ − ln 2|.", "Repeat on eˣ − 2x. Watch the error |xₖ − ln 2|."), wait=False)
        rows = ["k      xₖ              |xₖ − x*|"]
        rows.append("%d   %s   %s" % (0, nf(xs[0], 10), nf(err[0], 3)))
        rows.append("%d   %s   %s" % (1, nf(xs[1], 10), nf(err[1], 3)))
        self.readout(rows, color=WHITE, size=21, y=-3.0); self.wait(1.5)
        for k in range(1, 5):
            Pk, qk = par(xs[k]); self.play(Create(Pk), run_time=0.6)
            self.play(dot.animate.move_to(ax.c2p(xs[k + 1], f(xs[k + 1]))), run_time=0.6); self.play(FadeOut(Pk), run_time=0.3)
            rows.append(("%d   %s   %s" % (k + 1, nf(xs[k + 1], 10), sci(err[k + 1]) if err[k + 1] > 0 else "0"), MINT if k >= 2 else WHITE))
            self.readout(rows, color=WHITE, size=21, y=-3.0); self.wait(1.1)
        self.say(L("Gần nghiệm, số chữ số đúng gần như gấp đôi mỗi bước: sai số mới ≤ ½·(sai số cũ)². Đó là hội tụ bậc hai.",
                   "Near the answer the number of correct digits roughly doubles each step: new error ≤ ½·(old error)². That is quadratic convergence."), hold=7.2)
        self.wipe()
        a2 = plain_axes([-0.7, 1.3], [0.2, 3.2], 4.0, 6.0, [0, 1.15, 0])
        cs = contours(a2, lambda x, y: F2((x, y)), [F2S + dl for dl in (0.05, 0.3, 1.0, 2.0, 3.5, 5.5)], (-0.7, 1.3, 0.2, 3.2), N=70)
        self.play(Create(cs), run_time=1.2)
        self.add(Dot(a2.c2p(*X2S), radius=0.09, color=MINT))
        self.readout([("f = (10x₁² + x₂²)/2 + 5 log(1 + e^(−x₁−x₂))", WHITE), ("x₀ = %s,   x* ≈ %s" % (vec(S2, 1), vec(X2S, 3)), DIM)], size=22)
        self.say(L("Giờ là ví dụ hai chiều của bài: f = (10x₁² + x₂²)/2 + 5 log(1 + e^(−x₁−x₂)). Thung lũng dẹt, dốc theo x₁ gấp mười lần theo x₂.",
                   "Now the lesson's two-dimensional example: f = (10x₁² + x₂²)/2 + 5 log(1 + e^(−x₁−x₂)). A flat valley, ten times steeper in x₁ than in x₂."), hold=8.7)
        dg = Dot(a2.c2p(*S2), radius=0.11, color=SKY); dn = Dot(a2.c2p(*S2), radius=0.12, color=SUN); self.add(dg, dn)
        self.say(L("Xanh dương: GD bước cố định 1/L, L = 12,5. Vàng: Newton thuần.", "Blue: GD with fixed step 1/L, L = 12.5. Yellow: pure Newton."), wait=False)
        def r2(k): self.readout([("Newton  k = %d   f − f* = %s" % (min(k, KN2), sci(max(F2(NW2[min(k, KN2)]) - F2S, 1e-16))), SUN), ("GD      k = %d   f − f* = %s" % (k, sci(max(F2(GD2[k]) - F2S, 1e-16))), SKY)], size=22)
        for k in range(1, 13):
            an = [dg.animate.move_to(a2.c2p(*GD2[k]))]; segs = [Line(a2.c2p(*GD2[k - 1]), a2.c2p(*GD2[k]), color=SKY, stroke_width=3)]
            if k <= KN2: an.append(dn.animate.move_to(a2.c2p(*NW2[k]))); segs.append(Line(a2.c2p(*NW2[k - 1]), a2.c2p(*NW2[k]), color=SUN, stroke_width=5))
            self.play(*[Create(s_) for s_ in segs], *an, run_time=0.7 if k <= KN2 else 0.35); r2(k); self.wait(0.5 if k <= KN2 else 0.15)
        tail = VMobject(color=SKY, stroke_width=3).set_points_as_corners([a2.c2p(*p) for p in GD2[12:]])
        self.play(Create(tail), dg.animate.move_to(a2.c2p(*GD2[-1])), run_time=2.0); r2(KG2)
        self.say(L("Newton xong sau %d bước: hướng đầu tiên chỉ lệch khoảng %d° so với hướng tới nghiệm. −∇f lệch tới %d°, nên GD zig-zag theo x₁ rồi bò chậm theo x₂: %d bước." % (KN2, round(ANG_N), round(ANG_G), KG2),
                   "Newton is done after %d steps: its first direction is only about %d° off the line to the answer. −∇f is %d° off, so GD zig-zags in x₁ and then crawls along x₂: %d steps." % (KN2, round(ANG_N), round(ANG_G), KG2)), hold=9.2)
        self.say(L("Lý do: Hessian ở đây có trị riêng từ khoảng 1,8 tới 11. Newton chia cho đúng độ cong của từng hướng; GD chỉ có một bước t cho mọi hướng.",
                   "The reason: the Hessian here has eigenvalues from about 1.8 to 11. Newton divides by the right curvature in each direction; GD has a single step t for all of them."), hold=10.0)
        # ---- stage 4
        self.stage(4); self.wipe()
        ax2 = plain_axes([-6, 6], [0, 6.5], 7.8, 6.0, [0, 1.1, 0], ticks=True)
        H = ax2.plot(h, x_range=[-6, 6], color=PINK, stroke_width=6)
        self.play(Create(ax2), Create(H), run_time=0.8)
        self.say(L("Đối chiếu một: h(x) = √(1 + x²), lồi, cực tiểu tại 0. Bước Newton thuần ở đây là x ↦ −x³.",
                   "Contrast one: h(x) = √(1 + x²), convex, minimum at 0. Here the pure Newton step is x ↦ −x³."), hold=6.3)
        d = Dot(ax2.c2p(BAD[0], h(BAD[0])), radius=0.13, color=PINK); self.play(FadeIn(d), run_time=0.3)
        self.readout(["x₀ = %s" % nf(BAD[0], 1)], color=PINK)
        for k in range(1, 4):
            x = BAD[k]
            if abs(x) <= 6: self.play(d.animate.move_to(ax2.c2p(x, h(x))), run_time=0.7)
            else: self.play(d.animate.move_to(ax2.c2p(np.sign(x) * 6.3, 6.4)).set_opacity(0.3), run_time=0.7)
            self.readout(["x₀ = %s" % nf(BAD[0], 1)] + ["x%s = %s" % ("₁₂₃"[j - 1], nf(BAD[j], 3)) for j in range(1, k + 1)], color=PINK)
            self.wait(0.6)
        self.say(L("Từ x₀ = 1,2 các bước Newton thuần phóng ra xa: 1,2 → −1,728 → 5,16 → −137. Phân kỳ, dù hàm lồi.",
                   "From x₀ = 1.2 pure Newton blows up: 1.2 → −1.728 → 5.16 → −137. It diverges, even though h is convex."), hold=6.9)
        self.play(FadeOut(d), run_time=0.2)
        d = Dot(ax2.c2p(DMP[0], h(DMP[0])), radius=0.13, color=MINT); self.play(FadeIn(d), run_time=0.3)
        self.say(L("Sửa: Newton tắt dần. Giữ hướng Newton nhưng chọn bước t bằng backtracking cho tới khi h giảm đủ.",
                   "The fix: damped Newton. Keep the Newton direction but backtrack on t until h decreases enough."), wait=False)
        for k in range(1, len(DMP)):
            self.play(d.animate.move_to(ax2.c2p(DMP[k], h(DMP[k]))), run_time=0.6)
            self.readout(["k = %d   t = %s   x = %s" % (k, nf(DTS[k - 1], 3), nf(DMP[k], 6) if abs(DMP[k]) > 1e-6 else sci(abs(DMP[k])))], color=MINT); self.wait(0.7)
        self.say(L("Bước đầu bị cắt còn t = %s; khi đã gần 0 thì t = 1 và hội tụ bậc hai quay lại." % nf(DTS[0], 3),
                   "The first step is cut to t = %s; once close to 0, t = 1 and quadratic convergence is back." % nf(DTS[0], 3)), hold=6.6)
        self.wipe()
        ax3 = plain_axes([-1.6, 1.6], [-0.3, 0.42], 7.6, 4.6, [0, 1.6, 0])
        Q = ax3.plot(q, x_range=[-1.6, 1.6], color=ORANGE, stroke_width=6)
        conc = ax3.plot(q, x_range=[-1 / np.sqrt(3), 1 / np.sqrt(3)], color=PINK, stroke_width=9)
        self.play(Create(ax3), Create(Q), run_time=0.8); self.play(Create(conc), run_time=0.5)
        mins = VGroup(*[Dot(ax3.c2p(s_, -0.25), radius=0.09, color=MINT) for s_ in (-1, 1)])
        self.add(mins)
        self.readout([("q(x) = x⁴/4 − x²/2,   q″ = 3x² − 1", ORANGE), ("đoạn hồng: q″ < 0" if VI else "pink piece: q″ < 0", PINK)], size=23)
        self.say(L("Đối chiếu hai, hàm không lồi: q(x) = x⁴/4 − x²/2, cực tiểu tại ±1, cực đại địa phương tại 0. Trên đoạn hồng q″ < 0, parabol xấp xỉ úp xuống.",
                   "Contrast two, a nonconvex function: q(x) = x⁴/4 − x²/2, minima at ±1, a local maximum at 0. On the pink piece q″ < 0, so the local parabola opens downward."), hold=9.7)
        dq = Dot(ax3.c2p(QN[0], q(QN[0])), radius=0.12, color=SUN); dgq = Dot(ax3.c2p(QG[0], q(QG[0])), radius=0.1, color=SKY); self.add(dgq, dq)
        def rq(k): self.readout([("Newton: x%s = %s,  q = %s" % ("₀₁₂₃₄"[k], nf(QN[k], 3), nf(q(QN[k]), 4)), SUN), ("q′(%s) = %s < 0, q″(%s) = %s < 0" % (nf(0.4, 1), nf(q1(0.4), 3), nf(0.4, 1), nf(q2(0.4), 2)), DIM)], size=22)
        rq(0)
        for k in range(1, 5):
            self.play(dq.animate.move_to(ax3.c2p(QN[k], q(QN[k]))), run_time=0.7); rq(k); self.wait(0.8)
        self.say(L("Từ x₀ = 0,4, đi sang phải mới là xuống dốc. Nhưng bước Newton = −q′/q″ có hai dấu âm, nên nhảy sang trái, rồi hội tụ về đỉnh x = 0. q tăng dần: đi sai hướng.",
                   "From x₀ = 0.4, going right is downhill. But the Newton step −q′/q″ has two negative signs, so it jumps left and then converges to the peak x = 0. q keeps increasing: the wrong way."), hold=11.0)
        for k in range(1, 7): self.play(dgq.animate.move_to(ax3.c2p(QG[k], q(QG[k]))), run_time=0.35)
        self.readout([("GD t = %s:  %s → %s (cực tiểu)" % (nf(0.5, 1), nf(0.4, 1), nf(QG[-1], 3)) if VI else "GD t = %s:  %s → %s (minimum)" % (nf(0.5, 1), nf(0.4, 1), nf(QG[-1], 3)), SKY), ("Newton:  → 0 (cực đại)" if VI else "Newton:  → 0 (maximum)", SUN)], size=23)
        self.say(L("GD thì đơn giản đi xuống, về cực tiểu x = 1. Bài nói mô hình bậc hai lồi, chỉ đúng khi ∇²f ≻ 0. Hessian không xác định dương thì phải sửa, ví dụ cộng thêm λI.",
                   "GD simply goes downhill to the minimum x = 1. The lesson's claim that the quadratic model is convex holds only when ∇²f ≻ 0. With an indefinite Hessian it must be fixed, for example by adding λI."), hold=11.7)
        self.takeaway([L("Newton nhảy tới đáy parabol xấp xỉ: x⁺ = x − [∇²f]⁻¹∇f.", "Newton jumps to the bottom of the local parabola: x⁺ = x − [∇²f]⁻¹∇f."),
                       L("Gần nghiệm hội tụ bậc hai; ở ví dụ 2D: %d bước so với %d của GD." % (KN2, KG2), "Quadratic convergence near the answer; in the 2D example %d steps versus %d for GD." % (KN2, KG2)),
                       L("Xa nghiệm có thể phân kỳ: dùng Newton tắt dần (backtracking).", "Far away it can diverge: use damped Newton (backtracking)."),
                       L("Hessian không xác định dương: Newton có thể đi lên, về cực đại.", "Indefinite Hessian: Newton can go uphill, to a maximum.")], tail=4.0)
