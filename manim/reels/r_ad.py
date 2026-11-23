from rl import *
import math
# Bài 27-02 / 27-03: vi phân tự động, chế độ thuận (tiếp tuyến, số đối ngẫu) và chế độ nghịch (adjoint, backprop)
class Dual:                                   # số đối ngẫu a + bε, ε² = 0
    def __init__(s, a, b=0.): s.a, s.b = a, b
    def __add__(s, o): o = o if isinstance(o, Dual) else Dual(o); return Dual(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __mul__(s, o): o = o if isinstance(o, Dual) else Dual(o); return Dual(s.a * o.a, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
def dsin(u): return Dual(math.sin(u.a), math.cos(u.a) * u.b)
fx = lambda x1, x2: x1 * x2 + (dsin(x1) if isinstance(x1, Dual) else math.sin(x1))
X1, X2 = 2.0, 3.0
V3, V4 = X1 * X2, math.sin(X1); FV = V3 + V4
T1 = fx(Dual(X1, 1), Dual(X2, 0)); T2 = fx(Dual(X1, 0), Dual(X2, 1))
D1, D2 = X2 + math.cos(X1), X1
assert np.isclose(T1.a, FV) and np.isclose(T1.b, D1) and np.isclose(T2.b, D2) and np.isclose(D1, 2.584, atol=1e-3) and np.isclose(FV, 6.909, atol=1e-3)
# chế độ nghịch bằng một băng ghi (tape) nhỏ
def reverse(x1, x2):
    v3 = x1 * x2; v4 = math.sin(x1); f = v3 + v4
    fb = 1.0; v3b = fb; v4b = fb; x1b = v3b * x2 + v4b * math.cos(x1); x2b = v3b * x1
    return f, (v3b, v4b, x1b, x2b)
_, BAR = reverse(X1, X2); assert np.allclose(BAR[2:], [D1, D2])
h = 1e-6; assert abs((fx(X1 + h, X2) - fx(X1 - h, X2)) / (2 * h) - D1) < 1e-8 and abs((fx(X1, X2 + h) - fx(X1, X2 - h)) / (2 * h) - D2) < 1e-8
# ví dụ đồ chơi của bài 27-03
x, y, w1, w2 = 1.5, 0.3, 0.8, -0.4
loss = lambda w1, w2: (w2 * max(w1 * x, 0) - y) ** 2
z = w1 * x; hh = max(z, 0); pred = w2 * hh; ell = (pred - y) ** 2
pb = 2 * (pred - y); dw2 = pb * hh; hb = pb * w2; zb = hb * (z > 0); dw1 = zb * x
assert np.isclose(z, 1.2) and np.isclose(pred, -0.48) and np.isclose(ell, 0.6084) and np.isclose(pb, -1.56)
assert np.isclose(dw2, -1.872) and np.isclose(hb, 0.624) and np.isclose(dw1, 0.936)
assert abs((loss(w1 + h, w2) - loss(w1 - h, w2)) / (2 * h) - dw1) < 1e-7 and abs((loss(w1, w2 + h) - loss(w1, w2 - h)) / (2 * h) - dw2) < 1e-7
# số lượt quét để có cả gradient của f: Rⁿ → R (chế độ thuận: n; ngược: 1)
def sweeps(n, m=1): return dict(fwd=n, rev=m)
assert sweeps(2) == dict(fwd=2, rev=1) and sweeps(10 ** 6)["fwd"] == 10 ** 6

class Ad(Reel):
    def graph(self):
        P = {"x1": (-2.2, -1.4), "x2": (2.2, -1.4), "v4": (-2.2, 1.0), "v3": (1.2, 1.0), "f": (-0.5, 3.3)}
        lab = {"x1": "x₁", "x2": "x₂", "v4": "sin", "v3": "×", "f": "+"}
        N = {k: VGroup(Circle(0.42, color=SKY if k[0] == "x" else WHITE, stroke_width=3, fill_color=CARD, fill_opacity=1), Text(lab[k], font=MONO, font_size=26, color=SKY if k[0] == "x" else WHITE)).move_to([*P[k], 0]) for k in P}
        E = [("x1", "v4"), ("x1", "v3"), ("x2", "v3"), ("v4", "f"), ("v3", "f")]
        Ed = VGroup(*[Arrow(N[a].get_center(), N[b].get_center(), buff=0.45, color=DIM, stroke_width=3, max_tip_length_to_length_ratio=0.08) for a, b in E])
        return N, Ed

    def tag(self, N, k, s, c, side):
        return Text(s, font=MONO, font_size=21, color=c).next_to(N[k], side, buff=0.12)

    def construct(self):
        self.title(L("Vi phân tự động:\nchế độ thuận và nghịch", "Automatic differentiation:\nforward and reverse"))
        # ---- stage 1
        self.stage(1)
        N, Ed = self.graph()
        self.readout([("f(x₁, x₂) = x₁x₂ + sin x₁,   x = (2; 3)" if LANG == "vi" else "f(x₁, x₂) = x₁x₂ + sin x₁,   x = (2, 3)", SUN)], size=24)
        self.play(*[FadeIn(n) for n in N.values()], Create(Ed), run_time=1.2)
        self.say(L("Ví dụ của bài 27-02: f = x₁x₂ + sin x₁. Máy tính coi nó là một đồ thị tính toán: mỗi nút là một phép toán cơ bản, biết sẵn đạo hàm của mình.",
                   "The example of lesson 27-02: f = x₁x₂ + sin x₁. The computer sees it as a computation graph: each node is an elementary operation that knows its own derivative."), hold=9.0)
        vals = [("x1", "2", LEFT), ("x2", "3", RIGHT), ("v4", "0,909" if LANG == "vi" else "0.909", LEFT), ("v3", "6", RIGHT), ("f", "6,909" if LANG == "vi" else "6.909", LEFT)]
        T = {}
        for k, s_, sd in vals:
            T[k] = self.tag(N, k, s_, WHITE, sd); self.play(FadeIn(T[k]), Indicate(N[k], color=SUN, scale_factor=1.1), run_time=0.45)
        self.say(L("Lượt tính xuôi: đi từ đầu vào lên đầu ra, ghi lại giá trị từng nút. sin 2 ≈ 0,909, 2·3 = 6, cộng lại f ≈ 6,909.",
                   "The forward evaluation: go from inputs to output, recording each node's value. sin 2 ≈ 0.909, 2·3 = 6, so f ≈ 6.909."), hold=8.0)
        self.say(L("Câu hỏi: tính ∂f/∂x₁ và ∂f/∂x₂ chính xác, không sai số sai phân, chỉ bằng quy tắc dây chuyền. Có hai thứ tự để áp quy tắc này.",
                   "The question: compute ∂f/∂x₁ and ∂f/∂x₂ exactly, with no finite-difference error, using only the chain rule. There are two orders in which to apply it."), hold=8.5)
        # ---- stage 2
        self.stage(2)
        self.readout([("v̇ = ∂ᵤh·u̇ + ∂_w h·ẇ   (đi xuôi)" if LANG == "vi" else "v̇ = ∂ᵤh·u̇ + ∂_w h·ẇ   (forward)", SKY), ("hạt giống ẋ = (1; 0)" if LANG == "vi" else "seed ẋ = (1, 0)", WHITE)], size=24)
        self.say(L("Chế độ thuận: mỗi nút mang thêm một tiếp tuyến v̇, là đạo hàm theo một hướng chọn trước. Hạt giống ẋ = (1; 0) nghĩa là ta hỏi về x₁.",
                   "Forward mode: each node also carries a tangent v̇, the derivative along a chosen direction. The seed ẋ = (1, 0) means we are asking about x₁."), hold=8.5)
        tan1 = [("x1", "1", DOWN), ("x2", "0", DOWN), ("v4", "cos2·1 = −0,416" if LANG == "vi" else "cos2·1 = −0.416", DOWN), ("v3", "1·3 + 2·0 = 3", DOWN), ("f", "ḟ = 2,584" if LANG == "vi" else "ḟ = 2.584", RIGHT)]
        TA = VGroup()
        for k, s_, sd in tan1:
            m = self.tag(N, k, s_, SKY, sd); TA.add(m); self.play(FadeIn(m), run_time=0.4)
        self.say(L("Đi xuôi cùng với giá trị: nhánh sin cho cos 2 ≈ −0,416, nhánh nhân cho 3. Ở đầu ra ḟ = 3 + cos 2 ≈ 2,584 = ∂f/∂x₁.",
                   "Move forward together with the values: the sin branch gives cos 2 ≈ −0.416, the product branch gives 3. At the output ḟ = 3 + cos 2 ≈ 2.584 = ∂f/∂x₁."), hold=9.0)
        self.readout([("x₁ = 2 + ε,  x₂ = 3,  ε² = 0" if LANG == "vi" else "x₁ = 2 + ε,  x₂ = 3,  ε² = 0", SKY), ("f = 6,909 + 2,584ε" if LANG == "vi" else "f = 6.909 + 2.584ε", SUN)], size=25)
        self.say(L("Viết gọn bằng số đối ngẫu: thay x₁ bằng 2 + ε với ε² = 0 rồi tính f như bình thường. Phần ε của kết quả chính là đạo hàm.",
                   "In compact form with dual numbers: replace x₁ by 2 + ε with ε² = 0 and evaluate f as usual. The ε part of the result is the derivative."), hold=8.5)
        self.play(FadeOut(TA), run_time=0.3)
        tan2 = [("x1", "0", DOWN), ("x2", "1", DOWN), ("v4", "0", DOWN), ("v3", "0·3 + 2·1 = 2", DOWN), ("f", "ḟ = 2", RIGHT)]
        TB = VGroup()
        for k, s_, sd in tan2:
            m = self.tag(N, k, s_, PINK, sd); TB.add(m); self.play(FadeIn(m), run_time=0.3)
        self.readout([("hạt giống ẋ = (0; 1):  ḟ = 2 = ∂f/∂x₂" if LANG == "vi" else "seed ẋ = (0, 1):  ḟ = 2 = ∂f/∂x₂", PINK), ("n đầu vào  ⇒  n lượt xuôi" if LANG == "vi" else "n inputs  ⇒  n forward passes", ORANGE)], size=24)
        self.say(L("Muốn ∂f/∂x₂ thì phải chạy lại với hạt giống (0; 1), được 2 = x₁. Mỗi lượt chỉ cho một cột của Jacobian: n đầu vào cần n lượt.",
                   "For ∂f/∂x₂ we must run again with seed (0, 1), giving 2 = x₁. Each pass yields only one column of the Jacobian: n inputs need n passes."), hold=9.0)
        self.play(FadeOut(TB), run_time=0.3)
        # ---- stage 3
        self.stage(3)
        self.readout([("ū += v̄ · ∂ᵤh   (đi ngược)" if LANG == "vi" else "ū += v̄ · ∂ᵤh   (backward)", MINT), ("bắt đầu f̄ = 1" if LANG == "vi" else "start with f̄ = 1", WHITE)], size=24)
        self.say(L("Chế độ nghịch, bài 27-03: mỗi nút mang một adjoint v̄ = ∂f/∂v. Bắt đầu từ đầu ra với f̄ = 1, rồi đi ngược đồ thị.",
                   "Reverse mode, lesson 27-03: each node carries an adjoint v̄ = ∂f/∂v. Start at the output with f̄ = 1, then walk the graph backward."), hold=8.0)
        bars = [("f", "f̄ = 1", RIGHT), ("v3", "v̄ = 1", DOWN), ("v4", "v̄ = 1", DOWN), ("x2", "x̄₂ = 1·2 = 2", DOWN), ("x1", "x̄₁ = 1·3 + 1·cos2", DOWN)]
        TC = VGroup()
        for k, s_, sd in bars:
            m = self.tag(N, k, s_, MINT, sd); TC.add(m); self.play(FadeIn(m), Indicate(N[k], color=MINT, scale_factor=1.1), run_time=0.45)
        self.readout([("x̄₁ = 2,584,  x̄₂ = 2:  cả gradient sau 1 lượt" if LANG == "vi" else "x̄₁ = 2.584,  x̄₂ = 2:  the whole gradient in 1 pass", MINT)], size=24)
        self.say(L("Phép cộng chuyển adjoint nguyên vẹn cho hai nhánh. Phép nhân gửi về x₂ một lượng 1·x₁ = 2. x₁ nhận từ hai nhánh, nên cộng lại: 3 + cos 2 ≈ 2,584.",
                   "The sum passes the adjoint unchanged to both branches. The product sends 1·x₁ = 2 back to x₂. x₁ receives from two branches, so they add: 3 + cos 2 ≈ 2.584."), hold=9.5)
        self.say(L("Một lượt ngược cho cả hai đạo hàm cùng lúc. Đó là tích vector–Jacobian, và với hàm vô hướng thì là toàn bộ gradient.",
                   "One backward pass gives both derivatives at once. It is a vector–Jacobian product, and for a scalar function that is the whole gradient."), hold=8.0)
        self.wipe()
        VI = LANG == "vi"
        rows = VGroup(*[Text(s_, font=MONO, font_size=25, color=c_) for s_, c_ in (
            ("ℓ = (w₂·relu(w₁x) − y)²", SUN), ("x = 1,5;  y = 0,3" if VI else "x = 1.5,  y = 0.3", WHITE), ("w₁ = 0,8;  w₂ = −0,4" if VI else "w₁ = 0.8,  w₂ = −0.4", WHITE),
            ("xuôi:  z = 1,2;  h = 1,2" if VI else "forward:  z = 1.2,  h = 1.2", WHITE), ("       ŷ = −0,48;  ℓ = 0,6084" if VI else "          ŷ = −0.48,  ℓ = 0.6084", WHITE),
            ("ngược: ŷ̄ = 2(ŷ − y) = −1,56" if VI else "backward: ŷ̄ = 2(ŷ − y) = −1.56", MINT),
            ("       ∂ℓ/∂w₂ = ŷ̄·h = −1,872" if VI else "          ∂ℓ/∂w₂ = ŷ̄·h = −1.872", MINT),
            ("       h̄ = ŷ̄·w₂ = 0,624 = z̄" if VI else "          h̄ = ŷ̄·w₂ = 0.624 = z̄", MINT),
            ("       ∂ℓ/∂w₁ = z̄·x = 0,936" if VI else "          ∂ℓ/∂w₁ = z̄·x = 0.936", MINT))]).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        fit(rows, 8.2).move_to([0, 1.0, 0])
        self.play(FadeIn(rows[:5], lag_ratio=0.2), run_time=1.0)
        self.say(L("Backprop chính là chế độ nghịch. Ví dụ đồ chơi của bài 27-03: một nơ-ron ReLU, hai trọng số. Lượt xuôi cho ℓ = 0,6084.",
                   "Backprop is exactly reverse mode. The toy example of lesson 27-03: one ReLU neuron, two weights. The forward pass gives ℓ = 0.6084."), hold=8.0)
        self.play(FadeIn(rows[5:], lag_ratio=0.25), run_time=1.2)
        self.say(L("Lượt ngược: ∂ℓ/∂w₂ = −1,872 và ∂ℓ/∂w₁ = 0,936, khớp với sai phân hữu hạn. ReLU đang bật vì z > 0, nên adjoint đi qua nguyên vẹn.",
                   "Backward: ∂ℓ/∂w₂ = −1.872 and ∂ℓ/∂w₁ = 0.936, matching finite differences. The ReLU is active since z > 0, so the adjoint passes straight through."), hold=9.0)
        # ---- stage 4
        self.stage(4); self.wipe()
        VI = LANG == "vi"
        R = [(("f: Rⁿ → Rᵐ", "thuận", "nghịch") if VI else ("f: Rⁿ → Rᵐ", "fwd", "rev"), SUN), (("n = 2, m = 1", "2", "1"), WHITE),
             (("mạng: n = 10⁶, m = 1" if VI else "net: n = 10⁶, m = 1", "10⁶", "1"), MINT), (("n = 1, m = 10⁶", "1", "10⁶"), PINK),
             (("mỗi lượt cho" if VI else "each pass gives", "cột J" if VI else "J col", "hàng J" if VI else "J row"), DIM)]
        tb = VGroup(*[Text("%-21s%7s%8s" % r, font=MONO, font_size=25, color=c_) for r, c_ in R]).arrange(DOWN, aligned_edge=LEFT, buff=0.38).move_to([0, 1.9, 0])
        fit(tb, 8.2)
        self.play(FadeIn(tb, lag_ratio=0.15), run_time=1.2)
        self.say(L("Đếm số lượt quét. Chế độ thuận cần n lượt, mỗi lượt một cột Jacobian. Chế độ nghịch cần m lượt, mỗi lượt một hàng.",
                   "Count the sweeps. Forward mode needs n passes, one Jacobian column each. Reverse mode needs m passes, one row each."), hold=8.0)
        self.say(L("Huấn luyện mạng: một hàm mất mát, hàng triệu tham số. Thuận cần một triệu lượt, nghịch chỉ cần một lượt, cỡ vài lần chi phí tính f. Vì thế học sâu dùng backprop.",
                   "Training a network: one loss, millions of parameters. Forward needs a million passes, reverse just one, a few times the cost of evaluating f. That is why deep learning uses backprop."), hold=10.0)
        self.say(L("Ngược lại, một đầu vào và rất nhiều đầu ra thì chế độ thuận thắng. Và chế độ thuận không cần nhớ gì, còn chế độ nghịch phải lưu mọi giá trị trung gian của lượt xuôi.",
                   "Conversely, one input and many outputs favors forward mode. And forward mode needs no memory, while reverse mode must store every intermediate value of the forward pass."), hold=10.0)
        self.takeaway([L("Đồ thị tính toán: mỗi nút biết đạo hàm cục bộ.", "Computation graph: each node knows its local derivative."),
                       L("Thuận: tiếp tuyến đi xuôi, số đối ngẫu; n lượt cho n đầu vào.", "Forward: tangents flow forward, dual numbers; n passes for n inputs."),
                       L("Nghịch: adjoint đi ngược; một lượt cho cả gradient.", "Reverse: adjoints flow backward; one pass for the whole gradient."),
                       L("Backprop = chế độ nghịch, đổi lại phải lưu lượt xuôi.", "Backprop = reverse mode, at the price of storing the forward pass.")], tail=4.0)
