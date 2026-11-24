from rl import *
# Bài 16-02: điều kiện KKT, kiểm tra từng điều kiện bằng số trên bài chiếu lên đa diện
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

# kiểm tra bằng số tại p = (1,6; 1,2)
G1 = A @ X1 - b; ST1 = X1 - P1 + A.T @ L1
assert np.allclose(G1, [0, -1]) and np.allclose(ST1, 0) and np.allclose(L1 * G1, 0)
assert np.isclose((A[0] @ P1 - b[0]) / (A[0] @ A[0]), 0.8)
assert np.allclose(tour_pts()[80], P1)
# góc: p = (2,2; −1,2), cả hai ràng buộc chặt
assert np.allclose(X2, V) and np.allclose(V, [17 / 15, 1 / 15]) and np.allclose(L2, [13 / 45, 7 / 9]) and np.allclose(X2 - P2 + A.T @ L2, 0)
# độ nhạy: nới b₁ từ 1,2 lên 1,3 thì mục tiêu giảm ≈ λ₁·0,1
def obj_b1(b1):
    x = P1 - (A[0] @ P1 - b1) / (A[0] @ A[0]) * A[0]; assert A[1] @ x <= b[1]; return 0.5 * np.sum((x - P1) ** 2)
OB0, OB1 = obj_b1(1.2), obj_b1(1.3); assert np.isclose(OB0, 0.64) and np.isclose(OB1, 0.5625) and abs((OB0 - OB1) - 0.08) < 0.003
VI = LANG == "vi"

