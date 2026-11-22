from rl import *
# F(w) = ½ wᵀ diag(1, 100) w  (bài 26-02), w₀ = (−10, 1)
A = np.diag([1., 100.]); W0 = np.array([-10., 1.])
def run(kind, eta, beta, n=6000, tol=1e-4):
    w = W0.copy(); v = np.zeros(2); P = [w.copy()]; V = [v.copy()]
    for k in range(n):
        g = A @ (w - eta * beta * v) if kind == 'nag' else A @ w
        v = beta * v + g; w = w - eta * v; P.append(w.copy()); V.append(v.copy())
        if not np.isfinite(w).all() or np.linalg.norm(w) > 1e6: return None, np.array(P), V
        if np.linalg.norm(w) <= tol: return k + 1, np.array(P), V
    return None, np.array(P), V
NZ, PZ, _ = run('hb', .019, 0)
assert abs(PZ[1][1] + 0.9) < 1e-12 and abs(PZ[1][0] + 9.81) < 1e-12 and NZ == 601
E, B = .013, .9
NG, PG, _ = run('hb', E, 0); NH, PH, VH = run('hb', E, B); NN, PN, VN = run('nag', E, B)
assert (NG, NH, NN) == (880, 169, 144) and NN < NH < NG
OH, ON = PH[:, 0].max(), PN[:, 0].max(); assert abs(OH - 2.055) < 1e-3 and abs(ON - 1.598) < 1e-3
BS = [.5, .8, .9, .95, .99]; NB = [run('hb', E, b)[0] for b in BS]
assert NB == [426, 110, 169, 350, 1581] and min(NB) == NB[1] and NB[-1] > NG
N5, P5, _ = run('hb', E, .5); N99, P99, _ = run('hb', E, .99); N8, P8, _ = run('hb', E, .8)
assert N99 > 400 and N8 < 400 and N5 > 400 and P99[:, 0].max() < 9 and abs(P99[:, 1]).max() < 1.25 and P5[:, 0].max() < 0
NH19 = run('hb', .019, .9)[0]; NN19, PN19, _ = run('nag', .019, .9)
assert NH19 == 181 and NN19 is None and np.linalg.norm(PN19[-1]) > 1e6
LIM = 2 * (1 + B) / (1 + 2 * B); assert 1.3 < LIM < 1.36 and .019 * 100 > LIM and E * 100 < LIM
ES, BSt = (2 / (1 + 10)) ** 2, ((10 - 1) / (10 + 1)) ** 2; NGoh = run('hb', ES, BSt)[0]
assert NGoh == 73 and abs(ES - .0331) < 1e-4 and abs(BSt - .6694) < 1e-4
gain_s = sum(B ** j for j in range(400)); gain_a = abs(sum((-B) ** j for j in range(400)))
assert abs(gain_s - 10) < 1e-9 and abs(gain_a - 1 / 1.9) < 1e-9
# look-ahead tại bước 2 của Nesterov (cùng trạng thái w, v)
w2, v2 = PN[2], VN[2]; mom = -E * B * v2; wl = w2 + mom
gh = -E * (A @ w2); gn = -E * (A @ wl); hb_new = wl + gh; nag_new = wl + gn
assert np.allclose(nag_new, PN[3]) and abs((A @ wl)[1] - 110.79) < 1e-6 and abs((A @ w2)[1] - 44.1) < 1e-6
assert hb_new[1] > w2[1] and nag_new[1] < 0

def multi(sc, ax, paths, dots, cols, ks, rt, width=4, cb=None, start=0):
    segs = []; prev = start
    for k in ks:
        an = []
        for P, d, c in zip(paths, dots, cols):
            a, b = min(prev, len(P) - 1), min(k, len(P) - 1)
            if a == b: continue
            s = VMobject(color=c, stroke_width=width).set_points_as_corners([ax.c2p(*P[j]) for j in range(a, b + 1)]); segs.append(s)
            an += [Create(s), d.animate.move_to(ax.c2p(*P[b]))]
        if an: sc.play(*an, run_time=rt(k) if callable(rt) else rt, rate_func=linear)
        prev = k
        if cb: cb(k)
    sc.remove(*segs); g = VGroup(*segs); sc.add(g); sc.bring_to_front(*dots); return g

