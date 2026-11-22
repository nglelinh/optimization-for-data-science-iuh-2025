from rl import *
# Bài 05-01-01: max 3x₁ + 2x₂  s.t. x₁ + x₂ ≤ 4, 2x₁ + x₂ ≤ 6, x ≥ 0  (min −3x₁ − 2x₂, thêm biến bù s₁, s₂)
A0 = np.array([[1., 1, 1, 0], [2, 1, 0, 1]]); b0 = np.array([4., 6]); c0 = np.array([-3., -2, 0, 0])
VERT = [(0, 0), (3, 0), (2, 2), (0, 4)]; VAL = [3 * x + 2 * y for x, y in VERT]
assert VAL == [0, 9, 10, 8]
for x, y in VERT: assert x + y <= 4 + 1e-12 and 2 * x + y <= 6 + 1e-12
def tableau(A, b, c): return np.vstack([np.c_[A, b], np.r_[c, 0.]])
def pivot(T, r, j):
    T = T.copy(); T[r] /= T[r, j]
    for i in range(len(T)):
        if i != r: T[i] -= T[i, j] * T[r]
    return T
def choose(T):
    cb = T[-1, :-1]; j = int(np.argmin(cb))
    if cb[j] >= -1e-12: return None, None, None
    col = T[:-1, j]; rat = np.array([T[i, -1] / col[i] if col[i] > 1e-12 else np.inf for i in range(len(col))])
    return j, (int(np.argmin(rat)) if np.isfinite(rat).any() else None), rat
NAMES = ["x₁", "x₂", "s₁", "s₂"]
T0 = tableau(A0, b0, c0); B0 = [2, 3]
j1, r1, rat1 = choose(T0); assert (j1, r1) == (0, 1) and np.allclose(rat1, [4, 3])
T1 = pivot(T0, r1, j1); B1 = [2, 0]
assert np.allclose(T1, [[0, .5, 1, -.5, 1], [1, .5, 0, .5, 3], [0, -.5, 0, 1.5, 9]])
j2, r2, rat2 = choose(T1); assert (j2, r2) == (1, 0) and np.allclose(rat2, [2, 6])
T2 = pivot(T1, r2, j2); B2 = [1, 0]
assert np.allclose(T2, [[0, 1, 2, -1, 2], [1, 0, -1, 1, 2], [0, 0, 1, 1, 10]]) and choose(T2)[0] is None
Y = T2[-1, 2:4]; assert np.allclose(Y, [1, 1]) and abs(b0 @ Y - 10) < 1e-12 and np.all(A0[:, :2].T @ Y >= np.array([3, 2]) - 1e-12)
def bfs(T, B):
    x = np.zeros(4)
    for i, bi in enumerate(B): x[bi] = T[i, -1]
    return x
assert np.allclose(bfs(T0, B0)[:2], [0, 0]) and np.allclose(bfs(T1, B1)[:2], [3, 0]) and np.allclose(bfs(T2, B2)[:2], [2, 2])
# lối khác: cho x₂ vào trước → (0, 4) rồi (2, 2)
Ta = pivot(T0, 0, 1); assert np.allclose(Ta[-1, -1], 8); ja, ra, _ = choose(Ta); assert (ja, ra) == (0, 1)
Tb = pivot(Ta, 1, 0); assert np.allclose(Tb[-1, -1], 10)
# không bị chặn: max x₁ + x₂ s.t. x₁ − x₂ ≤ 3 (bài tập 1, 3)
U0 = tableau(np.array([[1., -1, 1]]), np.array([3.]), np.array([-1., -1, 0])); ju, ru, _ = choose(U0); assert (ju, ru) == (0, 0)
U1 = pivot(U0, 0, 0); jv, rv, ratv = choose(U1); assert jv == 1 and rv is None and U1[0, 1] < 0

def fm(v):
    if abs(v - round(v)) < 1e-9: s = "%d" % round(v)
    else: s = nf(v, 1)
    return s.replace("-", "−")

