---
layout: post
title: 15-11 Bài Tập Thực Hành - Phương Pháp Rào Cản
chapter: '15'
order: 17
owner: GitHub Copilot
lang: vi
categories:
- chapter15
lesson_type: required
redirect_from:
  - /contents/vi/chapter15/15_10_Practical_Exercises_Barrier_Method/
---

Để thực sự làm chủ phương pháp chắn, không có cách nào hiệu quả hơn việc tự tay tính đạo hàm của hàm chắn logarit, giải tường minh đường trung tâm $$x^*(t)$$ cho một bài toán LP nhỏ, thiết lập điều kiện KKT nhiễu, và tự tay tính cận số vòng lặp hội tụ. Những phép tính tưởng chừng ngắn gọn đó sẽ giúp bạn nhìn thấy rõ ràng từng khớp nối giữa giải tích, đại số tuyến tính và lý thuyết đối ngẫu.

Bộ bài tập thực hành dưới đây được biên soạn dựa trên các bài kinh điển của Boyd & Vandenberghe, Nocedal & Wright và Nesterov. Trước khi bắt tay giải, hãy xem qua bốn kỹ năng cốt lõi và một bài mẫu tính trọn vẹn từ hàm chắn đến kiểm tra KKT nhiễu.

## Bản đồ kiến thức nền: Bốn kỹ năng tự luận trọng tâm của bài tập Chương 15

- **Giải tích hàm chắn dạng ma trận:** Với $$h_i(x) = a_i^T x - b_i$$, tập thói quen viết gọn $$\nabla \phi(x) = A^T d$$ và $$\nabla^2 \phi(x) = A^T \operatorname{diag}(d^2) A$$ (với $$d_i = \frac{1}{b_i - a_i^T x}$$) để chứng minh nhanh tính lồi và tính tự hài hòa.
- **Giải tường minh đường trung tâm 1D/2D:** Đặt $$\nabla (t f(x) + \phi(x)) = 0$$ (cộng thêm $$A^T w = 0$$ nếu có ràng buộc đẳng thức), giải theo $$t$$ và luôn chọn nhánh nghiệm nằm trong miền khả thi chặt $$h_i(x) < 0$$.
- **Kiểm chứng cặp nguyên thủy – đối ngẫu trên đường trung tâm:** Từ $$x^*(t)$$, tính ngay $$u_i^*(t) = -\frac{1}{t h_i(x^*(t))}$$, kiểm tra $$u_i^* > 0$$, điều kiện dừng và xác nhận $$f(x^*(t)) - g(u^*(t)) = m/t$$.
- **Thiết lập Pha I và phân tích độ phức tạp:** Luôn kiểm tra cách chọn $$s^{(0)} > \max_i h_i(x^{(0)})$$ và nhớ công thức số vòng ngoài $$\lceil \log(m/(\epsilon t^{(0)})) / \log \mu \rceil$$.

### Khung giải thích (nên đọc chậm): Bài mẫu giải trọn vẹn đường trung tâm có ràng buộc đẳng thức

**Bài toán mẫu:** Tìm đường trung tâm $$x^*(t)$$ cho bài toán cực tiểu hóa 2 biến có cả ràng buộc đẳng thức và bất đẳng thức:
$$\min_{x \in \mathbb{R}^2} x_1 \qquad \text{với điều kiện } x_1 + x_2 = 1, \;\; x_1 \ge 0, \;\; x_2 \ge 0.$$

1. **Khử biến bằng ràng buộc đẳng thức (để thấy rõ đường trung tâm 1 chiều):**
   Vì $$x_2 = 1 - x_1$$ và $$x_1 > 0, x_2 > 0 \iff x_1 \in (0, 1)$$, bài toán chắn trở thành:
   $$\min_{x_1 \in (0, 1)} t x_1 - \log(x_1) - \log(1 - x_1).$$
2. **Giải điều kiện dừng:**
   $$t - \frac{1}{x_1} + \frac{1}{1 - x_1} = 0 \iff t x_1(1 - x_1) - (1 - 2x_1) = 0 \iff t x_1^2 - (t + 2)x_1 + 1 = 0.$$
   Chọn nghiệm nằm trong $$(0, 1)$$:
   $$x_1^*(t) = \frac{t + 2 - \sqrt{t^2 + 4}}{2t}, \qquad x_2^*(t) = 1 - x_1^*(t).$$
