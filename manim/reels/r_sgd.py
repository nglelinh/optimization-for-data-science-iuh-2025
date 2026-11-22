from rl import *
# m = 3 (bài 06-05): f(x) = Σ fᵢ(x), fᵢ(x) = ½(w·tᵢ + c − yᵢ)², x = (w, c), x⁰ = (1, 2)
T3 = np.array([0., 1, 2]); Y3 = np.array([1., 3, 2]); A3 = np.c_[T3, np.ones(3)]
XS = np.linalg.solve(A3.T @ A3, A3.T @ Y3); f3 = lambda x: 0.5 * np.sum((A3 @ x - Y3) ** 2); FS = f3(XS)
g3 = lambda x, i: (A3[i] @ x - Y3[i]) * A3[i]
X0 = np.array([1., 2.]); TS = 0.15
assert np.allclose(XS, [.5, 1.5]) and abs(FS - .75) < 1e-12
G0 = [g3(X0, i) for i in range(3)]; assert np.allclose(G0, [[0, 1], [0, 0], [4, 2]])
XG1 = X0 - TS * sum(G0); assert np.allclose(XG1, [.4, 1.55])
EP = [X0.copy()]
for i in range(3): EP.append(EP[-1] - TS * g3(EP[-1], i))
assert np.allclose(EP[3], [.44725, 1.584875]) and f3(EP[3]) < f3(XG1)
GS = [g3(XS, i) for i in range(3)]; assert np.allclose(GS, [[0, .5], [-1, -1], [1, .5]]) and np.allclose(sum(GS), 0)
def sgd3(sched, n, seed=5):
    r = np.random.default_rng(seed); x = X0.copy(); P = [x.copy()]
    for k in range(n): x = x - sched(k) * g3(x, r.integers(3)); P.append(x.copy())
    return np.array(P)
PC = sgd3(lambda k: TS, 300); PD = sgd3(lambda k: TS * 20 / (20 + k), 300)
PG = [X0.copy()]
for k in range(100): PG.append(PG[-1] - TS * sum(g3(PG[-1], i) for i in range(3)))
PG = np.array(PG)
fc = np.array([f3(p) - FS for p in PC]); fd = np.array([f3(p) - FS for p in PD])
MC, MD = fc[150:].mean(), fd[150:].mean(); assert MC > 10 * MD and MC > .1 and MD < .01
assert f3(PG[100]) - FS < 1e-12 and f3(PG[10]) - FS < fc[30]
assert PC[:, 0].min() > -.2 and PC[:, 0].max() < 1.6 and PC[:, 1].min() > .9 and PC[:, 1].max() < 2.3
# minibatch: n = 48 điểm tổng hợp (seed cố định), F = trung bình
rng = np.random.default_rng(7); NN = 48
TT = np.sort(rng.uniform(0, 4, NN)); YY = 1 + 0.5 * TT + rng.normal(0, 0.5, NN); AA = np.c_[TT, np.ones(NN)]
xs = np.linalg.solve(AA.T @ AA, AA.T @ YY); F = lambda x: 0.5 * np.mean((AA @ x - YY) ** 2); Fs = F(xs)
G = lambda x, idx: AA[idx].T @ (AA[idx] @ x - YY[idx]) / len(idx)
def mb(B, sched, budget=960, seed=1):
    r = np.random.default_rng(seed); x = np.array([0., 3.]); ev = 0; out = [(0, F(x) - Fs)]; k = 0
    while ev < budget:
        idx = r.integers(0, NN, B) if B < NN else np.arange(NN); x = x - sched(k) * G(x, idx); ev += B; k += 1; out.append((ev, F(x) - Fs))
    return np.array(out)
M1, M8, M48 = mb(1, lambda k: .1), mb(8, lambda k: .1), mb(48, lambda k: .1); M1d = mb(1, lambda k: .1 * 100 / (100 + k))
def ep(M):  # trung bình F − F* trong từng epoch (48 lần tính gradient)
    out = [(0, M[0, 1])]
    for e in range(1, 21):
        sel = (M[:, 0] > (e - 1) * 48) & (M[:, 0] <= e * 48); out.append((e * 48, M[sel, 1].mean()))
    return np.array(out)
