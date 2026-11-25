---
layout: post
title: "11-10 Bài Tập Thực Hành - Tính Đối Ngẫu Tổng Quát"
chapter: "11"
order: 11
owner: "GitHub Copilot"
lang: vi
categories:
  - chapter11
lesson_type: required
redirect_from:
  - /contents/vi/chapter11/11_08_Practical_Exercises_General_Duality/
---

Nếu muốn thực sự làm chủ đối ngẫu Lagrange — để gặp bất kỳ bài toán quy hoạch bậc hai, bài toán có hàm logarit, hay bài toán ràng buộc chuẩn nào cũng tự tin viết ra ngay hàm đối ngẫu và kiểm tra điều kiện Slater — không có con đường nào hiệu quả hơn là tự tay giải các bài tập kinh điển từ Boyd & Vandenberghe, Rockafellar và Bertsekas trong bài thực hành này!

Điểm thú vị nhất trong quá trình tự giải bài tập đối ngẫu là xử lý những **trường hợp biên (edge cases)** khi tính $$\inf_x L(x, u, v)$$: một biến mất bậc hai khiến biểu thức trở thành tuyến tính, hay miền xác định của $$\log(x)$$ đòi hỏi $$x > 0$$. Khung tính tay dưới đây chạy thử đúng tình huống kinh điển đó trên quy hoạch bậc hai 1 biến (gần với Bài tập 4) để bạn làm nóng tay trước khi vào bài!

## Bản đồ kiến thức nền: Bốn bước chuẩn mực để giải mọi bài tập đối ngẫu Lagrange

- **Bước 1 — Đưa về dạng chuẩn và xác định miền $$\mathcal{D}$$:** Viết mọi bất đẳng thức về dạng $$h_i(x) \le 0$$, đẳng thức về $$l_j(x) = 0$$, và ghi rõ miền xác định ẩn (ví dụ $$x > 0$$ cho $$\log x$$).
- **Bước 2 — Lập $$L(x, u, v)$$ và tìm $$\inf_x L(x, u, v)$$ cẩn thận theo từng miền tham số:** Giải $$\nabla_x L = 0$$ khi $$L$$ lồi và bức (coercive); luôn kiểm tra các giá trị $$(u, v)$$ làm cho $$\inf_x L = -\infty$$ để ghi rõ ràng buộc miền hữu dụng của bài toán đối ngẫu!
- **Bước 3 — Kiểm tra tính lồi và điều kiện Slater:** Xác nhận $$f, h_i$$ lồi và $$l_j$$ affine, sau đó chỉ ra tường minh một điểm $$\tilde{x}$$ thỏa $$h_i(\tilde{x}) < 0$$ (với $$h_i$$ phi tuyến) và $$l_j(\tilde{x}) = 0$$ để chốt đối ngẫu mạnh.
- **Bước 4 — Khôi phục nghiệm gốc $$x^*$$ từ nghiệm đối ngẫu $$(u^*, v^*)$$:** Khi $$L(x, u^*, v^*)$$ có cực tiểu duy nhất theo $$x$$ (chẳng hạn lồi chặt), điểm $$x^* = \arg\min_x L(x, u^*, v^*)$$ chính là nghiệm tối ưu gốc!

### Khung giải thích (nên đọc chậm): Giải tay trọn vẹn QP 1 biến với hai trường hợp $$q > 0$$ và $$q = 0$$

Xét bài toán $$\min_{x \in \mathbb{R}} \frac{1}{2}q x^2 + c x$$ với ràng buộc $$-x \le 0$$ (tức $$x \ge 0$$), trong đó $$q \ge 0$$.

1. **Lập hàm Lagrangian (nhân tử $$u \ge 0$$):**
   $$L(x, u) = \frac{1}{2}q x^2 + (c - u)x.$$
2. **Trường hợp $$q > 0$$ (parabol lồi chặt):**
   - Đạo hàm theo $$x$$ bằng $$0$$: $$qx + (c - u) = 0 \implies x(u) = -\frac{c - u}{q} = \frac{u - c}{q}$$.
   - Hàm đối ngẫu: $$g(u) = -\frac{(u - c)^2}{2q}$$ (xác định với mọi $$u \ge 0$$).
   - Cực đại hóa $$g(u)$$ trên $$u \ge 0$$:
     - Nếu $$c \ge 0$$: đỉnh parabol tại $$u^* = c \ge 0$$, cho $$g^* = 0$$ và $$x^* = (c - c)/q = 0$$.
     - Nếu $$c < 0$$: cực đại trên $$u \ge 0$$ đạt tại biên $$u^* = 0$$, cho $$g^* = -\frac{c^2}{2q}$$ và $$x^* = -c/q > 0$$!
3. **Trường hợp suy biến $$q = 0$$ (quay về LP!):**
   - $$L(x, u) = (c - u)x$$.
   - Infimum theo $$x \in \mathbb{R}$$ chỉ hữu hạn khi $$c - u = 0 \implies u = c$$!
   - Vì ta đòi $$u \ge 0$$, bài toán đối ngẫu chỉ khả thi khi $$c \ge 0$$ (cho $$g^* = 0$$), còn khi $$c < 0$$ thì đối ngẫu vô nghiệm (khớp hoàn toàn với việc bài toán gốc $$\min_{x \ge 0} cx = -\infty$$ không bị chặn dưới!).

