from rl import *
# Bài 06-02-02 / 06-02-03: tìm kiếm đường lùi và tìm kiếm đường chính xác
# 1D (06-02-02): f(x) = x² − 2x + 5, x₀ = 4, α = 0,5, β = 0,8
f1 = lambda x: x * x - 2 * x + 5; g1 = lambda x: 2 * x - 2
AL, BE = 0.5, 0.8
def bt(f, g, x, a=AL, b=BE):
    t = 1.; tr = []
    while f(x - t * g(x)) > f(x) - a * t * g(x) ** 2:
        tr.append((t, f(x - t * g(x)), f(x) - a * t * g(x) ** 2, False)); t *= b
    tr.append((t, f(x - t * g(x)), f(x) - a * t * g(x) ** 2, True)); return t, tr
T1, TR1 = bt(f1, g1, 4.)
assert len(TR1) == 5 and abs(T1 - 0.4096) < 1e-12 and abs(TR1[1][1] - 7.24) < 1e-9 and abs(TR1[2][1] - 4.7056) < 1e-9
assert abs(TR1[3][1] - 4.0052) < 1e-3 and abs(TR1[3][2] - 3.784) < 1e-9 and TR1[3][1] > TR1[3][2]   # t = 0,512 bị loại (sát nút)
X1 = 4 - T1 * 6; assert abs(X1 - 1.5424) < 1e-9
def fixed1(t, n=60):
    xs = [4.]
    for _ in range(n): xs.append(xs[-1] - t * g1(xs[-1]))
    return xs
S01, S15, S05 = fixed1(.1), fixed1(1.5, 6), fixed1(.5, 3)
assert abs(S01[20] - 1.0346) < 1e-4 and abs(S01[50] - 1) < 5e-5 and S15[:5] == [4., -5., 13., -23., 49.] and S05[1] == 1.
N01 = next(k for k, x in enumerate(S01) if abs(x - 1) < 1e-3); assert N01 == 36
xb, NB1, EV1 = 4., 0, 0
while abs(xb - 1) > 1e-6:
    t, tr = bt(f1, g1, xb); EV1 += len(tr); xb -= t * g1(xb); NB1 += 1
assert NB1 == 9 and EV1 == 45
# vì φ(t) = 13 − 36t + 36t² nên điều kiện Armijo ⇔ t ≤ 0,5
phi = lambda t: 36 * t * t - 36 * t + 13
assert all(abs(phi(r[0]) - r[1]) < 1e-9 for r in TR1)
# bậc bốn (06-02-02): f = x² + 0,1x⁴, x₀ = 2
f2 = lambda x: x * x + .1 * x ** 4; g2 = lambda x: 2 * x + .4 * x ** 3
T2, TR2 = bt(f2, g2, 2.); assert len(TR2) - 1 == 8 and abs(T2 - 0.16777) < 1e-4 and abs(2 - T2 * 7.2 - 0.792) < 1e-3
TE2 = 2 / 7.2; assert abs(g2(2 - TE2 * 7.2)) < 1e-12
# 2D (06-02-03, ví dụ 2): F = x₁² + 2x₂² − 2x₁ − 4x₂ + 3 = (x₁ − 1)² + 2(x₂ − 1)²
A = np.diag([2., 4.]); bb = np.array([2., 4.]); XS = np.array([1., 1.])
F = lambda x: x[0] ** 2 + 2 * x[1] ** 2 - 2 * x[0] - 4 * x[1] + 3; G = lambda x: A @ x - bb
assert abs(F(XS)) < 1e-12
def run(mode, step=None, tol=1e-6, n=3000):
    x = np.zeros(2); P = [x.copy()]; ev = 0; TT = []
    for k in range(n):
        gr = G(x)
        if np.linalg.norm(x - XS) < tol: return k, np.array(P), ev, TT
        if mode == "fixed": t = step
        elif mode == "exact": t = gr @ gr / (gr @ A @ gr)
        else:
            t = 1.
            while F(x - t * gr) > F(x) - AL * t * gr @ gr: t *= BE; ev += 1
            ev += 1
        x = x - t * gr; P.append(x.copy()); TT.append(t)
        if np.linalg.norm(x) > 1e6: return None, np.array(P), ev, TT
    return None, np.array(P), ev, TT
