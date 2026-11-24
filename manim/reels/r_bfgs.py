from rl import *
import math
def F(p):
    return float(np.logaddexp.reduce([p[0] + 3 * p[1] - .1, p[0] - 3 * p[1] - .1, -p[0] - .1]))
def G(p):
    a, b, c = math.exp(p[0] + 3 * p[1] - .1), math.exp(p[0] - 3 * p[1] - .1), math.exp(-p[0] - .1); z = a + b + c
    return np.array([(a + b - c) / z, (3 * a - 3 * b) / z])
def Hs(p):
    a, b, c = math.exp(p[0] + 3 * p[1] - .1), math.exp(p[0] - 3 * p[1] - .1), math.exp(-p[0] - .1); z = a + b + c; g = G(p)
    return np.array([[(a + b + c) / z - g[0] ** 2, (3 * a - 3 * b) / z - g[0] * g[1]], [(3 * a - 3 * b) / z - g[0] * g[1], 9 * (a + b) / z - g[1] ** 2]])
ps = np.zeros(2)
for _ in range(60): ps = ps - np.linalg.solve(Hs(ps), G(ps))
FS = F(ps); HINV = np.linalg.inv(Hs(ps))
def run(kind, start, maxit=400):
    p = np.array(start, float); pts = [p.copy()]; H = np.eye(2); Hh = [H.copy()]; it = 0
    while it < maxit and F(p) - FS > 1e-10:
        g = G(p)
        d = -g if kind == "gd" else (-H @ g if kind == "bfgs" else -np.linalg.solve(Hs(p), g))
        t = 1.0; gd = g @ d; k = 0
        while F(p + t * d) > F(p) + 0.1 * t * gd and k < 80: t *= 0.7; k += 1
        pn = p + t * d
        if kind == "bfgs":
            s = pn - p; y = G(pn) - g; sy = s @ y
            if sy > 1e-14:
                r = 1 / sy; I = np.eye(2); H = (I - r * np.outer(s, y)) @ H @ (I - r * np.outer(y, s)) + r * np.outer(s, s)
                assert np.allclose(H @ y, s)
        p = pn; pts.append(p.copy()); Hh.append(H.copy()); it += 1
    return pts, it, Hh
S0 = (1.6, 1.1)
GP, NG, _ = run("gd", S0); BP, NB, BH = run("bfgs", S0); NP, NN, _ = run("newton", S0)
assert (NG, NB) == (23, 8) and NN <= NB
assert np.allclose(BP[1], GP[1])          # first BFGS step (H0 = I) is a GD step
eG = [np.linalg.norm(p - ps) for p in GP]; eB = [np.linalg.norm(p - ps) for p in BP]
rG = eG[-1] / eG[-2]; rB = eB[-1] / eB[-2]
assert rB < 0.1 < rG
HE = [np.linalg.norm(H - HINV) / np.linalg.norm(HINV) for H in BH]

# cặp (s, y), điều kiện độ cong, độ xác định dương của Hₖ
SY = []
for k in range(NB):
    s_ = BP[k + 1] - BP[k]; y_ = G(BP[k + 1]) - G(BP[k]); SY.append((s_, y_, s_ @ y_, np.linalg.eigvalsh(BH[k + 1])))