class Simplex(Reel):
    def table(self, T, B, ratios=None, names=NAMES, cols=None, y=-1.25):
        hdr = [L("cơ sở", "basis")[LANG]] + names + ["b̄"] + ([L("tỉ số", "ratio")[LANG]] if ratios is not None else [])
        nr = len(T); ncol = len(hdr); xs = np.linspace(-3.5, 3.5, ncol) if ncol > 6 else np.linspace(-3.2, 2.6, ncol)
        g = VGroup(); cells = {}
        for k, h in enumerate(hdr):
            t = Text(h, font=MONO, font_size=22, color=DIM).move_to([xs[k], y + 0.95, 0]); g.add(t)
        for i in range(nr):
            yy = y + 0.35 - 0.55 * i - (0.15 if i == nr - 1 else 0)
            lab = names[B[i]] if i < nr - 1 else "c̄"
            row = [lab] + [fm(v) for v in T[i, :-1]] + [fm(T[i, -1])]
            if ratios is not None: row.append(("∞" if not np.isfinite(ratios[i]) else fm(ratios[i])) if i < nr - 1 else "")
            for k, s in enumerate(row):
                col = SUN if i == nr - 1 and k > 0 else (SKY if k == 0 else WHITE)
                t = Text(s, font=MONO, font_size=24, color=col).move_to([xs[k], yy, 0]); g.add(t); cells[(i, k)] = t
        ln = Line([xs[0] - 0.6, y + 0.65, 0], [xs[-1] + 0.6, y + 0.65, 0], color=DIM, stroke_width=1.5)
        ln2 = Line([xs[0] - 0.6, y + 0.35 - 0.55 * (nr - 1) + 0.25, 0], [xs[-1] + 0.6, y + 0.35 - 0.55 * (nr - 1) + 0.25, 0], color=DIM, stroke_width=1.5)
        g.add(ln, ln2); g.cells = cells; g.xs = xs
        return g

    def construct(self):
        self.title(L("Thuật toán simplex:\nđi từ đỉnh sang đỉnh", "The simplex method:\nwalking from vertex to vertex"))
        self.stage(1)
        ax = mkaxes([0, 4.6], [0, 4.6], 3.9, 3.9, [0.2, 2.45, 0], xt=(), yt=[])
        ax, lab = ax; self.play(Create(ax), FadeIn(lab), run_time=0.5)
        xl = Text("x₁", font=FONT, font_size=22, color=DIM).next_to(ax.c2p(4.6, 0), RIGHT, buff=0.08); yl = Text("x₂", font=FONT, font_size=22, color=DIM).next_to(ax.c2p(0, 4.6), UP, buff=0.08)
        self.add(xl, yl)
        self.say(L("Ví dụ của bài 05-01-01: tối đa hóa 3x₁ + 2x₂ với x₁ + x₂ ≤ 4, 2x₁ + x₂ ≤ 6, x₁, x₂ ≥ 0.",
                   "The example from lesson 05-01-01: maximize 3x₁ + 2x₂ subject to x₁ + x₂ ≤ 4, 2x₁ + x₂ ≤ 6, x₁, x₂ ≥ 0."), hold=6.0)
        c1 = Line(ax.c2p(0, 4), ax.c2p(4, 0), color=SKY, stroke_width=3); c2 = Line(ax.c2p(0.7, 4.6), ax.c2p(3, 0), color=PINK, stroke_width=3)
        l1 = Text("x₁ + x₂ = 4", font=MONO, font_size=18, color=SKY).next_to(ax.c2p(3.6, 0.4), UR, buff=0.05)
        l2 = Text("2x₁ + x₂ = 6", font=MONO, font_size=18, color=PINK).next_to(ax.c2p(0.9, 4.2), RIGHT, buff=0.1)
        self.play(Create(c1), Create(c2), FadeIn(l1), FadeIn(l2), run_time=0.8)
        poly = Polygon(*[ax.c2p(*v) for v in VERT], color=MINT, fill_color=MINT, fill_opacity=0.18, stroke_width=3)
        self.play(FadeIn(poly), run_time=0.6)
        vd = VGroup(*[Dot(ax.c2p(*v), radius=0.09, color=WHITE) for v in VERT])
        vl = VGroup(*[Text(("(%d; %d) → %d" if LANG == "vi" else "(%d, %d) → %d") % (v[0], v[1], val), font=MONO, font_size=18, color=WHITE) for v, val in zip(VERT, VAL)])
        for t, v, dr in zip(vl, VERT, (DL, DOWN, UR, LEFT)):
            t.next_to(ax.c2p(*v), dr, buff=0.12)
        vl[0].shift(RIGHT * 0.3); vl[3].shift(RIGHT * 0.05)
        self.play(FadeIn(vd), FadeIn(vl), run_time=0.6)
        self.say(L("Miền khả thi là đa giác xanh, có 4 đỉnh. Giá trị 3x₁ + 2x₂ tại các đỉnh: 0, 9, 10, 8.",
                   "The feasible set is the green polygon with 4 vertices. The values of 3x₁ + 2x₂ at the vertices: 0, 9, 10, 8."), hold=5.5)
        lv = VGroup()
        for val in (3, 6, 9, 10):
            p, q = (val / 3, 0), (0, val / 2)
            lv.add(DashedLine(ax.c2p(*p), ax.c2p(*q), color=SUN if val == 10 else DIM, stroke_width=2.5))
        for m in lv: self.play(Create(m), run_time=0.45)
        self.say(L("Các đường mức 3x₁ + 2x₂ = 3, 6, 9, 10 song song. Đường cuối cùng còn chạm đa giác là ở đỉnh (2; 2), giá trị 10.",
                   "The level lines 3x₁ + 2x₂ = 3, 6, 9, 10 are parallel. The last one that still touches the polygon touches at the vertex (2, 2), value 10."), hold=6.5)
        self.say(L("Đây là sự thật hình học của LP: nếu có nghiệm tối ưu hữu hạn thì có một nghiệm tại đỉnh. Simplex chỉ đi qua các đỉnh.",
                   "This is the geometric fact behind LP: if a finite optimum exists, one is attained at a vertex. Simplex only visits vertices."), hold=6.5)
        self.play(FadeOut(lv), run_time=0.3)
        # ---- stage 2
        self.stage(2)
        self.readout(["x₁ +  x₂ + s₁      = 4", "2x₁ + x₂      + s₂ = 6", "x₁, x₂, s₁, s₂ ≥ 0"], color=WHITE, size=23, y=-1.2)
        self.say(L("Thêm biến bù s₁, s₂ ≥ 0 để biến bất đẳng thức thành đẳng thức. s₁ là phần còn dư của ràng buộc thứ nhất.",
                   "Add slack variables s₁, s₂ ≥ 0 to turn the inequalities into equalities. s₁ is how much room is left in the first constraint."), hold=6.5)
        zs = [L("x₁ = x₂ = 0", "x₁ = x₂ = 0"), L("x₂ = s₂ = 0", "x₂ = s₂ = 0"), L("s₁ = s₂ = 0", "s₁ = s₂ = 0"), L("x₁ = s₁ = 0", "x₁ = s₁ = 0")]
        self.readout([("đỉnh (0; 0):  x₁ = x₂ = 0" if LANG == "vi" else "vertex (0, 0):  x₁ = x₂ = 0", WHITE), ("đỉnh (3; 0):  x₂ = s₂ = 0" if LANG == "vi" else "vertex (3, 0):  x₂ = s₂ = 0", WHITE), ("đỉnh (2; 2):  s₁ = s₂ = 0" if LANG == "vi" else "vertex (2, 2):  s₁ = s₂ = 0", WHITE), ("đỉnh (0; 4):  x₁ = s₁ = 0" if LANG == "vi" else "vertex (0, 4):  x₁ = s₁ = 0", WHITE)], size=22, y=-1.3)
        self.say(L("Mỗi đỉnh là nơi đúng 2 trong 4 biến bằng 0 (biến ngoài cơ sở). 2 biến còn lại là biến cơ sở, giải ra từ hai phương trình.",
                   "Each vertex is where exactly 2 of the 4 variables are 0 (the nonbasic ones). The other 2 are basic, solved from the two equations."), hold=7.0)
        self.say(L("Đi sang đỉnh kề = đổi một biến: một biến ngoài cơ sở được tăng lên (biến vào), một biến cơ sở giảm về 0 (biến ra). Đó là một bước xoay (pivot).",
                   "Moving to a neighboring vertex = swapping one variable: a nonbasic variable is increased (entering), a basic one drops to 0 (leaving). That is a pivot."), hold=7.5)
        self.say(L("Chọn biến vào nhờ chi phí rút gọn c̄: mục tiêu (dạng min −3x₁ − 2x₂) thay đổi bao nhiêu khi biến đó tăng 1. c̄ < 0 nghĩa là còn cải thiện được.",
                   "The entering variable is picked by its reduced cost c̄: how much the objective (as min −3x₁ − 2x₂) changes when that variable grows by 1. c̄ < 0 means we can still improve."), hold=8.0)
        # ---- stage 3
        self.stage(3); self.clear_ro()
        self.play(FadeOut(VGroup(l1, l2)), run_time=0.3)
        cur = Dot(ax.c2p(0, 0), radius=0.15, color=SUN); self.add(cur)
        tb = self.table(T0, B0); self.play(FadeIn(tb), run_time=0.5)
        self.say(L("Bảng simplex tại gốc (0; 0): cơ sở là s₁, s₂. Hàng c̄ = (−3; −2; 0; 0), giá trị mục tiêu hiện tại 0.",
                   "The simplex tableau at the origin (0, 0): the basis is s₁, s₂. Row c̄ = (−3, −2, 0, 0), current objective value 0."), hold=6.5)
        # pivot 1
        tbr = self.table(T0, B0, ratios=rat1); self.remove(tb); self.add(tbr)
        hc = SurroundingRectangle(VGroup(*[tbr.cells[(i, 1 + j1)] for i in range(3)]), color=SUN, buff=0.12)
        self.play(Create(hc), run_time=0.4)
        self.say(L("c̄ âm nhất là −3, ở cột x₁: x₁ vào cơ sở. Tăng x₁ là đi dọc trục x₁.",
                   "The most negative c̄ is −3, in column x₁: x₁ enters. Increasing x₁ means walking along the x₁ axis."), hold=5.5)
        hr = SurroundingRectangle(VGroup(*[tbr.cells[(r1, k)] for k in range(7)]), color=PINK, buff=0.1)
        self.play(Create(hr), run_time=0.4)
        self.say(L("Kiểm định tỉ số: 4/1 = 4 và 6/2 = 3. Lấy tỉ số nhỏ nhất, 3, ở hàng s₂: s₂ rời cơ sở. Đi xa hơn 3 thì vi phạm 2x₁ + x₂ ≤ 6.",
                   "Ratio test: 4/1 = 4 and 6/2 = 3. Take the smallest ratio, 3, in row s₂: s₂ leaves. Going beyond 3 would violate 2x₁ + x₂ ≤ 6."), hold=7.5)
        pc = Circle(radius=0.28, color=ORANGE, stroke_width=4).move_to(tbr.cells[(r1, 1 + j1)])
        self.play(Create(pc), run_time=0.3)
        edge1 = Line(ax.c2p(0, 0), ax.c2p(3, 0), color=SUN, stroke_width=6)
        tb1 = self.table(T1, B1)
        self.play(FadeOut(VGroup(hc, hr, pc)), ReplacementTransform(tbr, tb1), Create(edge1), cur.animate.move_to(ax.c2p(3, 0)), run_time=1.4)
        self.say(L("Xoay quanh phần tử 2: chia hàng cho 2, khử x₁ ở các hàng khác. Ta tới đỉnh (3; 0), giá trị 9.",
                   "Pivot on the entry 2: divide the row by 2, eliminate x₁ from the other rows. We reach the vertex (3, 0), value 9."), hold=6.0)
        # pivot 2
        tbr2 = self.table(T1, B1, ratios=rat2); self.remove(tb1); self.add(tbr2)
        hc = SurroundingRectangle(VGroup(*[tbr2.cells[(i, 1 + j2)] for i in range(3)]), color=SUN, buff=0.12)
        self.play(Create(hc), run_time=0.4)
        self.say(L("Hàng c̄ còn một số âm: −0,5 ở cột x₂. x₂ vào: đi lên dọc cạnh 2x₁ + x₂ = 6.",
                   "Row c̄ still has a negative entry: −0.5 in column x₂. x₂ enters: walk up along the edge 2x₁ + x₂ = 6."), hold=5.5)
        hr = SurroundingRectangle(VGroup(*[tbr2.cells[(r2, k)] for k in range(7)]), color=PINK, buff=0.1)
        self.play(Create(hr), run_time=0.4)
        self.say(L("Tỉ số: 1/0,5 = 2 và 3/0,5 = 6. Nhỏ nhất là 2, hàng s₁: s₁ rời cơ sở.",
                   "Ratios: 1/0.5 = 2 and 3/0.5 = 6. The smallest is 2, row s₁: s₁ leaves."), hold=5.0)
        pc = Circle(radius=0.32, color=ORANGE, stroke_width=4).move_to(tbr2.cells[(r2, 1 + j2)])
        self.play(Create(pc), run_time=0.3)
        edge2 = Line(ax.c2p(3, 0), ax.c2p(2, 2), color=SUN, stroke_width=6)
        tb2 = self.table(T2, B2)
        self.play(FadeOut(VGroup(hc, hr, pc)), ReplacementTransform(tbr2, tb2), Create(edge2), cur.animate.move_to(ax.c2p(2, 2)), run_time=1.4)
        self.say(L("Tới đỉnh (2; 2), giá trị 10. Hàng c̄ = (0; 0; 1; 1) không còn số âm: không biến nào tăng lên mà cải thiện được. Tối ưu.",
                   "We reach the vertex (2, 2), value 10. Row c̄ = (0, 0, 1, 1) has no negative entry: no variable can grow and improve. Optimal."), hold=7.5)
        self.readout([("y = c̄ của (s₁; s₂) = (1; 1)" if LANG == "vi" else "y = c̄ of (s₁, s₂) = (1, 1)", MINT), ("bᵀy = 4·1 + 6·1 = 10 = 3·2 + 2·2" if LANG == "vi" else "bᵀy = 4·1 + 6·1 = 10 = 3·2 + 2·2", MINT)], size=23)
        self.say(L("Bonus: c̄ của hai biến bù, y = (1; 1), là nghiệm đối ngẫu. bᵀy = 10 đúng bằng giá trị tối ưu: chứng chỉ tối ưu.",
                   "Bonus: the c̄ of the two slacks, y = (1, 1), is the dual solution. bᵀy = 10 equals the optimal value: a certificate of optimality."), hold=7.0)
        # ---- stage 4
        self.stage(4); self.clear_ro()
        alt = VGroup(Line(ax.c2p(0, 0), ax.c2p(0, 4), color=PINK, stroke_width=5), Line(ax.c2p(0, 4), ax.c2p(2, 2), color=PINK, stroke_width=5))
        self.play(Create(alt), run_time=1.0)
        self.readout([("lối 1: (0; 0) → (3; 0) → (2; 2):  0 → 9 → 10" if LANG == "vi" else "path 1: (0, 0) → (3, 0) → (2, 2):  0 → 9 → 10", SUN), ("lối 2: (0; 0) → (0; 4) → (2; 2):  0 → 8 → 10" if LANG == "vi" else "path 2: (0, 0) → (0, 4) → (2, 2):  0 → 8 → 10", PINK)], size=22)
        self.say(L("Nếu cho x₂ vào trước, simplex đi lối kia: (0; 0) → (0; 4) → (2; 2). Cũng 2 bước xoay, cùng đích. Quy tắc chọn biến vào chỉ đổi lộ trình.",
                   "If x₂ enters first, simplex takes the other way: (0, 0) → (0, 4) → (2, 2). Also 2 pivots, same destination. The entering rule only changes the route."), hold=7.5)
        self.wipe(); self.stage(4)
        ux = plain_axes([0, 6], [0, 3.5], 5.6, 3.4, [0, 2.3, 0])
        reg = Polygon(ux.c2p(0, 0), ux.c2p(3, 0), ux.c2p(6, 3), ux.c2p(6, 3.5), ux.c2p(0, 3.5), color=MINT, fill_color=MINT, fill_opacity=0.15, stroke_width=0)
        bl = Line(ux.c2p(3, 0), ux.c2p(6, 3), color=SKY, stroke_width=3)
        self.play(Create(ux), FadeIn(reg), Create(bl), run_time=0.7)
        self.say(L("Một trường hợp khác (bài tập 1 và 3): tối đa hóa x₁ + x₂ với x₁ − x₂ ≤ 3, x ≥ 0. Miền khả thi không bị chặn.",
                   "Another case (exercises 1 and 3): maximize x₁ + x₂ with x₁ − x₂ ≤ 3, x ≥ 0. The feasible set is unbounded."), hold=6.0)
        du = Dot(ux.c2p(0, 0), radius=0.13, color=SUN); self.add(du)
        self.play(du.animate.move_to(ux.c2p(3, 0)), Create(Line(ux.c2p(0, 0), ux.c2p(3, 0), color=SUN, stroke_width=5)), run_time=0.8)
        tu = self.table(U1, [0], ratios=[np.inf, 0], names=["x₁", "x₂", "s"], y=-1.35)
        self.add(tu)
        self.say(L("Bước 1: x₁ vào, tới (3; 0). Bước 2: c̄ của x₂ là −2 < 0, x₂ vào. Nhưng cột x₂ chỉ có hệ số −1, không có số dương nào.",
                   "Step 1: x₁ enters, reaching (3, 0). Step 2: the c̄ of x₂ is −2 < 0, so x₂ enters. But column x₂ has only −1, no positive entry."), hold=7.5)
        ray = Arrow(ux.c2p(3, 0), ux.c2p(6, 3), buff=0, color=PINK, stroke_width=6)
        self.play(GrowArrow(ray), run_time=0.8)
        self.say(L("Kiểm định tỉ số không có tỉ số nào (∞): tăng x₂ bao nhiêu cũng khả thi, dọc tia (3 + t; t), và mục tiêu tăng mãi. Simplex báo: không bị chặn.",
                   "The ratio test finds no ratio (∞): x₂ can grow forever along the ray (3 + t, t), and the objective grows without bound. Simplex reports: unbounded."), hold=8.0)
        self.takeaway([L("LP có nghiệm tối ưu hữu hạn thì có nghiệm tại một đỉnh của miền khả thi.", "If an LP has a finite optimum, one is at a vertex of the feasible set."),
                       L("Mỗi đỉnh = một nghiệm cơ sở. Một bước xoay = đổi một biến vào, một biến ra, sang đỉnh kề.", "Each vertex = a basic solution. A pivot = one variable in, one out: move to a neighbor."),
                       L("Biến vào: c̄ âm. Biến ra: tỉ số nhỏ nhất. Dừng khi c̄ ≥ 0: ở đây (2; 2), giá trị 10.", "Entering: negative c̄. Leaving: smallest ratio. Stop when c̄ ≥ 0: here (2, 2), value 10."),
                       L("Không có tỉ số dương nào: bài toán không bị chặn.", "No positive ratio at all: the problem is unbounded.")])
