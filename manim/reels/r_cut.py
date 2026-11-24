from rl import *
# Bài 25-01-03: lát cắt phân số Gomory, suy ra đầy đủ từ một hàng của bảng đơn hình
from o3lib import cuts, lp_solve, ILP_ROWS, hull, bnb
RD = cuts(); assert len(RD) == 5 and RD[-1]['lp'][0] == 20 and abs(RD[-1]['lp'][1][0] - 4) < 1e-9
LATT = [(i, j) for i in range(12) for j in range(12) if 6 * i + 4 * j <= 24 and i + 2 * j <= 6]
for rd in RD[1:]:
    c = rd['cut']; assert all(c[0] * i + c[1] * j <= c[2] for i, j in LATT)
    x = rd['lp'][1]
VALS = [r['lp'][0] for r in RD]; assert all(VALS[i + 1] <= VALS[i] for i in range(4))
for k in range(1, 5):
    c = RD[k]['cut']; xp = RD[k - 1]['lp'][1]; assert c[0] * xp[0] + c[1] * xp[1] > c[2] + 1e-9
def ihull():
    pts = [p for p in LATT]
    pts = sorted(set(pts)); 
    def cross(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, up = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0: lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0: up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]
IH = ihull()

# bảng đơn hình tối ưu: cơ sở {x₁, x₂}, biến bù s₁, s₂ (nguyên vì dữ liệu nguyên)
BM = np.array([[6, 4], [1, 2.]]); BI = np.linalg.inv(BM)
assert np.allclose(BI, [[0.25, -0.5], [-0.125, 0.75]]) and np.allclose(BI @ [24, 6], [3, 1.5])
ROW = (BI[1, 0], BI[1, 1], (BI @ [24, 6])[1])                       # x₂ − 0,125 s₁ + 0,75 s₂ = 1,5
fr = lambda v: v - np.floor(v + 1e-12)
FR = tuple(fr(v) for v in ROW); assert np.allclose(FR, (0.875, 0.75, 0.5))
# 0,875 s₁ + 0,75 s₂ ≥ 0,5 với s₁ = 24 − 6x₁ − 4x₂, s₂ = 6 − x₁ − 2x₂  ⇒  6x₁ + 5x₂ ≤ 25
cx1 = FR[0] * 6 + FR[1] * 1; cx2 = FR[0] * 4 + FR[1] * 2; cr = FR[0] * 24 + FR[1] * 6 - FR[2]
assert np.allclose((cx1, cx2, cr), (6, 5, 25)) and tuple(RD[1]['cut']) == (6, 5, 25)
assert 6 * 3 + 5 * 1.5 == 25.5 and max(6 * i + 5 * j for i, j in LATT) == 24
for i, j in LATT:   # lát cắt dạng s đúng với mọi điểm nguyên; vế trái hàng x₂ − s₁ − 1 là số nguyên
    s1, s2 = 24 - 6 * i - 4 * j, 6 - i - 2 * j; assert FR[0] * s1 + FR[1] * s2 >= FR[2] - 1e-12 and float(j - s1 - 1).is_integer()
assert np.isclose(FR[0] * 0 + FR[1] * 0, 0) and 0 < FR[2]            # tại đỉnh LP (s = 0) lát cắt bị vi phạm
NL = len(LATT); assert NL == 13
VI = LANG == "vi"
CUTW = "lát cắt" if VI else "cut"

