from rl import *
from o3lib import Fl, Gl, Hl
# Bài 14-03: Newton decrement  λ(x) = (∇fᵀ H⁻¹ ∇f)^{1/2}
# một biến: f(x) = eˣ − 2x, cực tiểu tại ln 2
f1 = lambda x: np.exp(x) - 2 * x; F1S = 2 - 2 * np.log(2)
def ndec1(x): g, h = np.exp(x) - 2, np.exp(x); return g * g / h, x - g / h
L0, X1 = ndec1(0.0); L1, X2 = ndec1(X1)
assert np.isclose(L0, 1) and np.isclose(X1, 1) and np.isclose(f1(0) - F1S, 0.3863, atol=1e-4)
assert np.isclose(L1 / 2, 0.0949, atol=1e-4) and np.isclose(f1(1) - F1S, 0.1046, atol=1e-4)
m0 = lambda x: 1 - x + 0.5 * x * x; assert np.isclose(m0(1), 0.5) and np.isclose(f1(0) - m0(1), L0 / 2)
# hai chiều: hàm log-sum-exp của bài toán Newton (o3lib), Newton tắt dần (backtracking α = 0,25, β = 0,5)
def newton(x, A=np.eye(2), n=6):
    R = []
    for k in range(n):
        F = lambda y: Fl(A @ y); g = A.T @ Gl(A @ x); H = A.T @ Hl(A @ x) @ A
        dx = -np.linalg.solve(H, g); lam2 = -g @ dx
        assert np.isclose(lam2, g @ np.linalg.solve(H, g)) and np.isclose(lam2, dx @ H @ dx)       # ba cách viết λ²
        t = 1.0
        while F(x + t * dx) > F(x) + 0.25 * t * (g @ dx): t *= 0.5
        R.append(dict(x=x.copy(), f=F(x), half=lam2 / 2, gn=np.linalg.norm(g), t=t)); x = x + t * dx
    return R
FS = newton(np.array([-2., 1.]), n=12)[-1]["f"]; assert np.isclose(FS, Fl(np.array([-np.log(2) / 2, 0])))
NR = newton(np.array([-2., 1.])); GAP = [r["f"] - FS for r in NR]; HALF = [r["half"] for r in NR]; TT = [r["t"] for r in NR]
assert np.isclose(GAP[0], 1.274, atol=1e-3) and np.isclose(HALF[0], 46.70, atol=1e-2) and TT[0] == 1 / 64 and TT[1:5] == [1, 1, 1, 1]
assert all(abs(HALF[k] / GAP[k] - 1) < 0.04 for k in (2, 3)) and GAP[3] < 1e-8
AM = np.diag([1., 0.1]); NA = newton(np.linalg.solve(AM, np.array([-2., 1.])), AM)
for r, s in zip(NR, NA): assert np.allclose(AM @ s["x"], r["x"]) and np.isclose(r["half"], s["half"], rtol=1e-9) and r["t"] == s["t"]
GF = [r["gn"] for r in NR]; GG = [r["gn"] for r in NA]
stop = lambda v, eps: next(k for k, a in enumerate(v) if a <= eps)
assert stop(GF, 1e-2) == 3 and stop(GG, 1e-2) == 2 and stop(HALF, 1e-6) == 3 and stop([s["half"] for s in NA], 1e-6) == 3
num = lambda v: nf(v, 3) if v >= 0.01 else sci(v, 1)

