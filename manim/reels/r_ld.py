from rl import *
from o3lib import LA, LB, soft, lasso_star, lasso_f
AT = LA.T
LMAX = np.abs(AT @ LB).max()
def at(l): x = lasso_star(l); u = LB - LA @ x; return x, u
for l in (.3, .8, 1.5, 3.0):
    x, u = at(l); a = np.abs(AT @ u); assert (a <= l + 1e-6).all() and all((abs(x[i]) > 1e-9) == (abs(a[i] - l) < 1e-6) for i in range(2))
assert np.allclose(at(LMAX + 0.1)[0], 0)
# events: smallest λ where x_i = 0 (scan)
LS = np.linspace(LMAX + 0.2, 0.2, 140); TAB = [at(l) for l in LS]
ev = {}
for i in range(2):
    nz = [l for l, (x, u) in zip(LS, TAB) if abs(x[i]) > 1e-7]
    ev[i] = max(nz) if nz else None
def dualD(u): return LB @ u - 0.5 * u @ u
def ista_gap(lam, n):
    Lc = np.linalg.eigvalsh(LA.T @ LA).max(); x = np.zeros(2); out = []
    for k in range(n + 1):
        r = LB - LA @ x; s = min(1.0, lam / max(np.abs(AT @ r).max(), 1e-12)); u = s * r
        out.append((k, x.copy(), lasso_f(x, lam) - dualD(u)))
        x = soft(x + AT @ (LB - LA @ x) / Lc, lam / Lc)
    return out
IG = ista_gap(0.8, 60)
assert all(r[2] >= -1e-12 for r in IG) and IG[-1][2] < 1e-6
xs8 = lasso_star(0.8); assert abs(lasso_f(xs8, 0.8) - dualD(LB - LA @ xs8)) < 1e-9
def clip_poly(poly, box):
    x0, x1, y0, y1 = box
    def clip(pts, inside, inter):
        out = []
        for i in range(len(pts)):
            a, b = pts[i - 1], pts[i]
            if inside(b):
                if not inside(a): out.append(inter(a, b))
                out.append(b)
            elif inside(a): out.append(inter(a, b))
        return out
    pts = [np.array(p, float) for p in poly]
    for k, v, sgn in ((0, x0, 1), (0, x1, -1), (1, y0, 1), (1, y1, -1)):
        ins = lambda p, k=k, v=v, sgn=sgn: sgn * (p[k] - v) >= 0
        def inter(a, b, k=k, v=v): t = (v - a[k]) / (b[k] - a[k]); return a + t * (b - a)
        pts = clip(pts, ins, inter)
        if not pts: break
    return pts
ATI = np.linalg.inv(AT)
def para_(l): return [ATI @ np.array(s) * l for s in ((1, 1), (1, -1), (-1, -1), (-1, 1))]