# Bài Tập Thực Hành - Tính Đối Ngẫu Tổng Quát

Các bài tập dưới đây được tham khảo từ Boyd & Vandenberghe (2004), Rockafellar (1970) và Bertsekas (1999).

---

## Phần I: Hàm Lagrangian và hàm đối ngẫu

### Bài tập 1: Xây dựng hàm Lagrangian (Boyd & Vandenberghe, Ex. 5.1)

Cho bài toán tối ưu tổng quát:

$$
\begin{align}
\min_{x} \quad & f_0(x) \\
\text{s.t.} \quad & f_i(x) \leq 0, \quad i = 1, \ldots, m \\
& h_j(x) = 0, \quad j = 1, \ldots, p
\end{align}
$$

**Yêu cầu:**
a) Viết hàm Lagrangian $$L(x, \lambda, \nu)$$.
b) Định nghĩa hàm đối ngẫu $$g(\lambda, \nu)$$.
c) Cho $$f_0(x) = x_1^2 + x_2^2$$, $$f_1(x) = x_1 + x_2 - 1$$, $$h_1(x) = x_1 - x_2$$. Tính $$L$$ và $$g$$.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Hàm Lagrangian:**

$$
L(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{j=1}^p \nu_j h_j(x)
$$

với:
- $$\lambda \in \mathbb{R}^m, \lambda \geq 0$$: vector biến đối ngẫu cho các ràng buộc bất đẳng thức.
- $$\nu \in \mathbb{R}^p$$: vector biến đối ngẫu cho các ràng buộc đẳng thức (không ràng buộc dấu).

---

**b) Hàm đối ngẫu:**

$$
g(\lambda, \nu) = \inf_x L(x, \lambda, \nu) = \inf_x \left( f_0(x) + \sum_i \lambda_i f_i(x) + \sum_j \nu_j h_j(x) \right)
$$

**Tính chất:**
- $$g(\lambda, \nu)$$ luôn là hàm **lõm** theo $$(\lambda, \nu)$$.
- $$g(\lambda, \nu) \leq p^*$$ với mọi $$\lambda \geq 0$$ (tính đối ngẫu yếu).

---

**c) Tính cụ thể:**

Với $$f_0(x) = x_1^2 + x_2^2$$, $$f_1(x) = x_1 + x_2 - 1$$ và $$h_1(x) = x_1 - x_2$$:

**Hàm Lagrangian:**

$$
L(x, \lambda, \nu) = x_1^2 + x_2^2 + \lambda(x_1 + x_2 - 1) + \nu(x_1 - x_2)
$$

**Tìm $$\inf_x L$$:** Điều kiện đạo hàm bậc nhất (FOC):

$$
\frac{\partial L}{\partial x_1} = 2x_1 + \lambda + \nu = 0 \Rightarrow x_1 = -\frac{\lambda + \nu}{2}
$$

$$
\frac{\partial L}{\partial x_2} = 2x_2 + \lambda - \nu = 0 \Rightarrow x_2 = -\frac{\lambda - \nu}{2}
$$

Thế vào $$L$$, ta thu được:

$$
g(\lambda, \nu) = -\frac{\lambda^2 + \nu^2}{2} - \lambda
$$

với $$\lambda \geq 0$$.

</details>

---

### Bài tập 2: Đối ngẫu yếu và mạnh (Boyd & Vandenberghe, Ex. 5.2)

Xét bài toán gốc và hàm đối ngẫu từ Bài tập 1c.

**Yêu cầu:**
a) Giải bài toán gốc.
b) Giải bài toán đối ngẫu $$\max_{\lambda \geq 0, \nu} g(\lambda, \nu)$$.
c) Kiểm tra tính đối ngẫu mạnh.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Giải bài toán gốc:**

$$
\begin{align}
\min_{x} \quad & x_1^2 + x_2^2 \\
\text{s.t.} \quad & x_1 + x_2 \leq 1 \\
& x_1 - x_2 = 0
\end{align}
$$

Từ $$x_1 = x_2$$ và $$x_1 + x_2 \leq 1$$ suy ra $$x_1 \leq 0.5$$. Hàm mục tiêu trở thành $$2x_1^2$$, đạt cực tiểu tại $$x_1 = 0$$.

**Nghiệm bài toán gốc:** $$x^* = (0, 0)$$, $$p^* = 0$$.

---

**b) Giải bài toán đối ngẫu:**

$$
\max_{\lambda \geq 0, \nu} \quad -\frac{\lambda^2 + \nu^2}{2} - \lambda
$$