class Kkt(Reel):
    def construct(self):
        self.title(L("Điều kiện KKT: pháp tuyến\nvà nhân tử Lagrange", "KKT conditions: normals\nand Lagrange multipliers"))
        # ---- stage 1
        self.stage(1)
        ax = plain_axes([-2.4, 3.0], [-2.2, 2.6], 7.4, 6.6, [0, 1.15, 0]); c = lambda p: ax.c2p(*p)
        box = [(-2.4, -2.2), (3.0, -2.2), (3.0, 2.6), (-2.4, 2.6)]
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
        self.say(L("Vùng khả thi: x + y ≤ 1,2 và x − 2y ≤ 1. Bài toán: tìm điểm khả thi gần p nhất, tức min ½‖x − p‖².",
                   "Feasible set: x + y ≤ 1.2 and x − 2y ≤ 1. Problem: find the feasible point closest to p, i.e. min ½‖x − p‖²."), hold=8.5)
        self.readout(["hᵢ(x) = aᵢᵀx − bᵢ ≤ 0", "a₁ = (1, 1),   b₁ = %s" % nf(1.2, 1), "a₂ = (1, −2),  b₂ = 1"], color=DIM, size=24)
        self.say(L("Theo ký hiệu của bài 16-02: hᵢ(x) = aᵢᵀx − bᵢ ≤ 0. Bài gọi nhân tử là uᵢ, ở đây gọi là λᵢ. Hàm mục tiêu lồi, ràng buộc tuyến tính, nên KKT là đủ.",
                   "In lesson 16-02's notation: hᵢ(x) = aᵢᵀx − bᵢ ≤ 0. The lesson calls the multipliers uᵢ; here they are λᵢ. Convex objective, linear constraints, so KKT is sufficient."), hold=10.5)
        # ---- stage 2
        self.stage(2)
        self.readout(["(1) x − p + λ₁a₁ + λ₂a₂ = 0", "(2) Ax ≤ b", "(3) λ ≥ 0", "(4) λᵢ·(aᵢᵀx − bᵢ) = 0"], color=SUN, size=25)
        self.say(L("Bốn điều kiện KKT: (1) dừng, (2) khả thi gốc, (3) khả thi đối ngẫu λ ≥ 0, (4) bù: ràng buộc nào không chặt thì λᵢ = 0.",
                   "The four KKT conditions: (1) stationarity, (2) primal feasibility, (3) dual feasibility λ ≥ 0, (4) complementary slackness: a slack constraint has λᵢ = 0."), hold=9.5)
        self.say(L("Hình học: p − x phải là tổ hợp KHÔNG ÂM của pháp tuyến các ràng buộc chặt, với aᵢ là hàng i của A.",
                   "Geometry: p − x must be a NONNEGATIVE combination of the normals of the tight constraints, where aᵢ is row i of A."), hold=8.0)
        # ---- stage 3: tour
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
                   "Move p (orange) around. The green dot is the solution x*; the arrows are λᵢaᵢ and add up to exactly p − x*."), hold=6.5)
        MSG = {(False, False): L("p ở trong: x* = p, không ràng buộc nào chặt, λ = 0.", "p inside: x* = p, nothing is tight, λ = 0."),
               (True, False): L("Chỉ ràng buộc 1 chặt: λ₁ > 0, λ₂ = 0. p − x* vuông góc với cạnh 1.", "Only constraint 1 is tight: λ₁ > 0, λ₂ = 0. p − x* is perpendicular to edge 1."),
               (True, True): L("Vùng góc: cả hai chặt, x* là đỉnh, λ₁ > 0 và λ₂ > 0.", "Corner region: both are tight, x* is the vertex, λ₁ > 0 and λ₂ > 0."),
               (False, True): L("Chỉ ràng buộc 2 chặt: λ₂ > 0, λ₁ = 0.", "Only constraint 2 is tight: λ₂ > 0, λ₁ = 0.")}
        state = lambda p: tuple(bool(v > 1e-9) for v in proj(p)[1])
        cur_state = None; seen = 0
        for k in range(0, n, 3):
            st_ = state(TP[k])
            if st_ != cur_state:
                if cur_state is not None: self.wait(2.2)
                self.say(MSG[st_], wait=False); cur_state = st_; seen += 1
            self.play(pt.animate.set_value(k), run_time=0.18, rate_func=linear); self.readout(ro(), color=WHITE, size=23)
        self.wait(2.5)
        assert seen >= 4
        # kiểm tra từng điều kiện tại p = (1,6; 1,2)
        self.play(pt.animate.set_value(80), run_time=1.0)
        self.readout(["p = %s" % vec(P1, 1), ("ứng viên x = %s,  λ = %s" % (vec(X1, 1), vec(L1, 1)) if VI else "candidate x = %s,  λ = %s" % (vec(X1, 1), vec(L1, 1)), WHITE), ("λ₁ = (a₁ᵀp − b₁)/‖a₁‖²", PINK), ("   = (%s − %s)/2 = %s" % (nf(2.8, 1), nf(1.2, 1), nf(0.8, 1)), PINK)], color=WHITE, size=23)
        self.say(L("Giờ kiểm tra tay tại p = (1,6; 1,2). Đoán chỉ ràng buộc 1 chặt: chiếu p lên cạnh 1 cho x = (0,8; 0,4), và λ₁ = (2,8 − 1,2)/2 = 0,8.",
                   "Now check by hand at p = (1.6, 1.2). Guess that only constraint 1 is tight: projecting p onto edge 1 gives x = (0.8, 0.4), and λ₁ = (2.8 − 1.2)/2 = 0.8."), hold=10.5)
        chk = [[("(2) a₁ᵀx = %s = b₁  (chặt)" % nf(1.2, 1) if VI else "(2) a₁ᵀx = %s = b₁  (tight)" % nf(1.2, 1), MINT), ("    a₂ᵀx = 0 < 1  (dư 1)  ✓" if VI else "    a₂ᵀx = 0 < 1  (slack 1)  ✓", MINT)],
               [("(3) λ = %s ≥ 0  ✓" % vec(L1, 1), MINT)],
               [("(4) λ₁·0 = 0,  λ₂·(−1) = 0  ✓", MINT)],
               [("(1) x − p + λ₁a₁ = %s  ✓" % vec(ST1, 0), MINT)]]
        caps = [L("Khả thi gốc: ràng buộc 1 bằng đúng 1,2, tức là chặt. Ràng buộc 2 cho 0 ≤ 1, còn dư 1, tức là lỏng.",
                  "Primal feasibility: constraint 1 equals exactly 1.2, so it is tight. Constraint 2 gives 0 ≤ 1 with slack 1, so it is loose."),
                L("Khả thi đối ngẫu: cả hai nhân tử đều không âm.", "Dual feasibility: both multipliers are nonnegative."),
                L("Bù: ràng buộc 1 chặt nên tích bằng 0; ràng buộc 2 lỏng nhưng λ₂ = 0 nên tích cũng bằng 0.",
                  "Complementary slackness: constraint 1 is tight, so its product is 0; constraint 2 is loose but λ₂ = 0, so its product is 0 too."),
                L("Dừng: 0,8 − 1,6 + 0,8 = 0 và 0,4 − 1,2 + 0,8 = 0, đúng từng toạ độ. Đủ cả bốn, nên x = (0,8; 0,4) là nghiệm tối ưu.",
                  "Stationarity: 0.8 − 1.6 + 0.8 = 0 and 0.4 − 1.2 + 0.8 = 0, coordinate by coordinate. All four hold, so x = (0.8, 0.4) is optimal.")]
        for j in range(4):
            self.readout(sum(chk[:j + 1], []), size=24)
            self.say(caps[j], hold=[8.5, 5.5, 8.5, 8.5][j])
        self.play(pt.animate.set_value(160), run_time=1.0)
        self.readout(["p = %s" % vec(P2, 1), ("x = đỉnh %s" % vec(X2, 3) if VI else "x = vertex %s" % vec(X2, 3), WHITE), ("λ = %s ≥ 0  ✓" % vec(L2, 3), MINT),
                      ("x − p + λ₁a₁ + λ₂a₂ = %s  ✓" % vec(X2 - P2 + A.T @ L2, 0), MINT)], color=WHITE, size=23)
        self.say(L("Ở góc p = (2,2; −1,2): cả hai chặt, x là đỉnh (1,133; 0,067). Giải hệ dừng cho λ = (0,289; 0,778), cả hai dương. KKT đủ, đây là nghiệm.",
                   "At the corner p = (2.2, −1.2): both are tight, x is the vertex (1.133, 0.067). Solving stationarity gives λ = (0.289, 0.778), both positive. KKT holds, so this is the answer."), hold=11.0)
        # ---- stage 4
        self.stage(4)
        self.play(pt.animate.set_value(80), run_time=1.0); self.readout(ro(), color=WHITE, size=23)
        self.say(L("Sai lầm thường gặp: ở p = (1,6; 1,2), thử bắt cả hai ràng buộc chặt, tức x = đỉnh.", "A common mistake: at p = (1.6, 1.2), force both constraints tight, i.e. x = the vertex."), hold=6.5)
        gh = Dot(c(V), radius=0.14, color=PINK); self.play(FadeIn(gh, scale=1.4), run_time=0.4)
        self.readout(["x = đỉnh %s" % vec(V, 3) if VI else "x = vertex %s" % vec(V, 3), ("λ = %s  →  λ₂ < 0  ✗" % vec(WRONG, 3), PINK)], color=WHITE, size=24)
        self.say(L("Giải ra λ₂ = %s < 0: vi phạm điều kiện (3), nên ràng buộc 2 không được chặt. Bỏ nó đi thì quay về nghiệm đúng (0,8; 0,4)." % nf(WRONG[1], 3),
                   "Solving gives λ₂ = %s < 0: it violates condition (3), so constraint 2 cannot be tight. Drop it and we are back at the right answer (0.8, 0.4)." % nf(WRONG[1], 3)), hold=9.5)
        self.play(FadeOut(gh), run_time=0.3)
        self.readout([("b₁ = %s:  ½‖x* − p‖² = %s" % (nf(1.2, 1), nf(OB0, 4)), WHITE), ("b₁ = %s:  ½‖x* − p‖² = %s" % (nf(1.3, 1), nf(OB1, 4)), WHITE), ("giảm %s ≈ λ₁ × %s = %s" % (nf(OB0 - OB1, 4), nf(0.1, 1), nf(0.08, 2)) if VI else "drop %s ≈ λ₁ × %s = %s" % (nf(OB0 - OB1, 4), nf(0.1, 1), nf(0.08, 2)), SUN)], size=23)
        self.say(L("λ còn đo độ “đẩy” của ràng buộc. Nới b₁ từ 1,2 lên 1,3: mục tiêu giảm từ 0,64 xuống 0,5625, tức 0,0775, gần đúng λ₁ × 0,1 = 0,08.",
                   "λ also measures how hard a constraint pushes. Relax b₁ from 1.2 to 1.3: the objective drops from 0.64 to 0.5625, i.e. 0.0775, close to λ₁ × 0.1 = 0.08."), hold=11.0)
        self.takeaway([L("Tại nghiệm: p − x* = Σ λᵢaᵢ với λᵢ ≥ 0 trên các ràng buộc chặt.", "At the solution: p − x* = Σ λᵢaᵢ with λᵢ ≥ 0 on the tight constraints."),
                       L("Kiểm tra đủ bốn điều: dừng, khả thi gốc, λ ≥ 0, bù.", "Check all four: stationarity, primal feasibility, λ ≥ 0, complementary slackness."),
                       L("Ràng buộc lỏng có λᵢ = 0. λᵢ âm báo hiệu chọn sai tập chặt.", "Slack constraints have λᵢ = 0. A negative λᵢ flags a wrong active set."),
                       L("λᵢ đo độ đẩy của ràng buộc: nới bᵢ một chút, mục tiêu giảm ≈ λᵢ lần.", "λᵢ measures the push of a constraint: relax bᵢ a little and the objective drops ≈ λᵢ times that.")], tail=4.0)
