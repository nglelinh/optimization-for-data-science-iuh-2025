from rl import *
LAM = 1.0
soft = lambda v, t=LAM: np.sign(v) * np.maximum(np.abs(v) - t, 0.0)
for y in (-2.4, -0.7, 0.3, 1.0, 1.8):
    xs = np.linspace(-4, 4, 80001); assert abs(xs[np.argmin(0.5 * (xs - y) ** 2 + LAM * np.abs(xs))] - soft(y)) < 2e-4
YV = np.array([2.3, -0.4, 0.9, -1.7, 0.2, 1.2]); PV = soft(YV)
assert np.allclose(PV, [1.3, 0, 0, -0.7, 0, 0.2])
A = np.array([[2, 0.5], [0.5, 1.0]]); b = np.array([2.0, 0.3]); lam = 0.6
F = lambda x: 0.5 * np.sum((A @ x - b) ** 2) + lam * np.abs(x).sum()
Lc = np.linalg.eigvalsh(A.T @ A).max()
def ista(n):
    x = np.array([-0.6, 1.4]); out = [x.copy()]
    for _ in range(n): x = soft(x - A.T @ (A @ x - b) / Lc, lam / Lc); out.append(x.copy())
    return out
IS = ista(400); XST = IS[-1]; FST = F(XST)
assert XST[1] == 0.0 and abs(XST[0] - 0.835294) < 1e-5 and abs((A.T @ (b - A @ XST))[1]) < lam - 0.5
KZ = next(k for k in range(len(IS)) if all(IS[j][1] == 0.0 for j in range(k, len(IS))))
def subg(n):
    x = np.array([-0.6, 1.4]); out = [x.copy()]
    for k in range(n):
        gr = A.T @ (A @ x - b) + lam * np.sign(x); x = x - 0.5 / Lc / np.sqrt(k + 1) * gr; out.append(x.copy())
    return out
SG = subg(400)
assert all(SG[k][1] != 0 for k in range(100, 401)) and abs(SG[-1][1]) > 1e-4 and F(SG[-1]) - FST > 1e-6

