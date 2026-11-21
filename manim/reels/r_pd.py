from rl import *
from o3lib import BA, BB, BC, barrier_run
A, B, C = BA, BB, BC; m = 5
VERTS = [(0.2, 0.2), (3, 0.2), (3, 1), (1.4, 2.6), (0.2, 2.6)]
PSTAR = C @ np.array([3, 1.0])
def pd(mu=10):
    x = np.array([1.5, 1.0]); lam = np.ones(5); rec = []
    def res(x, l, tt): return np.concatenate([C + A.T @ l, -l * (A @ x - B) - 1 / tt])
    for it in range(200):
        s = B - A @ x; eta = s @ lam; tt = mu * m / eta; r = res(x, lam, tt)
        rec.append(dict(x=x.copy(), eta=eta, rd=np.linalg.norm(r[:2]), lam=lam.copy()))
        if np.linalg.norm(r[:2]) < 1e-9 and eta < 1e-6: break
        H = (A * (lam / s)[:, None]).T @ A; rhs = -r[:2] + A.T @ (r[2:] / s); dx = np.linalg.solve(H, rhs); dl = (lam * (A @ dx) - r[2:]) / s
        smax = min([1.0] + [-lam[i] / dl[i] for i in range(5) if dl[i] < 0]); st = .99 * smax; nr = np.linalg.norm(r)
        for _ in range(60):
            xn = x + st * dx; ln = lam + st * dl
            if (A @ xn < B).all() and np.linalg.norm(res(xn, ln, tt)) <= (1 - .01 * st) * nr: break
            st *= .5
        rec[-1]["step"] = st
        x = x + st * dx; lam = lam + st * dl
    return rec
PD = pd(); NPD = len(PD) - 1
assert NPD == 10 and np.allclose(PD[-1]["x"], [3, 1], atol=1e-5) and PD[-1]["eta"] < 1e-6
# barrier with every Newton iterate
def bar_all(mu=10):
    x = np.array([1.5, 1.0]); t = 1.0; pts = [x.copy()]; outer = []
    while 5 / t > 1e-6:
        n0 = len(pts)
        for _ in range(80):
            s = B - A @ x; g = t * C + (A / s[:, None]).sum(0); H = (A / s[:, None] ** 2).T @ A; d = -np.linalg.solve(H, g); dec = -g @ d
            if dec / 2 < 1e-10: break
            phi = lambda y: t * C @ y - np.log(B - A @ y).sum(); s2 = 1.0
            while (B - A @ (x + s2 * d) <= 0).any() or phi(x + s2 * d) > phi(x) - .25 * s2 * dec: s2 *= .5
            x = x + s2 * d; pts.append(x.copy())
        outer.append((t, len(pts) - n0)); t *= mu
    return pts, outer
BP, BO = bar_all(); NB = len(BP) - 1
assert NB == barrier_run(10)[1] == 40
lamstar = PD[-1]["lam"]; assert np.allclose(C + A.T @ lamstar, 0, atol=1e-8) and (lamstar > -1e-9).all()

