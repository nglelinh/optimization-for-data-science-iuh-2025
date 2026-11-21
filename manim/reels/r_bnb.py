from rl import *
from o3lib import bnb, lp_solve, ILP_ROWS, hull
NODES, BEST, BX = bnb(); assert len(NODES) == 5 and BEST == 20 and BX == (4, 0)
LATT = [(i, j) for i in range(9) for j in range(9) if 6 * i + 4 * j <= 24 and i + 2 * j <= 6]
assert max(5 * i + 4 * j for i, j in LATT) == 20 and len(LATT) == 13
R0 = lp_solve(ILP_ROWS); assert abs(R0[0] - 21) < 1e-9 and np.allclose(R0[1], (3, 1.5))
assert 6 * 3 + 4 * 2 > 24 and 5 * 3 + 4 * 1 == 19
def stxt(n):
    st = n["st"]
    return {"branch": L("phân nhánh", "branch"), "integer": L("nguyên", "integer"), "pruned": L("cắt tỉa", "pruned"), "infeasible": L("vô nghiệm", "infeasible")}[st]

class Bnb(Reel):
    def construct(self):
        self.title(L("Nhánh và cận:\ngiải bài toán nguyên bằng LP", "Branch and bound:\ninteger programs via LPs"))
        self.stage(1)
        ax = plain_axes([0, 5.2], [0, 3.6], 7.2, 3.6, [0, 2.75, 0], ticks=True)
        P = lambda p: ax.c2p(p[0], p[1])
        poly = Polygon(*[P(v) for v in hull(R0[2])], color=SKY, stroke_width=3, fill_color=SKY, fill_opacity=0.15)
        dots = VGroup(*[Dot(P(q), radius=0.06, color=WHITE) for q in LATT])
        self.play(Create(ax), FadeIn(poly), FadeIn(dots), run_time=0.8)
        self.say(L("Tối đa 5x₁ + 4x₂ với 6x₁ + 4x₂ ≤ 24, x₁ + 2x₂ ≤ 6, x ≥ 0 và x NGUYÊN (chấm trắng).",
                   "Maximize 5x₁ + 4x₂ with 6x₁ + 4x₂ ≤ 24, x₁ + 2x₂ ≤ 6, x ≥ 0, and x INTEGER (white dots)."), hold=5.0)
        rd = Dot(P(R0[1]), radius=0.12, color=SUN); self.play(FadeIn(rd), run_time=0.3)
        self.readout(["LP nới lỏng: x = (3; 1,5), giá trị 21" if LANG == "vi" else "LP relaxation: x = (3, 1.5), value 21"], color=SUN, size=24, y=0.55)
        self.say(L("Bỏ điều kiện nguyên thì là LP: nghiệm (3; 1,5), giá trị 21. Đó là một cận trên, nhưng x₂ không nguyên.",
                   "Drop integrality and it is an LP: solution (3, 1.5), value 21. That is an upper bound, but x₂ is fractional."), hold=5.0)
        # key idea
        self.stage(2)
        self.say(L("Phân nhánh: x₂ ≤ 1 hoặc x₂ ≥ 2 — không nghiệm nguyên nào bị mất, nhưng điểm (3; 1,5) bị loại.",
                   "Branch: x₂ ≤ 1 or x₂ ≥ 2 — no integer point is lost, but (3, 1.5) is cut out."), hold=5.0)
        self.say(L("Cận: giá trị LP của một nút là trần cho mọi nghiệm nguyên trong nút đó. Trần ≤ nghiệm tốt nhất đã có thì bỏ cả nút.",
                   "Bound: a node's LP value caps every integer solution inside it. If the cap ≤ the best found so far, discard the node."), hold=5.5)
        # algorithm: tree
        self.stage(3); self.clear_ro()
        pos = {0: (0, 0.2), 1: (-1.8, -1.15), 4: (1.8, -1.15), 2: (-2.9, -2.5), 3: (-0.7, -2.5)}
        col = {"branch": SUN, "integer": MINT, "pruned": PINK, "infeasible": DIM}
        gm = {}; rmob = VGroup(); self.add(rmob)
        for n in NODES:
            i = n["id"]; x, y = pos[i]; v, xx, verts = n["lp"]
            box = RoundedRectangle(corner_radius=0.12, width=2.2, height=0.95, stroke_color=col[n["st"]], stroke_width=3, fill_color=CARD, fill_opacity=1).move_to([x, y, 0])
            t1 = Text("%s" % (n["label"].replace(">=", "≥").replace("<=", "≤").replace("x1", "x₁").replace("x2", "x₂") if n["label"] != "root" else tr(L("gốc", "root"))), font=FONT, font_size=19, color=WHITE)
            t2 = Text("LP = %s" % nf(v, 2), font=MONO, font_size=18, color=col[n["st"]])
            g = VGroup(box, VGroup(t1, t2).arrange(DOWN, buff=0.06).move_to(box)); gm[i] = g
            an = [FadeIn(g, scale=0.9)]
            if n["par"] >= 0: an.append(Create(Line(gm[n["par"]][0].get_bottom(), box.get_top(), color=DIM, stroke_width=2)))
            reg = Polygon(*[P(q) for q in hull(verts)], color=col[n["st"]], stroke_width=3, fill_color=col[n["st"]], fill_opacity=0.25) if len(verts) >= 3 else VGroup()
            an += [Transform(rmob, reg), rd.animate.move_to(P(xx))]
            self.play(*an, run_time=0.8)
            msgs = {0: L("Nút gốc: LP = 21 tại (3; 1,5). Phân nhánh theo x₂.", "Root: LP = 21 at (3, 1.5). Branch on x₂."),
                    1: L("x₂ ≤ 1: LP = 20,67 tại (3,33; 1). x₁ còn lẻ, phân nhánh tiếp theo x₁.", "x₂ ≤ 1: LP = 20.67 at (3.33, 1). x₁ is fractional; branch on x₁."),
                    2: L("x₁ ≤ 3: nghiệm nguyên (3; 1), giá trị 19. Nghiệm tốt nhất tạm thời = 19.", "x₁ ≤ 3: integer solution (3, 1), value 19. Incumbent = 19."),
                    3: L("x₁ ≥ 4: nghiệm nguyên (4; 0), giá trị 20 > 19. Nghiệm tốt nhất mới = 20.", "x₁ ≥ 4: integer solution (4, 0), value 20 > 19. New incumbent = 20."),
                    4: L("x₂ ≥ 2: LP chỉ được 18 ≤ 20. Cắt tỉa: không cần xét gì bên trong nút này.", "x₂ ≥ 2: the LP gives only 18 ≤ 20. Pruned: nothing inside needs to be explored.")}
            self.readout(["%s   %s" % (tr(stxt(n)), ("tốt nhất = %s" % nf(n["best"], 0) if LANG == "vi" else "best = %s" % nf(n["best"], 0)) if n["best"] > -1e17 else "")], color=col[n["st"]], size=23, y=-3.25)
            self.say(msgs[i], hold=4.2)
        self.say(L("Xong sau 5 LP: tối ưu nguyên là (4; 0) với giá trị 20.", "Done after 5 LPs: the integer optimum is (4, 0) with value 20."))
        # contrast
        self.stage(4)
        self.play(Transform(rmob, VGroup()), rd.animate.move_to(P(R0[1])), run_time=0.5)
        bad1 = Dot(P((3, 2)), radius=0.12, color=PINK); bad2 = Dot(P((3, 1)), radius=0.12, color=ORANGE)
        self.play(FadeIn(bad1), FadeIn(bad2), run_time=0.4)
        self.readout([("làm tròn lên (3; 2): 6·3 + 4·2 = 26 > 24  ✗" if LANG == "vi" else "round up (3, 2): 6·3 + 4·2 = 26 > 24  ✗", PINK), ("làm tròn xuống (3; 1): giá trị 19 < 20" if LANG == "vi" else "round down (3, 1): value 19 < 20", ORANGE)], size=22, y=-3.45)
        self.say(L("Làm tròn nghiệm LP không đủ: làm tròn lên thì vi phạm ràng buộc, làm tròn xuống thì được 19, kém tối ưu.",
                   "Rounding the LP answer is not enough: rounding up is infeasible, rounding down gives 19, not optimal."), hold=5.5)
        self.say(L("Duyệt hết cũng được ở đây (13 điểm nguyên), nhưng số điểm tăng theo hàm mũ với số biến; nhánh cận cắt bỏ phần lớn.",
                   "Brute force works here (13 integer points), but their number grows exponentially with the dimension; B&B prunes most of them."), hold=6.0)
        self.takeaway([L("LP nới lỏng cho cận trên; nghiệm nguyên tìm được cho cận dưới.", "The LP relaxation gives an upper bound; integer solutions give lower bounds."),
                       L("Phân nhánh trên biến lẻ; cắt tỉa nút có cận ≤ nghiệm tốt nhất.", "Branch on a fractional variable; prune nodes whose bound ≤ the incumbent."),
                       L("Làm tròn nghiệm LP có thể sai hoặc vô nghiệm.", "Rounding the LP solution can be wrong or infeasible.")])
