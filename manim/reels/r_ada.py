from rl import *
# f(w) = ½(0,1·w₁² + 10·w₂²): hai tọa độ lệch thang 100 lần; w₀ = (−8, 1,5)
AV = np.array([0.1, 10.]); W0 = np.array([-8., 1.5]); f = lambda w: 0.5 * np.sum(AV * w * w); gr = lambda w: AV * w
def run(kind, eta, n=600):
    w = W0.copy(); P = [w.copy()]; S = []; E = []; G = np.zeros(2); m = np.zeros(2); v = np.zeros(2)
    for k in range(n):
        g = gr(w)
        if kind == 'gd': e = np.array([eta, eta]); st = eta * g
        elif kind == 'ada': G = G + g * g; e = eta / (np.sqrt(G) + 1e-8); st = e * g
        elif kind == 'rms': v = .9 * v + .1 * g * g; e = eta / (np.sqrt(v) + 1e-8); st = e * g
        else:
            m = .9 * m + .1 * g; v = .999 * v + .001 * g * g
            mh, vh = (m / (1 - .9 ** (k + 1)), v / (1 - .999 ** (k + 1))) if kind == 'adam' else (m, v)
            e = eta / (np.sqrt(vh) + 1e-8); st = e * mh
        S.append(st); E.append(e); w = w - st; P.append(w.copy())
    fs = np.array([f(p) for p in P]); hit = int(np.argmax(fs < 1e-3)) if (fs < 1e-3).any() else None
    return np.array(P), np.array(S), np.array(E), fs, hit
PG, SG, _, FG, HG = run('gd', .19); assert HG == 211 and abs(1 - .19 * .1 - .981) < 1e-12 and abs(1 - .19 * 10 + .9) < 1e-12
ETA = .2
PA, SA, EA, FA, HA = run('ada', ETA); PR, SR, ER, FR, HR = run('rms', ETA); PM, SM, EM, FM, HM = run('adam', ETA); PN, SN, EN, FN, HN = run('adamnb', ETA)
assert np.allclose(SA[0], [-.2, .2]) and np.allclose(SM[0], [-.2, .2]) and np.allclose(np.abs(SN[0]), .2 * .1 / np.sqrt(.001), rtol=1e-6)
assert np.allclose(np.abs(SR[0]), .2 / np.sqrt(.1), rtol=1e-6)
assert HA is None and FA[-1] > .05 and PA[-1][0] < -1 and HR == 53 and FR[-1] > .04 and HM == 91 and FM[-1] < 1e-20
ERM = ER[:150, 0].max(); assert 100 < ERM < 150 and abs(EA[0][0] - .25) < 1e-6 and np.all(np.diff(EA[:, 0]) < 0) and ER[149][0] > 20 and ER[0][0] < 1
assert PN[:, 0].max() > 3.2 and PM[:, 0].max() < .2 and np.allclose(SG[0], [-.152, 2.85])
R316 = .1 / np.sqrt(.001); assert abs(R316 - 3.1623) < 1e-4
for P in (PA[:151], PR[:151], PM[:151], PN[:151], PG):
    assert P[:, 0].min() >= -8 and P[:, 0].max() < 3.5 and np.abs(P[:, 1]).max() <= 1.5

Fx = lambda x, y: 0.5 * (0.1 * x * x + 10 * y * y)
LV = [0.05, 0.3, 1, 2.2, 4, 6.5, 10]

