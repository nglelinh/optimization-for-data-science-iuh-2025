from rl import *
V = np.array([[-1.6, -1.0], [1.7, -0.9], [0.1, 1.8]]); PP = np.array([2.1, 1.0])
f = lambda x: 0.5 * np.sum((x - PP) ** 2)
def proj_tri(p):
    best = None
    for i in range(3):
        a, b = V[i], V[(i + 1) % 3]; t = np.clip((p - a) @ (b - a) / ((b - a) @ (b - a)), 0, 1); q = a + t * (b - a)
        if best is None or np.sum((q - p) ** 2) < np.sum((best - p) ** 2): best = q
    return best
XS = proj_tri(PP); FS = f(XS)
inside = lambda p: all(((V[(i + 1) % 3][0] - V[i][0]) * (p[1] - V[i][1]) - (V[(i + 1) % 3][1] - V[i][1]) * (p[0] - V[i][0])) >= -1e-9 for i in range(3))
assert not inside(PP)
def fw(n, ls=False):
    x = V[0].copy(); xs = [x.copy()]; ss = []; gaps = []
    for k in range(n):
        g = x - PP; s = int(np.argmin(V @ g)); d = V[s] - x; gaps.append(-g @ d); ss.append(s)
        gm = np.clip(-(g @ d) / (d @ d), 0, 1) if ls else 2 / (k + 2)
        x = x + gm * d; xs.append(x.copy())
    return xs, ss, gaps
FX, FSS, FG = fw(2000); LX, LSS, LG = fw(2000, ls=True)
assert all(inside(x) for x in FX[:200]) and all(FG[k] >= f(FX[k]) - FS - 1e-12 for k in range(2000))
Dm = max(np.linalg.norm(V[i] - V[j]) for i in range(3) for j in range(3))
assert all(f(FX[k]) - FS <= 2 * Dm ** 2 / (k + 2) for k in range(1, 2000))
E = {k: f(FX[k]) - FS for k in (10, 100, 1000)}
assert E[1000] < E[100] < E[10]
def pg(n):
    x = V[0].copy(); xs = [x.copy()]
    for _ in range(n): x = proj_tri(x - 1.0 * (x - PP)); xs.append(x.copy())
    return xs
PG = pg(3); assert np.allclose(PG[1], XS)

