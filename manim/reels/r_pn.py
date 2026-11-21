from rl import *
from o3lib import Fl, Gl, Hl, Fobj, soft, prox_methods
LAM = .1
o, XS, FS = prox_methods([1.6, 1.1], LAM); G, N = o['gd'], o['nw']
assert len(G) - 1 == 9 and len(N) - 1 == 5 and Fobj(G[-1], LAM) - FS < 1e-9 and Fobj(N[-1], LAM) - FS < 1e-9
def pn_sweeps(p, tol=1e-12):
    H = Hl(p); g = Gl(p); d = np.zeros(2)
    for sw in range(1, 500):
        dold = d.copy()
        for i in range(2):
            j = 1 - i; z = p[i] - (g[i] + H[i, j] * d[j]) / H[i, i]; d[i] = soft(z, LAM / H[i, i]) - p[i]
        if np.abs(d - dold).max() < tol: return sw
    return 500
SW = [pn_sweeps(N[k]) for k in range(len(N) - 1)]
o2, XS2, FS2 = prox_methods([1.6, 1.1], 0.6)
assert XS[1] == 0.0 and G[-1][1] == 0.0 and N[-1][1] == 0.0
eG = [Fobj(p, LAM) - FS for p in G]; eN = [Fobj(p, LAM) - FS for p in N]