class NDec(Reel):
    def construct(self):
        self.title(L("Newton decrement:\nbiết khi nào dừng", "The Newton decrement:\nknowing when to stop"))
        # ---- stage 1
        self.stage(1)
        ax = plain_axes([-0.8, 2.2], [0, 3], 7.4, 5.6, [0, 1.3, 0])
        cf = ax.plot(f1, x_range=[-0.8, 1.93], color=SKY, stroke_width=4)
        lf = Text("f(x) = eˣ − 2x", font=MONO, font_size=24, color=SKY).next_to(ax.c2p(-0.75, 2.7), RIGHT, buff=0)
        dm = Dot(ax.c2p(np.log(2), F1S), color=MINT, radius=0.08)
        self.play(Create(ax), Create(cf), FadeIn(lf), FadeIn(dm), run_time=1.0)
        self.readout([("Δx_nt = −∇²f(x)⁻¹ ∇f(x)", WHITE), ("λ(x) = (∇f(x)ᵀ ∇²f(x)⁻¹ ∇f(x))^½", SUN)], size=24)
        self.say(L("Phương pháp Newton đi bước Δx = −H⁻¹∇f. Bài 14-03 hỏi: làm sao biết đã gần nghiệm để dừng? Câu trả lời là Newton decrement λ(x).",
                   "Newton's method takes the step Δx = −H⁻¹∇f. Lesson 14-03 asks: how do we know we are close enough to stop? The answer is the Newton decrement λ(x)."), hold=8.5)
        cm = ax.plot(m0, x_range=[-0.8, 2.2], color=SUN, stroke_width=3)
        d0 = Dot(ax.c2p(0, 1), color=WHITE, radius=0.09); d1 = Dot(ax.c2p(1, 0.5), color=SUN, radius=0.09)
        self.play(FadeIn(d0), Create(cm), run_time=0.8); self.play(FadeIn(d1), run_time=0.3)
        self.say(L("Ví dụ một biến: f = eˣ − 2x tại x = 0. Đường vàng là mô hình bậc hai của Newton: cùng giá trị, cùng đạo hàm, cùng độ cong tại x = 0.",
                   "A one-variable example: f = eˣ − 2x at x = 0. The yellow curve is Newton's quadratic model: same value, same slope, same curvature at x = 0."), hold=9.5)
        gm = Line(ax.c2p(1.0, 1.0), ax.c2p(1.0, 0.5), color=SUN, stroke_width=6); g0 = DashedLine(ax.c2p(0, 1), ax.c2p(1.0, 1.0), color=DIM)
        gt = Line(ax.c2p(np.log(2) - 0.08, 1), ax.c2p(np.log(2) - 0.08, F1S), color=MINT, stroke_width=6)
        self.play(Create(g0), Create(gm), Create(gt), run_time=0.7)
        self.readout([("f′ = −1, f″ = 1  ⇒  λ² = f′²/f″ = 1" if LANG == "vi" else "f′ = −1, f″ = 1  ⇒  λ² = f′²/f″ = 1", WHITE), ("mô hình giảm được ½λ² = 0,5" if LANG == "vi" else "the model drops by ½λ² = 0.5", SUN), ("f thật giảm được f(0) − f* = 0,386" if LANG == "vi" else "the true f drops by f(0) − f* = 0.386", MINT)], size=23)
        self.say(L("Mô hình đạt đáy tại x = 1 và hạ được 0,5, đúng bằng ½λ². Hàm thật chỉ hạ được 0,386 từ x = 0. Vậy ½λ² là ước lượng khoảng cách tới tối ưu.",
                   "The model bottoms out at x = 1, a drop of 0.5, exactly ½λ². The true function drops 0.386 from x = 0. So ½λ² estimates the distance to optimal."), hold=9.0)
        # ---- stage 2
        self.stage(2)
        self.play(FadeOut(g0), FadeOut(gm), FadeOut(gt), FadeOut(cm), FadeOut(d0), run_time=0.3)
        self.readout([("f(x) − min_v m(x + v) = ½λ(x)²" , SUN), ("λ² = ∇fᵀH⁻¹∇f = Δxᵀ H Δx = −∇fᵀΔx", WHITE)], size=24)
        self.say(L("Vì sao? Mô hình m(x + v) = f + ∇fᵀv + ½vᵀHv đạt nhỏ nhất ở v = Δx_nt, và giá trị nhỏ nhất là f − ½∇fᵀH⁻¹∇f. Khoảng hạ được chính là ½λ².",
                   "Why? The model m(x + v) = f + ∇fᵀv + ½vᵀHv is smallest at v = Δx_nt, with minimum value f − ½∇fᵀH⁻¹∇f. The drop is exactly ½λ²."), hold=9.5)
        self.say(L("λ có ba gương mặt: theo gradient, λ² = ∇fᵀH⁻¹∇f. Theo bước, λ là độ dài của Δx đo bằng Hessian. Và −λ² là đạo hàm theo hướng Newton.",
                   "λ has three faces: in terms of the gradient, λ² = ∇fᵀH⁻¹∇f. In terms of the step, λ is the length of Δx measured by the Hessian. And −λ² is the derivative along the Newton direction."), hold=9.5)
        cm2 = ax.plot(lambda x: f1(1) + (np.e - 2) * (x - 1) + 0.5 * np.e * (x - 1) ** 2, x_range=[0.3, 1.5], color=SUN, stroke_width=3)
        d1b = Dot(ax.c2p(1, f1(1)), color=WHITE, radius=0.09)
        self.play(FadeOut(d1), FadeIn(d1b), Create(cm2), run_time=0.7)
        self.readout([("sau một bước Newton, x = 1:" if LANG == "vi" else "after one Newton step, x = 1:", WHITE), ("½λ² = %s   f − f* = %s" % (nf(L1 / 2, 4), nf(f1(1) - F1S, 4)), SUN)], size=24)
        self.say(L("Sau một bước Newton, ở x = 1: ½λ² = 0,0949 còn khoảng cách thật là 0,1046. Càng gần nghiệm, mô hình bậc hai càng đúng, ước lượng càng sát.",
                   "After one Newton step, at x = 1: ½λ² = 0.0949 and the true gap is 0.1046. The closer we get, the better the quadratic model, the tighter the estimate."), hold=8.5)
        # ---- stage 3
        self.stage(3); self.wipe()
        ax2 = plain_axes([-2.4, 0.6], [-0.6, 1.3], 7.6, 4.8, [0, 1.7, 0])
        Fxy = lambda a, b: Fl(np.array([a, b]))
        cs = contours(ax2, Fxy, [1.0, 1.2, 1.6, 2.2, 3.0, 4.0, 5.5], (-2.4, 0.6, -0.6, 1.3), N=80)
        self.play(Create(ax2), Create(cs), run_time=1.0)
        self.readout([("f(x) = log(e^(x₁+3x₂−0,1) + e^(x₁−3x₂−0,1) + e^(−x₁−0,1))" if LANG == "vi" else "f(x) = log(e^(x₁+3x₂−0.1) + e^(x₁−3x₂−0.1) + e^(−x₁−0.1))", SKY), ("Newton tắt dần từ (−2; 1)" if LANG == "vi" else "damped Newton from (−2, 1)", WHITE)], size=21)
        self.say(L("Giờ hai chiều, hàm log-sum-exp quen thuộc của chương Newton. Chạy Newton có tìm bước lùi, xuất phát từ (−2; 1).",
                   "Now in two dimensions, the familiar log-sum-exp function of the Newton chapter. Run Newton with backtracking, starting from (−2, 1)."), hold=8.0)
        P = np.array([r["x"] for r in NR])
        d = Dot(ax2.c2p(*P[0]), color=SUN, radius=0.09); self.add(d)
        def row(k): return ("%d   %s   %s   %s" % (k, num(GAP[k]).rjust(8), num(HALF[k]).rjust(8), ("1/64" if TT[k] < 1 else "1").rjust(4)), MINT if k >= 2 else WHITE)
        hdr = ("k   f − f*      ½λ²       t", SUN)
        rows = [hdr]
        def cb(k):
            rows.append(row(k)); self.readout(rows, size=22)
        rows.append(row(0)); self.readout(rows, size=22); self.wait(1.0)
        tr_ = trail(self, ax2, P, d, SUN, rt=0.8, ks=range(1, 4), cb=cb, width=3.5)
        self.say(L("Ở điểm đầu, ½λ² = 46,7 trong khi khoảng cách thật chỉ 1,27: xa nghiệm, mô hình bậc hai sai nhiều, nên bước bị cắt còn t = 1/64.",
                   "At the start ½λ² = 46.7 while the true gap is only 1.27: far from the solution the quadratic model is badly off, so the step is cut to t = 1/64."), hold=9.0)
        self.say(L("Từ bước 2, t = 1 và ½λ² gần như trùng với f − f*. Mỗi bước số chữ số đúng tăng gấp đôi: hội tụ bậc hai.",
                   "From step 2 on, t = 1 and ½λ² nearly equals f − f*. The number of correct digits doubles each step: quadratic convergence."), hold=9.5)
        self.say(L("Vì thế tiêu chuẩn dừng của Newton là ½λ² ≤ ε. Nó tính gần như miễn phí, vì λ² = −∇fᵀΔx có sẵn khi đã có bước Newton.",
                   "So Newton's stopping rule is ½λ² ≤ ε. It comes almost for free, since λ² = −∇fᵀΔx is at hand once the Newton step is known."), hold=9.5)
        # ---- stage 4
        self.stage(4); self.wipe()
        self.readout([("g(y) = f(Ay),  A = diag(1; 0,1)" if LANG == "vi" else "g(y) = f(Ay),  A = diag(1, 0.1)", SUN)], y=3.6, size=25)
        self.say(L("Đối chiếu với ‖∇f‖. Đổi biến x = Ay, với A = diag(1; 0,1): chỉ là đổi đơn vị của trục thứ hai. Bài toán vẫn y hệt.",
                   "Compare with ‖∇f‖. Change variables x = Ay with A = diag(1, 0.1): just a change of units on the second axis. The problem is the same."), hold=9.5)
        tb = VGroup(*[Text(s_, font=MONO, font_size=23, color=c_) for s_, c_ in [("k   ‖∇f‖     ‖∇g‖     ½λ² (f và g)" if LANG == "vi" else "k   ‖∇f‖     ‖∇g‖     ½λ² (f and g)", SUN)] +
                      [("%d   %s   %s   %s" % (k, num(GF[k]).rjust(7), num(GG[k]).rjust(7), num(HALF[k]).rjust(8)), WHITE) for k in range(5)]]).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to([0, 1.2, 0])
        self.play(FadeIn(tb, lag_ratio=0.1), run_time=1.2)
        self.say(L("Newton chạy trên g cho đúng các điểm cũ, chỉ đổi tọa độ, và λ giống hệt từng chữ số. Đó là tính bất biến affine trong bài.",
                   "Newton on g produces exactly the old points in new coordinates, and λ matches digit for digit. That is the affine invariance of the lesson."), hold=9.5)
        hl1 = SurroundingRectangle(tb[4], color=PINK, buff=0.06); hl2 = SurroundingRectangle(tb[3], color=ORANGE, buff=0.06)
        self.play(Create(hl1), Create(hl2), run_time=0.5)
        self.readout([("dừng khi ‖∇‖ ≤ 10⁻²:  f ở k = 3,  g ở k = 2" if LANG == "vi" else "stop at ‖∇‖ ≤ 10⁻²:  f at k = 3,  g at k = 2", PINK), ("dừng khi ½λ² ≤ 10⁻⁶:  cả hai ở k = 3" if LANG == "vi" else "stop at ½λ² ≤ 10⁻⁶:  both at k = 3", MINT)], size=23)
        self.say(L("Còn ‖∇g‖ = ‖Aᵀ∇f‖ thì khác hẳn. Dừng theo ‖∇‖ ≤ 10⁻², f dừng ở bước 3 nhưng g dừng ở bước 2: chỉ vì đổi đơn vị mà kết luận khác.",
                   "But ‖∇g‖ = ‖Aᵀ∇f‖ is quite different. Stopping at ‖∇‖ ≤ 10⁻², f stops at step 3 but g at step 2: a mere change of units changes the verdict."), hold=9.5)
        self.say(L("½λ² thì không bị ảnh hưởng, và còn đo đúng thứ ta quan tâm: f còn cao hơn tối ưu bao nhiêu. Giống khoảng cách Mahalanobis, Hessian đóng vai nghịch đảo hiệp phương sai.",
                   "½λ² is unaffected, and it measures what we care about: how far f is above optimal. Like a Mahalanobis distance, with the Hessian in the role of the inverse covariance."), hold=9.5)
        self.takeaway([L("λ² = ∇fᵀH⁻¹∇f = ΔxᵀHΔx = −∇fᵀΔx.", "λ² = ∇fᵀH⁻¹∇f = ΔxᵀHΔx = −∇fᵀΔx."),
                       L("½λ² là mức hạ của mô hình bậc hai, ước lượng f − f*.", "½λ² is the drop of the quadratic model, an estimate of f − f*."),
                       L("Gần nghiệm ước lượng rất sát; xa nghiệm có thể sai nhiều.", "Near the solution the estimate is tight; far away it can be way off."),
                       L("Dừng khi ½λ² ≤ ε: bất biến affine, khác ‖∇f‖.", "Stop when ½λ² ≤ ε: affine invariant, unlike ‖∇f‖.")], tail=4.0)
