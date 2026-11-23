from rl import *
# Bài 03-01-01 / 03-01-03: hàm lồi qua bốn phép thử: dây cung, tiếp tuyến, đạo hàm bậc hai, epigraph
f = lambda x: x * x                      # hàm lồi trong bài 03-01-03
g = lambda x: x ** 4 - 3 * x ** 2        # hàm không lồi để đối chiếu
df = lambda x: 2 * x; dg = lambda x: 4 * x ** 3 - 6 * x; d2g = lambda x: 12 * x * x - 6
XS = np.linspace(-2, 3, 501)
# dây cung: ví dụ Jensen của bài, x₁ = 1, x₂ = 3
chord = lambda z: 1 + (z - 1) * (9 - 1) / 2
TH = (0.5, 0.25, 0.8)
CH = [(t * 1 + (1 - t) * 3, f(t * 1 + (1 - t) * 3), t * f(1) + (1 - t) * f(3)) for t in TH]
assert CH[0] == (2, 4, 5) and np.allclose(CH[1], (2.5, 6.25, 7)) and np.allclose(CH[2], (1.4, 1.96, 2.6))
assert all(f(t * a + (1 - t) * b) <= t * f(a) + (1 - t) * f(b) + 1e-12 for a in XS[::25] for b in XS[::25] for t in np.linspace(0, 1, 11))
assert np.isclose(g(1.5), -1.6875) and g(0) == 0 > g(1.5)             # dây cung của g nằm dưới đồ thị tại 0
# tiếp tuyến: f(y) − [f(x₀) + f'(x₀)(y − x₀)] = (y − x₀)²
assert all(np.isclose(f(y) - f(x0) - df(x0) * (y - x0), (y - x0) ** 2) for x0 in XS[::50] for y in XS[::50])
T0 = 0.5; tg = lambda y: g(T0) + dg(T0) * (y - T0)
assert np.isclose(g(T0), -0.6875) and np.isclose(dg(T0), -2.5) and np.isclose(tg(0), 0.5625) and tg(0) > g(0)
# bậc hai
EH = np.linalg.eigvalsh(np.array([[2., 1], [1, 4]])); assert np.allclose(EH, [3 - 2 ** .5, 3 + 2 ** .5]) and EH.min() > 0
assert np.isclose((6 / 12) ** .5, 0.7071, atol=1e-4) and d2g(0) == -6 and d2g(1) == 6
# epigraph và tập mức dưới
assert np.isclose(g(1.2), -2.2464) and g(0) > g(1.2)
r1, r2 = ((3 - 5 ** .5) / 2) ** .5, ((3 + 5 ** .5) / 2) ** .5
assert np.isclose(r1, 0.618, atol=1e-3) and np.isclose(r2, 1.618, atol=1e-3) and np.isclose(g(r1), -1) and np.isclose(g(r2), -1)
xx = np.linspace(-2, 2, 40001); S = xx[g(xx) <= -1]; jumps = np.sum(np.diff(S) > 1e-3); assert jumps == 1
h = lambda x: abs(x) ** .5; assert np.isclose(h(0.5), 0.7071, atol=1e-4) and h(0.5) > 0.5 * h(0) + 0.5 * h(1)