assert all(t[2] > 0 for t in SY) and all(t[3].min() > 0 for t in SY)
S0V, Y0V = SY[0][0], SY[0][1]; assert np.allclose(BH[1] @ Y0V, S0V) and abs(SY[0][2] - 12.445) < 1e-3
# hàm không lồi: sᵀy < 0 thì không có H ≻ 0 nào thoả Hy = s
q1 = lambda x: x ** 3 - x                      # đạo hàm của x⁴/4 − x²/2
NS, NY = 0.2, q1(0.4) - q1(0.2); assert np.isclose(NY, -0.144) and NS * NY < 0 and NS / NY < 0
# L-BFGS: chỉ giữ m cặp gần nhất, đệ quy hai vòng
def lbfgs(start, m, maxit=400):
    p = np.array(start, float); S = []; Y = []; it = 0
    while it < maxit and F(p) - FS > 1e-10:
        g = G(p); q = g.copy(); al = []
        for s, y in reversed(list(zip(S, Y))):
            a = (s @ q) / (y @ s); al.append(a); q = q - a * y
        r = ((S[-1] @ Y[-1]) / (Y[-1] @ Y[-1]) if S else 1.0) * q
        for (s, y), a in zip(zip(S, Y), reversed(al)):
            r = r + s * (a - (y @ r) / (y @ s))
        d = -r; t = 1.0; gd = g @ d; k = 0
        while F(p + t * d) > F(p) + 0.1 * t * gd and k < 80: t *= 0.7; k += 1
        pn = p + t * d; s = pn - p; y = G(pn) - g
        if s @ y > 1e-14: S.append(s); Y.append(y); S = S[-m:]; Y = Y[-m:]
        p = pn; it += 1
    return it
LM = {m: lbfgs(S0, m) for m in (1, 2, 3)}
assert LM == {1: 15, 2: 11, 3: 9} and NB < LM[3] < LM[1] < NG
NBIG = 10 ** 6; assert NBIG * NBIG * 8 == 8 * 10 ** 12 and 2 * 10 * NBIG * 8 == 160 * 10 ** 6
VI = LANG == "vi"