Điều kiện đạo hàm bậc nhất:
- $$\frac{\partial g}{\partial \lambda} = -\lambda - 1 = 0 \Rightarrow \lambda = -1$$. Vì ràng buộc $$\lambda \geq 0$$ và $$g$$ giảm trên $$[0, +\infty)$$, nên $$\lambda^* = 0$$.
- $$\frac{\partial g}{\partial \nu} = -\nu = 0 \Rightarrow \nu^* = 0$$.

**Nghiệm bài toán đối ngẫu:** $$\lambda^* = 0$$, $$\nu^* = 0$$, $$d^* = 0$$.

---

**c) Kiểm tra đối ngẫu mạnh:**

$$p^* = 0 = d^*$$

Tính đối ngẫu mạnh được thỏa mãn ✓ (bài toán lồi và thỏa mãn điều kiện Slater).

</details>

---

## Phần II: Điều kiện Slater và tính đối ngẫu mạnh

### Bài tập 3: Kiểm tra điều kiện Slater (Rockafellar, Ex. 28.3)

Kiểm tra điều kiện Slater cho các bài toán sau:

**a)** $$\min x^2$$ s.t. $$x^2 \leq 1$$

**b)** $$\min x^2$$ s.t. $$x^2 \leq 0$$

**c)** $$\min \frac{1}{2}x^T Q x$$ s.t. $$Ax \leq b$$ với $$Q \succ 0$$

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Điều kiện Slater:** Tồn tại điểm khả thi chặt $$\tilde{x}$$ sao cho:
- $$f_i(\tilde{x}) < 0$$ với mọi ràng buộc bất đẳng thức phi tuyến $$i$$ (ràng buộc bất đẳng thức affine chỉ cần $$\leq 0$$),
- $$h_j(\tilde{x}) = 0$$ với mọi ràng buộc đẳng thức $$j$$.

---

**a) $$\min x^2$$ s.t. $$x^2 \leq 1$$:**

Điều kiện khả thi chặt là $$\tilde{x}^2 < 1$$; chọn $$\tilde{x} = 0$$ thỏa mãn ✓.

**Điều kiện Slater thỏa mãn**, nên tính đối ngẫu mạnh đúng.

---

**b) $$\min x^2$$ s.t. $$x^2 \leq 0$$:**

Bất đẳng thức $$\tilde{x}^2 < 0$$ vô nghiệm, nên **điều kiện Slater không thỏa mãn**.

Miền khả thi chỉ gồm một điểm duy nhất $$x = 0$$. Tuy nhiên, trong ví dụ cụ thể này tính đối ngẫu mạnh vẫn đúng ($$p^* = d^* = 0$$), minh họa rằng điều kiện Slater chỉ là điều kiện đủ.

---

**c) QP với $$Q \succ 0$$, $$Ax \leq b$$:**

Dạng nguyên bản của điều kiện Slater đòi hỏi tồn tại $$\tilde{x}$$ thỏa $$A\tilde{x} < b$$ (tức $$\{x : Ax < b\} \neq \emptyset$$). Tuy nhiên, vì các ràng buộc $$Ax \leq b$$ đều là hàm **affine**, theo dạng mở rộng (refined Slater's condition), chỉ cần miền khả thi $$\{x : Ax \leq b\}$$ khác rỗng là đã đủ đảm bảo tính đối ngẫu mạnh.

</details>

---

## Phần III: Quy hoạch bậc hai (Quadratic Programming)

### Bài tập 4: Quy hoạch bậc hai một biến

**Đề bài:**
$$\min_x \frac{1}{2}x^2 + x \quad \text{s.t.} \quad x \geq 1$$

**Yêu cầu:**
1. Viết lại bài toán ở dạng chuẩn.
2. Xây dựng hàm Lagrangian.
3. Tính hàm đối ngẫu $$g(u)$$.
4. Giải bài toán đối ngẫu.
5. So sánh nghiệm gốc và nghiệm đối ngẫu.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Viết lại ở dạng chuẩn**
$$\min_x \frac{1}{2}x^2 + x \quad \text{s.t.} \quad -x + 1 \leq 0$$

**Bước 2: Hàm Lagrangian**
$$L(x,u) = \frac{1}{2}x^2 + x + u(-x + 1) = \frac{1}{2}x^2 + (1-u)x + u$$

**Bước 3: Hàm đối ngẫu**
$$g(u) = \inf_x L(x,u)$$

Lấy đạo hàm theo $$x$$: $$\frac{\partial L}{\partial x} = x + (1 - u) = 0 \Rightarrow x^* = u - 1$$.

Thay vào $$L$$: $$g(u) = -\frac{1}{2}(u - 1)^2 + u$$.

**Bước 4: Giải bài toán đối ngẫu**
$$\max_u g(u) \quad \text{s.t.} \quad u \geq 0$$

Ta có $$g'(u) = -(u - 1) + 1 = 2 - u = 0 \Rightarrow u^* = 2$$ (thỏa $$u^* \geq 0$$).

**Bước 5: So sánh nghiệm**
- Nghiệm đối ngẫu: $$u^* = 2$$, $$g^* = \frac{3}{2}$$.
- Nghiệm gốc: $$x^* = 1$$, $$f^* = \frac{3}{2}$$.
- Tính đối ngẫu mạnh thỏa mãn: $$f^* = g^*$$ ✓.

</details>

---

### Bài tập 5: Quy hoạch bậc hai nhiều ràng buộc

**Đề bài:**
$$\min_{x,y} x^2 + y^2 \quad \text{s.t.} \quad x + y \geq 2, \quad x \geq 0, \quad y \geq 0$$

**Yêu cầu:**
1. Xây dựng hàm Lagrangian đầy đủ.
2. Viết các điều kiện KKT.
3. Giải tìm nghiệm tối ưu gốc và đối ngẫu.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Hàm Lagrangian:**
$$L(x,y,u_1,u_2,u_3) = x^2 + y^2 + u_1(-x - y + 2) + u_2(-x) + u_3(-y)$$

**Điều kiện KKT:**
- Dừng (stationarity): $$\frac{\partial L}{\partial x} = 2x - u_1 - u_2 = 0$$ và $$\frac{\partial L}{\partial y} = 2y - u_1 - u_3 = 0$$.
- Điều kiện bù: $$u_1(-x - y + 2) = 0$$, $$u_2 x = 0$$, $$u_3 y = 0$$.
- Khả thi gốc và đối ngẫu ($$u_1, u_2, u_3 \geq 0$$).

**Nghiệm:** $$x^* = y^* = 1$$, $$(u_1^*, u_2^*, u_3^*) = (2, 0, 0)$$.

</details>

---

## Phần IV: Đối ngẫu của Support Vector Machine (SVM)

### Bài tập 6: Dạng đối ngẫu của SVM (Boyd & Vandenberghe, Ex. 8.6)

Cho bài toán SVM lề cứng:

$$
\begin{align}
\min_{w, b} \quad & \frac{1}{2}\|w\|^2 \\
\text{s.t.} \quad & y_i(w^T x_i + b) \geq 1, \quad i = 1, \ldots, m
\end{align}
$$

**Yêu cầu:**
a) Viết hàm Lagrangian.
b) Tính hàm đối ngẫu $$g(\alpha)$$.
c) Viết bài toán đối ngẫu.
d) Với 3 điểm dữ liệu $$(1, 1, +1)$$, $$(1, -1, +1)$$ và $$(-1, 0, -1)$$, tìm nghiệm đối ngẫu tối ưu.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Hàm Lagrangian:**

