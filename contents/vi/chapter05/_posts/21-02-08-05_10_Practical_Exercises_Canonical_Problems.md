---
layout: post
title: 05-10 Bài Tập Thực Hành - Các Bài Toán Chuẩn
chapter: '05'
order: 16
owner: GitHub Copilot
lang: vi
categories:
- chapter05
lesson_type: required
redirect_from:
  - /contents/vi/chapter05/05_08_Practical_Exercises_Canonical_Problems/
---

# Bài Tập Thực Hành - Các Bài Toán Chuẩn (Canonical Problems)

Các bài tập được tham khảo từ Boyd & Vandenberghe (2004), Ben-Tal & Nemirovski (2001).

---

## 📝 **Phần I: Linear Programming (LP)**

### **Bài tập 1: Bài toán Dinh dưỡng (Diet Problem)**

Một người cần lập kế hoạch dinh dưỡng với 3 loại thực phẩm:
- Thực phẩm 1: 2 đơn vị protein, 1 đơn vị carbs, giá 3 USD
- Thực phẩm 2: 1 đơn vị protein, 2 đơn vị carbs, giá 2 USD  
- Thực phẩm 3: 1 đơn vị protein, 1 đơn vị carbs, giá 1.5 USD

Yêu cầu tối thiểu: 5 đơn vị protein, 6 đơn vị carbs mỗi ngày.

**Yêu cầu:**  
a) Viết bài toán LP để minimize chi phí  
b) Tìm nghiệm tối ưu  
c) Giải thích ý nghĩa dual variables (shadow prices)

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Formulation:**

Biến: $$x_i$$ = lượng thực phẩm $$i$$ ($$i = 1,2,3$$)

$$
\begin{align}
\min_{x} \quad & 3x_1 + 2x_2 + 1.5x_3 \\
\text{s.t.} \quad & 2x_1 + x_2 + x_3 \geq 5 \quad \text{(protein)} \\
& x_1 + 2x_2 + x_3 \geq 6 \quad \text{(carbs)} \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**Dạng chuẩn (min với $$\leq$$):**

$$
\begin{align}
\min_{x} \quad & 3x_1 + 2x_2 + 1.5x_3 \\
\text{s.t.} \quad & -2x_1 - x_2 - x_3 \leq -5 \\
& -x_1 - 2x_2 - x_3 \leq -6 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

---

**b) Tìm nghiệm tối ưu:**

Thực phẩm 3 rẻ nhất trên mỗi đơn vị dinh dưỡng, nên nghiệm tối ưu dùng nhiều thực phẩm 3. Xét đỉnh $$x = (0, 1, 4)$$ (cả hai ràng buộc chặt, $$x_1 = 0$$):

$$\text{Protein: } 0 + 1 + 4 = 5 \text{ ✓}, \qquad \text{Carbs: } 0 + 2 + 4 = 6 \text{ ✓}$$

Chi phí: $$3 \cdot 0 + 2 \cdot 1 + 1.5 \cdot 4 = 8$$ USD.

Tính tối ưu được xác nhận bằng dual ở phần c): có $$\lambda$$ khả thi với giá trị dual bằng 8.

**Nghiệm tối ưu:** $$x^* = (0, 1, 4)$$, chi phí = 8 USD

(Lưu ý: đỉnh $$x_3 = 0$$, $$x = (\frac{4}{3}, \frac{7}{3}, 0)$$ là khả thi nhưng chi phí $$\frac{26}{3} \approx 8.67 > 8$$ nên **không** tối ưu.)

---

---

**c) Dual variables (Shadow prices):**

Dual problem:

$$
\max_{\lambda} \quad 5\lambda_1 + 6\lambda_2 \quad \text{s.t.} \quad A^T\lambda \leq c, \, \lambda \geq 0
$$

tức là $$2\lambda_1 + \lambda_2 \leq 3$$, $$\lambda_1 + 2\lambda_2 \leq 2$$, $$\lambda_1 + \lambda_2 \leq 1.5$$.

Với $$\lambda^* = (1, \frac{1}{2})$$ (từ complementary slackness, vì $$x_2, x_3 > 0$$ nên ràng buộc dual 2 và 3 phải chặt): ràng buộc 1 là $$2 + 0.5 = 2.5 < 3$$ (lỏng, khớp với $$x_1^* = 0$$), và giá trị dual $$5(1) + 6(0.5) = 8$$ bằng giá trị primal → tối ưu (strong duality).

**Ý nghĩa:**
- $$\lambda_1^* = 1$$: Tăng yêu cầu protein 1 đơn vị → chi phí tăng 1 USD
- $$\lambda_2^* = \frac{1}{2}$$: Tăng yêu cầu carbs 1 đơn vị → chi phí tăng 0.5 USD

