from rl import *
from o3lib import BA, BB, BC, barrier_run
# Bài 17-04: điểm trong gốc - đối ngẫu cho LP dạng chuẩn, một vòng lặp tính đầy đủ; so với phương pháp rào cản
A, B, C = BA, BB, BC; m = 5
VERTS = [(0.2, 0.2), (3, 0.2), (3, 1), (1.4, 2.6), (0.2, 2.6)]
PSTAR = C @ np.array([3, 1.0])
# dạng chuẩn: x̃ = (x₁ − 0,2; x₂ − 0,2; 3 biến bù) ≥ 0,  Ãx̃ = b̃
AT = np.array([[1, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1.]]); BT = np.array([3.6, 2.8, 2.4]); CT = np.array([-1, -0.7, 0, 0, 0.])
NS, MS = 5, 3
for v in VERTS:   # mỗi đỉnh của đa giác ứng với một nghiệm cơ sở khả thi của dạng chuẩn
    xx = np.array([v[0] - .2, v[1] - .2]); sl = BT - AT[:, :2] @ xx; assert (sl >= -1e-12).all() and np.allclose(B - A @ np.array(v), np.r_[v[0] - .2, v[1] - .2, sl])
def pdstd(sig=0.1, tol=1e-6):
    x = np.ones(NS); s = np.ones(NS); y = np.zeros(MS); rec = []
    for k in range(60):
        rp = AT @ x - BT; rd = AT.T @ y + s - CT; eta = x @ s; tau = sig * eta / NS
        rec.append(dict(x=x.copy(), y=y.copy(), s=s.copy(), rp=rp, rd=rd, eta=eta, tau=tau))
        if np.linalg.norm(rp) < 1e-9 and np.linalg.norm(rd) < 1e-9 and eta < tol: break
        K = np.zeros((2 * NS + MS, 2 * NS + MS))
        K[:NS, NS:NS + MS] = AT.T; K[:NS, NS + MS:] = np.eye(NS); K[NS:NS + MS, :NS] = AT; K[NS + MS:, :NS] = np.diag(s); K[NS + MS:, NS + MS:] = np.diag(x)
        d = np.linalg.solve(K, -np.concatenate([rd, rp, x * s - tau])); dx, dy, ds = d[:NS], d[NS:NS + MS], d[NS + MS:]
        a = 1.0
        for v, dv in ((x, dx), (s, ds)):
            if (dv < 0).any(): a = min(a, 0.99 * np.min(-v[dv < 0] / dv[dv < 0]))
        rec[-1].update(dx=dx, dy=dy, ds=ds, a=a)
        x = x + a * dx; y = y + a * dy; s = s + a * ds
    return rec
PD = pdstd(); NPD = len(PD) - 1
XY = lambda r: r["x"][:2] + 0.2
assert NPD == 8 and np.allclose(XY(PD[-1]), [3, 1], atol=1e-5) and PD[-1]["eta"] < 1e-6
nr = lambda v: float(np.linalg.norm(v))
R0 = PD[0]; assert np.allclose(R0["rp"], [-0.6, -0.8, -0.4]) and np.allclose(R0["rd"], [2, 1.7, 1, 1, 1]) and R0["eta"] == 5 and np.isclose(R0["tau"], 0.1)
assert abs(nr(R0["rp"]) - 1.077) < 1e-3 and abs(nr(R0["rd"]) - 3.144) < 1e-3
assert np.isclose(R0["a"], 0.99 / 1.5625) and np.isclose(R0["ds"].min(), -1.5625)
for k in range(NPD):   # phần dư tuyến tính co đúng theo (1 − α)
    assert np.allclose(PD[k + 1]["rp"], (1 - PD[k]["a"]) * PD[k]["rp"], atol=1e-12) and np.allclose(PD[k + 1]["rd"], (1 - PD[k]["a"]) * PD[k]["rd"], atol=1e-12)
