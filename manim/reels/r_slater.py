from rl import *
# Lồi, Slater đúng: min x² + 1 s.t. h(x) = 2 − x ≤ 0  →  g(λ) = 1 + 2λ − λ²/4
f = lambda x: x * x + 1; g = lambda l: 1 + 2 * l - l * l / 4
XG = np.linspace(-6, 10, 160001)
for l in (0, 1, 2, 3, 4, 6): assert abs((f(XG) + l * (2 - XG)).min() - g(l)) < 1e-6
PS = f(2.0); LS = 4.0; assert PS == 5 and g(LS) == 5 and abs(np.linspace(0, 8, 8001)[np.argmax(g(np.linspace(0, 8, 8001)))] - 4) < 1e-9
LG = np.linspace(0, 8, 801); assert (g(LG) <= PS + 1e-12).all()
XF, LF = 2.5, 3.0; GAP = f(XF) - g(LF); assert abs(f(XF) - 7.25) < 1e-12 and abs(g(LF) - 4.75) < 1e-12 and abs(GAP - 2.5) < 1e-12 and f(XF) - PS <= GAP
assert 2 - 3.0 < 0  # x = 3 khả thi nghiêm ngặt (Slater)
# Slater sai: min e^(−x) s.t. x²/y ≤ 0, y > 0  →  p* = 1, g(λ) = 0
def g2(l):
    xs = np.linspace(0, 60, 6001); ys = np.maximum(xs, 1e-9) ** 3
    return (np.exp(-xs) + l * xs ** 2 / ys)[1:].min()
for l in (0.5, 1, 5): assert 0 <= g2(l) < 0.1
G2 = [g2(l) for l in (0.5, 1, 5)]
# inf thực sự là 0: e^(−x) + λ/x → 0 khi x → ∞ (với y = x³)
assert np.exp(-200) + 5 / 200 < 0.03 and np.exp(-2000) + 5 / 2000 < 0.003

