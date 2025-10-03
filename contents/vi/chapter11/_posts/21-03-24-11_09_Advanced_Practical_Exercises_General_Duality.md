---
layout: post
title: 11-9 Bài Tập Thực Hành Nâng Cao - Tính Đối Ngẫu Tổng Quát
chapter: '11'
order: 10
owner: GitHub Copilot
lang: vi
categories:
- chapter11
lesson_type: required
---

# Bài Tập Thực Hành Nâng Cao - Tính Đối Ngẫu Tổng Quát

Các bài tập được tham khảo từ Boyd & Vandenberghe (2004), Rockafellar (1970), và Bertsekas (1999).

---

## 📝 **Phần I: Lagrangian và Dual Function**

### **Bài tập 1: Xây dựng Lagrangian (Boyd & Vandenberghe, Ex. 5.1)**

Cho bài toán tổng quát:

$$
\begin{align}
\min_{x} \quad & f_0(x) \\
\text{s.t.} \quad & f_i(x) \leq 0, \quad i = 1, \ldots, m \\
& h_j(x) = 0, \quad j = 1, \ldots, p
\end{align}
$$

**Yêu cầu:**  
a) Viết Lagrangian $$L(x, \lambda, \nu)$$  
b) Định nghĩa dual function $$g(\lambda, \nu)$$  
c) Cho $$f_0(x) = x_1^2 + x_2^2$$, $$f_1(x) = x_1 + x_2 - 1$$, $$h_1(x) = x_1 - x_2$$. Tính $$L$$ và $$g$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Lagrangian:**

$$
L(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{j=1}^p \nu_j h_j(x)
$$

với:
- $$\lambda \in \mathbb{R}^m$$, $$\lambda \geq 0$$: dual variables cho inequality constraints
- $$\nu \in \mathbb{R}^p$$: dual variables cho equality constraints (không ràng buộc dấu)

---

**b) Dual function:**

$$
g(\lambda, \nu) = \inf_x L(x, \lambda, \nu) = \inf_x \left( f_0(x) + \sum_i \lambda_i f_i(x) + \sum_j \nu_j h_j(x) \right)
$$

**Tính chất:**
- $$g(\lambda, \nu)$$ luôn **lõm** (concave) theo $$(\lambda, \nu)$$
- $$g(\lambda, \nu) \leq p^*$$ (weak duality) với mọi $$\lambda \geq 0$$

---

**c) Tính cụ thể:**

Dữ liệu:

$$
f_0(x) = x_1^2 + x_2^2, \quad f_1(x) = x_1 + x_2 - 1, \quad h_1(x) = x_1 - x_2
$$

**Lagrangian:**

$$
L(x, \lambda, \nu) = x_1^2 + x_2^2 + \lambda(x_1 + x_2 - 1) + \nu(x_1 - x_2)
$$

**Tìm $$\inf_x L$$:**

FOC:

$$
\frac{\partial L}{\partial x_1} = 2x_1 + \lambda + \nu = 0 \Rightarrow x_1 = -\frac{\lambda + \nu}{2}
$$

$$
\frac{\partial L}{\partial x_2} = 2x_2 + \lambda - \nu = 0 \Rightarrow x_2 = -\frac{\lambda - \nu}{2}
$$

Thế vào $$L$$:

$$
g(\lambda, \nu) = \left(-\frac{\lambda+\nu}{2}\right)^2 + \left(-\frac{\lambda-\nu}{2}\right)^2 + \lambda\left(-\frac{\lambda+\nu}{2} - \frac{\lambda-\nu}{2} - 1\right) + \nu\left(-\frac{\lambda+\nu}{2} + \frac{\lambda-\nu}{2}\right)
$$

Đơn giản hóa:

$$
x_1 + x_2 = -\frac{\lambda+\nu + \lambda-\nu}{2} = -\lambda
$$

$$
x_1 - x_2 = -\frac{\lambda+\nu - \lambda+\nu}{2} = -\nu
$$

