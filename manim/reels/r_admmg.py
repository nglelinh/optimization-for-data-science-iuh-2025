from rl import *
# Bài 20-04-01: ADMM tổng quát  min f(x) + g(z)  s.t.  Ax + Bz = c, áp vào bài đồng thuận (consensus)
A_ = np.array([1., 2, 4]); B_ = np.array([-2., 1, 3]); ZS = (A_ @ B_) / A_.sum()       # fᵢ(x) = ½aᵢ(x − bᵢ)²
assert np.isclose(ZS, 12 / 7)
def admm(rho, n):
    z = 0.; u = np.zeros(3); H = []
    for _ in range(n):
        x = (A_ * B_ - u + rho * z) / (A_ + rho)                 # x-update: argmin L_ρ(x, z, u), tách theo từng i
        zp = z; z = np.mean(x + u / rho)                         # z-update
        u = u + rho * (x - z)                                    # u-update (dạng không co giãn như trong bài)
        H.append(dict(x=x.copy(), z=z, u=u.copy(), r=np.linalg.norm(x - z), s=rho * 3 ** .5 * abs(z - zp)))
    return H
# kiểm tra x-update bằng lưới
def Lx(x, i, z, u, rho): return 0.5 * A_[i] * (x - B_[i]) ** 2 + u * (x - z) + rho / 2 * (x - z) ** 2
gx = np.linspace(-5, 5, 200001)
for i in range(3): assert abs(gx[np.argmin(Lx(gx, i, 0.7, 0.3, 1.0))] - (A_[i] * B_[i] - 0.3 + 0.7) / (A_[i] + 1)) < 1e-4
H1 = admm(1.0, 60)
assert np.allclose(H1[0]["x"], [-1, 2 / 3, 2.4]) and np.isclose(H1[0]["z"], 0.6889, atol=1e-4)
assert abs(H1[-1]["z"] - ZS) < 1e-7 and np.allclose(H1[-1]["u"], A_ * (B_ - ZS), atol=1e-6) and abs(H1[-1]["u"].sum()) < 1e-9
def iters(rho): H = admm(rho, 3000); return next(k + 1 for k, h in enumerate(H) if abs(h["z"] - ZS) < 1e-6 and h["r"] < 1e-6)
RH = (0.1, 1, 3, 10); IT = [iters(r) for r in RH]; assert IT == [407, 46, 25, 68], IT
avg = B_.mean(); assert np.isclose(avg, 2 / 3)
COL = (SKY, MINT, PINK)

