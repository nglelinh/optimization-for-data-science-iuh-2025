from rl import *
A = np.array([[1, 1], [1, -2.]]); b = np.array([1.2, 1.0]); V = np.linalg.solve(A, b)
def proj(p):
    if (A @ p <= b + 1e-12).all(): return p.copy(), np.zeros(2)
    for i in range(2):
        lam = (A[i] @ p - b[i]) / (A[i] @ A[i]); x = p - lam * A[i]
        if lam >= 0 and (A @ x <= b + 1e-9).all(): l = np.zeros(2); l[i] = lam; return x, l
    return V.copy(), np.linalg.solve(A.T, p - V)
def kkt_ok(p, x, l):
    return np.allclose(x - p + A.T @ l, 0, atol=1e-9) and (A @ x <= b + 1e-9).all() and (l >= -1e-12).all() and np.allclose(l * (A @ x - b), 0, atol=1e-9)
for p in [np.array(q) for q in ((-0.6, 0.3), (1.6, 1.2), (2.2, -1.2), (0.6, -1.6), (-1.5, 2.0))]:
    x, l = proj(p); assert kkt_ok(p, x, l)
    xs = np.random.default_rng(0).uniform(-3, 3, (20000, 2)); ok = (xs @ A.T <= b).all(1)
    assert 0.5 * np.sum((x - p) ** 2) <= (0.5 * np.sum((xs[ok] - p) ** 2, 1)).min() + 1e-9
P1 = np.array([1.6, 1.2]); X1, L1 = proj(P1); assert np.allclose(X1, [.8, .4]) and np.allclose(L1, [.8, 0])
P2 = np.array([2.2, -1.2]); X2, L2 = proj(P2); assert (L2 > 1e-9).all()
WRONG = np.linalg.solve(A.T, P1 - V); assert WRONG.min() < 0
X1only2 = P2 - (A[0] @ P2 - b[0]) / (A[0] @ A[0]) * A[0]; assert (A @ X1only2 > b + 1e-9).any()
TOUR = [(-0.6, 0.3), (0.5, 1.6), (1.6, 1.2), (2.4, 0.2), (2.2, -1.2), (0.9, -1.7), (-0.6, -0.9), (-0.6, 0.3)]
def tour_pts(n=40):
    out = []
    for a, c in zip(TOUR[:-1], TOUR[1:]):
        for s in np.linspace(0, 1, n, endpoint=False): out.append((1 - s) * np.array(a) + s * np.array(c))
    out.append(np.array(TOUR[-1])); return out

