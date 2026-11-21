from rl import *
from o3lib import BA, BB, BC, bar_center, barrier_run
A, B, C = BA, BB, BC
def phi(x, t):
    s = B - A @ x
    return np.inf if (s <= 0).any() else t * C @ x - np.log(s).sum()
VERTS = [(0.2, 0.2), (3, 0.2), (3, 1), (1.4, 2.6), (0.2, 2.6)]
assert all((A @ np.array(v) <= B + 1e-9).all() for v in VERTS)
PSTAR = C @ np.array([3, 1.0])
# analytic center and outer iterations, mu = 10
xa, _ = bar_center(1e-9, np.array([1.5, 1.0]))
def outer(mu, t0=1.0, tol=1e-6):
    x = np.array([1.5, 1.0]); t = t0; rec = []
    while True:
        x, s = bar_center(t, x); rec.append((t, x.copy(), s, C @ x - PSTAR))
        if 5 / t <= tol: break
        t *= mu
    return rec
R10 = outer(10)
assert all(r[3] <= 5 / r[0] + 1e-7 for r in R10) and np.linalg.norm(R10[-1][1] - [3, 1]) < 1e-4
TOT = {mu: (len(outer(mu)), sum(r[2] for r in outer(mu))) for mu in (2, 10, 100, 1000)}
print("TOT", TOT)
TS = [10 ** (k / 20) for k in range(-30, 101)]
PATH = []; x = np.array([1.5, 1.0])
for t in TS: x, _ = bar_center(t, x); PATH.append(x.copy())

