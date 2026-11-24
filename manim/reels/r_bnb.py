from rl import *
import itertools, math
from o3lib import hull
# Bài 24-05: nhánh và cận trên một bài nguyên đầy đủ: phân nhánh, cắt tỉa theo cận và theo vô nghiệm
CC = (5, 4); ROWS = [(2, 1, 8), (2, 3, 11), (-1, 0, 0), (0, -1, 0)]          # max 5x₁ + 4x₂, 2x₁ + x₂ ≤ 8, 2x₁ + 3x₂ ≤ 11, x ≥ 0
def lp(rows):
    best = None; bx = None; V = []
    for a, b in itertools.combinations(rows, 2):
        det = a[0] * b[1] - a[1] * b[0]
        if abs(det) < 1e-12: continue
        x = ((a[2] * b[1] - a[1] * b[2]) / det, (a[0] * b[2] - a[2] * b[0]) / det)
        if all(r[0] * x[0] + r[1] * x[1] <= r[2] + 1e-9 for r in rows):
            V.append(x); v = CC[0] * x[0] + CC[1] * x[1]
            if best is None or v > best + 1e-12: best, bx = v, x
    return None if best is None else (best, bx, V)
def bnb():
    nodes = []; best = -1e18; bx = None; stack = [(ROWS, 'root', -1)]
    while stack:
        rows, lab, par = stack.pop(); r = lp(rows); rec = dict(rows=rows, label=lab, lp=r, par=par, id=len(nodes), inc=best)
        if r is None: rec['st'] = 'infeasible'
        elif r[0] <= best + 1e-9: rec['st'] = 'pruned'
        else:
            fr = [i for i in (0, 1) if abs(r[1][i] - round(r[1][i])) > 1e-6]
            if not fr:
                rec['st'] = 'integer'
                if r[0] > best: best = r[0]; bx = tuple(round(v) for v in r[1])
            else:
                i = max(fr, key=lambda i: -abs(r[1][i] - math.floor(r[1][i]) - 0.5)); f = math.floor(r[1][i] + 1e-9); rec['st'] = 'branch'; rec['var'] = i
                dn = [0, 0, 0]; up = [0, 0, 0]; dn[i] = 1; dn[2] = f; up[i] = -1; up[2] = -(f + 1)
                stack.append((rows + [tuple(up)], 'x%d >= %d' % (i + 1, f + 1), rec['id'])); stack.append((rows + [tuple(dn)], 'x%d <= %d' % (i + 1, f), rec['id']))
        rec['best'] = best; nodes.append(rec)
    return nodes, best, bx
NODES, BEST, BX = bnb()
ST = [n['st'] for n in NODES]; LB_ = [n['label'] for n in NODES]
assert ST == ['branch', 'branch', 'integer', 'integer', 'branch', 'pruned', 'infeasible'] and BEST == 20 and BX == (4, 0)
assert LB_ == ['root', 'x2 <= 1', 'x1 <= 3', 'x1 >= 4', 'x2 >= 2', 'x1 <= 2', 'x1 >= 3']
V_ = [n['lp'][0] if n['lp'] else None for n in NODES]; X_ = [n['lp'][1] if n['lp'] else None for n in NODES]
assert np.allclose(V_[:6], [22.25, 21.5, 19, 20, 20.5, 58 / 3]) and np.allclose(X_[0], (3.25, 1.5)) and np.allclose(X_[1], (3.5, 1)) and np.allclose(X_[4], (2.5, 2)) and np.allclose(X_[5], (2, 7 / 3))
assert 2 * 3 + 3 * 2 > 11                                                 # x₁ ≥ 3, x₂ ≥ 2 mâu thuẫn với 2x₁ + 3x₂ ≤ 11
LATT = [(i, j) for i in range(9) for j in range(9) if 2 * i + j <= 8 and 2 * i + 3 * j <= 11]
assert len(LATT) == 14 and max(CC[0] * i + CC[1] * j for i, j in LATT) == 20 and [p for p in LATT if 5 * p[0] + 4 * p[1] == 20] == [(4, 0)]
assert 2 * 3 + 3 * 2 > 11 and 5 * 3 + 4 * 1 == 19                          # làm tròn (3,25; 1,5): lên (3; 2) vô nghiệm, xuống (3; 1) chỉ 19
VI = LANG == "vi"
def stxt(n):
    return {"branch": L("phân nhánh", "branch"), "integer": L("nguyên", "integer"), "pruned": L("cắt tỉa theo cận", "pruned by bound"), "infeasible": L("vô nghiệm, cắt tỉa", "infeasible, pruned")}[n["st"]]
