from rl import *
# Bài 04-03: điều kiện tối ưu bậc nhất  ∇f(x*)ᵀ(y − x*) ≥ 0 với mọi y ∈ C
V = np.array([[0., 0], [1, 0], [0, 1]])            # C = {x ≥ 0, x₁ + x₂ ≤ 1}: tam giác
def proj_simplex(v):
    u = np.sort(v)[::-1]; css = np.cumsum(u); r = np.nonzero(u * np.arange(1, 3) > css - 1)[0][-1]; t = (css[r] - 1) / (r + 1); return np.maximum(v - t, 0)
def PC(v):
    z = np.maximum(v, 0); return z if z.sum() <= 1 else proj_simplex(v)
P1 = np.array([1., 1.5]); P2 = np.array([2., -1.])
gradf = lambda x, p: 2 * (x - p)
test = lambda x, p: min(gradf(x, p) @ (v - x) for v in V)   # tuyến tính theo y ⇒ chỉ cần xét đỉnh
XS = np.array([0.25, 0.75]); XV = np.array([1., 0])
assert np.allclose(PC(P1), XS) and np.allclose(PC(P2), XV)
assert np.allclose(gradf(XS, P1), [-1.5, -1.5]) and np.allclose([gradf(XS, P1) @ (v - XS) for v in V], [1.5, 0, 0])
A_ = np.array([.2, .2]); B_ = np.array([.5, .5])
assert np.allclose(gradf(A_, P1), [-1.6, -2.6]) and np.isclose(test(A_, P1), -1.76)
assert np.allclose(gradf(B_, P1), [-1, -2]) and np.isclose(test(B_, P1), -0.5) and np.isclose(test(XS, P1), 0)
# kiểm tra bằng lưới: x* đúng là cực tiểu trên C
G = np.array([[a, b] for a in np.linspace(0, 1, 101) for b in np.linspace(0, 1, 101) if a + b <= 1 + 1e-12])
fv = ((G - P1) ** 2).sum(1); assert np.allclose(G[fv.argmin()], XS) and fv.min() >= ((XS - P1) ** 2).sum() - 1e-12
# đỉnh: −∇f(x*) = (2, −2) = 2·(1, 1) + 4·(0, −1) nằm trong nón pháp tuyến
assert np.allclose(-gradf(XV, P2), [2, -2]) and np.allclose(2 * np.array([1, 1]) + 4 * np.array([0, -1]), [2, -2]) and np.isclose(test(XV, P2), 0)
# gradient chiếu
ETA = 0.15; PG = [np.array([0.1, 0.1])]
for _ in range(40): PG.append(PC(PG[-1] - ETA * gradf(PG[-1], P1)))
PG = np.array(PG); KG = int(np.argmax(np.linalg.norm(PG - XS, axis=1) < 1e-3)); assert 10 <= KG <= 30, KG
TG = [test(x, P1) for x in PG]; assert TG[0] < 0 and abs(TG[-1]) < 1e-6
# ví dụ 1 (không ràng buộc) và ví dụ 2 (không lồi) của bài
E1 = np.linalg.eigvalsh(np.array([[2., 1], [1, 4]])); assert np.allclose(E1, [3 - 2 ** .5, 3 + 2 ** .5])
CP = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1)]
Hc = lambda a, b: np.linalg.eigvalsh(np.diag([12 * a * a - 4, 12 * b * b - 4.]))
kind = lambda a, b: "max" if Hc(a, b).max() < 0 else ("min" if Hc(a, b).min() > 0 else "saddle")
KD = [kind(a, b) for a, b in CP]; assert (KD.count("min"), KD.count("max"), KD.count("saddle")) == (4, 1, 4)
for a, b in CP: assert np.allclose([4 * a ** 3 - 4 * a, 4 * b ** 3 - 4 * b], 0)
f2 = lambda x, y: x ** 4 + y ** 4 - 2 * x * x - 2 * y * y; assert f2(1, 1) == -2 and f2(0, 0) == 0 and f2(1, 0) == -1

