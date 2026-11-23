from rl import *
# Bài 28-05: điều kiện Polyak–Łojasiewicz  ½‖∇F‖² ≥ μ(F − F*)
F = lambda x: x * x + 3 * np.sin(x) ** 2; dF = lambda x: 2 * x + 3 * np.sin(2 * x); d2F = lambda x: 2 + 6 * np.cos(2 * x)
XX = np.linspace(-30, 30, 3000001); XX = XX[np.abs(XX) > 1e-3]
RAT = dF(XX) ** 2 / (2 * F(XX)); MU = float(RAT.min()); XMU = float(abs(XX[RAT.argmin()]))
assert abs(MU - 0.1755) < 5e-4 and abs(XMU - 2.20) < 0.01 and MU > 1 / 32
assert np.isclose(d2F(0), 8) and np.isclose(d2F(np.pi / 2), -4)
LL = 8.0
xs = np.linspace(-4.5, 4.5, 9001); assert d2F(xs).max() <= LL + 1e-9 and d2F(xs).min() >= -4 - 1e-9
C1, C2 = np.arccos(-1 / 3) / 2, np.pi - np.arccos(-1 / 3) / 2          # F″ < 0 trên (C1, C2) + kπ
assert abs(C1 - 0.9553) < 1e-4 and abs(C2 - 2.1863) < 1e-4 and d2F(1.5) < 0 and d2F(0.9) > 0 and d2F(2.25) > 0 and d2F(4.2) < 0
# điểm tới hạn duy nhất là 0: dF đổi dấu đúng một lần
assert (np.diff(np.sign(dF(xs[np.abs(xs) > 1e-6]))) != 0).sum() == 1
# dây cung cắt dưới đồ thị: hàm không lồi
assert F((1.2 + 2.2) / 2) > (F(1.2) + F(2.2)) / 2
W = [4.0]
for _ in range(14): W.append(W[-1] - dF(W[-1]) / LL)
W = np.array(W); FW = F(W)
assert np.isclose(W[1], 2.629, atol=1e-3) and FW[8] < 0.2 and FW[10] < 1e-14
for k in range(10): assert FW[k + 1] <= (1 - MU / LL) * FW[k] + 1e-15        # tốc độ tuyến tính của định lý
BOUND = FW[0] * (1 - MU / LL) ** np.arange(15); assert np.all(FW <= BOUND + 1e-12)
# x⁴: lồi nhưng không PL (tỉ số 8x² → 0)
q = [1.0]
for _ in range(100): q.append(q[-1] - 0.1 * 4 * q[-1] ** 3)
Q4 = np.array(q) ** 4; assert 7e-4 < Q4[40] < 9e-4 and Q4[100] > 1e-4
# bình phương tối thiểu quá tham số hóa, đúng đoạn mã của bài
rng = np.random.default_rng(0); n, d = 20, 50
X = rng.normal(size=(n, d)); w_star = rng.normal(size=d); y = X @ w_star
s = np.linalg.svd(X, compute_uv=False); MUL = s[-1] ** 2 / n; LLS = s[0] ** 2 / n
assert abs(MUL - 0.360) < 1e-3 and abs(LLS - 6.611) < 1e-3
FL = lambda w: np.sum((X @ w - y) ** 2) / (2 * n); GL = lambda w: X.T @ (X @ w - y) / n
def gd(w):
    out = [FL(w)]
    for _ in range(100): w = w - GL(w) / LLS; out.append(FL(w))
    return np.array(out), w
LA, WA = gd(np.zeros(d)); LB, WB = gd(rng.normal(size=d) * 2)
assert LA[100] < 1e-6 and LB[100] < 1e-4 and np.all(LA[1:] <= (1 - MUL / LLS) * LA[:-1] + 1e-15) and np.all(LB[1:] <= (1 - MUL / LLS) * LB[:-1] + 1e-15)
DW = np.linalg.norm(WA - WB); assert DW > 10, DW
for w in (WA, WB, np.zeros(d)): assert 0.5 * np.sum(GL(w) ** 2) >= MUL * FL(w) - 1e-12

