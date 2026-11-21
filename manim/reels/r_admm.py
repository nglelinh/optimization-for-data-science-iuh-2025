from rl import *
from o3lib import LA, LB, soft, lasso_star, lasso_f, admm
LAMB = .8
ST = lasso_star(LAMB)
def admm_full(rho, n):
    M = np.linalg.inv(LA.T @ LA + rho * np.eye(2)); Atb = LA.T @ LB; z = np.zeros(2); u = np.zeros(2); rec = []
    for k in range(n):
        x = M @ (Atb + rho * (z - u)); zo = z.copy(); z = soft(x + u, LAMB / rho); u = u + x - z
        rec.append(dict(x=x.copy(), z=z.copy(), u=u.copy(), r=np.linalg.norm(x - z), s=rho * np.linalg.norm(z - zo)))
    return rec
R = admm_full(1.0, 60)
xs_, zs_ = admm(LAMB, 1, 60); assert all(np.allclose(R[k]["z"], zs_[k + 1]) for k in range(60))
assert np.linalg.norm(R[-1]["z"] - ST) < 1e-8 and R[-1]["z"][1] == 0.0
def iters(rho, tol=1e-6):
    rec = admm_full(rho, 5000); return next(k + 1 for k in range(5000) if np.linalg.norm(rec[k]["z"] - ST) < tol)
RH = {rho: iters(rho) for rho in (0.1, 0.3, 1, 3, 10)}
assert RH[1] < RH[0.1] and RH[1] < RH[10]
ZK = next(k for k in range(60) if all(R[j]["z"][1] == 0 for j in range(k, 60)))