class Foc(Reel):
    def construct(self):
        self.title(L("Điều kiện tối ưu bậc nhất\ntrên tập lồi", "First-order optimality\non a convex set"))
        ax = plain_axes([-0.4, 2.3], [-1.3, 1.9], 5.4, 6.4, [0, 1.0, 0])
        F1 = lambda x, y: (x - 1) ** 2 + (y - 1.5) ** 2
        # ---- stage 1
        self.stage(1)
        self.readout([("min f(x)  với  x ∈ C" if LANG == "vi" else "min f(x)  subject to  x ∈ C", SUN), ("không ràng buộc: ∇f(x*) = 0" if LANG == "vi" else "unconstrained: ∇f(x*) = 0", WHITE)], size=25)
        self.say(L("Bài 04-03: f lồi, khả vi, cực tiểu trên tập lồi C. Không có ràng buộc thì quen thuộc: x* tối ưu khi và chỉ khi ∇f(x*) = 0.",
                   "Lesson 04-03: f convex and differentiable, minimized over a convex set C. Without constraints it is familiar: x* is optimal if and only if ∇f(x*) = 0."), hold=8.5)
        self.readout([("f = x₁² + x₁x₂ + 2x₂²" , SKY), ("∇f = (2x₁ + x₂; x₁ + 4x₂) = 0  ⇒  x* = (0; 0)" if LANG == "vi" else "∇f = (2x₁ + x₂, x₁ + 4x₂) = 0  ⇒  x* = (0, 0)", WHITE), ("H có trị riêng 3 ± √2 > 0" if LANG == "vi" else "H has eigenvalues 3 ± √2 > 0", MINT)], size=23)
        self.say(L("Ví dụ 1 của bài: giải ∇f = 0 được x* = (0; 0). Hàm lồi nên chỉ cần thế là đủ, không phải kiểm tra gì thêm.",
                   "Example 1 of the lesson: solving ∇f = 0 gives x* = (0, 0). The function is convex, so that alone is enough."), hold=7.5)
        tri = Polygon(*[ax.c2p(*v) for v in V], stroke_color=SKY, stroke_width=3, fill_color=SKY, fill_opacity=0.25)
        cs = contours(ax, F1, [0.25, 0.6, 1.8, 2.6], (-0.4, 2.3, -1.3, 1.9), N=70)
        c0 = contours(ax, F1, [1.125], (-0.4, 2.3, -1.3, 1.9), N=70, color=SUN, width=2.5)
        dp = Dot(ax.c2p(*P1), color=PINK, radius=0.1); lp = Text("p", font=MONO, font_size=24, color=PINK).next_to(dp, RIGHT, buff=0.1)
        lc = Text("C", font=MONO, font_size=28, color=SKY).move_to(ax.c2p(0.25, 0.25))
        self.clear_ro()
        self.play(Create(ax), Create(cs), FadeIn(tri), FadeIn(lc), FadeIn(dp), FadeIn(lp), run_time=1.3)
        self.readout([("f(x) = ‖x − p‖²,  p = (1; 1,5)" if LANG == "vi" else "f(x) = ‖x − p‖²,  p = (1, 1.5)", PINK), ("C = {x ≥ 0, x₁ + x₂ ≤ 1}" , SKY)], size=24)
        self.say(L("Giờ thêm ràng buộc, ví dụ cụ thể: f = ‖x − p‖² với p = (1; 1,5), còn C là tam giác x ≥ 0, x₁ + x₂ ≤ 1. Tâm p nằm ngoài C.",
                   "Now add a constraint, a concrete example: f = ‖x − p‖² with p = (1, 1.5), and C is the triangle x ≥ 0, x₁ + x₂ ≤ 1. The center p is outside C."), hold=9.0)
        dx = Dot(ax.c2p(*XS), color=SUN, radius=0.1); lx = Text("x*", font=MONO, font_size=24, color=SUN).next_to(dx, LEFT, buff=0.12)
        self.play(Create(c0), FadeIn(dx), FadeIn(lx), run_time=0.8)
        self.readout([("x* = (0,25; 0,75),  f(x*) = 1,125" if LANG == "vi" else "x* = (0.25, 0.75),  f(x*) = 1.125", SUN), ("∇f(x*) = (−1,5; −1,5) ≠ 0" if LANG == "vi" else "∇f(x*) = (−1.5, −1.5) ≠ 0", ORANGE)], size=24)
        self.say(L("Đường mức vàng chạm C tại x* = (0,25; 0,75). Nhưng ở đó ∇f = (−1,5; −1,5), khác 0. Vậy cần một điều kiện khác.",
                   "The yellow level curve touches C at x* = (0.25, 0.75). But there ∇f = (−1.5, −1.5), not 0. So we need a different condition."), hold=8.0)
        # ---- stage 2
        self.stage(2)
        ng = Arrow(ax.c2p(*XS), ax.c2p(*(XS + 0.4 * np.array([1, 1]))), buff=0, color=ORANGE, stroke_width=5, max_tip_length_to_length_ratio=0.3)
        lng = Text("−∇f", font=MONO, font_size=22, color=ORANGE).next_to(ng.get_end(), UR, buff=0.05)
        arr = VGroup(*[Arrow(ax.c2p(*XS), ax.c2p(*v), buff=0.08, color=MINT, stroke_width=3.5, max_tip_length_to_length_ratio=0.12) for v in V])
        self.readout(["∇f(x*)ᵀ(y − x*) ≥ 0   ∀ y ∈ C" if LANG == "vi" else "∇f(x*)ᵀ(y − x*) ≥ 0   for all y ∈ C"], color=SUN, size=26)
        self.play(GrowArrow(ng), FadeIn(lng), run_time=0.6)
        self.say(L("Điều kiện bậc nhất: x* tối ưu khi và chỉ khi ∇f(x*)ᵀ(y − x*) ≥ 0 với mọi y trong C.",
                   "First-order condition: x* is optimal if and only if ∇f(x*)ᵀ(y − x*) ≥ 0 for every y in C."), hold=7.0)
        self.play(*[GrowArrow(a) for a in arr], run_time=0.8)
        self.say(L("Nghĩa là: đi từ x* theo bất kỳ hướng khả thi y − x* nào (mũi tên xanh), f không giảm ở bậc nhất. Không còn hướng nào vừa ở trong C vừa đi xuống.",
                   "Meaning: moving from x* in any feasible direction y − x* (green arrows), f does not decrease to first order. No direction stays in C and goes downhill."), hold=9.0)
        hp = Line(ax.c2p(-0.35, 1.35), ax.c2p(1.35, -0.35), color=SUN, stroke_width=2.5)
        self.play(Create(hp), run_time=0.5)
        self.readout([("C ⊂ {y : ∇f(x*)ᵀ(y − x*) ≥ 0}" , SUN), ("−∇f(x*) ∈ N_C(x*): nón pháp tuyến" if LANG == "vi" else "−∇f(x*) ∈ N_C(x*): the normal cone", ORANGE)], size=24)
        self.say(L("Hình học: C nằm trọn trong nửa mặt phẳng có biên là đường vàng qua x*. Nói cách khác, −∇f(x*) chĩa ra ngoài C, nằm trong nón pháp tuyến của C tại x*.",
                   "Geometrically: C lies entirely in a half-plane whose boundary is the yellow line through x*. In other words, −∇f(x*) points out of C, inside the normal cone of C at x*."), hold=9.5)
        self.say(L("Nếu x* nằm bên trong C, mọi hướng đều khả thi, kể cả −∇f. Khi đó điều kiện ép ∇f(x*) = 0: ta lấy lại trường hợp không ràng buộc.",
                   "If x* is inside C, every direction is feasible, including −∇f. Then the condition forces ∇f(x*) = 0: we recover the unconstrained case."), hold=8.5)
        self.play(FadeOut(arr), FadeOut(hp), run_time=0.3)
        # ---- stage 3
        self.stage(3)
        dA = Dot(ax.c2p(*A_), color=WHITE, radius=0.09); dB = Dot(ax.c2p(*B_), color=WHITE, radius=0.09)
        lA = Text("A", font=MONO, font_size=22).next_to(dA, DL, buff=0.05); lB = Text("B", font=MONO, font_size=22).next_to(dB, RIGHT, buff=0.1)
        self.play(FadeIn(dA), FadeIn(dB), FadeIn(lA), FadeIn(lB), run_time=0.4)
        self.readout([("min_y ∇fᵀ(y − x): chỉ cần xét 3 đỉnh" if LANG == "vi" else "min_y ∇fᵀ(y − x): only 3 vertices needed", SUN), ("A (0,2; 0,2):    −1,76  ✗" if LANG == "vi" else "A (0.2, 0.2):    −1.76  ✗", PINK), ("B (0,5; 0,5):    −0,50  ✗" if LANG == "vi" else "B (0.5, 0.5):    −0.50  ✗", PINK), ("x* (0,25; 0,75):  0,00  ✓" if LANG == "vi" else "x* (0.25, 0.75):  0.00  ✓", MINT)], size=22)
        self.say(L("Kiểm tra bằng số. Biểu thức tuyến tính theo y, nên giá trị nhỏ nhất trên tam giác đạt ở một đỉnh: chỉ cần thử ba đỉnh.",
                   "Check with numbers. The expression is linear in y, so its minimum over the triangle is at a vertex: just try the three vertices."), hold=7.5)
        dirB = Arrow(ax.c2p(*B_), ax.c2p(0.05, 0.95), buff=0, color=PINK, stroke_width=4, max_tip_length_to_length_ratio=0.25)
        self.play(GrowArrow(dirB), run_time=0.5)
        self.say(L("A ở trong C mà ∇f ≠ 0: hỏng. B nằm trên cạnh, nhưng đi về đỉnh (0; 1) cho giá trị −0,5 < 0: trượt dọc cạnh vẫn giảm được f. Chỉ x* cho min bằng 0.",
                   "A is inside C with ∇f ≠ 0: fails. B is on the edge, but heading to vertex (0, 1) gives −0.5 < 0: sliding along the edge still lowers f. Only x* gives a minimum of 0."), hold=10.0)
        self.play(FadeOut(dA), FadeOut(dB), FadeOut(lA), FadeOut(lB), FadeOut(dirB), run_time=0.3)
        d = Dot(ax.c2p(*PG[0]), color=MINT, radius=0.08)
        self.add(d)
        def rg(k): self.readout([("gradient chiếu, η = 0,15:  k = %d" % k if LANG == "vi" else "projected gradient, η = 0.15:  k = %d" % k, MINT), ("min_y ∇fᵀ(y − x_k) = %s" % nf(TG[k], 3), WHITE)], size=23)
        pt = trail(self, ax, PG, d, MINT, rt=0.3, ks=range(1, 21), cb=rg, width=3)
        self.say(L("Gradient chiếu: đi theo −∇f rồi chiếu về C. Đại lượng kiểm tra tăng dần về 0 và các điểm dồn về x* sau khoảng %d bước." % KG,
                   "Projected gradient: step along −∇f, then project back onto C. The test value rises to 0 and the iterates settle at x* after about %d steps." % KG), hold=8.0)
        self.play(*[FadeOut(m) for m in (pt, d, c0, cs, dp, lp, dx, lx, ng, lng)], run_time=0.4)
        cs2 = contours(ax, lambda x, y: (x - 2) ** 2 + (y + 1) ** 2, [0.5, 2, 3.5], (-0.4, 2.3, -1.3, 1.9), N=70)
        c2 = contours(ax, lambda x, y: (x - 2) ** 2 + (y + 1) ** 2, [2.0], (-0.4, 2.3, -1.3, 1.9), N=70, color=SUN)
        dp2 = Dot(ax.c2p(*P2), color=PINK, radius=0.1); lp2 = Text("p = (2; −1)" if LANG == "vi" else "p = (2, −1)", font=MONO, font_size=22, color=PINK).next_to(dp2, LEFT, buff=0.12)
        cone = Polygon(ax.c2p(1, 0), ax.c2p(1.9, 0.9), ax.c2p(2.3, 0.9), ax.c2p(2.3, -1.3), ax.c2p(1, -1.3), stroke_width=0, fill_color=SUN, fill_opacity=0.22)
        ng2 = Arrow(ax.c2p(1, 0), ax.c2p(1.4, -0.4), buff=0, color=ORANGE, stroke_width=5, max_tip_length_to_length_ratio=0.3)
        dv = Dot(ax.c2p(1, 0), color=SUN, radius=0.1)
        self.play(FadeIn(cone), Create(cs2), Create(c2), FadeIn(dp2), FadeIn(lp2), FadeIn(dv), GrowArrow(ng2), run_time=1.0)
        self.readout([("p = (2; −1)  ⇒  x* = (1; 0), một đỉnh" if LANG == "vi" else "p = (2, −1)  ⇒  x* = (1, 0), a vertex", SUN), ("−∇f(x*) = (2; −2) = 2·(1; 1) + 4·(0; −1)" if LANG == "vi" else "−∇f(x*) = (2, −2) = 2·(1, 1) + 4·(0, −1)", ORANGE)], size=23)
        self.say(L("Đổi p = (2; −1): nghiệm là đỉnh (1; 0). Tại đỉnh, nón pháp tuyến là cả vùng vàng, sinh bởi hai pháp tuyến (1; 1) và (0; −1). −∇f nằm trong đó: đạt tối ưu.",
                   "Move p to (2, −1): the solution is the vertex (1, 0). At a vertex the normal cone is the whole yellow wedge, spanned by the normals (1, 1) and (0, −1). −∇f lies inside it: optimal."), hold=10.0)
        # ---- stage 4
        self.stage(4); self.wipe()
        ax3 = plain_axes([-1.7, 1.7], [-1.7, 1.7], 6.6, 6.6, [0, 1.0, 0])
        cs3 = contours(ax3, f2, [-1.8, -1.4, -0.9, -0.5, 0.5, 1.5, 3], (-1.7, 1.7, -1.7, 1.7), N=90)
        col = {"min": MINT, "max": ORANGE, "saddle": PINK}
        dots = VGroup(*[Dot(ax3.c2p(a, b), radius=0.11, color=col[k]) for (a, b), k in zip(CP, KD)])
        self.play(Create(ax3), Create(cs3), run_time=1.0); self.play(FadeIn(dots, lag_ratio=0.1), run_time=0.9)
        self.readout([("f = x₁⁴ + x₂⁴ − 2x₁² − 2x₂²:  9 điểm ∇f = 0" if LANG == "vi" else "f = x₁⁴ + x₂⁴ − 2x₁² − 2x₂²:  9 points with ∇f = 0", WHITE), ("4 cực tiểu (f = −2)" if LANG == "vi" else "4 minima (f = −2)", MINT), ("4 điểm yên ngựa (f = −1),  1 cực đại (f = 0)" if LANG == "vi" else "4 saddles (f = −1),  1 maximum (f = 0)", PINK)], size=22)
        self.say(L("Đối chiếu với hàm không lồi, ví dụ 2 của bài: x₁⁴ + x₂⁴ − 2x₁² − 2x₂². Có 9 điểm ∇f = 0, nhưng chỉ 4 điểm xanh là cực tiểu.",
                   "Compare a nonconvex function, example 2 of the lesson: x₁⁴ + x₂⁴ − 2x₁² − 2x₂². It has 9 points with ∇f = 0, but only the 4 green ones are minima."), hold=9.0)
        self.say(L("Gốc tọa độ là cực đại, bốn điểm hồng là yên ngựa. Không có lồi, ∇f = 0 chỉ là điều kiện cần; phải xem thêm Hessian ở điều kiện bậc hai.",
                   "The origin is a maximum, the four pink points are saddles. Without convexity, ∇f = 0 is only necessary; the Hessian must be checked by the second-order conditions."), hold=9.0)
        self.say(L("Ví dụ một biến còn gọn hơn: x³ có đạo hàm 0 tại 0 mà không phải cực tiểu. Chính tính lồi biến điều kiện cần thành điều kiện đủ.",
                   "A one-variable example is even shorter: x³ has zero derivative at 0 but no minimum there. Convexity is what turns the necessary condition into a sufficient one."), hold=8.5)
        self.takeaway([L("Không ràng buộc, f lồi: x* tối ưu ⇔ ∇f(x*) = 0.", "Unconstrained, convex f: x* optimal ⇔ ∇f(x*) = 0."),
                       L("Có tập lồi C: ∇f(x*)ᵀ(y − x*) ≥ 0 với mọi y ∈ C.", "Convex set C: ∇f(x*)ᵀ(y − x*) ≥ 0 for all y ∈ C."),
                       L("Tức −∇f(x*) nằm trong nón pháp tuyến: chĩa ra ngoài C.", "That is, −∇f(x*) lies in the normal cone: it points out of C."),
                       L("Không lồi: điều kiện chỉ còn là cần.", "Nonconvex: the condition is only necessary.")])
