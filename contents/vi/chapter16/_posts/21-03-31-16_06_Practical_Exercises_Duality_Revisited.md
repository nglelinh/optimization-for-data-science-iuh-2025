---
layout: post
title: 16-06 Bài Tập Thực Hành - Duality Revisited
chapter: '16'
order: 7
owner: GitHub Copilot
lang: vi
categories:
- chapter16
lesson_type: required
redirect_from:
  - /contents/vi/chapter16/16_05_Practical_Exercises_Duality_Revisited/
---

# Bài Tập Thực Hành - Tính đối ngẫu (Nhìn lại)

Các bài tập được tham khảo từ Boyd & Vandenberghe (2004) và Rockafellar (1970).

---

## 📝 **Bài tập 1: Phân tích nhiễu loạn (Perturbation Analysis)**

Cho bài toán:

$$
\begin{align}
\min_{x} \quad & x^2 \\
\text{s.t.} \quad & x \geq u
\end{align}
$$

**Yêu cầu:**  
a) Tìm hàm giá trị tối ưu $$p^*(u)$$ theo tham số $$u$$.  
b) Kiểm chứng $$\lambda^* = \frac{dp^*}{du}$$ (ràng buộc $$u - x \leq 0$$ càng chặt khi $$u$$ tăng).  
c) Giải thích ý nghĩa kinh tế của nhân tử $$\lambda^*$$.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Hàm giá trị tối ưu:**

$$p^*(u) = \begin{cases}
u^2 & \text{if } u \geq 0 \\
0 & \text{if } u < 0
\end{cases}$$

**b) Đạo hàm:**

$$\frac{dp^*}{du} = \begin{cases}
2u & \text{if } u > 0 \\
0 & \text{if } u < 0
\end{cases}$$

**Hàm Lagrange:**

$$L(x, \lambda) = x^2 - \lambda(x - u)$$

Điều kiện KKT: $$2x^* - \lambda^* = 0$$, $$\lambda^*(x^* - u) = 0$$.

- Nếu $$u \geq 0$$: $$x^* = u$$, $$\lambda^* = 2u = \frac{dp^*}{du}$$ ✓
- Nếu $$u < 0$$: $$x^* = 0$$, $$\lambda^* = 0$$ ✓

**c) Ý nghĩa:** $$\lambda^*$$ biểu thị độ nhạy (giá bóng — shadow price) của chi phí tối ưu khi mức ràng buộc $$u$$ thay đổi.

</details>

---

## 📝 **Bài tập 2: Tính đối ngẫu mạnh qua điều kiện Slater**

Cho bài toán QCQP:

$$
\begin{align}
\min_{x} \quad & x_1^2 + x_2^2 \\
\text{s.t.} \quad & (x_1 - 1)^2 + x_2^2 \leq 1 \\
& x_1 + x_2 \geq 1
\end{align}
$$

**Yêu cầu:**  
a) Kiểm tra điều kiện Slater.  
b) Viết bài toán đối ngẫu.  
c) Kiểm chứng tính đối ngẫu mạnh.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Kiểm tra điều kiện Slater:**

Cần tìm một điểm $$\tilde{x}$$ khả thi ngặt:

$$
\begin{cases}
(x_1 - 1)^2 + x_2^2 < 1 \\
x_1 + x_2 > 1
\end{cases}
$$

Chọn thử $$\tilde{x} = (1, 0.5)$$:

$$(1-1)^2 + (0.5)^2 = 0.25 < 1$$ ✓

$$1 + 0.5 = 1.5 > 1$$ ✓

**Điều kiện Slater được thỏa mãn**, suy ra tính đối ngẫu mạnh đúng.

---

**b) Hàm Lagrange:**

$$L(x, \lambda_1, \lambda_2) = x_1^2 + x_2^2 + \lambda_1[(x_1-1)^2 + x_2^2 - 1] - \lambda_2(x_1 + x_2 - 1)$$

**Hàm đối ngẫu:**

$$g(\lambda_1, \lambda_2) = \inf_x L(x, \lambda)$$

Điều kiện dừng KKT $$\nabla_x L = 0$$:

$$2x_1 + 2\lambda_1(x_1 - 1) - \lambda_2 = 0$$

$$2x_2 + 2\lambda_1 x_2 - \lambda_2 = 0$$

---

**c) Kiểm chứng bằng số:**

Nghiệm tối ưu nguyên thủy: $$x^* = (0.5, 0.5)$$, $$p^* = 0.5$$ (ràng buộc hình đĩa không tác dụng vì $$(0.5-1)^2 + 0.5^2 = 0.5 < 1$$).