class Ada(Reel):
    def plane(self, xr=(-8.6, 3.6)):
        ax = plain_axes(list(xr), [-1.7, 1.7], 7.8, 4.4, [0, 1.75, 0])
        cs = contours(ax, Fx, LV, (xr[0], xr[1], -1.7, 1.7), N=90)
        return ax, cs

    def construct(self):
        self.title(L("AdaGrad → RMSProp → Adam:\nmỗi tọa độ một bước riêng", "AdaGrad → RMSProp → Adam:\na separate step per coordinate"))
        self.stage(1)
        ax, cs = self.plane(); self.play(Create(cs), run_time=1.0)
        self.add(Dot(ax.c2p(0, 0), radius=0.1, color=MINT))
        self.say(L("Bài toán lệch thang: f(w) = ½(0,1·w₁² + 10·w₂²). Theo w₂, độ cong gấp 100 lần theo w₁. Xuất phát w₀ = (−8; 1,5).",
                   "A badly scaled problem: f(w) = ½(0.1·w₁² + 10·w₂²). The curvature along w₂ is 100 times that along w₁. Start w₀ = (−8, 1.5)."), hold=7.0)
        self.readout(["∇f(w₀) = (−0,8; 15)" if LANG == "vi" else "∇f(w₀) = (−0.8, 15)"], color=SUN, size=24)
        self.say(L("Gradient tại w₀ là (−0,8; 15): tọa độ thứ hai lớn gấp gần 20 lần, dù w₁ còn phải đi xa hơn nhiều.",
                   "The gradient at w₀ is (−0.8, 15): the second coordinate is almost 20 times larger, even though w₁ has much farther to go."), hold=6.5)
        d = Dot(ax.c2p(*W0), radius=0.11, color=SKY); self.add(d)
        self.say(L("GD dùng một η chung. Vì w₂, phải có η < 2/10 = 0,2. Thử η = 0,19.", "GD uses one shared η. Because of w₂ we need η < 2/10 = 0.2. Try η = 0.19."), wait=False)
        def rg(k):
            self.readout(["GD η = %s,  k = %d" % (nf(.19, 2), k), "w = %s" % vec(PG[k], 3), ("f = %s" % nf(FG[k], 4), WHITE)], color=SKY, size=23)
        trail(self, ax, PG, d, SKY, rt=lambda k: 0.45 if k < 5 else 0.06, ks=list(range(1, 6)) + list(range(8, 212, 3)), cb=rg, width=3)
        self.say(L("Theo w₂: nhân −0,9 mỗi bước, nảy qua lại. Theo w₁: nhân 0,981, bò chậm. Cần %d bước để f < 10⁻³." % HG,
                   "Along w₂: times −0.9 per step, bouncing. Along w₁: times 0.981, a slow crawl. It takes %d steps to get f < 10⁻³." % HG), hold=6.5)
        self.say(L("Một η chung không thể vừa với cả hai tọa độ.", "One shared η cannot fit both coordinates."), hold=3.0)
        # ---- stage 2
        self.stage(2); self.wipe()
        t1 = para(L("AdaGrad: chia mỗi tọa độ cho độ lớn gradient của chính nó", "AdaGrad: divide each coordinate by its own gradient size"), 26, SUN).move_to([0, 4.0, 0])
        f1 = Text("G ← G + g⊙g", font=MONO, font_size=28).move_to([0, 3.25, 0])
        f2 = Text("w ← w − η·g ⊘ (√G + ε)", font=MONO, font_size=28).move_to([0, 2.65, 0])
        self.play(FadeIn(t1), FadeIn(f1), FadeIn(f2), run_time=0.6)
        self.say(L("AdaGrad cộng dồn bình phương gradient của từng tọa độ vào G, rồi chia bước theo √G. ⊙ và ⊘ là nhân, chia từng phần tử.",
                   "AdaGrad accumulates each coordinate's squared gradients in G, then divides the step by √G. ⊙ and ⊘ are elementwise multiply and divide."), hold=7.0)
        self.readout([("bước đầu GD (η = 0,19):     %s" % vec(-SG[0], 3) if LANG == "vi" else "first GD step (η = 0.19):   %s" % vec(-SG[0], 3), SKY),
                      ("bước đầu AdaGrad (η = 0,2): %s" % vec(-SA[0], 3) if LANG == "vi" else "first AdaGrad step (η = 0.2): %s" % vec(-SA[0], 3), SUN)], y=1.4, size=22)
        self.say(L("Ở bước đầu, G = g², nên g/√G = ±1: mỗi tọa độ đi đúng η = 0,2, bất kể gradient lớn hay nhỏ. GD thì đi (0,152; −2,85).",
                   "At the first step G = g², so g/√G = ±1: every coordinate moves exactly η = 0.2, whatever its gradient size. GD moves (0.152, −2.85)."), hold=7.5)
        self.say(L("Nhược điểm: G chỉ tăng, không bao giờ quên. Bước hiệu dụng η/√G co lại mãi.",
                   "The catch: G only grows, it never forgets. The effective step η/√G keeps shrinking."), hold=5.0)
        self.clear_ro()
        t2 = para(L("RMSProp: thay tổng bằng trung bình trượt", "RMSProp: replace the sum by a moving average"), 26, PINK).move_to([0, 1.5, 0])
        f3 = Text("v ← 0,9·v + 0,1·g⊙g" if LANG == "vi" else "v ← 0.9·v + 0.1·g⊙g", font=MONO, font_size=26).move_to([0, 0.9, 0])
        self.play(FadeIn(t2), FadeIn(f3), run_time=0.5)
        self.say(L("RMSProp chỉ nhớ các gradient gần đây (γ = 0,9). Thang đo của bước có thể lớn lên lại.",
                   "RMSProp only remembers recent gradients (γ = 0.9). The step scale can grow again."), hold=5.0)
        t3 = para(L("Adam: momentum + RMSProp + hiệu chỉnh chệch", "Adam: momentum + RMSProp + bias correction"), 26, MINT).move_to([0, 0.0, 0])
        f4 = VGroup(Text("m ← 0,9·m + 0,1·g" if LANG == "vi" else "m ← 0.9·m + 0.1·g", font=MONO, font_size=24), Text("v ← 0,999·v + 0,001·g⊙g" if LANG == "vi" else "v ← 0.999·v + 0.001·g⊙g", font=MONO, font_size=24),
                    Text("m̂ = m/(1 − 0,9ᵏ),  v̂ = v/(1 − 0,999ᵏ)" if LANG == "vi" else "m̂ = m/(1 − 0.9ᵏ),  v̂ = v/(1 − 0.999ᵏ)", font=MONO, font_size=24), Text("w ← w − η·m̂ ⊘ (√v̂ + ε)", font=MONO, font_size=24)).arrange(DOWN, buff=0.12).move_to([0, -1.4, 0])
        fit(f4, 7.8); self.play(FadeIn(t3), FadeIn(f4), run_time=0.6)
        self.say(L("Adam giữ thêm trung bình m của gradient (như momentum), và chia cho (1 − βᵏ) để sửa việc m, v bắt đầu từ 0. Mặc định β₁ = 0,9; β₂ = 0,999.",
                   "Adam also keeps an average m of the gradient (like momentum), and divides by (1 − βᵏ) to fix m and v starting at 0. Defaults β₁ = 0.9, β₂ = 0.999."), hold=8.0)
        # ---- stage 3
        self.stage(3); self.wipe()
        ax, cs = self.plane(); self.play(Create(cs), run_time=1.0); self.add(Dot(ax.c2p(0, 0), radius=0.1, color=MINT))
        lg = VGroup(*[Text(s, font=FONT, font_size=21, color=c) for s, c in (("AdaGrad", SUN), ("RMSProp", PINK), ("Adam", MINT))]).arrange(RIGHT, buff=0.6).move_to([0, 4.25, 0]); self.add(lg)
        self.say(L("Ba phương pháp, cùng η = 0,2, cùng điểm đầu. Chạy 150 bước.", "Three methods, same η = 0.2, same start. Run 150 steps."), hold=3.5)
        dots = [Dot(ax.c2p(*W0), radius=0.1, color=c) for c in (SUN, PINK, MINT)]; self.add(*dots)
        segs = []; prev = [0]
        def go(ks, rt):
            for k in ks:
                an = []
                for P, dt, c in zip((PA, PR, PM), dots, (SUN, PINK, MINT)):
                    s = VMobject(color=c, stroke_width=3).set_points_as_corners([ax.c2p(*P[j]) for j in range(prev[0], k + 1)]); segs.append(s); an += [Create(s), dt.animate.move_to(ax.c2p(*P[k]))]
                self.play(*an, run_time=rt, rate_func=linear); prev[0] = k
                self.readout([("k = %d" % k, WHITE), ("AdaGrad  f = %s" % nf(FA[k], 4), SUN), ("RMSProp  f = %s" % nf(FR[k], 4), PINK), ("Adam     f = %s" % nf(FM[k], 4), MINT)], size=23)
        go(range(1, 13), 0.4)
        self.say(L("Ngay từ đầu, cả ba đi chéo về phía tâm: w₁ tiến nhanh như w₂, không nảy qua lại như GD. Đường của Adam lượn sóng vì có momentum.",
                   "From the start all three head diagonally toward the center: w₁ moves as fast as w₂, no bouncing like GD. Adam's path waves because of its momentum."), wait=False)
        go(range(15, 151, 3), 0.12); self.wait(2.5)
        self.readout([("sau 150 bước, w₁ của AdaGrad = %s" % nf(PA[150][0], 2) if LANG == "vi" else "after 150 steps, AdaGrad's w₁ = %s" % nf(PA[150][0], 2), SUN), ("bước hiệu dụng η/√G cho w₁: %s → %s" % (nf(EA[0][0], 2), nf(EA[149][0], 3)) if LANG == "vi" else "effective step η/√G for w₁: %s → %s" % (nf(EA[0][0], 2), nf(EA[149][0], 3)), SUN)], size=22)
        self.say(L("AdaGrad chậm dần rồi gần như dừng: sau 150 bước w₁ vẫn ở %s, vì bước hiệu dụng của w₁ co từ %s xuống %s." % (nf(PA[150][0], 2), nf(EA[0][0], 2), nf(EA[149][0], 3)),
                   "AdaGrad slows down and nearly stops: after 150 steps w₁ is still at %s, because w₁'s effective step shrank from %s to %s." % (nf(PA[150][0], 2), nf(EA[0][0], 2), nf(EA[149][0], 3))), hold=7.5)
        self.readout([("f < 10⁻³ lần đầu ở bước:" if LANG == "vi" else "first step with f < 10⁻³:", WHITE), ("RMSProp  %d    f sau 600 bước = %s" % (HR, nf(FR[-1], 3)) if LANG == "vi" else "RMSProp  %d    f after 600 steps = %s" % (HR, nf(FR[-1], 3)), PINK), ("Adam     %d    f sau 600 bước < 10⁻²⁰" % HM if LANG == "vi" else "Adam     %d    f after 600 steps < 10⁻²⁰" % HM, MINT), ("AdaGrad  chưa tới sau 600 bước" if LANG == "vi" else "AdaGrad  not reached in 600 steps", SUN)], size=21)
        self.say(L("RMSProp tới f < 10⁻³ nhanh nhất (bước %d), nhưng rồi rung quanh tâm, f quay lên khoảng %s. Adam tới ở bước %d và tiếp tục hội tụ." % (HR, nf(FR[-1], 2), HM),
                   "RMSProp is first to f < 10⁻³ (step %d), but then jitters around the center and f climbs back to about %s. Adam gets there at step %d and keeps converging." % (HR, nf(FR[-1], 2), HM)), hold=8.0)
        # ---- stage 4
        self.stage(4); self.wipe()
        ex = plain_axes([0, 150], [-2, 2.2], 7.0, 3.6, [0.3, 2.2, 0])
        yl = VGroup(*[Text(s, font=MONO, font_size=18, color=DIM).next_to(ex.c2p(0, v), LEFT, buff=0.1) for v, s in ((2, "100"), (1, "10"), (0, "1"), (-1, "10⁻¹"), (-2, "10⁻²"))])
        tl = para(L("bước hiệu dụng của w₁ theo k", "effective step for w₁ versus k"), 22, DIM).move_to([0, 4.3, 0])
        self.play(Create(ex), FadeIn(yl), FadeIn(tl), run_time=0.5)
        ca = VMobject(color=SUN, stroke_width=3).set_points_as_corners([ex.c2p(k, np.log10(EA[k][0])) for k in range(150)])
        cr = VMobject(color=PINK, stroke_width=3).set_points_as_corners([ex.c2p(k, np.log10(ER[k][0])) for k in range(150)])
        self.play(Create(ca), run_time=1.5); self.play(Create(cr), run_time=1.5)
        self.say(L("AdaGrad (vàng): η/√G chỉ giảm. RMSProp (hồng): η/√v lớn lên lại khi gradient nhỏ dần, có lúc tới khoảng %d. Đó là lý do nó đi nhanh, và cũng là lý do nó rung." % round(ERM),
                   "AdaGrad (yellow): η/√G only goes down. RMSProp (pink): η/√v grows again as the gradient shrinks, at times up to about %d. That is why it is fast, and also why it jitters." % round(ERM)), hold=8.5)
        self.play(FadeOut(VGroup(ex, yl, tl, ca, cr)), run_time=0.4); self.clear_ro()
        self.readout([("bước 1: m = 0,1·g,  v = 0,001·g²" if LANG == "vi" else "step 1: m = 0.1·g,  v = 0.001·g²", WHITE), ("không hiệu chỉnh: m/√v = %s·dấu(g)" % nf(R316, 2) if LANG == "vi" else "no correction: m/√v = %s·sign(g)" % nf(R316, 2), PINK), ("có hiệu chỉnh:  m̂/√v̂ = dấu(g)" if LANG == "vi" else "with correction: m̂/√v̂ = sign(g)", MINT)], y=3.5, size=23)
        self.say(L("Hiệu chỉnh chệch để làm gì? Ở bước 1, m và v bắt đầu từ 0 nên bị kéo nhỏ: m = 0,1·g, v = 0,001·g².",
                   "Why bias correction? At step 1, m and v start from 0 and are pulled small: m = 0.1·g, v = 0.001·g²."), hold=6.0)
        self.say(L("Tỉ số m/√v khi đó là 0,1/√0,001 ≈ 3,16: bước đầu dài gấp 3 lần η. Chia cho (1 − 0,9) và (1 − 0,999) đưa nó về đúng η.",
                   "The ratio m/√v is then 0.1/√0.001 ≈ 3.16: the first step is 3 times η. Dividing by (1 − 0.9) and (1 − 0.999) brings it back to η."), hold=7.0)
        ax, cs = self.plane(); ax.shift(DOWN * 1.2); cs.shift(DOWN * 1.2); self.play(Create(cs), run_time=0.8)
        self.add(Dot(ax.c2p(0, 0), radius=0.1, color=MINT))
        d1, d2 = Dot(ax.c2p(*W0), radius=0.1, color=MINT), Dot(ax.c2p(*W0), radius=0.1, color=PINK); self.add(d1, d2)
        k2 = list(range(1, 11)) + list(range(13, 151, 3)); pv = 0
        for k in k2:
            self.play(Create(VMobject(color=MINT, stroke_width=3).set_points_as_corners([ax.c2p(*PM[j]) for j in range(pv, k + 1)])), Create(VMobject(color=PINK, stroke_width=3).set_points_as_corners([ax.c2p(*PN[j]) for j in range(pv, k + 1)])),
                      d1.animate.move_to(ax.c2p(*PM[k])), d2.animate.move_to(ax.c2p(*PN[k])), run_time=0.3 if k <= 10 else 0.08, rate_func=linear); pv = k
        self.readout([("vượt quá w₁ = 0 nhiều nhất:" if LANG == "vi" else "largest overshoot past w₁ = 0:", WHITE), ("Adam có hiệu chỉnh    w₁ = %s" % nf(PM[:, 0].max(), 2) if LANG == "vi" else "Adam, corrected     w₁ = %s" % nf(PM[:, 0].max(), 2), MINT), ("Adam không hiệu chỉnh w₁ = %s" % nf(PN[:, 0].max(), 2) if LANG == "vi" else "Adam, uncorrected   w₁ = %s" % nf(PN[:, 0].max(), 2), PINK)], y=3.5, size=23)
        self.say(L("Không hiệu chỉnh (hồng), những bước đầu quá dài, đà tích quá mạnh: w₁ vượt tâm tới %s. Có hiệu chỉnh (xanh lá) chỉ vượt %s." % (nf(PN[:, 0].max(), 2), nf(PM[:, 0].max(), 2)),
                   "Without correction (pink) the early steps are too long and build too much momentum: w₁ overshoots to %s. With correction (green) only to %s." % (nf(PN[:, 0].max(), 2), nf(PM[:, 0].max(), 2))), hold=7.5)
        self.takeaway([L("Bài lệch thang: một η chung buộc GD bò theo tọa độ phẳng (%d bước)." % HG, "Badly scaled problem: one shared η makes GD crawl along the flat coordinate (%d steps)." % HG),
                       L("AdaGrad chia mỗi tọa độ cho √(tổng g²): bước đầu đều η, nhưng bước co mãi.", "AdaGrad divides each coordinate by √(sum of g²): equal first steps, but steps shrink forever."),
                       L("RMSProp dùng trung bình trượt: bước lớn lên lại được, nhưng có thể rung.", "RMSProp uses a moving average: steps can grow again, but it may jitter."),
                       L("Adam = momentum + RMSProp + hiệu chỉnh chệch. Đây là tiền điều kiện đường chéo, không phải phương pháp bậc hai.", "Adam = momentum + RMSProp + bias correction. It is a diagonal preconditioner, not a second-order method.")])
