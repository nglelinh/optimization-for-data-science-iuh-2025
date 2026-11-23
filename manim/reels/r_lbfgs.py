from rl import *
# Bài 18-07: L-BFGS: chỉ giữ m cặp (s, y), tính H·q bằng đệ quy hai vòng
# bộ nhớ (số thực 8 byte)
MB = lambda nums: nums * 8 / 1e6
assert MB(1e3 ** 2) == 8 and MB(1e6 ** 2) == 8e6 and MB(2 * 10 * 1e6) == 160      # 8 MB, 8 TB, 160 MB
def two_loop(q, S, Y, log=None):
    al = []
    for s, y in zip(reversed(S), reversed(Y)):
        a = (s @ q) / (y @ s); al.append(a); q = q - a * y
        if log is not None: log.append(("a", a, q.copy()))
    gam = (S[-1] @ Y[-1]) / (Y[-1] @ Y[-1]); r = gam * q
    if log is not None: log.append(("g", gam, r.copy()))
    for (s, y), a in zip(zip(S, Y), reversed(al)):
        b = (y @ r) / (y @ s); r = r + s * (a - b)
        if log is not None: log.append(("b", b, r.copy()))
    return r
def bfgs_H(H, s, y):
    rho = 1 / (y @ s); I = np.eye(len(s)); return (I - rho * np.outer(s, y)) @ H @ (I - rho * np.outer(y, s)) + rho * np.outer(s, s)
# ví dụ 2 chiều: f = ½xᵀQx, hai cặp s₁ = e₁, s₂ = e₂, y = Qs
Q = np.array([[2., 1], [1, 3]]); S2 = [np.array([1., 0]), np.array([0., 1])]; Y2 = [Q @ s for s in S2]; q0 = np.array([1., 1])
LOG = []; R2 = two_loop(q0, S2, Y2, LOG)
GAM = 0.3; H = GAM * np.eye(2)
for s, y in zip(S2, Y2): H = bfgs_H(H, s, y)
assert np.allclose(R2, H @ q0) and np.allclose(R2, [23 / 60, 37 / 180]) and np.isclose(LOG[2][1], GAM)
assert np.allclose(LOG[0][2], [2 / 3, 0]) and np.allclose(LOG[1][2], [0, -1 / 3]) and np.isclose(LOG[0][1], 1 / 3) and np.isclose(LOG[1][1], 1 / 3)
assert np.allclose(LOG[3][2], [23 / 60, -0.1]) and np.isclose(LOG[3][1], -0.05) and np.isclose(LOG[4][1], 1 / 36)
NEWT = np.linalg.solve(Q, q0); assert np.allclose(NEWT, [0.4, 0.2])
# so sánh: hồi quy logistic + L2, N = 400, d = 100
rng = np.random.default_rng(0); N, D = 400, 100
X = rng.standard_normal((N, D)) * np.linspace(0.05, 2, D); w0 = rng.standard_normal(D); yy = np.sign(X @ w0 + 0.5 * rng.standard_normal(N)); LAM = 1e-2
fo = lambda w: np.mean(np.logaddexp(0, -yy * (X @ w))) + LAM / 2 * w @ w
go = lambda w: X.T @ (-yy / (1 + np.exp(yy * (X @ w)))) / N + LAM * w
def run(kind, m=10, tol=1e-6, maxit=2000):
    w = np.zeros(D); S = []; Y = []; Hm = np.eye(D); gw = go(w); hist = [np.linalg.norm(gw)]; Lc = np.linalg.norm(X, 2) ** 2 / (4 * N) + LAM
    for k in range(maxit):
        if kind == "gd": p = -gw / Lc; t = 1.
        else:
            p = -(two_loop(gw, S, Y) if (kind == "lbfgs" and S) else (Hm @ gw)); t = 1.
            while fo(w + t * p) > fo(w) + 1e-4 * t * (gw @ p): t *= 0.5
        wn = w + t * p; gn = go(wn); s, y = wn - w, gn - gw
        if kind == "lbfgs": S = (S + [s])[-m:]; Y = (Y + [y])[-m:]
        elif kind == "bfgs":
            if k == 0: Hm = (s @ y) / (y @ y) * np.eye(D)
            Hm = bfgs_H(Hm, s, y)
        w, gw = wn, gn; hist.append(np.linalg.norm(gw))
        if hist[-1] < tol: break
    return len(hist) - 1, np.array(hist)