class Pl(Reel):
    def construct(self):
        self.title(L("Điều kiện PL:\nhội tụ tuyến tính không cần lồi", "The PL condition:\nlinear convergence without convexity"))
        # ---- stage 1
        self.stage(1)
        self.readout([("½‖∇F(w)‖² ≥ μ (F(w) − F*)   với mọi w" if LANG == "vi" else "½‖∇F(w)‖² ≥ μ (F(w) − F*)   for all w", SUN)], size=25)
        self.say(L("Chương 06: GD hội tụ tuyến tính nếu hàm lồi mạnh. Nhưng hàm mất mát học sâu không lồi, vậy mà vẫn hay thấy hội tụ nhanh. Bài 28-05 giải thích bằng điều kiện PL.",
                   "Chapter 06: GD converges linearly if the function is strongly convex. Deep-learning losses are not convex, yet often converge fast. Lesson 28-05 explains this with the PL condition."), hold=10.0)
        VI = LANG == "vi"
        ch = VGroup(*[Text(s_, font=FONT, font_size=27, color=c_) for s_, c_ in (("lồi mạnh (hệ số m)" if VI else "strongly convex (modulus m)", SKY), ("⇓", DIM), ("PL với μ = m" if VI else "PL with μ = m", SUN), ("⇓", DIM), ("∇F(w) = 0  ⇒  F(w) = F*", MINT), ("⇓", DIM), ("GD hội tụ tuyến tính" if VI else "GD converges linearly", ORANGE))]).arrange(DOWN, buff=0.22).move_to([0, 1.0, 0])
        self.play(FadeIn(ch[0]), run_time=0.4); self.play(FadeIn(ch[1:3]), run_time=0.5)
        self.say(L("PL nói: ở đâu F còn cao hơn đáy, ở đó gradient không được quá nhỏ. Bình phương gradient luôn ít nhất bằng μ lần khoảng cách tới giá trị tối ưu.",
                   "PL says: wherever F is still above the bottom, the gradient cannot be too small. The squared gradient is always at least μ times the gap to the optimal value."), hold=9.0)
        self.play(FadeIn(ch[3:5]), run_time=0.5)
        self.say(L("Hệ quả ngay: nếu ∇F(w) = 0 thì F(w) = F*. Mọi điểm dừng đều là cực tiểu toàn cục, dù hàm không lồi.",
                   "Immediate consequence: if ∇F(w) = 0 then F(w) = F*. Every stationary point is a global minimum, even if the function is not convex."), hold=8.0)
        self.play(FadeIn(ch[5:]), run_time=0.5)
        self.say(L("Lồi mạnh kéo theo PL, nhưng PL yếu hơn nhiều: không đòi lồi, không đòi nghiệm duy nhất. Vậy mà vẫn đủ cho GD hội tụ tuyến tính.",
                   "Strong convexity implies PL, but PL is much weaker: no convexity, no unique solution required. Yet it is still enough for GD to converge linearly."), hold=9.0)
        # ---- stage 2
        self.stage(2); self.play(FadeOut(ch), run_time=0.3)
        ax = plain_axes([-4.5, 4.5], [0, 24], 7.6, 4.0, [0, 2.2, 0])
        cf = ax.plot(F, x_range=[-4.5, 4.5], color=SKY, stroke_width=4)
        segs = VGroup(*[ax.plot(F, x_range=[a, b], color=ORANGE, stroke_width=7) for a, b in ((-C2, -C1), (C1, C2), (-4.5, -C1 - np.pi), (C1 + np.pi, 4.5)) ])
        lf = Text("F(w) = w² + 3 sin² w", font=MONO, font_size=23, color=SKY).next_to(ax.c2p(-4.4, 22), RIGHT, buff=0)
        self.play(Create(ax), Create(cf), FadeIn(lf), run_time=1.0)
        self.say(L("Ví dụ của bài: F = w² + 3 sin² w. Cực tiểu F* = 0 tại w = 0, và đó là điểm dừng duy nhất.",
                   "The lesson's example: F = w² + 3 sin² w. The minimum F* = 0 is at w = 0, and it is the only stationary point."), hold=7.5)
        self.play(Create(segs), run_time=0.8)
        self.readout([("F″ = 2 + 6 cos 2w ∈ [−4; 8]" if LANG == "vi" else "F″ = 2 + 6 cos 2w ∈ [−4, 8]", ORANGE), ("đoạn cam: F″ < 0, cong xuống" if LANG == "vi" else "orange: F″ < 0, curving down", ORANGE)], size=24)
        self.say(L("Nhưng F″ = 2 + 6 cos 2w có lúc bằng −4: trên các đoạn cam đồ thị cong xuống, nên F không lồi, càng không lồi mạnh.",
                   "But F″ = 2 + 6 cos 2w goes as low as −4: on the orange pieces the graph curves down, so F is not convex, let alone strongly convex."), hold=8.5)
        ax2 = plain_axes([-4.5, 4.5], [0, 8.5], 7.6, 2.6, [0, -1.0, 0])
        rr = lambda x: dF(x) ** 2 / (2 * F(x)) if abs(x) > 1e-4 else 8.0
        cr = ax2.plot(rr, x_range=[-4.5, 4.5, 0.01], color=MINT, stroke_width=3.5)
        ml = DashedLine(ax2.c2p(-4.5, MU), ax2.c2p(4.5, MU), color=SUN, stroke_width=2.5)
        lr = Text("½F′² / F", font=MONO, font_size=21, color=MINT).next_to(ax2.c2p(-4.4, 8.3), RIGHT, buff=0)
        self.play(Create(ax2), Create(cr), Create(ml), FadeIn(lr), run_time=1.2)
        self.readout([("μ = min ½F′²/F ≈ %s  (tại |w| ≈ 2,2)" % nf(MU, 3) if LANG == "vi" else "μ = min ½F′²/F ≈ %s  (at |w| ≈ 2.2)" % nf(MU, 3), SUN), ("L = max F″ = 8" , WHITE)], size=24)
        self.say(L("Kiểm tra PL bằng số: vẽ tỉ số ½F′²/F. Nó không bao giờ chạm 0; nhỏ nhất khoảng %s ở |w| ≈ 2,2. Vậy F thỏa PL với μ ≈ %s." % (nf(MU, 3), nf(MU, 3)),
                   "Check PL numerically: plot the ratio ½F′²/F. It never touches 0; its minimum is about %s at |w| ≈ 2.2. So F satisfies PL with μ ≈ %s." % (nf(MU, 3), nf(MU, 3))), hold=9.5)
        # ---- stage 3
        self.stage(3)
        self.play(FadeOut(ax2), FadeOut(cr), FadeOut(ml), FadeOut(lr), run_time=0.4)
        d = Dot(ax.c2p(W[0], FW[0]), color=SUN, radius=0.1); self.add(d)
        self.readout([("F⁺ ≤ F − (1/2L)‖∇F‖²   (bổ đề giảm)" if LANG == "vi" else "F⁺ ≤ F − (1/2L)‖∇F‖²   (descent lemma)", WHITE), ("    ≤ F − (μ/L)(F − F*)   (PL)", SUN), ("⇒ F_k − F* ≤ (1 − μ/L)ᵏ (F₀ − F*)" if LANG == "vi" else "⇒ F_k − F* ≤ (1 − μ/L)ᵏ (F₀ − F*)", MINT)], size=23)
        self.say(L("Chứng minh chỉ hai dòng. GD với η = 1/L giảm F ít nhất ‖∇F‖²/2L. PL đổi ‖∇F‖² thành khoảng cách tới tối ưu. Vậy mỗi bước khoảng cách co ít nhất theo hệ số 1 − μ/L.",
                   "The proof is two lines. GD with η = 1/L lowers F by at least ‖∇F‖²/2L. PL turns ‖∇F‖² into the gap to optimal. So each step the gap shrinks by at least the factor 1 − μ/L."), hold=10.5)
        def rw(k): self.readout([("GD, η = 1/8, w₀ = 4:  k = %d" % k if LANG == "vi" else "GD, η = 1/8, w₀ = 4:  k = %d" % k, SUN), ("w = %s,  F = %s" % (nf(W[k], 3), nf(FW[k], 3) if FW[k] > 1e-3 else sci(FW[k], 1)), WHITE)], size=23)
        P = [(w, F(w)) for w in W]
        pt = trail(self, ax, P, d, SUN, rt=lambda k: 0.7, ks=range(1, 11), cb=rw, width=3)
        self.say(L("Chạy GD từ w₀ = 4. Qua vùng cong xuống quanh w ≈ 2, bước nhỏ lại vì dốc thoải, nhưng gradient không bao giờ bằng 0, nên vẫn đi tiếp và rơi xuống đáy.",
                   "Run GD from w₀ = 4. Through the downward-curving region near w ≈ 2 the steps shrink because the slope is gentle, but the gradient never vanishes, so it keeps going and drops to the bottom."), hold=10.0)
        self.wipe()
        fx = plain_axes([0, 14], [0, 18], 7.4, 4.8, [0.25, 1.7, 0])
        yt = VGroup(*[Text(s_, font=MONO, font_size=17, color=DIM).next_to(fx.c2p(0, v + 16), LEFT, buff=0.1) for v, s_ in ((0, "1"), (-8, "10⁻⁸"), (-16, "10⁻¹⁶"))])
        xt = VGroup(*[Text(str(v), font=MONO, font_size=17, color=DIM).next_to(fx.c2p(v, 0), DOWN, buff=0.1) for v in (5, 10)])
        lg = lambda v: max(np.log10(max(v, 1e-30)), -16) + 16
        c1 = VMobject(color=SUN, stroke_width=3.5).set_points_as_corners([fx.c2p(k, lg(FW[k])) for k in range(15)])
        c2 = DashedVMobject(VMobject(color=DIM, stroke_width=3).set_points_as_corners([fx.c2p(k, lg(BOUND[k])) for k in range(15)]), num_dashes=30)
        self.play(Create(fx), FadeIn(yt), FadeIn(xt), run_time=0.4); self.play(Create(c2), Create(c1), run_time=1.6)
        self.readout([("F(w_k), thang log" if LANG == "vi" else "F(w_k), log scale", SUN), ("nét đứt: cận (1 − μ/L)ᵏ F₀,  1 − μ/L = %s" % nf(1 - MU / LL, 4) if LANG == "vi" else "dashed: bound (1 − μ/L)ᵏ F₀,  1 − μ/L = %s" % nf(1 - MU / LL, 4), DIM)], size=22)
        self.say(L("Trên thang log: đường vàng luôn nằm dưới cận nét đứt, như định lý hứa. Cận khá dè dặt; gần đáy F″ = 8 = L nên GD còn nhanh hơn nhiều.",
                   "On a log scale: the yellow curve always stays below the dashed bound, as the theorem promises. The bound is cautious; near the bottom F″ = 8 = L, so GD is much faster still."), hold=9.5)
        # ---- stage 4
        self.stage(4); self.wipe()
        fx2 = plain_axes([0, 100], [0, 15], 7.4, 4.8, [0.25, 1.7, 0])
        yt2 = VGroup(*[Text(s_, font=MONO, font_size=17, color=DIM).next_to(fx2.c2p(0, v + 12), LEFT, buff=0.1) for v, s_ in ((0, "1"), (-6, "10⁻⁶"), (-12, "10⁻¹²"))])
        xt2 = VGroup(*[Text(str(v), font=MONO, font_size=17, color=DIM).next_to(fx2.c2p(v, 0), DOWN, buff=0.1) for v in (50, 100)])
        cv = lambda A, c: VMobject(color=c, stroke_width=3.5).set_points_as_corners([fx2.c2p(k, max(np.log10(A[k]), -12) + 12) for k in range(101)])
        self.play(Create(fx2), FadeIn(yt2), FadeIn(xt2), run_time=0.4)
        c4 = cv(Q4, PINK); self.play(Create(c4), run_time=1.2)
        self.readout([("F = w⁴: lồi, nhưng ½F′²/F = 8w² → 0" if LANG == "vi" else "F = w⁴: convex, but ½F′²/F = 8w² → 0", PINK), ("GD η = 0,1: F₁₀₀ ≈ %s" % sci(Q4[100], 1) if LANG == "vi" else "GD η = 0.1: F₁₀₀ ≈ %s" % sci(Q4[100], 1), PINK)], size=23)
        self.say(L("Đối chiếu một: F = w⁴ lồi, nhưng không thỏa PL, vì gần đáy gradient nhỏ đi quá nhanh. GD chỉ bò chậm kiểu đa thức: sau 100 bước F vẫn còn cỡ 10⁻⁴.",
                   "Contrast one: F = w⁴ is convex but not PL, because near the bottom the gradient shrinks too fast. GD only crawls polynomially: after 100 steps F is still around 10⁻⁴."), hold=9.5)
        ca, cb = cv(LA, MINT), cv(LB, SKY); self.play(Create(ca), Create(cb), run_time=1.5)
        self.readout([("bình phương tối thiểu n = 20, d = 50" if LANG == "vi" else "least squares n = 20, d = 50", MINT), ("μ = %s,  L = %s,  1 − μ/L = %s" % (nf(MUL, 3), nf(LLS, 3), nf(1 - MUL / LLS, 3)), WHITE), ("hai điểm đầu → hai nghiệm cách nhau %s" % nf(DW, 1) if LANG == "vi" else "two starts → two solutions %s apart" % nf(DW, 1), SKY)], size=22)
        self.say(L("Đối chiếu hai, đoạn mã của bài: bình phương tối thiểu với d = 50 > n = 20. Hessian suy biến nên không lồi mạnh, có vô số nghiệm, nhưng vẫn PL với μ = trị riêng khác 0 nhỏ nhất của XᵀX/n.",
                   "Contrast two, the lesson's code: least squares with d = 50 > n = 20. The Hessian is singular, so not strongly convex, with infinitely many solutions, yet PL holds with μ = the smallest nonzero eigenvalue of XᵀX/n."), hold=11.0)
        self.say(L("Hai điểm đầu khác nhau hội tụ tuyến tính tới hai nghiệm khác nhau, cách nhau %s. PL không cần nghiệm duy nhất, chỉ cần giá trị tối ưu đạt được." % nf(DW, 1),
                   "Two different starts converge linearly to two different solutions, %s apart. PL does not need a unique solution, only that the optimal value is attained." % nf(DW, 1)), hold=9.0)
        self.takeaway([L("PL: ½‖∇F‖² ≥ μ(F − F*); điểm dừng nào cũng là tối ưu toàn cục.", "PL: ½‖∇F‖² ≥ μ(F − F*); every stationary point is globally optimal."),
                       L("GD bước 1/L: F − F* co theo (1 − μ/L)ᵏ.", "GD with step 1/L: F − F* shrinks like (1 − μ/L)ᵏ."),
                       L("Không cần lồi: w² + 3 sin² w thỏa PL.", "No convexity needed: w² + 3 sin² w is PL."),
                       L("Lồi chưa đủ (w⁴); nghiệm không cần duy nhất.", "Convexity is not enough (w⁴); solutions need not be unique.")], tail=4.0)