class Path(Reel):
    def construct(self):
        self.title(L("Phương pháp rào cản: đường\ntrung tâm dẫn tới đỉnh tối ưu", "The barrier method: the central\npath leads to the optimal vertex"))
        self.stage(1)
        ax = plain_axes([0, 3.4], [0, 3.0], 7.4, 6.5, [0, 1.15, 0])
        P = lambda p: ax.c2p(p[0], p[1])
        poly = Polygon(*[P(v) for v in VERTS], color=SKY, stroke_width=4, fill_color=SKY, fill_opacity=0.12)
        self.play(Create(poly), run_time=1.0)
        self.say(L("Bài toán LP: tối đa x + 0,7y trên đa giác 5 ràng buộc. Đáp số là đỉnh (3; 1).",
                   "An LP: maximize x + 0.7y over a polygon with 5 constraints. The answer is the vertex (3, 1)."))
        vt = Dot(P((3, 1)), radius=0.13, color=MINT); arr = Arrow(P((1.0, 0.9)), P((1.75, 1.42)), color=ORANGE, buff=0, stroke_width=6)
        self.play(FadeIn(vt), GrowArrow(arr), run_time=0.6)
        self.readout(["min cᵀx,  c = (−1, −0,7)" if LANG == "vi" else "min cᵀx,  c = (−1, −0.7)", "s.t. aᵢᵀx ≤ bᵢ,  i = 1..5", "p* = " + nf(PSTAR, 2)], color=DIM, size=24)
        self.say(L("Simplex đi dọc các cạnh. Phương pháp điểm trong thì đi xuyên qua bên trong.", "Simplex walks along the edges. Interior-point methods cut through the inside."))
        # key idea
        self.stage(2)
        self.readout(["φ(x) = −Σ log(bᵢ − aᵢᵀx)", "x*(t) = argmin  t·cᵀx + φ(x)"], color=SUN, size=25)
        self.say(L("Thay ràng buộc bằng hàng rào φ: tiến tới vô cùng khi chạm biên. Cực tiểu hoá t·cᵀx + φ(x).",
                   "Replace the constraints by a barrier φ that blows up at the boundary. Minimize t·cᵀx + φ(x)."), hold=4.5)
        lv = [phi(xa, 1e-9) + d for d in (0.3, 1.0, 2.0, 3.5, 5.5)]
        cs = contours(ax, lambda x, y: phi(np.array([x, y]), 1e-9), lv, (0.2, 3.0, 0.2, 2.6), N=70, color="#5a6890")
        ac = Dot(P(xa), radius=0.12, color=SUN)
        self.play(Create(cs), FadeIn(ac), run_time=1.2)
        self.say(L("t ≈ 0: chỉ còn hàng rào; cực tiểu là tâm giải tích %s, nằm sâu bên trong." % vec(xa, 2),
                   "t ≈ 0: only the barrier is left; its minimizer is the analytic center %s, deep inside." % vec(xa, 2)))
        lv2 = [phi(PATH[60], TS[60]) + d for d in (0.3, 1.0, 2.0, 3.5, 5.5)]
        cs2 = contours(ax, lambda x, y: phi(np.array([x, y]), TS[60]), lv2, (0.2, 3.0, 0.2, 2.6), N=70, color="#5a6890")
        self.play(Transform(cs, cs2), ac.animate.move_to(P(PATH[60])), run_time=1.2)
        self.say(L("t = 10: mục tiêu nặng hơn, cực tiểu trượt về phía đỉnh tối ưu.", "t = 10: the objective weighs more, and the minimizer slides toward the optimal vertex."))
        pc = VMobject(color=SUN, stroke_width=5).set_points_smoothly([P(p) for p in PATH])
        self.play(FadeOut(cs), Create(pc), ac.animate.move_to(P(PATH[-1])), run_time=2.5)
        self.say(L("Tập các x*(t) khi t chạy từ 0 tới ∞ là đường trung tâm. Nó kết thúc tại đỉnh tối ưu.",
                   "The set of x*(t) for t from 0 to ∞ is the central path. It ends at the optimal vertex."))
        # algorithm
        self.stage(3); self.play(FadeOut(ac), pc.animate.set_stroke(opacity=0.35), run_time=0.4)
        self.say(L("Phương pháp rào cản: t₀ = 1, nhân t lên μ = 10 mỗi vòng; mỗi vòng dùng Newton để định tâm.",
                   "The barrier method: t₀ = 1, multiply t by μ = 10 each round; each round re-centers with Newton."), hold=4.5)
        d = Dot(P((1.5, 1.0)), radius=0.13, color=MINT); self.add(d)
        tot = 0
        for i, (t, x, s, gap) in enumerate(R10):
            tot += s
            self.play(d.animate.move_to(P(x)), run_time=0.8)
            self.readout(["t = %s   Newton steps = %d" % (sci(t, 0) if t >= 10 else "1", s) if LANG == "en" else "t = %s   số bước Newton = %d" % (sci(t, 0) if t >= 10 else "1", s),
                          "x*(t) = %s" % vec(x, 5), ("cᵀx − p* = %s  ≤  m/t = %s" % (sci(max(gap, 1e-12)), sci(5 / t)), MINT)], color=WHITE, size=22)
            self.wait(0.9 if i < 3 else 0.5)
        self.say(L("Sai số luôn ≤ m/t = 5/t: biết chính xác khi nào dừng. Tổng cộng %d bước Newton qua %d vòng." % (TOT[10][1], TOT[10][0]),
                   "The gap is always ≤ m/t = 5/t: we know exactly when to stop. %d Newton steps in total over %d rounds." % (TOT[10][1], TOT[10][0])), hold=5.0)
        # contrast
        self.stage(4)
        rows = [("  μ     vòng   bước Newton" if LANG == "vi" else "  μ     rounds   Newton steps", WHITE)]
        for mu in (2, 10, 100, 1000):
            rows.append(("%5d    %3d      %3d" % (mu, TOT[mu][0], TOT[mu][1]), MINT if mu == 10 else SKY))
        self.readout(rows, size=24)
        self.say(L("μ nhỏ: nhiều vòng rẻ (≈ %s bước Newton mỗi vòng). μ lớn: ít vòng, mỗi vòng tốn hơn (≈ %s bước)." % (nf(TOT[2][1] / TOT[2][0], 1), nf(TOT[1000][1] / TOT[1000][0], 1)),
                   "Small μ: many cheap rounds (≈ %s Newton steps each). Large μ: few rounds, each costlier (≈ %s steps)." % (nf(TOT[2][1] / TOT[2][0], 1), nf(TOT[1000][1] / TOT[1000][0], 1))), hold=5.5)
        self.say(L("Với LP nhỏ này μ lớn thắng về tổng số bước; tổng chi phí chỉ đổi vài lần trong khi μ đổi gấp 500 lần.",
                   "On this small LP a large μ wins on the total; the total changes only a few-fold while μ changes 500-fold."), hold=5.0)
        self.takeaway([L("Hàng rào log thay ràng buộc; t·cᵀx + φ(x) là bài toán trơn không ràng buộc.", "A log barrier replaces the constraints; t·cᵀx + φ(x) is smooth and unconstrained."),
                       L("x*(t) vạch ra đường trung tâm, với sai số ≤ m/t.", "x*(t) traces the central path, with gap ≤ m/t."),
                       L("Tăng t theo cấp số nhân, định tâm lại bằng Newton: vài chục bước là đủ.", "Increase t geometrically and re-center with Newton: a few dozen steps suffice.")])