3. **Kiểm tra hai đầu mút và số liệu tại $$t = 2$$:**
   - Khi $$t \to 0^+$$: $$x_1^*(t) \to \frac{1}{2}, x_2^*(t) \to \frac{1}{2}$$ (tâm giải tích của đơn hình chuẩn!).
   - Tại $$t = 2$$: $$x_1^*(2) = \frac{4 - \sqrt{8}}{4} = 1 - \frac{\sqrt{2}}{2} \approx 0.2929$$, $$x_2^*(2) \approx 0.7071$$.
   - Kiểm tra khoảng cách dưới tối ưu ($$m = 2, f^* = 0$$): $$f(x^*(2)) - f^* = 0.2929 \le \frac{m}{t} = \frac{2}{2} = 1.0$$!

---

# Bài Tập Thực Hành - Phương Pháp Chắn (Barrier Method)

Các bài tập dưới đây được tham khảo từ Boyd & Vandenberghe (2004), Nocedal & Wright (2006) và Nesterov (2004).

---

## 📝 **Phần I: Hàm chắn logarit (Log-Barrier Function)**

### **Bài tập 1: Tính đạo hàm của hàm chắn logarit (Boyd & Vandenberghe, Ex. 11.1)**

Xét bài toán tối ưu:

$$
\begin{align}
\min_{x} \quad & f(x) \\
\text{s.t.} \quad & h_i(x) \leq 0, \quad i = 1, \ldots, m
\end{align}
$$

với hàm chắn logarit:

$$
\phi(x) = -\sum_{i=1}^m \log(-h_i(x))
$$

**Yêu cầu:**  
a) Tính $$\nabla \phi(x)$$ và $$\nabla^2 \phi(x)$$.  
b) Cho $$f(x) = x^2$$, $$h_1(x) = x - 1$$, $$h_2(x) = -x - 1$$ (tương ứng $$-1 \leq x \leq 1$$). Tính $$\phi(x)$$, $$\nabla \phi(x)$$ và $$\nabla^2 \phi(x)$$.  
c) Tính các giá trị trên tại $$x = 0$$.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Gradient và Hessian của $$\phi(x)$$:**

**Gradient:**

$$
\nabla \phi(x) = -\sum_{i=1}^m \frac{1}{-h_i(x)} (-\nabla h_i(x)) = \sum_{i=1}^m \frac{\nabla h_i(x)}{-h_i(x)}
$$

**Hessian:**

$$
\nabla^2 \phi(x) = \sum_{i=1}^m \left( \frac{\nabla^2 h_i(x)}{-h_i(x)} + \frac{\nabla h_i(x) \nabla h_i(x)^T}{h_i(x)^2} \right)
$$

---

**b) Trường hợp cụ thể:**

$$
f(x) = x^2, \quad h_1(x) = x - 1, \quad h_2(x) = -x - 1
$$

**Hàm chắn:**

$$
\phi(x) = -\log(-(x-1)) - \log(-(-x-1)) = -\log(1-x) - \log(1+x)
$$

**Gradient:**

$$
\nabla h_1(x) = 1, \quad \nabla h_2(x) = -1
$$

$$
\nabla \phi(x) = \frac{1}{1-x} + \frac{-1}{1+x} = \frac{1+x-(1-x)}{(1-x)(1+x)} = \frac{2x}{1-x^2}
$$

**Hessian:**

$$
\nabla^2 h_1(x) = 0, \quad \nabla^2 h_2(x) = 0
$$

$$
\nabla^2 \phi(x) = \frac{1}{(1-x)^2} + \frac{1}{(1+x)^2}
$$

$$
= \frac{(1+x)^2 + (1-x)^2}{(1-x^2)^2} = \frac{2(1+x^2)}{(1-x^2)^2}
$$

---

**c) Tại $$x = 0$$:**

$$
\phi(0) = -\log(1) - \log(1) = 0
$$

$$
\nabla \phi(0) = \frac{0}{1} = 0
$$

$$
\nabla^2 \phi(0) = \frac{2 \cdot 1}{1} = 2
$$

**Nhận xét:** Tại tâm miền khả thi ($$x = 0$$), hàm chắn đạt cực tiểu nên gradient bằng $$0$$.

