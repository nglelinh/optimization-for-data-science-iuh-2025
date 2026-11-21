from rl import *
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

class Cut(Reel):
    def construct(self):
        self.title(L("Mặt cắt Gomory: gọt dần\nđiểm phân số", "Gomory cuts: shaving off\nthe fractional point"))
        self.stage(1)
        ax = plain_axes([0, 5.2], [0, 3.6], 7.4, 5.2, [0, 1.75, 0], ticks=True); P = lambda p: ax.c2p(p[0], p[1])
        poly = Polygon(*[P(v) for v in hull(RD[0]['lp'][2])], color=SKY, stroke_width=3, fill_color=SKY, fill_opacity=0.15)
        dots = VGroup(*[Dot(P(q), radius=0.07, color=WHITE) for q in LATT])
        self.play(Create(ax), FadeIn(poly), FadeIn(dots), run_time=0.8)
        self.say(L("Cùng bài nguyên: tối đa 5x₁ + 4x₂ trên đa giác, chỉ lấy điểm nguyên. LP nới lỏng cho (3; 1,5), giá trị 21.",
                   "The same integer program: maximize 5x₁ + 4x₂ over the polygon, integer points only. The LP relaxation gives (3, 1.5), value 21."), hold=5.5)
        d = Dot(P(RD[0]['lp'][1]), radius=0.13, color=SUN); self.play(FadeIn(d), run_time=0.3)
        # key idea
        self.stage(2)
        ih = Polygon(*[P(q) for q in IH], color=MINT, stroke_width=3).set_fill(opacity=0)
        ih = DashedVMobject(ih, num_dashes=60)
        self.play(Create(ih), run_time=1.0)
        self.say(L("Đường đứt xanh: bao lồi các điểm nguyên. Trên đó, LP cho luôn nghiệm nguyên. Mục tiêu: tiến về nó.",
                   "Dashed green: the convex hull of the integer points. Over it, the LP answer is integer. Goal: move toward it."), hold=5.0)
        self.say(L("Một mặt cắt là bất đẳng thức mới: mọi điểm nguyên vẫn thoả, nhưng đỉnh LP hiện tại bị loại.",
                   "A cut is a new inequality: every integer point still satisfies it, but the current LP vertex violates it."), hold=5.0)
        self.say(L("Gomory đọc nó ra từ bảng đơn hình: lấy phần lẻ của các hệ số rồi làm tròn xuống.", "Gomory reads it off the simplex tableau: take fractional parts of the coefficients and round down."))
        # algorithm
        self.stage(3)
        cur = poly
        for k in range(1, 5):
            c = RD[k]['cut']; r = RD[k]['lp']
            # clip the line c0*x + c1*y = c2 to the plot box [0, 5.2] x [0, 3.6]
            cand = []
            for xb in (0.0, 5.2):
                if abs(c[1]) > 1e-12:
                    yb = (c[2] - c[0] * xb) / c[1]
                    if 0 <= yb <= 3.2: cand.append((xb, yb))
            for yb in (0.0, 3.2):
                if abs(c[0]) > 1e-12:
                    xb = (c[2] - c[1] * yb) / c[0]
                    if 0 <= xb <= 5.2: cand.append((xb, yb))
            cand = sorted(set((round(a, 9), round(b_, 9)) for a, b_ in cand))
            assert len(cand) >= 2
            pts = [cand[0], cand[-1]]
            cl = Line(P(pts[0]), P(pts[1]), color=PINK, stroke_width=4)
            self.play(Create(cl), run_time=0.6)
            newp = Polygon(*[P(v) for v in hull(r[2])], color=SKY, stroke_width=3, fill_color=SKY, fill_opacity=0.15)
            self.play(Transform(cur, newp), d.animate.move_to(P(r[1])), cl.animate.set_stroke(opacity=0.35, width=2.5), run_time=0.9)
            ok = sum(1 for i, j in LATT if c[0] * i + c[1] * j <= c[2])
            self.readout(["mặt cắt %d:  %dx₁ + %dx₂ ≤ %d" % (k, c[0], c[1], c[2]) if LANG == "vi" else "cut %d:  %dx₁ + %dx₂ ≤ %d" % (k, c[0], c[1], c[2]),
                          ("giữ %d/%d điểm nguyên ✓" % (ok, len(LATT)) if LANG == "vi" else "keeps %d/%d integer points ✓" % (ok, len(LATT)), MINT),
                          ("LP = %s tại %s" % (nf(r[0], 3), vec(r[1], 3)) if LANG == "vi" else "LP = %s at %s" % (nf(r[0], 3), vec(r[1], 3)), SUN)], color=PINK, size=23, y=-3.0)
            self.wait(2.2)
        self.say(L("Sau 4 mặt cắt, đỉnh LP là (4; 0), nguyên. Giá trị 21 → 20,67 → 20,6 → 20,4 → 20: đó là tối ưu nguyên.",
                   "After 4 cuts the LP vertex is (4, 0), integral. Value 21 → 20.67 → 20.6 → 20.4 → 20: the integer optimum."), hold=6.0)
        # contrast
        self.stage(4)
        nodes, best, bx = bnb(); assert bx == (4, 0)
        self.readout([("mặt cắt:      4 lần thêm ràng buộc, 5 LP" if LANG == "vi" else "cutting planes: 4 cuts, 5 LPs", PINK), ("nhánh và cận: %d nút, %d LP" % (len(nodes), len(nodes)) if LANG == "vi" else "branch & bound: %d nodes, %d LPs" % (len(nodes), len(nodes)), SKY)], size=24, y=-3.0)
        self.say(L("Nhánh cận chia nhỏ vùng; mặt cắt làm chặt vùng. Ở bài nhỏ này hai cách tốn ngang nhau.", "Branch and bound splits the region; cuts tighten it. On this small problem the costs are similar."), hold=4.5)
        self.say(L("Mặt cắt thuần thường chậm dần (mỗi lần gọt một chút) — nên các bộ giải hiện đại kết hợp cả hai: branch-and-cut.",
                   "Pure cutting often stalls (each cut shaves a little) — so modern solvers combine both: branch-and-cut."), hold=5.5)
        self.takeaway([L("Mặt cắt hợp lệ: giữ mọi điểm nguyên, loại đỉnh LP lẻ.", "A valid cut keeps every integer point and removes the fractional LP vertex."),
                       L("Thêm mặt cắt và giải lại LP cho tới khi nghiệm nguyên: ở đây 4 lần.", "Add cuts and re-solve until the LP answer is integral: 4 rounds here."),
                       L("Trong thực tế: kết hợp với nhánh cận (branch-and-cut).", "In practice: combine with branching (branch-and-cut).")])