$$
L(w, b, \alpha) = \frac{1}{2}\|w\|^2 - \sum_{i=1}^m \alpha_i (y_i(w^T x_i + b) - 1)
$$

**b) Hàm đối ngẫu:**

Điều kiện dừng theo $$w$$ và $$b$$ cho: $$w = \sum_i \alpha_i y_i x_i$$ và $$\sum_i \alpha_i y_i = 0$$.

Thế vào $$L$$, ta được:

$$
g(\alpha) = \sum_i \alpha_i - \frac{1}{2}\sum_{i,j} \alpha_i \alpha_j y_i y_j x_i^T x_j
$$

**c) Bài toán đối ngẫu:**

$$
\boxed{
\begin{align}
\max_{\alpha} \quad & \sum_i \alpha_i - \frac{1}{2}\sum_{i,j} \alpha_i \alpha_j y_i y_j x_i^T x_j \\
\text{s.t.} \quad & \sum_i \alpha_i y_i = 0 \\
& \alpha_i \geq 0
\end{align}
}
$$

**d) Tính cụ thể:** Cả 3 điểm đều là vector hỗ trợ (support vector). Từ $$w = \sum_i \alpha_i y_i x_i$$, $$\sum_i \alpha_i y_i = 0$$ và $$y_i(w^T x_i + b) = 1$$, ta giải được $$\alpha^* = (1/4,\ 1/4,\ 1/2)$$, $$w^* = (1, 0)^T$$, $$b^* = 0$$, với giá trị đối ngẫu $$1 - \frac{1}{2}\|w^*\|^2 = \frac{1}{2}$$. Biên quyết định là đường thẳng $$x_1 = 0$$.

</details>

---

## Phần V: Điều kiện bù và khoảng cách đối ngẫu

### Bài tập 7: Áp dụng điều kiện bù

Cho bài toán LP:

$$
\begin{align}
\min_x \quad & c^T x \\
\text{s.t.} \quad & Ax = b \\
& x \geq 0
\end{align}
$$

**Yêu cầu:**
a) Viết điều kiện bù (complementary slackness).
b) Cho $$c = \begin{bmatrix} -1 \\ -2 \end{bmatrix}$$, $$A = \begin{bmatrix} 1 & 1 \end{bmatrix}$$, $$b = 1$$, tìm nghiệm tối ưu gốc và đối ngẫu.
c) Kiểm tra điều kiện bù.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Điều kiện bù:**

$$\lambda_i^* \cdot (-x_i^*) = 0$$

**Ý nghĩa:**
- Nếu $$x_i^* > 0$$ thì $$\lambda_i^* = 0$$.
- Nếu $$\lambda_i^* > 0$$ thì $$x_i^* = 0$$.