class Admm(Reel):
    def construct(self):
        self.title(L("ADMM: tách bài toán,\nrồi kéo hai nửa lại gần nhau", "ADMM: split the problem,\nthen pull the halves together"))
        self.stage(1)
        self.readout(["min ½‖Ax − b‖² + λ‖x‖₁,   λ = 0,8" if LANG == "vi" else "min ½‖Ax − b‖² + λ‖x‖₁,   λ = 0.8", ("⇕", DIM), "min ½‖Ax − b‖² + λ‖z‖₁   s.t.  x = z"], color=WHITE, size=25, y=2.8)
        self.say(L("Lasso khó vì có cả phần bình phương lẫn phần ℓ₁. ADMM nhân đôi biến: x giữ phần bình phương, z giữ phần ℓ₁, buộc x = z.",
                   "Lasso is awkward because it mixes a squared part and an ℓ₁ part. ADMM duplicates the variable: x takes the squares, z the ℓ₁, with x = z."), hold=6.0)
        # key idea
        self.stage(2)
        self.readout(["x ← (AᵀA + ρI)⁻¹(Aᵀb + ρ(z − u))", ("z ← soft(x + u, λ/ρ)", PINK), ("u ← u + x − z", ORANGE)], color=SKY, size=24, y=2.8)
        self.say(L("Ba bước luân phiên: x giải một hệ tuyến tính (ridge), z co ngưỡng mềm, u cộng dồn phần lệch x − z.",
                   "Three alternating steps: x solves a linear system (ridge), z soft-thresholds, u accumulates the mismatch x − z."), hold=5.5)
        self.say(L("u là biến đối ngẫu (giá đã chia ρ) cho ràng buộc x = z: lệch mãi thì giá tăng, kéo hai bên lại.",
                   "u is the (scaled) dual variable for x = z: a persistent mismatch raises the price and pulls the two together."), hold=5.0)
        # algorithm
        self.stage(3); self.clear_ro()
        ax = plain_axes([-0.6, 2.6], [-1.0, 1.9], 7.2, 5.8, [0, 1.6, 0])
        xo = np.linalg.solve(LA, LB); Qm = LA.T @ LA
        cs = contours(ax, lambda x, y: lasso_f(np.array([x, y]), LAMB), [lasso_f(ST, LAMB) + d for d in (0.05, 0.2, 0.5, 1.0, 1.7, 2.6)], (-0.6, 2.6, -1.0, 1.9), N=70)
        zl = DashedLine(ax.c2p(-0.6, 0), ax.c2p(2.6, 0), color=DIM, stroke_width=2)
        self.play(Create(cs), Create(zl), run_time=1.2)
        self.add(Dot(ax.c2p(*ST), radius=0.11, color=MINT))
        px = Dot(ax.c2p(0, 0), radius=0.12, color=SKY); pz = Dot(ax.c2p(0, 0), radius=0.12, color=PINK); self.add(px, pz)
        self.say(L("ρ = 1. Xanh dương: x. Hồng: z. Xanh lá: nghiệm lasso.", "ρ = 1. Blue: x. Pink: z. Green: the lasso solution."), wait=False)
        sx, sz = [], []
        for k in range(1, 16):
            r = R[k - 1]; a = Line(px.get_center(), ax.c2p(*r["x"]), color=SKY, stroke_width=3.5); c_ = Line(pz.get_center(), ax.c2p(*r["z"]), color=PINK, stroke_width=3.5)
            sx.append(a); sz.append(c_)
            self.play(Create(a), Create(c_), px.animate.move_to(ax.c2p(*r["x"])), pz.animate.move_to(ax.c2p(*r["z"])), run_time=0.6 if k < 7 else 0.35)
            self.readout(["k = %2d   x = %s" % (k, vec(r["x"], 3)), ("        z = %s" % vec(r["z"], 3), PINK), ("‖x − z‖ = %s   ρ‖Δz‖ = %s" % (sci(r["r"]), sci(max(r["s"], 1e-16))), MINT)], color=SKY, size=22)
            self.wait(0.45 if k < 7 else 0.25)
        self.say(L("z luôn có z₂ = 0 chính xác (từ bước %d), còn x tiến dần về z. Cả hai phần dư → 0." % (ZK + 1),
                   "z has z₂ = 0 exactly (from step %d on), while x creeps toward z. Both residuals → 0." % (ZK + 1)), hold=4.5)
        self.readout(["k = 60   z = %s" % vec(R[-1]["z"], 6), ("‖z − z*‖ < 10⁻⁸  ✓", MINT)], color=PINK, size=23)
        self.wait(1.5)
        # contrast
        self.stage(4)
        rows = [("   ρ     số bước tới ‖z − z*‖ < 10⁻⁶" if LANG == "vi" else "   ρ     steps to ‖z − z*‖ < 10⁻⁶", WHITE)] + [("%5s    %d" % (nf(rho, 1) if rho < 1 else str(rho), RH[rho]), MINT if rho == 1 else SKY) for rho in (0.1, 0.3, 1, 3, 10)]
        self.readout(rows, size=24)
        self.say(L("ρ là tham số duy nhất. ρ nhỏ: z hầu như không bị kéo về x. ρ lớn: x, z dính nhau nhưng tiến chậm về nghiệm.",
                   "ρ is the only knob. Small ρ: z is barely tied to x. Large ρ: x and z stick together but crawl toward the answer."), hold=6.0)
        self.say(L("Ở đây ρ = 1 cần %d bước, ρ = 0,1 cần %d, ρ = 10 cần %d. ADMM luôn hội tụ, chỉ nhanh hay chậm." % (RH[1], RH[0.1], RH[10]),
                   "Here ρ = 1 needs %d steps, ρ = 0.1 needs %d, ρ = 10 needs %d. ADMM always converges; ρ only sets the speed." % (RH[1], RH[0.1], RH[10])), hold=5.0)
        self.takeaway([L("ADMM tách mục tiêu thành hai phần dễ, nối bằng ràng buộc x = z.", "ADMM splits the objective into two easy parts linked by x = z."),
                       L("Mỗi vòng: một bước ridge, một bước co ngưỡng, một bước cập nhật giá u.", "Each round: a ridge step, a thresholding step, a price update u."),
                       L("Hội tụ với mọi ρ > 0; ρ quyết định tốc độ.", "Converges for every ρ > 0; ρ sets the speed.")])
