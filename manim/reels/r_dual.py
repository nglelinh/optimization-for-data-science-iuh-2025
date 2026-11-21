from rl import *
f = lambda x: (x - 2) ** 2
g = lambda l: 1.5 * l - l * l / 4
xl = lambda l: 2 - l / 2
xs = np.linspace(-3, 6, 90001)
for l in (0, 1, 3, 5): assert abs(((xs - 2) ** 2 + l * (xs - .5)).min() - g(l)) < 1e-6
PS = 2.25; assert abs(g(3) - PS) < 1e-12
def ascent(a, n):
    l = 0.0; out = [l]
    for _ in range(n): l = max(0.0, l + a * (xl(l) - 0.5)); out.append(l)
    return out
DA = ascent(1.0, 12); assert abs(DA[-1] - 3) < 1e-3
DB = ascent(4.5, 8); assert abs(DB[-1] - 3) > 1
# nonconvex
h = lambda x: x ** 4 - 2 * x ** 2 + 0.5 * x
XG = np.linspace(-3, 3, 60001); HX = h(XG)
PN = HX[XG >= 0].min(); XPN = XG[XG >= 0][HX[XG >= 0].argmin()]
LM = np.linspace(0, 6, 3001); GN = np.array([(HX - l * XG).min() for l in LM]); DN = GN.max(); LN = LM[GN.argmax()]
assert abs(DN + 1) < 1e-6 and abs(LN - 0.5) < 1e-6 and PN - DN > 0.45