class Pdip(Reel):
    def construct(self):
        self.title(L("Điểm trong gốc - đối ngẫu\nso với phương pháp rào cản", "Primal-dual interior point\nvs the barrier method"))
        self.stage(1)
        ax = plain_axes([0, 3.4], [0, 3.0], 7.4, 6.5, [0, 1.15, 0]); P = lambda p: ax.c2p(p[0], p[1])
        poly = Polygon(*[P(v) for v in VERTS], color=SKY, stroke_width=4, fill_color=SKY, fill_opacity=0.12)
        self.play(Create(poly), run_time=0.8); vt = Dot(P((3, 1)), radius=0.12, color=MINT); self.add(vt)
        self.say(L("Cùng LP: tối đa x + 0,7y trên đa giác, nghiệm là đỉnh (3; 1). Hai thuật toán điểm trong, cùng xuất phát (1,5; 1).",
                   "The same LP: maximize x + 0.7y over the polygon, solution at the vertex (3, 1). Two interior-point methods, both from (1.5, 1)."), hold=5.0)
        # key idea
        self.stage(2)
        self.readout(["c + Aᵀλ = 0", "λᵢ·sᵢ = 1/t,   sᵢ = bᵢ − aᵢᵀx > 0", "λ ≥ 0"], color=SUN, size=25)
        self.say(L("KKT nhiễu: điều kiện bù λᵢsᵢ = 0 được nới thành λᵢsᵢ = 1/t. Khi t → ∞ ta về KKT thật.",
                   "Perturbed KKT: complementary slackness λᵢsᵢ = 0 is relaxed to λᵢsᵢ = 1/t. As t → ∞ we recover true KKT."), hold=5.0)
        self.say(L("Rào cản: với mỗi t, giải đúng bài định tâm (nhiều bước Newton), rồi mới tăng t. Gốc - đối ngẫu: một bước Newton cho cả (x, λ), rồi cập nhật t ngay.",
                   "Barrier: for each t, solve the centering problem fully (many Newton steps), then raise t. Primal-dual: one Newton step on (x, λ) together, then update t right away."), hold=7.0)
        # algorithm
        self.stage(3); self.clear_ro()
        d = Dot(P(PD[0]["x"]), radius=0.13, color=SUN); self.add(d)
        self.say(L("Gốc - đối ngẫu: t = μm/η với η = sᵀλ là khoảng cách đối ngẫu thay thế; μ = 10.", "Primal-dual: t = μm/η, where η = sᵀλ is the surrogate duality gap; μ = 10."), wait=False)
        segs = []
        for k in range(1, NPD + 1):
            sg = Line(P(PD[k - 1]["x"]), P(PD[k]["x"]), color=SUN, stroke_width=5); segs.append(sg)
            self.play(Create(sg), d.animate.move_to(P(PD[k]["x"])), run_time=0.7)
            r = PD[k]
            self.readout(["k = %d   bước = %s" % (k, nf(PD[k - 1]["step"], 3)) if LANG == "vi" else "k = %d   step = %s" % (k, nf(PD[k - 1]["step"], 3)), "x = %s" % vec(r["x"], 5),
                          ("η = %s   ‖rdual‖ = %s" % (sci(r["eta"]), sci(max(r["rd"], 1e-16))), MINT)], color=SUN, size=22)
            self.wait(0.6)
        self.say(L("%d bước Newton: η giảm từ %s xuống dưới 10⁻⁶. Mỗi bước giảm η gần 10 lần." % (NPD, nf(PD[0]["eta"], 2)), "%d Newton steps: η falls from %s to below 10⁻⁶, about 10× per step." % (NPD, nf(PD[0]["eta"], 2))), hold=4.5)
        self.readout(["λ* = %s" % vec(lamstar, 2), ("c + Aᵀλ* = 0  ✓", MINT)], color=WHITE, size=22)
        self.say(L("Phần thưởng: λ* — nghiệm đối ngẫu — có sẵn. Chỉ hai ràng buộc chặt tại đỉnh có λᵢ > 0.", "Bonus: λ*, the dual solution, comes for free. Only the two constraints tight at the vertex have λᵢ > 0."), hold=4.5)
        # contrast
        self.stage(4); self.play(*[s.animate.set_stroke(opacity=0.3) for s in segs], FadeOut(d), run_time=0.4)
        db = Dot(P(BP[0]), radius=0.11, color=PINK); self.add(db)
        self.say(L("Phương pháp rào cản (μ = 10): mỗi chấm nhỏ là một bước Newton trong vòng định tâm.", "The barrier method (μ = 10): every small dot is one Newton step inside a centering loop."), wait=False)
        k0 = 0; marks = VGroup(); self.add(marks)
        for j, (t, ns) in enumerate(BO):
            for i in range(k0 + 1, k0 + ns + 1):
                self.play(db.animate.move_to(P(BP[i])), run_time=0.22)
                marks.add(Dot(P(BP[i]), radius=0.05, color=PINK))
            k0 += ns
            self.readout(["t = %s   bước Newton: %d   tổng: %d" % (sci(t, 0) if t > 1 else "1", ns, k0) if LANG == "vi" else "t = %s   Newton steps: %d   total: %d" % (sci(t, 0) if t > 1 else "1", ns, k0)], color=PINK, size=23)
        self.readout([("rào cản:       %d bước Newton" % NB if LANG == "vi" else "barrier:       %d Newton steps" % NB, PINK), ("gốc - đối ngẫu: %d bước Newton" % NPD if LANG == "vi" else "primal-dual:   %d Newton steps" % NPD, SUN)], size=25)
        self.say(L("Cùng độ chính xác: %d bước so với %d. Gốc - đối ngẫu không phải đi sát đường trung tâm, và có thể xuất phát không khả thi với ràng buộc đẳng thức." % (NB, NPD),
                   "Same accuracy: %d steps versus %d. Primal-dual does not have to hug the central path, and can even start infeasible for equality constraints." % (NB, NPD)), hold=6.5)
        self.takeaway([L("Cả hai giải KKT nhiễu λᵢsᵢ = 1/t với t → ∞.", "Both solve the perturbed KKT λᵢsᵢ = 1/t with t → ∞."),
                       L("Gốc - đối ngẫu: một bước Newton cho (x, λ) rồi tăng t ngay; ở đây %d bước so với %d." % (NPD, NB), "Primal-dual: one Newton step on (x, λ), then raise t at once; here %d steps vs %d." % (NPD, NB)),
                       L("η = sᵀλ cho biết khoảng cách tới tối ưu ở mỗi bước.", "η = sᵀλ tells you the distance to optimal at every step.")])
