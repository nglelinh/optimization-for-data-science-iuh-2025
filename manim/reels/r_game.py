from rl import *
P = np.array([[2, 0, -1], [-3, 1, 2]], float)
col = lambda j, x: P[0, j] * x + P[1, j] * (1 - x)
xs = np.linspace(0, 1, 100001); env = np.max([col(j, xs) for j in range(3)], axis=0)
assert abs(env.min() - 1 / 3) < 1e-4 and abs(xs[env.argmin()] - 2 / 3) < 1e-4
YS = np.array([1 / 6, 5 / 6, 0])
assert np.allclose(P @ YS, [1 / 3, 1 / 3]) and abs(np.array([2 / 3, 1 / 3]) @ P @ YS - 1 / 3) < 1e-12
assert all(np.array([2 / 3, 1 / 3]) @ P[:, j] <= 1 / 3 + 1e-12 for j in range(3))
PURE_J = P.max(axis=1).min(); PURE_R = P.min(axis=0).max()
assert PURE_J == 2 and PURE_R == 0
def fict(n):
    cr = np.zeros(2); cc = np.zeros(3); cr[0] = 1; cc[0] = 1; out = []
    for k in range(1, n + 1):
        xr = cr / cr.sum(); yc = cc / cc.sum()
        out.append((k, xr.copy(), yc.copy(), (P @ yc).min(), (xr @ P).max()))
        i = int(np.argmin(P @ yc)); j = int(np.argmax(xr @ P)); cr[i] += 1; cc[j] += 1
    return out
FP = fict(5000)
assert all(r[3] <= 1 / 3 + 1e-12 <= r[4] + 2e-12 for r in FP) and FP[-1][4] - FP[-1][3] < 0.03