</details>

---

### **Bài tập 2: Đường trung tâm (Boyd & Vandenberghe, Ex. 11.2)**

Tiếp tục Bài tập 1, xét bài toán chắn:

$$
\min_x \quad t f(x) + \phi(x) = t x^2 - \log(1-x) - \log(1+x)
$$

**Yêu cầu:**  
a) Viết điều kiện tối ưu bậc nhất (FOC).  
b) Giải điều kiện bậc nhất để tìm điểm đường trung tâm $$x^*(t)$$.  
c) Tính $$x^*(1)$$, $$x^*(10)$$, $$x^*(100)$$.  
d) Xác định giới hạn $$\lim_{t \to \infty} x^*(t)$$.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Điều kiện tối ưu bậc nhất (FOC):**

$$
\frac{d}{dx}\left( t x^2 - \log(1-x) - \log(1+x) \right) = 0
$$

$$
2tx + \frac{1}{1-x} - \frac{1}{1+x} = 0
$$

$$
2tx + \frac{2x}{1-x^2} = 0
$$

$$
x\left( 2t + \frac{2}{1-x^2} \right) = 0
$$

**Hai trường hợp:**
1. $$x = 0$$.
2. $$2t + \frac{2}{1-x^2} = 0$$ (vô nghiệm trên $$(-1, 1)$$ vì với mọi $$t > 0$$ và $$|x| < 1$$, vế trái luôn dương).

**Kết luận:** $$x^*(t) = 0$$ với mọi $$t > 0$$.

---

**b) Giải thích:**

Do cả hàm mục tiêu $$f(x) = x^2$$ lẫn miền khả thi $$(-1, 1)$$ đều đối xứng qua $$x = 0$$, đường trung tâm suy biến thành một điểm cố định $$x^*(t) = 0$$ với mọi $$t > 0$$.

---

**c) Các giá trị cụ thể:**

$$
x^*(1) = 0, \quad x^*(10) = 0, \quad x^*(100) = 0
$$

---

**d) Giới hạn khi $$t \to \infty$$:**

$$
\lim_{t \to \infty} x^*(t) = 0
$$

Đây chính là nghiệm của bài toán gốc: $$\min_{-1 \leq x \leq 1} x^2 = 0$$ đạt tại $$x = 0$$.

**Lưu ý:** Đây là trường hợp đặc biệt do tính đối xứng; tổng quát, điểm $$x^*(t)$$ sẽ dịch chuyển dọc theo đường trung tâm khi $$t$$ tăng.

</details>

---

## 📝 **Phần II: Phân tích đường trung tâm**

### **Bài tập 3: Đường trung tâm cho quy hoạch tuyến tính (Nocedal & Wright, Ex. 14.1)**

Xét bài toán quy hoạch tuyến tính (LP):

$$
\begin{align}
\min_{x} \quad & c^T x \\
\text{s.t.} \quad & Ax = b \\
& x \geq 0
\end{align}
$$

với $$c = \begin{bmatrix} -1 \\ -1 \end{bmatrix}$$, $$A = \begin{bmatrix} 1 & 1 \end{bmatrix}$$, $$b = 1$$.

**Yêu cầu:**  
a) Viết bài toán chắn tương ứng.  
b) Tìm đường trung tâm $$x^*(t)$$.  
c) Tính $$\lim_{t \to \infty} x^*(t)$$.  
d) Đối chiếu với bài toán đối ngẫu và tính khoảng cách đối ngẫu.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Bài toán chắn:**

$$
\min_x \quad t c^T x - \sum_{i=1}^2 \log x_i \quad \text{s.t.} \quad x_1 + x_2 = 1
$$

$$
= \min_x \quad -t(x_1 + x_2) - \log x_1 - \log x_2 \quad \text{s.t.} \quad x_1 + x_2 = 1
$$

---

**b) Tìm đường trung tâm:**

**Hàm Lagrange:**

$$
L(x, \nu) = -t(x_1 + x_2) - \log x_1 - \log x_2 - \nu(x_1 + x_2 - 1)
$$

**Điều kiện tối ưu bậc nhất:**

$$
\frac{\partial L}{\partial x_1} = -t - \frac{1}{x_1} - \nu = 0 \Rightarrow \frac{1}{x_1} = -t - \nu
$$