class AdmmG(Reel):
    def construct(self):
        self.title(L("ADMM tổng quát:\ntách bài toán làm đôi", "General ADMM:\nsplitting a problem in two"))
        # ---- stage 1
        self.stage(1)
        self.readout([("min f(x) + g(z)   s.t.  Ax + Bz = c" if LANG == "en" else "min f(x) + g(z)   với  Ax + Bz = c", SUN)], size=26)
        self.say(L("Bài 20-04-01: ADMM giải bài toán có hai khối biến x và z, hàm mục tiêu tách thành f(x) + g(z), nối với nhau bằng ràng buộc tuyến tính Ax + Bz = c.",
                   "Lesson 20-04-01: ADMM solves a problem with two blocks of variables x and z, whose objective splits as f(x) + g(z), coupled by a linear constraint Ax + Bz = c."), hold=9.5)
        lag = VGroup(*[Text(s_, font=MONO, font_size=25, color=c_) for s_, c_ in (("L_ρ(x, z, u) = f(x) + g(z)", WHITE), ("  + uᵀ(Ax + Bz − c)", SKY), ("  + (ρ/2)‖Ax + Bz − c‖²", MINT))]).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to([0, 2.4, 0])
        self.play(FadeIn(lag, lag_ratio=0.2), run_time=1.0)
        self.say(L("Công cụ chính là Lagrangian tăng cường: thêm nhân tử u cho ràng buộc, cộng một số hạng phạt bậc hai với hệ số ρ > 0.",
                   "The main tool is the augmented Lagrangian: add a multiplier u for the constraint, plus a quadratic penalty with weight ρ > 0."), hold=8.0)
        mm = Text(L("phương pháp nhân tử:\n(x, z) ← argmin L_ρ cùng lúc", "method of multipliers:\n(x, z) ← argmin L_ρ jointly")[LANG], font=MONO, font_size=24, color=ORANGE, line_spacing=1.2).move_to([0, 0.2, 0])
        self.play(FadeIn(mm), run_time=0.4)
        self.say(L("Phương pháp nhân tử cực tiểu L_ρ theo x và z cùng lúc. Nhưng số hạng phạt ‖Ax + Bz − c‖² trộn x với z, nên bài con khó như bài gốc.",
                   "The method of multipliers minimizes L_ρ over x and z jointly. But the penalty ‖Ax + Bz − c‖² mixes x with z, so the subproblem is as hard as the original."), hold=9.0)
        # ---- stage 2
        self.stage(2)
        upd = VGroup(*[Text(s_, font=MONO, font_size=24, color=c_) for s_, c_ in (("x⁺ = argmin_x L_ρ(x, z, u)", SKY), ("z⁺ = argmin_z L_ρ(x⁺, z, u)", MINT), ("u⁺ = u + ρ(Ax⁺ + Bz⁺ − c)", SUN))]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, 0.0, 0])
        self.play(FadeOut(mm), FadeIn(upd, lag_ratio=0.2), run_time=0.9)
        self.say(L("ADMM đổi một bài khó thành hai bài dễ, làm lần lượt: cực tiểu theo x với z cố định, rồi theo z với x vừa tính, rồi cập nhật u.",
                   "ADMM turns one hard problem into two easy ones, done in turn: minimize over x with z fixed, then over z with the new x, then update u."), hold=8.5)
        self.say(L("Bước u là đi lên theo gradient của bài đối ngẫu, với bước đúng bằng ρ. u giống như giá phạt cho việc vi phạm ràng buộc.",
                   "The u step is gradient ascent on the dual problem, with step size exactly ρ. u acts like a price for violating the constraint."), hold=8.0)
        self.wipe()
        ex = VGroup(*[Text(s_, font=MONO, font_size=23, color=c_) for s_, c_ in (
            ("đồng thuận: min Σ ½aᵢ(xᵢ − bᵢ)²" if LANG == "vi" else "consensus: min Σ ½aᵢ(xᵢ − bᵢ)²", WHITE), ("           với  xᵢ = z,  i = 1, 2, 3" if LANG == "vi" else "           s.t.  xᵢ = z,  i = 1, 2, 3", WHITE),
            ("a = (1; 2; 4),  b = (−2; 1; 3)" if LANG == "vi" else "a = (1, 2, 4),  b = (−2, 1, 3)", WHITE),
            ("xᵢ⁺ = (aᵢbᵢ − uᵢ + ρz) / (aᵢ + ρ)", SKY), ("z⁺ = trung bình(xᵢ⁺ + uᵢ/ρ)" if LANG == "vi" else "z⁺ = mean(xᵢ⁺ + uᵢ/ρ)", MINT), ("uᵢ⁺ = uᵢ + ρ(xᵢ⁺ − z⁺)", SUN))]).arrange(DOWN, aligned_edge=LEFT, buff=0.28).move_to([0, 1.3, 0])
        self.play(FadeIn(ex, lag_ratio=0.15), run_time=1.0)
        self.say(L("Ví dụ cụ thể: ba máy, máy i giữ hàm ½aᵢ(x − bᵢ)². Mỗi máy có biến riêng xᵢ, và cả ba phải đồng ý một giá trị chung z. Ở đây A = I, B = −1, c = 0.",
                   "A concrete example: three machines, machine i holds ½aᵢ(x − bᵢ)². Each has its own variable xᵢ, and all three must agree on a common value z. Here A = I, B = −1, c = 0."), hold=10.0)
        self.say(L("Bước x tách thành ba bài nhỏ, mỗi máy tự giải, có công thức đóng. Bước z chỉ là lấy trung bình. Rồi mỗi máy chỉnh giá uᵢ của mình.",
                   "The x step splits into three small problems, each machine solving its own, in closed form. The z step is just an average. Then each machine adjusts its price uᵢ."), hold=9.0)
        # ---- stage 3
        self.stage(3); self.wipe()
        nl = NumberLine(x_range=[-2.5, 3.5, 1], length=7.6, color=DIM, include_numbers=False).move_to([0, 2.0, 0])
        labs = VGroup(*[Text(("−" if v < 0 else "") + str(abs(v)), font=MONO, font_size=18, color=DIM).next_to(nl.n2p(v), DOWN, buff=0.15) for v in range(-2, 4)])
        bm = VGroup(*[Triangle(color=c, fill_opacity=1).scale(0.12).rotate(PI).move_to(nl.n2p(b) + UP * 0.55) for b, c in zip(B_, COL)])
        bl = VGroup(*[Text("b%s" % s_, font=MONO, font_size=18, color=c).next_to(m, UP, buff=0.08) for s_, m, c in zip("₁₂₃", bm, COL)])
        zst = DashedLine(nl.n2p(ZS) + UP * 1.4, nl.n2p(ZS) + DOWN * 0.6, color=SUN, stroke_width=2.5)
        zl = Text("z* = 12/7", font=MONO, font_size=20, color=SUN).next_to(zst, UP, buff=0.08)
        self.play(Create(nl), FadeIn(labs), FadeIn(bm), FadeIn(bl), Create(zst), FadeIn(zl), run_time=0.8)
        self.say(L("Nghiệm đúng là trung bình có trọng số: z* = Σaᵢbᵢ / Σaᵢ = 12/7 ≈ 1,714. Tam giác là bᵢ, chỗ mỗi máy muốn nhất.",
                   "The true answer is the weighted mean: z* = Σaᵢbᵢ / Σaᵢ = 12/7 ≈ 1.714. The triangles are the bᵢ, where each machine would like to be."), hold=8.5)
        xd = VGroup(*[Dot(nl.n2p(0) + DOWN * 0.0, radius=0.11, color=c) for c in COL]); zd = Dot(nl.n2p(0), radius=0.08, color=WHITE)
        for i, d in enumerate(xd): d.shift(UP * (0.25 * (i - 1)))
        self.add(xd, zd)
        def ro(k):
            h = H1[k - 1]
            self.readout([("ρ = 1,  k = %d" % k if LANG == "vi" else "ρ = 1,  k = %d" % k, WHITE), ("x = %s" % vec(h["x"], 3), SKY), ("z = %s,   u = %s" % (nf(h["z"], 3), vec(h["u"], 2)), SUN), ("‖x − z‖ = %s" % (nf(h["r"], 3) if h["r"] > 1e-3 else sci(h["r"], 1)), MINT)], size=21)
        for k in range(1, 13):
            h = H1[k - 1]
            self.play(*[d.animate.move_to(nl.n2p(h["x"][i]) + UP * (0.25 * (i - 1))) for i, d in enumerate(xd)], zd.animate.move_to(nl.n2p(h["z"])), run_time=0.45 if k > 2 else 0.8)
            ro(k)
            if k == 1:
                self.say(L("Bắt đầu z = 0, u = 0. Bước 1: mỗi máy kéo xᵢ về phía bᵢ của mình, nhưng phạt ρ giữ chúng gần z. Lấy trung bình được z = 0,689.",
                           "Start with z = 0, u = 0. Step 1: each machine pulls xᵢ toward its own bᵢ, but the ρ penalty keeps it near z. Averaging gives z = 0.689."), hold=9.0)
            elif k == 2:
                self.say(L("Máy nằm dưới z (xanh dương) nhận giá u âm, máy nằm trên (hồng) nhận u dương. Giá này đẩy các máy về gần nhau ở vòng sau.",
                           "The machine below z (blue) gets a negative price u, the one above (pink) a positive one. These prices push the machines together next round."), hold=8.5)
            else: self.wait(0.25)
        h = H1[-1]
        self.play(*[d.animate.move_to(nl.n2p(h["x"][i]) + UP * (0.25 * (i - 1))) for i, d in enumerate(xd)], zd.animate.move_to(nl.n2p(h["z"])), run_time=0.6)
        ro(len(H1))
        self.say(L("Sau 46 vòng, cả ba xᵢ và z trùng nhau ở 12/7. Giá cuối uᵢ = aᵢ(bᵢ − z*) có tổng bằng 0: chính là nhân tử Lagrange của bài toán.",
                   "After 46 rounds, all three xᵢ and z coincide at 12/7. The final prices uᵢ = aᵢ(bᵢ − z*) sum to 0: they are exactly the Lagrange multipliers of the problem."), hold=9.5)
        self.say(L("Để ý: nếu chỉ lấy trung bình thường của bᵢ thì được 2/3, sai. ADMM tự tìm ra trọng số aᵢ qua giá u, mà không máy nào phải gửi hàm của mình đi.",
                   "Note: a plain average of the bᵢ would give 2/3, which is wrong. ADMM finds the weights aᵢ through the prices u, without any machine sending out its function."), hold=9.5)
        # ---- stage 4
        self.stage(4); self.wipe()
        bars = VGroup(); mx = max(IT)
        for j, (r, n) in enumerate(zip(RH, IT)):
            bh = 4.0 * n / mx; bx = Rectangle(width=1.1, height=bh, stroke_width=0, fill_color=MINT if n == min(IT) else SKY, fill_opacity=0.85).move_to([-2.7 + 1.8 * j, -1.6 + bh / 2, 0])
            t1 = Text(str(n), font=MONO, font_size=24, color=WHITE).next_to(bx, UP, buff=0.1); t2 = Text("ρ = " + nf(r, 1 if r < 1 else 0), font=MONO, font_size=22, color=DIM).next_to(bx, DOWN, buff=0.15)
            bars.add(VGroup(bx, t1, t2))
        hd = Text(L("số vòng tới sai số 10⁻⁶", "rounds to 10⁻⁶ accuracy")[LANG], font=FONT, font_size=25, color=SUN).move_to([0, 3.7, 0])
        self.play(FadeIn(hd), FadeIn(bars, lag_ratio=0.2), run_time=1.2)
        self.say(L("ADMM hội tụ với mọi ρ > 0, nhưng tốc độ phụ thuộc ρ. ρ = 0,1 cần 407 vòng, ρ = 3 chỉ 25 vòng, còn ρ = 10 lại tăng lên 68.",
                   "ADMM converges for every ρ > 0, but the speed depends on ρ. ρ = 0.1 needs 407 rounds, ρ = 3 only 25, and ρ = 10 goes back up to 68."), hold=9.0)
        self.say(L("ρ nhỏ: phạt yếu, các máy lâu đồng ý, phần dư ‖x − z‖ giảm chậm. ρ lớn: bị ép đồng ý sớm nhưng z nhích rất chậm. Thực tế người ta chỉnh ρ theo hai phần dư.",
                   "Small ρ: a weak penalty, machines take long to agree, the residual ‖x − z‖ shrinks slowly. Large ρ: forced to agree early but z creeps slowly. In practice ρ is tuned from the two residuals."), hold=10.0)
        self.say(L("Cùng khung này cho bài chia sẻ (sharing), lasso, hay ràng buộc tập: chỉ cần f và g dễ cực tiểu riêng lẻ, ví dụ có toán tử prox gọn.",
                   "The same template covers sharing problems, the lasso, or set constraints: all it needs is that f and g are easy to minimize separately, e.g. with a simple prox."), hold=9.0)
        self.takeaway([L("Bài toán: min f(x) + g(z) với Ax + Bz = c.", "Problem: min f(x) + g(z) s.t. Ax + Bz = c."),
                       L("Cực tiểu L_ρ lần lượt theo x rồi z, sau đó u += ρ·phần dư.", "Minimize L_ρ over x then z in turn, then u += ρ·residual."),
                       L("Đồng thuận: mỗi máy tự giải, z là trung bình, u là giá.", "Consensus: each machine solves locally, z is an average, u is a price."),
                       L("Hội tụ với mọi ρ > 0; ρ quyết định tốc độ.", "Converges for any ρ > 0; ρ sets the speed.")], tail=4.0)