class Slater(Reel):
    def construct(self):
        self.title(L("Đối ngẫu mạnh và Slater:\nkhi nào khoảng cách bằng 0?", "Strong duality and Slater:\nwhen is the gap zero?"))
        self.stage(1)
        ax = plain_axes([-1, 4], [0, 10.5], 7.2, 4.6, [0.2, 1.9, 0])
        cf = ax.plot(f, x_range=[-1, 3.08], color=SKY, stroke_width=4)
        feas = Rectangle(width=ax.c2p(4, 0)[0] - ax.c2p(2, 0)[0], height=4.6, fill_color=MINT, fill_opacity=0.1, stroke_width=0).move_to([(ax.c2p(4, 0)[0] + ax.c2p(2, 0)[0]) / 2, 1.9, 0])
        self.play(Create(ax), FadeIn(feas), Create(cf), run_time=0.8)
        pd = Dot(ax.c2p(2, 5), radius=0.11, color=MINT); pl = Text("p* = 5", font=MONO, font_size=22, color=MINT).next_to(pd, RIGHT, buff=0.15)
        self.play(FadeIn(pd), FadeIn(pl), run_time=0.4)
        self.say(L("Bài toán gốc lồi: min x² + 1 với ràng buộc h(x) = 2 − x ≤ 0, tức x ≥ 2 (vùng xanh). Nghiệm x* = 2, p* = 5.",
                   "A convex primal: min x² + 1 subject to h(x) = 2 − x ≤ 0, i.e. x ≥ 2 (green region). Solution x* = 2, p* = 5."), hold=6.5)
        self.readout(["L(x, λ) = x² + 1 + λ(2 − x)", "g(λ) = min L = 1 + 2λ − λ²/4" if LANG == "vi" else "g(λ) = min over x of L = 1 + 2λ − λ²/4"], color=SUN, size=24)
        self.say(L("Lagrangian cộng ràng buộc vào mục tiêu với nhân tử λ ≥ 0. Hàm đối ngẫu g(λ) là giá trị nhỏ nhất của L theo x (đạt tại x = λ/2).",
                   "The Lagrangian adds the constraint to the objective with a multiplier λ ≥ 0. The dual function g(λ) is the minimum of L over x (attained at x = λ/2)."), hold=7.5)
        # ---- stage 2
        self.stage(2); self.wipe()
        gx = plain_axes([0, 8], [0, 6], 7.0, 4.4, [0.2, 1.9, 0])
        gl = VGroup(*[Text(str(v), font=MONO, font_size=18, color=DIM).next_to(gx.c2p(v, 0), DOWN, buff=0.1) for v in (2, 4, 6, 8)], Text("λ", font=FONT, font_size=22, color=DIM).next_to(gx.c2p(8, 0), UR, buff=0.05))
        pline = DashedLine(gx.c2p(0, 5), gx.c2p(8, 5), color=MINT, stroke_width=3); plab = Text("p* = 5", font=MONO, font_size=20, color=MINT).next_to(gx.c2p(0, 5), UP, buff=0.08).shift(RIGHT * 0.6)
        self.play(Create(gx), FadeIn(gl), Create(pline), FadeIn(plab), run_time=0.7)
        gc = gx.plot(lambda l: max(g(l), 0), x_range=[0, 8], color=SUN, stroke_width=4)
        self.play(Create(gc), run_time=1.5)
        self.readout([("g(0) = %s   g(2) = %s   g(4) = %s   g(6) = %s" % (nf(g(0), 0), nf(g(2), 0), nf(g(4), 0), nf(g(6), 0)), SUN)], size=23)
        self.say(L("Đồ thị g(λ) (vàng) luôn nằm dưới p* = 5: đối ngẫu yếu. Lý do: với x khả thi và λ ≥ 0 thì λ·h(x) ≤ 0, nên L(x, λ) ≤ f(x).",
                   "The graph of g(λ) (yellow) always stays below p* = 5: weak duality. Reason: for feasible x and λ ≥ 0, λ·h(x) ≤ 0, so L(x, λ) ≤ f(x)."), hold=8.0)
        self.say(L("g(λ) luôn lõm vì nó là min của các hàm tuyến tính theo λ. Nên bài max g(λ) luôn là bài lồi, kể cả khi bài gốc không lồi.",
                   "g(λ) is always concave, since it is a minimum of functions that are linear in λ. So max g(λ) is always a convex problem, even when the primal is not."), hold=6.5)
        dd = Dot(gx.c2p(4, 5), radius=0.11, color=ORANGE); self.play(FadeIn(dd, scale=1.5), run_time=0.4)
        self.say(L("Cận dưới tốt nhất: d* = max g(λ) = g(4) = 5 = p*. Khoảng cách đối ngẫu p* − d* = 0. Đó là đối ngẫu mạnh.",
                   "The best lower bound: d* = max g(λ) = g(4) = 5 = p*. The duality gap p* − d* = 0. That is strong duality."), hold=7.0)
        # certificate
        self.readout([("x = 2,5 khả thi:  f(x) = %s" % nf(f(XF), 2) if LANG == "vi" else "x = 2.5 feasible:  f(x) = %s" % nf(f(XF), 2), SKY), ("λ = 3:            g(λ) = %s" % nf(g(LF), 2), SUN), ("khoảng cách f(x) − g(λ) = %s" % nf(GAP, 2) if LANG == "vi" else "gap f(x) − g(λ) = %s" % nf(GAP, 2), PINK), ("⇒ f(x) − p* ≤ %s   (thật ra = %s)" % (nf(GAP, 2), nf(f(XF) - PS, 2)) if LANG == "vi" else "⇒ f(x) − p* ≤ %s   (actually %s)" % (nf(GAP, 2), nf(f(XF) - PS, 2)), WHITE)], size=22)
        self.say(L("Bài 11-05: một cặp khả thi bất kỳ cho chứng chỉ. x = 2,5 và λ = 3 cho f − g = 2,5, nên x cách tối ưu không quá 2,5 (thật ra 2,25). Thuật toán dùng điều này làm tiêu chí dừng.",
                   "Lesson 11-05: any feasible pair gives a certificate. x = 2.5 and λ = 3 give f − g = 2.5, so x is within 2.5 of optimal (actually 2.25). Algorithms use this as a stopping rule."), hold=9.0)
        # ---- stage 3
        self.stage(3); self.wipe()
        ux = plain_axes([-1.2, 1.8], [0, 10.5], 6.6, 5.2, [0.3, 1.6, 0])
        tax = DashedLine(ux.c2p(0, 0), ux.c2p(0, 10.5), color=DIM, stroke_width=2)
        ul = VGroup(Text("u = h(x)", font=MONO, font_size=20, color=DIM).next_to(ux.c2p(1.8, 0), UP, buff=0.1).shift(LEFT * 0.6), Text("t = f(x)", font=MONO, font_size=20, color=DIM).next_to(ux.c2p(-1.2, 10.5), RIGHT, buff=0.1))
        Gc = ParametricFunction(lambda s_: ux.c2p(2 - s_, f(s_)), t_range=[0.4, 3.0], color=SKY, stroke_width=5)
        self.play(Create(ux), Create(tax), FadeIn(ul), run_time=0.6); self.play(Create(Gc), run_time=1.0)
        self.say(L("Một hình nhìn rõ hơn: vẽ mọi cặp (u, t) = (h(x), f(x)) khi x chạy. Ta được đường cong xanh G.",
                   "A clearer picture: plot every pair (u, t) = (h(x), f(x)) as x varies. That gives the blue curve G."), hold=5.5)
        self.say(L("Khả thi nghĩa là u ≤ 0 (bên trái trục dọc). p* là điểm thấp nhất của G bên trái trục: (0; 5).",
                   "Feasible means u ≤ 0 (left of the vertical axis). p* is the lowest point of G on that side: (0, 5)."), hold=5.5)
        self.add(Dot(ux.c2p(0, 5), radius=0.1, color=MINT))
        self.say(L("Với mỗi λ, g(λ) = min (t + λu) trên G. Hình học: đường thẳng dốc −λ tì sát dưới G, và g(λ) là chỗ nó cắt trục t.",
                   "For each λ, g(λ) = min of (t + λu) over G. Geometrically: a line of slope −λ resting under G, and g(λ) is where it crosses the t-axis."), hold=7.5)
        ln = None
        for lam, col in ((1, DIM), (2, PINK), (6, PINK), (4, SUN)):
            gg = g(lam)
            u0 = max(-1.2, (gg - 10.5) / lam); u1 = min(1.8, gg / lam)
            new = VGroup(Line(ux.c2p(u0, gg - u0 * lam), ux.c2p(u1, gg - u1 * lam), color=col, stroke_width=3), Dot(ux.c2p(0, gg), radius=0.09, color=col))
            if ln is None: self.play(Create(new), run_time=0.8)
            else: self.play(FadeOut(ln), Create(new), run_time=0.8)
            ln = new
            self.readout([("λ = %d:  đường t = %s − %d·u,  g(λ) = %s" % (lam, nf(gg, 2), lam, nf(gg, 2)) if LANG == "vi" else "λ = %d:  line t = %s − %d·u,  g(λ) = %s" % (lam, nf(gg, 2), lam, nf(gg, 2)), col if col is not DIM else WHITE)], size=22)
            if lam == 1:
                self.say(L("λ = 1: đường tì dưới G cắt trục t ở %s, thấp hơn p* = 5 khá xa." % nf(gg, 2), "λ = 1: the line under G crosses the t-axis at %s, well below p* = 5." % nf(gg, 2)), hold=4.0)
            elif lam == 2:
                self.say(L("λ = 2: dốc hơn, cắt trục ở %s. Vẫn còn khe hở." % nf(gg, 2), "λ = 2: steeper, crossing at %s. Still a gap." % nf(gg, 2)), hold=3.6)
            elif lam == 6:
                self.say(L("λ = 6: dốc quá, cắt trục ở %s. Lại thấp xuống." % nf(gg, 2), "λ = 6: too steep, crossing at %s. Lower again." % nf(gg, 2)), hold=3.6)
            else:
                self.wait(1.0)
        self.say(L("λ = 4: đường tì đúng vào điểm (0; 5), cắt trục t ở 5 = p*. Không còn khe hở: đối ngẫu mạnh.",
                   "λ = 4: the line rests exactly on (0, 5) and crosses the t-axis at 5 = p*. No gap left: strong duality."), hold=6.0)
        sd = Dot(ux.c2p(2 - 3, f(3)), radius=0.11, color=MINT); self.play(FadeIn(sd, scale=1.4), run_time=0.4)
        self.say(L("Điều kiện Slater (bài 11-04): bài lồi và có x khả thi nghiêm ngặt, ví dụ x = 3 cho h = −1 < 0. Khi đó G có điểm hẳn bên trái trục, và đối ngẫu mạnh được bảo đảm.",
                   "Slater's condition (lesson 11-04): a convex problem with a strictly feasible x, e.g. x = 3 gives h = −1 < 0. Then G has points strictly left of the axis, and strong duality is guaranteed."), hold=9.0)
        # ---- stage 4
        self.stage(4); self.wipe()
        vx = plain_axes([-0.6, 3], [0, 2.6], 6.6, 3.8, [0.3, 1.45, 0])
        vax = DashedLine(vx.c2p(0, 0), vx.c2p(0, 2.6), color=DIM, stroke_width=2)
        quad = Rectangle(width=vx.c2p(3, 0)[0] - vx.c2p(0, 0)[0], height=vx.c2p(0, 2.6)[1] - vx.c2p(0, 0)[1], fill_color=SKY, fill_opacity=0.25, stroke_width=0).move_to([(vx.c2p(3, 0)[0] + vx.c2p(0, 0)[0]) / 2, (vx.c2p(0, 2.6)[1] + vx.c2p(0, 0)[1]) / 2, 0])
        self.play(Create(vx), Create(vax), run_time=0.5)
        prob = VGroup(Text("min  e⁻ˣ", font=MONO, font_size=24, color=WHITE), Text("với  x²/y ≤ 0,  y > 0" if LANG == "vi" else "s.t. x²/y ≤ 0,  y > 0", font=MONO, font_size=24, color=WHITE)).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to([0, -1.35, 0])
        self.play(FadeIn(prob), run_time=0.4)
        self.say(L("Một bài lồi mà Slater sai: min e⁻ˣ với x²/y ≤ 0, y > 0. Hàm x²/y lồi khi y > 0.",
                   "A convex problem where Slater fails: min e⁻ˣ subject to x²/y ≤ 0, y > 0. The function x²/y is convex for y > 0."), hold=6.0)
        self.say(L("x²/y ≤ 0 chỉ xảy ra khi x = 0. Không có điểm nào cho x²/y < 0: không có điểm khả thi nghiêm ngặt. Và p* = e⁰ = 1.",
                   "x²/y ≤ 0 only when x = 0. No point gives x²/y < 0: there is no strictly feasible point. And p* = e⁰ = 1."), hold=6.5)
        p1 = Dot(vx.c2p(0, 1), radius=0.12, color=MINT); p1l = Text("(0; 1)" if LANG == "vi" else "(0, 1)", font=MONO, font_size=20, color=MINT).next_to(p1, LEFT, buff=0.12)
        self.play(FadeIn(quad), FadeIn(p1), FadeIn(p1l), run_time=0.7)
        self.say(L("Tập G ở đây: điểm (0; 1) từ x = 0, cộng cả góc phần tư u > 0, t > 0 (x ≠ 0). G không có điểm nào bên trái trục.",
                   "The set G here: the point (0, 1) from x = 0, plus the whole quadrant u > 0, t > 0 (x ≠ 0). G has no point left of the axis."), hold=7.0)
        sl = Line(vx.c2p(-0.6, 0.3), vx.c2p(0.45, -0.225), color=PINK, stroke_width=4)
        self.play(Create(sl), FadeIn(Dot(vx.c2p(0, 0), radius=0.1, color=PINK)), run_time=0.6)
        self.readout([("g(λ) = inf (e⁻ˣ + λ·x²/y) = 0  với mọi λ ≥ 0" if LANG == "vi" else "g(λ) = inf (e⁻ˣ + λ·x²/y) = 0  for every λ ≥ 0", PINK), ("(chọn y = x³, x → ∞: e⁻ˣ + λ/x → 0)" if LANG == "vi" else "(take y = x³, x → ∞: e⁻ˣ + λ/x → 0)", DIM), ("d* = 0,  p* = 1,  khoảng cách = 1" if LANG == "vi" else "d* = 0,  p* = 1,  gap = 1", WHITE)], size=22)
        self.say(L("Đường tì dưới G nào cũng phải đi qua gốc (góc phần tư sát tới 0), nên g(λ) = 0 với mọi λ. d* = 0 < p* = 1: khoảng cách đối ngẫu bằng 1, dù bài toán lồi.",
                   "Every line resting under G must pass through the origin (the quadrant reaches toward 0), so g(λ) = 0 for every λ. d* = 0 < p* = 1: a duality gap of 1, even though the problem is convex."), hold=9.0)
        self.say(L("Lồi thôi chưa đủ. Slater (hoặc ràng buộc affine, như bài SVM ở 11-04) là thứ bảo đảm khoảng cách bằng 0.",
                   "Convexity alone is not enough. Slater (or affine constraints, as in the SVM example of 11-04) is what guarantees a zero gap."), hold=6.0)
        self.takeaway([L("Đối ngẫu yếu: g(λ) ≤ p* với mọi λ ≥ 0, luôn đúng.", "Weak duality: g(λ) ≤ p* for every λ ≥ 0, always."),
                       L("Một cặp khả thi (x, λ) cho chứng chỉ: f(x) − p* ≤ f(x) − g(λ).", "A feasible pair (x, λ) gives a certificate: f(x) − p* ≤ f(x) − g(λ)."),
                       L("Bài lồi + có điểm khả thi nghiêm ngặt (Slater) ⇒ d* = p*.", "Convex + a strictly feasible point (Slater) ⇒ d* = p*."),
                       L("Không có Slater, bài lồi vẫn có thể có khoảng cách: e⁻ˣ, x²/y ≤ 0 cho p* = 1, d* = 0.", "Without Slater a convex problem can still have a gap: e⁻ˣ, x²/y ≤ 0 gives p* = 1, d* = 0.")])
