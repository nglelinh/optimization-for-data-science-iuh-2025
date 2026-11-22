from rl import *
# Bài 28-01 / 28-02: điểm yên ngựa, GD bị kẹt, thoát nhờ nhiễu
# Gần gốc F ≈ x² − y² (bài tập 28-01); thêm ½y⁴ để hàm có đáy.
F = lambda w: w[0] ** 2 - w[1] ** 2 + .5 * w[1] ** 4
G = lambda w: np.array([2 * w[0], -2 * w[1] + 2 * w[1] ** 3])
H = lambda w: np.diag([2., -2 + 6 * w[1] ** 2])
ETA = 0.1
for c in ([0, 0], [0, 1], [0, -1]): assert np.linalg.norm(G(np.array(c, float))) == 0
assert np.allclose(np.linalg.eigvalsh(H(np.zeros(2))), [-2, 2]) and np.allclose(np.linalg.eigvalsh(H(np.array([0, 1.]))), [2, 4]) and F(np.array([0, 1.])) == -0.5
# bài tập 28-01 trên x² − y², η = 0,1
w = np.array([0, 1e-3]); EX = []
for _ in range(2): w = w - ETA * np.array([2 * w[0], -2 * w[1]]); EX.append(w.copy())
assert np.allclose(EX[0], [0, 1.2e-3]) and np.allclose(EX[1], [0, 1.44e-3])
def gd(w0, n=150, pert=None, sgd=None, seed=0):
    rng = np.random.default_rng(seed); w = np.array(w0, float); P = [w.copy()]; last = -99; kicks = []
    for k in range(n):
        g = G(w)
        if sgd: g = g + sgd * rng.standard_normal(2)
        w = w - ETA * g
        if pert and np.linalg.norm(G(w)) < pert[0] and k - last > pert[2]:
            u = rng.standard_normal(2); u /= np.linalg.norm(u); w = w + pert[1] * u * rng.random() ** .5; last = k; kicks.append(k + 1)
        P.append(w.copy())
    return np.array(P), kicks
PA, _ = gd([1.5, 0]); PB, _ = gd([1.5, 1e-8]); PC, KC = gd([1.5, 0], pert=(1e-3, 0.1, 20), seed=2); PD, _ = gd([1.5, 0], sgd=0.05, seed=0)
FA, FB, FC, FD = [np.array([F(p) for p in P]) for P in (PA, PB, PC, PD)]
esc = lambda Fk: int(np.argmax(Fk < -0.25)) if (Fk < -0.25).any() else None
EA, EB, EC, ED = esc(FA), esc(FB), esc(FC), esc(FD)
assert EA is None and abs(FA[-1]) < 1e-25 and np.linalg.norm(G(PA[60])) < 1e-5 and (EB, EC, ED) == (99, 47, 33), (EB, EC, ED)
SB = [k for k in range(EB) if np.linalg.norm(G(PB[k])) < 1e-3]; S0, S1 = SB[0], SB[-1]; assert (S0, S1, len(SB)) == (36, 59, 24)
assert abs(PB[-1][1] - 1) < 1e-6 and abs(abs(PC[-1][1]) - 1) < 0.01 and abs(abs(PD[-1][1]) - 1) < 0.02 and KC[0] == 36
# chiều cao: tỉ lệ ma trận đối xứng ngẫu nhiên có mọi trị riêng dương
rng = np.random.default_rng(0); DS = (1, 2, 3, 4, 5, 6); PR = []
for d in DS:
    M = rng.standard_normal((20000, d, d)); Sm = (M + M.transpose(0, 2, 1)) / 2
    PR.append(float((np.linalg.eigvalsh(Sm) > 0).all(1).mean()))
assert abs(PR[0] - .5) < .01 and abs(PR[1] - .145) < .01 and abs(PR[2] - .027) < .003 and PR[3] < .005 and PR[4] < .001 and PR[5] < PR[4] + 1e-12
Fx = lambda x, y: x * x - y * y + .5 * y ** 4
LVL = [-0.45, -0.35, -0.2, -0.08, 0.3, 0.8, 1.5, 2.4]