class Cut(Reel):
    def construct(self):
        self.title(L("Lát cắt Gomory: gọt dần\nđiểm phân số", "Gomory cuts: shaving off\nthe fractional point"))
        # ---- stage 1
        self.stage(1)
        ax = plain_axes([0, 5.2], [0, 3.6], 7.4, 5.2, [0, 1.75, 0], ticks=True); P = lambda p: ax.c2p(p[0], p[1])
        poly = Polygon(*[P(v) for v in hull(RD[0]['lp'][2])], color=SKY, stroke_width=3, fill_color=SKY, fill_opacity=0.15)
        dots = VGroup(*[Dot(P(q), radius=0.07, color=WHITE) for q in LATT])
        self.play(Create(ax), FadeIn(poly), FadeIn(dots), run_time=0.8)
        self.readout(["max 5x₁ + 4x₂", "6x₁ + 4x₂ ≤ 24,   x₁ + 2x₂ ≤ 6", ("x ≥ 0, x nguyên" if VI else "x ≥ 0, x integer", DIM)], color=WHITE, size=24, y=-3.0)
        self.say(L("Bài quy hoạch nguyên: tối đa 5x₁ + 4x₂ trên đa giác xanh, nhưng chỉ được lấy %d điểm nguyên màu trắng." % NL,
                   "An integer program: maximize 5x₁ + 4x₂ over the blue polygon, but only the %d white integer points are allowed." % NL), hold=8.5)
        d = Dot(P(RD[0]['lp'][1]), radius=0.13, color=SUN); self.play(FadeIn(d), run_time=0.3)
        self.readout([("LP nới lỏng: x = (3; 1,5), giá trị 21" if VI else "LP relaxation: x = (3, 1.5), value 21", SUN), ("x₂ = 1,5 không nguyên" if VI else "x₂ = 1.5 is not integer", PINK)], size=24, y=-3.0)
        self.say(L("Bỏ điều kiện nguyên thì LP cho đỉnh vàng (3; 1,5), giá trị 21. Đẹp nhưng vô dụng: x₂ không nguyên.",
                   "Drop integrality and the LP returns the yellow vertex (3, 1.5), value 21. Nice, but useless: x₂ is not integer."), hold=8.0)
        # ---- stage 2
        self.stage(2); self.clear_ro()
        ih = Polygon(*[P(q) for q in IH], color=MINT, stroke_width=3).set_fill(opacity=0)
        ih = DashedVMobject(ih, num_dashes=60)
        self.play(Create(ih), run_time=1.0)
        self.say(L("Đường đứt xanh lá: bao lồi của các điểm nguyên. Nếu LP chạy trên vùng đó thì đỉnh tối ưu tự nhiên là điểm nguyên. Mục tiêu: gọt đa giác dần về phía nó.",
                   "Dashed green: the convex hull of the integer points. An LP over that region lands on an integer vertex by itself. Goal: shave the polygon toward it."), hold=10.0)
        self.say(L("Một lát cắt hợp lệ là bất đẳng thức mới: mọi điểm nguyên vẫn thoả, nhưng đỉnh LP hiện tại thì bị loại.",
                   "A valid cut is a new inequality: every integer point still satisfies it, but the current LP vertex does not."), hold=8.0)
        self.readout([("a ≤ b  và  a nguyên  ⇒  a ≤ ⌊b⌋" if VI else "a ≤ b  and  a integer  ⇒  a ≤ ⌊b⌋", SUN)], size=26, y=-3.0)
        self.say(L("Gomory dựa vào một nhận xét rất sơ cấp trong bài: nếu a ≤ b và a là số nguyên thì a ≤ ⌊b⌋. Làm tròn xuống vế phải vẫn đúng.",
                   "Gomory builds on a very elementary remark in the lesson: if a ≤ b and a is an integer, then a ≤ ⌊b⌋. Rounding the right side down stays valid."), hold=9.5)
        # ---- stage 3: suy ra lát cắt đầu tiên
        self.stage(3)
        self.readout(["6x₁ + 4x₂ + s₁ = 24", "x₁ + 2x₂ + s₂ = 6", ("s₁, s₂ ≥ 0 và nguyên" if VI else "s₁, s₂ ≥ 0 and integer", DIM)], color=WHITE, size=24, y=-3.0)
        self.say(L("Thêm biến bù s₁, s₂ để có đẳng thức. Hệ số và vế phải đều nguyên, nên khi x nguyên thì s cũng nguyên.",
                   "Add slack variables s₁, s₂ to get equalities. The coefficients and right sides are integers, so integer x gives integer s."), hold=8.5)
        self.readout([("bảng đơn hình tối ưu (cơ sở x₁, x₂):" if VI else "optimal simplex tableau (basis x₁, x₂):", DIM), "x₁ + %s s₁ − %s s₂ = 3" % (nf(0.25), nf(0.5, 1)), ("x₂ − %s s₁ + %s s₂ = %s" % (nf(0.125, 3), nf(0.75), nf(1.5, 1)), SUN)], color=WHITE, size=24, y=-3.0)
        self.say(L("Ở đỉnh tối ưu, simplex cho hai hàng này: s₁ = s₂ = 0 thì đọc ra x₁ = 3, x₂ = 1,5. Hàng của x₁ có vế phải nguyên, nên ta dùng hàng của x₂.",
                   "At the optimal vertex, simplex gives these two rows: with s₁ = s₂ = 0 they read x₁ = 3, x₂ = 1.5. The x₁ row has an integer right side, so we use the x₂ row."), hold=11.0)
        self.readout(["−%s = −1 + %s" % (nf(0.125, 3), nf(0.875, 3)), "%s = 0 + %s     %s = 1 + %s" % (nf(0.75), nf(0.75), nf(1.5, 1), nf(0.5, 1)), ("x₂ − s₁ − 1 = %s − %s s₁ − %s s₂" % (nf(0.5, 1), nf(0.875, 3), nf(0.75)), SUN)], color=WHITE, size=24, y=-3.0)
        self.say(L("Tách mỗi hệ số thành phần nguyên cộng phần lẻ: −0,125 = −1 + 0,875; 0,75 = 0 + 0,75; 1,5 = 1 + 0,5. Dồn phần nguyên sang trái, phần lẻ sang phải.",
                   "Split each coefficient into an integer part plus a fractional part: −0.125 = −1 + 0.875; 0.75 = 0 + 0.75; 1.5 = 1 + 0.5. Integer parts go left, fractional parts right."), hold=11.0)
        self.readout([("vế trái: số nguyên" if VI else "left side: an integer", WHITE), ("vế phải ≤ %s < 1  ⇒  vế phải ≤ 0" % nf(0.5, 1) if VI else "right side ≤ %s < 1  ⇒  right side ≤ 0" % nf(0.5, 1), WHITE), ("⇒  %s s₁ + %s s₂ ≥ %s" % (nf(0.875, 3), nf(0.75), nf(0.5, 1)), PINK)], size=25, y=-3.0)
        self.say(L("Vế trái là số nguyên. Vế phải thì không vượt quá 0,5 vì s ≥ 0. Một số nguyên ≤ 0,5 phải ≤ 0. Ta được lát cắt Gomory: 0,875s₁ + 0,75s₂ ≥ 0,5, đúng công thức của bài.",
                   "The left side is an integer. The right side is at most 0.5 because s ≥ 0. An integer ≤ 0.5 must be ≤ 0. That gives the Gomory cut 0.875s₁ + 0.75s₂ ≥ 0.5, exactly the lesson's formula."), hold=12.5)
        self.readout(["%s s₁ + %s s₂ ≥ %s" % (nf(0.875, 3), nf(0.75), nf(0.5, 1)), ("s₁ = 24 − 6x₁ − 4x₂", DIM), ("s₂ = 6 − x₁ − 2x₂", DIM), "⇔  %s − 6x₁ − 5x₂ ≥ %s" % (nf(25.5, 1), nf(0.5, 1)), ("⇔  6x₁ + 5x₂ ≤ 25", PINK)], color=WHITE, size=23, y=-3.0)
        c = RD[1]['cut']
        def cline(c):
            cand = []
            for xb in (0.0, 5.2):
                if abs(c[1]) > 1e-12:
                    yb = (c[2] - c[0] * xb) / c[1]
                    if 0 <= yb <= 3.2: cand.append((xb, yb))
            for yb in (0.0, 3.2):
                if abs(c[0]) > 1e-12:
                    xb = (c[2] - c[1] * yb) / c[0]
                    if 0 <= xb <= 5.2: cand.append((xb, yb))
            cand = sorted(set((round(a, 9), round(b_, 9)) for a, b_ in cand)); assert len(cand) >= 2
            return Line(P(cand[0]), P(cand[-1]), color=PINK, stroke_width=4)
        cl = cline(c); self.play(Create(cl), run_time=0.8)
        self.say(L("Thay s₁ = 24 − 6x₁ − 4x₂ và s₂ = 6 − x₁ − 2x₂ vào, rút gọn: 6x₁ + 5x₂ ≤ 25. Đó là đường hồng trên hình.",
                   "Substitute s₁ = 24 − 6x₁ − 4x₂ and s₂ = 6 − x₁ − 2x₂ and simplify: 6x₁ + 5x₂ ≤ 25. That is the pink line."), hold=9.5)
        self.readout([("(3; 1,5): 6·3 + 5·1,5 = 25,5 > 25  ✗" if VI else "(3, 1.5): 6·3 + 5·1.5 = 25.5 > 25  ✗", PINK), ("điểm nguyên: max 6x₁ + 5x₂ = 24 ≤ 25" if VI else "integer points: max 6x₁ + 5x₂ = 24 ≤ 25", MINT), ("giữ %d/%d điểm nguyên  ✓" % (NL, NL) if VI else "keeps %d/%d integer points  ✓" % (NL, NL), MINT)], size=24, y=-3.0)
        self.say(L("Kiểm tra: đỉnh (3; 1,5) cho 25,5 > 25, bị loại. Mọi điểm nguyên cho nhiều nhất 24, nên cả %d điểm đều còn nguyên vẹn." % NL,
                   "Check: the vertex (3, 1.5) gives 25.5 > 25, so it is removed. Every integer point gives at most 24, so all %d survive." % NL), hold=9.5)
        cur = poly
        for k in range(1, 5):
            c = RD[k]['cut']; r = RD[k]['lp']
            if k > 1:
                cl = cline(c); self.play(Create(cl), run_time=0.6)
            newp = Polygon(*[P(v) for v in hull(r[2])], color=SKY, stroke_width=3, fill_color=SKY, fill_opacity=0.15)
            self.play(Transform(cur, newp), d.animate.move_to(P(r[1])), cl.animate.set_stroke(opacity=0.35, width=2.5), run_time=0.9)
            ok = sum(1 for i, j in LATT if c[0] * i + c[1] * j <= c[2])
            self.readout(["%s %d:  %dx₁ + %dx₂ ≤ %d" % (CUTW, k, c[0], c[1], c[2]),
                          ("giữ %d/%d điểm nguyên ✓" % (ok, NL) if VI else "keeps %d/%d integer points ✓" % (ok, NL), MINT),
                          ("LP = %s tại %s" % (nf(r[0], 3), vec(r[1], 3)) if VI else "LP = %s at %s" % (nf(r[0], 3), vec(r[1], 3)), SUN)], color=PINK, size=23, y=-3.0)
            if k == 1:
                self.say(L("Giải lại LP với lát cắt mới: đỉnh dời tới (3,33; 1), giá trị 20,67. Vẫn lẻ, nên lặp lại đúng quy trình trên với bảng mới.",
                           "Re-solve the LP with the new cut: the vertex moves to (3.33, 1), value 20.67. Still fractional, so repeat the same recipe on the new tableau."), hold=9.0)
            else: self.wait(2.6)
        self.say(L("Sau 4 lát cắt, đỉnh LP là (4; 0), nguyên. Giá trị 21 → 20,67 → 20,6 → 20,4 → 20: đó là tối ưu nguyên.",
                   "After 4 cuts the LP vertex is (4, 0), integral. Value 21 → 20.67 → 20.6 → 20.4 → 20: the integer optimum."), hold=9.0)
        # ---- stage 4
        self.stage(4)
        nodes, best, bx = bnb(); assert bx == (4, 0)
        self.readout([("lát cắt:      4 lần thêm ràng buộc, 5 LP" if VI else "cutting planes: 4 cuts, 5 LPs", PINK), ("nhánh và cận: %d nút, %d LP" % (len(nodes), len(nodes)) if VI else "branch & bound: %d nodes, %d LPs" % (len(nodes), len(nodes)), SKY)], size=24, y=-3.0)
        self.say(L("Nhánh và cận chia nhỏ vùng; lát cắt làm chặt vùng. Ở bài nhỏ này hai cách tốn ngang nhau: 5 lần giải LP.",
                   "Branch and bound splits the region; cuts tighten it. On this small problem the costs are similar: 5 LP solves each."), hold=8.0)
        self.say(L("Giá trị LP chỉ giảm từng chút một: 0,33 rồi 0,07 rồi 0,2. Lát cắt thuần thường chậm dần như vậy, nên các bộ giải hiện đại kết hợp cả hai: branch-and-cut.",
                   "The LP value drops only a little each time: 0.33, then 0.07, then 0.2. Pure cutting often stalls like this, so modern solvers combine both: branch-and-cut."), hold=10.5)
        self.takeaway([L("Lát cắt hợp lệ: giữ mọi điểm nguyên, loại đỉnh LP lẻ.", "A valid cut keeps every integer point and removes the fractional LP vertex."),
                       L("Công thức: từ hàng có vế phải lẻ, Σ phần lẻ(aⱼ)·xⱼ ≥ phần lẻ(a₀).", "Recipe: from a row with fractional right side, Σ frac(aⱼ)·xⱼ ≥ frac(a₀)."),
                       L("Ở đây hàng của x₂ cho 6x₁ + 5x₂ ≤ 25; 4 lát cắt thì tới (4; 0).", "Here the x₂ row gives 6x₁ + 5x₂ ≤ 25; 4 cuts reach (4, 0)."),
                       L("Trong thực tế: kết hợp với nhánh cận (branch-and-cut).", "In practice: combine with branching (branch-and-cut).")], tail=4.0)