$$
\frac{\partial L}{\partial x_2} = -t - \frac{1}{x_2} - \nu = 0 \Rightarrow \frac{1}{x_2} = -t - \nu
$$

Từ hai phương trình trên suy ra $$x_1 = x_2$$. Kết hợp với $$x_1 + x_2 = 1$$, ta được $$x_1 = x_2 = 0.5$$.

**Đường trung tâm:**

$$
x^*(t) = \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix} \quad \forall t > 0
$$

**Biến đối ngẫu:**

$$
\frac{1}{0.5} = -t - \nu \Rightarrow \nu = -t - 2
$$

---

**c) Giới hạn khi $$t \to \infty$$:**

$$
\lim_{t \to \infty} x^*(t) = \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix}
$$

**Đối chiếu với bài toán gốc:**

$$
\min -x_1 - x_2 \quad \text{s.t.} \quad x_1 + x_2 = 1, \quad x \geq 0
$$

Giá trị tối ưu là $$-1$$ tại mọi điểm trên đoạn thẳng nối $$(0,1)$$ và $$(1,0)$$. Đường trung tâm hội tụ về **tâm giải tích (analytic center)** của tập nghiệm tối ưu là $$(0.5, 0.5)^T$$.

---

**d) Đối chiếu nguyên thủy–đối ngẫu:**

**Bài toán đối ngẫu:**

$$
\max_{\nu} \quad \nu \quad \text{s.t.} \quad \begin{bmatrix} \nu \\ \nu \end{bmatrix} \leq \begin{bmatrix} -1 \\ -1 \end{bmatrix}
$$

Điều kiện $$\nu \leq -1$$ cho nghiệm tối ưu đối ngẫu $$\nu^* = -1$$.

**Khoảng cách đối ngẫu:**

$$
\text{gap}(t) = c^T x^*(t) - b^T y(t)
$$

Điểm khả thi đối ngẫu suy ra từ đường trung tâm là $$\lambda_i(t) = \frac{1}{t x_i^*(t)} = \frac{2}{t}$$ và $$y(t) = \frac{\nu(t)}{t} = -1 - \frac{2}{t} \leq -1$$. Giá trị hàm mục tiêu đối ngẫu là $$b^Ty(t) = -1 - \frac{2}{t}$$, nên:

$$
\text{gap}(t) = -1 - \left(-1 - \frac{2}{t}\right) = \frac{2}{t} = \frac{m}{t}
$$

Khoảng cách đối ngẫu luôn dương với mọi $$t$$ hữu hạn và tiến về $$0$$ khi $$t \to \infty$$, khớp với công thức $$m/t$$ (ở đây $$m = 2$$).

**Lưu ý:** Công thức $$\text{gap} = m/t$$ luôn đúng dọc theo đường trung tâm; khoảng cách chỉ bằng $$0$$ khi đối chiếu với giá trị đối ngẫu tối ưu $$\nu^* = -1$$ ở giới hạn $$t \to \infty$$.

</details>

---

## 📝 **Phần III: Điều kiện KKT nhiễu**

### **Bài tập 4: Điều kiện KKT của bài toán chắn (Boyd & Vandenberghe, Ex. 11.4)**

Xét bài toán chắn:

$$
\min_x \quad t f(x) + \phi(x)
$$

**Yêu cầu:**  
a) Viết điều kiện tối ưu cho bài toán chắn.  
b) Chứng minh: Nếu $$x^*(t)$$ tối ưu cho bài toán chắn thì tồn tại $$\lambda^*(t)$$ thỏa mãn:

$$
\begin{align}
\nabla f(x^*(t)) + \sum_i \lambda_i^*(t) \nabla h_i(x^*(t)) &= 0 \\
\lambda_i^*(t) &= -\frac{1}{t h_i(x^*(t))} \\
h_i(x^*(t)) &< 0
\end{align}
$$

c) Tính tích $$\lambda_i^*(t) h_i(x^*(t))$$.  
d) Điều gì xảy ra khi $$t \to \infty$$?

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Điều kiện tối ưu cho bài toán chắn:**

$$
\min_x \quad t f(x) + \phi(x) = t f(x) - \sum_i \log(-h_i(x))
$$