class Saddle(Reel):
    def field(self):
        ax = plain_axes([-1.7, 1.7], [-1.4, 1.4], 7.4, 6.1, [0, 1.75, 0])
        cs = contours(ax, Fx, LVL, (-1.7, 1.7, -1.4, 1.4), N=100)
        c0 = contours(ax, Fx, [0.0], (-1.7, 1.7, -1.4, 1.4), N=100, color=SUN, width=2.5)
        return ax, cs, c0

    def construct(self):
        self.title(L("Điểm yên ngựa:\nGD bị kẹt, nhiễu giúp thoát", "Saddle points:\nGD gets stuck, noise helps escape"))
        # ---- stage 1
        self.stage(1)
        ax, cs, c0 = self.field(); self.play(Create(cs), Create(c0), run_time=1.3)
        o = Dot(ax.c2p(0, 0), radius=0.11, color=ORANGE); m1 = Dot(ax.c2p(0, 1), radius=0.11, color=MINT); m2 = Dot(ax.c2p(0, -1), radius=0.11, color=MINT)
        self.add(o, m1, m2)
        self.say(L("Bài 28-01: w là điểm tới hạn nếu ∇F(w) = 0. Hessian H phân loại nó: mọi trị riêng dương là cực tiểu, có cả dương lẫn âm là yên ngựa.",
                   "Lesson 28-01: w is a critical point if ∇F(w) = 0. The Hessian H classifies it: all eigenvalues positive means a minimum, both signs means a saddle."), hold=8.0)
        self.readout(["F(x, y) = x² − y² + ½y⁴", "∇F = (2x; 2y³ − 2y)" if LANG == "vi" else "∇F = (2x, 2y³ − 2y)"], color=SUN, size=24)
        self.say(L("Ví dụ: F = x² − y² + ½y⁴. Gần gốc F ≈ x² − y², đúng hàm trong bài tập 28-01. Số hạng ½y⁴ chỉ để hàm có đáy.",
                   "Example: F = x² − y² + ½y⁴. Near the origin F ≈ x² − y², the function of exercise 28-01. The ½y⁴ term only gives the function a bottom."), hold=7.5)
        self.readout([("(0; 0): H = diag(2; −2) ⇒ yên ngựa, F = 0" if LANG == "vi" else "(0, 0): H = diag(2, −2) ⇒ saddle, F = 0", ORANGE), ("(0; ±1): H = diag(2; 4) ⇒ cực tiểu, F = −0,5" if LANG == "vi" else "(0, ±1): H = diag(2, 4) ⇒ minima, F = −0.5", MINT)], size=23)
        self.say(L("Ba điểm tới hạn. Gốc là yên ngựa: đi theo x thì F tăng, theo y thì F giảm. Hai cực tiểu ở (0; ±1). Đường vàng là mức F = 0 qua yên ngựa.",
                   "Three critical points. The origin is a saddle: along x F goes up, along y F goes down. Two minima at (0, ±1). The yellow curve is the level F = 0 through the saddle."), hold=8.5)
        # ---- stage 2
        self.stage(2)
        self.readout([("gần gốc:  x ← (1 − 2η)·x = 0,8·x" if LANG == "vi" else "near 0:  x ← (1 − 2η)·x = 0.8·x", SKY), ("         y ← (1 + 2η)·y = 1,2·y" if LANG == "vi" else "        y ← (1 + 2η)·y = 1.2·y", PINK)], size=23)
        self.say(L("GD với η = 0,1 gần gốc: theo x mỗi bước nhân 0,8 (bị hút vào), theo y nhân 1,2 (bị đẩy ra). Hướng y là hướng độ cong âm.",
                   "GD with η = 0.1 near the origin: along x each step multiplies by 0.8 (pulled in), along y by 1.2 (pushed out). The y direction is the negative-curvature direction."), hold=8.0)
        self.readout([("(0; 10⁻³) → (0; 0,0012) → (0; 0,00144)" if LANG == "vi" else "(0, 10⁻³) → (0, 0.0012) → (0, 0.00144)", PINK), ("(0; 0) → (0; 0) → (0; 0) → ...  mãi mãi" if LANG == "vi" else "(0, 0) → (0, 0) → (0, 0) → ...  forever", ORANGE)], size=23)
        self.say(L("Bài tập 28-01: từ (0; 10⁻³), hai bước cho (0; 0,0012) rồi (0; 0,00144): rời yên ngựa, nhưng rất chậm lúc đầu. Từ đúng (0; 0) thì ∇F = 0, GD không bao giờ nhúc nhích.",
                   "Exercise 28-01: from (0, 10⁻³), two steps give (0, 0.0012) then (0, 0.00144): leaving the saddle, but very slowly at first. From exactly (0, 0), ∇F = 0 and GD never moves."), hold=9.5)
        # ---- stage 3
        self.stage(3); self.clear_ro()
        dA = Dot(ax.c2p(1.5, 0), radius=0.1, color=SKY); self.add(dA)
        def ra(k): self.readout([("GD từ (1,5; 0):  k = %d" % k if LANG == "vi" else "GD from (1.5, 0):  k = %d" % k, SKY), ("‖∇F‖ = %s,  F = %s" % (sci(np.linalg.norm(G(PA[k])), 1), nf(FA[k], 3)), WHITE)], size=22)
        pa = trail(self, ax, PA, dA, SKY, rt=lambda k: 0.35 if k < 8 else 0.1, ks=range(1, 41), cb=ra, width=3)
        self.say(L("GD từ (1,5; 0): y = 0 suốt, nên GD trượt thẳng vào yên ngựa. Sau 60 bước ‖∇F‖ < 10⁻⁵: trông như đã hội tụ, nhưng F = 0, không phải −0,5.",
                   "GD from (1.5, 0): y stays 0, so GD slides straight into the saddle. After 60 steps ‖∇F‖ < 10⁻⁵: it looks converged, but F = 0, not −0.5."), hold=8.5)
        dB = Dot(ax.c2p(1.5, 0), radius=0.1, color=PINK); self.add(dB)
        def rb(k): self.readout([("GD từ (1,5; 10⁻⁸):  k = %d" % k if LANG == "vi" else "GD from (1.5, 10⁻⁸):  k = %d" % k, PINK), ("y = %s,  F = %s" % (sci(PB[k][1], 1) if abs(PB[k][1]) < 1e-2 else nf(PB[k][1], 3), nf(FB[k], 3)), WHITE)], size=22)
        pb = trail(self, ax, PB, dB, PINK, rt=lambda k: 0.12, ks=list(range(2, 121, 2)), cb=rb, width=3)
        self.say(L("Lệch chỉ 10⁻⁸ theo y. GD vẫn bị hút về gần yên ngựa: từ bước %d đến %d có ‖∇F‖ < 10⁻³, trông như đã dừng. Rồi y lớn dần và tới gần đáy ở bước %d." % (S0, S1, EB),
                   "An offset of only 10⁻⁸ in y. GD is still pulled near the saddle: from step %d to %d, ‖∇F‖ < 10⁻³ and it looks stopped. Then y grows and it nears the bottom at step %d." % (S0, S1, EB)), hold=9.0)
        self.play(FadeOut(pa), FadeOut(pb), FadeOut(dA), FadeOut(dB), run_time=0.4)
        dC = Dot(ax.c2p(1.5, 0), radius=0.1, color=MINT); dD = Dot(ax.c2p(1.5, 0), radius=0.1, color=ORANGE)
        self.add(dC, dD)
        self.readout([("GD nhiễu: khi ‖∇F‖ < 10⁻³, cộng nhiễu bán kính 0,1" if LANG == "vi" else "perturbed GD: when ‖∇F‖ < 10⁻³, add noise of radius 0.1", MINT), ("kiểu SGD: gradient + nhiễu σ = 0,05 mỗi bước" if LANG == "vi" else "SGD-like: gradient + noise σ = 0.05 every step", dD.get_color())], size=22)
        self.say(L("Bài 28-02: nhiễu giúp thoát. Hai cách, cùng xuất phát (1,5; 0) như đường bị kẹt.",
                   "Lesson 28-02: noise helps escape. Two ways, both starting at (1.5, 0) like the stuck run."), wait=False)
        def multi(paths, dots, cols, ks):
            segs = []; prev = 0
            for k in ks:
                an = []
                for Pp, d, c in zip(paths, dots, cols):
                    s = VMobject(color=c, stroke_width=3).set_points_as_corners([ax.c2p(*Pp[j]) for j in range(prev, k + 1)]); segs.append(s)
                    an += [Create(s), d.animate.move_to(ax.c2p(*Pp[k]))]
                self.play(*an, run_time=0.12, rate_func=linear); prev = k
            g = VGroup(*segs); self.remove(*segs); self.add(g); self.bring_to_front(*dots); return g
        pcd = multi([PC, PD], [dC, dD], [MINT, dD.get_color()], list(range(2, 81, 2)))
        self.say(L("GD nhiễu (xanh lá) đến gần yên ngựa, bị hất một cú ở bước %d, thoát ở bước %d. Nhiễu kiểu SGD (cam) không bao giờ ở yên trên trục, thoát ở bước %d." % (KC[0], EC, ED),
                   "Perturbed GD (green) reaches the saddle, gets one kick at step %d, and escapes at step %d. SGD-like noise (orange) never stays on the axis and escapes at step %d." % (KC[0], EC, ED)), hold=9.0)
        # ---- stage 4
        self.stage(4); self.wipe()
        fx = plain_axes([0, 120], [-0.6, 2.4], 7.4, 4.6, [0.25, 2.2, 0])
        xt = VGroup(*[Text(str(v), font=MONO, font_size=17, color=DIM).next_to(fx.c2p(v, -0.6), DOWN, buff=0.1) for v in (40, 80, 120)])
        yt = VGroup(*[Text(s_, font=MONO, font_size=17, color=DIM).next_to(fx.c2p(0, v), LEFT, buff=0.1) for v, s_ in ((0, "0"), (-0.5, "−0,5" if LANG == "vi" else "−0.5"), (2, "2"))])
        fl = Text("F", font=MONO, font_size=20, color=DIM).next_to(fx.c2p(0, 2.4), UR, buff=0.08)
        self.play(Create(fx), FadeIn(xt), FadeIn(yt), FadeIn(fl), run_time=0.5)
        ks = np.arange(121)
        cv = lambda Fk, c: VMobject(color=c, stroke_width=3.5).set_points_as_corners([fx.c2p(k, Fk[k]) for k in ks])
        cA, cB, cC, cD = cv(FA, SKY), cv(FB, PINK), cv(FC, MINT), cv(FD, ORANGE)
        self.play(Create(cA), Create(cB), Create(cC), Create(cD), run_time=3.0, rate_func=linear)
        self.readout([("tới F < −0,25:" if LANG == "vi" else "reach F < −0.25:", WHITE), ("GD (1,5; 0): không bao giờ" if LANG == "vi" else "GD (1.5, 0): never", SKY), ("GD lệch 10⁻⁸: bước %d" % EB if LANG == "vi" else "GD offset 10⁻⁸: step %d" % EB, PINK), ("GD nhiễu: bước %d,  kiểu SGD: bước %d" % (EC, ED) if LANG == "vi" else "perturbed GD: step %d,  SGD-like: step %d" % (EC, ED), MINT)], size=22)
        self.say(L("Theo F: cả bốn đều có một đoạn bằng phẳng ở F = 0, đó là lúc ngồi gần yên ngựa. Đường xanh dương không bao giờ rời. Có nhiễu thì đoạn phẳng ngắn hơn nhiều.",
                   "In terms of F: all four have a flat stretch at F = 0, the time spent near the saddle. The blue curve never leaves. With noise the flat stretch is much shorter."), hold=9.0)
        self.play(*[FadeOut(m) for m in (fx, xt, yt, fl, cA, cB, cC, cD)], run_time=0.4); self.clear_ro()
        def pct(p_):
            if p_ == 0: return "0 / 20000"
            t_ = ("%.1f%%" if p_ >= 1e-3 else "%.3f%%") % (100 * p_)
            return t_.replace(".", ",") if LANG == "vi" else t_
        rows = VGroup(*[Text("d = %d:  %s" % (d, pct(p_)), font=MONO, font_size=28, color=WHITE) for d, p_ in zip(DS, PR)]).arrange(DOWN, aligned_edge=LEFT, buff=0.28).move_to([0, 1.2, 0])
        hd = Text(L("tỉ lệ ma trận đối xứng ngẫu nhiên d×d\ncó mọi trị riêng dương (20000 mẫu)", "share of random symmetric d×d matrices\nwith all eigenvalues positive (20000 samples)")[LANG], font=FONT, font_size=25, color=SUN).next_to(rows, UP, buff=0.45)
        self.play(FadeIn(hd), FadeIn(rows), run_time=0.7)
        self.say(L("Ở chiều cao thì sao? Nếu Hessian tại điểm tới hạn giống ma trận đối xứng ngẫu nhiên, xác suất mọi trị riêng dương giảm rất nhanh: 50%, 14,5%, 2,7%, ... Ở d = 6 không còn mẫu nào.",
                   "What about high dimensions? If the Hessian at a critical point looks like a random symmetric matrix, the chance that all eigenvalues are positive drops very fast: 50%, 14.5%, 2.7%, ... At d = 6 not a single sample is left."), hold=9.5)
        self.say(L("Vì vậy với hàm chiều cao, hầu hết điểm tới hạn là yên ngựa. \"Kẹt ở cực tiểu địa phương\" thường là chẩn đoán sai: thường là đang ngồi gần yên ngựa.",
                   "So for high-dimensional functions, most critical points are saddles. \"Stuck in a local minimum\" is often the wrong diagnosis: usually it is sitting near a saddle."), hold=8.0)
        self.say(L("Bài 28-02 còn nhắc: momentum có thể giúp vượt qua vùng phẳng nhưng cũng có thể dao động, nên không phải bảo đảm thoát. Bước bậc hai thì đi thẳng theo vector riêng âm nhất của H.",
                   "Lesson 28-02 also notes: momentum can carry you over a flat region but can also oscillate, so it is no escape guarantee. A second-order step walks straight along the most negative eigenvector of H."), hold=9.0)
        self.say(L("Câu hỏi của bài 28-02: nhiễu SGD giảm khi batch B → n. Khi đó cơ chế thoát yên ngựa này yếu dần.",
                   "The question of lesson 28-02: SGD noise shrinks as the batch B → n. Then this escape mechanism gets weaker."), hold=6.0)
        self.takeaway([L("Yên ngựa: ∇F = 0, H có trị riêng âm và dương.", "Saddle: ∇F = 0, H has negative and positive eigenvalues."),
                       L("GD đúng trên trục ổn định thì kẹt mãi; lệch nhỏ thì ngồi lâu rồi mới thoát.", "GD exactly on the stable axis is stuck forever; a tiny offset sits a long time before escaping."),
                       L("‖∇F‖ nhỏ chưa chắc là cực tiểu.", "A small ‖∇F‖ does not mean a minimum."),
                       L("Nhiễu (GD nhiễu, SGD) đẩy ra theo hướng độ cong âm.", "Noise (perturbed GD, SGD) pushes out along negative curvature.")])