class FW(Reel):
    def construct(self):
        self.title(L("Frank-Wolfe: tiến về một đỉnh,\nkhông cần phép chiếu", "Frank-Wolfe: step toward a vertex,\nno projection needed"))
        self.stage(1)
        ax = plain_axes([-2.8, 3.2], [-2.2, 2.6], 7.8, 6.24, [0, 1.15, 0])
        P = lambda p: ax.c2p(p[0], p[1])
        tri = Polygon(*[P(v) for v in V], color=SKY, stroke_width=4, fill_color=SKY, fill_opacity=0.12)
        circ = VGroup(*[Circle(radius=r * (ax.c2p(1, 0)[0] - ax.c2p(0, 0)[0]), color="#2c3350", stroke_width=2.5).move_to(P(PP)) for r in (0.5, 1.0, 1.6, 2.3, 2.9)])
        pp = Dot(P(PP), radius=0.12, color=ORANGE)
        self.play(Create(tri), FadeIn(pp), Create(circ), run_time=1.2)
        self.say(L("Tìm điểm trong tam giác gần điểm cam p nhất: min ½‖x − p‖² trên tam giác.", "Find the point of the triangle closest to the orange point p: min ½‖x − p‖² over the triangle."))
        xs = Dot(P(XS), radius=0.1, color=MINT); self.play(FadeIn(xs), run_time=0.3)
        self.readout(["x* = " + vec(XS, 3) + "   (on an edge)" if LANG == "en" else "x* = " + vec(XS, 3) + "   (nằm trên một cạnh)", "f* = " + nf(FS, 4)], color=DIM)
        self.say(L("Đáp số (chấm xanh) nằm trên cạnh phải. Gradient chiếu cần phép chiếu lên tập: với tập phức tạp thì đắt.",
                   "The answer (green) lies on the right edge. Projected gradient needs a projection onto the set: expensive for complicated sets."), hold=5.0)
        # key idea
        self.stage(2)
        self.readout(["sₖ = argmin_{s ∈ tam giác} ⟨∇f(xₖ), s⟩" if LANG == "vi" else "sₖ = argmin_{s ∈ triangle} ⟨∇f(xₖ), s⟩", "xₖ₊₁ = xₖ + γₖ(sₖ − xₖ),  γₖ = 2/(k+2)"], color=SUN, size=23)
        self.say(L("Frank-Wolfe chỉ cần cực tiểu một hàm TUYẾN TÍNH trên tập: đáp số luôn là một đỉnh. Rồi đi một đoạn về đỉnh đó.",
                   "Frank-Wolfe only minimizes a LINEAR function over the set: the answer is always a vertex. Then it moves part way toward it."), hold=5.5)
        # algorithm
        self.stage(3)
        d = Dot(P(FX[0]), radius=0.13, color=SUN); self.add(d)
        segs = []
        for k in range(8):
            x = FX[k]; g = x - PP; s = FSS[k]
            ar = Arrow(P(x), P(x - 0.7 * g / np.linalg.norm(g)), color=PINK, buff=0, stroke_width=5)
            hv = Circle(radius=0.2, color=PINK, stroke_width=4).move_to(P(V[s])); gl = DashedLine(P(x), P(V[s]), color=PINK, stroke_width=2.5)
            self.play(GrowArrow(ar), Create(hv), Create(gl), run_time=0.5 if k else 0.8)
            sg = Line(P(x), P(FX[k + 1]), color=SUN, stroke_width=4); segs.append(sg)
            self.play(Create(sg), d.animate.move_to(P(FX[k + 1])), FadeOut(ar), FadeOut(hv), FadeOut(gl), run_time=0.6)
            self.readout(["k = %d   s = v%d   γ = %s" % (k, s + 1, nf(2 / (k + 2), 3)), "f − f* = %s" % nf(f(FX[k + 1]) - FS, 4), ("FW gap = %s  ≥ f − f*" % nf(FG[k + 1], 4), MINT)], color=SUN, size=23)
            if k == 0:
                self.say(L("Mũi tên hồng: −∇f. Đỉnh được chọn là đỉnh đi xa nhất theo hướng đó.", "Pink arrow: −∇f. The chosen vertex is the one furthest in that direction."), wait=False)
            self.wait(0.5)
        self.say(L("Khoảng cách FW ⟨∇f, x − s⟩ luôn là cận trên của f − f*: một chứng nhận dừng miễn phí.",
                   "The FW gap ⟨∇f, x − s⟩ is always an upper bound on f − f*: a free stopping certificate."), hold=4.5)
        for k in list(range(9, 41)):
            sg = Line(P(FX[k - 1]), P(FX[k]), color=SUN, stroke_width=3); segs.append(sg)
            self.play(Create(sg), d.animate.move_to(P(FX[k])), run_time=0.1, rate_func=linear)
        self.readout([("k      f − f*" , WHITE)] + [("%4d   %s" % (k, sci(E[k])), SUN) for k in (10, 100, 1000)], size=23)
        self.say(L("Gần đáp số trên cạnh, các bước zig-zag giữa các đỉnh: sai số giảm như O(1/k), chậm ở đuôi.",
                   "Near an answer on an edge, the steps zig-zag between vertices: the error falls like O(1/k), a slow tail."), hold=5.0)
        # contrast
        self.stage(4)
        self.play(*[FadeOut(s) for s in segs], FadeOut(d), run_time=0.5)
        d2 = Dot(P(V[0]), radius=0.13, color=PINK); self.play(FadeIn(d2), run_time=0.3)
        mid = V[0] - 1.0 * (V[0] - PP)
        self.play(d2.animate.move_to(P(mid)), run_time=0.7); self.play(d2.animate.move_to(P(PG[1])), run_time=0.7)
        self.say(L("Gradient chiếu với bước 1: nhảy tới p rồi chiếu về tam giác, xong ngay sau 1 bước, vì ở đây phép chiếu dễ.",
                   "Projected gradient with step 1: jump to p, project back, done in 1 step, because this projection is easy."), hold=5.0)
        self.say(L("Đổi lại, FW chỉ cần một bài toán tuyến tính mỗi bước, và xₖ là tổ hợp của nhiều nhất k + 1 đỉnh: thưa, rẻ khi tập lớn.",
                   "In exchange, FW needs only a linear problem per step, and xₖ mixes at most k + 1 vertices: sparse and cheap for big sets."), hold=5.5)
        self.takeaway([L("Mỗi bước: cực tiểu hàm tuyến tính trên tập → một đỉnh; không phép chiếu.", "Each step minimizes a linear function over the set → a vertex; no projection."),
                       L("Khoảng cách FW là cận trên miễn phí của f − f*.", "The FW gap is a free upper bound on f − f*."),
                       L("Tốc độ O(1/k): chậm ở đuôi, nhưng mỗi bước rất rẻ.", "Rate O(1/k): a slow tail, but every step is cheap.")])