NF, PF, _, _ = run("fixed", .1); NB, PB, EVB, TB = run("bt"); NE, PE, _, TE = run("exact"); ND, PD, _, _ = run("fixed", .55, n=12)
assert (NF, NB, NE, EVB) == (62, 12, 12, 70) and ND is None
assert abs(TE[0] - 5 / 18) < 1e-12 and np.allclose(PE[1], [5 / 9, 10 / 9]) and abs(G(PE[0]) @ G(PE[1])) < 1e-12
assert abs(TB[0] - .8 ** 6) < 1e-12 and np.allclose(PF[1], [.2, .4]) and abs(PD[3][1] - 1 - (-1.2) ** 3 * (-1)) < 1e-9
Fx = lambda x, y: (x - 1) ** 2 + 2 * (y - 1) ** 2
LV = [0.02, 0.1, 0.3, 0.6, 1.0, 1.5, 2.2, 3.0]

def tn(t):
    s_ = ("%.4f" % t).rstrip("0").rstrip(".")
    return s_.replace(".", ",") if LANG == "vi" else s_

def mark(t, ok):
    return L("nhận", "accept") if ok else L("loại", "reject")

class Ls(Reel):
    def construct(self):
        self.title(L("Tìm kiếm đường:\nchọn bước t ở mỗi vòng", "Line search:\nchoosing the step t each round"))
        # ---- stage 1
        self.stage(1)
        ax = plain_axes([-3, 5], [0, 26], 7.6, 4.6, [0, 1.7, 0])
        cur = ax.plot(f1, x_range=[-3, 5], color=SKY, stroke_width=4)
        st = Dot(ax.c2p(1, 4), radius=0.1, color=MINT); stl = Text("x* = 1", font=MONO, font_size=20, color=MINT).next_to(st, DOWN, buff=0.15)
        self.play(Create(ax), Create(cur), run_time=1.0); self.add(st, stl)
        self.say(L("Bài 06-02-02: f(x) = x² − 2x + 5, xuất phát x₀ = 4. Nghiệm x* = 1, f* = 4.",
                   "Lesson 06-02-02: f(x) = x² − 2x + 5, starting at x₀ = 4. Solution x* = 1, f* = 4."), hold=5.5)
        self.readout(["x ← x − t·f′(x),   f′(x) = 2x − 2"], color=SUN, size=24)
        self.say(L("Gradient descent: x ← x − t·f′(x). Câu hỏi của bài: chọn bước t bằng bao nhiêu?",
                   "Gradient descent: x ← x − t·f′(x). The question of the lesson: how big should the step t be?"), hold=5.0)
        d = Dot(ax.c2p(4, f1(4)), radius=0.11, color=SKY); self.add(d)
        P01 = [(x, f1(x)) for x in S01]
        def r01(k): self.readout([("t = 0,1:  k = %d,  x = %s" % (k, nf(S01[k], 4)) if LANG == "vi" else "t = 0.1:  k = %d,  x = %s" % (k, nf(S01[k], 4)), SKY)], size=23)
        p1 = trail(self, ax, P01, d, SKY, rt=lambda k: 0.45 if k < 6 else 0.15, ks=range(1, 21), cb=r01, width=3)
        self.say(L("t = 0,1: mỗi bước khoảng cách tới x* chỉ nhân 0,8. Cần %d bước để |x − 1| < 10⁻³." % N01,
                   "t = 0.1: each step multiplies the distance to x* by only 0.8. It needs %d steps to reach |x − 1| < 10⁻³." % N01), hold=5.5)
        self.play(FadeOut(p1), d.animate.move_to(ax.c2p(4, f1(4))), run_time=0.4)
        self.readout([("t = 1,5:  x = 4 → −5 → 13 → −23 → 49" if LANG == "vi" else "t = 1.5:  x = 4 → −5 → 13 → −23 → 49", PINK)], size=23)
        jl = Line(ax.c2p(4, f1(4)), ax.c2p(-3, 26), color=PINK, stroke_width=3)
        self.play(Create(jl), d.animate.move_to(ax.c2p(-3, 26)).set_color(PINK), run_time=0.7)
        self.say(L("t = 1,5: bước quá dài. Khoảng cách nhân −2 mỗi bước, điểm nhảy ra khỏi hình và phân kỳ.",
                   "t = 1.5: the step is too long. The distance is multiplied by −2 each step, the point jumps out and diverges."), hold=5.5)
        self.play(FadeOut(jl), d.animate.move_to(ax.c2p(4, f1(4))).set_color(SKY), run_time=0.4)
        self.readout([("t = 0,5:  x = 4 → 1   (một bước)" if LANG == "vi" else "t = 0.5:  x = 4 → 1   (one step)", MINT)], size=23)
        jm = Line(ax.c2p(4, f1(4)), ax.c2p(1, 4), color=MINT, stroke_width=3)
        self.play(Create(jm), d.animate.move_to(ax.c2p(1, 4)), run_time=0.6)
        self.say(L("t = 0,5 tới đích ngay. Nhưng đó là may: phải biết độ cong của f mới chọn được. Với hàm khác, số này sai.",
                   "t = 0.5 lands right away. But that is luck: you need to know the curvature of f to pick it. For another function this number is wrong."), hold=6.5)
        # ---- stage 2
        self.stage(2); self.wipe()
        px = plain_axes([0, 1.05], [-6, 14], 7.4, 5.0, [0.2, 1.7, 0])
        ph = px.plot(phi, x_range=[0, 1.05], color=SKY, stroke_width=4)
        tg = DashedLine(px.c2p(0, 13), px.c2p(0.53, 13 - 36 * 0.53), color=DIM, stroke_width=2.5)
        ar = Line(px.c2p(0, 13), px.c2p(1.05, 13 - 18 * 1.05), color=SUN, stroke_width=3.5)
        tlab = Text("t", font=FONT, font_size=22, color=DIM).next_to(px.c2p(1.05, 0), DOWN, buff=0.12)
        phl = Text("φ(t) = f(x − t·f′(x))", font=MONO, font_size=20, color=SKY).move_to(px.c2p(0.62, 12.5))
        self.play(Create(px), FadeIn(tlab), run_time=0.5); self.play(Create(ph), FadeIn(phl), run_time=0.8)
        self.say(L("Đứng ở x = 4 (f′ = 6). Xét φ(t) = f(4 − 6t): giá trị f sau bước dài t. Ở đây φ(t) = 36t² − 36t + 13.",
                   "Stand at x = 4 (f′ = 6). Look at φ(t) = f(4 − 6t): the value of f after a step of length t. Here φ(t) = 36t² − 36t + 13."), hold=7.0)
        self.play(Create(tg), run_time=0.5)
        self.say(L("Đường đứt nét là tiếp tuyến 13 − 36t: mức giảm mà xấp xỉ tuyến tính hứa hẹn. f lồi nên φ luôn nằm trên nó.",
                   "The dashed line is the tangent 13 − 36t: the decrease the linear approximation promises. f is convex, so φ always stays above it."), hold=6.5)
        self.play(Create(ar), run_time=0.6)
        self.readout([("điều kiện Armijo:  φ(t) ≤ f(x) − α·t·f′(x)²" if LANG == "vi" else "Armijo condition:  φ(t) ≤ f(x) − α·t·f′(x)²", SUN), ("α = 0,5:  đường 13 − 18t" if LANG == "vi" else "α = 0.5:  line 13 − 18t", SUN)], size=22)
        self.say(L("Tìm kiếm đường lùi chỉ đòi một phần α của mức hứa hẹn. Với α = 0,5: nhận t nếu φ(t) nằm dưới đường vàng 13 − 18t.",
                   "Backtracking asks for only a fraction α of the promised decrease. With α = 0.5: accept t if φ(t) lies below the yellow line 13 − 18t."), hold=7.0)
        self.say(L("Bắt đầu t = 1. Nếu bị loại thì nhân t với β = 0,8 và thử lại.",
                   "Start with t = 1. If rejected, multiply t by β = 0.8 and try again."), hold=4.0)
        marks = VGroup()
        for (t, ph_, rh, ok) in TR1:
            c = MINT if ok else PINK
            m = VGroup(DashedLine(px.c2p(t, rh), px.c2p(t, ph_), color=c, stroke_width=2), Dot(px.c2p(t, ph_), radius=0.1, color=c))
            self.play(FadeIn(m), run_time=0.4); marks.add(m)
            self.readout([("t = %s" % tn(t), WHITE), ("φ(t) = %s   %s   13 − 18t = %s" % (nf(ph_, 3), "≤" if ok else ">", nf(rh, 3)), c), (mark(t, ok)[LANG], c)], size=22)
            self.wait(1.7 if not ok else 1.0)
        self.say(L("t = 0,512 bị loại sát nút: 4,005 > 3,784. t = 0,4096 được nhận. Bước mới x₁ = 4 − 0,4096·6 = %s." % nf(X1, 4),
                   "t = 0.512 is rejected by a hair: 4.005 > 3.784. t = 0.4096 is accepted. New point x₁ = 4 − 0.4096·6 = %s." % nf(X1, 4)), hold=7.0)
        acc = Rectangle(width=px.c2p(0.5, 0)[0] - px.c2p(0, 0)[0], height=0.18, fill_color=MINT, fill_opacity=0.6, stroke_width=0).move_to([(px.c2p(0.5, 0)[0] + px.c2p(0, 0)[0]) / 2, px.c2p(0, -6)[1] + 0.09, 0])
        self.play(FadeIn(acc), run_time=0.4)
        self.say(L("Vùng được nhận ở đây là 0 < t ≤ 0,5 (vạch xanh). Lùi bằng β luôn rơi vào vùng này sau vài lần thử.",
                   "The accepted region here is 0 < t ≤ 0.5 (green bar). Shrinking by β always lands in it after a few tries."), hold=6.0)
        # ---- stage 3
        self.stage(3); self.wipe()
        bx = plain_axes([-0.25, 1.75], [-0.25, 1.55], 7.6, 6.0, [0, 1.6, 0])
        cs = contours(bx, Fx, LV, (-0.25, 1.75, -0.25, 1.55), N=80)
        self.play(Create(cs), run_time=1.0)
        stb = Dot(bx.c2p(1, 1), radius=0.1, color=WHITE); self.add(stb)
        x0l = Text("x⁰ = (0; 0)" if LANG == "vi" else "x⁰ = (0, 0)", font=MONO, font_size=20, color=DIM).next_to(bx.c2p(0, 0), DR, buff=0.1)
        self.add(x0l)
        self.say(L("Bài 06-02-03, ví dụ 2: F = x₁² + 2x₂² − 2x₁ − 4x₂ + 3, xuất phát (0; 0). Nghiệm x* = (1; 1).",
                   "Lesson 06-02-03, example 2: F = x₁² + 2x₂² − 2x₁ − 4x₂ + 3, starting at (0, 0). Solution x* = (1, 1)."), hold=6.0)
        self.readout(["φ(t) = F(2t; 4t) = 36t² − 20t + 3" if LANG == "vi" else "φ(t) = F(2t, 4t) = 36t² − 20t + 3", "φ′(t) = 72t − 20 = 0  ⇒  t* = 5/18", "x¹ = (5/9; 10/9) ≈ %s" % vec(PE[1], 3) if LANG == "vi" else "x¹ = (5/9, 10/9) ≈ %s" % vec(PE[1], 3)], color=MINT, size=22)
        self.say(L("Tìm kiếm đường chính xác chọn t làm φ(t) nhỏ nhất. Hàm bậc hai nên giải được: t* = 5/18, x¹ = (5/9; 10/9).",
                   "Exact line search picks the t that minimizes φ(t). For a quadratic this is solvable: t* = 5/18, x¹ = (5/9, 10/9)."), hold=7.0)
        dF = Dot(bx.c2p(0, 0), radius=0.09, color=SKY); dB = Dot(bx.c2p(0, 0), radius=0.09, color=SUN); dE = Dot(bx.c2p(0, 0), radius=0.09, color=MINT)
        self.add(dF, dB, dE)
        pe = trail(self, bx, PE, dE, MINT, rt=0.6, ks=range(1, 7), width=3)
        self.say(L("Mỗi bước chính xác đi tới điểm thấp nhất trên đường thẳng, nên gradient mới vuông góc với hướng cũ: đường zig-zag vuông góc.",
                   "Each exact step goes to the lowest point on its line, so the new gradient is perpendicular to the old direction: a right-angle zig-zag."), hold=7.0)
        pb = trail(self, bx, PB, dB, SUN, rt=0.6, ks=range(1, 7), width=3)
        self.say(L("Đường lùi (vàng, α = 0,5, β = 0,8): bước đầu t = 0,8⁶ ≈ 0,262, gần 5/18 ≈ 0,278. Không cần giải gì, chỉ thử f vài lần.",
                   "Backtracking (yellow, α = 0.5, β = 0.8): the first step is t = 0.8⁶ ≈ 0.262, close to 5/18 ≈ 0.278. Nothing to solve, just a few tries of f."), hold=7.0)
        leg = VGroup(Text(L("chính xác", "exact")[LANG], font=FONT, font_size=20, color=MINT), Text(L("đường lùi", "backtracking")[LANG], font=FONT, font_size=20, color=SUN), Text(L("t = 0,1", "t = 0.1")[LANG], font=FONT, font_size=20, color=SKY)).arrange(RIGHT, buff=0.5).move_to([0, -1.75, 0])
        self.play(FadeIn(leg), run_time=0.3)
        pf = trail(self, bx, PF, dF, SKY, rt=0.25, ks=range(1, 21), width=3)
        self.readout([("t cố định 0,1:   %d vòng" % NF if LANG == "vi" else "fixed t = 0.1:   %d rounds" % NF, SKY), ("đường lùi:       %d vòng,  %d lần tính f" % (NB, EVB) if LANG == "vi" else "backtracking:    %d rounds, %d evaluations of f" % (NB, EVB), SUN), ("chính xác:       %d vòng" % NE if LANG == "vi" else "exact:           %d rounds" % NE, MINT)], size=22)
        self.say(L("Đếm số vòng để ‖x − x*‖ < 10⁻⁶: t = 0,1 cần %d, đường lùi %d, chính xác %d." % (NF, NB, NE),
                   "Rounds until ‖x − x*‖ < 10⁻⁶: t = 0.1 needs %d, backtracking %d, exact %d." % (NF, NB, NE)), hold=6.0)
        self.say(L("Còn t cố định 0,55 thì phân kỳ: theo x₂ mỗi bước nhân 1 − 4·0,55 = −1,2. Đường lùi tự tránh được lỗi này.",
                   "A fixed t = 0.55 diverges: along x₂ each step multiplies by 1 − 4·0.55 = −1.2. Backtracking avoids this by itself."), hold=6.5)
        # ---- stage 4
        self.stage(4); self.wipe()
        qx = plain_axes([0, 1.05], [-6, 14], 7.4, 4.4, [0.2, 2.0, 0])
        q1 = qx.plot(phi, x_range=[0, 1.05], color=SKY, stroke_width=4)
        qt = Line(qx.c2p(0, 13), qx.c2p(0.53, 13 - 36 * 0.53), color=PINK, stroke_width=3.5)
        qtl = Text(L("α = 1: tiếp tuyến 13 − 36t", "α = 1: tangent 13 − 36t")[LANG], font=MONO, font_size=20, color=PINK).move_to(qx.c2p(0.62, -4.5))
        self.play(Create(qx), Create(q1), run_time=0.7); self.play(Create(qt), FadeIn(qtl), run_time=0.5)
        self.say(L("Vì sao α phải nhỏ hơn 1? Với α = 1, đường chấp nhận trùng tiếp tuyến (hồng). f lồi nên φ luôn ở trên, không t > 0 nào được nhận: vòng lùi chạy mãi.",
                   "Why must α be below 1? With α = 1 the acceptance line is the tangent (pink). f is convex, so φ always stays above it: no t > 0 is accepted and the loop never ends."), hold=8.5)
        self.say(L("Thường chọn α trong (0; 0,5] và β trong khoảng 0,5 đến 0,9.",
                   "Typical choices: α in (0, 0.5] and β between 0.5 and 0.9."), hold=4.5)
        self.play(FadeOut(VGroup(qx, q1, qt, qtl)), run_time=0.4)
        phi2 = lambda t: f2(2 - 7.2 * t)
        rx = plain_axes([0, 0.7], [-1, 12], 7.4, 4.4, [0.2, 2.0, 0])
        tmax = max(t for t in np.linspace(0, 0.7, 701) if phi2(t) <= 12)
        r1 = rx.plot(phi2, x_range=[0, tmax], color=SKY, stroke_width=4)
        r2 = Line(rx.c2p(0, 5.6), rx.c2p(5.6 / 25.92, 0), color=SUN, stroke_width=3.5)
        r2b = DashedLine(rx.c2p(5.6 / 25.92, 0), rx.c2p(0.25, 5.6 - 25.92 * 0.25), color=SUN, stroke_width=2.5)
        self.play(Create(rx), Create(r1), Create(r2), Create(r2b), run_time=0.8)
        for (t, p_, rh, ok) in TR2:
            if p_ > 12: continue
            c = MINT if ok else PINK
            self.play(FadeIn(Dot(rx.c2p(t, p_), radius=0.09, color=c)), run_time=0.25)
        self.readout([("f(x) = x² + 0,1x⁴,  x₀ = 2,  f′(2) = 7,2" if LANG == "vi" else "f(x) = x² + 0.1x⁴,  x₀ = 2,  f′(2) = 7.2", WHITE), ("đường lùi: lùi %d lần, t = 0,8⁸ ≈ %s" % (len(TR2) - 1, nf(T2, 3)) if LANG == "vi" else "backtracking: %d shrinks, t = 0.8⁸ ≈ %s" % (len(TR2) - 1, nf(T2, 3)), SUN), ("  ⇒ x₁ ≈ %s" % nf(2 - T2 * 7.2, 3), SUN), ("chính xác: t* = %s ⇒ x₁ = 0" % nf(TE2, 3) if LANG == "vi" else "exact: t* = %s ⇒ x₁ = 0" % nf(TE2, 3), MINT), ("(phải giải φ′(t) = 0, bậc ba)" if LANG == "vi" else "(must solve φ′(t) = 0, a cubic)", MINT)], size=21, y=-2.9)
        self.say(L("Ví dụ bậc bốn của bài 06-02-02: đường lùi lùi %d lần rồi nhận t ≈ %s, x₁ ≈ %s. Mỗi lần thử chỉ tốn một lần tính f." % (len(TR2) - 1, nf(T2, 3), nf(2 - T2 * 7.2, 2)),
                   "The quartic example of lesson 06-02-02: backtracking shrinks %d times, then accepts t ≈ %s, x₁ ≈ %s. Each try costs one evaluation of f." % (len(TR2) - 1, nf(T2, 3), nf(2 - T2 * 7.2, 2))), hold=7.5)
        self.say(L("Tìm chính xác cho bước tốt nhất, nhưng với hàm không bậc hai phải giải thêm một bài tối ưu một biến ở mỗi vòng. Vì vậy thực tế hay dùng đường lùi.",
                   "Exact search gives the best step, but for non-quadratic functions it needs a one-variable optimization every round. That is why backtracking is used in practice."), hold=8.0)
        self.takeaway([L("t cố định: nhỏ thì chậm, lớn thì phân kỳ.", "Fixed t: too small is slow, too large diverges."),
                       L("Đường lùi: bắt đầu t = 1, nhân β tới khi φ(t) ≤ f − α·t·‖∇f‖².", "Backtracking: start at t = 1, multiply by β until φ(t) ≤ f − α·t·‖∇f‖²."),
                       L("Cần 0 < α < 1; f lồi nằm trên tiếp tuyến nên α = 1 không bao giờ nhận.", "Need 0 < α < 1; a convex f lies above its tangent, so α = 1 never accepts."),
                       L("Chính xác: t = argmin φ(t), tốt nhất mỗi bước nhưng đắt.", "Exact: t = argmin φ(t), best per step but expensive.")])