---

**b) Giải bài toán:**

$$\min \quad -x_1 - 2x_2 \quad \text{s.t.} \quad x_1 + x_2 = 1, \quad x \geq 0$$

Tương đương với cực đại hóa $$x_1 + 2x_2$$ trên đoạn $$x_1 + x_2 = 1, x \geq 0$$.

- **Nghiệm gốc:** $$x^* = (0, 1)^T$$, $$p^* = -2$$.
- **Nghiệm đối ngẫu:** $$\nu^* = -2$$, $$\lambda^* = (1, 0)^T$$.

**c) Kiểm tra điều kiện bù:**
- $$\lambda_1^* \cdot 0 = 0$$ ✓
- $$\lambda_2^* \cdot (-1) = 0$$ ✓

</details>

---

### Bài tập 8: Phân tích khoảng cách đối ngẫu (Bertsekas, Ex. 6.1.2)

Cho bài toán (lưu ý $$x(x-2) = x^2 - 2x$$ là hàm lồi):

$$
\min_{x \in [0,2]} \quad x(x-2)
$$

**Yêu cầu:**
a) Giải bài toán gốc.
b) Viết hàm Lagrangian và tìm hàm đối ngẫu.
c) Giải bài toán đối ngẫu.
d) Tính khoảng cách đối ngẫu.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Giải bài toán gốc:**

$$f(x) = x^2 - 2x = (x-1)^2 - 1$$

Hàm đạt cực tiểu tại $$x = 1 \in [0, 2]$$ với $$p^* = -1$$.

---

**b) Hàm Lagrangian:**

Viết lại bài toán: $$\min_x x^2 - 2x$$ s.t. $$-x \leq 0$$, $$x - 2 \leq 0$$.

$$L(x, \lambda_1, \lambda_2) = x^2 - 2x - \lambda_1 x + \lambda_2(x - 2)$$

**c) Giải bài toán đối ngẫu:**

Cực tiểu hóa theo $$x$$ cho $$x = \frac{2 + \lambda_1 - \lambda_2}{2}$$, suy ra $$g(\lambda_1, \lambda_2) = -\frac{(2 + \lambda_1 - \lambda_2)^2}{4} - 2\lambda_2$$. Trên miền $$\lambda \geq 0$$, $$g$$ đạt cực đại tại $$\lambda_1 = \lambda_2 = 0$$ với $$d^* = g(0, 0) = -1$$.

**d) Khoảng cách đối ngẫu:**

$$\text{Gap} = p^* - d^* = -1 - (-1) = 0$$. Bài toán lồi và thỏa mãn điều kiện Slater (ví dụ $$x = 1$$ thỏa chặt cả hai bất đẳng thức), nên tính đối ngẫu mạnh đúng. Vì nghiệm $$x^* = 1$$ nằm trong phần trong của miền khả thi, cả hai ràng buộc đều lỏng nên $$\lambda^* = 0$$ (phù hợp điều kiện bù).

</details>

---

## Phần VI: Xấp xỉ chuẩn và tối ưu entropy

### Bài tập 9: Xấp xỉ chuẩn (Boyd & Vandenberghe, Ex. 5.3)

**Đề bài:**
$$\min_x \lVert Ax - b \rVert$$

với chuẩn lần lượt là $$\ell_1, \ell_2$$ và $$\ell_\infty$$.

**Yêu cầu:**
1. Biến đổi thành bài toán có ràng buộc.
2. Xây dựng bài toán đối ngẫu cho từng trường hợp.
3. So sánh các bài toán đối ngẫu thu được.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Trường hợp 1: Chuẩn $$\ell_1$$**

$$\min_{x,t} \mathbf{1}^T t \quad \text{s.t.} \quad -t \leq Ax - b \leq t$$

Bài toán đối ngẫu:
$$\max_{\lambda,\mu} -b^T(\lambda - \mu) \quad \text{s.t.} \quad A^T(\lambda - \mu) = 0, \quad \lambda + \mu = \mathbf{1}, \quad \lambda,\mu \geq 0$$

---

**Trường hợp 2: Chuẩn $$\ell_2$$**

$$\min_{x,t} t \quad \text{s.t.} \quad \lVert Ax - b \rVert_2 \leq t$$

Bài toán đối ngẫu:
$$\max_{\nu} -b^T \nu \quad \text{s.t.} \quad A^T \nu = 0, \quad \lVert \nu \rVert_2 \leq 1$$

---

**Trường hợp 3: Chuẩn $$\ell_\infty$$**

$$\min_{x,t} t \quad \text{s.t.} \quad -t\mathbf{1} \leq Ax - b \leq t\mathbf{1}$$

Bài toán đối ngẫu:
$$\max_{\lambda,\mu} -b^T(\lambda - \mu) \quad \text{s.t.} \quad A^T(\lambda - \mu) = 0, \quad \lVert \lambda - \mu \rVert_1 \leq 1$$

</details>

---