def lab(s):
    return tr(L("gốc", "root")) if s == "root" else s.replace(">=", "≥").replace("<=", "≤").replace("x1", "x₁").replace("x2", "x₂")

class Bnb(Reel):
    def construct(self):
        self.title(L("Nhánh và cận:\ngiải bài toán nguyên bằng LP", "Branch and bound:\ninteger programs via LPs"))
        # ---- stage 1
        self.stage(1)
        ax = plain_axes([0, 4.6], [0, 3.9], 6.6, 3.5, [0, 2.75, 0], ticks=True)
        P = lambda p: ax.c2p(p[0], p[1])
        R0 = NODES[0]['lp']
        poly = Polygon(*[P(v) for v in hull(R0[2])], color=SKY, stroke_width=3, fill_color=SKY, fill_opacity=0.15)
        dots = VGroup(*[Dot(P(q), radius=0.06, color=WHITE) for q in LATT])
        self.play(Create(ax), FadeIn(poly), FadeIn(dots), run_time=0.8)
        self.readout(["max 5x₁ + 4x₂", "2x₁ + x₂ ≤ 8,   2x₁ + 3x₂ ≤ 11", ("x ≥ 0, x nguyên" if VI else "x ≥ 0, x integer", DIM)], color=WHITE, size=24, y=-0.4)
        self.say(L("Tối đa 5x₁ + 4x₂ với 2x₁ + x₂ ≤ 8, 2x₁ + 3x₂ ≤ 11, x ≥ 0 và x NGUYÊN: chỉ được chọn 14 chấm trắng.",
                   "Maximize 5x₁ + 4x₂ with 2x₁ + x₂ ≤ 8, 2x₁ + 3x₂ ≤ 11, x ≥ 0, and x INTEGER: only the 14 white dots are allowed."), hold=8.5)
        rd = Dot(P(R0[1]), radius=0.12, color=SUN); self.play(FadeIn(rd), run_time=0.3)
        self.readout([("LP nới lỏng: x = (3,25; 1,5), giá trị 22,25" if VI else "LP relaxation: x = (3.25, 1.5), value 22.25", SUN), ("cả hai toạ độ đều lẻ" if VI else "both coordinates are fractional", PINK)], size=24, y=-0.4)
        self.say(L("Bỏ điều kiện nguyên thì là LP: nghiệm (3,25; 1,5), giá trị 22,25. Vì LP có nhiều lựa chọn hơn, 22,25 là cận trên cho mọi nghiệm nguyên.",
                   "Drop integrality and it is an LP: solution (3.25, 1.5), value 22.25. The LP has more freedom, so 22.25 is an upper bound on every integer solution."), hold=9.5)
        # ---- stage 2
        self.stage(2)
        self.readout([("x₂ ≤ 1   hoặc   x₂ ≥ 2" if VI else "x₂ ≤ 1   or   x₂ ≥ 2", SUN), ("dải 1 < x₂ < 2 bị bỏ: không có điểm nguyên" if VI else "the strip 1 < x₂ < 2 is dropped: no integer points", DIM)], size=24, y=-0.4)
        strip = Polygon(P((0, 1)), P((4.6, 1)), P((4.6, 2)), P((0, 2)), stroke_width=0, fill_color=PINK, fill_opacity=0.18)
        self.play(FadeIn(strip), run_time=0.4)
        self.say(L("Phân nhánh trên biến lẻ nhất, x₂ = 1,5: chia thành x₂ ≤ 1 hoặc x₂ ≥ 2. Không mất điểm nguyên nào, nhưng điểm (3,25; 1,5) bị loại.",
                   "Branch on the most fractional variable, x₂ = 1.5: split into x₂ ≤ 1 or x₂ ≥ 2. No integer point is lost, but (3.25, 1.5) is cut out."), hold=9.5)
        self.play(FadeOut(strip), run_time=0.3)
        self.readout([("cắt tỉa nút khi:" if VI else "prune a node when:", WHITE), ("• LP vô nghiệm" if VI else "• its LP is infeasible", DIM), ("• cận LP ≤ nghiệm tốt nhất đã có" if VI else "• its LP bound ≤ the incumbent", PINK), ("• LP đã cho nghiệm nguyên" if VI else "• its LP answer is already integer", MINT)], size=24, y=-0.4)
        self.say(L("Cận: giá trị LP của một nút là trần cho mọi nghiệm nguyên bên trong nút đó. Trần không vượt nghiệm tốt nhất đã có thì bỏ cả nút.",
                   "Bound: a node's LP value caps every integer solution inside that node. If the cap does not beat the incumbent, discard the whole node."), hold=9.0)
        self.say(L("Bài 24-05 viết cho bài cực tiểu: nới lỏng cho cận dưới, nghiệm khả thi cho cận trên. Ở đây ta cực đại, nên hai vai đổi chỗ.",
                   "Lesson 24-05 is written for minimization: the relaxation gives a lower bound, feasible points give upper bounds. Here we maximize, so the roles swap."), hold=9.0)
        # ---- stage 3: cây
        self.stage(3); self.clear_ro()
        pos = {0: (0, 0.35), 1: (-1.95, -0.95), 4: (1.95, -0.95), 2: (-2.95, -2.25), 3: (-0.95, -2.25), 5: (0.95, -2.25), 6: (2.95, -2.25)}
        col = {"branch": SUN, "integer": MINT, "pruned": PINK, "infeasible": DIM}
        gm = {}; rmob = VGroup(); self.add(rmob)
        msgs = {0: L("Nút gốc: LP = 22,25 tại (3,25; 1,5). Phân nhánh theo x₂.", "Root: LP = 22.25 at (3.25, 1.5). Branch on x₂."),
                1: L("Nhánh x₂ ≤ 1: LP = 21,5 tại (3,5; 1). x₁ còn lẻ, phân nhánh tiếp theo x₁: x₁ ≤ 3 hoặc x₁ ≥ 4.", "Branch x₂ ≤ 1: LP = 21.5 at (3.5, 1). x₁ is fractional; branch on x₁: x₁ ≤ 3 or x₁ ≥ 4."),
                2: L("x₁ ≤ 3: LP cho luôn điểm nguyên (3; 1), giá trị 19. Nghiệm tốt nhất tạm thời = 19.", "x₁ ≤ 3: the LP lands on the integer point (3, 1), value 19. Incumbent = 19."),
                3: L("x₁ ≥ 4: nghiệm nguyên (4; 0), giá trị 20 > 19. Nghiệm tốt nhất mới = 20.", "x₁ ≥ 4: integer solution (4, 0), value 20 > 19. New incumbent = 20."),
                4: L("Quay lại nhánh x₂ ≥ 2: LP = 20,5 tại (2,5; 2). 20,5 > 20 nên chưa bỏ được, phải phân nhánh theo x₁.", "Back to the branch x₂ ≥ 2: LP = 20.5 at (2.5, 2). 20.5 > 20, so it cannot be dropped yet; branch on x₁."),
                5: L("x₁ ≤ 2: LP = 19,33 tại (2; 2,33). Vẫn lẻ, nhưng 19,33 ≤ 20: không điểm nguyên nào ở đây thắng được 20. Cắt tỉa theo cận.", "x₁ ≤ 2: LP = 19.33 at (2, 2.33). Still fractional, but 19.33 ≤ 20: nothing in here can beat 20. Pruned by bound."),
                6: L("x₁ ≥ 3 cùng với x₂ ≥ 2: 2·3 + 3·2 = 12 > 11. Vùng rỗng, LP vô nghiệm. Cắt tỉa theo vô nghiệm.", "x₁ ≥ 3 together with x₂ ≥ 2: 2·3 + 3·2 = 12 > 11. The region is empty, the LP is infeasible. Pruned by infeasibility.")}
        holds = {0: 6.0, 1: 9.0, 2: 7.5, 3: 7.0, 4: 9.5, 5: 10.5, 6: 10.0}
        for n in NODES:
            i = n["id"]; x, y = pos[i]
            box = RoundedRectangle(corner_radius=0.12, width=1.85, height=0.95, stroke_color=col[n["st"]], stroke_width=3, fill_color=CARD, fill_opacity=1).move_to([x, y, 0])
            t1 = Text(lab(n["label"]), font=FONT, font_size=19, color=WHITE)
            t2 = Text(("LP = %s" % nf(n["lp"][0], 2)) if n["lp"] else tr(L("vô nghiệm", "infeasible")), font=MONO, font_size=17, color=col[n["st"]])
            g = VGroup(box, VGroup(t1, t2).arrange(DOWN, buff=0.06).move_to(box)); gm[i] = g
            an = [FadeIn(g, scale=0.9)]
            if n["par"] >= 0: an.append(Create(Line(gm[n["par"]][0].get_bottom(), box.get_top(), color=DIM, stroke_width=2)))
            if n["lp"]:
                verts = n["lp"][2]
                reg = Polygon(*[P(q) for q in hull(verts)], color=col[n["st"]], stroke_width=3, fill_color=col[n["st"]], fill_opacity=0.25) if len(verts) >= 3 else Line(P(verts[0]), P(verts[-1]), color=col[n["st"]], stroke_width=6)
                an += [Transform(rmob, reg), rd.animate.move_to(P(n["lp"][1])).set_opacity(1)]
            else:
                an += [Transform(rmob, VGroup()), rd.animate.set_opacity(0)]
            self.play(*an, run_time=0.8)
            self.readout(["%s   %s" % (tr(stxt(n)), ("tốt nhất = %s" % nf(n["best"], 0) if VI else "best = %s" % nf(n["best"], 0)) if n["best"] > -1e17 else "")], color=col[n["st"]], size=23, y=-3.3)
            self.say(msgs[i], hold=holds[i])
        self.say(L("Xong sau 7 LP, không còn nút nào mở: tối ưu nguyên là (4; 0) với giá trị 20. Cận trên cuối cùng cũng là 20, nên chắc chắn tối ưu.",
                   "Done after 7 LPs with no open node left: the integer optimum is (4, 0) with value 20. The final upper bound is also 20, so optimality is certain."), hold=9.5)
        # ---- stage 4
        self.stage(4)
        self.play(Transform(rmob, VGroup()), rd.animate.move_to(P(R0[1])).set_opacity(1), run_time=0.5)
        bad1 = Dot(P((3, 2)), radius=0.12, color=PINK); bad2 = Dot(P((3, 1)), radius=0.12, color=ORANGE)
        self.play(FadeIn(bad1), FadeIn(bad2), run_time=0.4)
        self.readout([("làm tròn (3; 2): 2·3 + 3·2 = 12 > 11  ✗" if VI else "round to (3, 2): 2·3 + 3·2 = 12 > 11  ✗", PINK), ("làm tròn xuống (3; 1): 19 < 20" if VI else "round down (3, 1): 19 < 20", ORANGE)], size=23, y=-3.3)
        self.say(L("Làm tròn nghiệm LP không đủ: làm tròn x₂ lên thì vi phạm ràng buộc, làm tròn xuống cả hai thì được 19, kém tối ưu.",
                   "Rounding the LP answer is not enough: rounding x₂ up breaks a constraint, rounding both down gives 19, not optimal."), hold=9.0)
        self.readout([("khoảng cách nguyên: 22,25 − 20 = 2,25" if VI else "integrality gap: 22.25 − 20 = 2.25", SUN), ("duyệt hết: 14 điểm; B&B: 7 LP" if VI else "brute force: 14 points; B&B: 7 LPs", SKY)], size=23, y=-3.3)
        self.say(L("Khoảng cách giữa LP gốc và tối ưu nguyên là 2,25: cận ban đầu khá lỏng, và cây phải đi sâu hai tầng để khép lại.",
                   "The gap between the root LP and the integer optimum is 2.25: the first bound is loose, and the tree has to go two levels deep to close it."), hold=9.0)
        self.say(L("Duyệt hết cũng được ở đây (14 điểm), nhưng số điểm tăng theo hàm mũ với số biến. Nhánh cận nhờ cận và vô nghiệm mà bỏ được cả vùng một lúc.",
                   "Brute force works here (14 points), but their number grows exponentially with the dimension. Branch and bound drops whole regions at once thanks to bounds and infeasibility."), hold=10.0)
        self.takeaway([L("LP nới lỏng cho cận trên; nghiệm nguyên tìm được cho cận dưới (bài cực đại).", "The LP relaxation gives an upper bound; integer solutions give lower bounds (maximization)."),
                       L("Phân nhánh trên biến lẻ: xⱼ ≤ ⌊xⱼ*⌋ hoặc xⱼ ≥ ⌈xⱼ*⌉.", "Branch on a fractional variable: xⱼ ≤ ⌊xⱼ*⌋ or xⱼ ≥ ⌈xⱼ*⌉."),
                       L("Cắt tỉa khi: LP vô nghiệm, cận ≤ nghiệm tốt nhất, hoặc LP đã nguyên.", "Prune when the LP is infeasible, its bound ≤ the incumbent, or it is already integer."),
                       L("Làm tròn nghiệm LP có thể sai hoặc vô nghiệm.", "Rounding the LP solution can be wrong or infeasible.")], tail=4.0)
