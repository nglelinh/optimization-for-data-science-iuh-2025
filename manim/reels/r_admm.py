from rl import *
from o3lib import LA, LB, soft, lasso_star, lasso_f, admm
# Bài 21-03: ADMM cho lasso, dạng chia tỉ lệ (bài viết β, α, w; reel viết x, z, u)
LAMB = .8
ST = lasso_star(LAMB)
def admm_full(rho, n):
    M = np.linalg.inv(LA.T @ LA + rho * np.eye(2)); Atb = LA.T @ LB; z = np.zeros(2); u = np.zeros(2); rec = []
    for k in range(n):
        x = M @ (Atb + rho * (z - u)); zo = z.copy(); uo = u.copy(); z = soft(x + u, LAMB / rho); u = u + x - z
        rec.append(dict(x=x.copy(), v=x + uo, z=z.copy(), u=u.copy(), r=np.linalg.norm(x - z), s=rho * np.linalg.norm(z - zo)))
    return rec
R = admm_full(1.0, 60)
xs_, zs_ = admm(LAMB, 1, 60); assert all(np.allclose(R[k]["z"], zs_[k + 1]) for k in range(60))
assert np.linalg.norm(R[-1]["z"] - ST) < 1e-8 and R[-1]["z"][1] == 0.0
MR = LA.T @ LA + np.eye(2); ATB = LA.T @ LB
assert np.allclose(MR, [[3.72, 1.56], [1.56, 2.7]]) and np.allclose(ATB, [3.72, 2.46])
# vòng 1 và 2 tính tay
assert np.allclose(R[0]["x"], [0.8155, 0.4399], atol=1e-4) and np.allclose(R[0]["z"], [0.0155, 0], atol=1e-4) and np.allclose(R[0]["u"], [0.8, 0.4399], atol=1e-4)
assert np.isclose(R[0]["x"][0] - 0.8, R[0]["z"][0]) and R[0]["x"][1] < 0.8
assert np.allclose(R[1]["v"], [1.4274, 0.8256], atol=1e-4) and np.allclose(R[1]["z"], [0.6274, 0.0256], atol=1e-4) and np.allclose(R[1]["u"], [0.8, 0.8])
# dạng chia tỉ lệ: yᵀr + ρ/2‖r‖² = ρ/2‖r + u‖² − ρ/2‖u‖², u = y/ρ
_g = np.random.default_rng(1)
for _ in range(5):
    r_, y_, rho_ = _g.normal(size=2), _g.normal(size=2), _g.uniform(0.1, 5); u_ = y_ / rho_
    assert np.isclose(y_ @ r_ + rho_ / 2 * r_ @ r_, rho_ / 2 * (r_ + u_) @ (r_ + u_) - rho_ / 2 * u_ @ u_)
# điều kiện tối ưu lasso đọc từ biến đối ngẫu: ρu* = Aᵀ(b − Az*) ∈ λ∂‖z*‖₁
US = R[-1]["u"]; GS = LA.T @ (LB - LA @ ST)
assert np.allclose(US, GS, atol=1e-8) and np.isclose(GS[0], LAMB) and abs(GS[1]) < LAMB and ST[0] > 0
assert abs(GS[1] - 0.7853) < 1e-4 and abs(ST[0] - 1.073529) < 1e-6
def iters(rho, tol=1e-6):
    rec = admm_full(rho, 5000); return next(k + 1 for k in range(5000) if np.linalg.norm(rec[k]["z"] - ST) < tol)
RH = {rho: iters(rho) for rho in (0.1, 0.3, 1, 3, 10)}
assert RH[1] < RH[0.1] and RH[1] < RH[10]
ZK = next(k for k in range(60) if all(R[j]["z"][1] == 0 for j in range(k, 60)))
VI = LANG == "vi"