class Game(Reel):
    def construct(self):
        self.title(L("Trò chơi ma trận:\nminimax và đối ngẫu", "A matrix game:\nminimax and duality"))
        self.stage(1)
        cells = VGroup()
        for i in range(2):
            for j in range(3):
                r = Square(1.25, stroke_color=DIM, stroke_width=2, fill_color=CARD, fill_opacity=1).move_to([(j - 1) * 1.25 + 0.5, 2.4 - i * 1.25, 0])
                cells.add(VGroup(r, Text(nf(P[i, j], 0) if True else "", font=MONO, font_size=34, color=WHITE).move_to(r)))
        rl_ = VGroup(*[Text("J%d" % (i + 1) if LANG == "en" else "J%d" % (i + 1), font=FONT, font_size=26, color=SKY).move_to([-1.75, 2.4 - i * 1.25, 0]) for i in range(2)])
        cl_ = VGroup(*[Text("R%d" % (j + 1), font=FONT, font_size=26, color=PINK).move_to([(j - 1) * 1.25 + 0.5, 3.45, 0]) for j in range(3)])
        self.play(FadeIn(cells), FadeIn(rl_), FadeIn(cl_), run_time=0.8)
        self.say(L("J chọn hàng, R chọn cột, cùng lúc. J trả cho R số tiền trong ô. J muốn nhỏ, R muốn lớn.",
                   "J picks a row, R picks a column, simultaneously. J pays R the number in the cell. J wants it small, R wants it large."), hold=5.0)
        # pure strategies
        self.readout(["J (thuần): min_hàng max_cột = %d" % PURE_J if LANG == "vi" else "J (pure): min over rows of row max = %d" % PURE_J,
                      "R (thuần): max_cột min_hàng = %d" % PURE_R if LANG == "vi" else "R (pure): max over cols of col min = %d" % PURE_R], color=WHITE, size=23, y=-0.4)
        self.say(L("Chơi thuần: J đảm bảo trả ≤ 2, R đảm bảo nhận ≥ 0. Còn một khoảng hở [0, 2].",
                   "Pure play: J can guarantee paying ≤ 2, R can guarantee getting ≥ 0. There is a gap [0, 2]."), hold=4.5)
        # key idea
        self.stage(2)
        self.say(L("Ý tưởng: chơi ngẫu nhiên. J chọn hàng 1 với xác suất x. Mỗi cột cho R một đường thẳng theo x.",
                   "The idea: randomize. J plays row 1 with probability x. Each column gives R a line in x."), hold=4.5)
        self.play(FadeOut(cells), FadeOut(rl_), FadeOut(cl_), run_time=0.4); self.clear_ro()
        ax = plain_axes([0, 1], [-3.2, 2.4], 6.6, 5.6, [0.2, 1.4, 0], ticks=False)
        cols = [SKY, PINK, ORANGE]
        self.play(Create(ax), run_time=0.4)
        ls = VGroup(*[Line(ax.c2p(0, col(j, 0)), ax.c2p(1, col(j, 1)), color=cols[j], stroke_width=4) for j in range(3)])
        labs = VGroup(*[Text("R%d" % (j + 1), font=FONT, font_size=22, color=cols[j]).next_to(ax.c2p(1, col(j, 1)), RIGHT, buff=0.1) for j in range(3)])
        xl = VGroup(Text("x = 0", font=FONT, font_size=20, color=DIM).next_to(ax.c2p(0, -3.2), DOWN, buff=0.1), Text("x = 1", font=FONT, font_size=20, color=DIM).next_to(ax.c2p(1, -3.2), DOWN, buff=0.1))
        self.play(Create(ls), FadeIn(labs), FadeIn(xl), run_time=1.0)
        e = VMobject(color=SUN, stroke_width=9).set_points_as_corners([ax.c2p(x, v) for x, v in zip(xs[::500], env[::500])])
        self.play(Create(e), run_time=1.5)
        self.say(L("R sẽ đáp lại bằng cột tốt nhất, nên J phải trả theo đường bao trên (vàng). J chọn x hạ thấp nó nhất.",
                   "R will answer with the best column, so J pays the upper envelope (yellow). J picks the x that lowers it most."), hold=5.0)
        m = Dot(ax.c2p(2 / 3, 1 / 3), radius=0.16, color=MINT); self.play(FadeIn(m, scale=1.5), run_time=0.4)
        self.readout(["x* = 2/3   →   J trả ≤ 1/3" if LANG == "vi" else "x* = 2/3   →   J pays ≤ 1/3"], color=MINT, size=26)
        self.say(L("Đáy đường bao: x = 2/3, giá trị 1/3. Chơi hỗn hợp, J đảm bảo trả không quá 1/3.", "Bottom of the envelope: x = 2/3, value 1/3. Mixing, J guarantees paying at most 1/3."))
        # algorithm: fictitious play
        self.stage(3)
        self.say(L("Fictitious play: mỗi vòng, mỗi người đáp trả tốt nhất với tần suất chơi trong quá khứ của đối thủ.",
                   "Fictitious play: each round, each player best-responds to the opponent's past frequencies."), hold=4.5)
        dj = Dot(ax.c2p(FP[0][1][0], (FP[0][1] @ P).max()), radius=0.12, color=SKY); self.add(dj)
        for k in (1, 2, 3, 4, 5, 6, 8, 10, 15, 20, 50, 100, 500, 1000, 5000):
            r = FP[k - 1]; xr = r[1]
            self.play(dj.animate.move_to(ax.c2p(xr[0], (xr @ P).max())), run_time=0.45)
            self.readout(["vòng %d   x = %s" % (k, nf(xr[0], 3)) if LANG == "vi" else "round %d   x = %s" % (k, nf(xr[0], 3)),
                          ("cận dưới %s ≤ 1/3 ≤ cận trên %s" % (nf(r[3], 3), nf(r[4], 3)) if LANG == "vi" else "lower %s ≤ 1/3 ≤ upper %s" % (nf(r[3], 3), nf(r[4], 3)), MINT)], color=SKY, size=23)
            self.wait(0.5 if k < 10 else 0.35)
        self.say(L("Hai cận kẹp dần về 1/3: tần suất của J tiến tới 2/3, của R tới (1/6; 5/6; 0).", "The two bounds squeeze toward 1/3: J's frequency tends to 2/3, R's to (1/6, 5/6, 0)."))
        # contrast: duality
        self.stage(4); self.play(FadeOut(dj), run_time=0.2)
        self.say(L("Nhìn từ phía R: R trộn các cột với xác suất y. J đáp lại bằng hàng tốt nhất cho J.", "From R's side: R mixes the columns with probabilities y. J answers with J's best row."), hold=4.0)
        self.play(FadeOut(ls), FadeOut(labs), FadeOut(e), FadeOut(m), FadeOut(xl), run_time=0.4)
        row_ = lambda i, y: P[i, 0] * y + P[i, 1] * (1 - y)
        ys = np.linspace(0, 1, 2001); lo = np.minimum(row_(0, ys), row_(1, ys))
        assert abs(lo.max() - 1 / 3) < 1e-3 and abs(ys[lo.argmax()] - 1 / 6) < 1e-3
        rl2 = VGroup(*[Line(ax.c2p(0, row_(i, 0)), ax.c2p(1, row_(i, 1)), color=[SKY, PINK][i], stroke_width=4) for i in range(2)])
        lo_ = VMobject(color=MINT, stroke_width=9).set_points_as_corners([ax.c2p(y, v) for y, v in zip(ys[::20], lo[::20])])
        yl = Text("y₁: R1 vs R2" if LANG == "en" else "y₁: R1 hay R2", font=FONT, font_size=20, color=DIM).next_to(ax.c2p(0.5, -3.2), DOWN, buff=0.1)
        self.play(Create(rl2), FadeIn(yl), run_time=0.8); self.play(Create(lo_), run_time=1.2)
        mm = Dot(ax.c2p(1 / 6, 1 / 3), radius=0.16, color=MINT); self.play(FadeIn(mm, scale=1.5), run_time=0.4)
        self.readout(["max_y min_hàng = 1/3 = min_x max_cột" if LANG == "vi" else "max_y min_row = 1/3 = min_x max_col"], color=MINT, size=24)
        self.say(L("R đảm bảo nhận ít nhất 1/3 bằng y = (1/6; 5/6; 0). Khoảng hở [0, 2] của chơi thuần đóng lại tại đúng 1/3.",
                   "R guarantees at least 1/3 with y = (1/6, 5/6, 0). The pure-play gap [0, 2] closes at exactly 1/3."), hold=5.0)
        self.say(L("Hai bài toán của J và R là một cặp LP đối ngẫu: định lý minimax chính là đối ngẫu mạnh.",
                   "J's and R's problems form a primal-dual LP pair: the minimax theorem is strong duality."))
        self.takeaway([L("Chơi thuần để lại khoảng hở; chơi hỗn hợp đóng nó lại.", "Pure strategies leave a gap; mixed strategies close it."),
                       L("Giá trị trò chơi = 1/3: min_x max_y = max_y min_x.", "Game value = 1/3: min over x of max over y = max over y of min over x."),
                       L("Hai người chơi giải hai LP đối ngẫu nhau.", "The two players solve two LPs that are duals of each other.")])