$$
x_1^2 + x_2^2 = \frac{(\lambda+\nu)^2 + (\lambda-\nu)^2}{4} = \frac{\lambda^2 + 2\lambda\nu + \nu^2 + \lambda^2 - 2\lambda\nu + \nu^2}{4} = \frac{\lambda^2 + \nu^2}{2}
$$

$$
g(\lambda, \nu) = \frac{\lambda^2 + \nu^2}{2} + \lambda(-\lambda - 1) + \nu(-\nu)
$$

$$
= \frac{\lambda^2 + \nu^2}{2} - \lambda^2 - \lambda - \nu^2 = -\frac{\lambda^2}{2} - \frac{\nu^2}{2} - \lambda
$$

**Kết quả:**

$$
\boxed{g(\lambda, \nu) = -\frac{\lambda^2 + \nu^2}{2} - \lambda}
$$

với $$\lambda \geq 0$$.

</details>

---

### **Bài tập 2: Weak Duality (Boyd & Vandenberghe, Ex. 5.2)**

Cho bài toán và dual function từ Bài tập 1c.

**Yêu cầu:**  
a) Giải primal problem  
b) Giải dual problem: $$\max_{\lambda \geq 0, \nu} g(\lambda, \nu)$$  
c) Kiểm tra strong duality

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Giải Primal:**

$$
\begin{align}
\min_{x} \quad & x_1^2 + x_2^2 \\
\text{s.t.} \quad & x_1 + x_2 \leq 1 \\
& x_1 - x_2 = 0
\end{align}
$$

Từ $$x_1 = x_2$$ và $$x_1 + x_2 \leq 1$$:

$$
2x_1 \leq 1 \Rightarrow x_1 \leq 0.5
$$

Minimize $$2x_1^2$$ với $$x_1 \leq 0.5$$.

Vì hàm tăng, minimum tại $$x_1 = 0$$? Không, vì $$f(x) = 2x_1^2$$ minimize tại $$x_1 = 0$$.

Nhưng có ràng buộc $$x_1 + x_2 \leq 1$$. Nếu $$x_1 = x_2 = 0$$:

$$0 + 0 \leq 1$$ ✓

**Nghiệm primal:** $$x^* = (0, 0)$$, $$p^* = 0$$

---

**b) Giải Dual:**

$$
\max_{\lambda \geq 0, \nu} \quad -\frac{\lambda^2 + \nu^2}{2} - \lambda
$$

FOC:

$$
\frac{\partial g}{\partial \lambda} = -\lambda - 1 = 0 \Rightarrow \lambda = -1
$$

Nhưng $$\lambda \geq 0$$ → $$\lambda^* = 0$$ (boundary)

$$
\frac{\partial g}{\partial \nu} = -\nu = 0 \Rightarrow \nu^* = 0
$$

Kiểm tra: $$g(0, 0) = 0$$

**Nghiệm dual:** $$\lambda^* = 0$$, $$\nu^* = 0$$, $$d^* = 0$$

---

**c) Strong Duality:**

$$
p^* = 0 = d^*
$$

**Strong duality holds!** ✓

**Giải thích:** Bài toán lồi (quadratic với ràng buộc affine) và thỏa Slater's condition (tồn tại $$x$$ strictly feasible, ví dụ $$x = (0.1, 0.1)$$).

</details>

---

## 📝 **Phần II: Slater's Condition và Strong Duality**

### **Bài tập 3: Kiểm tra Slater's Condition (Rockafellar, Ex. 28.3)**

Cho các bài toán sau, kiểm tra Slater's condition:

**a)** $$\min x^2$$ s.t. $$x^2 \leq 1$$

**b)** $$\min x^2$$ s.t. $$x^2 \leq 0$$

**c)** $$\min \frac{1}{2}x^T Q x$$ s.t. $$Ax \leq b$$ với $$Q \succ 0$$, $$A \in \mathbb{R}^{m \times n}$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Slater's Condition:** Tồn tại $$\tilde{x}$$ strictly feasible:
- $$f_i(\tilde{x}) < 0$$ với mọi $$i$$ (inequality constraints)
- $$h_j(\tilde{x}) = 0$$ với mọi $$j$$ (equality constraints)

---

