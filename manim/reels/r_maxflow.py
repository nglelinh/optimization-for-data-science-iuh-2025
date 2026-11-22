from rl import *
import itertools
# Bài 10-03: luồng cực đại và lát cắt cực tiểu, mạng nhỏ 6 đỉnh
V = ["s", "a", "b", "c", "d", "t"]
CAP = {("s", "a"): 3, ("s", "b"): 4, ("a", "b"): 4, ("a", "c"): 2, ("b", "d"): 3, ("c", "t"): 3, ("d", "t"): 4}
E = list(CAP)
def resid(fl):
    R = {}
    for e in E:
        i, j = e; R[(i, j)] = R.get((i, j), 0) + CAP[e] - fl[e]; R[(j, i)] = R.get((j, i), 0) + fl[e]
    return R
def push(fl, path, amt):
    fl = dict(fl)
    for u, v in zip(path, path[1:]):
        if (u, v) in CAP: fl[(u, v)] += amt
        else: fl[(v, u)] -= amt
    return fl
def bottleneck(fl, path):
    R = resid(fl); return min(R[(u, v)] for u, v in zip(path, path[1:]))
def reach(fl, forward_only=False):
    R = resid(fl); S_ = {"s"}; ch = True
    while ch:
        ch = False
        for (u, v), c in R.items():
            if forward_only and (u, v) not in CAP: continue
            if u in S_ and v not in S_ and c > 0: S_.add(v); ch = True
    return S_
def value(fl): return sum(f for (i, j), f in fl.items() if i == "s") - sum(f for (i, j), f in fl.items() if j == "s")
def check(fl):
    assert all(0 <= fl[e] <= CAP[e] for e in E)
    for k in "abcd": assert sum(f for (i, j), f in fl.items() if j == k) == sum(f for (i, j), f in fl.items() if i == k)
F0 = {e: 0 for e in E}
P1 = ["s", "a", "b", "d", "t"]; B1 = bottleneck(F0, P1); F1 = push(F0, P1, B1); check(F1)
assert B1 == 3 and value(F1) == 3
assert "t" not in reach(F1, forward_only=True) and reach(F1, forward_only=True) == {"s", "b"}   # chỉ đi xuôi: kẹt ở 3
P2 = ["s", "b", "a", "c", "t"]; B2 = bottleneck(F1, P2); F2 = push(F1, P2, B2); check(F2)
assert B2 == 2 and value(F2) == 5 and resid(F1)[("b", "a")] == 3
AS = reach(F2); assert AS == {"s", "a", "b"} and "t" not in AS
CUTS = []
for r in range(5):
    for S_ in itertools.combinations("abcd", r):
        A_ = {"s", *S_}; CUTS.append((sum(c for (i, j), c in CAP.items() if i in A_ and j not in A_), "".join(sorted(A_, key=V.index))))
CUTS.sort(); assert CUTS[0] == (5, "sab") and CUTS[1][0] > 5 and len(CUTS) == 16
CUTV = {nm: v for v, nm in CUTS}; assert CUTV["s"] == 7 and CUTV["sa"] == 10 and CUTV["sb"] == 6 and CUTV["sabcd"] == 7
CE = [e for e in E if e[0] in AS and e[1] not in AS]; assert CE == [("a", "c"), ("b", "d")] and all(F2[e] == CAP[e] for e in CE)
BE = [e for e in E if e[0] not in AS and e[1] in AS]; assert BE == [] 
# đối ngẫu LP: x = 1 trên A, 0 trên B; b_ij = max(0; x_i − x_j)
X = {v: (1 if v in AS else 0) for v in V}; Bd = {e: max(0, X[e[0]] - X[e[1]]) for e in E}
assert all(Bd[e] + X[e[1]] - X[e[0]] >= 0 for e in E) and sum(Bd[e] * CAP[e] for e in E) == value(F2) == 5
assert np.isclose(sum(Bd.values()), 2)

POS = {"s": (-3.3, 2.4), "a": (-1.15, 3.9), "b": (-1.15, 0.9), "c": (1.15, 3.9), "d": (1.15, 0.9), "t": (3.3, 2.4)}
def P(v): return np.array([*POS[v], 0.])