class Dual(Reel):
    def construct(self):
        self.title(L("Hàm đối ngẫu luôn là\nmột cận dưới", "The dual function is\nalways a lower bound"))
        self.stage(1)
        ax = plain_axes([-1, 4.5], [-1, 7], 7.6, 3.4, [0, 2.75, 0], ticks=True)
        F_ = ax.plot(f, x_range=[-0.64, 4.5], color=SKY, stroke_width=5)
        feas = Rectangle(width=ax.c2p(0.5, 0)[0] - ax.c2p(-1, 0)[0], height=3.4, stroke_width=0, fill_color=MINT, fill_opacity=0.12).move_to([(ax.c2p(0.5, 0)[0] + ax.c2p(-1, 0)[0]) / 2, 2.75, 0])
        self.play(Create(ax), FadeIn(feas), Create(F_), run_time=1.0)
        ps = Dot(ax.c2p(0.5, PS), radius=0.12, color=MINT); self.add(ps)
        self.say(L("Cực tiểu (x − 2)² với ràng buộc x ≤ 0,5 (vùng xanh). Đáp số: x = 0,5, p* = 2,25.", "Minimize (x − 2)² subject to x ≤ 0.5 (green region). Answer: x = 0.5, p* = 2.25."))
        # key idea
        self.stage(2)
        self.readout(["L(x, λ) = (x − 2)² + λ(x − 0,5),  λ ≥ 0" if LANG == "vi" else "L(x, λ) = (x − 2)² + λ(x − 0.5),  λ ≥ 0", "g(λ) = minₓ L(x, λ) = 1,5λ − λ²/4" if LANG == "vi" else "g(λ) = minₓ L(x, λ) = 1.5λ − λ²/4"], color=SUN, size=23, y=0.35)
        self.say(L("Lagrangian: cộng ràng buộc vào mục tiêu với giá λ ≥ 0. Trên vùng khả thi, x − 0,5 ≤ 0 nên L ≤ f.",
                   "The Lagrangian adds the constraint to the objective at a price λ ≥ 0. On the feasible set x − 0.5 ≤ 0, so L ≤ f."), hold=5.0)
        gx = plain_axes([0, 6], [-1, 3], 6.6, 2.4, [0, -2.0, 0], ticks=True)
        lt = ValueTracker(0.0)
        def Lcurve():
            l = lt.get_value(); xx = [x for x in np.linspace(-1, 4.5, 300) if -1 <= f(x) + l * (x - 0.5) <= 7]
            return VMobject(color=SUN, stroke_width=4).set_points_smoothly([ax.c2p(x, f(x) + l * (x - 0.5)) for x in xx])
        Lc = always_redraw(Lcurve)
        md = always_redraw(lambda: Dot(ax.c2p(xl(lt.get_value()), g(lt.get_value())), radius=0.1, color=SUN))
        pl = DashedLine(gx.c2p(0, PS), gx.c2p(6, PS), color=MINT, stroke_width=3)
        self.play(Create(gx), Create(pl), run_time=0.5); self.add(Lc, md)
        tr_ = TracedPath(lambda: gx.c2p(lt.get_value(), g(lt.get_value())), stroke_color=SUN, stroke_width=6); gd = always_redraw(lambda: Dot(gx.c2p(lt.get_value(), g(lt.get_value())), radius=0.1, color=SUN))
        self.add(tr_, gd)
        self.say(L("Quét λ: với mỗi λ, đáy của L (chấm vàng) cho g(λ), vẽ ở dưới. Đường xanh đứt là p* = 2,25.",
                   "Sweep λ: for each λ the bottom of L (yellow dot) gives g(λ), plotted below. The dashed green line is p* = 2.25."), wait=False)
        self.play(lt.animate.set_value(6), run_time=7, rate_func=linear)
        self.play(lt.animate.set_value(3), run_time=1.5)
        self.say(L("g(λ) không bao giờ vượt p*: mọi λ ≥ 0 đều cho một cận dưới. Cận tốt nhất: λ* = 3, g = 2,25 = p*.",
                   "g(λ) never exceeds p*: every λ ≥ 0 gives a lower bound. The best one: λ* = 3, g = 2.25 = p*."), hold=5.0)
        # algorithm
        self.stage(3)
        self.say(L("Tìm λ* bằng đi lên đối ngẫu: λ ← max(0, λ + α(x(λ) − 0,5)), với x(λ) = 2 − λ/2 là nghiệm của bài con.",
                   "Find λ* by dual ascent: λ ← max(0, λ + α(x(λ) − 0.5)), where x(λ) = 2 − λ/2 solves the inner problem."), hold=5.0)
        self.play(lt.animate.set_value(0), run_time=0.8); self.clear_ro()
        rows = [("  k    λ        x(λ)      g(λ)", WHITE)]
        for k in range(0, 9):
            l = DA[k]; self.play(lt.animate.set_value(l), run_time=0.5)
            rows.append(("%3d   %-7s  %-8s  %s" % (k, nf(l, 4), nf(xl(l), 4), nf(g(l), 5)), SUN if k < 8 else MINT))
            if len(rows) > 4: rows = [rows[0]] + rows[-3:]
            self.readout(rows, size=21, y=0.15); self.wait(0.4)
        self.say(L("Với α = 1, khoảng cách tới λ* giảm một nửa mỗi bước; x(λ) tiến về 0,5 và g tiến về p*.",
                   "With α = 1 the distance to λ* halves every step; x(λ) moves to 0.5 and g climbs to p*."), hold=4.5)
        # contrast
        self.stage(4); self.wipe()
        ax3 = plain_axes([-1.8, 1.8], [-1.8, 2.2], 7.4, 4.6, [0, 2.2, 0], ticks=True)
        H = ax3.plot(h, x_range=[-1.62, 1.68], color=PINK, stroke_width=5)
        feas = Rectangle(width=ax3.c2p(1.8, 0)[0] - ax3.c2p(0, 0)[0], height=4.6, stroke_width=0, fill_color=MINT, fill_opacity=0.12).move_to([(ax3.c2p(1.8, 0)[0] + ax3.c2p(0, 0)[0]) / 2, 2.2, 0])
        self.play(Create(ax3), FadeIn(feas), Create(H), run_time=1.0)
        self.say(L("Bài toán KHÔNG lồi: cực tiểu x⁴ − 2x² + 0,5x với x ≥ 0. Hai hố, hố sâu hơn nằm ngoài vùng khả thi.",
                   "A NONCONVEX problem: minimize x⁴ − 2x² + 0.5x with x ≥ 0. Two wells; the deeper one is infeasible."), hold=5.0)
        self.play(FadeIn(Dot(ax3.c2p(XPN, PN), radius=0.12, color=MINT)), run_time=0.3)
        self.readout(["p* = %s  (x = %s)" % (nf(PN, 3), nf(XPN, 3)), ("d* = max g(λ) = %s  (λ = %s)" % (nf(DN, 3), nf(LN, 2)), PINK), ("khoảng cách đối ngẫu = %s" % nf(PN - DN, 3) if LANG == "vi" else "duality gap = %s" % nf(PN - DN, 3), ORANGE)], color=MINT, size=24, y=-1.6)
        self.say(L("Đối ngẫu vẫn cho cận dưới (−1 ≤ %s), nhưng không chạm tới p*: khoảng cách %s." % (nf(PN, 3), nf(PN - DN, 3)),
                   "The dual still gives a lower bound (−1 ≤ %s), but it cannot reach p*: a gap of %s." % (nf(PN, 3), nf(PN - DN, 3))), hold=5.0)
        self.takeaway([L("Đối ngẫu yếu: g(λ) ≤ p* với mọi λ ≥ 0, bài toán nào cũng vậy.", "Weak duality: g(λ) ≤ p* for every λ ≥ 0, for any problem."),
                       L("Bài toán lồi (có Slater): max g = p*, đối ngẫu mạnh.", "Convex (with Slater): max g = p*, strong duality."),
                       L("Không lồi: có thể còn khoảng cách đối ngẫu.", "Nonconvex: a duality gap may remain.")])