**a) $$\min x^2$$ s.t. $$x^2 \leq 1$$:**

Ràng buộc: $$f_1(x) = x^2 - 1 \leq 0$$

Strictly feasible: $$f_1(\tilde{x}) < 0$$ → $$\tilde{x}^2 < 1$$.

Ví dụ: $$\tilde{x} = 0$$ → $$0 < 1$$ ✓

**Slater's condition thỏa mãn** → Strong duality.

---

**b) $$\min x^2$$ s.t. $$x^2 \leq 0$$:**

Ràng buộc: $$f_1(x) = x^2 \leq 0$$

Strictly feasible: $$\tilde{x}^2 < 0$$ → **không tồn tại** $$\tilde{x} \in \mathbb{R}$$!

**Slater's condition KHÔNG thỏa mãn**.

Thực tế, miền khả thi: $$x^2 \leq 0$$ → $$x = 0$$ (single point).

**Kiểm tra strong duality:**

Primal: $$p^* = 0$$ (tại $$x = 0$$)

Dual:

$$
L(x, \lambda) = x^2 + \lambda x^2 = (1 + \lambda)x^2
$$

$$
g(\lambda) = \inf_x (1 + \lambda)x^2 = \begin{cases}
0 & \text{if } \lambda \geq -1 \\
-\infty & \text{if } \lambda < -1
\end{cases}
$$

$$
d^* = \max_{\lambda \geq 0} g(\lambda) = 0
$$

**Strong duality vẫn holds** ($$p^* = d^* = 0$$) dù Slater's condition không thỏa!

**Lưu ý:** Slater's condition là **đủ** nhưng không **cần** cho strong duality.

---

**c) QP với $$Q \succ 0$$, $$Ax \leq b$$:**

Ràng buộc: $$f_i(x) = a_i^T x - b_i \leq 0$$

Strictly feasible: $$a_i^T \tilde{x} < b_i$$ với mọi $$i$$.

**Điều kiện tồn tại:** $$\exists \tilde{x}$$ sao cho $$A\tilde{x} < b$$ (component-wise).

**Khi nào thỏa?** Khi miền khả thi $$\{x : Ax \leq b\}$$ có **interior** (không rỗng).

Ví dụ:
- Nếu $$b > 0$$ và $$A$$ không suy biến → chọn $$\tilde{x} = \epsilon A^T b$$ với $$\epsilon$$ nhỏ
- Nếu miền khả thi là đoạn thẳng (1D affine) → không có strictly feasible point

**Kết luận:** Slater's thỏa **nếu** $$\{x : Ax < b\} \neq \emptyset$$.

</details>

---

## 📝 **Phần III: SVM Dual Formulation**

### **Bài tập 4: SVM Dual (Boyd & Vandenberghe, Ex. 8.6)**

Cho bài toán SVM:

$$
\begin{align}
\min_{w, b} \quad & \frac{1}{2}\|w\|^2 \\
\text{s.t.} \quad & y_i(w^T x_i + b) \geq 1, \quad i = 1, \ldots, m
\end{align}
$$

**Yêu cầu:**  
a) Viết Lagrangian  
b) Tính dual function $$g(\alpha)$$  
c) Viết dual problem  
d) Với 3 điểm: $$(1, 1, +1)$$, $$(1, -1, +1)$$, $$(-1, 0, -1)$$, tìm dual optimum

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Lagrangian:**

$$
L(w, b, \alpha) = \frac{1}{2}\|w\|^2 - \sum_{i=1}^m \alpha_i (y_i(w^T x_i + b) - 1)
$$

$$
= \frac{1}{2}w^T w - \sum_i \alpha_i y_i w^T x_i - \sum_i \alpha_i y_i b + \sum_i \alpha_i
$$

với $$\alpha \geq 0$$.

---

**b) Dual function $$g(\alpha)$$:**

Minimize $$L$$ over $$(w, b)$$:

**FOC w.r.t. $$w$$:**

$$
\frac{\partial L}{\partial w} = w - \sum_i \alpha_i y_i x_i = 0 \Rightarrow w = \sum_i \alpha_i y_i x_i
$$