class MaxFlow(Reel):
    def nodes(self, shade=None):
        g = VGroup()
        for v in V:
            c = Circle(radius=0.36, color=WHITE if v in "st" else SKY, stroke_width=3).set_fill("#151a28", 1).move_to(P(v))
            g.add(VGroup(c, Text(v, font=FONT, font_size=26, color=WHITE).move_to(P(v))))
        return g
    def edge(self, i, j, lab, col, dashed=False, off=0.0, lab_side=1):
        a, b = P(i), P(j); d = (b - a) / np.linalg.norm(b - a); nrm = np.array([-d[1], d[0], 0])
        a2, b2 = a + nrm * off, b + nrm * off
        ar = Arrow(a2, b2, buff=0.42, stroke_width=4, color=col, max_tip_length_to_length_ratio=0.13, max_stroke_width_to_length_ratio=8)
        if dashed: ar = DashedVMobject(ar, num_dashes=12)
        m = (a2 + b2) / 2 + nrm * 0.3 * lab_side
        t = Text(lab, font=MONO, font_size=22, color=col).move_to(m)
        return VGroup(ar, t)
    def flowview(self, fl):
        g = VGroup()
        for (i, j) in E:
            f, c = fl[(i, j)], CAP[(i, j)]
            col = PINK if f == c else (SKY if f > 0 else DIM)
            side = -1 if (i, j) in (("a", "b"),) else 1
            if (i, j) in (("s", "b"), ("b", "d"), ("d", "t")): side = -1
            g.add(self.edge(i, j, "%d/%d" % (f, c), col, lab_side=side))
        return g
    def capview(self):
        g = VGroup()
        for (i, j) in E:
            side = -1 if (i, j) in (("a", "b"), ("s", "b"), ("b", "d"), ("d", "t")) else 1
            g.add(self.edge(i, j, str(CAP[(i, j)]), WHITE, lab_side=side))
        return g
    def residview(self, fl):
        g = VGroup()
        for (i, j) in E:
            f, c = fl[(i, j)], CAP[(i, j)]
            side = -1 if (i, j) in (("a", "b"), ("s", "b"), ("b", "d"), ("d", "t")) else 1
            if c - f > 0: g.add(self.edge(i, j, str(c - f), MINT, off=0.17 * (1 if f > 0 else 0), lab_side=side))
            if f > 0: g.add(self.edge(j, i, str(f), ORANGE, dashed=True, off=0.17, lab_side=side))
        return g
    def hl(self, path, col=SUN):
        return VGroup(*[Line(P(u), P(v), color=col, stroke_width=14, stroke_opacity=0.35) for u, v in zip(path, path[1:])])

    def construct(self):
        self.title(L("Luồng cực đại = lát cắt cực tiểu", "Max flow = min cut"))
        # ---- stage 1
        self.stage(1)
        nd = self.nodes(); cv = self.capview()
        self.play(FadeIn(nd), run_time=0.6); self.play(*[Create(e[0]) for e in cv], *[FadeIn(e[1]) for e in cv], run_time=1.2)
        self.say(L("Mạng có hướng 6 đỉnh. Số trên mỗi cạnh là công suất cᵢⱼ: lượng tối đa chảy qua cạnh đó.",
                   "A directed network with 6 nodes. The number on each edge is its capacity cᵢⱼ: the most that can flow through it."), hold=6.0)
        self.readout(["0 ≤ fᵢⱼ ≤ cᵢⱼ", "vào k = ra k   (k ≠ s, t)" if LANG == "vi" else "in(k) = out(k)   (k ≠ s, t)", "giá trị luồng = tổng ra khỏi s" if LANG == "vi" else "flow value = total out of s"], color=SUN, size=23)
        self.say(L("Luồng f phải nằm trong công suất, và ở mỗi đỉnh giữa lượng vào bằng lượng ra. Bài 10-03: tìm luồng lớn nhất từ s tới t.",
                   "A flow f must stay within capacities, and at every middle node what goes in equals what goes out. Lesson 10-03: find the largest flow from s to t."), hold=7.5)
        self.say(L("Bài 10-03 nhắc tới các ứng dụng: thoát nước đô thị, truyền tải điện, vận chuyển hàng.",
                   "Lesson 10-03 mentions the applications: city drainage, power transmission, shipping goods."), hold=5.0)
        # ---- stage 2
        self.stage(2); self.clear_ro()
        h1 = self.hl(P1); self.play(FadeIn(h1), run_time=0.5)
        self.readout([("đường 1: s → a → b → d → t" if LANG == "vi" else "path 1: s → a → b → d → t", SUN), ("nút cổ chai = min(3; 4; 3; 4) = 3" if LANG == "vi" else "bottleneck = min(3, 4, 3, 4) = 3", SUN)], size=23)
        self.say(L("Đường tăng luồng: một đường từ s tới t còn chỗ. Lượng đẩy được là công suất nhỏ nhất trên đường, ở đây là 3.",
                   "An augmenting path: a path from s to t with room left. The amount we can push is the smallest capacity on it, here 3."), hold=6.5)
        fv1 = self.flowview(F1); self.play(FadeOut(cv), FadeIn(fv1), FadeOut(h1), run_time=0.8)
        self.readout([("giá trị luồng = 3" if LANG == "vi" else "flow value = 3", WHITE)], size=24)
        self.say(L("Nhãn bây giờ là f/c. Cạnh hồng đã đầy: s → a và b → d.",
                   "Labels are now f/c. Pink edges are full: s → a and b → d."), hold=4.5)
        self.say(L("Nếu chỉ đi xuôi chiều cạnh thì kẹt: từ s chỉ tới được b, mà b → d đã đầy. Tham lam dừng ở 3. Nhưng 3 chưa phải cực đại.",
                   "If we only move along edges, we are stuck: from s we only reach b, and b → d is full. Greedy stops at 3. But 3 is not the maximum."), hold=7.5)
        rv1 = self.residview(F1); self.play(FadeOut(fv1), FadeIn(rv1), run_time=0.8)
        self.readout([("xanh: còn trống cᵢⱼ − fᵢⱼ" if LANG == "vi" else "green: room left cᵢⱼ − fᵢⱼ", MINT), ("cam đứt: đi ngược, trả lại fᵢⱼ" if LANG == "vi" else "orange dashed: go back, undo fᵢⱼ", ORANGE)], size=23)
        self.say(L("Đồ thị dư: mỗi cạnh có phần còn trống (xanh), và một cạnh ngược (cam) cho phép rút lại luồng đã đẩy.",
                   "The residual graph: each edge has its room left (green), and a reverse edge (orange) that lets us take back flow already pushed."), hold=7.0)
        h2 = self.hl(P2); self.play(FadeIn(h2), run_time=0.5)
        self.readout([("đường 2: s → b ⇢ a → c → t" if LANG == "vi" else "path 2: s → b ⇢ a → c → t", SUN), ("nút cổ chai = min(4; 3; 2; 3) = 2" if LANG == "vi" else "bottleneck = min(4, 3, 2, 3) = 2", SUN)], size=23)
        self.say(L("Trong đồ thị dư có đường mới: s → b, đi ngược b ⇢ a, rồi a → c → t. Đẩy thêm 2.",
                   "The residual graph has a new path: s → b, back along b ⇢ a, then a → c → t. Push 2 more."), hold=6.0)
        self.say(L("Đi ngược b ⇢ a nghĩa là bớt 2 đơn vị trên a → b. Hai đơn vị đó rời a theo a → c, còn b nhận 2 đơn vị mới từ s.",
                   "Going back b ⇢ a means removing 2 units from a → b. Those 2 units leave a through a → c instead, and b gets 2 new units from s."), hold=8.0)
        # ---- stage 3
        self.stage(3)
        fv2 = self.flowview(F2); self.play(FadeOut(rv1), FadeOut(h2), FadeIn(fv2), run_time=0.8)
        self.readout([("giá trị luồng = 3 + 2 = 5" if LANG == "vi" else "flow value = 3 + 2 = 5", WHITE), ("a: vào 3 = ra 1 + 2,   b: vào 2 + 1 = ra 3" if LANG == "vi" else "a: in 3 = out 1 + 2,   b: in 2 + 1 = out 3", DIM)], size=22)
        self.say(L("Luồng mới: giá trị 5. Kiểm tra cân bằng: ở a vào 3, ra 1 + 2; ở b vào 2 + 1, ra 3.",
                   "The new flow has value 5. Check balance: at a, 3 in and 1 + 2 out; at b, 2 + 1 in and 3 out."), hold=6.5)
        rv2 = self.residview(F2); self.play(FadeOut(fv2), FadeIn(rv2), run_time=0.8)
        sh = RoundedRectangle(corner_radius=0.3, width=3.9, height=4.4, color=SKY, stroke_width=2).set_fill(SKY, 0.10).move_to([-1.9, 2.4, 0])
        self.play(FadeIn(sh), run_time=0.5)
        self.readout([("từ s tới được: A = {s, a, b}" if LANG == "vi" else "reachable from s: A = {s, a, b}", SKY), ("không tới được t ⇒ dừng" if LANG == "vi" else "t is not reachable ⇒ stop", WHITE)], size=23)
        self.say(L("Đồ thị dư mới không còn đường tới t. Các đỉnh tới được từ s là A = {s, a, b} (vùng xanh). Thuật toán dừng.",
                   "The new residual graph has no path to t. The nodes reachable from s are A = {s, a, b} (blue region). The algorithm stops."), hold=7.0)
        self.say(L("Đây là thuật toán Ford–Fulkerson mà bài nhắc tới: tìm đường trong đồ thị dư, đẩy, lặp lại tới khi hết đường. Công suất nguyên nên mỗi lần tăng ít nhất 1, chắc chắn dừng.",
                   "This is the Ford–Fulkerson algorithm the lesson refers to: find a path in the residual graph, push, repeat until no path is left. Capacities are integers, so each push adds at least 1 and it must stop."), hold=8.5)
        self.play(FadeOut(rv2), FadeIn(fv2), run_time=0.6)
        cl = DashedLine([0.5, 4.55, 0], [0.5, 0.1, 0], color=PINK, stroke_width=4); self.play(Create(cl), run_time=0.5)
        self.readout([("lát cắt A → B: a → c (2) + b → d (3) = 5" if LANG == "vi" else "cut A → B: a → c (2) + b → d (3) = 5", PINK), ("cả hai cạnh đều đầy" if LANG == "vi" else "both edges are full", PINK)], size=23)
        self.say(L("Lát cắt (A, B) gồm các cạnh từ A sang B: a → c và b → d. Công suất cắt = 2 + 3 = 5, đúng bằng giá trị luồng. Cả hai cạnh đã đầy.",
                   "The cut (A, B) is the set of edges from A to B: a → c and b → d. Its capacity is 2 + 3 = 5, exactly the flow value. Both edges are full."), hold=8.0)
        self.readout([("{s}: %d    {s, b}: %d    {s, a}: %d" % (CUTV["s"], CUTV["sb"], CUTV["sa"]), WHITE), ("{s, a, b}: %d    {s, a, b, c, d}: %d" % (CUTV["sab"], CUTV["sabcd"]), WHITE), (("16 lát cắt, nhỏ nhất = %d" if LANG == "vi" else "16 cuts, smallest = %d") % CUTS[0][0], PINK)], size=22)
        self.say(L("Mạng này có 16 lát cắt s–t. Kiểm hết: nhỏ nhất là 5, chính là lát cắt vừa tìm.",
                   "This network has 16 s–t cuts. Checking all of them: the smallest is 5, the very cut we just found."), hold=6.0)
        # ---- stage 4
        self.stage(4)
        self.say(L("Vì sao luồng không thể vượt lát cắt? Mọi đơn vị từ s tới t đều phải qua một cạnh từ A sang B. Nên mọi luồng ≤ mọi lát cắt.",
                   "Why can no flow exceed a cut? Every unit from s to t must cross some edge from A to B. So every flow ≤ every cut."), hold=7.5)
        self.readout([("luồng sau đường 1: 3 ≤ 5 ≤ lát cắt {s, b}: %d" % CUTV["sb"] if LANG == "vi" else "flow after path 1: 3 ≤ 5 ≤ cut {s, b}: %d" % CUTV["sb"], WHITE)], size=23)
        self.say(L("Ví dụ: luồng 3 sau đường 1 nhỏ hơn mọi lát cắt, như lát cắt {s, b} có công suất %d. Khi một luồng bằng một lát cắt, cả hai đều tối ưu." % CUTV["sb"],
                   "For example: the flow of 3 after path 1 is below every cut, such as the cut {s, b} with capacity %d. When a flow equals a cut, both are optimal." % CUTV["sb"]), hold=7.0)
        self.play(*[FadeOut(m) for m in (nd, fv2, sh, cl)], run_time=0.5); self.clear_ro()
        lp = VGroup(Text(L("LP luồng cực đại:", "max-flow LP:")[LANG], font=FONT, font_size=24, color=SKY),
                    Text("max Σ fₛⱼ,  0 ≤ f ≤ c,  vào = ra" if LANG == "vi" else "max Σ fₛⱼ,  0 ≤ f ≤ c,  in = out", font=MONO, font_size=21, color=SKY),
                    Text(L("LP đối ngẫu (bài 10-03):", "dual LP (lesson 10-03):")[LANG], font=FONT, font_size=24, color=SUN),
                    Text("min Σ bᵢⱼcᵢⱼ", font=MONO, font_size=21, color=SUN),
                    Text("bᵢⱼ ≥ xᵢ − xⱼ,  b ≥ 0,  xₛ = 1,  xₜ = 0", font=MONO, font_size=21, color=SUN)).arrange(DOWN, aligned_edge=LEFT, buff=0.22).move_to([0, 3.0, 0])
        self.play(FadeIn(lp), run_time=0.7)
        self.say(L("Bài 10-03 viết luồng cực đại thành LP và lấy đối ngẫu: mỗi đỉnh có biến xᵢ, mỗi cạnh có biến bᵢⱼ.",
                   "Lesson 10-03 writes max flow as an LP and takes its dual: a variable xᵢ for each node and bᵢⱼ for each edge."), hold=6.5)
        self.readout([("x = 1 trên A = {s, a, b},  x = 0 trên B" if LANG == "vi" else "x = 1 on A = {s, a, b},  x = 0 on B", WHITE), ("b = 1 trên a → c, b → d; còn lại b = 0" if LANG == "vi" else "b = 1 on a → c, b → d; other b = 0", WHITE), ("Σ bᵢⱼcᵢⱼ = 2 + 3 = 5 = giá trị luồng" if LANG == "vi" else "Σ bᵢⱼcᵢⱼ = 2 + 3 = 5 = flow value", PINK)], size=22, y=-0.6)
        self.say(L("Lấy x = 1 trên A, 0 trên B. Khi đó bᵢⱼ = 1 đúng trên các cạnh cắt, và mục tiêu đối ngẫu bằng công suất cắt: 5. Nghiệm đối ngẫu chính là lát cắt.",
                   "Take x = 1 on A and 0 on B. Then bᵢⱼ = 1 exactly on the cut edges, and the dual objective equals the cut capacity: 5. The dual solution is the cut."), hold=8.5)
        chain = VGroup(Text(L("luồng cực đại ≤ LP đối ngẫu", "max flow ≤ dual LP")[LANG], font=FONT, font_size=23, color=WHITE),
                       Text(L("= lát cắt nới lỏng LP ≤ lát cắt cực tiểu", "= LP-relaxed min cut ≤ min cut")[LANG], font=FONT, font_size=23, color=WHITE),
                       Text(L("ở đây: 5 = 5 = 5 = 5", "here: 5 = 5 = 5 = 5")[LANG], font=FONT, font_size=24, color=MINT)).arrange(DOWN, buff=0.2).move_to([0, -3.3, 0])
        self.play(FadeIn(chain), run_time=0.6)
        self.say(L("Chuỗi bất đẳng thức của bài thành đẳng thức: luồng cực đại = lát cắt cực tiểu. Đó là đối ngẫu mạnh của LP.",
                   "The lesson's chain of inequalities becomes equalities: max flow = min cut. That is LP strong duality."), hold=6.5)
        self.takeaway([L("Đường tăng luồng: đẩy thêm bằng nút cổ chai.", "Augmenting path: push as much as the bottleneck."),
                       L("Cần cạnh ngược trong đồ thị dư; chỉ đi xuôi sẽ kẹt ở 3 thay vì 5.", "Reverse edges in the residual graph are needed; forward-only gets stuck at 3 instead of 5."),
                       L("Hết đường tới t: các đỉnh tới được từ s cho lát cắt cực tiểu.", "No path to t: the nodes reachable from s give a min cut."),
                       L("Luồng cực đại = lát cắt cực tiểu = đối ngẫu LP.", "Max flow = min cut = LP duality.")])