RUNS = {"gd": run("gd"), 1: run("lbfgs", 1), 3: run("lbfgs", 3), 10: run("lbfgs", 10), 30: run("lbfgs", 30), "bfgs": run("bfgs")}
IT = {k: v[0] for k, v in RUNS.items()}
assert IT == {"gd": 906, 1: 42, 3: 38, 10: 37, 30: 36, "bfgs": 74}, IT

class Lbfgs(Reel):
    def construct(self):
        self.title(L("L-BFGS:\nBFGS với bộ nhớ nhỏ", "L-BFGS:\nBFGS on a small memory"))
        # ---- stage 1
        self.stage(1)
        self.readout([("H⁺ = (I − ρsyᵀ) H (I − ρysᵀ) + ρssᵀ", SUN), ("ρ = 1/yᵀs;  bước x⁺ = x − t·H∇f(x)" if LANG == "vi" else "ρ = 1/yᵀs;  step x⁺ = x − t·H∇f(x)", WHITE)], size=25)
        self.say(L("Nhắc lại BFGS: giữ một ma trận H xấp xỉ nghịch đảo Hessian, mỗi bước cập nhật bằng cặp s = x⁺ − x và y = ∇f⁺ − ∇f.",
                   "Recall BFGS: keep a matrix H approximating the inverse Hessian, and update it each step with the pair s = x⁺ − x and y = ∇f⁺ − ∇f."), hold=8.5)
        big = Square(4.2, stroke_color=PINK, stroke_width=3, fill_color=PINK, fill_opacity=0.25).move_to([0, 1.6, 0])
        grid = VGroup(*[Line(big.get_corner(UL) + RIGHT * 4.2 * i / 12, big.get_corner(DL) + RIGHT * 4.2 * i / 12, color=PINK, stroke_width=0.8) for i in range(1, 12)],
                      *[Line(big.get_corner(UL) + DOWN * 4.2 * i / 12, big.get_corner(UR) + DOWN * 4.2 * i / 12, color=PINK, stroke_width=0.8) for i in range(1, 12)])
        lb = Text("H: n × n", font=MONO, font_size=26, color=PINK).next_to(big, UP, buff=0.15)
        self.play(FadeIn(big), Create(grid), FadeIn(lb), run_time=1.0)
        self.readout([("n = 10³:  n² số = 8 MB" if LANG == "vi" else "n = 10³:  n² numbers = 8 MB", WHITE), ("n = 10⁶:  n² số = 8 TB" if LANG == "vi" else "n = 10⁶:  n² numbers = 8 TB", PINK), ("mỗi bước còn tốn O(n²) phép tính" if LANG == "vi" else "and each step costs O(n²) operations", ORANGE)], size=24)
        self.say(L("Vấn đề nằm ở H: n × n số. Với n = 1000 chỉ 8 MB, nhưng với một triệu biến là 8 terabyte, và mỗi bước tốn cỡ n² phép tính.",
                   "The problem is H: n × n numbers. With n = 1000 that is only 8 MB, but with a million variables it is 8 terabytes, and each step costs about n² operations."), hold=10.0)
        # ---- stage 2
        self.stage(2)
        cols = VGroup(*[Rectangle(width=0.2, height=4.2, stroke_color=c, stroke_width=2, fill_color=c, fill_opacity=0.35) for i in range(10) for c in (SKY, MINT)]).arrange(RIGHT, buff=0.12).move_to([0, 1.6, 0])
        lc = Text(L("m cặp (sᵢ, yᵢ): 2mn số", "m pairs (sᵢ, yᵢ): 2mn numbers")[LANG], font=MONO, font_size=26, color=MINT).next_to(cols, UP, buff=0.15)
        self.play(ReplacementTransform(VGroup(big, grid), cols), ReplacementTransform(lb, lc), run_time=1.2)
        self.readout([("H₀ = γI,  γ = sᵀy / yᵀy  (cặp mới nhất)" if LANG == "vi" else "H₀ = γI,  γ = sᵀy / yᵀy  (newest pair)", SUN), ("n = 10⁶, m = 10:  2·10⁷ số = 160 MB" if LANG == "vi" else "n = 10⁶, m = 10:  2·10⁷ numbers = 160 MB", MINT)], size=24)
        self.say(L("Ý tưởng của L-BFGS: đừng lưu H. Chỉ giữ m cặp (s, y) gần nhất, thường m từ 3 đến 20. H được định nghĩa ngầm: bắt đầu từ γI rồi áp m lần công thức BFGS.",
                   "The L-BFGS idea: don't store H. Keep only the m most recent pairs (s, y), typically m between 3 and 20. H is defined implicitly: start from γI and apply the BFGS formula m times."), hold=10.0)
        self.say(L("Với một triệu biến và m = 10, bộ nhớ là 160 MB thay vì 8 TB. Cặp cũ nhất bị bỏ khi có cặp mới.",
                   "With a million variables and m = 10, the memory is 160 MB instead of 8 TB. The oldest pair is dropped when a new one arrives."), hold=7.5)
        self.readout([("α = ρ sᵀq,   q ← q − α y", SKY), ("r ← H r  (đệ quy, cặp cũ hơn)" if LANG == "vi" else "r ← H r  (recurse, older pairs)", WHITE), ("β = ρ yᵀr,   r ← r + (α − β) s", MINT)], size=24)
        self.say(L("Ta không cần H, chỉ cần tích H·∇f. Bài 18-07 viết một bước của công thức thành: tính α, trừ αy khỏi q, nhân với H cũ, rồi cộng (α − β)s.",
                   "We never need H itself, only the product H·∇f. Lesson 18-07 writes one step of the formula as: compute α, subtract αy from q, multiply by the old H, then add (α − β)s."), hold=10.5)
        self.say(L("Lồng đệ quy m lần thành hai vòng lặp: vòng đi từ cặp mới về cũ tính các α, nhân γ, rồi vòng đi từ cũ về mới tính các β. Chi phí chỉ cỡ 4mn.",
                   "Unrolling the recursion m times gives two loops: one from newest to oldest pair computing the α's, multiply by γ, then one from oldest to newest computing the β's. The cost is only about 4mn."), hold=10.0)
        # ---- stage 3
        self.stage(3); self.wipe()
        ax = plain_axes([-1.15, 0.25], [-1.15, 0.25], 3.4, 3.4, [-2.2, 2.6, 0])
        o = ax.c2p(0, 0)
        a1 = Arrow(o, ax.c2p(-1, -1), buff=0, color=PINK, stroke_width=4, max_tip_length_to_length_ratio=0.12)
        self.play(Create(ax), GrowArrow(a1), run_time=0.6)
        info = VGroup(*[Text(s_, font=MONO, font_size=21, color=c_) for s_, c_ in (("Q = [[2, 1], [1, 3]]", WHITE), ("s₁ = (1; 0), y₁ = (2; 1)" if LANG == "vi" else "s₁ = (1, 0), y₁ = (2, 1)", SKY), ("s₂ = (0; 1), y₂ = (1; 3)" if LANG == "vi" else "s₂ = (0, 1), y₂ = (1, 3)", SKY), ("q = ∇f = (1; 1)" if LANG == "vi" else "q = ∇f = (1, 1)", PINK))]).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to([1.9, 2.6, 0])
        self.play(FadeIn(info), run_time=0.5)
        self.say(L("Làm tay một ví dụ nhỏ: f = ½xᵀQx trong 2 chiều, giữ m = 2 cặp, với y = Qs. Cần tính H·q với q = ∇f = (1; 1), mũi tên hồng là −∇f.",
                   "Work a small example by hand: f = ½xᵀQx in 2D, keep m = 2 pairs, with y = Qs. We want H·q with q = ∇f = (1, 1); the pink arrow is −∇f."), hold=10.0)
        V = lambda v: vec(v, 3)
        steps = [("vòng 1, cặp 2:  α₂ = %s,  q = %s" % (nf(LOG[0][1], 3), V(LOG[0][2])) if LANG == "vi" else "loop 1, pair 2:  α₂ = %s,  q = %s" % (nf(LOG[0][1], 3), V(LOG[0][2])), SKY),
                 ("vòng 1, cặp 1:  α₁ = %s,  q = %s" % (nf(LOG[1][1], 3), V(LOG[1][2])) if LANG == "vi" else "loop 1, pair 1:  α₁ = %s,  q = %s" % (nf(LOG[1][1], 3), V(LOG[1][2])), SKY),
                 ("γ = sᵀy/yᵀy = 3/10:  r = %s" % V(LOG[2][2]), SUN),
                 ("vòng 2, cặp 1:  β₁ = %s,  r = %s" % (nf(LOG[3][1], 3), V(LOG[3][2])) if LANG == "vi" else "loop 2, pair 1:  β₁ = %s,  r = %s" % (nf(LOG[3][1], 3), V(LOG[3][2])), MINT),
                 ("vòng 2, cặp 2:  β₂ = %s,  r = %s" % (nf(LOG[4][1], 3), V(LOG[4][2])) if LANG == "vi" else "loop 2, pair 2:  β₂ = %s,  r = %s" % (nf(LOG[4][1], 3), V(LOG[4][2])), MINT)]
        tx = VGroup(*[Text(s_, font=MONO, font_size=22, color=c_) for s_, c_ in steps]).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        fit(tx, 8.2).move_to([0, -0.6, 0])
        caps = [L("Vòng 1 bắt đầu từ cặp mới nhất: α₂ = 1/3, trừ α₂y₂ khỏi q. Rồi tới cặp 1: α₁ = 1/3, q còn (0; −1/3).",
                  "Loop 1 starts with the newest pair: α₂ = 1/3, subtract α₂y₂ from q. Then pair 1: α₁ = 1/3, leaving q = (0, −1/3)."),
                L("Ở giữa, nhân với H₀ = γI. γ = s₂ᵀy₂ / y₂ᵀy₂ = 3/10 lấy thang đo từ cặp mới nhất.",
                  "In the middle, multiply by H₀ = γI. γ = s₂ᵀy₂ / y₂ᵀy₂ = 3/10 takes its scale from the newest pair."),
                L("Vòng 2 đi ngược lại, từ cặp cũ tới mới: mỗi lần tính β rồi cộng (α − β)s. Kết quả r = H·q ≈ (0,383; 0,206).",
                  "Loop 2 goes the other way, oldest to newest: each time compute β and add (α − β)s. The result r = H·q ≈ (0.383, 0.206).")]
        self.play(FadeIn(tx[0]), run_time=0.3); self.play(FadeIn(tx[1]), run_time=0.3); self.say(caps[0], hold=8.0)
        self.play(FadeIn(tx[2]), run_time=0.3); self.say(caps[1], hold=7.0)
        self.play(FadeIn(tx[3]), run_time=0.3); self.play(FadeIn(tx[4]), run_time=0.3)
        a2 = Arrow(o, ax.c2p(*(-R2)), buff=0, color=MINT, stroke_width=5, max_tip_length_to_length_ratio=0.3)
        a3 = DashedLine(o, ax.c2p(*(-NEWT)), color=SUN, stroke_width=3)
        self.play(GrowArrow(a2), Create(a3), run_time=0.6); self.say(caps[2], hold=8.5)
        self.readout([("−H·q = %s   (xanh lá)" % V(-R2) if LANG == "vi" else "−H·q = %s   (green)" % V(-R2), MINT), ("Newton −Q⁻¹q = %s   (vàng)" % V(-NEWT) if LANG == "vi" else "Newton −Q⁻¹q = %s   (yellow)" % V(-NEWT), SUN)], size=23)
        self.say(L("Kiểm tra: đúng bằng H·q khi tính H đầy đủ bằng hai lần cập nhật BFGS. Và hướng này rất gần hướng Newton (0,4; 0,2), khác xa −∇f.",
                   "Check: it equals H·q with H formed explicitly by two BFGS updates. And this direction is very close to the Newton direction (0.4, 0.2), far from −∇f."), hold=10.0)
        # ---- stage 4
        self.stage(4); self.wipe()
        fx = plain_axes([0, 120], [0, 7], 7.4, 5.2, [0.25, 1.6, 0])
        yt = VGroup(*[Text(s_, font=MONO, font_size=17, color=DIM).next_to(fx.c2p(0, v + 6.5), LEFT, buff=0.1) for v, s_ in ((0, "1"), (-3, "10⁻³"), (-6, "10⁻⁶"))])
        xt = VGroup(*[Text(str(v), font=MONO, font_size=17, color=DIM).next_to(fx.c2p(v, 0), DOWN, buff=0.1) for v in (40, 80, 120)])
        yl = Text("‖∇f‖", font=MONO, font_size=20, color=DIM).next_to(fx.c2p(0, 7), UR, buff=0.08)
        self.play(Create(fx), FadeIn(yt), FadeIn(xt), FadeIn(yl), run_time=0.5)
        def cv(h, c): n = min(len(h), 121); return VMobject(color=c, stroke_width=3.5).set_points_as_corners([fx.c2p(k, max(np.log10(h[k]), -6.5) + 6.5) for k in range(n)])
        cs = [cv(RUNS[k][1], c) for k, c in (("gd", PINK), (1, ORANGE), (10, MINT), ("bfgs", SKY))]
        self.play(*[Create(c) for c in cs], run_time=3.0, rate_func=linear)
        self.readout([("hồi quy logistic, d = 100: bước tới ‖∇f‖ < 10⁻⁶" if LANG == "vi" else "logistic regression, d = 100: steps to ‖∇f‖ < 10⁻⁶", WHITE), ("GD: %d" % IT["gd"], PINK), ("L-BFGS m = 1: %d,  m = 3: %d" % (IT[1], IT[3]), ORANGE), ("L-BFGS m = 10: %d,  m = 30: %d" % (IT[10], IT[30]), MINT), ("BFGS đầy đủ: %d" % IT["bfgs"] if LANG == "vi" else "full BFGS: %d" % IT["bfgs"], SKY)], size=21)
        self.say(L("Thử trên hồi quy logistic 100 biến. GD cần %d bước. L-BFGS chỉ cần %d đến %d bước, và m = 3 đã gần như tốt bằng m = 30." % (IT["gd"], IT[30], IT[1]),
                   "Try logistic regression with 100 variables. GD needs %d steps. L-BFGS needs only %d to %d steps, and m = 3 is already almost as good as m = 30." % (IT["gd"], IT[30], IT[1])), hold=10.5)
        self.say(L("Ở bài này BFGS đầy đủ còn chậm hơn, %d bước: thang đo γ của nó chỉ đặt một lần lúc đầu, còn L-BFGS chọn lại γ mỗi bước từ cặp mới nhất." % IT["bfgs"],
                   "On this problem full BFGS is even slower, %d steps: its scale γ is set once at the start, while L-BFGS re-picks γ every step from the newest pair." % IT["bfgs"]), hold=10.5)
        self.say(L("Cái giá: m nhỏ thì H quên độ cong cũ, nên với bài khó, L-BFGS có thể cần nhiều bước hơn BFGS. Đổi lại, bộ nhớ O(mn) thay vì O(n²).",
                   "The price: with small m, H forgets old curvature, so on hard problems L-BFGS can need more steps than BFGS. In exchange, memory is O(mn) instead of O(n²)."), hold=10.5)
        self.takeaway([L("BFGS cần ma trận n × n: không khả thi khi n rất lớn.", "BFGS needs an n × n matrix: infeasible when n is huge."),
                       L("L-BFGS chỉ giữ m cặp (s, y) gần nhất, H₀ = γI.", "L-BFGS keeps only the m newest pairs (s, y), with H₀ = γI."),
                       L("Hai vòng lặp tính H·∇f với chi phí O(mn).", "Two loops compute H·∇f at O(mn) cost."),
                       L("m từ 3 đến 20 thường đã đủ.", "m between 3 and 20 is usually enough.")], tail=4.0)