Nghiệm tối ưu đối ngẫu: $$\lambda^* = (0, 1)$$, $$d^* = 0.5$$ (từ $$g(0, \lambda_2) = \lambda_2 - \lambda_2^2/2$$, đạt cực đại tại $$\lambda_2 = 1$$).

**Khoảng cách đối ngẫu:** $$p^* - d^* = 0$$ ✓ (thỏa mãn tính đối ngẫu mạnh).

</details>

---

## 📝 **Bài tập 3: Nón đối ngẫu và đối ngẫu nón (Conic Duality)**

Cho nón bậc hai (second-order cone): $$K = \{(x, t) : \|x\| \leq t\}$$.

**Yêu cầu:**  
a) Tìm nón đối ngẫu $$K^*$$.  
b) Kiểm chứng $$K^{**} = K$$ (tính tự đối ngẫu).  
c) Áp dụng cho tính đối ngẫu của bài toán SOCP.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Nón đối ngẫu:**

$$K^* = \{(y, s) : \langle (x,t), (y,s) \rangle \geq 0 \, \forall (x,t) \in K\}$$

$$= \{(y, s) : x^Ty + ts \geq 0 \, \forall \|x\| \leq t\}$$

Xét trường hợp bất lợi nhất $$x = -t\frac{y}{\|y\|}$$ (với $$y \neq 0$$):

$$-t\|y\| + ts \geq 0 \Rightarrow s \geq \|y\|$$

Do đó:

$$K^* = \{(y, s) : \|y\| \leq s\} = K$$

Như vậy, **nón bậc hai là nón tự đối ngẫu**.

---

**b) Kiểm chứng:**

$$K^{**} = (K^*)^* = K^* = K$$ ✓

---

**c) Đối ngẫu của bài toán SOCP:**

**Bài toán nguyên thủy:**

$$
\begin{align}
\min \quad & c^Tx \\
\text{s.t.} \quad & \|A_ix + b_i\| \leq c_i^Tx + d_i
\end{align}
$$

**Bài toán đối ngẫu:**

$$
\begin{align}
\max \quad & -\sum_i (b_i^Ty_i + d_iz_i) \\
\text{s.t.} \quad & \sum_i (A_i^Ty_i + c_iz_i) = c \\
& \|y_i\| \leq z_i
\end{align}
$$

Tính tự đối ngẫu của nón bậc hai tạo nên mối quan hệ đối xứng giữa bài toán nguyên thủy và bài toán đối ngẫu của SOCP.

</details>

---

## 📝 **Bài tập 4: Đối ngẫu Minimax**

Cho bài toán điểm yên:

$$\min_{x \in X} \max_{y \in Y} f(x, y)$$

với $$f(x, y) = x^TAy + b^Tx + c^Ty$$.

**Yêu cầu:**  
a) Viết bài toán đối ngẫu.  
b) Nêu điều kiện để giá trị minimax bằng maximin.  
c) Giải ví dụ trò chơi ma trận với $$A = \begin{bmatrix} 2 & -1 \\ -1 & 1 \end{bmatrix}$$, $$X = Y = \Delta_2$$ (đơn hình xác suất).

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Bài toán đối ngẫu:**

$$\max_{y \in Y} \min_{x \in X} f(x, y)$$

**Tính đối ngẫu yếu:**

$$\min_x \max_y f(x, y) \geq \max_y \min_x f(x, y)$$

---

**b) Định lý Minimax (von Neumann):**

Nếu $$X, Y$$ là các tập lồi compact và $$f$$ lồi theo $$x$$, lõm theo $$y$$ (convex-concave), thì:

$$\min_x \max_y f = \max_y \min_x f$$

và tồn tại điểm yên $$(x^*, y^*)$$.

---

**c) Trò chơi ma trận:**

$$\min_{x \in \Delta_2} \max_{y \in \Delta_2} x^T A y$$

$$A = \begin{bmatrix} 2 & -1 \\ -1 & 1 \end{bmatrix}$$

**Bài toán cực đại bên trong:**

$$\max_y x^TAy = \max\{2x_1 - x_2, -x_1 + x_2\}$$

(chọn chiến lược thuần mang lại giá trị lớn hơn).

**Bài toán cực tiểu bên ngoài:**

$$\min_x \max\{2x_1 - x_2, -x_1 + x_2\}$$

Với $$x_1 + x_2 = 1$$, thay $$x_2 = 1 - x_1$$:

$$\max\{2x_1 - (1-x_1), -x_1 + (1-x_1)\} = \max\{3x_1 - 1, 1 - 2x_1\}$$

Giao điểm hai đường thẳng: $$3x_1 - 1 = 1 - 2x_1 \Rightarrow 5x_1 = 2 \Rightarrow x_1 = 0.4$$.