Protein "đắt" hơn carbs trong bối cảnh này!

</details>

---

## 📝 **Phần II: Quadratic Programming (QP)**

### **Bài tập 2: Portfolio Optimization**

Đầu tư vào 2 tài sản với:
- Lợi nhuận kỳ vọng: $$\mu = (0.12, 0.10)^T$$
- Ma trận hiệp phương sai: $$\Sigma = \begin{bmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{bmatrix}$$

**Yêu cầu:**  
a) Viết bài toán minimize risk với target return $$r = 0.11$$  
b) Tìm portfolio tối ưu  
c) Vẽ efficient frontier

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Formulation:**

$$
\begin{align}
\min_{x} \quad & \frac{1}{2} x^T \Sigma x \\
\text{s.t.} \quad & \mu^T x = r \\
& \mathbf{1}^T x = 1 \\
& x \geq 0
\end{align}
$$

Với $$r = 0.11$$:

$$
\begin{align}
\min_{x} \quad & \frac{1}{2}(0.04x_1^2 + 0.02x_1x_2 + 0.09x_2^2) \\
\text{s.t.} \quad & 0.12x_1 + 0.10x_2 = 0.11 \\
& x_1 + x_2 = 1 \\
& x_1, x_2 \geq 0
\end{align}
$$

---

**b) Giải bằng Lagrangian:**

Từ $$x_1 + x_2 = 1$$ và $$0.12x_1 + 0.10x_2 = 0.11$$:

$$0.12x_1 + 0.10(1-x_1) = 0.11 \Rightarrow 0.02x_1 = 0.01 \Rightarrow x_1 = 0.5$$

$$x_2 = 0.5$$

**Nghiệm:** $$x^* = (0.5, 0.5)^T$$

**Kiểm tra feasibility:** $$0.5 + 0.5 = 1$$ ✓, $$0.12(0.5) + 0.10(0.5) = 0.11$$ ✓

**Risk (variance):**

$$\sigma^2 = x^{*T} \Sigma x^* = \begin{bmatrix} 0.5 & 0.5 \end{bmatrix} \begin{bmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{bmatrix} \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix}$$

$$= \begin{bmatrix} 0.5 & 0.5 \end{bmatrix} \begin{bmatrix} 0.025 \\ 0.05 \end{bmatrix} = 0.0375$$

**Standard deviation:** $$\sigma = \sqrt{0.0375} \approx 0.194 = 19.4\%$$

---

**c) Efficient frontier:**

Thay đổi $$r$$ từ $$\min(\mu_i) = 0.10$$ đến $$\max(\mu_i) = 0.12$$:

| Return $$r$$ | $$x_1$$ | $$x_2$$ | Risk $$\sigma$$ |
|-------------|---------|---------|-----------------|
| 0.10 | 0 | 1 | 0.300 |
| 0.105 | 0.25 | 0.75 | 0.238 |
| 0.11 | 0.5 | 0.5 | 0.194 |
| 0.1145 | 0.727 | 0.273 | 0.178 (rủi ro nhỏ nhất) |
| 0.115 | 0.75 | 0.25 | 0.179 |
| 0.12 | 1 | 0 | 0.200 |

**Kết luận:** Đường cong (risk, return) có rủi ro nhỏ nhất tại $$x_1 = 0.08/0.11 \approx 0.727$$ ($$r \approx 0.1145$$). Chỉ nhánh $$r \geq 0.1145$$ mới là **efficient frontier** (với cùng rủi ro, lợi nhuận cao hơn); các điểm với $$r < 0.1145$$ bị chi phối (dominated).

</details>

---

## 📝 **Phần III: QCQP và SOCP**

### **Bài tập 3: Robust Least Squares (SOCP)**

Cho dữ liệu $$A \in \mathbb{R}^{m \times n}$$, $$b \in \mathbb{R}^m$$. Thay vì least squares thông thường, xét robust version:

$$
\min_{x} \quad \|Ax - b\|_2 + \gamma \|x\|_2
$$

với $$\gamma > 0$$ là regularization parameter.

**Yêu cầu:**  
a) Viết dưới dạng SOCP  
b) Với $$A = \begin{bmatrix} 1 & 1 \\ 1 & -1 \\ 2 & 0 \end{bmatrix}$$, $$b = \begin{bmatrix} 2 \\ 0 \\ 3 \end{bmatrix}$$, $$\gamma = 0.1$$, tìm nghiệm

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) SOCP formulation:**

Đặt:
- $$t_1$$ sao cho $$\|Ax - b\|_2 \leq t_1$$
- $$t_2$$ sao cho $$\|x\|_2 \leq t_2$$

Bài toán trở thành:

$$
\begin{align}
\min_{x, t_1, t_2} \quad & t_1 + \gamma t_2 \\
\text{s.t.} \quad & \|Ax - b\|_2 \leq t_1 \\
& \|x\|_2 \leq t_2
\end{align}
$$

Đây là **SOCP** với 2 second-order cone constraints.

**Dạng chuẩn SOCP:**

$$
\begin{align}
\min \quad & c^T y \\
\text{s.t.} \quad & \|A_i y + b_i\|_2 \leq c_i^T y + d_i, \quad i = 1, \ldots, k
\end{align}
$$

---

**b) Giải số:**

Dữ liệu:

$$A = \begin{bmatrix} 1 & 1 \\ 1 & -1 \\ 2 & 0 \end{bmatrix}, \quad b = \begin{bmatrix} 2 \\ 0 \\ 3 \end{bmatrix}, \quad \gamma = 0.1$$

**Phương pháp giải tích (xấp xỉ):**

Gradient của $$f(x) = \|Ax-b\|_2 + \gamma\|x\|_2$$:

$$\nabla f(x) = \frac{A^T(Ax-b)}{\|Ax-b\|_2} + \gamma \frac{x}{\|x\|_2}$$

(Phức tạp do non-smooth tại $$x = 0$$ và $$Ax = b$$)

**Cách 1: xấp xỉ bằng regularized LS có closed-form:**

Xấp xỉ bằng $$\min \|Ax-b\|_2^2 + \gamma^2\|x\|_2^2$$:

$$x_{\text{ridge}} = (A^TA + \gamma^2 I)^{-1} A^T b$$

Tính:

$$A^TA = \begin{bmatrix} 1 & 1 & 2 \\ 1 & -1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & -1 \\ 2 & 0 \end{bmatrix} = \begin{bmatrix} 6 & 0 \\ 0 & 2 \end{bmatrix}$$

$$A^TA + 0.01I = \begin{bmatrix} 6.01 & 0 \\ 0 & 2.01 \end{bmatrix}$$

$$A^Tb = \begin{bmatrix} 1 & 1 & 2 \\ 1 & -1 & 0 \end{bmatrix} \begin{bmatrix} 2 \\ 0 \\ 3 \end{bmatrix} = \begin{bmatrix} 8 \\ 2 \end{bmatrix}$$

Giải: $$x_{\text{ridge}} = \left(\frac{8}{6.01}, \frac{2}{2.01}\right) \approx (1.331, 0.995)^T$$, với $$f(x_{\text{ridge}}) \approx 0.744$$.

**Cách 2: nghiệm số của SOCP gốc** (giải trực tiếp $$\min \|Ax-b\|_2 + 0.1\|x\|_2$$):

$$x^* \approx (1.326, 0.983)^T, \qquad f(x^*) \approx 0.743$$

(Hai nghiệm gần nhau nhưng không trùng, vì bài toán gốc dùng chuẩn $$\ell_2$$ chứ không phải bình phương.)

</details>

---

## 📝 **Phần IV: Semidefinite Programming (SDP)**

### **Bài tập 4: Matrix Completion**

Cho ma trận $$M \in \mathbb{R}^{3 \times 3}$$ với một số entries bị thiếu. Biết:

$$M_{11} = 4, \quad M_{12} = 2, \quad M_{22} = 5, \quad M_{23} = 1$$

Tìm ma trận positive semidefinite $$X$$ hoàn chỉnh với trace nhỏ nhất.

**Yêu cầu:**  
a) Viết bài toán SDP  
b) Tìm nghiệm

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) SDP formulation:**

$$
\begin{align}
\min_{X} \quad & \text{tr}(X) \\
\text{s.t.} \quad & X_{11} = 4 \\
& X_{12} = X_{21} = 2 \\
& X_{22} = 5 \\
& X_{23} = X_{32} = 1 \\
& X \succeq 0 \\
& X = X^T
\end{align}
$$

Ma trận:

$$X = \begin{bmatrix} 4 & 2 & x_{13} \\ 2 & 5 & 1 \\ x_{13} & 1 & x_{33} \end{bmatrix}$$

---

**b) Giải:**

**Điều kiện PSD:** Tất cả principal minors $$\geq 0$$.

**Minor 1×1:** $$4 > 0$$ ✓

**Minor 2×2:** 

$$\begin{vmatrix} 4 & 2 \\ 2 & 5 \end{vmatrix} = 20 - 4 = 16 > 0$$ ✓

**Minor 3×3 (determinant):**

$$\det(X) = 4(5x_{33} - 1) - 2(2x_{33} - x_{13}) + x_{13}(2 - 5x_{13})$$

$$= 20x_{33} - 4 - 4x_{33} + 2x_{13} + 2x_{13} - 5x_{13}^2$$

$$= 16x_{33} - 5x_{13}^2 + 4x_{13} - 4$$