class Cvx(Reel):
    def construct(self):
        self.title(L("Hàm lồi:\nbốn cách kiểm tra", "Convex functions:\nfour ways to check"))
        ax = plain_axes([-2.2, 3.3], [-2.6, 10], 7.6, 6.3, [0, 1.0, 0])
        # ---- stage 1
        self.stage(1)
        cf = ax.plot(f, x_range=[-2.2, 3.15], color=SKY, stroke_width=4)
        lf = Text("f(x) = x²", font=MONO, font_size=24, color=SKY).next_to(ax.c2p(-1.6, 7.5), UP, buff=0)
        self.play(Create(ax), Create(cf), FadeIn(lf), run_time=1.2)
        self.say(L("Bài 03-01-01: f lồi nếu với mọi x, y và 0 ≤ θ ≤ 1, giá trị tại điểm trộn không vượt quá trộn các giá trị.",
                   "Lesson 03-01-01: f is convex if for all x, y and 0 ≤ θ ≤ 1, the value at the mixed point is at most the mix of the values."), hold=7.5)
        self.readout(["f(θx + (1−θ)y) ≤ θf(x) + (1−θ)f(y)"], color=SUN, size=25)
        A, B = Dot(ax.c2p(1, 1), color=SUN, radius=0.09), Dot(ax.c2p(3, 9), color=SUN, radius=0.09)
        cl = Line(ax.c2p(1, 1), ax.c2p(3, 9), color=SUN, stroke_width=3.5)
        self.play(FadeIn(A), FadeIn(B), Create(cl), run_time=0.7)
        self.say(L("Hình học: dây cung nối (x, f(x)) và (y, f(y)) luôn nằm trên đồ thị. Ở đây x = 1, y = 3 như ví dụ trong bài 03-01-03.",
                   "Geometrically: the chord joining (x, f(x)) and (y, f(y)) always lies above the graph. Here x = 1, y = 3, as in the example of lesson 03-01-03."), hold=8.0)
        th = ValueTracker(0.5)
        z = lambda: th.get_value() + (1 - th.get_value()) * 3
        gap = always_redraw(lambda: Line(ax.c2p(z(), f(z())), ax.c2p(z(), chord(z())), color=MINT, stroke_width=6))
        dz = always_redraw(lambda: Dot(ax.c2p(z(), f(z())), color=MINT, radius=0.08))
        self.add(gap, dz)
        def ro(i): self.readout([("θ = %s:  điểm %s" % (nf(TH[i], 2), nf(CH[i][0], 1)) if LANG == "vi" else "θ = %s:  point %s" % (nf(TH[i], 2), nf(CH[i][0], 1)), WHITE), ("f = %s  ≤  dây cung %s" % (nf(CH[i][1], 2), nf(CH[i][2], 2)) if LANG == "vi" else "f = %s  ≤  chord %s" % (nf(CH[i][1], 2), nf(CH[i][2], 2)), MINT)], size=24)
        ro(0)
        self.say(L("θ = 0,5: điểm giữa là 2, f(2) = 4, còn dây cung cho 5. Đoạn xanh lá là khoảng cách, luôn ≥ 0.",
                   "θ = 0.5: the midpoint is 2, f(2) = 4, while the chord gives 5. The green segment is the gap, always ≥ 0."), hold=7.0)
        for i in (1, 2):
            self.play(th.animate.set_value(TH[i]), run_time=1.2); ro(i); self.wait(1.6)
        self.say(L("Đây cũng là bất đẳng thức Jensen với hai điểm: f của trung bình ≤ trung bình của f.",
                   "This is also Jensen's inequality with two points: f of the average ≤ the average of f."), hold=6.0)
        self.play(*[FadeOut(m) for m in (gap, dz, A, B, cl)], run_time=0.4); self.remove(gap, dz)
        cg = ax.plot(g, x_range=[-2.05, 2.05], color=PINK, stroke_width=4)
        lg = Text("g(x) = x⁴ − 3x²", font=MONO, font_size=24, color=PINK).next_to(ax.c2p(1.4, 4.6), RIGHT, buff=0.05).shift(LEFT * 0.4 + UP * 0.2)
        self.play(FadeOut(cf), FadeOut(lf), Create(cg), FadeIn(lg), run_time=1.0)
        A2, B2 = Dot(ax.c2p(-1.5, g(1.5)), color=SUN, radius=0.09), Dot(ax.c2p(1.5, g(1.5)), color=SUN, radius=0.09)
        cl2 = Line(ax.c2p(-1.5, g(1.5)), ax.c2p(1.5, g(1.5)), color=SUN, stroke_width=3.5)
        bad = Line(ax.c2p(0, g(1.5)), ax.c2p(0, 0), color=ORANGE, stroke_width=6)
        self.play(FadeIn(A2), FadeIn(B2), Create(cl2), run_time=0.6); self.play(Create(bad), run_time=0.5)
        self.readout([("g(−1,5) = g(1,5) = −1,6875" if LANG == "vi" else "g(−1.5) = g(1.5) = −1.6875", SUN), ("giữa: g(0) = 0  >  −1,6875" if LANG == "vi" else "middle: g(0) = 0  >  −1.6875", ORANGE)], size=24)
        self.say(L("Đối chiếu với g = x⁴ − 3x² hình chữ W. Dây cung từ −1,5 đến 1,5 nằm ở −1,6875, nhưng g(0) = 0 cao hơn. Một lần vi phạm là đủ: g không lồi.",
                   "Compare g = x⁴ − 3x², a W shape. The chord from −1.5 to 1.5 sits at −1.6875, but g(0) = 0 is higher. One violation is enough: g is not convex."), hold=9.0)
        self.play(*[FadeOut(m) for m in (A2, B2, cl2, bad)], run_time=0.3)
        # ---- stage 2
        self.stage(2)
        self.play(FadeOut(cg), FadeOut(lg), FadeIn(cf), FadeIn(lf), run_time=0.6)
        x0 = ValueTracker(1.0)
        tl = always_redraw(lambda: ax.plot(lambda y: f(x0.get_value()) + df(x0.get_value()) * (y - x0.get_value()), x_range=[max(-2.2, x0.get_value() - 1.6), min(3.3, x0.get_value() + 1.6)], color=SUN, stroke_width=3.5))
        tp = always_redraw(lambda: Dot(ax.c2p(x0.get_value(), f(x0.get_value())), color=SUN, radius=0.09))
        self.add(tl, tp)
        self.readout(["f(y) ≥ f(x₀) + f′(x₀)(y − x₀)", ("x²: hiệu = (y − x₀)² ≥ 0" if LANG == "vi" else "x²: gap = (y − x₀)² ≥ 0", MINT)], color=SUN, size=24)
        self.say(L("Bài 03-01-03, điều kiện bậc nhất: f khả vi thì lồi khi và chỉ khi tiếp tuyến tại mọi điểm nằm dưới toàn bộ đồ thị.",
                   "Lesson 03-01-03, first-order condition: a differentiable f is convex if and only if the tangent at every point lies below the whole graph."), hold=8.0)
        self.play(x0.animate.set_value(-1.5), run_time=2.0); self.play(x0.animate.set_value(2.4), run_time=2.5)
        self.say(L("Với x², lấy f(y) trừ tiếp tuyến ta được đúng (y − x₀)², luôn không âm. Xoay x₀ đi đâu, tiếp tuyến vẫn ở dưới.",
                   "For x², f(y) minus the tangent is exactly (y − x₀)², never negative. Move x₀ anywhere: the tangent stays below."), hold=7.5)
        self.play(x0.animate.set_value(0.0), run_time=1.2)
        self.say(L("Hệ quả quan trọng: nếu f′(x₀) = 0 thì tiếp tuyến nằm ngang, nên f(y) ≥ f(x₀) với mọi y. Điểm dừng của hàm lồi là cực tiểu toàn cục.",
                   "Key consequence: if f′(x₀) = 0 the tangent is flat, so f(y) ≥ f(x₀) for all y. A stationary point of a convex function is a global minimum."), hold=8.5)
        self.remove(tl, tp)
        self.play(FadeOut(cf), FadeOut(lf), FadeIn(cg), FadeIn(lg), run_time=0.6)
        tl2 = ax.plot(tg, x_range=[-0.6, 1.6], color=SUN, stroke_width=3.5); tp2 = Dot(ax.c2p(T0, g(T0)), color=SUN, radius=0.09)
        bad2 = Line(ax.c2p(0, 0), ax.c2p(0, tg(0)), color=ORANGE, stroke_width=6)
        self.play(Create(tl2), FadeIn(tp2), run_time=0.6); self.play(Create(bad2), run_time=0.4)
        self.readout([("tiếp tuyến của g tại x₀ = 0,5" if LANG == "vi" else "tangent of g at x₀ = 0.5", SUN), ("tại y = 0: 0,5625  >  g(0) = 0" if LANG == "vi" else "at y = 0: 0.5625  >  g(0) = 0", ORANGE)], size=24)
        self.say(L("Với g, tiếp tuyến tại 0,5 cắt lên trên đồ thị: tại y = 0 tiếp tuyến cho 0,5625 nhưng g(0) = 0. Phép thử thất bại.",
                   "For g, the tangent at 0.5 cuts above the graph: at y = 0 the tangent gives 0.5625 but g(0) = 0. The test fails."), hold=8.0)
        self.play(FadeOut(tl2), FadeOut(tp2), FadeOut(bad2), run_time=0.3)
        # ---- stage 3
        self.stage(3)
        a = (6 / 12) ** .5
        conc = ax.plot(g, x_range=[-a, a], color=ORANGE, stroke_width=9)
        self.play(Create(conc), run_time=0.8)
        self.readout([("f″(x) = 2 > 0 mọi nơi  ⇒ lồi" if LANG == "vi" else "f″(x) = 2 > 0 everywhere  ⇒ convex", SKY), ("g″(x) = 12x² − 6 < 0 khi |x| < 0,707" if LANG == "vi" else "g″(x) = 12x² − 6 < 0 for |x| < 0.707", ORANGE)], size=24)
        self.say(L("Điều kiện bậc hai: f khả vi hai lần thì lồi khi và chỉ khi f″ ≥ 0, tức đồ thị luôn cong lên.",
                   "Second-order condition: a twice-differentiable f is convex if and only if f″ ≥ 0, i.e. the graph always curves up."), hold=7.0)
        self.say(L("x² có f″ = 2 ở mọi nơi. Còn g″ = 12x² − 6 âm khi |x| < 0,707: đoạn cam là chỗ g cong xuống, chính là nơi dây cung và tiếp tuyến thất bại.",
                   "x² has f″ = 2 everywhere. But g″ = 12x² − 6 is negative for |x| < 0.707: the orange piece is where g curves down, exactly where the chord and tangent tests failed."), hold=9.5)
        self.wipe()
        rows = VGroup(*[Text(s_, font=MONO, font_size=26, color=c_) for s_, c_ in (
            ("nhiều biến: ∇²f(x) ⪰ 0" if LANG == "vi" else "many variables: ∇²f(x) ⪰ 0", SUN),
            ("x₁² + x₁x₂ + 2x₂²", SKY), ("H = [[2, 1], [1, 4]]", SKY),
            ("trị riêng 3 ± √2 = %s; %s  ⇒ lồi" % (nf(EH[0], 3), nf(EH[1], 3)) if LANG == "vi" else "eigenvalues 3 ± √2 = %s, %s  ⇒ convex" % (nf(EH[0], 3), nf(EH[1], 3)), MINT),
            ("x₁² − x₂²", PINK), ("H = diag(2, −2)", PINK),
            ("trị riêng 2 và −2  ⇒ không lồi" if LANG == "vi" else "eigenvalues 2 and −2  ⇒ not convex", ORANGE))]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, 1.0, 0])
        self.play(FadeIn(rows, lag_ratio=0.15), run_time=1.5)
        self.say(L("Nhiều biến thì thay f″ bằng ma trận Hessian và đòi nó nửa xác định dương: mọi trị riêng ≥ 0.",
                   "With many variables, replace f″ by the Hessian matrix and require it to be positive semidefinite: all eigenvalues ≥ 0."), hold=7.0)
        self.say(L("Ví dụ của bài 04-03: x₁² + x₁x₂ + 2x₂² có trị riêng 3 ± √2, đều dương nên lồi. Còn x₁² − x₂² có một trị riêng âm: hình yên ngựa, không lồi.",
                   "Example from lesson 04-03: x₁² + x₁x₂ + 2x₂² has eigenvalues 3 ± √2, both positive, so it is convex. x₁² − x₂² has a negative eigenvalue: a saddle, not convex."), hold=9.5)
        # ---- stage 4
        self.stage(4); self.wipe()
        ax2 = plain_axes([-2.2, 2.2], [-2.6, 6], 7.6, 6.3, [0, 1.0, 0]); self.play(Create(ax2), run_time=0.4)
        xs = np.linspace(-2.2, 2.2, 89)
        ep = Polygon(*[ax2.c2p(x, min(f(x), 6)) for x in xs], ax2.c2p(2.2, 6), ax2.c2p(-2.2, 6), stroke_width=0, fill_color=SKY, fill_opacity=0.35)
        cf2 = ax2.plot(f, x_range=[-2.2, 2.2], color=SKY, stroke_width=4).set_z_index(2)
        self.play(FadeIn(ep), Create(cf2), run_time=0.8)
        self.readout([("epi f = {(x, t) : f(x) ≤ t}" if LANG == "vi" else "epi f = {(x, t) : f(x) ≤ t}", SUN), ("f lồi  ⇔  epi f là tập lồi" if LANG == "vi" else "f convex  ⇔  epi f is a convex set", WHITE)], size=24)
        self.say(L("Cách thứ tư: epigraph, phần mặt phẳng nằm trên đồ thị. f lồi khi và chỉ khi tập này lồi: nối hai điểm bất kỳ trong vùng xanh, đoạn thẳng vẫn ở trong.",
                   "Fourth way: the epigraph, the region above the graph. f is convex if and only if this set is convex: join any two points in the blue region and the segment stays inside."), hold=9.5)
        ep2 = Polygon(*[ax2.c2p(x, min(g(x), 6)) for x in xs], ax2.c2p(2.2, 6), ax2.c2p(-2.2, 6), stroke_width=0, fill_color=PINK, fill_opacity=0.35)
        cg2 = ax2.plot(g, x_range=[-2.05, 2.05], color=PINK, stroke_width=4).set_z_index(2)
        self.play(FadeOut(ep), FadeOut(cf2), FadeIn(ep2), Create(cg2), run_time=0.8)
        P1, P2 = Dot(ax2.c2p(-1.2, g(1.2)), color=SUN, radius=0.09).set_z_index(3), Dot(ax2.c2p(1.2, g(1.2)), color=SUN, radius=0.09).set_z_index(3)
        sg = Line(P1.get_center(), P2.get_center(), color=SUN, stroke_width=3.5).set_z_index(3); mid = Dot(ax2.c2p(0, g(1.2)), color=ORANGE, radius=0.1).set_z_index(3)
        self.play(FadeIn(P1), FadeIn(P2), Create(sg), FadeIn(mid), run_time=0.7)
        self.readout([("(±1,2; −2,2464) thuộc epi g" if LANG == "vi" else "(±1.2, −2.2464) are in epi g", SUN), ("trung điểm (0; −2,2464): g(0) = 0 > −2,2464" if LANG == "vi" else "midpoint (0, −2.2464): g(0) = 0 > −2.2464", ORANGE)], size=23)
        self.say(L("Epigraph của g có hai cái túi. Hai điểm vàng nằm trong, nhưng trung điểm (cam) nằm dưới đồ thị, ra ngoài tập. Không lồi.",
                   "The epigraph of g has two pockets. Both yellow points are inside, but the midpoint (orange) is below the graph, outside the set. Not convex."), hold=8.5)
        lv = DashedLine(ax2.c2p(-2.2, -1), ax2.c2p(2.2, -1), color=MINT, stroke_width=2.5)
        s1 = Line(ax2.c2p(-r2, -2.45), ax2.c2p(-r1, -2.45), color=MINT, stroke_width=9); s2 = Line(ax2.c2p(r1, -2.45), ax2.c2p(r2, -2.45), color=MINT, stroke_width=9)
        self.play(FadeOut(sg), FadeOut(mid), FadeOut(P1), FadeOut(P2), Create(lv), Create(s1), Create(s2), run_time=0.8)
        self.readout([("{g ≤ −1} = [−1,618; −0,618] ∪ [0,618; 1,618]" if LANG == "vi" else "{g ≤ −1} = [−1.618, −0.618] ∪ [0.618, 1.618]", MINT), ("{f ≤ 4} = [−2; 2]: một đoạn" if LANG == "vi" else "{f ≤ 4} = [−2, 2]: one interval", SKY)], size=23)
        self.say(L("Tập mức dưới của hàm lồi luôn lồi. {g ≤ −1} là hai đoạn rời nhau, nên lại thấy g không lồi.",
                   "Sublevel sets of a convex function are always convex. {g ≤ −1} is two separate intervals, so again g is not convex."), hold=7.5)
        self.readout([("h = √|x|:  {h ≤ t} = [−t²; t²], một đoạn" if LANG == "vi" else "h = √|x|:  {h ≤ t} = [−t², t²], one interval", MINT), ("h(0,5) ≈ 0,707  >  ½h(0) + ½h(1) = 0,5" if LANG == "vi" else "h(0.5) ≈ 0.707  >  ½h(0) + ½h(1) = 0.5", ORANGE)], size=23)
        self.say(L("Nhưng chiều ngược lại sai: √|x| có mọi tập mức dưới là một đoạn, vậy mà √0,5 ≈ 0,707 lớn hơn trung bình 0,5 của √0 và √1. Tập mức lồi chưa đủ.",
                   "But the converse is false: √|x| has every sublevel set an interval, yet √0.5 ≈ 0.707 is larger than 0.5, the average of √0 and √1. Convex sublevel sets are not enough."), hold=9.5)
        self.takeaway([L("Dây cung nằm trên đồ thị: định nghĩa, cũng là Jensen.", "The chord lies above the graph: the definition, also Jensen."),
                       L("Tiếp tuyến nằm dưới đồ thị; nên ∇f = 0 là cực tiểu toàn cục.", "The tangent lies below the graph; so ∇f = 0 is a global minimum."),
                       L("Hessian ⪰ 0: đồ thị luôn cong lên.", "Hessian ⪰ 0: the graph always curves up."),
                       L("f lồi ⇔ epigraph lồi; tập mức dưới lồi là cần, chưa đủ.", "f convex ⇔ epigraph convex; convex sublevel sets are necessary, not sufficient.")])