**Cân bằng Nash:** $$x^* = (0.4, 0.6)$$, giá trị trò chơi bằng $$0.2$$.

</details>

---

## 📝 **Bài tập 5: Nới lỏng Lagrange (Lagrangian Relaxation)**

Cho bài toán quy hoạch nguyên:

$$
\begin{align}
\min \quad & c^Tx \\
\text{s.t.} \quad & Ax \leq b \\
& x \in \{0, 1\}^n
\end{align}
$$

**Yêu cầu:**  
a) Viết bài toán nới lỏng Lagrange.  
b) Giải thích tính chất cận dưới của bài toán đối ngẫu.  
c) Giải ví dụ với $$c = (-1, -2)$$, $$A = [1, 1]$$, $$b = 1$$.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Nới lỏng Lagrange:**

$$L(x, \lambda) = c^Tx + \lambda^T(Ax - b)$$

$$g(\lambda) = \min_{x \in \{0,1\}^n} L(x, \lambda) = \min_{x \in \{0,1\}^n} (c + A^T\lambda)^Tx - \lambda^Tb$$

Cực tiểu hóa độc lập từng thành phần $$x_i$$:

$$x_i^* = \begin{cases}
0 & \text{if } c_i + (A^T\lambda)_i > 0 \\
1 & \text{if } c_i + (A^T\lambda)_i < 0
\end{cases}$$

---

**b) Tính chất cận dưới:**

$$\max_{\lambda \geq 0} g(\lambda) \leq p^*$$

Giải bài toán đối ngẫu (dễ giải hơn) cung cấp cận dưới cho bài toán nguyên thủy (thuộc lớp NP-hard).

---

**c) Ví dụ:**

$$\min -x_1 - 2x_2$$ thỏa mãn $$x_1 + x_2 \leq 1$$, $$x \in \{0,1\}^2$$.

**Nghiệm tối ưu nguyên thủy:** $$x^* = (0, 1)$$, $$p^* = -2$$.

**Hàm Lagrange** (với $$\lambda \geq 0$$):

$$L(x, \lambda) = -x_1 - 2x_2 + \lambda(x_1 + x_2 - 1) = (\lambda - 1)x_1 + (\lambda - 2)x_2 - \lambda$$

**Hàm đối ngẫu:**

$$g(\lambda) = \min(0, \lambda - 1) + \min(0, \lambda - 2) - \lambda = \begin{cases} \lambda - 3 & 0 \leq \lambda \leq 1 \\ -2 & 1 \leq \lambda \leq 2 \\ -\lambda & \lambda \geq 2 \end{cases}$$

**Nghiệm tối ưu đối ngẫu:** $$\lambda^* \in [1, 2]$$, $$d^* = -2 = p^*$$.

Trường hợp này đạt **tính đối ngẫu mạnh** (đây là trường hợp đặc biệt thuận lợi; tổng quát, nới lỏng Lagrange chỉ đảm bảo cận dưới $$d^* \leq p^*$$).

</details>

---

## 💡 **Tổng kết**

### **Các khái niệm cốt lõi về đối ngẫu:**

| Khái niệm | Ý tưởng chính |
|---------|----------|
| **Phân tích nhiễu loạn (Perturbation)** | $$\lambda^* = -dp^*/du$$ cho ràng buộc $$f_i(x) \leq u_i$$ (độ nhạy) |
| **Điều kiện Slater** | Đảm bảo tính đối ngẫu mạnh cho bài toán lồi |
| **Nón đối ngẫu (Dual cone)** | $$K^* = \{y : y^Tx \geq 0 \, \forall x \in K\}$$ |
| **Định lý Minimax** | $$\min \max = \max \min$$ dưới điều kiện lồi – lõm và compact |
| **Nới lỏng Lagrange** | Nới lỏng ràng buộc khó để thu được cận dưới đối ngẫu |

### **Khi nào tính đối ngẫu mạnh được thỏa mãn:**
- **LP:** Luôn đúng khi bài toán khả thi.
- **Bài toán lồi:** Khi thỏa mãn điều kiện Slater.
- **SOCP/SDP:** Khi tồn tại điểm trong khả thi ngặt.
- **Bài toán không lồi:** Nhìn chung không đảm bảo (thường có khe đối ngẫu khác 0).

---

## 📚 **Tài liệu tham khảo**

1. Boyd, S., & Vandenberghe, L. (2004). *Convex Optimization*. Chapter 5.
2. Rockafellar, R. T. (1970). *Convex Analysis*. Princeton.
3. Borwein, J., & Lewis, A. (2006). *Convex Analysis and Nonlinear Optimization*.
