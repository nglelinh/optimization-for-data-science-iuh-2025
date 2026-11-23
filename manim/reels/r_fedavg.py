from rl import *
# Bài 29-02: FedAvg: K máy khách, E bước cục bộ, máy chủ lấy trung bình có trọng số; dữ liệu không IID gây trôi (client drift)
AC = [np.diag([4., .5]), np.diag([.5, 4.]), np.array([[2., 1.2], [1.2, 2.]])]      # Fc(w) = ½(w − bc)ᵀAc(w − bc)
BC = [np.array([2., 0]), np.array([0., 2]), np.array([-1.5, -1])]
NC = np.array([50, 30, 20]); PC = NC / NC.sum()
AG = sum(p * a for p, a in zip(PC, AC)); WS = np.linalg.solve(AG, sum(p * a @ b for p, a, b in zip(PC, AC, BC)))
FG = lambda w: sum(p * 0.5 * (w - b) @ a @ (w - b) for p, a, b in zip(PC, AC, BC)); FS = FG(WS)
assert np.allclose(WS, [1.1701, 0.7347], atol=1e-4) and np.allclose(PC, [.5, .3, .2])
W0 = np.array([2.5, 2.5]); ETA = 0.1
def fed(E, R=40, dec=False):
    w = W0.copy(); H = [w.copy()]; PATHS = []
    for r in range(R):
        e = ETA / (1 + r / 5) if dec else ETA; cl = []; pr = []
        for a, b in zip(AC, BC):
            v = w.copy(); pth = [v.copy()]
            for _ in range(E): v = v - e * a @ (v - b); pth.append(v.copy())
            cl.append(v); pr.append(np.array(pth))
        w = sum(p * v for p, v in zip(PC, cl)); H.append(w.copy()); PATHS.append(pr)
    return np.array(H), PATHS
# E = 1 đúng bằng GD trên hàm toàn cục
H1, _ = fed(1, 60); g = W0.copy()
for k in range(60): g = g - ETA * AG @ (g - WS)
assert np.allclose(H1[-1], g, atol=1e-12) and np.linalg.norm(H1[-1] - WS) < 1e-3
RUN = {E: fed(E, 40) for E in (1, 5, 20)}
GAP = {E: np.array([FG(h) - FS for h in RUN[E][0]]) for E in RUN}
first = lambda v, t: next(i for i, x in enumerate(v) if x < t)
RT = {E: first(GAP[E], 0.3) for E in RUN}; assert RT == {1: 6, 5: 2, 20: 1}, RT
PLAT = {E: GAP[E][-1] for E in RUN}; assert PLAT[1] < 1e-6 and abs(PLAT[5] - 0.0515) < 1e-3 and abs(PLAT[20] - 0.2617) < 1e-3
DIST = {E: np.linalg.norm(RUN[E][0][-1] - WS) for E in RUN}; assert abs(DIST[5] - 0.204) < 1e-3 and abs(DIST[20] - 0.454) < 1e-3
HD, _ = fed(5, 2000, dec=True); DD = np.linalg.norm(HD[[100, 1999]] - WS, axis=1); assert DD[0] < 0.012 and DD[1] < 0.001
# dữ liệu IID: mọi máy cùng hàm toàn cục ⇒ E bước cục bộ = E bước GD, không trôi
v = W0.copy()
for _ in range(5): v = v - ETA * AG @ (v - WS)
assert np.linalg.norm(v - WS) < np.linalg.norm(W0 - WS)
# E rất lớn: mỗi máy chạy tới đáy riêng, FedAvg → Σ p_c b_c thay vì w*
BAVG = sum(p * b for p, b in zip(PC, BC)); assert np.allclose(BAVG, [0.7, 0.4]); assert np.linalg.norm(fed(200, 60)[0][-1] - BAVG) < 1e-3
COL = (SKY, MINT, PINK)