class Kkt(Reel):
    def construct(self):
        self.title(L("Điều kiện KKT: pháp tuyến\nvà nhân tử Lagrange", "KKT conditions: normals\nand Lagrange multipliers"))
        self.stage(1)
        ax = plain_axes([-2.4, 3.0], [-2.2, 2.6], 7.4, 6.6, [0, 1.15, 0]); c = lambda p: ax.c2p(*p)
        box = [(-2.4, -2.2), (3.0, -2.2), (3.0, 2.6), (-2.4, 2.6)]
        reg = [p for p in [np.array(q) for q in ((-2.4, -2.2), (V[0], V[1]), (-2.4, 3.6))]]
        # feasible region polygon: clip box by the two half-planes
        pts = [np.array(q, float) for q in box]
        for i in range(2):
            out = []
            for j in range(len(pts)):
                a, d = pts[j - 1], pts[j]; ia, idd = A[i] @ a <= b[i], A[i] @ d <= b[i]
                if idd:
                    if not ia: t = (b[i] - A[i] @ a) / (A[i] @ (d - a)); out.append(a + t * (d - a))
                    out.append(d)
                elif ia: t = (b[i] - A[i] @ a) / (A[i] @ (d - a)); out.append(a + t * (d - a))
            pts = out
        region = Polygon(*[c(p) for p in pts], color=SKY, stroke_width=3, fill_color=SKY, fill_opacity=0.13)
        self.play(FadeIn(region), run_time=0.6)
        self.say(L("Vùng khả thi: x + y ≤ 1,2 và x − 2y ≤ 1. Bài toán: tìm điểm khả thi gần p nhất, min ½‖x − p‖².",
                   "Feasible set: x + y ≤ 1.2 and x − 2y ≤ 1. Problem: the feasible point closest to p, min ½‖x − p‖²."), hold=5.0)
        # key idea
        self.stage(2)
        self.readout(["x − p + λ₁a₁ + λ₂a₂ = 0", "Ax ≤ b,   λ ≥ 0", "λᵢ·(aᵢᵀx − bᵢ) = 0"], color=SUN, size=25)
        self.say(L("KKT: (1) dừng, (2) khả thi, (3) λ ≥ 0, (4) bù: ràng buộc không chặt thì λᵢ = 0.", "KKT: (1) stationarity, (2) feasibility, (3) λ ≥ 0, (4) complementary slackness: a slack constraint has λᵢ = 0."), hold=5.0)
        self.say(L("Hình học: p − x phải là tổ hợp KHÔNG ÂM của pháp tuyến các ràng buộc chặt, aᵢ = hàng i của A.",
                   "Geometry: p − x must be a NONNEGATIVE combination of the normals of the tight constraints, aᵢ = row i of A."), hold=5.0)
        # algorithm: tour
        self.stage(3)
        pt = ValueTracker(0)
        TP = tour_pts(); n = len(TP)
        def cur(): return TP[min(int(round(pt.get_value())), n - 1)]
        pd = always_redraw(lambda: Dot(c(cur()), radius=0.12, color=ORANGE))
        xd = always_redraw(lambda: Dot(c(proj(cur())[0]), radius=0.12, color=MINT))
        conn = always_redraw(lambda: DashedLine(c(proj(cur())[0]), c(cur()), color=WHITE, stroke_width=2.5) if np.linalg.norm(proj(cur())[0] - cur()) > 1e-6 else VGroup())
        def arrows():
            x, l = proj(cur()); g = VGroup()
            for i in range(2):
                if l[i] > 1e-6: g.add(Arrow(c(x), c(x + l[i] * A[i]), buff=0, color=[PINK, ORANGE][i], stroke_width=6, max_tip_length_to_length_ratio=0.18))
            return g
        arr = always_redraw(arrows)
        self.add(conn, arr, pd, xd)
        def ro():
            p = cur(); x, l = proj(p)
            return ["p = %s   x* = %s" % (vec(p, 2), vec(x, 2)), ("λ₁ = %s" % nf(l[0], 3), PINK), ("λ₂ = %s" % nf(l[1], 3), ORANGE)]
        self.readout(ro(), color=WHITE, size=23)
        self.say(L("Cho p (cam) đi vòng quanh. Chấm xanh là nghiệm x*; mũi tên là λᵢaᵢ, cộng lại đúng bằng p − x*.",
                   "Move p (orange) around. The green dot is the solution x*; the arrows are λᵢaᵢ and add up to exactly p − x*."), hold=4.5)
        MSG = {(False, False): L("p ở trong: x* = p, không ràng buộc nào chặt, λ = 0.", "p inside: x* = p, nothing is tight, λ = 0."),
               (True, False): L("Chỉ ràng buộc 1 chặt: λ₁ > 0, λ₂ = 0. p − x* vuông góc với cạnh 1.", "Only constraint 1 is tight: λ₁ > 0, λ₂ = 0. p − x* is perpendicular to edge 1."),
               (True, True): L("Vùng góc: cả hai chặt, x* là đỉnh, λ₁ > 0 và λ₂ > 0.", "Corner region: both are tight, x* is the vertex, λ₁ > 0 and λ₂ > 0."),
               (False, True): L("Chỉ ràng buộc 2 chặt: λ₂ > 0, λ₁ = 0.", "Only constraint 2 is tight: λ₂ > 0, λ₁ = 0.")}
        state = lambda p: tuple(bool(v > 1e-9) for v in proj(p)[1])
        cur_state = None; seen = 0
        for k in range(0, n, 3):
            st_ = state(TP[k])
            if st_ != cur_state:
                if cur_state is not None: self.wait(1.6)
                self.say(MSG[st_], wait=False); cur_state = st_; seen += 1
            self.play(pt.animate.set_value(k), run_time=0.16, rate_func=linear); self.readout(ro(), color=WHITE, size=23)
        self.wait(2.0)
        assert seen >= 4
        # contrast
        self.stage(4)
        self.play(pt.animate.set_value(80), run_time=1.0); self.readout(ro(), color=WHITE, size=23)
        self.say(L("Sai lầm thường gặp: ở p = (1,6; 1,2), thử bắt cả hai ràng buộc chặt (x = đỉnh).", "A common mistake: at p = (1.6, 1.2), force both constraints tight (x = the vertex)."), wait=False)
        gh = Dot(c(V), radius=0.14, color=PINK); self.play(FadeIn(gh, scale=1.4), run_time=0.4)
        self.readout(["x = đỉnh %s" % vec(V, 3) if LANG == "vi" else "x = vertex %s" % vec(V, 3), ("λ = %s  →  λ₂ < 0  ✗" % vec(WRONG, 3), PINK)], color=WHITE, size=24)
        self.say(L("Giải ra λ₂ = %s < 0: vi phạm λ ≥ 0, nên ràng buộc 2 không được chặt. Bỏ nó đi → nghiệm đúng (0,8; 0,4)." % nf(WRONG[1], 3),
                   "Solving gives λ₂ = %s < 0: it violates λ ≥ 0, so constraint 2 cannot be tight. Drop it → the right answer (0.8, 0.4)." % nf(WRONG[1], 3)), hold=6.0)
        self.play(FadeOut(gh), run_time=0.3)
        self.takeaway([L("Tại nghiệm: p − x* = Σ λᵢaᵢ với λᵢ ≥ 0 trên các ràng buộc chặt.", "At the solution: p − x* = Σ λᵢaᵢ with λᵢ ≥ 0 on the tight constraints."),
                       L("Ràng buộc lỏng có λᵢ = 0 (bù). λᵢ âm báo hiệu chọn sai tập chặt.", "Slack constraints have λᵢ = 0 (complementary slackness). A negative λᵢ flags a wrong active set."),
                       L("λᵢ đo độ 'đẩy' của ràng buộc: nới bᵢ một chút, mục tiêu giảm ≈ λᵢ.", "λᵢ measures how hard a constraint pushes: relax bᵢ a bit and the objective drops by ≈ λᵢ.")])
