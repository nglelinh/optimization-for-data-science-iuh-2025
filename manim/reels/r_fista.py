from rl import *
# Bài 09-05: ISTA (proximal gradient) và FISTA trên lasso  min ½‖Ax − b‖² + λ‖x‖₁
S = lambda z, a: np.sign(z) * np.maximum(np.abs(z) - a, 0)
def solve(A, b, lam, x0, n, kind):
    t = 1 / np.linalg.eigvalsh(A.T @ A).max()
    F = lambda x: .5 * np.sum((A @ x - b) ** 2) + lam * np.abs(x).sum(); g = lambda x: A.T @ (A @ x - b)
    x = x0.copy(); xp = x.copy(); k = 0; P = [x.copy()]; Rs = []
    for it in range(1, n + 1):
        if kind == "ista": x = S(x - t * g(x), t * lam)
        else:
            k += 1; v = x + (k - 2) / (k + 1) * (x - xp) if k > 1 else x
            xn = S(v - t * g(v), t * lam)
            if kind == "restart" and F(xn) > F(x): k = 1; xn = S(x - t * g(x), t * lam); Rs.append(it)
            xp, x = x, xn
        P.append(x.copy())
    return np.array(P), np.array([F(p) for p in P]), Rs
# 2 biến: AᵀA = R·diag(1; 50)·Rᵀ (xoay 35°), b = A·c
th = np.deg2rad(35); Rm = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
Q = Rm @ np.diag([1., 50.]) @ Rm.T; A2 = np.linalg.cholesky(Q).T; C2 = np.array([2.5, 0.3]); B2 = A2 @ C2; LAM2 = 1.0; X0 = np.array([-0.6, -0.4])
assert np.allclose(A2.T @ A2, Q) and abs(np.linalg.cond(Q) - 50) < 1e-9
PI, EI, _ = solve(A2, B2, LAM2, X0, 3000, "ista"); PF, EF, _ = solve(A2, B2, LAM2, X0, 3000, "fista"); PR, ER, RS2 = solve(A2, B2, LAM2, X0, 3000, "restart")
XS = PI[-1]; FS = EI[-1]
first = lambda E, tol=1e-8: int(np.argmax(E - FS < tol))
NI, NF, NR = first(EI), first(EF), first(ER)
assert abs(XS[0] - 2.0382) < 1e-4 and XS[1] == 0 and np.allclose(PF[-1], XS) and (NI, NF, NR) == (121, 61, 34)
ZI = int(np.argmax(PI[:, 1] == 0)); assert (PI[ZI:, 1] == 0).all(); assert ZI == 106
ZF = int(np.argmax([(PF[j:, 1] == 0).all() for j in range(len(PF))])); assert ZF == 36
NM2 = int((np.diff(EF[:60]) > 0).sum()); assert NM2 == 15 and (np.diff(EI) <= 1e-15).all()
W = [(k - 2) / (k + 1) for k in range(2, 8)]; assert np.allclose(W, [0, .25, .4, .5, 4 / 7, .625])
# lasso ngẫu nhiên n = 50, p = 100 (seed 3)
rng = np.random.default_rng(3); n, p = 50, 100
A = rng.standard_normal((n, p)); xt = np.zeros(p); xt[:5] = [3, -2, 2, -1.5, 1]; b = A @ xt + 0.5 * rng.standard_normal(n)
LAM = 0.1 * np.abs(A.T @ b).max()
_, E1, _ = solve(A, b, LAM, np.zeros(p), 600, "ista"); _, E2, _ = solve(A, b, LAM, np.zeros(p), 600, "fista"); P3, E3, RS = solve(A, b, LAM, np.zeros(p), 600, "restart")
_, Elong, _ = solve(A, b, LAM, np.zeros(p), 20000, "ista"); FS2 = min(Elong.min(), E3.min())
hit = lambda E, tol: int(np.argmax(E - FS2 < tol))
H = [[hit(E, tol) for tol in (1e-2, 1e-8)] for E in (E1, E2, E3)]
assert H == [[51, 133], [25, 115], [20, 43]], H
NM = int((np.diff(E2) > 1e-12).sum()); assert NM == 75 and (np.diff(E3) <= 1e-12).all() and RS[:3] == [15, 28, 39]
NNZ = int((np.abs(P3[-1]) > 1e-8).sum()); assert NNZ == 6
Q3 = Rm @ np.diag([1., 3.]) @ Rm.T; A3 = np.linalg.cholesky(Q3).T; B3 = A3 @ C2
_, E3I, _ = solve(A3, B3, 1., X0, 400, "ista"); _, E3F, _ = solve(A3, B3, 1., X0, 400, "fista"); _, E3R, _ = solve(A3, B3, 1., X0, 400, "restart")
F3 = E3I[-1]; K3 = [int(np.argmax(E - F3 < 1e-8)) for E in (E3I, E3F, E3R)]; assert K3 == [14, 16, 8], K3
lg = lambda e: np.log10(np.maximum(e, 1e-9)) + 9   # trục dọc: 0 ↔ 10⁻⁹
Fx = lambda x, y: .5 * (np.array([x, y]) - C2) @ Q @ (np.array([x, y]) - C2) + LAM2 * (abs(x) + abs(y))
LV = [FS + d for d in (0.1, 0.6, 2, 5, 10, 18, 30)]