KF = next(k for k in range(NPD) if PD[k]["a"] == 1.0); assert KF == 3 and nr(PD[KF + 1]["rp"]) < 1e-12
assert all(PD[k + 1]["eta"] < PD[k]["eta"] for k in range(NPD)) and all(abs(PD[k + 1]["eta"] / PD[k]["eta"] - 0.1) < 1e-6 for k in range(KF + 1, NPD))
YS, SS = PD[-1]["y"], PD[-1]["s"]
assert np.allclose(YS, [-0.7, -0.3, 0], atol=1e-6) and np.allclose(SS, [0, 0, 0.7, 0.3, 0], atol=1e-6) and abs(CT @ PD[-1]["x"] - BT @ YS) < 1e-5
assert np.isclose(-(CT @ np.array([2.8, 0.8, 0, 0, 1.6])) + 0.2 + 0.14, -PSTAR)
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
VI = LANG == "vi"

def mtx(rows, color=WHITE, size=24):
    """ma trận nhỏ: lưới số + hai ngoặc vuông"""
    cells = VGroup(*[Text(s, font=MONO, font_size=size, color=color) for r in rows for s in r])
    g = cells.arrange_in_grid(rows=len(rows), cols=len(rows[0]), buff=(0.35, 0.12), col_alignments="r" * len(rows[0]))
    h = g.height + 0.16; l = g.get_left()[0] - 0.12; rr = g.get_right()[0] + 0.12; cy = g.get_center()[1]
    br = VGroup(*[VMobject(color=color, stroke_width=2.5).set_points_as_corners([[x0 + dx, cy + h / 2, 0], [x0, cy + h / 2, 0], [x0, cy - h / 2, 0], [x0 + dx, cy - h / 2, 0]]) for x0, dx in ((l, 0.12), (rr, -0.12))])
    return VGroup(g, br)

def eq_row(parts, size=24):
    """hàng gồm chữ và ma trận xếp ngang"""
    ms = [Text(p, font=MONO, font_size=size, color=WHITE) if isinstance(p, str) else p for p in parts]
    return VGroup(*ms).arrange(RIGHT, buff=0.2)