Điều kiện tối ưu bậc nhất:

$$
t \nabla f(x) + \nabla \phi(x) = 0
$$

$$
t \nabla f(x) + \sum_i \frac{\nabla h_i(x)}{-h_i(x)} = 0
$$

---

**b) Chứng minh điều kiện KKT nhiễu:**

Đặt:

$$
\lambda_i^*(t) := -\frac{1}{t h_i(x^*(t))}
$$

Chia cả hai vế của điều kiện bậc nhất cho $$t > 0$$:

$$
t \nabla f(x^*) + \sum_i \frac{\nabla h_i(x^*)}{-h_i(x^*)} = 0
$$

$$
\nabla f(x^*) + \sum_i \frac{1}{-t h_i(x^*)} \nabla h_i(x^*) = 0
$$

$$
\nabla f(x^*) + \sum_i \left(-\frac{1}{t h_i(x^*)}\right) \nabla h_i(x^*) = 0
$$

$$
\nabla f(x^*) + \sum_i \lambda_i^*(t) \nabla h_i(x^*) = 0
$$

Đây chính là điều kiện dừng của hệ KKT.

**Khả thi nguyên thủy:** Vì $$x^*(t)$$ thuộc miền xác định của hàm chắn nên $$h_i(x^*(t)) < 0$$.

**Khả thi đối ngẫu:**

$$
\lambda_i^* = -\frac{1}{t h_i(x^*)} > 0 \quad \text{(vì } h_i(x^*) < 0 \text{ và } t > 0\text{)}
$$

---

**c) Độ lệch bù bị nhiễu:**

$$
\lambda_i^*(t) h_i(x^*(t)) = -\frac{1}{t h_i(x^*)} \cdot h_i(x^*) = -\frac{1}{t}
$$

Tích này khác $$0$$ mà bằng $$-1/t$$, nên được gọi là **điều kiện độ lệch bù nhiễu (perturbed complementary slackness)**.

---

**d) Giới hạn khi $$t \to \infty$$:**

$$
\lambda_i^*(t) h_i(x^*(t)) = -\frac{1}{t} \to 0
$$

Hệ điều kiện KKT nhiễu tiến về hệ điều kiện KKT chính xác của bài toán gốc, nên $$x^*(t) \to x^*$$ và $$\lambda^*(t) \to \lambda^*$$.

**Khoảng cách đối ngẫu:**

$$
\text{gap}(t) = f(x^*(t)) - g(\lambda^*(t), \nu^*(t)) = \frac{m}{t}
$$

với $$m$$ là số ràng buộc bất đẳng thức.

</details>

---

## 📝 **Phần IV: Phân tích hội tụ**

### **Bài tập 5: Khoảng cách đối ngẫu và hội tụ (Boyd & Vandenberghe, Theorem 11.2)**

Xét phương pháp chắn với tham số $$t^{(k)} = \mu^k t^{(0)}$$, trong đó $$\mu > 1$$.

**Yêu cầu:**  
a) Xác định khoảng cách đối ngẫu sau $$k$$ vòng lặp ngoài: $$\text{gap}^{(k)} = \frac{m}{t^{(k)}}$$.  
b) Để đạt $$\text{gap} < \epsilon$$, cần ít nhất bao nhiêu vòng lặp ngoài?  
c) Với $$m = 100$$, $$\mu = 10$$, $$\epsilon = 10^{-6}$$ (và $$t^{(0)} = 1$$), tính số vòng lặp ngoài.  
d) Ước lượng tổng số bước Newton (giả sử mỗi vòng lặp ngoài cần khoảng $$10$$ bước Newton).

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Khoảng cách đối ngẫu:**

Tại vòng lặp ngoài thứ $$k$$, điểm đường trung tâm $$x^*(t^{(k)})$$ thỏa mãn điều kiện KKT nhiễu:

$$
\lambda_i^*(t^{(k)}) h_i(x^*(t^{(k)})) = -\frac{1}{t^{(k)}}
$$

Khoảng cách đối ngẫu tương ứng là:

$$
\eta(t^{(k)}) = f(x^*(t^{(k)})) - g(\lambda^*(t^{(k)}), \nu^*(t^{(k)}))
$$

Theo lý thuyết phương pháp chắn (Boyd & Vandenberghe, Theorem 11.2):