def multi(sc, ax, paths, dots, cols, ks, rt, width=3, start=0):
    segs = []; prev = start
    for k in ks:
        an = []
        for P, d, c in zip(paths, dots, cols):
            a, b_ = min(prev, len(P) - 1), min(k, len(P) - 1)
            if a == b_: continue
            s = VMobject(color=c, stroke_width=width).set_points_as_corners([ax.c2p(*P[j]) for j in range(a, b_ + 1)]); segs.append(s)
            an += [Create(s), d.animate.move_to(ax.c2p(*P[b_]))]
        if an: sc.play(*an, run_time=rt(k) if callable(rt) else rt, rate_func=linear)
        prev = k
    sc.remove(*segs); g = VGroup(*segs); sc.add(g); sc.bring_to_front(*dots); return g

def curve(ax, ks, ys, col, w=3.5):
    ys = np.asarray(ys); cut = int(np.argmax(ys <= 0)) if (ys <= 0).any() else len(ys) - 1
    ks, ys = ks[:cut + 1], ys[:cut + 1]
    return VMobject(color=col, stroke_width=w).set_points_as_corners([ax.c2p(k, y) for k, y in zip(ks, ys)])

class Fista(Reel):
    def construct(self):
        self.title(L("ISTA và FISTA:\ntăng tốc proximal gradient", "ISTA and FISTA:\naccelerating proximal gradient"))
        # ---- stage 1
        self.stage(1)
        ax = plain_axes([-1.0, 2.6], [-1.8, 0.6], 7.6, 5.07, [0, 1.9, 0])
        cs = contours(ax, Fx, LV, (-1.0, 2.6, -1.8, 0.6), N=110, color="#4a5582", width=2.5)
        self.play(Create(ax), Create(cs), run_time=1.2)
        st = Dot(ax.c2p(*XS), radius=0.1, color=WHITE); stl = Text("x*", font=FONT, font_size=24, color=WHITE).next_to(st, UP, buff=0.12)
        self.add(st, stl)
        self.say(L("Bài toán lasso của bài 09-05: min ½‖Ax − b‖² + λ‖x‖₁. Phần đầu g trơn, phần sau h = λ‖x‖₁ không trơn.",
                   "The lasso problem of lesson 09-05: min ½‖Ax − b‖² + λ‖x‖₁. The first part g is smooth, the second part h = λ‖x‖₁ is not."), hold=7.0)
        self.say(L("Ví dụ 2 biến, λ = 1, κ(AᵀA) = 50: thung lũng hẹp, nghiêng. Các đường mức bị gãy trên hai trục vì |x₁| + |x₂|.",
                   "A 2-variable example, λ = 1, κ(AᵀA) = 50: a narrow, tilted valley. The level curves bend on the two axes because of |x₁| + |x₂|."), hold=7.0)
        self.say(L("Bước cố định t = 1/L, với L = λmax(AᵀA) = 50: bước lớn nhất mà định lý của bài 09-05-02 cho phép.",
                   "A fixed step t = 1/L, with L = λmax(AᵀA) = 50: the largest step the theorem of lesson 09-05-02 allows."), hold=6.0)
        self.readout([("x* = (%s; 0),  F* = %s" % (nf(XS[0], 3), nf(FS, 3)) if LANG == "vi" else "x* = (%s, 0),  F* = %s" % (nf(XS[0], 3), nf(FS, 3)), WHITE)], size=23)
        self.say(L("Nghiệm x* = (%s; 0) nằm đúng trên trục: x₂* = 0. Lasso cho nghiệm thưa." % nf(XS[0], 2),
                   "The solution x* = (%s, 0) lies exactly on the axis: x₂* = 0. Lasso gives sparse solutions." % nf(XS[0], 2)), hold=5.5)
        # ---- stage 2
        self.stage(2); self.wipe()
        sx = plain_axes([-3, 3], [-2.2, 2.2], 6.0, 4.4, [0, 2.2, 0])
        idl = DashedLine(sx.c2p(-2.2, -2.2), sx.c2p(2.2, 2.2), color=DIM, stroke_width=2)
        sth = VMobject(color=SUN, stroke_width=5).set_points_as_corners([sx.c2p(-3, -2), sx.c2p(-1, 0), sx.c2p(1, 0), sx.c2p(3, 2)])
        zl = Text("z", font=FONT, font_size=22, color=DIM).next_to(sx.c2p(3, 0), DOWN, buff=0.1)
        sl = Text("S(z) = sign(z)·max(|z| − tλ; 0)" if LANG == "vi" else "S(z) = sign(z)·max(|z| − tλ, 0)", font=MONO, font_size=20, color=SUN).move_to(sx.c2p(0, -2.7))
        self.play(Create(sx), FadeIn(zl), Create(idl), run_time=0.6); self.play(Create(sth), FadeIn(sl), run_time=0.8)
        self.readout([("ISTA:  x⁺ = S(x − t·∇g(x)),   t = 1/L", SKY)], size=23)
        self.say(L("ISTA = proximal gradient: bước gradient trên g, rồi áp prox của λ‖x‖₁. Prox đó là ngưỡng mềm S: kéo mỗi tọa độ về 0 một đoạn tλ, và cắt hẳn về 0 nếu nhỏ hơn.",
                   "ISTA = proximal gradient: a gradient step on g, then the prox of λ‖x‖₁. That prox is soft thresholding S: pull each coordinate toward 0 by tλ, and cut it to exactly 0 if it is smaller."), hold=9.0)
        self.say(L("Phần cắt về 0 (đoạn nằm ngang) là lý do ISTA cho ra nghiệm thưa.",
                   "The cut to 0 (the flat segment) is why ISTA produces sparse solutions."), hold=4.5)
        self.play(FadeOut(VGroup(sx, idl, sth, zl, sl)), run_time=0.4)
        rows = VGroup(Text("FISTA:", font=MONO, font_size=24, color=PINK),
                      Text("v = x⁽ᵏ⁻¹⁾ + (k − 2)/(k + 1)·(x⁽ᵏ⁻¹⁾ − x⁽ᵏ⁻²⁾)", font=MONO, font_size=21, color=PINK),
                      Text("x⁽ᵏ⁾ = S(v − t·∇g(v))", font=MONO, font_size=21, color=PINK)).arrange(DOWN, aligned_edge=LEFT, buff=0.22).move_to([0, 3.2, 0])
        self.play(FadeIn(rows), run_time=0.6)
        wt = VGroup(*[Text("k = %d: %s" % (k, nf(w, 3)), font=MONO, font_size=21, color=WHITE) for k, w in zip(range(2, 8), W)]).arrange_in_grid(rows=3, cols=2, buff=(0.8, 0.2)).move_to([0, 0.9, 0])
        self.say(L("FISTA giữ nguyên bước prox, chỉ đổi điểm tính: ngoại suy tới v theo hướng vừa đi, như momentum Nesterov.",
                   "FISTA keeps the same prox step and only changes where it is taken: extrapolate to v along the last move, like Nesterov momentum."), hold=6.5)
        self.play(FadeIn(wt), run_time=0.6)
        self.say(L("Trọng số (k − 2)/(k + 1) bắt đầu từ 0 rồi tăng dần về 1: 0; 0,25; 0,4; 0,5; ... Lý thuyết: ISTA có F − F* = O(1/k), FISTA có O(1/k²).",
                   "The weight (k − 2)/(k + 1) starts at 0 and grows toward 1: 0, 0.25, 0.4, 0.5, ... Theory: ISTA has F − F* = O(1/k), FISTA has O(1/k²)."), hold=8.5)
        # ---- stage 3
        self.stage(3); self.wipe()
        ax = plain_axes([-1.0, 2.6], [-1.8, 0.6], 7.6, 5.07, [0, 1.9, 0])
        cs = contours(ax, Fx, LV, (-1.0, 2.6, -1.8, 0.6), N=110, color="#4a5582", width=2.5)
        self.play(Create(ax), Create(cs), run_time=0.8)
        st = Dot(ax.c2p(*XS), radius=0.1, color=WHITE); self.add(st)
        dI = Dot(ax.c2p(*X0), radius=0.1, color=SKY); dF = Dot(ax.c2p(*X0), radius=0.1, color=PINK); self.add(dI, dF)
        lgI = Text("ISTA", font=FONT, font_size=22, color=SKY); lgF = Text("FISTA", font=FONT, font_size=22, color=PINK)
        lg_ = VGroup(lgI, lgF).arrange(RIGHT, buff=0.6).move_to([0, -1.2, 0]); self.add(lg_)
        self.say(L("Cùng xuất phát x⁰ = (−0,6; −0,4), cùng bước t = 1/L. Xanh là ISTA, hồng là FISTA.",
                   "Same start x⁰ = (−0.6, −0.4), same step t = 1/L. Blue is ISTA, pink is FISTA."), wait=False)
        def rt(k): return 0.5 if k <= 3 else (0.3 if k <= 12 else 0.12)
        g1 = multi(self, ax, [PI, PF], [dI, dF], [SKY, PINK], list(range(1, 13)), rt)
        self.say(L("Bước đầu hai cách giống nhau (trọng số bằng 0). Sau đó FISTA lấy đà và đi dọc thung lũng nhanh hơn, có lúc vượt quá x*.",
                   "The first step is the same for both (the weight is 0). Then FISTA builds speed and moves along the valley faster, sometimes overshooting x*."), hold=7.0)
        g2 = multi(self, ax, [PI, PF], [dI, dF], [SKY, PINK], list(range(14, 61, 2)), 0.12, start=12)
        self.readout([("tới F − F* < 10⁻⁸:" if LANG == "vi" else "reach F − F* < 10⁻⁸:", WHITE), ("ISTA  %d vòng,  x₂ = 0 từ vòng %d" % (NI, ZI) if LANG == "vi" else "ISTA  %d rounds,  x₂ = 0 from round %d" % (NI, ZI), SKY), ("FISTA %d vòng,  x₂ = 0 từ vòng %d" % (NF, ZF) if LANG == "vi" else "FISTA %d rounds,  x₂ = 0 from round %d" % (NF, ZF), PINK)], size=22)
        self.say(L("Đếm vòng tới F − F* < 10⁻⁸: ISTA %d, FISTA %d. FISTA cũng giữ được x₂ = 0 sớm hơn nhiều (từ vòng %d so với vòng %d)." % (NI, NF, ZF, ZI),
                   "Rounds to F − F* < 10⁻⁸: ISTA %d, FISTA %d. FISTA also settles at x₂ = 0 much earlier (from round %d versus round %d)." % (NI, NF, ZF, ZI)), hold=7.5)
        self.say(L("Vì sao ISTA chậm? Dọc đáy thung lũng độ cong chỉ là 1, nên mỗi bước chỉ rút ngắn t·1 = 1/50 = 2% khoảng cách còn lại.",
                   "Why is ISTA slow? Along the valley floor the curvature is only 1, so each step shrinks the remaining distance by just t·1 = 1/50 = 2%."), hold=6.5)
        self.say(L("Nhưng FISTA không phải phương pháp giảm: trong 60 vòng đầu, F tăng lại %d lần. ISTA thì giảm ở mọi vòng." % NM2,
                   "But FISTA is not a descent method: in the first 60 rounds F goes back up %d times. ISTA decreases at every round." % NM2), hold=6.5)
        # ---- stage 4
        self.stage(4); self.wipe()
        K = 150
        lx = plain_axes([0, K], [0, 13], 7.4, 5.4, [0.25, 1.8, 0])
        ytl = VGroup(*[Text(s_, font=MONO, font_size=17, color=DIM).next_to(lx.c2p(0, v + 9), LEFT, buff=0.1) for v, s_ in ((3, "10³"), (0, "1"), (-4, "10⁻⁴"), (-8, "10⁻⁸"))])
        xtl = VGroup(*[Text(str(v), font=MONO, font_size=17, color=DIM).next_to(lx.c2p(v, 0), DOWN, buff=0.1) for v in (50, 100, 150)])
        ylab = Text("F − F*", font=MONO, font_size=20, color=DIM).next_to(lx.c2p(0, 13), UR, buff=0.08)
        self.play(Create(lx), FadeIn(ytl), FadeIn(xtl), FadeIn(ylab), run_time=0.6)
        self.say(L("Một lasso lớn hơn: n = 50 mẫu, p = 100 biến, λ = 0,1·‖Aᵀb‖∞. Trục dọc là F − F* theo thang log.",
                   "A bigger lasso: n = 50 samples, p = 100 variables, λ = 0.1·‖Aᵀb‖∞. The vertical axis is F − F* on a log scale."), hold=7.0)
        ks = np.arange(K + 1)
        cI = curve(lx, ks, lg(E1[:K + 1] - FS2), SKY); cF = curve(lx, ks, lg(E2[:K + 1] - FS2), PINK)
        self.play(Create(cI), Create(cF), run_time=4.0, rate_func=linear)
        self.readout([("tới 10⁻²:   ISTA %d,  FISTA %d" % (H[0][0], H[1][0]) if LANG == "vi" else "to 10⁻²:   ISTA %d,  FISTA %d" % (H[0][0], H[1][0]), WHITE), ("tới 10⁻⁸:   ISTA %d,  FISTA %d" % (H[0][1], H[1][1]) if LANG == "vi" else "to 10⁻⁸:   ISTA %d,  FISTA %d" % (H[0][1], H[1][1]), WHITE)], size=22)
        self.say(L("Lúc đầu FISTA nhanh gấp đôi: tới 10⁻² sau %d vòng so với %d. Rồi đường hồng gợn sóng: F lên xuống, %d lần tăng trong 600 vòng." % (H[1][0], H[0][0], NM),
                   "Early on FISTA is twice as fast: 10⁻² after %d rounds versus %d. Then the pink curve ripples: F goes up and down, %d increases in 600 rounds." % (H[1][0], H[0][0], NM)), hold=8.5)
        self.say(L("Đó là \"gợn sóng Nesterov\" trong bài. Trọng số đà tiến tới 1, nên gần nghiệm điểm vẫn chạy quá rồi quay lại. ISTA giảm đều và gần như đuổi kịp: %d vòng so với %d tới 10⁻⁸." % (H[0][1], H[1][1]),
                   "These are the \"Nesterov ripples\" of the lesson. The momentum weight goes to 1, so near the solution the point still runs past and comes back. ISTA decreases steadily and almost catches up: %d rounds versus %d to 10⁻⁸." % (H[0][1], H[1][1])), hold=9.5)
        self.readout([("κ(AᵀA) = 3 (bài 2 biến, điều kiện tốt):" if LANG == "vi" else "κ(AᵀA) = 3 (2-variable problem, well conditioned):", WHITE), ("tới 10⁻⁸:  ISTA %d,  FISTA %d" % (K3[0], K3[1]) if LANG == "vi" else "to 10⁻⁸:  ISTA %d,  FISTA %d" % (K3[0], K3[1]), PINK)], size=22)
        self.say(L("Khi bài toán có điều kiện tốt, đà còn có thể làm chậm: với κ = 3, ISTA cần %d vòng, FISTA cần %d. ISTA đã hội tụ tuyến tính nhanh, đà chỉ thêm dao động." % (K3[0], K3[1]),
                   "When the problem is well conditioned, momentum can even slow things down: with κ = 3, ISTA needs %d rounds, FISTA needs %d. ISTA already converges linearly and fast; momentum only adds oscillation." % (K3[0], K3[1])), hold=8.0)
        e3 = E3[:K + 1] - FS2; kz = int(np.argmax(e3 < 1e-9)) if (e3 < 1e-9).any() else K
        cR = curve(lx, ks[:kz + 1], lg(e3[:kz + 1]), MINT)
        self.play(Create(cR), run_time=2.0, rate_func=linear)
        self.readout([("khởi động lại: k ← 1 khi F tăng" if LANG == "vi" else "restart: k ← 1 when F goes up", MINT), ("tới 10⁻⁸:  ISTA %d,  FISTA %d,  restart %d" % (H[0][1], H[1][1], H[2][1]) if LANG == "vi" else "to 10⁻⁸:  ISTA %d,  FISTA %d,  restart %d" % (H[0][1], H[1][1], H[2][1]), WHITE)], size=22)
        self.say(L("Cách sửa chuẩn (bài 09-05-04): khởi động lại. Khi F tăng, đặt lại k = 1 để bỏ đà. Đường xanh lá giảm đều và tới 10⁻⁸ chỉ sau %d vòng." % H[2][1],
                   "The standard fix (lesson 09-05-04): restart. When F goes up, reset k = 1 to drop the momentum. The green curve decreases steadily and reaches 10⁻⁸ after only %d rounds." % H[2][1]), hold=8.5)
        self.say(L("Kiểm tra F tăng chỉ tốn thêm một lần tính F mỗi vòng. Ở đây việc khởi động lại xảy ra ở các vòng %d, %d, %d, ..." % tuple(RS[:3]),
                   "Checking whether F went up costs one extra evaluation of F per round. Here restarts happen at rounds %d, %d, %d, ..." % tuple(RS[:3])), hold=6.0)
        self.takeaway([L("ISTA: bước gradient trên g, rồi ngưỡng mềm. F − F* = O(1/k).", "ISTA: gradient step on g, then soft thresholding. F − F* = O(1/k)."),
                       L("FISTA: cùng bước prox tại điểm ngoại suy v, trọng số (k − 2)/(k + 1). O(1/k²).", "FISTA: the same prox step at the extrapolated point v, weight (k − 2)/(k + 1). O(1/k²)."),
                       L("FISTA không đơn điệu: có gợn sóng Nesterov.", "FISTA is not monotone: Nesterov ripples."),
                       L("Khởi động lại khi F tăng: giữ tốc độ, bỏ dao động.", "Restart when F goes up: keep the speed, drop the oscillation.")])