Fx = lambda x, y: 0.5 * (x * x + 100 * y * y)
LV = [0.5, 2, 6, 14, 26, 42, 62]

class Mom(Reel):
    def valley(self, xr, c=(0, 1.7, 0), h=4.4):
        ax = plain_axes(xr, [-1.3, 1.3], 7.8, h, list(c))
        cs = contours(ax, Fx, LV, (xr[0], xr[1], -1.3, 1.3), N=90)
        return ax, cs

    def construct(self):
        self.title(L("Momentum và Nesterov:\nđi nhanh trong thung lũng hẹp", "Momentum and Nesterov:\nmoving fast in a narrow valley"))
        self.stage(1)
        ax, cs = self.valley([-11, 3])
        self.play(Create(cs), run_time=1.2)
        star = Dot(ax.c2p(0, 0), radius=0.1, color=MINT); self.add(star)
        lab = Text("w*", font=FONT, font_size=24, color=MINT).next_to(star, UP, buff=0.12); self.add(lab)
        self.say(L("Bài toán trong bài 26-02: F(w) = ½(w₁² + 100·w₂²). Cực tiểu tại w* = (0; 0).",
                   "The problem from lesson 26-02: F(w) = ½(w₁² + 100·w₂²). Minimum at w* = (0, 0)."))
        self.say(L("Độ cong theo w₂ gấp 100 lần theo w₁. Số điều kiện κ = 100: thung lũng dài và hẹp. (Hình đã giãn trục dọc cho dễ nhìn.)",
                   "The curvature along w₂ is 100 times that along w₁. Condition number κ = 100: a long, narrow valley. (The vertical axis is stretched.)"), hold=6.0)
        self.readout(["∇F(w) = (w₁; 100·w₂)" if LANG == "vi" else "∇F(w) = (w₁, 100·w₂)", "GD:  w ← w − η·∇F(w)"], color=SUN, size=24)
        self.say(L("Gradient descent: w ← w − η·∇F(w). Theo w₂, mỗi bước nhân với (1 − 100η). Muốn không nổ thì phải có η < 2/100 = 0,02.",
                   "Gradient descent: w ← w − η·∇F(w). Along w₂ each step multiplies by (1 − 100η). To stay stable we need η < 2/100 = 0.02."), hold=6.5)
        d = Dot(ax.c2p(*W0), radius=0.12, color=SKY); self.add(d)
        self.say(L("Thử η = 0,019, sát giới hạn. Xuất phát từ w₀ = (−10; 1).", "Try η = 0.019, close to the limit. Start from w₀ = (−10, 1)."), wait=False)
        def rz(k):
            self.readout(["η = %s,  k = %d" % (nf(.019, 3), k), "w = %s" % vec(PZ[k], 3), ("‖w‖ = %s" % nf(np.linalg.norm(PZ[k]), 3), WHITE)], color=SKY, size=23)
        pz = trail(self, ax, PZ, d, SKY, rt=lambda k: 0.5 if k < 6 else 0.12, ks=range(1, 41), cb=rz, width=3)
        self.say(L("Theo w₂: 1 − 100·0,019 = −0,9. Dấu đổi liên tục, điểm nảy qua lại giữa hai vách.",
                   "Along w₂: 1 − 100·0.019 = −0.9. The sign flips every step, so the point bounces between the walls."), hold=5.1)
        self.say(L("Theo w₁: 1 − 0,019 = 0,981. Mỗi bước chỉ tiến 1,9%%. Cần %d bước để ‖w‖ ≤ 10⁻⁴." % NZ,
                   "Along w₁: 1 − 0.019 = 0.981. Each step gains only 1.9%%. It takes %d steps to reach ‖w‖ ≤ 10⁻⁴." % NZ), hold=5.6)
        self.say(L("Đây là zíc-zắc: bước lớn thì nảy vách, bước nhỏ thì bò dọc thung lũng. GD không có trí nhớ.",
                   "This is the zigzag: a big step bounces off the walls, a small step crawls along the valley. GD has no memory."), hold=5.1)
        # ---- stage 2
        self.stage(2); self.wipe()
        hb = para(L("Heavy ball (Polyak):", "Heavy ball (Polyak):"), 28, SUN).move_to([0, 4.0, 0])
        f1 = Text("v ← β·v + ∇F(w)", font=MONO, font_size=30, color=WHITE).move_to([0, 3.3, 0])
        f2 = Text("w ← w − η·v", font=MONO, font_size=30, color=WHITE).move_to([0, 2.7, 0])
        self.play(FadeIn(hb), FadeIn(f1), FadeIn(f2), run_time=0.6)
        self.say(L("Thêm một vận tốc v. Mỗi bước, v giữ lại một phần β của chính nó rồi cộng gradient mới.",
                   "Add a velocity v. Each step, v keeps a fraction β of itself and adds the new gradient."), hold=5.1)
        f3 = Text("v = ∇F(k) + β·∇F(k−1) + β²·∇F(k−2) + …", font=MONO, font_size=26, color=SKY).move_to([0, 1.9, 0])
        fit(f3, 7.8); self.play(FadeIn(f3), run_time=0.4)
        self.say(L("Khai triển ra: v là tổng các gradient cũ, gradient càng cũ thì trọng số càng nhỏ: 1, β, β², β³, …",
                   "Unrolled: v is a sum of past gradients, older ones weighted less: 1, β, β², β³, …"), hold=4.7)
        # filter picture: same sign vs alternating
        def stack(sign, x0, col):
            g = VGroup(); y = 1.25
            for j in range(8):
                s = (1 if sign > 0 else (-1) ** j) * B ** j
                ar = Arrow([x0, y, 0], [x0 + 1.1 * s, y, 0], buff=0, color=col, stroke_width=5, max_tip_length_to_length_ratio=0.25)
                g.add(ar); y -= 0.36
            return g
        s1 = stack(1, -3.3, MINT); s2 = stack(-1, 1.4, PINK)
        t1 = para(L("cùng dấu (dọc thung lũng)", "same sign (along the valley)"), 22, MINT, 3.8).move_to([-2.2, -1.95, 0])
        t2 = para(L("đổi dấu (giữa hai vách)", "alternating (wall to wall)"), 22, PINK, 3.8).move_to([2.2, -1.95, 0])
        self.play(LaggedStart(*[GrowArrow(a) for a in s1], lag_ratio=0.15), LaggedStart(*[GrowArrow(a) for a in s2], lag_ratio=0.15), FadeIn(t1), FadeIn(t2), run_time=2.0)
        self.readout([("β = %s:  tổng cùng dấu = 1/(1−β) = %s" % (nf(B, 1), nf(gain_s, 0)) if LANG == "vi" else "β = %s:  same-sign sum = 1/(1−β) = %s" % (nf(B, 1), nf(gain_s, 0)), MINT),
                      ("        tổng đổi dấu = 1/(1+β) ≈ %s" % nf(gain_a, 2) if LANG == "vi" else "        alternating sum = 1/(1+β) ≈ %s" % nf(gain_a, 2), PINK)], size=22)
        self.say(L("Với β = 0,9: phần gradient luôn cùng dấu được nhân lên tới 10 lần. Phần đổi dấu mỗi bước bị triệt, chỉ còn khoảng 0,53.",
                   "With β = 0.9: the part of the gradient that keeps its sign is amplified up to 10 times. The part that flips every step cancels to about 0.53."), hold=7.0)
        self.say(L("Đó là bộ lọc thông thấp: hướng dọc thung lũng được tăng tốc, dao động giữa hai vách tắt dần.",
                   "It is a low-pass filter: motion along the valley speeds up, the wall-to-wall oscillation dies out."), hold=5.1)
        self.play(FadeOut(VGroup(s1, s2, t1, t2, f3)), run_time=0.4); self.clear_ro()
        nv = para(L("Nesterov: tính gradient ở điểm nhìn trước", "Nesterov: take the gradient at a look-ahead point"), 27, MINT).move_to([0, 1.9, 0])
        f4 = Text("v ← β·v + ∇F(w − η·β·v)", font=MONO, font_size=28, color=MINT).move_to([0, 1.2, 0])
        self.play(FadeIn(nv), FadeIn(f4), run_time=0.5)
        self.say(L("Nesterov chỉ đổi một chỗ: gradient không tính tại w, mà tại điểm w − η·β·v, nơi vận tốc sắp đưa ta tới.",
                   "Nesterov changes one thing: the gradient is taken not at w but at w − η·β·v, where the velocity is about to carry us."), hold=6.0)
        # look-ahead diagram (real numbers, step 2 of Nesterov with η = 0.013, β = 0.9)
        self.play(FadeOut(VGroup(hb, f1, f2, nv)), f4.animate.move_to([0, 4.0, 0]), run_time=0.5)
        zx = plain_axes([-9.75, -9.15], [-0.5, 1.3], 6.0, 5.4, [0, 0.55, 0])
        P0, P1, PHb, PNg = (zx.c2p(*p) for p in (w2, wl, hb_new, nag_new))
        dw = Dot(P0, radius=0.1, color=WHITE); lw = Text("w", font=FONT, font_size=24).next_to(dw, LEFT, buff=0.12)
        a_m = Arrow(P0, P1, buff=0, color=ORANGE, stroke_width=6, max_tip_length_to_length_ratio=0.12)
        l_m = Text("−η·β·v", font=MONO, font_size=22, color=ORANGE).next_to(a_m.get_center(), LEFT, buff=0.2)
        dl = Dot(P1, radius=0.09, color=ORANGE)
        self.play(FadeIn(dw), FadeIn(lw), run_time=0.3); self.play(GrowArrow(a_m), FadeIn(l_m), FadeIn(dl), run_time=0.6)
        self.say(L("Số thật ở bước 2 (η = 0,013; β = 0,9). Mũi tên cam: phần quán tính. Nó đẩy w₂ đi lên, vượt qua đáy.",
                   "Real numbers at step 2 (η = 0.013, β = 0.9). Orange arrow: the inertia part. It pushes w₂ upward, past the floor."), hold=5.6)
        a_h = Arrow(P1, PHb, buff=0, color=SUN, stroke_width=5, max_tip_length_to_length_ratio=0.2)
        l_h = Text("−η·∇F(w)", font=MONO, font_size=22, color=SUN).next_to(PHb, RIGHT, buff=0.15)
        self.play(GrowArrow(a_h), FadeIn(l_h), run_time=0.6)
        self.readout([("heavy ball: ∂F/∂w₂ tại w = %s" % nf((A @ w2)[1], 1) if LANG == "vi" else "heavy ball: ∂F/∂w₂ at w = %s" % nf((A @ w2)[1], 1), SUN)], size=22)
        self.say(L("Heavy ball cộng gradient tính tại w (vàng). Độ dốc ở đó còn nhỏ, nên bước mới vẫn đi lên: w₂ thành %s." % nf(hb_new[1], 2),
                   "Heavy ball adds the gradient taken at w (yellow). The slope there is still small, so the new step still goes up: w₂ becomes %s." % nf(hb_new[1], 2)), hold=6.0)
        a_n = Arrow(P1, PNg, buff=0, color=MINT, stroke_width=5, max_tip_length_to_length_ratio=0.12)
        l_n = Text("−η·∇F(w − ηβv)", font=MONO, font_size=22, color=MINT).next_to(PNg, RIGHT, buff=0.15)
        self.play(GrowArrow(a_n), FadeIn(l_n), run_time=0.6)
        self.readout([("heavy ball: ∂F/∂w₂ tại w = %s" % nf((A @ w2)[1], 1) if LANG == "vi" else "heavy ball: ∂F/∂w₂ at w = %s" % nf((A @ w2)[1], 1), SUN),
                      ("Nesterov:   ∂F/∂w₂ nhìn trước = %s" % nf((A @ wl)[1], 1) if LANG == "vi" else "Nesterov:   look-ahead ∂F/∂w₂ = %s" % nf((A @ wl)[1], 1), MINT)], size=22)
        self.say(L("Nesterov hỏi độ dốc tại điểm cam. Ở đó dốc hơn nhiều (%s so với %s), nên phanh sớm: w₂ quay xuống %s." % (nf((A @ wl)[1], 1), nf((A @ w2)[1], 1), nf(nag_new[1], 2)),
                   "Nesterov asks for the slope at the orange point. It is much steeper there (%s vs %s), so it brakes early: w₂ turns down to %s." % (nf((A @ wl)[1], 1), nf((A @ w2)[1], 1), nf(nag_new[1], 2))), hold=7.0)
        self.say(L("Nhìn trước một bước giúp sửa hướng sớm hơn một nhịp, nên dao động nhỏ hơn.",
                   "Looking one step ahead corrects the direction one beat earlier, so the oscillation is smaller."), hold=4.2)
        # ---- stage 3
        self.stage(3); self.wipe()
        ax, cs = self.valley([-11, 3]); self.play(Create(cs), run_time=1.0)
        self.add(Dot(ax.c2p(0, 0), radius=0.1, color=MINT))
        lg = VGroup(*[Text(tr(s), font=FONT, font_size=21, color=c) for s, c in ((L("GD (β = 0)", "GD (β = 0)"), SKY), (L("heavy ball β = 0,9", "heavy ball β = 0.9"), SUN), (L("Nesterov β = 0,9", "Nesterov β = 0.9"), MINT))])
        lg.arrange(RIGHT, buff=0.35); fit(lg, 7.8).move_to([0, 4.2, 0]); self.add(lg)
        self.say(L("Ba phương pháp, cùng hàm, cùng điểm đầu, cùng bước η = 0,013. Chỉ khác cách dùng gradient.",
                   "Three methods, same function, same start, same step η = 0.013. They differ only in how they use the gradient."), hold=5.1)
        dots = [Dot(ax.c2p(*W0), radius=0.11, color=c) for c in (SKY, SUN, MINT)]; self.add(*dots)
        def r3(k):
            self.readout([("k = %d" % k, WHITE), ("GD         w = %s" % vec(PG[min(k, len(PG) - 1)], 2), SKY), ("heavy ball w = %s" % vec(PH[min(k, len(PH) - 1)], 2), SUN), ("Nesterov   w = %s" % vec(PN[min(k, len(PN) - 1)], 2), MINT)], size=22)
        g3 = multi(self, ax, [PG, PH, PN], dots, [SKY, SUN, MINT], range(1, 61), rt=lambda k: 0.45 if k <= 8 else 0.14, width=3, cb=r3)
        self.say(L("Sau 60 bước: GD mới đi được một đoạn. Hai phương pháp có quán tính đã tới gần đáy và vượt qua w₁ = 0.",
                   "After 60 steps: GD has covered only a short stretch. The two momentum methods are near the bottom and have overshot w₁ = 0."), hold=6.0)
        g4 = multi(self, ax, [PG, PH, PN], dots, [SKY, SUN, MINT], range(64, 181, 4), rt=0.1, width=3, cb=r3, start=60)
        self.readout([("vượt quá w₁ = 0 nhiều nhất:" if LANG == "vi" else "largest overshoot past w₁ = 0:", WHITE), ("heavy ball  w₁ = %s" % nf(OH, 2), SUN), ("Nesterov    w₁ = %s" % nf(ON, 2), MINT)], size=23)
        self.say(L("Cả hai đều vượt đáy rồi quay lại, như quả bóng lăn. Heavy ball vượt tới w₁ = %s, Nesterov chỉ tới %s." % (nf(OH, 2), nf(ON, 2)),
                   "Both overshoot the bottom and roll back, like a ball. Heavy ball overshoots to w₁ = %s, Nesterov only to %s." % (nf(OH, 2), nf(ON, 2))), hold=6.0)
        self.readout([("số bước tới ‖w‖ ≤ 10⁻⁴:" if LANG == "vi" else "steps to ‖w‖ ≤ 10⁻⁴:", WHITE), ("GD          %4d" % NG, SKY), ("heavy ball  %4d" % NH, SUN), ("Nesterov    %4d" % NN, MINT)], size=24)
        self.say(L("Đếm số bước tới ‖w‖ ≤ 10⁻⁴: GD cần %d, heavy ball %d, Nesterov %d. Momentum nhanh hơn khoảng 5–6 lần." % (NG, NH, NN),
                   "Steps to reach ‖w‖ ≤ 10⁻⁴: GD needs %d, heavy ball %d, Nesterov %d. Momentum is about 5–6 times faster." % (NG, NH, NN)), hold=6.5)
        # ---- stage 4
        self.stage(4); self.wipe()
        tx = plain_axes([0, 400], [-10.5, 10.5], 7.4, 3.6, [0.2, 2.1, 0], ticks=False)
        zl = DashedLine(tx.c2p(0, 0), tx.c2p(400, 0), color=DIM, stroke_width=2)
        yl = Text("w₁", font=FONT, font_size=22, color=DIM).next_to(tx.c2p(0, 10.5), LEFT, buff=0.12)
        xl = Text("k = 400", font=MONO, font_size=20, color=DIM).next_to(tx.c2p(400, -10.5), DOWN, buff=0.1)
        self.play(Create(tx), Create(zl), FadeIn(yl), FadeIn(xl), run_time=0.6)
        self.say(L("β là ma sát. Cùng η = 0,013, vẽ w₁ theo số bước k cho heavy ball với ba giá trị β.",
                   "β is friction. Same η = 0.013: plot w₁ against the step count k for heavy ball with three values of β."), hold=4.7)
        curves = VGroup(); labs = VGroup()
        for P, c, bl in ((P5, SKY, "β = 0,5" if LANG == "vi" else "β = 0.5"), (P8, MINT, "β = 0,8" if LANG == "vi" else "β = 0.8"), (P99, PINK, "β = 0,99" if LANG == "vi" else "β = 0.99")):
            n = min(401, len(P)); cv = VMobject(color=c, stroke_width=3).set_points_as_corners([tx.c2p(k, P[k][0]) for k in range(n)])
            curves.add(cv); labs.add(Text(bl, font=MONO, font_size=21, color=c))
        labs.arrange(RIGHT, buff=0.5).move_to([0, 4.25, 0])
        for cv, lb in zip(curves, labs):
            self.play(FadeIn(lb), Create(cv), run_time=2.2, rate_func=linear)
        self.say(L("β = 0,5 (xanh): ma sát nhiều, w₁ bò chậm về 0. β = 0,99 (hồng): ma sát quá ít, lắc qua lại tới w₁ ≈ %s rồi mới tắt dần." % nf(P99[:, 0].max(), 1),
                   "β = 0.5 (blue): much friction, w₁ crawls toward 0. β = 0.99 (pink): too little friction, it swings out to w₁ ≈ %s and dies out slowly." % nf(P99[:, 0].max(), 1)), hold=6.5)
        self.say(L("β = 0,8 (xanh lá): vượt qua 0 một chút rồi về đích nhanh nhất.", "β = 0.8 (green): overshoots 0 a little, then arrives fastest."), hold=3.7)
        # bar chart of steps vs beta
        bars = VGroup(); mx = max(NB + [NG])
        rows = [(nf(0, 2), NG)] + [(nf(b, 2), n) for b, n in zip(BS, NB)]
        for i, (bl, n) in enumerate(rows):
            y = -0.05 - 0.4 * i
            col = MINT if n == min(NB) else (PINK if n > NG else SKY)
            r = Rectangle(width=4.6 * n / mx, height=0.3, fill_color=col, fill_opacity=0.85, stroke_width=0).move_to([-2.0, y, 0], aligned_edge=LEFT)
            bars.add(VGroup(Text("β = " + bl, font=MONO, font_size=20, color=WHITE).move_to([-3.0, y, 0]), r, Text(str(n), font=MONO, font_size=20, color=col).next_to(r, RIGHT, buff=0.12)))
        self.play(LaggedStart(*[FadeIn(b, shift=RIGHT * 0.2) for b in bars], lag_ratio=0.15), run_time=1.5)
        self.say(L("Số bước theo β: tốt nhất quanh β = 0,8 (%d bước). β = 0,99 cần %d bước, còn chậm hơn GD thuần (%d)." % (NB[1], NB[-1], NG),
                   "Steps versus β: best near β = 0.8 (%d steps). β = 0.99 needs %d steps, even slower than plain GD (%d)." % (NB[1], NB[-1], NG)), hold=6.5)
        self.say(L("Nếu biết κ, có công thức cho cặp tốt nhất: η* = %s, β* = %s, heavy ball chỉ cần %d bước. Thực tế thường dùng β = 0,9." % (nf(ES, 4), nf(BSt, 3), NGoh),
                   "If κ is known there is a formula for the best pair: η* = %s, β* = %s, and heavy ball needs only %d steps. In practice people use β = 0.9." % (nf(ES, 4), nf(BSt, 3), NGoh)), hold=7.0)
        self.play(FadeOut(bars), run_time=0.3)
        self.readout([("η = %s,  β = %s:" % (nf(.019, 3), nf(B, 1)), WHITE), ("heavy ball  hội tụ sau %d bước" % NH19 if LANG == "vi" else "heavy ball  converges in %d steps" % NH19, SUN),
                      ("Nesterov    nổ: ‖w‖ > 10⁶ sau %d bước" % (len(PN19) - 1) if LANG == "vi" else "Nesterov    blows up: ‖w‖ > 10⁶ after %d steps" % (len(PN19) - 1), PINK)], y=-1.0, size=22)
        self.say(L("Nhưng nhìn trước không miễn phí. Ở η = 0,019 (bước sát giới hạn của GD), heavy ball vẫn hội tụ, Nesterov với β = 0,9 thì nổ.",
                   "But look-ahead is not free. At η = 0.019 (near GD's limit), heavy ball still converges, while Nesterov with β = 0.9 blows up."), hold=6.5)
        self.say(L("Với β hằng, Nesterov cần η·L < 2(1+β)/(1+2β) ≈ %s. Ở đây L = 100 nên phải có η < %s." % (nf(LIM, 2), nf(LIM / 100, 4)),
                   "With constant β, Nesterov needs η·L < 2(1+β)/(1+2β) ≈ %s. Here L = 100, so η < %s." % (nf(LIM, 2), nf(LIM / 100, 4))), hold=6.0)
        self.takeaway([L("GD trong thung lũng hẹp: nảy giữa hai vách và bò dọc đáy (%d bước)." % NG, "GD in a narrow valley: bounces between the walls and crawls along the floor (%d steps)." % NG),
                       L("Momentum cộng dồn gradient cũ: hướng cùng dấu được tăng tốc, dao động bị triệt (%d bước)." % NH, "Momentum sums past gradients: consistent directions speed up, oscillation cancels (%d steps)." % NH),
                       L("Nesterov tính gradient ở điểm nhìn trước nên phanh sớm hơn (%d bước), nhưng cần bước nhỏ hơn." % NN, "Nesterov takes the gradient at a look-ahead point and brakes earlier (%d steps), but needs a smaller step." % NN),
                       L("β là ma sát: quá nhỏ thì bò, quá lớn thì lắc lư. β = 0,9 là mặc định an toàn.", "β is friction: too small and it crawls, too large and it swings. β = 0.9 is a safe default.")])