### Bài tập 10: Cực đại hóa entropy (Boyd & Vandenberghe, Ex. 5.4)

**Đề bài:**
$$\max_x -\sum_{i=1}^n x_i \log x_i \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$

**Yêu cầu:**
1. Chuyển về bài toán cực tiểu hóa.
2. Xây dựng hàm Lagrangian.
3. Tính hàm đối ngẫu.
4. Tìm dạng nghiệm tối ưu.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Chuyển đổi:**
$$\min_x \sum_{i=1}^n x_i \log x_i \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$

**Hàm Lagrangian:**
$$L(x,\nu,\lambda) = \sum_{i=1}^n x_i \log x_i + \nu^T(Ax - b) - \lambda^T x$$

**Điều kiện dừng:**
$$\frac{\partial L}{\partial x_i} = \log x_i + 1 + (A^T \nu)_i - \lambda_i = 0$$

Suy ra: $$x_i = e^{-(A^T \nu)_i + \lambda_i - 1}$$.

**Điều kiện bù:**
Vì $$x_i = e^{\cdots} > 0$$ nên $$\lambda_i = 0$$, dẫn đến $$x_i = e^{-(A^T \nu)_i - 1}$$. Hàm đối ngẫu là $$g(\nu) = -b^T \nu - \sum_{i=1}^n e^{-(A^T \nu)_i - 1}$$; ta giải bài toán không ràng buộc $$\max_\nu g(\nu)$$ rồi thế ngược lại để thu được $$x^*$$.

</details>

---

## Phần VII: Bài tập tính toán cụ thể với nhân tử Lagrange

### Bài tập 11: Tối ưu danh mục đầu tư với biến đối ngẫu

**Đề bài:** Một nhà đầu tư có 100 triệu đồng muốn phân bổ vào 3 tài sản với:
- Vector lợi nhuận kỳ vọng: $$r = (12\%, 8\%, 5\%)^T$$
- Ma trận hiệp phương sai rủi ro: $$\Sigma = \begin{bmatrix} 0.04 & 0.01 & 0 \\ 0.01 & 0.02 & 0 \\ 0 & 0 & 0.01 \end{bmatrix}$$

Bài toán: $$\min_x \frac{1}{2}x^T \Sigma x$$ s.t. $$r^T x \geq 10\%$$, $$\mathbf{1}^T x = 1$$, $$x \geq 0$$.

**Yêu cầu:**
a) Viết hàm Lagrangian với đầy đủ các ràng buộc.
b) Viết hệ điều kiện KKT.
c) Giải tìm phân bổ tối ưu $$x^*$$.
d) Tính các biến đối ngẫu và giải thích ý nghĩa kinh tế.

<details markdown="1">
<summary><strong>Lời giải chi tiết từng bước</strong></summary>

**a) Hàm Lagrangian:**

$$
L(x, \lambda_1, \nu, \lambda_2) = \frac{1}{2}x^T \Sigma x - \lambda_1(r^T x - 0.1) + \nu(\mathbf{1}^T x - 1) - \lambda_2^T x
$$

với $$\lambda_1, \lambda_2 \geq 0$$.

---

**b) Điều kiện KKT:**

- **Điều kiện dừng (Stationarity):** $$\nabla_x L = \Sigma x - \lambda_1 r + \nu \mathbf{1} - \lambda_2 = 0$$.
- **Khả thi gốc:** $$r^T x \geq 0.1$$, $$\mathbf{1}^T x = 1$$, $$x \geq 0$$.
- **Khả thi đối ngẫu:** $$\lambda_1, \lambda_2 \geq 0$$.
- **Điều kiện bù:** $$\lambda_1(r^T x - 0.1) = 0$$ và $$\lambda_{2i} x_i = 0$$ với mọi $$i$$.

---

**c) Giải bài toán:**

Giả sử ràng buộc lợi nhuận chặt ($$r^T x = 0.1$$) và mọi $$x_i > 0$$ (không bán khống). Khi đó từ điều kiện bù suy ra $$\lambda_2 = 0$$, và điều kiện dừng trở thành $$\Sigma x = \lambda_1 r - \nu \mathbf{1}$$:

$$
\begin{bmatrix} 0.04 & 0.01 & 0 \\ 0.01 & 0.02 & 0 \\ 0 & 0 & 0.01 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \lambda_1 \begin{bmatrix} 0.12 \\ 0.08 \\ 0.05 \end{bmatrix} - \nu \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}
$$

Kết hợp với hai ràng buộc $$x_1 + x_2 + x_3 = 1$$ và $$0.12x_1 + 0.08x_2 + 0.05x_3 = 0.1$$ (suy ra $$x_3 = 1 - x_1 - x_2$$ và $$0.07x_1 + 0.03x_2 = 0.05$$), ta giải hệ 5 phương trình tuyến tính 5 ẩn:

$$
x^* = \begin{bmatrix} 7/12 \\ 11/36 \\ 1/9 \end{bmatrix} \approx \begin{bmatrix} 0.583 \\ 0.306 \\ 0.111 \end{bmatrix}, \quad \lambda_1^* = \frac{13}{36} \approx 0.361, \quad \nu^* = \frac{61}{3600} \approx 0.017
$$