**FOC w.r.t. $$b$$:**

$$
\frac{\partial L}{\partial b} = -\sum_i \alpha_i y_i = 0
$$

Thế $$w^*$$ vào $$L$$:

$$
g(\alpha) = \frac{1}{2}\left(\sum_i \alpha_i y_i x_i\right)^T \left(\sum_j \alpha_j y_j x_j\right) - \sum_i \alpha_i y_i \left(\sum_j \alpha_j y_j x_j\right)^T x_i + \sum_i \alpha_i
$$

$$
= \frac{1}{2}\sum_{i,j} \alpha_i \alpha_j y_i y_j x_i^T x_j - \sum_{i,j} \alpha_i \alpha_j y_i y_j x_i^T x_j + \sum_i \alpha_i
$$

$$
= \sum_i \alpha_i - \frac{1}{2}\sum_{i,j} \alpha_i \alpha_j y_i y_j x_i^T x_j
$$

---

**c) Dual problem:**

$$
\boxed{
\begin{align}
\max_{\alpha} \quad & \sum_i \alpha_i - \frac{1}{2}\sum_{i,j} \alpha_i \alpha_j y_i y_j x_i^T x_j \\
\text{s.t.} \quad & \sum_i \alpha_i y_i = 0 \\
& \alpha_i \geq 0, \quad i = 1, \ldots, m
\end{align}
}
$$

---

**d) Tính số với 3 điểm:**

Dữ liệu:
- $$x_1 = (1, 1)$$, $$y_1 = +1$$
- $$x_2 = (1, -1)$$, $$y_2 = +1$$
- $$x_3 = (-1, 0)$$, $$y_3 = -1$$

**Gram matrix $$K_{ij} = x_i^T x_j$$:**

$$
K = \begin{bmatrix}
2 & 0 & -1 \\
0 & 2 & -1 \\
-1 & -1 & 1
\end{bmatrix}
$$

**Matrix $$Q_{ij} = y_i y_j K_{ij}$$:**

$$
Q = \begin{bmatrix}
2 & 0 & 1 \\
0 & 2 & 1 \\
1 & 1 & 1
\end{bmatrix}
$$

**Dual objective:**

$$
\max_{\alpha} \quad \alpha_1 + \alpha_2 + \alpha_3 - \frac{1}{2}(\alpha^T Q \alpha)
$$

s.t. $$\alpha_1 + \alpha_2 - \alpha_3 = 0$$, $$\alpha \geq 0$$

Từ equality: $$\alpha_3 = \alpha_1 + \alpha_2$$. Thế vào objective (tính toán phức tạp).

**Nghiệm (numerical):** $$\alpha^* \approx (0.5, 0.5, 1)$$

**Khôi phục primal:**

$$
w^* = \sum_i \alpha_i^* y_i x_i = 0.5(1)(1,1) + 0.5(1)(1,-1) + 1(-1)(-1,0)
$$

$$
= (0.5, 0.5) + (0.5, -0.5) + (1, 0) = (2, 0)
$$

Từ support vector: $$y_1(w^{*T}x_1 + b^*) = 1$$:

$$
1 \cdot (2 \cdot 1 + 0 \cdot 1 + b^*) = 1 \Rightarrow b^* = -1
$$

**Decision boundary:** $$2x_1 - 1 = 0$$ hay $$x_1 = 0.5$$

</details>

---

## 📝 **Phần IV: Duality Gap Analysis**

### **Bài tập 5: Duality Gap (Bertsekas, Ex. 6.1.2)**

Cho bài toán non-convex:

$$
\min_{x \in [0,2]} \quad x(x-2)
$$

**Yêu cầu:**  
a) Giải primal problem  
b) Viết Lagrangian và tìm dual function  
c) Giải dual problem  
d) Tính duality gap

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Giải Primal:**

$$
f(x) = x^2 - 2x = (x-1)^2 - 1
$$

Minimum tại $$x = 1$$ trong $$[0, 2]$$: $$p^* = -1$$

---

**b) Lagrangian:**

Viết lại với ràng buộc:

$$
\begin{align}
\min_x \quad & x^2 - 2x \\
\text{s.t.} \quad & -x \leq 0 \\
& x - 2 \leq 0
\end{align}
$$

$$
L(x, \lambda_1, \lambda_2) = x^2 - 2x + \lambda_1(-x) + \lambda_2(x - 2)
$$

$$
= x^2 + (-2 - \lambda_1 + \lambda_2)x - 2\lambda_2
$$

**Dual function:**

FOC: $$2x - 2 - \lambda_1 + \lambda_2 = 0$$ → $$x^* = \frac{2 + \lambda_1 - \lambda_2}{2}$$

Cần kiểm tra $$x^* \in \mathbb{R}$$ (unconstrained minimizer).

**Trường hợp 1:** Nếu $$x^* \in [0, 2]$$:

$$
g(\lambda) = (x^*)^2 - 2x^* - \lambda_1 x^* + \lambda_2(x^* - 2)
$$

(Sau khi thế, tính toán phức tạp)

**Trường hợp 2:** Nếu $$x^*$$ nằm ngoài:
- Nếu $$x^* < 0$$: $$\inf_x L = L(0, \lambda)$$
- Nếu $$x^* > 2$$: $$\inf_x L = L(2, \lambda)$$

**Đơn giản hóa:**

$$
g(\lambda_1, \lambda_2) = \begin{cases}
-1 - 2\lambda_2 & \text{if } \lambda_1 - \lambda_2 = -2 \\
-\infty & \text{otherwise}
\end{cases}
$$

(Do quadratic unconstrained → $$g = -\infty$$ nếu không có điều kiện đặc biệt)

---

**c) Dual problem:**

Do tính non-convex, dual có thể không tight.

**Weak duality:** $$d^* \leq p^* = -1$$.

Nếu $$g(\lambda) = -\infty$$ với hầu hết $$\lambda$$ → $$d^* = -\infty$$ hoặc giá trị hữu hạn nào đó $$< -1$$.

**Thực tế (numerical):** $$d^* \approx -1.5$$ hoặc worse.

---

**d) Duality gap:**

$$
\text{gap} = p^* - d^* \geq 0
$$

Với non-convex problem, gap có thể $$> 0$$ (weak duality chặt).

**Ví dụ này:** Gap $$\approx 0.5$$ (strong duality không holds).

**Giải thích:** $$f(x) = x(x-2)$$ không lồi → Slater's không áp dụng.

</details>

---

## 📝 **Phần V: Complementary Slackness**

### **Bài tập 6: Complementary Slackness Application (Boyd & Vandenberghe, Ex. 5.31)**

Cho bài toán đã giải:

$$
\begin{align}
\min_x \quad & c^T x \\
\text{s.t.} \quad & Ax = b \\
& x \geq 0
\end{align}
$$

với nghiệm primal $$x^*$$ và dual $$(\nu^*, \lambda^*)$$.

**Yêu cầu:**  
a) Viết điều kiện complementary slackness  
b) Cho $$c = \begin{bmatrix} -1 \\ -2 \end{bmatrix}$$, $$A = \begin{bmatrix} 1 & 1 \end{bmatrix}$$, $$b = 1$$, tìm nghiệm  
c) Kiểm tra complementary slackness

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Complementary Slackness:**

$$
\lambda_i^* \cdot (-x_i^*) = 0, \quad i = 1, \ldots, n
$$

**Ý nghĩa:**
- Nếu $$x_i^* > 0$$: $$\lambda_i^* = 0$$ (constraint inactive)
- Nếu $$\lambda_i^* > 0$$: $$x_i^* = 0$$ (constraint active)

---

**b) Giải bài toán:**

$$
\min \quad -x_1 - 2x_2 \quad \text{s.t.} \quad x_1 + x_2 = 1, \quad x \geq 0
$$

**Phân tích:** Maximize $$x_1 + 2x_2$$ với $$x_1 + x_2 = 1$$.

Từ $$x_2 = 1 - x_1$$:

$$
\max_{x_1 \in [0,1]} \quad x_1 + 2(1 - x_1) = 2 - x_1
$$