Để $$\det(X) \geq 0$$: $$16x_{33} \geq 5x_{13}^2 - 4x_{13} + 4$$

**Minimize $$\text{tr}(X) = 4 + 5 + x_{33} = 9 + x_{33}$$:**

Cần minimize $$x_{33}$$ subject to PSD.

Từ PSD, cần:

$$x_{33} \geq \frac{5x_{13}^2 - 4x_{13} + 4}{16}$$

Minimize RHS over $$x_{13}$$:

$$\frac{d}{dx_{13}}\left(\frac{5x_{13}^2 - 4x_{13} + 4}{16}\right) = \frac{10x_{13} - 4}{16} = 0$$

$$x_{13}^* = 0.4$$

$$x_{33}^{\min} = \frac{5(0.4)^2 - 4(0.4) + 4}{16} = \frac{0.8 - 1.6 + 4}{16} = \frac{3.2}{16} = 0.2$$

**Nghiệm:**

$$X^* = \begin{bmatrix} 4 & 2 & 0.4 \\ 2 & 5 & 1 \\ 0.4 & 1 & 0.2 \end{bmatrix}, \quad \text{tr}(X^*) = 9.2$$

**Kiểm tra:** $$\det(X^*) = 16(0.2) - 5(0.16) + 1.6 - 4 = 0$$ (rank-deficient, nhưng $$\succeq 0$$ ✓)

</details>

---

## 📝 **Phần V: Tổng hợp**

### **Bài tập 5: Chọn Formulation phù hợp**

Với mỗi bài toán, xác định dạng chuẩn (LP, QP, QCQP, SOCP, SDP):

**a)** $$\min c^T x$$ s.t. $$Ax = b$$, $$\|x\|_\infty \leq 1$$

**b)** $$\min \|Ax - b\|_1$$

**c)** $$\min x^TQx$$ s.t. $$\|Ax - b\|_2 \leq \delta$$ (với $$Q \succeq 0$$)

**d)** $$\min \text{tr}(X)$$ s.t. $$X \succeq yy^T$$, $$X \succeq 0$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) $$\min c^Tx$$ s.t. $$Ax = b$$, $$\|x\|_\infty \leq 1$$:**

$$\|x\|_\infty \leq 1 \Leftrightarrow -1 \leq x_i \leq 1$$ (linear constraints)

→ **Linear Programming (LP)**

---

**b) $$\min \|Ax - b\|_1$$:**

$$\|Ax - b\|_1 = \sum_i |r_i|$$ với $$r = Ax - b$$

Đặt $$t_i \geq |r_i|$$:

$$
\begin{align}
\min \quad & \sum_i t_i \\
\text{s.t.} \quad & -t_i \leq (Ax - b)_i \leq t_i
\end{align}
$$

→ **Linear Programming (LP)**

---

**c) $$\min x^TQx$$ s.t. $$\|Ax - b\|_2 \leq \delta$$ (với $$Q \succeq 0$$):**

- Objective: quadratic
- Constraint: second-order cone ($$\ell_2$$ norm)

→ **Second-Order Cone Programming (SOCP)**

(Hoặc QCQP nếu viết $$\|Ax-b\|_2^2 \leq \delta^2$$)

---

**d) $$\min \text{tr}(X)$$ s.t. $$X \succeq yy^T$$, $$X \succeq 0$$:**

- Objective: linear trong $$X$$
- Constraint: $$X \succeq yy^T$$ → $$X - yy^T \succeq 0$$ (PSD constraint)

→ **Semidefinite Programming (SDP)**

</details>

---

## 💡 **Tổng kết**

### **Hierarchy of Convex Problems:**

$$
\text{LP} \subset \text{QP} \subset \text{SOCP} \subset \text{SDP}
$$

| Problem | Objective | Constraints | Example |
|---------|-----------|-------------|---------|
| **LP** | Linear | Linear | Diet problem, transportation |
| **QP** | Quadratic | Linear | Portfolio, least squares |
| **QCQP** | Quadratic | Quadratic | Robust optimization |
| **SOCP** | Linear | $$\ell_2$$ cones | Robust LS, antenna design |
| **SDP** | Linear | PSD cones | Matrix completion, relaxation |

### **Khi nào dùng gì:**
- **LP:** Khi mọi thứ đều tuyến tính
- **QP:** Risk minimization, LS với regularization
- **SOCP:** Robust optimization, $$\ell_2$$ constraints
- **SDP:** Matrix variables, combinatorial relaxation

---

## 📚 **Tài liệu Tham khảo**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 4.

2. **Ben-Tal, A., & Nemirovski, A.** (2001). *Lectures on Modern Convex Optimization*. SIAM.

3. **Lobo, M. S., et al.** (1998). "Applications of Second-Order Cone Programming". *Linear Algebra and Applications*.