E1, E8, E48, E1d = ep(M1), ep(M8), ep(M48), ep(M1d)
e1, e8, e48, e1d = E1[-1, 1], E8[-1, 1], E48[-1, 1], E1d[-1, 1]
assert e48 > e1 > e8 > e1d and e1d < e1 / 10 and E1[5, 1] < E8[5, 1] < E48[5, 1] and abs(E1[5, 1] - E1[20, 1]) < 0.01
assert len(M48) == 21 and len(M8) == 121 and len(M1) == 961
gi = np.array([G(xs, [i]) for i in range(NN)]); V1 = np.mean(np.sum(gi ** 2, 1)); assert np.allclose(gi.mean(0), 0, atol=1e-12)
r0 = np.random.default_rng(0); V8 = np.mean([np.sum(G(xs, r0.integers(0, NN, 8)) ** 2) for _ in range(20000)])
assert abs(V8 / (V1 / 8) - 1) < 0.05

class Sgd(Reel):
    def construct(self):
        self.title(L("SGD và minibatch:\nđi bằng gradient nhiễu", "SGD and minibatches:\nwalking on noisy gradients"))
        self.stage(1)
        dx = mkaxes([-0.3, 2.5], [0, 3.6], 6.4, 4.4, [0.3, 1.9, 0], xt=(0, 1, 2), yt=[(1, "1"), (2, "2"), (3, "3")])
        ax, lab = dx; self.play(Create(ax), FadeIn(lab), run_time=0.6)
        pts = VGroup(*[Dot(ax.c2p(t, y), radius=0.12, color=SUN) for t, y in zip(T3, Y3)])
        pl = VGroup(*[Text("(%d; %d)" % (t, y) if LANG == "vi" else "(%d, %d)" % (t, y), font=MONO, font_size=20, color=SUN).next_to(ax.c2p(t, y), UR, buff=0.08) for t, y in zip(T3, Y3)])
        self.play(FadeIn(pts), FadeIn(pl), run_time=0.5)
        self.say(L("Ví dụ m = 3 của bài 06-05, làm cụ thể: khớp đường thẳng y = w·t + c qua ba điểm dữ liệu.",
                   "The m = 3 example from lesson 06-05, made concrete: fit a line y = w·t + c through three data points."), hold=5.5)
        self.readout(["f(x) = f₁ + f₂ + f₃,  x = (w; c)" if LANG == "vi" else "f(x) = f₁ + f₂ + f₃,  x = (w, c)", "f₁ = ½(c − 1)²   f₂ = ½(w + c − 3)²", "f₃ = ½(2w + c − 2)²"], color=WHITE, size=22)
        self.say(L("Mỗi điểm cho một hàm mất mát fᵢ: bình phương sai số tại điểm đó. Mục tiêu là tổng f = f₁ + f₂ + f₃.",
                   "Each point gives a loss fᵢ: the squared error at that point. The objective is the sum f = f₁ + f₂ + f₃."), hold=6.0)
        l0 = Line(ax.c2p(-0.3, 1.7), ax.c2p(1.6, 3.6), color=SKY, stroke_width=4)
        self.play(Create(l0), run_time=0.6)
        self.say(L("Điểm xuất phát như trong bài: x⁰ = (1; 2), tức đường y = t + 2 (xanh). Nó đi qua đúng điểm thứ hai.",
                   "The starting point from the lesson: x⁰ = (1, 2), i.e. the line y = t + 2 (blue). It passes exactly through the second point."), hold=6.0)
        ls = Line(ax.c2p(-0.3, 1.5 - 0.15), ax.c2p(2.5, 1.5 + 1.25), color=MINT, stroke_width=4)
        self.play(Create(ls), run_time=0.6)
        self.readout(["x* = (0,5; 1,5),  f* = 0,75" if LANG == "vi" else "x* = (0.5, 1.5),  f* = 0.75"], color=MINT, size=24)
        self.say(L("Đường tốt nhất (xanh lá): x* = (0,5; 1,5), f* = 0,75. Ba điểm không thẳng hàng nên f* > 0.",
                   "The best line (green): x* = (0.5, 1.5), f* = 0.75. The three points are not collinear, so f* > 0."), hold=5.5)
        # parameter plane
        self.wipe()
        px = plain_axes([-0.2, 1.6], [0.9, 2.3], 7.6, 5.9, [0, 1.25, 0])
        cs = contours(px, lambda w, c: f3(np.array([w, c])), [FS + d for d in (0.02, 0.08, 0.2, 0.4, 0.7, 1.1)], (-0.2, 1.6, 0.9, 2.3), N=70)
        lines = VGroup(Line(px.c2p(-0.2, 1), px.c2p(1.6, 1), color=PINK, stroke_width=3),
                       Line(px.c2p(0.7, 2.3), px.c2p(1.6, 1.4), color=ORANGE, stroke_width=3),
                       Line(px.c2p(-0.15, 2.3), px.c2p(0.55, 0.9), color=SKY, stroke_width=3))
        ll = VGroup(Text("f₁ = 0", font=MONO, font_size=20, color=PINK).next_to(px.c2p(1.4, 1), UP, buff=0.08),
                    Text("f₂ = 0", font=MONO, font_size=20, color=ORANGE).next_to(px.c2p(1.45, 1.55), RIGHT, buff=0.05).shift(LEFT * 0.9 + UP * 0.1),
                    Text("f₃ = 0", font=MONO, font_size=20, color=SKY).next_to(px.c2p(0.0, 2.0), RIGHT, buff=0.1))
        axl = VGroup(Text("w", font=FONT, font_size=22, color=DIM).next_to(px.c2p(1.6, 0.9), UP, buff=0.08), Text("c", font=FONT, font_size=22, color=DIM).next_to(px.c2p(-0.2, 2.3), RIGHT, buff=0.08))
        self.play(Create(cs), FadeIn(axl), run_time=1.0)
        self.play(Create(lines), FadeIn(ll), run_time=0.8)
        self.add(Dot(px.c2p(*XS), radius=0.1, color=MINT))
        d0 = Dot(px.c2p(*X0), radius=0.11, color=WHITE); self.add(d0)
        self.say(L("Giờ nhìn trong mặt phẳng tham số (w; c). Mỗi đường màu là nơi một fᵢ = 0. Cực tiểu x* nằm giữa ba đường.",
                   "Now look in the parameter plane (w, c). Each colored line is where one fᵢ = 0. The minimizer x* sits between the three lines."), hold=6.5)
        # ---- stage 2
        self.stage(2)
        self.readout(["∇f₁(x⁰) = (0; 1)   ∇f₂(x⁰) = (0; 0)" if LANG == "vi" else "∇f₁(x⁰) = (0, 1)   ∇f₂(x⁰) = (0, 0)", "∇f₃(x⁰) = (4; 2)   tổng = (4; 3)" if LANG == "vi" else "∇f₃(x⁰) = (4, 2)   sum = (4, 3)"], color=WHITE, size=23)
        self.say(L("Tại x⁰, ba gradient riêng rất khác nhau. ∇f₂ = 0 vì đường xanh đi qua điểm thứ hai.",
                   "At x⁰ the three per-sample gradients are very different. ∇f₂ = 0 because the blue line passes through the second point."), hold=5.5)
        gd_ar = Arrow(px.c2p(*X0), px.c2p(*XG1), buff=0, color=SKY, stroke_width=5, max_tip_length_to_length_ratio=0.12)
        self.play(GrowArrow(gd_ar), run_time=0.6)
        self.readout([("GD, t = 0,15:  x¹ = x⁰ − t·(4; 3) = (0,4; 1,55)" if LANG == "vi" else "GD, t = 0.15:  x¹ = x⁰ − t·(4, 3) = (0.4, 1.55)", SKY), ("f(x¹) − f* = %s" % nf(f3(XG1) - FS, 4), SKY)], size=22)
        self.say(L("Batch GD: cộng cả ba gradient tại cùng điểm x⁰, rồi đi một bước. Tốn 3 lần tính gradient.",
                   "Batch GD: add all three gradients at the same point x⁰, then take one step. That costs 3 gradient evaluations."), hold=5.5)
        sg = VGroup(*[Arrow(px.c2p(*EP[j]), px.c2p(*EP[j + 1]), buff=0, color=SUN, stroke_width=5, max_tip_length_to_length_ratio=0.25) for j in range(3)])
        for j in range(3):
            self.play(GrowArrow(sg[j]), run_time=0.6)
            self.readout([("SGD vòng tròn, bước %d: dùng f%s" % (j + 1, "₁₂₃"[j]) if LANG == "vi" else "cyclic SGD, step %d: use f%s" % (j + 1, "₁₂₃"[j]), SUN), ("x = %s" % vec(EP[j + 1], 4), SUN)], size=22)
            self.wait(1.2)
        self.readout([("SGD 1 epoch:  x³ = %s" % vec(EP[3], 3), SUN), ("f(x³) − f* = %s" % nf(f3(EP[3]) - FS, 4), SUN), ("GD 1 bước:    f(x¹) − f* = %s" % nf(f3(XG1) - FS, 4) if LANG == "vi" else "GD 1 step:    f(x¹) − f* = %s" % nf(f3(XG1) - FS, 4), SKY)], size=22)
        self.say(L("SGD vòng tròn: dùng f₁, rồi f₂, rồi f₃, mỗi lần tại điểm mới nhất. Cùng 3 lần tính gradient, nhưng đi 3 bước.",
                   "Cyclic SGD: use f₁, then f₂, then f₃, each at the newest point. The same 3 gradient evaluations, but 3 steps."), hold=6.5)
        self.say(L("Khác biệt then chốt: GD tính mọi gradient tại cùng x⁰, SGD tính mỗi gradient tại một điểm khác nhau trên đường đi.",
                   "The key difference: GD evaluates every gradient at the same x⁰, SGD evaluates each one at a different point along the path."), hold=6.5)
        self.say(L("Nếu chọn i ngẫu nhiên đều, trung bình của ∇fᵢ là ⅓·∇f: đúng hướng gradient đầy đủ, chỉ có nhiễu quanh nó.",
                   "If i is picked uniformly at random, the average of ∇fᵢ is ⅓·∇f: the full-gradient direction on average, plus noise around it."), hold=6.5)
        # ---- stage 3
        self.stage(3); self.play(FadeOut(VGroup(gd_ar, sg)), run_time=0.3)
        ds, dg = Dot(px.c2p(*X0), radius=0.1, color=SUN), Dot(px.c2p(*X0), radius=0.1, color=SKY); self.add(dg, ds)
        self.say(L("Chạy 300 lần tính gradient. SGD chọn i ngẫu nhiên, bước hằng t = 0,15 (vàng). GD dùng cùng t, mỗi bước tốn 3 lần (xanh).",
                   "Run 300 gradient evaluations. SGD picks i at random, constant step t = 0.15 (yellow). GD uses the same t, 3 evaluations per step (blue)."), wait=False)
        segs = []
        def go(ks, rt, wd=2.5):
            prev = go.prev
            for k in ks:
                an = []
                s = VMobject(color=SUN, stroke_width=wd).set_points_as_corners([px.c2p(*PC[j]) for j in range(prev, k + 1)]); segs.append(s); an += [Create(s), ds.animate.move_to(px.c2p(*PC[k]))]
                a, b = prev // 3, k // 3
                if b > a:
                    s2 = VMobject(color=SKY, stroke_width=3).set_points_as_corners([px.c2p(*PG[j]) for j in range(a, b + 1)]); segs.append(s2); an += [Create(s2), dg.animate.move_to(px.c2p(*PG[b]))]
                self.play(*an, run_time=rt, rate_func=linear); prev = k
                self.readout([("lần tính gradient: %d" % k if LANG == "vi" else "gradient evaluations: %d" % k, WHITE), ("SGD  f − f* = %s" % nf(fc[k], 4), SUN), ("GD   f − f* = %s" % nf(f3(PG[k // 3]) - FS, 4), SKY)], size=23)
            go.prev = prev
        go.prev = 0
        go(range(1, 31), 0.32)
        self.say(L("GD đi thẳng về x*. SGD nhảy lung tung: mỗi bước chỉ nghe theo một điểm dữ liệu.",
                   "GD heads straight to x*. SGD jumps around: each step listens to a single data point."), wait=False)
        go(range(36, 301, 6), 0.12, wd=1.3)
        self.readout([("SGD, bước hằng: trung bình f − f* = %s" % nf(MC, 3) if LANG == "vi" else "SGD, constant step: mean f − f* = %s" % nf(MC, 3), SUN), ("(lần tính 150 → 300)" if LANG == "vi" else "(evaluations 150 → 300)", DIM), ("GD: f − f* < 10⁻¹²", SKY)], size=22)
        self.say(L("Sau 300 lần, GD đã tới x*. SGD bước hằng không dừng lại: nó cứ lượn quanh x*, f − f* trung bình %s." % nf(MC, 3),
                   "After 300 evaluations GD has reached x*. Constant-step SGD never settles: it keeps circling x*, with mean f − f* = %s." % nf(MC, 3)), hold=6.5)
        ga = VGroup(*[Arrow(px.c2p(*XS), px.c2p(*(XS - 0.25 * GS[i])), buff=0, color=c, stroke_width=5, max_tip_length_to_length_ratio=0.3) for i, c in ((0, PINK), (1, ORANGE), (2, SKY))])
        self.play(*[GrowArrow(a) for a in ga], run_time=0.6)
        self.readout(["∇f₁(x*) = (0; 0,5)  ∇f₂(x*) = (−1; −1)" if LANG == "vi" else "∇f₁(x*) = (0, 0.5)  ∇f₂(x*) = (−1, −1)", "∇f₃(x*) = (1; 0,5)   tổng = (0; 0)" if LANG == "vi" else "∇f₃(x*) = (1, 0.5)   sum = (0, 0)"], color=WHITE, size=22)
        self.say(L("Lý do: tại x*, tổng gradient bằng 0 nhưng từng ∇fᵢ thì không. Mỗi bước SGD vẫn đẩy điểm ra khỏi x*.",
                   "The reason: at x* the gradients sum to 0, but each ∇fᵢ does not. Every SGD step still pushes the point away from x*."), hold=6.5)
        self.play(FadeOut(VGroup(*segs)), FadeOut(ga), FadeOut(ds), FadeOut(dg), run_time=0.4)
        dd = Dot(px.c2p(*X0), radius=0.1, color=MINT); self.add(dd)
        self.say(L("Cách sửa: giảm bước dần, tₖ = 0,15·20/(20 + k). Cùng chuỗi chọn ngẫu nhiên kiểu này.",
                   "The fix: shrink the step, tₖ = 0.15·20/(20 + k). Same kind of random picks."), wait=False)
        trail(self, px, PD, dd, MINT, rt=0.12, width=1.8, ks=list(range(1, 31)) + list(range(36, 301, 6)), rate=linear)
        self.readout([("bước hằng:    trung bình f − f* = %s" % nf(MC, 3) if LANG == "vi" else "constant step:  mean f − f* = %s" % nf(MC, 3), SUN), ("bước giảm dần: trung bình f − f* = %s" % nf(MD, 4) if LANG == "vi" else "decaying step:  mean f − f* = %s" % nf(MD, 4), MINT)], size=22)
        self.say(L("Bước giảm dần làm nhiễu nhỏ lại theo thời gian: điểm co về x*. Trung bình f − f* từ %s xuống %s." % (nf(MC, 3), nf(MD, 4)),
                   "A decaying step shrinks the noise over time: the point closes in on x*. Mean f − f* drops from %s to %s." % (nf(MC, 3), nf(MD, 4))), hold=6.5)
        # ---- stage 4
        self.stage(4); self.wipe()
        lx = plain_axes([0, 960], [-3.2, 0.3], 7.2, 4.6, [0.3, 1.75, 0])
        yl = VGroup(*[Text(s, font=MONO, font_size=18, color=DIM).next_to(lx.c2p(0, v), LEFT, buff=0.1) for v, s in ((0, "1"), (-1, "10⁻¹"), (-2, "10⁻²"), (-3, "10⁻³"))])
        xl = Text("960", font=MONO, font_size=18, color=DIM).next_to(lx.c2p(960, -3.2), DOWN, buff=0.08)
        tl = para(L("F − F*, trung bình mỗi epoch", "F − F*, averaged per epoch"), 22, DIM).move_to([0, 4.3, 0])
        self.play(Create(lx), FadeIn(yl), FadeIn(xl), FadeIn(tl), run_time=0.6)
        self.say(L("Bài lớn hơn: 48 điểm dữ liệu, F là trung bình mất mát. Ngân sách như nhau: 960 lần tính gradient (20 epoch).",
                   "A bigger problem: 48 data points, F is the average loss. Same budget for everyone: 960 gradient evaluations (20 epochs)."), hold=6.5)
        def curve(M, c):
            return VMobject(color=c, stroke_width=2.5).set_points_as_corners([lx.c2p(e, np.log10(v)) for e, v in M])
        for M, c, d in ((E48, SKY, L("Mỗi điểm trên đồ thị là trung bình F − F* trong một epoch. B = 48 (GD đầy đủ): chỉ 20 bước, mượt nhưng chậm, cuối cùng còn %s." % nf(e48, 3), "Each point is F − F* averaged over one epoch. B = 48 (full GD): only 20 steps, smooth but slow, ending at %s." % nf(e48, 3))),
                        (E1, SUN, L("B = 1 (SGD): 960 bước. Xuống rất nhanh lúc đầu, rồi kẹt ở mức nhiễu, F − F* ≈ %s." % nf(e1, 3), "B = 1 (SGD): 960 steps. Drops very fast at first, then stalls at a noise level, F − F* ≈ %s." % nf(e1, 3))),
                        (E8, PINK, L("B = 8 (minibatch): 120 bước, ít nhiễu hơn. Cuối cùng F − F* = %s." % nf(e8, 4), "B = 8 (minibatch): 120 steps, less noise. It ends at F − F* = %s." % nf(e8, 4)))):
            cv = curve(M, c); self.play(Create(cv), run_time=2.0, rate_func=linear); self.say(d, hold=6.0)
        self.readout([("B = 1:  phương sai gradient = %s" % nf(V1, 3) if LANG == "vi" else "B = 1:  gradient variance = %s" % nf(V1, 3), SUN), ("B = 8:  phương sai gradient ≈ %s" % nf(V8, 3) if LANG == "vi" else "B = 8:  gradient variance ≈ %s" % nf(V8, 3), PINK)], size=22)
        self.say(L("Tại sao? Trung bình B gradient làm phương sai giảm theo 1/B: từ %s xuống khoảng %s (≈ chia 8). Đổi lại, mỗi bước tốn B lần tính." % (nf(V1, 3), nf(V8, 3)),
                   "Why? Averaging B gradients cuts the variance by 1/B: from %s to about %s (≈ divided by 8). In exchange, each step costs B evaluations." % (nf(V1, 3), nf(V8, 3))), hold=7.5)
        cv = curve(E1d, MINT); self.play(Create(cv), run_time=2.0, rate_func=linear)
        self.say(L("Và B = 1 với bước giảm dần tₖ = 0,1·100/(100 + k) (xanh lá): vượt qua mức nhiễu, F − F* = %s." % nf(e1d, 4),
                   "And B = 1 with a decaying step tₖ = 0.1·100/(100 + k) (green): it breaks through the noise level, F − F* = %s." % nf(e1d, 4)), hold=6.5)
        self.takeaway([L("SGD dùng gradient của một mẫu: rẻ, trung bình đúng hướng, nhưng nhiễu.", "SGD uses one sample's gradient: cheap, right on average, but noisy."),
                       L("Bước hằng: SGD lượn mãi quanh x*, vì tại x* từng ∇fᵢ vẫn khác 0.", "Constant step: SGD keeps circling x*, because each ∇fᵢ is nonzero at x*."),
                       L("Bước giảm dần dập nhiễu theo thời gian và đưa SGD về gần x*.", "A decaying step damps the noise over time and brings SGD close to x*."),
                       L("Minibatch B: phương sai giảm 1/B, mỗi bước tốn B lần. Chọn B ở giữa thường lợi nhất.", "Minibatch B: variance drops by 1/B, each step costs B. A middle B often pays off best.")])