$$
\eta(t) = \frac{m}{t}
$$

với $$m$$ là số ràng buộc bất đẳng thức.

---

**b) Số vòng lặp ngoài cần thiết:**

Điều kiện dừng: $$\frac{m}{t^{(k)}} < \epsilon \iff t^{(k)} > \frac{m}{\epsilon}$$.

Thay $$t^{(k)} = \mu^k t^{(0)}$$:

$$
\mu^k t^{(0)} > \frac{m}{\epsilon}
$$

$$
k > \frac{\log(m/(\epsilon t^{(0)}))}{\log \mu}
$$

Khi $$t^{(0)} = 1$$:

$$
k > \frac{\log(m/\epsilon)}{\log \mu}
$$

---

**c) Tính toán cụ thể:**

$$
k > \frac{\log(100/10^{-6})}{\log 10} = \frac{\log(10^8)}{\log 10} = 8
$$

Do đó cần $$k = 9$$ vòng lặp ngoài (tại $$k = 8$$ ta có $$\text{gap} = m/\mu^8 = 10^{-6} = \epsilon$$, chưa nhỏ hơn chặt $$\epsilon$$).

---

**d) Tổng số bước Newton ước lượng:**

Giả sử mỗi vòng lặp ngoài cần xấp xỉ $$10$$ bước Newton:

$$
\text{Tổng số bước Newton} \approx 9 \times 10 = 90
$$

**Nhận xét:**
- Với $$\mu$$ cố định, số vòng lặp ngoài là $$O(\log(m/\epsilon))$$.
- Với bước tăng ngắn $$\mu = 1 + 1/\sqrt{m}$$, cần $$O(\sqrt{m}\log(m/\epsilon))$$ vòng lặp ngoài nhưng mỗi vòng chỉ cần $$O(1)$$ bước Newton.
- Tổng độ phức tạp lý thuyết là $$O(\sqrt{m} \log(m/\epsilon))$$ bước Newton.

Với $$\mu = 10$$ (lớn), số vòng lặp ngoài ít nhưng mỗi vòng lặp ngoài có thể đòi hỏi nhiều bước Newton hơn.

</details>

---

## 📝 **Phần V: Tìm điểm khả thi và Phase I**

### **Bài tập 6: Phương pháp Phase I (Nocedal & Wright, Ex. 14.3)**

Tìm một điểm khả thi chặt cho hệ ràng buộc:

$$
\begin{align}
& x_1 + x_2 \leq 1 \\
& x_1 - x_2 \leq 0.5 \\
& -x_1 \leq 0 \\
& -x_2 \leq 0
\end{align}
$$

**Yêu cầu:**  
a) Viết bài toán Phase I:

$$
\min_{x, s} \quad s \quad \text{s.t.} \quad h_i(x) \leq s, \quad i=1,\ldots,m
$$

b) Giải bài toán Phase I.  
c) Nếu nghiệm thỏa $$s^* < 0$$, chỉ ra một điểm khả thi chặt.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Bài toán Phase I:**

$$
\begin{align}
\min_{x_1, x_2, s} \quad & s \\
\text{s.t.} \quad & x_1 + x_2 - 1 \leq s \\
& x_1 - x_2 - 0.5 \leq s \\
& -x_1 \leq s \\
& -x_2 \leq s
\end{align}
$$

Tương đương:

$$
\min_{x, s} \quad s \quad \text{s.t.} \quad h_i(x) - s \leq 0
$$

---

**b) Giải bài toán Phase I:**

Bài toán chắn tương ứng:

$$
\min_{x, s} \quad t \cdot s - \sum_i \log(-(h_i(x) - s))
$$

Khi $$t$$ lớn, nghiệm tiến về nghiệm của bài toán LP 3 biến $$(x_1, x_2, s)$$:

$$
\min_{x, s} \quad s \quad \text{s.t.} \quad h_i(x) \leq s
$$

tức $$s^* = \min_x \max_i h_i(x)$$.

Tại nghiệm tối ưu, ba ràng buộc $$h_1, h_3, h_4$$ cùng đạt dấu bằng:

$$x_1 + x_2 - 1 = -x_1 = -x_2 = s \;\Rightarrow\; x_1 = x_2 = -s,\quad -2s - 1 = s \;\Rightarrow\; s = -\tfrac{1}{3}$$