**Kiểm tra:**
- Lợi nhuận: $$0.12 \cdot \frac{7}{12} + 0.08 \cdot \frac{11}{36} + 0.05 \cdot \frac{1}{9} = 0.1$$ ✓; tổng tỷ trọng $$= 1$$ ✓; mọi $$x_i > 0$$ ✓ (giả thiết ban đầu đúng).
- Giá trị hàm mục tiêu rủi ro: $$\frac{1}{2}x^{*T}\Sigma x^* = \frac{23}{2400} \approx 0.00958$$.

---

**d) Ý nghĩa kinh tế:**

- $$\lambda_1^* \approx 0.361$$ là **giá bóng của ràng buộc lợi nhuận**: nếu nâng yêu cầu lợi nhuận từ 10% lên 11%, giá trị rủi ro tối ưu tăng thêm khoảng $$0.361 \times 0.01 \approx 0.0036$$.
- $$\nu^* \approx 0.017$$ là **độ nhạy theo ràng buộc ngân sách**: nếu thay $$\mathbf{1}^T x = 1$$ bằng $$1 + \delta$$ (với $$\delta$$ nhỏ), rủi ro tối ưu thay đổi khoảng $$-\nu^* \delta$$.
- $$\lambda_2 = 0$$: không có tài sản nào chạm biên không bán khống.

**Phân bổ tối ưu:** khoảng 58,3% vào tài sản 1, 30,6% vào tài sản 2 và 11,1% vào tài sản 3 (tương ứng khoảng 58,3 / 30,6 / 11,1 triệu đồng).

</details>

---

### Bài tập 12: Sản xuất tối ưu với nhân tử Lagrange

**Đề bài:** Một công ty sản xuất 2 sản phẩm A và B:
- Lợi nhuận: sản phẩm A đạt 40 nghìn/đơn vị, sản phẩm B đạt 30 nghìn/đơn vị.
- Ràng buộc nguồn lực:
  - Lao động: $$2A + B \leq 100$$ giờ
  - Vật liệu: $$A + 2B \leq 80$$ kg
  - Máy móc: $$A \leq 40$$ sản phẩm

Bài toán: $$\max_{x_1, x_2} 40x_1 + 30x_2$$ với các ràng buộc trên và $$x_1, x_2 \geq 0$$.

**Yêu cầu:**
a) Chuyển về bài toán cực tiểu hóa và viết hàm Lagrangian.
b) Tìm nghiệm tối ưu bằng điều kiện KKT.
c) Tính giá bóng của từng nguồn lực.
d) Nếu có thể mua thêm 10 giờ lao động với giá 8 nghìn/giờ, có nên mua không?

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Chuyển về bài toán cực tiểu hóa:**

$$\min_{x_1, x_2} -40x_1 - 30x_2$$
$$\text{s.t.} \quad 2x_1 + x_2 \leq 100, \quad x_1 + 2x_2 \leq 80, \quad x_1 \leq 40, \quad x_1, x_2 \geq 0$$

**Hàm Lagrangian:**

$$
L(x, \lambda) = -40x_1 - 30x_2 + \lambda_1(2x_1 + x_2 - 100) + \lambda_2(x_1 + 2x_2 - 80) + \lambda_3(x_1 - 40)
$$

---

**b) Điều kiện KKT:**

- **Điều kiện dừng:**
  $$\frac{\partial L}{\partial x_1} = -40 + 2\lambda_1 + \lambda_2 + \lambda_3 = 0$$
  $$\frac{\partial L}{\partial x_2} = -30 + \lambda_1 + 2\lambda_2 = 0$$
- **Điều kiện bù:**
  $$\lambda_1(2x_1 + x_2 - 100) = 0$$
  $$\lambda_2(x_1 + 2x_2 - 80) = 0$$
  $$\lambda_3(x_1 - 40) = 0$$

**Nhận xét:** Đỉnh $$(40, 20)$$ làm **cả ba** ràng buộc đều chặt cùng lúc: $$2(40) + 20 = 100$$, $$40 + 2(20) = 80$$, $$x_1 = 40$$. Đây là một đỉnh suy biến (degenerate).

So sánh giá trị lợi nhuận tại các đỉnh của miền khả thi: $$(0, 0) \to 0$$, $$(0, 40) \to 1200$$, $$(40, 20) \to 2200$$, $$(40, 0) \to 1600$$.

**Nghiệm tối ưu:** $$x_1^* = 40$$, $$x_2^* = 20$$, lợi nhuận $$40(40) + 30(20) = 2200$$ nghìn đồng.

**Nhân tử KKT:** Vì $$x_1^*, x_2^* > 0$$, điều kiện dừng cho hệ:

$$2\lambda_1 + \lambda_2 + \lambda_3 = 40$$
$$\lambda_1 + 2\lambda_2 = 30$$