def mtx(rows, color=WHITE, size=24):
    """ma trận nhỏ: lưới số + hai ngoặc vuông"""
    cells = VGroup(*[Text(s, font=MONO, font_size=size, color=color) for r in rows for s in r])
    g = cells.arrange_in_grid(rows=len(rows), cols=len(rows[0]), buff=(0.35, 0.12), col_alignments="r" * len(rows[0]))
    h = g.height + 0.16; l = g.get_left()[0] - 0.12; rr = g.get_right()[0] + 0.12; cy = g.get_center()[1]
    br = VGroup(*[VMobject(color=color, stroke_width=2.5).set_points_as_corners([[x0 + dx, cy + h / 2, 0], [x0, cy + h / 2, 0], [x0, cy - h / 2, 0], [x0 + dx, cy - h / 2, 0]]) for x0, dx in ((l, 0.12), (rr, -0.12))])
    return VGroup(g, br)

def eq_row(parts, size=24):
    """hàng gồm chữ và ma trận xếp ngang"""
    ms = [Text(p, font=MONO, font_size=size, color=WHITE) if isinstance(p, str) else p for p in parts]
    return VGroup(*ms).arrange(RIGHT, buff=0.2)

class Admm(Reel):
    def construct(self):
        self.title(L("ADMM: tách bài toán,\nrồi kéo hai nửa lại gần nhau", "ADMM: split the problem,\nthen pull the halves together"))
        # ---- stage 1
        self.stage(1)
        self.readout(["min ½‖Ax − b‖² + λ‖x‖₁,   λ = 0,8" if VI else "min ½‖Ax − b‖² + λ‖x‖₁,   λ = 0.8", ("⇕", DIM), "min ½‖Ax − b‖² + λ‖z‖₁   s.t.  x = z"], color=WHITE, size=25, y=2.8)
        self.say(L("Lasso khó vì có cả phần bình phương lẫn phần ℓ₁ không trơn. ADMM nhân đôi biến: x giữ phần bình phương, z giữ phần ℓ₁, rồi buộc x = z.",
                   "Lasso is awkward because it mixes a squared part and a non-smooth ℓ₁ part. ADMM duplicates the variable: x takes the squares, z the ℓ₁, with x = z."), hold=8.5)
        data = eq_row(["A =", mtx([[nf(1.6, 1), nf(0.7, 1)], [nf(0.4, 1), nf(1.1, 1)]], SKY), "   b =", mtx([[nf(2.1, 1)], [nf(0.9, 1)]], SKY)]).move_to([0, 0.6, 0])
        self.play(FadeIn(data), run_time=0.5)
        self.say(L("Số liệu cụ thể: A là ma trận 2×2 này, b = (2,1; 0,9), λ = 0,8. Bài 21-03 viết β, α, w; ở đây gọi là x, z, u.",
                   "Concrete data: A is this 2×2 matrix, b = (2.1, 0.9), λ = 0.8. Lesson 21-03 writes β, α, w; here they are x, z, u."), hold=8.5)
        # ---- stage 2: dạng chia tỉ lệ
        self.stage(2); self.play(FadeOut(data), run_time=0.3)
        self.readout(["L_ρ(x, z, y) = f(x) + g(z)", "  + yᵀ(x − z) + (ρ/2)‖x − z‖²"], color=SUN, size=25, y=2.8)
        self.say(L("Bắt đầu từ Lagrange tăng cường: f là phần bình phương, g = λ‖·‖₁, y là nhân tử của x = z, cộng thêm phạt (ρ/2)‖x − z‖².",
                   "Start from the augmented Lagrangian: f is the squared part, g = λ‖·‖₁, y is the multiplier for x = z, plus the penalty (ρ/2)‖x − z‖²."), hold=9.5)
        self.readout(["L_ρ(x, z, y) = f(x) + g(z)", "  + yᵀ(x − z) + (ρ/2)‖x − z‖²", ("u = y/ρ:", ORANGE), ("  = f(x) + g(z) + (ρ/2)‖x − z + u‖² − (ρ/2)‖u‖²", ORANGE)], color=SUN, size=24, y=2.6)
        self.say(L("Dạng chia tỉ lệ: đặt u = y/ρ rồi gom thành bình phương. Số hạng tuyến tính biến mất, chỉ còn (ρ/2)‖x − z + u‖². Công thức gọn hẳn.",
                   "The scaled form: set u = y/ρ and complete the square. The linear term disappears, leaving (ρ/2)‖x − z + u‖². Much tidier."), hold=10.0)
        self.readout([("x⁺ = argmin  ½‖Ax − b‖² + (ρ/2)‖x − z + u‖²", SKY), ("z⁺ = argmin  λ‖z‖₁ + (ρ/2)‖x⁺ − z + u‖²", PINK), ("u⁺ = u + x⁺ − z⁺", ORANGE)], size=23, y=2.6)
        self.say(L("ADMM cực tiểu hoá lần lượt theo x, rồi theo z, rồi cập nhật u bằng phần lệch. Mỗi bước con đều dễ.",
                   "ADMM minimizes over x, then over z, then updates u with the mismatch. Each sub-step is easy."), hold=8.0)
        self.readout([("x⁺ = (AᵀA + ρI)⁻¹(Aᵀb + ρ(z − u))", SKY), ("z⁺ = soft(x⁺ + u, λ/ρ)", PINK), ("u⁺ = u + x⁺ − z⁺", ORANGE)], size=24, y=2.6)
        self.say(L("Bước x: đạo hàm bằng 0 cho hệ tuyến tính kiểu ridge. Bước z: co ngưỡng mềm từng toạ độ, ngưỡng λ/ρ. Bước u: cộng dồn x − z.",
                   "x-step: setting the gradient to 0 gives a ridge-type linear system. z-step: soft-threshold each coordinate at λ/ρ. u-step: accumulate x − z."), hold=10.0)
        self.say(L("u là giá (đã chia ρ) của ràng buộc x = z: còn lệch thì giá còn tăng, kéo hai bên lại gần nhau.",
                   "u is the (scaled) price of x = z: while they still differ the price keeps rising and pulls them together."), hold=7.5)
        # ---- stage 3: tính tay rồi chạy
        self.stage(3); self.clear_ro()
        m1 = eq_row(["AᵀA + ρI =", mtx([[nf(3.72), nf(1.56)], [nf(1.56), nf(2.70)]], SKY)], 24)
        m2 = Text("Aᵀb = " + vec(ATB, 2), font=MONO, font_size=24, color=SKY)
        top = VGroup(m1, m2).arrange(DOWN, buff=0.3).move_to([0, 3.2, 0])
        self.play(FadeIn(top), run_time=0.5)
        self.say(L("Tính tay vòng đầu với ρ = 1, xuất phát z = u = 0. Ma trận AᵀA + I và vectơ Aᵀb tính một lần, dùng cho mọi vòng.",
                   "Work the first round by hand with ρ = 1, starting from z = u = 0. The matrix AᵀA + I and the vector Aᵀb are computed once and reused."), hold=9.0)
        def hand(k):
            r = R[k - 1]; up = R[k - 2]["u"] if k > 1 else np.zeros(2)
            return ["k = %d:  x = %s" % (k, vec(r["x"], 3)), ("x + u = %s" % vec(r["v"], 3), DIM),
                    ("z = soft(·; 0,8) = %s" % vec(r["z"], 3) if VI else "z = soft(·, 0.8) = %s" % vec(r["z"], 3), PINK),
                    ("u = %s + x − z = %s" % (vec(up, 3), vec(r["u"], 3)), ORANGE)]
        self.readout(hand(1), color=SKY, size=23, y=1.0)
        self.say(L("Vòng 1: giải hệ được x = (0,816; 0,440). Co ngưỡng 0,8: toạ độ đầu còn 0,816 − 0,8 = 0,016, toạ độ sau nhỏ hơn 0,8 nên về đúng 0.",
                   "Round 1: solving gives x = (0.816, 0.440). Threshold at 0.8: the first coordinate keeps 0.816 − 0.8 = 0.016, the second is below 0.8, so it becomes exactly 0."), hold=11.0)
        self.say(L("Phần lệch x − z dồn vào u = (0,8; 0,440). Đây chính là giá phải trả cho việc x và z chưa khớp.",
                   "The mismatch x − z goes into u = (0.8, 0.440). That is the price for x and z not agreeing yet."), hold=7.5)
        self.readout(hand(2), color=SKY, size=23, y=1.0)
        self.say(L("Vòng 2: u kéo z lên: x + u = (1,427; 0,826), co ngưỡng cho z = (0,627; 0,026). Toạ độ thứ hai lóe lên một chút rồi sẽ lại về 0.",
                   "Round 2: u pulls z up: x + u = (1.427, 0.826), thresholding gives z = (0.627, 0.026). The second coordinate flickers up a little, then returns to 0."), hold=10.0)
        self.play(FadeOut(top), run_time=0.3); self.clear_ro()
        ax = plain_axes([-0.6, 2.6], [-1.0, 1.9], 7.2, 5.8, [0, 1.6, 0])
        cs = contours(ax, lambda x, y: lasso_f(np.array([x, y]), LAMB), [lasso_f(ST, LAMB) + d for d in (0.05, 0.2, 0.5, 1.0, 1.7, 2.6)], (-0.6, 2.6, -1.0, 1.9), N=70)
        zl = DashedLine(ax.c2p(-0.6, 0), ax.c2p(2.6, 0), color=DIM, stroke_width=2)
        self.play(Create(cs), Create(zl), run_time=1.2)
        self.add(Dot(ax.c2p(*ST), radius=0.11, color=MINT))
        px = Dot(ax.c2p(0, 0), radius=0.12, color=SKY); pz = Dot(ax.c2p(0, 0), radius=0.12, color=PINK); self.add(px, pz)
        self.say(L("Giờ cho chạy. Xanh dương: x. Hồng: z. Xanh lá: nghiệm lasso. Đường đứt: trục z₂ = 0.", "Now let it run. Blue: x. Pink: z. Green: the lasso solution. Dashed: the axis z₂ = 0."), wait=False)
        for k in range(1, 16):
            r = R[k - 1]; a = Line(px.get_center(), ax.c2p(*r["x"]), color=SKY, stroke_width=3.5); c_ = Line(pz.get_center(), ax.c2p(*r["z"]), color=PINK, stroke_width=3.5)
            self.play(Create(a), Create(c_), px.animate.move_to(ax.c2p(*r["x"])), pz.animate.move_to(ax.c2p(*r["z"])), run_time=0.6 if k < 7 else 0.35)
            self.readout(["k = %2d   x = %s" % (k, vec(r["x"], 3)), ("        z = %s" % vec(r["z"], 3), PINK), ("r = ‖x − z‖ = %s   s = ρ‖Δz‖ = %s" % (sci(r["r"]), sci(max(r["s"], 1e-16))), MINT)], color=SKY, size=22)
            self.wait(0.55 if k < 7 else 0.3)
        self.say(L("Hai phần dư để dừng: r = ‖x − z‖ là phần dư gốc (ràng buộc x = z), s = ρ‖zₖ − zₖ₋₁‖ là phần dư đối ngẫu. Cả hai đều về 0.",
                   "Two residuals decide when to stop: r = ‖x − z‖ is the primal residual (the constraint x = z), s = ρ‖zₖ − zₖ₋₁‖ is the dual residual. Both go to 0."), hold=10.0)
        self.say(L("z luôn có z₂ = 0 chính xác (từ bước %d), còn x tiến dần về z. Đó là lợi thế của bước co ngưỡng: số 0 là 0 thật." % (ZK + 1),
                   "z has z₂ = 0 exactly (from step %d on), while x creeps toward z. That is the perk of thresholding: a zero is a true zero." % (ZK + 1)), hold=8.0)
        self.readout(["k = 60   z* = %s" % vec(R[-1]["z"], 6), ("ρu* = Aᵀ(b − Az*) = %s" % vec(GS, 3), ORANGE),
                      ("z₁ > 0  ⇒  ρu₁ = λ = %s  ✓" % nf(0.8, 1), MINT), ("|ρu₂| = %s ≤ λ  ⇒  z₂ = 0  ✓" % nf(abs(GS[1]), 3), MINT)], color=PINK, size=22)
        self.say(L("Kiểm tra tối ưu bằng chính biến đối ngẫu: ρu* = Aᵀ(b − Az*) = (0,8; 0,785). Toạ độ khác 0 có đúng bằng λ, toạ độ bằng 0 có trị tuyệt đối ≤ λ. Đúng điều kiện tối ưu của lasso.",
                   "Check optimality with the dual variable itself: ρu* = Aᵀ(b − Az*) = (0.8, 0.785). The nonzero coordinate gets exactly λ, the zero one has absolute value ≤ λ. That is exactly lasso optimality."), hold=12.0)
        # ---- stage 4
        self.stage(4)
        rows = [("   ρ     số bước tới ‖z − z*‖ < 10⁻⁶" if VI else "   ρ     steps to ‖z − z*‖ < 10⁻⁶", WHITE)] + [("%5s    %d" % (nf(rho, 1) if rho < 1 else str(rho), RH[rho]), MINT if rho == 1 else SKY) for rho in (0.1, 0.3, 1, 3, 10)]
        self.readout(rows, size=24)
        self.say(L("ρ là tham số duy nhất. ρ nhỏ: z hầu như không bị kéo về x. ρ lớn: x, z dính nhau ngay nhưng tiến rất chậm về nghiệm.",
                   "ρ is the only knob. Small ρ: z is barely tied to x. Large ρ: x and z stick together at once but crawl toward the answer."), hold=8.5)
        self.say(L("Ở đây ρ = 1 cần %d bước, ρ = 0,1 cần %d, ρ = 10 cần %d. ADMM hội tụ với mọi ρ > 0, ρ chỉ quyết định nhanh hay chậm." % (RH[1], RH[0.1], RH[10]),
                   "Here ρ = 1 needs %d steps, ρ = 0.1 needs %d, ρ = 10 needs %d. ADMM converges for every ρ > 0; ρ only sets the speed." % (RH[1], RH[0.1], RH[10])), hold=9.0)
        self.readout([("chi phí mỗi vòng" if VI else "cost per round", WHITE), ("Cholesky của AᵀA + ρI: một lần, O(p³)" if VI else "Cholesky of AᵀA + ρI: once, O(p³)", SKY), ("mỗi bước x sau đó: O(p²)" if VI else "each x-step afterwards: O(p²)", SKY), ("bước z, u: O(p)" if VI else "z- and u-steps: O(p)", PINK)], size=24)
        self.say(L("Về chi phí: ma trận AᵀA + ρI không đổi, nên phân rã Cholesky một lần với O(p³), sau đó mỗi vòng chỉ O(p²). Đổi ρ giữa chừng thì phải phân rã lại.",
                   "On cost: AᵀA + ρI never changes, so factor it once with Cholesky in O(p³); after that each round costs O(p²). Changing ρ midway means refactoring."), hold=10.0)
        self.takeaway([L("ADMM tách mục tiêu thành hai phần dễ, nối bằng ràng buộc x = z.", "ADMM splits the objective into two easy parts linked by x = z."),
                       L("Dạng chia tỉ lệ: x ← ridge, z ← soft(x + u, λ/ρ), u ← u + x − z.", "Scaled form: x ← ridge, z ← soft(x + u, λ/ρ), u ← u + x − z."),
                       L("Dừng khi phần dư gốc r và đối ngẫu s đều nhỏ; ρu* kiểm tra tối ưu.", "Stop when the primal residual r and dual residual s are small; ρu* certifies optimality."),
                       L("Hội tụ với mọi ρ > 0; ρ quyết định tốc độ.", "Converges for every ρ > 0; ρ sets the speed.")], tail=4.0)