class LassoDual(Reel):
    def construct(self):
        self.title(L("Đối ngẫu của lasso: chiếu b\nlên một hình bình hành", "The lasso dual: project b\nonto a parallelogram"))
        self.stage(1)
        self.readout(["min ½‖Ax − b‖² + λ‖x‖₁", "A = [[1,6; 0,7], [0,4; 1,1]],  b = (2,1; 0,9)" if LANG == "vi" else "A = [[1.6, 0.7], [0.4, 1.1]],  b = (2.1, 0.9)"], color=WHITE, size=25, y=2.6)
        self.say(L("Lasso với 2 biến. Khi λ đủ lớn, nghiệm là x = 0. Khi λ giảm, các tọa độ lần lượt khác 0. Vì sao?",
                   "A lasso with 2 variables. For large λ the solution is x = 0. As λ shrinks, coordinates switch on one by one. Why?"), hold=5.0)
        # key idea
        self.stage(2)
        self.readout(["max_u  bᵀu − ½‖u‖²", "s.t.   |aᵢᵀu| ≤ λ,  i = 1, 2", "u* = b − Ax*"], color=SUN, size=25, y=2.6)
        self.say(L("Bài toán đối ngẫu: bᵀu − ½‖u‖² = ½‖b‖² − ½‖u − b‖². Nên u* là hình chiếu của b lên tập khả thi.",
                   "The dual: bᵀu − ½‖u‖² = ½‖b‖² − ½‖u − b‖². So u* is the projection of b onto the feasible set."), hold=5.5)
        self.say(L("Tập khả thi |aᵢᵀu| ≤ λ là giao của hai dải: một hình bình hành, co giãn theo λ.", "The feasible set |aᵢᵀu| ≤ λ is the intersection of two strips: a parallelogram that scales with λ."))
        self.clear_ro()
        ax = plain_axes([-2.2, 3.0], [-2.4, 2.4], 7.4, 6.8, [0, 1.15, 0])
        box = (-2.2, 3.0, -2.4, 2.4); Pt = lambda p: ax.c2p(p[0], p[1])
        self.play(Create(ax), run_time=0.4)
        bd = Dot(Pt(LB), radius=0.12, color=ORANGE); bl = Text("b", font=FONT, font_size=26, color=ORANGE).next_to(Pt(LB), UR, buff=0.08)
        self.add(bd, bl)
        lt = ValueTracker(LMAX + 0.3)
        def para_m():
            pts = clip_poly(para_(lt.get_value()), box)
            return Polygon(*[Pt(p) for p in pts], color=SKY, stroke_width=4, fill_color=SKY, fill_opacity=0.15)
        pm = always_redraw(para_m)
        ud = always_redraw(lambda: Dot(Pt(at(lt.get_value())[1]), radius=0.11, color=MINT))
        ul = always_redraw(lambda: DashedLine(Pt(LB), Pt(at(lt.get_value())[1]), color=MINT, stroke_width=3))
        self.play(FadeIn(pm), run_time=0.5); self.add(ul, ud)
        # algorithm / sweep
        self.stage(3)
        def ro():
            l = lt.get_value(); x, u = at(l); a = AT @ u
            return ["λ = %s" % nf(l, 2), ("x* = %s" % vec(x, 3), SUN), "|a₁ᵀu*| = %s   |a₂ᵀu*| = %s" % (nf(abs(a[0]), 2), nf(abs(a[1]), 2))]
        self.readout(ro(), color=WHITE, size=23)
        self.say(L("λ = %s > λ_max = ‖Aᵀb‖∞ = %s: b nằm trong hình, u* = b, nên x* = 0." % (nf(LMAX + 0.3, 2), nf(LMAX, 2)),
                   "λ = %s > λ_max = ‖Aᵀb‖∞ = %s: b is inside, u* = b, so x* = 0." % (nf(LMAX + 0.3, 2), nf(LMAX, 2))), hold=4.5)
        for target, msg in ((ev[0] - 0.25, L("Khi λ < %s, b ra ngoài và chạm cạnh |a₁ᵀu| = λ: x₁ bắt đầu khác 0." % nf(LMAX, 2), "Below λ = %s, b is outside and touches the face |a₁ᵀu| = λ: x₁ switches on." % nf(LMAX, 2))),
                            (ev[1] - 0.25, L("Dưới λ ≈ %s, hình chiếu chạm cả cạnh thứ hai: x₂ cũng khác 0." % nf(ev[1], 2), "Below λ ≈ %s the projection hits the second face too: x₂ switches on as well." % nf(ev[1], 2))),
                            (0.3, L("Cạnh nào bị chạm (|aᵢᵀu*| = λ) thì xᵢ được phép khác 0. Cạnh không chạm thì xᵢ = 0.", "A face that is touched (|aᵢᵀu*| = λ) lets xᵢ be nonzero. An untouched face forces xᵢ = 0."))):
            n = 18
            for v in np.linspace(lt.get_value(), target, n)[1:]:
                self.play(lt.animate.set_value(v), run_time=0.22, rate_func=linear); self.readout(ro(), color=WHITE, size=23)
            self.say(msg, hold=4.5)
        # contrast: gap certificate
        self.stage(4); self.play(lt.animate.set_value(0.8), run_time=1.0); self.readout(ro(), color=WHITE, size=23)
        self.say(L("Đối ngẫu cũng là chứng nhận. Chạy ISTA ở λ = 0,8; mỗi bước co r = b − Ax vào hình để có u khả thi.",
                   "The dual is also a certificate. Run ISTA at λ = 0.8; each step scales r = b − Ax into the set to get a feasible u."), hold=5.0)
        rows = [("  k    x                    P(x) − D(u)", WHITE)]
        for k in (0, 1, 2, 3, 5, 10, 20, 40, 60):
            r = IG[k]; rows.append(("%3d   %-19s  %s" % (k, vec(r[1], 3), sci(max(r[2], 1e-16))), SUN))
            if len(rows) > 6: rows = [rows[0]] + rows[-5:]
            self.readout(rows, size=21); self.wait(0.6)
        self.say(L("Khoảng cách P − D ≥ 0 luôn chặn trên sai số thật; khi nó < 10⁻⁶ ta biết chắc đã gần tối ưu.",
                   "The gap P − D ≥ 0 always bounds the true error; once it is below 10⁻⁶ we know we are near optimal."), hold=5.0)
        self.takeaway([L("Đối ngẫu lasso: chiếu b lên {u : ‖Aᵀu‖∞ ≤ λ}, u* = b − Ax*.", "Lasso dual: project b onto {u : ‖Aᵀu‖∞ ≤ λ}, u* = b − Ax*."),
                       L("xᵢ ≠ 0 chỉ khi ràng buộc |aᵢᵀu*| ≤ λ chặt; λ ≥ ‖Aᵀb‖∞ thì x* = 0.", "xᵢ ≠ 0 only if |aᵢᵀu*| ≤ λ is tight; λ ≥ ‖Aᵀb‖∞ gives x* = 0."),
                       L("Mọi u khả thi cho cận dưới: khoảng cách P − D là tiêu chí dừng.", "Any feasible u gives a lower bound: the gap P − D is a stopping rule.")])