class QN(Reel):
    def construct(self):
        self.title(L("Gradient descent và BFGS\ntrên cùng một hàm", "Gradient descent vs BFGS\non the same function"))
        # ---- stage 1
        self.stage(1)
        ax = plain_axes([-2.6, 2.4], [-2.6, 2.4], 6.6, 6.6, [0, 1.0, 0])
        cs = contours(ax, lambda x, y: F((x, y)), [FS + d for d in (0.05, 0.2, 0.5, 1.0, 1.6, 2.4, 3.3)], (-2.6, 2.4, -2.6, 2.4), N=70)
        self.play(Create(cs), run_time=1.5)
        st = Dot(ax.c2p(*ps), radius=0.1, color=MINT); self.add(st)
        self.say(L("f(x, y) = log(e^(x+3y−0,1) + e^(x−3y−0,1) + e^(−x−0,1)): trơn, lồi, có một thung lũng hẹp. Chấm xanh lá là cực tiểu.",
                   "f(x, y) = log(e^(x+3y−0.1) + e^(x−3y−0.1) + e^(−x−0.1)): smooth, convex, with a narrow valley. The green dot is the minimum."), hold=8.5)
        self.readout(["x* = " + vec(ps, 3) + "   f* = " + nf(FS, 4), "start = " + vec(S0, 1)], color=DIM)
        self.say(L("Hai thuật toán cùng xuất phát từ (1,6; 1,1), cùng dùng line search backtracking. Chỉ khác nhau ở hướng đi.",
                   "Both methods start at (1.6, 1.1) and use the same backtracking line search. Only the direction differs."), hold=7.0)
        # ---- stage 2
        self.stage(2)
        self.readout(["GD:    d = −∇f(x)", "BFGS:  d = −Hₖ∇f(x),  Hₖ ≈ [∇²f]⁻¹"], color=SUN, size=24)
        self.say(L("GD đi theo −gradient. BFGS nhân gradient với ma trận Hₖ, học dần nghịch đảo Hessian chỉ từ các gradient, không cần đạo hàm bậc hai.",
                   "GD follows −gradient. BFGS multiplies it by a matrix Hₖ that learns the inverse Hessian from gradients alone, no second derivatives."), hold=8.5)
        self.readout(["sₖ = xₖ₊₁ − xₖ,   yₖ = ∇fₖ₊₁ − ∇fₖ", ("yₖ ≈ ∇²f · sₖ   (Taylor)", DIM), ("⇒  đòi  Hₖ₊₁ yₖ = sₖ   (phương trình cát tuyến)" if VI else "⇒  require  Hₖ₊₁ yₖ = sₖ   (secant equation)", SUN)], color=WHITE, size=23)
        self.say(L("Phương trình cát tuyến: gradient thay đổi xấp xỉ bằng Hessian nhân bước đi, yₖ ≈ ∇²f·sₖ. Nên ma trận mới phải biến yₖ trở lại thành sₖ.",
                   "The secant equation: the change in gradient is roughly the Hessian times the step, yₖ ≈ ∇²f·sₖ. So the new matrix must map yₖ back to sₖ."), hold=10.0)
        self.readout(["ρₖ = 1/(yₖᵀsₖ)", "Hₖ₊₁ = (I − ρₖsₖyₖᵀ) Hₖ (I − ρₖyₖsₖᵀ)", "        + ρₖ sₖsₖᵀ"], color=SUN, size=24)
        self.say(L("Bài 18-04: trong mọi ma trận đối xứng thoả cát tuyến, chọn cái gần Hₖ nhất. Kết quả là công thức sửa hạng hai này, chỉ tốn O(n²).",
                   "Lesson 18-04: among all symmetric matrices satisfying the secant equation, pick the one closest to Hₖ. The result is this rank-two update, costing only O(n²)."), hold=10.0)
        self.readout([("điều kiện độ cong:  sₖᵀyₖ > 0" if VI else "curvature condition:  sₖᵀyₖ > 0", ORANGE), ("Hₖ₊₁ ≻ 0, Hₖ₊₁yₖ = sₖ  ⇒  sₖᵀyₖ = yₖᵀHₖ₊₁yₖ > 0", WHITE)], size=23)
        self.say(L("Điều kiện độ cong sᵀy > 0: nếu H xác định dương và Hy = s thì sᵀy = yᵀHy phải dương. Ngược lại, có sᵀy > 0 thì BFGS giữ được H ≻ 0, nên −Hg luôn là hướng giảm.",
                   "The curvature condition sᵀy > 0: if H is positive definite and Hy = s, then sᵀy = yᵀHy must be positive. Conversely, with sᵀy > 0 BFGS keeps H ≻ 0, so −Hg is always a descent direction."), hold=12.0)
        # ---- stage 3
        self.stage(3); self.clear_ro()
        dg = Dot(ax.c2p(*S0), radius=0.12, color=SKY); db = Dot(ax.c2p(*S0), radius=0.12, color=SUN); self.add(dg, db)
        self.say(L("Xanh: GD.  Vàng: BFGS. H₀ = I nên bước đầu của hai bên trùng nhau.", "Blue: GD.  Yellow: BFGS. H₀ = I, so the first steps coincide."), wait=False)
        for k in range(1, NG + 1):
            an = []
            sg = Line(ax.c2p(*GP[k - 1]), ax.c2p(*GP[k]), color=SKY, stroke_width=4); an += [Create(sg), dg.animate.move_to(ax.c2p(*GP[k]))]
            if k <= NB:
                sb = Line(ax.c2p(*BP[k - 1]), ax.c2p(*BP[k]), color=SUN, stroke_width=5); an += [Create(sb), db.animate.move_to(ax.c2p(*BP[k]))]
            self.play(*an, run_time=0.8 if k <= NB else 0.3)
            kb = min(k, NB)
            rows = [("GD    k = %2d   f − f* = %s" % (k, sci(max(F(GP[k]) - FS, 1e-16))), SKY), ("BFGS  k = %2d   f − f* = %s" % (kb, sci(max(F(BP[kb]) - FS, 1e-16))), SUN)]
            if k <= NB: rows += [("sₖ₋₁ᵀyₖ₋₁ = %s" % sci(SY[k - 1][2]), ORANGE), ("‖Hₖ − [∇²f(x*)]⁻¹‖ / ‖·‖ = %s" % nf(HE[k], 2), DIM)]
            self.readout(rows, color=WHITE, size=22)
            if k == 1: self.wait(1.0)
            if k == NB:
                self.say(L("BFGS xong sau %d bước (f − f* < 10⁻¹⁰), và Hₖ đã gần nghịch đảo Hessian thật tại nghiệm." % NB,
                           "BFGS is done after %d steps (f − f* < 10⁻¹⁰), and Hₖ is close to the true inverse Hessian at the solution." % NB), hold=6.5)
        self.say(L("GD cần %d bước, zig-zag qua lại thung lũng hẹp." % NG, "GD needs %d steps, zig-zagging across the narrow valley." % NG), hold=5.5)
        self.readout(["s₀ = %s" % vec(S0V, 3), "y₀ = %s" % vec(Y0V, 3), ("H₁y₀ = %s = s₀  ✓" % vec(BH[1] @ Y0V, 3), MINT), ("s₀ᵀy₀ = %s > 0" % nf(SY[0][2], 2), ORANGE)], color=WHITE, size=23)
        self.say(L("Kiểm tra bằng số ở bước đầu: s₀ và y₀ như trên, sau khi cập nhật thì H₁y₀ trả lại đúng s₀. Tích s₀ᵀy₀ ≈ 12,45, dương.",
                   "A numeric check at the first step: with s₀ and y₀ as shown, after the update H₁y₀ returns exactly s₀. The product s₀ᵀy₀ ≈ 12.45 is positive."), hold=9.5)
        rows = [("k   sₖᵀyₖ        trị riêng của Hₖ₊₁" if VI else "k   sₖᵀyₖ        eigenvalues of Hₖ₊₁", WHITE)] + [("%d   %-10s   %s, %s" % (k, sci(t[2], 2), nf(t[3][0], 3), nf(t[3][1], 3)) if not VI else "%d   %-10s   %s; %s" % (k, sci(t[2], 2), nf(t[3][0], 3), nf(t[3][1], 3)), SUN) for k, t in enumerate(SY)]
        self.readout(rows, size=21, y=-3.0)
        self.say(L("Cả 8 bước đều có sᵀy > 0 vì f lồi, nên mọi Hₖ có hai trị riêng dương. sᵀy nhỏ dần chỉ vì bước đi ngắn lại gần nghiệm.",
                   "All 8 steps have sᵀy > 0 because f is convex, so every Hₖ has two positive eigenvalues. sᵀy shrinks only because the steps get short near the answer."), hold=10.0)
        # ---- stage 4
        self.stage(4)
        self.readout([("tỉ lệ sai số cuối  ‖eₖ₊₁‖/‖eₖ‖" if VI else "last error ratio  ‖eₖ₊₁‖/‖eₖ‖", WHITE), ("GD:    %s" % nf(rG, 3), SKY), ("BFGS:  %s" % nf(rB, 4), SUN),
                      ("Newton (Hessian thật): %d bước" % NN if VI else "Newton (true Hessian): %d steps" % NN, MINT)], color=WHITE, size=23)
        self.say(L("GD co sai số theo một tỉ lệ gần như cố định. Với BFGS tỉ lệ này tiến về 0: hội tụ siêu tuyến tính.",
                   "GD shrinks the error by a roughly fixed ratio. For BFGS the ratio goes to 0: superlinear convergence."), hold=7.5)
        self.say(L("Newton thật chỉ cần %d bước nhưng phải tính và giải với Hessian mỗi bước, O(n³). BFGS chỉ tốn O(n²)." % NN,
                   "True Newton needs %d steps but must form and solve with the Hessian every step, O(n³). BFGS costs O(n²)." % NN), hold=8.0)
        self.readout([("f(x) = x⁴/4 − x²/2  (không lồi)" if VI else "f(x) = x⁴/4 − x²/2  (nonconvex)", PINK), "x: %s → %s   s = %s" % (nf(0.2, 1), nf(0.4, 1), nf(NS, 1)), "y = f′(%s) − f′(%s) = %s" % (nf(0.4, 1), nf(0.2, 1), nf(NY, 3)),
                      ("sᵀy = %s < 0  ⇒  H = s/y = %s < 0  ✗" % (nf(NS * NY, 4), nf(NS / NY, 2)), PINK)], color=WHITE, size=22)
        self.say(L("Đối chiếu: trên hàm không lồi, sᵀy có thể âm. Ví dụ này cho H = s/y ≈ −1,39: hướng −Hg đi lên dốc. Vì vậy line search phải đảm bảo điều kiện Wolfe, hoặc bỏ qua cặp đó.",
                   "Contrast: on a nonconvex function sᵀy can be negative. This example gives H = s/y ≈ −1.39: the direction −Hg goes uphill. That is why the line search must enforce the Wolfe conditions, or skip that pair."), hold=12.0)
        self.readout([("n = 10⁶ biến:" if VI else "n = 10⁶ variables:", WHITE), ("BFGS: Hₖ dày, n² = 10¹² số ≈ 8 TB" if VI else "BFGS: dense Hₖ, n² = 10¹² numbers ≈ 8 TB", PINK), ("L-BFGS, m = 10 cặp (s, y):" if VI else "L-BFGS, m = 10 pairs (s, y):", MINT), ("2mn = 2·10⁷ số ≈ 160 MB" if VI else "2mn = 2·10⁷ numbers ≈ 160 MB", MINT)], size=22)
        self.say(L("Cầu nối sang bài 18-07: với một triệu biến, riêng ma trận Hₖ đã 8 TB. L-BFGS không lưu Hₖ, chỉ giữ m cặp (s, y) gần nhất và tính Hₖ∇f bằng đệ quy hai vòng, O(mn).",
                   "Bridge to lesson 18-07: with a million variables, Hₖ alone takes 8 TB. L-BFGS never stores Hₖ; it keeps the last m pairs (s, y) and computes Hₖ∇f with a two-loop recursion, O(mn)."), hold=12.0)
        self.readout([("cùng hàm, cùng line search, f − f* < 10⁻¹⁰" if VI else "same function, same line search, f − f* < 10⁻¹⁰", WHITE), ("GD               %d bước" % NG if VI else "GD               %d steps" % NG, SKY),
                      ("L-BFGS  m = 1    %d" % LM[1], MINT), ("L-BFGS  m = 2    %d" % LM[2], MINT), ("L-BFGS  m = 3    %d" % LM[3], MINT), ("BFGS (đầy đủ)    %d" % NB if VI else "BFGS (full)      %d" % NB, SUN)], size=23)
        self.say(L("Ngay trên hàm này: L-BFGS chỉ nhớ 1 cặp đã cần %d bước thay vì %d của GD; nhớ 3 cặp được %d, sát BFGS đầy đủ (%d)." % (LM[1], NG, LM[3], NB),
                   "On this very function: L-BFGS remembering just 1 pair needs %d steps instead of GD's %d; with 3 pairs it takes %d, close to full BFGS (%d)." % (LM[1], NG, LM[3], NB)), hold=10.0)
        self.takeaway([L("Phương trình cát tuyến Hₖ₊₁yₖ = sₖ: học nghịch đảo Hessian từ gradient.", "Secant equation Hₖ₊₁yₖ = sₖ: learn the inverse Hessian from gradients."),
                       L("Cần điều kiện độ cong sᵀy > 0 để Hₖ luôn xác định dương.", "The curvature condition sᵀy > 0 keeps Hₖ positive definite."),
                       L("Ở đây: %d bước so với %d của GD; gần nghiệm hội tụ siêu tuyến tính." % (NB, NG), "Here: %d steps versus %d for GD; superlinear near the answer." % (NB, NG)),
                       L("L-BFGS chỉ giữ m cặp (s, y): bộ nhớ O(mn), dùng được cho n rất lớn.", "L-BFGS keeps only m pairs (s, y): O(mn) memory, fit for huge n.")], tail=4.0)