class Pn(Reel):
    def construct(self):
        self.title(L("Newton gần kề so với\ngradient gần kề", "Proximal Newton vs\nproximal gradient"))
        self.stage(1)
        ax = plain_axes([-1.6, 2.0], [-1.4, 1.6], 7.4, 6.2, [0, 1.15, 0])
        cs = contours(ax, lambda x, y: Fobj(np.array([x, y]), LAM), [FS + d for d in (0.03, 0.12, 0.3, 0.6, 1.0, 1.6, 2.4)], (-1.6, 2.0, -1.4, 1.6), N=70)
        self.play(Create(cs), run_time=1.4)
        st = Dot(ax.c2p(*XS), radius=0.1, color=MINT); self.add(st)
        self.say(L("F(x) = g(x) + λ‖x‖₁: g là hàm log-sum-exp trơn, cộng phạt ℓ₁ với λ = 0,1.", "F(x) = g(x) + λ‖x‖₁: g is a smooth log-sum-exp, plus an ℓ₁ penalty with λ = 0.1."))
        self.readout(["x* = %s   F* = %s" % (vec(XS, 4), nf(FS, 5)), "start = (1,6; 1,1)" if LANG == "vi" else "start = (1.6, 1.1)"], color=DIM, size=23)
        self.say(L("Nghiệm x* có x₂ = 0 đúng: phần ℓ₁ làm nghiệm thưa.", "The solution has x₂ = 0 exactly: the ℓ₁ part makes it sparse."))
        # key idea
        self.stage(2)
        self.readout(["prox-grad: min ⟨∇g, d⟩ + ‖d‖²/(2t) + λ‖x+d‖₁", "prox-Newton: min ⟨∇g, d⟩ + ½dᵀ∇²g d + λ‖x+d‖₁"], color=SUN, size=21)
        self.say(L("Cả hai thay g bằng một mô hình bậc hai và giữ nguyên λ‖x‖₁. Gradient gần kề dùng độ cong 1/t giống nhau mọi hướng.",
                   "Both replace g by a quadratic model and keep λ‖x‖₁ exact. Proximal gradient uses the same curvature 1/t in every direction."), hold=5.5)
        self.say(L("Newton gần kề dùng Hessian thật ∇²g. Bài con không còn tách được, nên phải giải bằng vòng lặp trong (coordinate descent).",
                   "Proximal Newton uses the true Hessian ∇²g. The subproblem no longer separates, so it needs an inner loop (coordinate descent)."), hold=5.5)
        # algorithm
        self.stage(3); self.clear_ro()
        dg = Dot(ax.c2p(*G[0]), radius=0.12, color=SKY); dn = Dot(ax.c2p(*N[0]), radius=0.12, color=SUN); self.add(dg, dn)
        self.say(L("Xanh: gradient gần kề (backtracking).  Vàng: Newton gần kề.", "Blue: proximal gradient (backtracking).  Yellow: proximal Newton."), wait=False)
        sgs = []
        for k in range(1, len(G)):
            an = []
            s1 = Line(ax.c2p(*G[k - 1]), ax.c2p(*G[k]), color=SKY, stroke_width=4); sgs.append(s1); an += [Create(s1), dg.animate.move_to(ax.c2p(*G[k]))]
            if k < len(N):
                s2 = Line(ax.c2p(*N[k - 1]), ax.c2p(*N[k]), color=SUN, stroke_width=5); sgs.append(s2); an += [Create(s2), dn.animate.move_to(ax.c2p(*N[k]))]
            self.play(*an, run_time=0.8)
            kn = min(k, len(N) - 1)
            self.readout([("prox-grad    k = %d   F − F* = %s" % (k, sci(max(eG[k], 1e-16))), SKY), ("prox-Newton  k = %d   F − F* = %s" % (kn, sci(max(eN[kn], 1e-16))), SUN)], size=22)
            self.wait(0.7)
        self.say(L("Newton gần kề: %d bước. Gradient gần kề: %d bước. Cả hai cho x₂ = 0 đúng." % (len(N) - 1, len(G) - 1),
                   "Proximal Newton: %d steps. Proximal gradient: %d steps. Both land on x₂ = 0 exactly." % (len(N) - 1, len(G) - 1)))
        rows = [("  k   F − F* (Newton)", WHITE)] + [("%3d   %s" % (k, sci(max(eN[k], 1e-16))), SUN) for k in range(len(N))]
        self.readout(rows, size=22)
        self.say(L("Gần nghiệm, sai số của Newton gần kề rơi siêu nhanh: hội tụ bậc hai cục bộ, giống Newton thường.", "Near the answer the proximal Newton error collapses: local quadratic convergence, like plain Newton."), hold=4.5)
        # contrast
        self.stage(4)
        rows = [("bước Newton   vòng CD bên trong" if LANG == "vi" else "Newton step   inner CD sweeps", WHITE)] + [("%6d        %d" % (k + 1, SW[k]), SUN) for k in range(len(SW))]
        self.readout(rows, size=22)
        self.say(L("Cái giá: mỗi bước Newton cần giải bài con tới chính xác cao — ở đây %d đến %d vòng coordinate descent." % (min(SW), max(SW)),
                   "The price: every Newton step solves its subproblem to high accuracy — here %d to %d coordinate-descent sweeps." % (min(SW), max(SW))), hold=5.0)
        self.say(L("Ở 2 chiều thì rẻ. Ở hàng triệu chiều, mỗi bước gradient gần kề rẻ hơn rất nhiều, nên lựa chọn phụ thuộc vào chi phí Hessian.",
                   "In 2D that is cheap. In millions of dimensions each proximal-gradient step is far cheaper, so the choice depends on the Hessian's cost."), hold=6.0)
        self.takeaway([L("Cả hai: mô hình bậc hai của g + phạt λ‖x‖₁ giữ nguyên.", "Both: a quadratic model of g plus the exact λ‖x‖₁ penalty."),
                       L("Newton gần kề dùng Hessian: ít bước (%d so với %d), hội tụ nhanh gần nghiệm." % (len(N) - 1, len(G) - 1), "Proximal Newton uses the Hessian: fewer steps (%d vs %d), fast local convergence." % (len(N) - 1, len(G) - 1)),
                       L("Nhưng mỗi bước cần một vòng lặp trong: đáng giá khi Hessian rẻ.", "But each step needs an inner loop: worth it when the Hessian is cheap.")])
