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

class QN(Reel):
    def construct(self):
        self.title(L("Gradient descent và BFGS\ntrên cùng một hàm", "Gradient descent vs BFGS\non the same function"))
        self.stage(1)
        ax = plain_axes([-2.6, 2.4], [-2.6, 2.4], 6.6, 6.6, [0, 1.0, 0])
        cs = contours(ax, lambda x, y: F((x, y)), [FS + d for d in (0.05, 0.2, 0.5, 1.0, 1.6, 2.4, 3.3)], (-2.6, 2.4, -2.6, 2.4), N=70)
        self.play(Create(cs), run_time=1.5)
        st = Dot(ax.c2p(*ps), radius=0.1, color=MINT); self.add(st)
        self.say(L("f(x, y) = log(e^(x+3y−0,1) + e^(x−3y−0,1) + e^(−x−0,1)): trơn, lồi, thung lũng hẹp.",
                   "f(x, y) = log(e^(x+3y−0.1) + e^(x−3y−0.1) + e^(−x−0.1)): smooth, convex, a narrow valley."))
        self.readout(["x* = " + vec(ps, 3) + "   f* = " + nf(FS, 4), "start = " + vec(S0, 1)], color=DIM)
        self.say(L("Hai thuật toán cùng xuất phát từ (1,6; 1,1), cùng dùng line search backtracking.", "Both methods start at (1.6, 1.1) and use the same backtracking line search."))
        # key idea
        self.stage(2)
        self.readout(["GD:    d = −∇f(x)", "BFGS:  d = −Hₖ∇f(x),  Hₖ ≈ [∇²f]⁻¹", "Hₖ₊₁ yₖ = sₖ   (secant)"], color=SUN, size=24)
        self.say(L("GD đi theo −gradient. BFGS nhân gradient với ma trận Hₖ, học dần nghịch đảo Hessian chỉ từ các gradient.",
                   "GD follows −gradient. BFGS multiplies it by a matrix Hₖ that learns the inverse Hessian from gradients alone."), hold=5.0)
        self.say(L("Mỗi bước cho cặp sₖ = xₖ₊₁ − xₖ, yₖ = ∇fₖ₊₁ − ∇fₖ. Hₖ₊₁ được sửa hạng 2 để Hₖ₊₁yₖ = sₖ.",
                   "Each step gives a pair sₖ = xₖ₊₁ − xₖ, yₖ = ∇fₖ₊₁ − ∇fₖ. Hₖ₊₁ gets a rank-two fix so that Hₖ₊₁yₖ = sₖ."), hold=5.0)
        # algorithm
        self.stage(3)
        dg = Dot(ax.c2p(*S0), radius=0.12, color=SKY); db = Dot(ax.c2p(*S0), radius=0.12, color=SUN); self.add(dg, db)
        self.say(L("Xanh: GD.  Vàng: BFGS. H₀ = I nên bước đầu của hai bên trùng nhau.", "Blue: GD.  Yellow: BFGS. H₀ = I, so the first steps coincide."), wait=False)
        segG, segB = [], []
        for k in range(1, NG + 1):
            an = []
            sg = Line(ax.c2p(*GP[k - 1]), ax.c2p(*GP[k]), color=SKY, stroke_width=4); segG.append(sg); an += [Create(sg), dg.animate.move_to(ax.c2p(*GP[k]))]
            if k <= NB:
                sb = Line(ax.c2p(*BP[k - 1]), ax.c2p(*BP[k]), color=SUN, stroke_width=5); segB.append(sb); an += [Create(sb), db.animate.move_to(ax.c2p(*BP[k]))]
            self.play(*an, run_time=0.7 if k <= NB else 0.3)
            kb = min(k, NB)
            rows = [("GD    k = %2d   f − f* = %s" % (k, sci(max(F(GP[k]) - FS, 1e-16))), SKY), ("BFGS  k = %2d   f − f* = %s" % (kb, sci(max(F(BP[kb]) - FS, 1e-16))), SUN)]
            if k <= NB: rows.append(("‖Hₖ − [∇²f(x*)]⁻¹‖ / ‖·‖ = %s" % nf(HE[k], 3), DIM))
            self.readout(rows, color=WHITE, size=22)
            if k == NB:
                self.say(L("BFGS xong sau %d bước (f − f* < 10⁻¹⁰), ma trận Hₖ đã gần nghịch đảo Hessian thật." % NB,
                           "BFGS is done after %d steps (f − f* < 10⁻¹⁰), and Hₖ is close to the true inverse Hessian." % NB), hold=4.0)
        self.say(L("GD cần %d bước, zig-zag qua lại thung lũng hẹp." % NG, "GD needs %d steps, zig-zagging across the narrow valley." % NG))
        # contrast
        self.stage(4)
        self.readout([("tỉ lệ sai số cuối  ‖eₖ₊₁‖/‖eₖ‖" if LANG == "vi" else "last error ratio  ‖eₖ₊₁‖/‖eₖ‖", WHITE), ("GD:    %s" % nf(rG, 3), SKY), ("BFGS:  %s" % nf(rB, 4), SUN),
                      ("Newton (Hessian thật): %d bước" % NN if LANG == "vi" else "Newton (true Hessian): %d steps" % NN, MINT)], color=WHITE, size=23)
        self.say(L("GD co sai số theo một tỉ lệ gần như cố định. Với BFGS tỉ lệ này tiến về 0: hội tụ siêu tuyến tính.",
                   "GD shrinks the error by a roughly fixed ratio. For BFGS the ratio goes to 0: superlinear convergence."), hold=5.0)
        self.say(L("Newton thật chỉ cần %d bước nhưng phải tính và giải với Hessian mỗi bước (O(n³)). BFGS chỉ tốn O(n²)." % NN,
                   "True Newton needs %d steps but must form and solve with the Hessian every step (O(n³)). BFGS costs O(n²)." % NN), hold=5.5)
        self.takeaway([L("BFGS học nghịch đảo Hessian từ các cặp (s, y), không cần đạo hàm bậc hai.", "BFGS learns the inverse Hessian from (s, y) pairs, no second derivatives."),
                       L("Ở đây: %d bước so với %d bước của gradient descent." % (NB, NG), "Here: %d steps versus %d for gradient descent." % (NB, NG)),
                       L("Gần nghiệm hội tụ siêu tuyến tính, mỗi bước chỉ O(n²).", "Superlinear convergence near the answer, only O(n²) per step.")])