Suy ra nghiệm tối ưu là $$x^* = \left(\tfrac{1}{3}, \tfrac{1}{3}\right)$$ và $$s^* = -\tfrac{1}{3}$$.

**Kiểm tra:**

$$
\begin{align}
h_1 &= \tfrac{1}{3} + \tfrac{1}{3} - 1 = -\tfrac{1}{3} \\
h_2 &= \tfrac{1}{3} - \tfrac{1}{3} - 0.5 = -0.5 \\
h_3 &= -\tfrac{1}{3} \\
h_4 &= -\tfrac{1}{3}
\end{align}
$$

Do đó $$\max_i h_i = -\tfrac{1}{3}$$. (Lưu ý rằng điểm $$x = (0.25, 0.25)$$ cũng khả thi chặt với $$s = -0.25$$ nhưng chưa tối ưu cho Phase I vì $$-0.25 > -\tfrac{1}{3}$$.)

---

**c) Điểm khả thi chặt:**

Vì $$s^* = -\tfrac{1}{3} < 0$$, hệ ràng buộc khả thi chặt và điểm $$x = (\tfrac{1}{3}, \tfrac{1}{3})$$ thỏa mãn chặt cả bốn bất đẳng thức ($$h_i = -\tfrac{1}{3}, -0.5, -\tfrac{1}{3}, -\tfrac{1}{3} < 0$$).

Trong thực hành, không cần giải Phase I đến tối ưu tuyệt đối — chỉ cần dừng ngay khi tìm được một cặp $$(x, s)$$ có $$s < 0$$ (ví dụ $$x = (0.25, 0.25)$$ với $$s = -0.25$$) là đủ làm điểm khởi tạo cho phương pháp chắn.

</details>

---

## 📝 **Phần VI: Bài toán tổng hợp**

### **Bài tập 7: Tối ưu danh mục đầu tư bằng phương pháp chắn (Boyd & Vandenberghe, Ex. 11.10)**

Xét bài toán tối ưu danh mục đầu tư:

$$
\begin{align}
\min_x \quad & x^T \Sigma x \\
\text{s.t.} \quad & \mu^T x \geq r_{\min} \\
& \mathbf{1}^T x = 1 \\
& x \geq 0
\end{align}
$$

với $$\Sigma = \begin{bmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{bmatrix}$$, $$\mu = \begin{bmatrix} 0.10 \\ 0.15 \end{bmatrix}$$, $$r_{\min} = 0.12$$.

**Yêu cầu:**  
a) Viết bài toán chắn tương ứng.  
b) Xác định điểm đường trung tâm tại $$t = 1, 10, 100$$.  
c) Phân tích tốc độ hội tụ.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Bài toán chắn:**

Đưa các ràng buộc về dạng chuẩn:

$$
\begin{align}
\min_x \quad & x^T \Sigma x \\
\text{s.t.} \quad & -\mu^T x + r_{\min} \leq 0 \quad \text{(bất đẳng thức 1)} \\
& \mathbf{1}^T x = 1 \quad \text{(đẳng thức)} \\
& -x_i \leq 0, \quad i=1,2 \quad \text{(bất đẳng thức 2, 3)}
\end{align}
$$

**Hàm chắn logarit:**

$$
\phi(x) = -\log(-(-\mu^T x + r_{\min})) - \sum_{i=1}^2 \log x_i
$$

$$
= -\log(\mu^T x - r_{\min}) - \log x_1 - \log x_2
$$

**Bài toán chắn:**

$$
\min_x \quad t \cdot x^T \Sigma x - \log(\mu^T x - r_{\min}) - \log x_1 - \log x_2
$$

thỏa mãn $$\mathbf{1}^T x = 1$$.

---

**b) Đường trung tâm (tính số):**

**Hàm Lagrange:**

$$
L = t x^T \Sigma x - \log(\mu^T x - r_{\min}) - \sum_i \log x_i - \nu(x_1 + x_2 - 1)
$$

**Điều kiện tối ưu bậc nhất:**

$$
2t \Sigma x - \frac{\mu}{\mu^T x - r_{\min}} - \begin{bmatrix} 1/x_1 \\ 1/x_2 \end{bmatrix} - \nu \mathbf{1} = 0
$$