class Prox(Reel):
    def construct(self):
        self.title(L("Co ngưỡng mềm: prox của λ|x|\nvà vì sao lasso cho số 0 thật", "Soft-thresholding: the prox of λ|x|\nand why lasso gives exact zeros"))
        self.stage(1)
        ax = plain_axes([-3.2, 3.2], [0, 5], 7.6, 2.9, [0, 2.95, 0], ticks=False)
        bx = plain_axes([-3, 3], [-2.2, 2.2], 5.2, 3.0, [0, -1.0, 0], ticks=False)
        yt = ValueTracker(1.8)
        phi = lambda x, y: 0.5 * (x - y) ** 2 + LAM * abs(x)
        curve = always_redraw(lambda: ax.plot(lambda x: min(phi(x, yt.get_value()), 5), x_range=[-3.2, 3.2, 0.02], color=SKY, stroke_width=5))
        mdot = always_redraw(lambda: Dot(ax.c2p(soft(yt.get_value()), phi(soft(yt.get_value()), yt.get_value())), radius=0.12, color=SUN))
        self.play(Create(ax), run_time=0.4); self.add(curve, mdot)
        self.say(L("prox(y) = argminₓ ½(x − y)² + λ|x|, λ = 1: ở gần y, nhưng bị phạt vì khác 0.",
                   "prox(y) = argminₓ ½(x − y)² + λ|x|, λ = 1: stay close to y, but pay for being nonzero."), hold=4.5)
        lab = always_redraw(lambda: Text("y = %s  →  prox = %s" % (nf(yt.get_value(), 2), nf(soft(yt.get_value()), 2)), font=MONO, font_size=24, color=SUN).move_to([0, 1.2, 0]))
        self.add(lab); self.wait(1.5)
        self.say(L("Với y = 1,8 cực tiểu nằm ở 0,8: kéo về 0 đúng một đoạn λ.", "For y = 1.8 the minimizer is 0.8: pulled toward 0 by exactly λ."))
        # key idea
        self.stage(2)
        self.play(Create(bx), run_time=0.4)
        trace = TracedPath(lambda: bx.c2p(yt.get_value(), soft(yt.get_value())), stroke_color=SUN, stroke_width=6)
        tdot = always_redraw(lambda: Dot(bx.c2p(yt.get_value(), soft(yt.get_value())), radius=0.09, color=SUN))
        self.add(trace, tdot)
        self.say(L("Quét y từ 2,8 xuống −2,8 và vẽ prox(y) bên dưới.", "Sweep y from 2.8 down to −2.8 and draw prox(y) below."), wait=False)
        self.play(yt.animate.set_value(2.8), run_time=0.8); self.play(yt.animate.set_value(-2.8), run_time=6.0, rate_func=linear)
        dz = Rectangle(width=bx.c2p(1, 0)[0] - bx.c2p(-1, 0)[0], height=0.5, stroke_width=0, fill_color=PINK, fill_opacity=0.35).move_to(bx.c2p(0, 0))
        self.play(FadeIn(dz), run_time=0.4)
        self.readout(["prox(y) = sign(y)·max(|y| − λ, 0)"], color=SUN, size=24, y=-3.25)
        self.say(L("Cả đoạn |y| ≤ λ (vùng hồng) bị ép về ĐÚNG 0. Ngoài đoạn đó, y bị co về 0 một lượng λ.",
                   "The whole interval |y| ≤ λ (pink) is mapped to EXACTLY 0. Outside it, y is shrunk toward 0 by λ."), hold=5.0)
        self.wipe(); 
        bars = plain_axes([0, 6.6], [-2.6, 2.6], 7.2, 5.0, [0, 1.6, 0])
        self.play(Create(bars), run_time=0.3)
        def bar(i, v, col, w=0.42, dx=0):
            return Rectangle(width=w, height=max(abs(v) * 5.0 / 5.2, 0.02), stroke_width=0, fill_color=col, fill_opacity=0.9).move_to(bars.c2p(i + 0.55 + dx, v / 2))
        bs = VGroup(*[bar(i, v, SKY) for i, v in enumerate(YV)]); self.play(FadeIn(bs), run_time=0.5)
        self.readout(["y    = " + vec(YV, 1)], color=SKY, size=22)
        self.say(L("Áp dụng cho cả một vectơ: mỗi tọa độ được co riêng.", "Apply it to a whole vector: each coordinate is shrunk separately."), wait=False)
        self.wait(1.0)
        ps = VGroup(*[bar(i, v, SUN) for i, v in enumerate(PV)]); self.play(Transform(bs, ps), run_time=1.5)
        self.readout(["y    = " + vec(YV, 1), ("prox = " + vec(PV, 1), SUN)], color=SKY, size=22)
        self.say(L("Ba tọa độ nhỏ (|y| ≤ 1) thành 0: prox tạo ra vectơ thưa.", "The three small entries (|y| ≤ 1) become 0: the prox produces a sparse vector."))
        # algorithm
        self.wipe(); self.stage(3)
        ax2 = plain_axes([-1.0, 2.0], [-0.6, 1.6], 7.2, 5.2, [0, 1.3, 0])
        cs = contours(ax2, lambda x, y: F(np.array([x, y])), [FST + d for d in (0.02, 0.1, 0.3, 0.6, 1.0, 1.6, 2.4)], (-1.0, 2.0, -0.6, 1.6), N=70)
        zl = DashedLine(ax2.c2p(-1, 0), ax2.c2p(2, 0), color=PINK, stroke_width=3)
        self.play(Create(cs), Create(zl), run_time=1.0)
        self.readout(["F(x) = ½‖Ax − b‖² + %s‖x‖₁" % nf(lam, 1), "x⁺ = prox_{tλ‖·‖₁}(x − t·Aᵀ(Ax − b))"], color=SUN, size=22)
        self.say(L("Gradient gần kề (ISTA) cho lasso 2 biến: bước gradient trên phần trơn, rồi co ngưỡng mềm.",
                   "Proximal gradient (ISTA) on a 2-variable lasso: a gradient step on the smooth part, then soft-thresholding."), hold=5.0)
        d = Dot(ax2.c2p(*IS[0]), radius=0.12, color=SUN); self.add(d)
        def rd(k):
            self.readout(["k = %2d   x = %s" % (k, vec(IS[k], 4)), ("x₂ = 0 ✓" if IS[k][1] == 0 else "x₂ = %s" % nf(IS[k][1], 4), MINT if IS[k][1] == 0 else WHITE), "F − F* = %s" % sci(max(F(IS[k]) - FST, 1e-16))], color=SUN)
            self.wait(0.35)
        p1 = trail(self, ax2, IS, d, SUN, rt=0.55, ks=range(1, KZ + 3), cb=rd)
        self.say(L("Ở bước %d, x₂ chạm đúng 0 (đường hồng) và ở lại đó mãi. Nghiệm: x* = %s." % (KZ, vec(XST, 3)),
                   "At step %d, x₂ lands exactly on 0 (pink line) and stays there. Solution: x* = %s." % (KZ, vec(XST, 3))), hold=4.5)
        # contrast
        self.stage(4)
        d2 = Dot(ax2.c2p(*SG[0]), radius=0.12, color=PINK); self.add(d2)
        self.say(L("Đối chiếu: phương pháp gradient dưới trên cùng F, dùng sign(x) cho phần |x|.", "Contrast: the subgradient method on the same F, using sign(x) for the |x| part."), wait=False)
        p2 = trail(self, ax2, SG, d2, PINK, rt=0.12, ks=list(range(1, 30)) + list(range(30, 401, 10)), rate=linear, width=3)
        self.readout([("sau 400 bước:" if LANG == "vi" else "after 400 steps:", WHITE), ("ISTA       x₂ = 0          F − F* = %s" % sci(max(F(IS[400]) - FST, 1e-16)), SUN),
                      ("subgradient x₂ = %s   F − F* = %s" % (sci(abs(SG[400][1])), sci(F(SG[400]) - FST)), PINK)], size=21)
        self.say(L("Gradient dưới chỉ lảng vảng quanh 0 (x₂ ≈ %s), không bao giờ cho số 0 thật, và chậm hơn nhiều." % sci(abs(SG[400][1])),
                   "The subgradient method only hovers near 0 (x₂ ≈ %s), never an exact zero, and is far slower." % sci(abs(SG[400][1]))), hold=5.0)
        self.takeaway([L("prox của λ|x| = co ngưỡng mềm: co về 0 một đoạn λ.", "The prox of λ|x| is soft-thresholding: shrink toward 0 by λ."),
                       L("Vùng chết |y| ≤ λ cho số 0 chính xác: nghiệm thưa.", "The dead zone |y| ≤ λ gives exact zeros: sparse solutions."),
                       L("Gradient gần kề = bước gradient + prox: nhanh và thưa, khác hẳn gradient dưới.", "Proximal gradient = gradient step + prox: fast and sparse, unlike subgradients.")])