class FedAvg(Reel):
    def plane(self):
        ax = plain_axes([-2, 3], [-1.5, 3], 7.0, 6.3, [0, 1.0, 0])
        cs = contours(ax, lambda x, y: FG(np.array([x, y])), [FS + t for t in (0.1, 0.5, 1.2, 2.2, 3.5, 5.5)], (-2, 3, -1.5, 3), N=70)
        st = VGroup(*[Star(5, outer_radius=0.16, color=c, fill_opacity=1).move_to(ax.c2p(*b)) for b, c in zip(BC, COL)])
        ws = Dot(ax.c2p(*WS), radius=0.11, color=WHITE); lw = Text("w*", font=MONO, font_size=22, color=WHITE).next_to(ws, DR, buff=0.05)
        return ax, cs, st, ws, lw

    def construct(self):
        self.title(L("FedAvg: học liên kết\nvà hiện tượng trôi", "FedAvg: federated learning\nand client drift"))
        # ---- stage 1
        self.stage(1)
        ax, cs, st, ws, lw = self.plane()
        self.play(Create(ax), Create(cs), FadeIn(st), FadeIn(ws), FadeIn(lw), run_time=1.2)
        self.readout([("min F(w) = Σ (n_c/n) F_c(w)" , SUN), ("n_c = 50, 30, 20  (xanh dương, xanh lá, hồng)" if LANG == "vi" else "n_c = 50, 30, 20  (blue, green, pink)", WHITE)], size=24)
        self.say(L("Bài 29-02: dữ liệu nằm trên K máy khách và không được gửi đi. Mục tiêu là cực tiểu F, trung bình có trọng số của các hàm mất mát riêng F_c.",
                   "Lesson 29-02: the data lives on K clients and may not leave them. The goal is to minimize F, the weighted average of the local losses F_c."), hold=10.0)
        self.say(L("Ví dụ: ba máy, mỗi máy một hàm bậc hai với đáy riêng (ngôi sao) và hình dạng riêng, như mỗi máy chỉ thấy một kiểu dữ liệu. Đường mức là của F, đáy chung là w* (chấm trắng).",
                   "Example: three clients, each with a quadratic with its own bottom (star) and its own shape, as if each saw only one kind of data. The contours are F's, and its bottom is w* (white dot)."), hold=10.0)
        # ---- stage 2
        self.stage(2)
        self.readout([("1. máy chủ gửi w_t" if LANG == "vi" else "1. server broadcasts w_t", WHITE), ("2. mỗi máy chạy E bước GD trên F_c" if LANG == "vi" else "2. each client runs E GD steps on F_c", SKY), ("3. w_{t+1} = Σ (n_c/n) w_c", SUN)], size=24)
        self.say(L("FedAvg lặp các vòng giao tiếp: máy chủ gửi mô hình w_t, mỗi máy tự chạy E bước trên dữ liệu của mình, rồi máy chủ lấy trung bình có trọng số các kết quả.",
                   "FedAvg repeats communication rounds: the server sends the model w_t, each client runs E steps on its own data, then the server takes a weighted average of the results."), hold=11.0)
        self.say(L("Với E = 1, trung bình của ba bước gradient chính là một bước gradient của F: FedAvg lúc đó chỉ là GD thường, chính xác nhưng tốn một vòng giao tiếp cho mỗi bước.",
                   "With E = 1, the average of three gradient steps is exactly one gradient step on F: FedAvg is then plain GD, exact but costing one communication round per step."), hold=11.0)
        self.say(L("Giao tiếp mới là thứ đắt. Nên ta muốn E lớn: mỗi vòng làm được nhiều việc hơn. Câu hỏi là cái giá phải trả.",
                   "Communication is the expensive part. So we want a large E: more work per round. The question is what it costs."), hold=9.0)
        # ---- stage 3
        self.stage(3)
        H5, P5 = RUN[5]
        d = Dot(ax.c2p(*W0), radius=0.1, color=SUN); self.add(d)
        def rr(E, r, H): self.readout([("E = %d,  vòng %d" % (E, r) if LANG == "vi" else "E = %d,  round %d" % (E, r), SUN), ("w = %s,  F − F* = %s" % (vec(H[r], 3), nf(FG(H[r]) - FS, 3)), WHITE)], size=23)
        rr(5, 0, H5)
        trailg = VGroup()
        for r in range(4):
            ls = VGroup(*[VMobject(color=c, stroke_width=3).set_points_as_corners([ax.c2p(*q) for q in P5[r][i]]) for i, c in enumerate(COL)])
            ends = VGroup(*[Dot(ax.c2p(*P5[r][i][-1]), radius=0.06, color=c) for i, c in enumerate(COL)])
            self.play(Create(ls), FadeIn(ends), run_time=1.0 if r == 0 else 0.6)
            seg = Line(ax.c2p(*H5[r]), ax.c2p(*H5[r + 1]), color=SUN, stroke_width=3.5); trailg.add(seg)
            self.play(d.animate.move_to(ax.c2p(*H5[r + 1])), Create(seg), FadeOut(ls), FadeOut(ends), run_time=0.6)
            rr(5, r + 1, H5)
            if r == 0:
                self.say(L("Chạy E = 5. Vòng 1: mỗi máy đi 5 bước về phía ngôi sao của mình (các nét màu), rồi máy chủ lấy trung bình ra điểm vàng. F giảm rất nhanh.",
                           "Run E = 5. Round 1: each client walks 5 steps toward its own star (colored strokes), then the server averages them into the yellow point. F drops very fast."), hold=11.0)
        self.say(L("Nhưng để ý: điểm vàng không dừng ở w*. Mỗi máy kéo về đáy riêng của nó, và trung bình các điểm kéo đó không phải là đáy của F.",
                   "But notice: the yellow point does not stop at w*. Each client pulls toward its own bottom, and the average of those pulls is not the bottom of F."), hold=10.0)
        for r in range(4, 40):
            seg = Line(ax.c2p(*H5[r]), ax.c2p(*H5[r + 1]), color=SUN, stroke_width=3.5); trailg.add(seg)
            self.play(d.animate.move_to(ax.c2p(*H5[r + 1])), Create(seg), run_time=0.06)
        rr(5, 40, H5)
        H20 = RUN[20][0]; d2 = Dot(ax.c2p(*W0), radius=0.1, color=ORANGE); self.add(d2)
        tr2 = VGroup()
        for r in range(12):
            seg = Line(ax.c2p(*H20[r]), ax.c2p(*H20[r + 1]), color=ORANGE, stroke_width=3.5); tr2.add(seg)
            self.play(d2.animate.move_to(ax.c2p(*H20[r + 1])), Create(seg), run_time=0.25)
        self.readout([("E = 5:  dừng cách w* %s" % nf(DIST[5], 3) if LANG == "vi" else "E = 5:  stops %s from w*" % nf(DIST[5], 3), SUN), ("E = 20: dừng cách w* %s" % nf(DIST[20], 3) if LANG == "vi" else "E = 20: stops %s from w*" % nf(DIST[20], 3), ORANGE)], size=23)
        self.say(L("Đó là hiện tượng trôi của máy khách. Với E = 5, FedAvg dừng cách w* một đoạn %s. Với E = 20 (cam) còn trôi xa hơn, %s: mỗi máy gần như chạy tới tận đáy riêng." % (nf(DIST[5], 3), nf(DIST[20], 3)),
                   "This is client drift. With E = 5, FedAvg stops %s away from w*. With E = 20 (orange) it drifts further, %s: each client nearly reaches its own bottom." % (nf(DIST[5], 3), nf(DIST[20], 3))), hold=10.0)
        bav = Cross(scale_factor=0.13, stroke_color=ORANGE, stroke_width=5).move_to(ax.c2p(*BAVG)); self.play(FadeIn(bav), run_time=0.3)
        self.readout([("Σ (n_c/n)·b_c = (0,7; 0,4)  (dấu ×)" if LANG == "vi" else "Σ (n_c/n)·b_c = (0.7, 0.4)  (the ×)", ORANGE), ("w* = (1,170; 0,735)" if LANG == "vi" else "w* = (1.170, 0.735)", WHITE)], size=23)
        self.say(L("Vì sao? Khi E rất lớn, mỗi máy tới đúng đáy riêng b_c, và máy chủ chỉ còn lấy trung bình các đáy: (0,7; 0,4), dấu ×. Nhưng w* còn phụ thuộc hình dạng từng hàm, nên khác hẳn.",
                   "Why? When E is very large each client reaches its own bottom b_c, and the server just averages the bottoms: (0.7, 0.4), the ×. But w* also depends on each function's shape, so it is quite different."), hold=11.0)
        # ---- stage 4
        self.stage(4); self.wipe()
        fx = plain_axes([0, 40], [0, 5], 7.4, 4.4, [0.25, 2.0, 0])
        yt = VGroup(*[Text(s_, font=MONO, font_size=17, color=DIM).next_to(fx.c2p(0, v + 4), LEFT, buff=0.1) for v, s_ in ((0, "1"), (-2, "10⁻²"), (-4, "10⁻⁴"))])
        xt = VGroup(*[Text(str(v), font=MONO, font_size=17, color=DIM).next_to(fx.c2p(v, 0), DOWN, buff=0.1) for v in (10, 20, 30, 40)])
        yl = Text("F − F*", font=MONO, font_size=20, color=DIM).next_to(fx.c2p(0, 5), UR, buff=0.08)
        self.play(Create(fx), FadeIn(yt), FadeIn(xt), FadeIn(yl), run_time=0.5)
        cv = lambda E, c: VMobject(color=c, stroke_width=3.5).set_points_as_corners([fx.c2p(r, max(np.log10(max(GAP[E][r], 1e-12)), -4) + 4) for r in range(41)])
        cc = [cv(1, SKY), cv(5, SUN), cv(20, ORANGE)]
        self.play(*[Create(c) for c in cc], run_time=2.0, rate_func=linear)
        self.readout([("theo vòng giao tiếp:  tới F − F* < 0,3   sàn" if LANG == "vi" else "per communication round:  to F − F* < 0.3   floor", WHITE), ("E = 1  (GD):    %d vòng      0" % RT[1] if LANG == "vi" else "E = 1  (GD):    %d rounds    0" % RT[1], SKY), ("E = 5:          %d vòng      %s" % (RT[5], nf(PLAT[5], 3)) if LANG == "vi" else "E = 5:          %d rounds    %s" % (RT[5], nf(PLAT[5], 3)), SUN), ("E = 20:         %d vòng      %s" % (RT[20], nf(PLAT[20], 3)) if LANG == "vi" else "E = 20:         %d round     %s" % (RT[20], nf(PLAT[20], 3)), ORANGE)], size=21)
        self.say(L("Đặt cạnh nhau theo số vòng giao tiếp. Để F − F* < 0,3, E = 1 cần %d vòng, E = 5 cần %d, E = 20 chỉ cần %d. Đó là khoản tiết kiệm giao tiếp." % (RT[1], RT[5], RT[20]),
                   "Side by side, per communication round. To reach F − F* < 0.3, E = 1 needs %d rounds, E = 5 needs %d, E = 20 only %d. That is the communication saving." % (RT[1], RT[5], RT[20])), hold=11.0)
        self.say(L("Nhưng E lớn thì kẹt ở một sàn: %s với E = 5, %s với E = 20. Chỉ E = 1 đi thẳng tới tối ưu. Đúng như bài nói: E > 1 trôi khi dữ liệu không IID." % (nf(PLAT[5], 3), nf(PLAT[20], 3)),
                   "But large E gets stuck at a floor: %s with E = 5, %s with E = 20. Only E = 1 goes all the way. Just as the lesson says: E > 1 drifts on non-IID data." % (nf(PLAT[5], 3), nf(PLAT[20], 3))), hold=11.0)
        self.say(L("Nếu dữ liệu IID, mọi máy có cùng hàm F, nên E bước cục bộ chỉ là E bước GD: không trôi. Còn khi không IID, giảm dần bước cục bộ sẽ kéo sai số về 0 (E = 5: cách w* dưới 0,001 sau 2000 vòng).",
                   "With IID data every client has the same F, so E local steps are just E GD steps: no drift. On non-IID data, a decaying local step drives the error to 0 (E = 5: under 0.001 from w* after 2000 rounds)."), hold=11.0)
        self.takeaway([L("FedAvg: gửi w, mỗi máy chạy E bước, lấy trung bình có trọng số.", "FedAvg: send w, each client runs E steps, take a weighted average."),
                       L("E = 1 chính là GD; E lớn tiết kiệm vòng giao tiếp.", "E = 1 is exactly GD; large E saves communication rounds."),
                       L("Dữ liệu không IID: mỗi máy kéo về đáy riêng, gây trôi.", "Non-IID data: each client pulls toward its own bottom, causing drift."),
                       L("Chọn E là đánh đổi giữa giao tiếp và độ chính xác.", "Choosing E trades communication against accuracy.")], tail=4.0)