$$
x_1 + x_2 = 1
$$

Giải số hệ phương trình trên thu được các điểm xấp xỉ:

- **$$t = 1$$:** $$x^*(1) \approx (0.247, 0.753)$$ (với $$t$$ nhỏ, hàm chắn chi phối nên nghiệm gần tâm giải tích của miền khả thi).
- **$$t = 10$$:** $$x^*(10) \approx (0.282, 0.718)$$.
- **$$t = 100$$:** $$x^*(100) \approx (0.448, 0.552)$$ (và $$x^*(1000) \approx (0.571, 0.429)$$).

Khi $$t \to \infty$$, nghiệm hội tụ về $$x^* = (0.6, 0.4)$$ (tại đó ràng buộc lợi suất chặt: $$0.10(0.6) + 0.15(0.4) = 0.12$$ và phương sai tối ưu $$x^T\Sigma x = 0.0336$$).

---

**c) Phân tích hội tụ:**

Bài toán có $$m = 3$$ ràng buộc bất đẳng thức, nên khoảng cách đối ngẫu là:

$$
\text{gap}(t) = \frac{3}{t}
$$

- $$t = 1$$: $$\text{gap} = 3$$
- $$t = 10$$: $$\text{gap} = 0.3$$
- $$t = 100$$: $$\text{gap} = 0.03$$

Để đạt $$\text{gap} < 10^{-6}$$, cần $$t > 3 \times 10^6$$.

Với $$\mu = 10$$ và $$t^{(0)} = 1$$:

$$
k > \frac{\log(3 \times 10^6)}{\log 10} \approx 6.5 \Rightarrow k = 7 \text{ vòng lặp ngoài}
$$

</details>

---

## 💡 **Tổng kết và lưu ý thực hành**

### **Hàm chắn logarit:**
- $$\phi(x) = -\sum_i \log(-h_i(x))$$
- $$\nabla \phi(x) = \sum_i \frac{\nabla h_i(x)}{-h_i(x)}$$
- $$\phi(x) \to \infty$$ khi $$x$$ tiến sát biên

### **Đường trung tâm:**
- $$x^*(t)$$ là nghiệm của bài toán $$\min t f(x) + \phi(x)$$ (với $$Ax = b$$)
- Khi $$t \to \infty$$: $$x^*(t) \to x^*$$ (nghiệm tối ưu gốc)
- Đặc trưng bởi hệ điều kiện KKT nhiễu

### **Điều kiện KKT nhiễu:**
- $$\nabla f(x^*) + \sum_i \lambda_i^* \nabla h_i(x^*) = 0$$
- $$\lambda_i^* = -\frac{1}{t h_i(x^*)}$$
- $$\lambda_i^* h_i(x^*) = -\frac{1}{t} \to 0$$ khi $$t \to \infty$$

### **Phân tích hội tụ:**
- Khoảng cách đối ngẫu: $$\eta(t) = \frac{m}{t}$$
- Số vòng lặp ngoài: $$O(\log(m/\epsilon) / \log \mu)$$
- Với $$\mu = 10$$: cần xấp xỉ $$\log_{10}(m/\epsilon)$$ vòng lặp ngoài
- Mỗi vòng lặp ngoài giải bài toán chắn bằng phương pháp Newton

### **Phương pháp Phase I:**
- Mục tiêu: tìm điểm khởi tạo khả thi chặt
- Bài toán: $$\min_{x,s} s$$ thỏa mãn $$h_i(x) \leq s$$ (và $$Ax = b$$)
- Nếu $$s^* < 0$$: bài toán khả thi chặt và $$x^*$$ dùng làm điểm xuất phát

---

## 📚 **Tài liệu tham khảo**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 11.

2. **Nocedal, J., & Wright, S. J.** (2006). *Numerical Optimization* (2nd ed.). Springer. Chapter 14, 19.

3. **Nesterov, Y.** (2004). *Introductory Lectures on Convex Optimization*. Springer. Chapter 4.

4. **Wright, S. J.** (1997). *Primal-Dual Interior-Point Methods*. SIAM.

5. **Ben-Tal, A., & Nemirovski, A.** (2001). *Lectures on Modern Convex Optimization*. SIAM. Chapter 4.