Đặt $$\lambda_2 = s$$, ta có $$\lambda_1 = 30 - 2s$$ và $$\lambda_3 = 3s - 20$$. Điều kiện $$\lambda \geq 0$$ suy ra $$20/3 \leq s \leq 15$$, nên tập nhân tử đối ngẫu **không duy nhất** (do suy biến). Ví dụ:
- $$s = 20/3$$: $$\lambda = (50/3,\ 20/3,\ 0)$$
- $$s = 10$$: $$\lambda = (10,\ 10,\ 10)$$
- $$s = 15$$: $$\lambda = (0,\ 15,\ 25)$$

Mọi lựa chọn hợp lệ đều cho cùng giá trị đối ngẫu $$100\lambda_1 + 80\lambda_2 + 40\lambda_3 = 2200$$ ✓ (đối ngẫu mạnh).

---

**c) Giá bóng của từng nguồn lực:**

Vì nhân tử đối ngẫu không duy nhất, giá bóng chỉ có ý nghĩa **một phía**:
- **Lao động:** $$\lambda_1 \in [0,\ 50/3]$$. Giảm 1 giờ lao động làm lợi nhuận giảm $$50/3 \approx 16{,}7$$ nghìn đồng, nhưng **tăng** thêm 1 giờ thì lợi nhuận tăng **0**.
- **Vật liệu:** $$\lambda_2 \in [20/3,\ 15]$$. Tăng 1 kg làm lợi nhuận tăng $$20/3 \approx 6{,}7$$ nghìn đồng; giảm 1 kg làm lợi nhuận giảm 15 nghìn đồng.
- **Máy móc:** $$\lambda_3 \in [0,\ 25]$$. Nới $$x_1 \leq 40$$ thêm 1 đơn vị không làm tăng lợi nhuận (vì ràng buộc lao động lập tức chặn lại); siết lại 1 đơn vị làm giảm 25 nghìn đồng.

---

**d) Quyết định mua thêm lao động:**

Khi tăng quỹ lao động lên 110 giờ, hai ràng buộc $$x_1 \leq 40$$ và $$x_1 + 2x_2 \leq 80$$ vẫn giữ nguyên nghiệm tối ưu tại $$(40, 20)$$ với lợi nhuận 2200 nghìn đồng; tức giá bóng **theo chiều tăng** của lao động bằng 0.

Chi phí bỏ ra là $$10 \times 8 = 80$$ nghìn đồng trong khi lợi ích thu thêm bằng 0.

**Kết luận:** ❌ **Không nên mua.** Việc mua thêm 10 giờ lao động gây lỗ 80 nghìn đồng; nút thắt thực sự nằm ở vật liệu và máy móc.

**Lưu ý:** Tại đỉnh suy biến, đạo hàm trái và đạo hàm phải của giá trị tối ưu theo từng nguồn lực có thể khác nhau, nên cần kiểm tra miền độ nhạy trước khi áp dụng giá bóng.

</details>

---

## Tổng kết chiến lược giải bài tập

### Đối ngẫu Lagrange
- **Hàm Lagrangian:** $$L(x, \lambda, \nu) = f_0(x) + \sum_i \lambda_i f_i(x) + \sum_j \nu_j h_j(x)$$
- **Hàm đối ngẫu:** $$g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$$
- **Bài toán đối ngẫu:** $$\max_{\lambda \geq 0, \nu} g(\lambda, \nu)$$

### Quan hệ đối ngẫu
- **Đối ngẫu yếu:** $$d^* \leq p^*$$ luôn đúng.
- **Đối ngẫu mạnh:** $$d^* = p^*$$ (ví dụ khi bài toán lồi và thỏa điều kiện Slater).
- **Khoảng cách đối ngẫu:** $$p^* - d^* \geq 0$$.

### Điều kiện bù
- $$\lambda_i^* f_i(x^*) = 0$$ với mọi $$i$$.
- Ràng buộc chặt (active) có thể có $$\lambda_i^* > 0$$.
- Ràng buộc lỏng (inactive) bắt buộc có $$\lambda_i^* = 0$$.

### Khi nào nên giải qua bài toán đối ngẫu
- Bài toán đối ngẫu có cấu trúc đơn giản hơn hoặc ít biến hơn (ví dụ SVM khi số mẫu nhỏ hơn số đặc trưng).
- Cần phân tích độ nhạy thông qua giá bóng.
- Cần khoảng cách đối ngẫu làm tiêu chí dừng trong các thuật toán điểm trong (interior-point).

---

## Tài liệu tham khảo

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 5.

2. **Rockafellar, R. T.** (1970). *Convex Analysis*. Princeton University Press. Chapter 28.

3. **Bertsekas, D. P.** (1999). *Nonlinear Programming* (2nd ed.). Athena Scientific. Chapter 6.

4. **Luenberger, D. G., & Ye, Y.** (2008). *Linear and Nonlinear Programming* (3rd ed.). Springer.

5. **Bazaraa, M. S., Sherali, H. D., & Shetty, C. M.** (2006). *Nonlinear Programming: Theory and Algorithms* (3rd ed.). Wiley.