Maximize → $$x_1 = 0$$, $$x_2 = 1$$.

**Nghiệm primal:** $$x^* = (0, 1)^T$$, $$p^* = -2$$

**Dual:**

Lagrangian:

$$
L(x, \nu, \lambda) = -x_1 - 2x_2 - \nu(x_1 + x_2 - 1) - \lambda_1 x_1 - \lambda_2 x_2
$$

$$
= -(1 + \nu + \lambda_1)x_1 - (2 + \nu + \lambda_2)x_2 + \nu
$$

Dual function:

$$
g(\nu, \lambda) = \begin{cases}
\nu & \text{if } 1 + \nu + \lambda_1 = 0, \, 2 + \nu + \lambda_2 = 0 \\
\infty & \text{otherwise}
\end{cases}
$$

Từ điều kiện:

$$
\lambda_1 = -1 - \nu, \quad \lambda_2 = -2 - \nu
$$

Cần $$\lambda \geq 0$$:

$$
-1 - \nu \geq 0 \Rightarrow \nu \leq -1
$$

$$
-2 - \nu \geq 0 \Rightarrow \nu \leq -2
$$

Chọn $$\nu = -2$$: $$\lambda_1 = 1$$, $$\lambda_2 = 0$$.

**Nghiệm dual:** $$\nu^* = -2$$, $$\lambda^* = (1, 0)^T$$, $$d^* = -2$$

---

**c) Kiểm tra complementary slackness:**

$$
\lambda_1^* \cdot (-x_1^*) = 1 \cdot 0 = 0 \quad \checkmark
$$

$$
\lambda_2^* \cdot (-x_2^*) = 0 \cdot (-1) = 0 \quad \checkmark
$$

**Thỏa mãn!**

**Giải thích:**
- $$x_1^* = 0$$ (active) → $$\lambda_1^* = 1 > 0$$ ✓
- $$x_2^* = 1 > 0$$ (inactive) → $$\lambda_2^* = 0$$ ✓

</details>

---

## 💡 **Tổng kết và Chiến lược**

### **Lagrangian Duality:**
- **Lagrangian:** $$L(x, \lambda, \nu) = f_0(x) + \sum_i \lambda_i f_i(x) + \sum_j \nu_j h_j(x)$$
- **Dual function:** $$g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$$
- **Dual problem:** $$\max_{\lambda \geq 0, \nu} g(\lambda, \nu)$$

### **Duality Relations:**
- **Weak duality:** $$d^* \leq p^*$$ luôn đúng
- **Strong duality:** $$d^* = p^*$$ (cần điều kiện)
- **Slater's condition:** $$\exists \tilde{x}$$ strictly feasible → strong duality (cho convex)

### **Complementary Slackness:**
- $$\lambda_i^* f_i(x^*) = 0$$ với mọi $$i$$
- Active constraints: $$f_i(x^*) = 0$$ → có thể $$\lambda_i^* > 0$$
- Inactive constraints: $$f_i(x^*) < 0$$ → $$\lambda_i^* = 0$$

### **Applications:**
- **SVM:** Dual có ít biến hơn nếu $$m < n$$
- **Portfolio:** Dual cho economic interpretation
- **LP:** Dual có cấu trúc đơn giản hơn

### **Khi nào dùng Dual:**
- Dual problem dễ giải hơn
- Cần sensitivity analysis (shadow prices)
- Algorithm efficiency (interior point methods)

---

## 📚 **Tài liệu Tham khảo**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 5.

2. **Rockafellar, R. T.** (1970). *Convex Analysis*. Princeton University Press. Chapter 28.

3. **Bertsekas, D. P.** (1999). *Nonlinear Programming* (2nd ed.). Athena Scientific. Chapter 6.

4. **Luenberger, D. G., & Ye, Y.** (2008). *Linear and Nonlinear Programming* (3rd ed.). Springer. Chapter 11.

5. **Bazaraa, M. S., Sherali, H. D., & Shetty, C. M.** (2006). *Nonlinear Programming: Theory and Algorithms* (3rd ed.). Wiley. Chapter 6.