class Pdip(Reel):
    def construct(self):
        self.title(L("Điểm trong gốc - đối ngẫu\nso với phương pháp rào cản", "Primal-dual interior point\nvs the barrier method"))
        # ---- stage 1
        self.stage(1)
        ax = plain_axes([0, 3.4], [0, 3.0], 7.4, 6.5, [0, 1.15, 0]); P = lambda p: ax.c2p(p[0], p[1])
        poly = Polygon(*[P(v) for v in VERTS], color=SKY, stroke_width=4, fill_color=SKY, fill_opacity=0.12)
        self.play(Create(poly), run_time=0.8); vt = Dot(P((3, 1)), radius=0.12, color=MINT); self.add(vt)
        self.say(L("LP: tối đa x₁ + 0,7x₂ trên đa giác xanh, với 0,2 ≤ x₁ ≤ 3, 0,2 ≤ x₂ ≤ 2,6, x₁ + x₂ ≤ 4. Nghiệm là đỉnh (3; 1), giá trị 3,7.",
                   "LP: maximize x₁ + 0.7x₂ over the blue polygon, with 0.2 ≤ x₁ ≤ 3, 0.2 ≤ x₂ ≤ 2.6, x₁ + x₂ ≤ 4. The answer is the vertex (3, 1), value 3.7."), hold=10.0)
        self.readout([("dạng chuẩn:  min cᵀx,  Ax = b,  x ≥ 0" if VI else "standard form:  min cᵀx,  Ax = b,  x ≥ 0", SUN), ("x = (x₁ − 0,2; x₂ − 0,2; 3 biến bù) ∈ ℝ⁵" if VI else "x = (x₁ − 0.2, x₂ − 0.2, 3 slacks) ∈ ℝ⁵", WHITE),
                      ("c = (−1; −0,7; 0; 0; 0),  b = (3,6; 2,8; 2,4)" if VI else "c = (−1, −0.7, 0, 0, 0),  b = (3.6, 2.8, 2.4)", WHITE)], size=22)
        self.say(L("Để dùng đúng công thức của bài 17-04, viết lại thành dạng chuẩn: dời gốc đi 0,2 và thêm 3 biến bù. Được 5 biến không âm, 3 ràng buộc đẳng thức.",
                   "To use lesson 17-04's formulas as written, rewrite it in standard form: shift the origin by 0.2 and add 3 slacks. That gives 5 nonnegative variables and 3 equality constraints."), hold=11.0)
        # ---- stage 2
        self.stage(2); self.clear_ro(); self.play(FadeOut(poly), FadeOut(vt), run_time=0.4)
        eqs = VGroup(*[Text(t_, font=MONO, font_size=26, color=c_) for t_, c_ in (("Aᵀy + s = c", WHITE), ("Ax = b", WHITE), ("XS𝟙 = τ𝟙", SUN), ("x > 0,  s > 0", WHITE))]).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to([0, 2.9, 0])
        self.play(FadeIn(eqs), run_time=0.5)
        self.say(L("Đường trung tâm: khả thi đối ngẫu, khả thi gốc, và điều kiện bù bị nới: xᵢsᵢ = τ thay vì 0. Cho τ → 0 thì về đúng KKT của LP.",
                   "The central path: dual feasibility, primal feasibility, and relaxed complementarity: xᵢsᵢ = τ instead of 0. Let τ → 0 and we get the LP's KKT conditions."), hold=10.0)
        nm = VGroup(mtx([["0", "Aᵀ", "I"], ["A", "0", "0"], ["S", "0", "X"]], WHITE, 24), mtx([["Δx"], ["Δy"], ["Δs"]], WHITE, 24), Text("= −", font=MONO, font_size=26), mtx([["r_dual"], ["r_pri"], ["r_cent"]], SUN, 24)).arrange(RIGHT, buff=0.25).move_to([0, 0.4, 0])
        self.play(FadeIn(nm), run_time=0.5)
        self.readout([("r_dual = Aᵀy + s − c", WHITE), ("r_pri = Ax − b", WHITE), ("r_cent = XS𝟙 − τ𝟙,   τ = σ·η/n,   η = xᵀs", SUN)], size=23, y=-1.6)
        self.say(L("Mỗi vòng giải đúng một hệ Newton này. Vế phải là ba phần dư: đối ngẫu, gốc, và độ lệch khỏi đường trung tâm.",
                   "Each round solves exactly one Newton system like this. The right side holds three residuals: dual, primal, and distance from the central path."), hold=9.0)
        self.say(L("η = xᵀs là khoảng cách đối ngẫu thay thế: khi đã khả thi, nó đúng bằng cᵀx − bᵀy. Mục tiêu τ được đặt bằng σ·η/n với σ = 0,1, tức μ = 10 như bài.",
                   "η = xᵀs is the surrogate duality gap: once feasible, it equals cᵀx − bᵀy exactly. The target τ is set to σ·η/n with σ = 0.1, i.e. μ = 10 as in the lesson."), hold=11.0)
        self.say(L("Khác rào cản: không định tâm cho xong rồi mới giảm τ. Chỉ một bước Newton cho cả (x, y, s), rồi giảm τ ngay.",
                   "Unlike the barrier method, it never finishes centering before lowering τ. Just one Newton step on (x, y, s) together, then lower τ at once."), hold=8.5)
        # ---- stage 3: một vòng lặp đầy đủ
        self.stage(3); self.play(FadeOut(eqs), FadeOut(nm), run_time=0.3); self.clear_ro()
        def rows0(r, extra=()):
            return [("k = 0:  x = s = 𝟙,  y = 0" if VI else "k = 0:  x = s = 𝟙,  y = 0", WHITE), ("r_pri = %s,  ‖·‖ = %s" % (vec(r["rp"], 1), nf(nr(r["rp"]), 2)), SKY), ("r_dual = %s" % vec(r["rd"], 1), PINK), ("‖r_dual‖ = %s,   η = %s,   τ = %s" % (nf(nr(r["rd"]), 2), nf(r["eta"], 0), nf(r["tau"], 1)), SUN)] + list(extra)
        self.readout(rows0(R0), size=22, y=2.6)
        self.say(L("Tính tay vòng đầu. Xuất phát x = s = 1, y = 0: chưa khả thi gì cả. Phần dư gốc ≈ 1,08, phần dư đối ngẫu ≈ 3,14, η = 5, nên τ = 0,1·5/5 = 0,1.",
                   "Work the first round by hand. Start at x = s = 1, y = 0: nothing is feasible yet. Primal residual ≈ 1.08, dual residual ≈ 3.14, η = 5, so τ = 0.1·5/5 = 0.1."), hold=12.0)
        self.readout(rows0(R0, [("Δx = %s" % vec(R0["dx"], 2), MINT), ("Δs = %s" % vec(R0["ds"], 2), MINT), ("α = %s × 1/%s = %s" % (nf(0.99, 2), nf(1.5625, 4), nf(R0["a"], 3)), ORANGE)]), size=22, y=1.8)
        self.say(L("Giải hệ Newton được Δx, Δy, Δs. Bước đầy đủ sẽ làm s₁ âm, vì Δs₁ = −1,5625. Nên chỉ đi 99% quãng tới biên: α = 0,99/1,5625 ≈ 0,634.",
                   "Solving the Newton system gives Δx, Δy, Δs. A full step would make s₁ negative, since Δs₁ = −1.5625. So go only 99% of the way to the boundary: α = 0.99/1.5625 ≈ 0.634."), hold=12.0)
        r1 = PD[1]
        self.readout(rows0(R0, [("Δx = %s" % vec(R0["dx"], 2), MINT), ("Δs = %s" % vec(R0["ds"], 2), MINT), ("α = %s × 1/%s = %s" % (nf(0.99, 2), nf(1.5625, 4), nf(R0["a"], 3)), ORANGE),
                                ("k = 1:  ‖r_pri‖ = %s = (1 − α)·%s" % (nf(nr(r1["rp"]), 3), nf(nr(R0["rp"]), 3)), SKY), ("‖r_dual‖ = %s,   η = %s" % (nf(nr(r1["rd"]), 3), nf(r1["eta"], 2)), SUN)]), size=22, y=1.6)
        self.say(L("Sau bước này, hai phần dư tuyến tính co đúng theo hệ số 1 − α: 1,08 còn 0,395. Còn η giảm từ 5 xuống 1,57.",
                   "After this step both linear residuals shrink by exactly the factor 1 − α: 1.08 becomes 0.395. And η drops from 5 to 1.57."), hold=9.5)
        self.clear_ro(); self.play(FadeIn(poly), FadeIn(vt), run_time=0.4)
        d = Dot(P(XY(PD[0])), radius=0.13, color=SUN); self.add(d)
        self.say(L("Giờ chạy hết. Chấm vàng là (x₁, x₂) của nghiệm gốc hiện tại. Bảng: phần dư gốc, phần dư đối ngẫu, η, và bước α.",
                   "Now run it all. The yellow dot is (x₁, x₂) of the current primal iterate. Table: primal residual, dual residual, η, and the step α."), wait=False)
        segs = []; rows = [("k   ‖r_pri‖    ‖r_dual‖   η          α" , WHITE)]
        for k in range(1, NPD + 1):
            sg = Line(P(XY(PD[k - 1])), P(XY(PD[k])), color=SUN, stroke_width=5); segs.append(sg)
            self.play(Create(sg), d.animate.move_to(P(XY(PD[k]))), run_time=0.8)
            r = PD[k]; rows.append(("%d   %-9s  %-9s  %-9s  %s" % (k, sci(max(nr(r["rp"]), 1e-16)), sci(max(nr(r["rd"]), 1e-16)), sci(r["eta"]), nf(PD[k - 1]["a"], 3)), SUN))
            if len(rows) > 6: rows = [rows[0]] + rows[-5:]
            self.readout(rows, size=21, y=-3.1); self.wait(0.9)
            if k == KF + 1:
                self.say(L("Ở vòng %d bước đầy đủ α = 1 được chấp nhận: hai phần dư rơi về 0 (cỡ 10⁻¹⁶). Từ đây mọi điểm đều khả thi, η giảm đúng 10 lần mỗi vòng." % (KF + 1),
                           "At round %d the full step α = 1 is accepted: both residuals drop to 0 (around 10⁻¹⁶). From here on every iterate is feasible and η falls exactly 10× per round." % (KF + 1)), wait=False)
        self.wait(5.5)
        self.readout([("y* = %s" % vec(YS, 2), WHITE), ("s* = %s" % vec(SS, 2), WHITE), ("cᵀx* = bᵀy* = %s  ⇒  max = %s" % (nf(CT @ PD[-1]["x"], 2), nf(-PSTAR, 1)), MINT)], size=22, y=-3.1)
        self.say(L("%d bước Newton là η < 10⁻⁶. Nghiệm đối ngẫu có sẵn: s* = 0,7 và 0,3 ở hai biến bù của hai ràng buộc chặt tại đỉnh. Hai giá trị gốc và đối ngẫu bằng nhau." % NPD,
                   "%d Newton steps bring η below 10⁻⁶. The dual solution comes for free: s* = 0.7 and 0.3 on the slacks of the two constraints tight at the vertex. Primal and dual values agree." % NPD), hold=11.5)
        # ---- stage 4
        self.stage(4); self.play(*[s.animate.set_stroke(opacity=0.3) for s in segs], FadeOut(d), run_time=0.4)
        db = Dot(P(BP[0]), radius=0.11, color=PINK); self.add(db)
        self.say(L("Phương pháp rào cản (μ = 10) trên cùng đa giác: mỗi chấm nhỏ là một bước Newton trong vòng định tâm.", "The barrier method (μ = 10) on the same polygon: every small dot is one Newton step inside a centering loop."), wait=False)
        k0 = 0; marks = VGroup(); self.add(marks)
        for j, (t, ns) in enumerate(BO):
            for i in range(k0 + 1, k0 + ns + 1):
                self.play(db.animate.move_to(P(BP[i])), run_time=0.24)
                marks.add(Dot(P(BP[i]), radius=0.05, color=PINK))
            k0 += ns
            self.readout(["t = %s   bước Newton: %d   tổng: %d" % (sci(t, 0) if t > 1 else "1", ns, k0) if VI else "t = %s   Newton steps: %d   total: %d" % (sci(t, 0) if t > 1 else "1", ns, k0)], color=PINK, size=23)
        self.readout([("rào cản:        %d bước Newton" % NB if VI else "barrier:       %d Newton steps" % NB, PINK), ("gốc - đối ngẫu: %d bước Newton" % NPD if VI else "primal-dual:   %d Newton steps" % NPD, SUN), ("cùng mức khoảng cách ≤ 10⁻⁶" if VI else "same gap ≤ 10⁻⁶", WHITE)], size=24)
        self.say(L("Cùng độ chính xác: %d bước so với %d. Rào cản tốn công nhất ở mấy lần định tâm đầu, khi t còn nhỏ." % (NB, NPD),
                   "Same accuracy: %d steps versus %d. The barrier method spends most of its work on the first few centerings, while t is small." % (NB, NPD)), hold=9.0)
        self.say(L("Thêm một lợi thế: rào cản cần một điểm xuất phát khả thi ngặt. Gốc - đối ngẫu thì như vừa thấy, xuất phát không khả thi vẫn chạy, phần dư tự co về 0.",
                   "One more advantage: the barrier method needs a strictly feasible start. Primal-dual, as we just saw, can start infeasible; the residuals shrink to 0 on their own."), hold=10.0)
        self.takeaway([L("Cả hai đi theo đường trung tâm XS𝟙 = τ𝟙 với τ → 0.", "Both follow the central path XS𝟙 = τ𝟙 with τ → 0."),
                       L("Gốc - đối ngẫu: mỗi vòng một bước Newton cho (x, y, s), α giữ x, s > 0.", "Primal-dual: one Newton step on (x, y, s) per round, α keeps x, s > 0."),
                       L("Phần dư gốc, đối ngẫu co theo (1 − α); η = xᵀs đo khoảng cách tới tối ưu.", "Primal and dual residuals shrink by (1 − α); η = xᵀs measures the gap to optimal."),
                       L("Ở đây %d bước Newton so với %d của rào cản." % (NPD, NB), "Here %d Newton steps versus %d for the barrier method." % (NPD, NB))], tail=4.0)
