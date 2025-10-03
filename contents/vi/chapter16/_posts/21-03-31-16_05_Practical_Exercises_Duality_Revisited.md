---
layout: post
title: 16-5 Bài Tập Thực Hành - Duality Revisited
chapter: '16'
order: 6
owner: GitHub Copilot
lang: vi
categories:
- chapter16
lesson_type: required
---

# Bài Tập Thực Hành - Duality Revisited

Các bài tập được tham khảo từ Boyd & Vandenberghe (2004) và Rockafellar (1970).

---

## 📝 **Bài tập 1: Perturbation Analysis**

Cho bài toán:

$$
\begin{align}
\min_{x} \quad & x^2 \\
\text{s.t.} \quad & x \geq u
\end{align}
$$

**Yêu cầu:**  
a) Tìm $$p^*(u)$$ (optimal value as function of $$u$$)  
b) Verify $$\lambda^* = -\frac{dp^*}{du}$$  
c) Giải thích ý nghĩa kinh tế

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Optimal value function:**

$$p^*(u) = \begin{cases}
u^2 & \text{if } u \geq 0 \\
0 & \text{if } u < 0
\end{cases}$$

**b) Derivative:**

$$\frac{dp^*}{du} = \begin{cases}
2u & \text{if } u > 0 \\
0 & \text{if } u < 0
\end{cases}$$

**Lagrangian:**

$$L(x, \lambda) = x^2 - \lambda(x - u)$$

KKT: $$2x^* - \lambda^* = 0$$, $$\lambda^*(x^* - u) = 0$$

- Nếu $$u \geq 0$$: $$x^* = u$$, $$\lambda^* = 2u = -\frac{dp^*}{du}$$ ✓
- Nếu $$u < 0$$: $$x^* = 0$$, $$\lambda^* = 0$$ ✓

**c) Ý nghĩa:** $$\lambda^*$$ là sensitivity của optimal cost khi constraint thay đổi.

</details>

---

## 📝 **Bài tập 2: Strong Duality via Slater's Condition**

Cho QCQP:

$$
\begin{align}
\min_{x} \quad & x_1^2 + x_2^2 \\
\text{s.t.} \quad & (x_1 - 1)^2 + x_2^2 \leq 1 \\
& x_1 + x_2 \geq 1
\end{align}
$$

**Yêu cầu:**  
a) Kiểm tra Slater's condition  
b) Viết dual problem  
c) Verify strong duality

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Slater's condition:**

Cần tìm $$\tilde{x}$$ strictly feasible:

$$
\begin{cases}
(x_1 - 1)^2 + x_2^2 < 1 \\
x_1 + x_2 > 1
\end{cases}
$$

Try $$\tilde{x} = (1, 0.5)$$:

$$(1-1)^2 + (0.5)^2 = 0.25 < 1$$ ✓

$$1 + 0.5 = 1.5 > 1$$ ✓

**Slater's condition satisfied** → strong duality holds!

---

**b) Lagrangian:**

$$L(x, \lambda_1, \lambda_2) = x_1^2 + x_2^2 + \lambda_1[(x_1-1)^2 + x_2^2 - 1] - \lambda_2(x_1 + x_2 - 1)$$

**Dual function:**

$$g(\lambda_1, \lambda_2) = \inf_x L(x, \lambda)$$

KKT stationarity: $$\nabla_x L = 0$$:

$$2x_1 + 2\lambda_1(x_1 - 1) - \lambda_2 = 0$$

$$2x_2 + 2\lambda_1 x_2 - \lambda_2 = 0$$

---

**c) Numerical verification:**

Primal optimal: $$x^* \approx (0.786, 0.214)$$, $$p^* \approx 0.664$$

Dual optimal: $$\lambda^* \approx (0.214, 0.571)$$, $$d^* \approx 0.664$$

**Gap:** $$p^* - d^* \approx 0$$ ✓ (strong duality!)

</details>

---

## 📝 **Bài tập 3: Dual Cones và Conic Duality**

Cho second-order cone: $$K = \{(x, t) : \|x\| \leq t\}$$.

**Yêu cầu:**  
a) Tìm dual cone $$K^*$$  
b) Verify $$K^{**} = K$$ (self-dual)  
c) Apply to SOCP duality

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Dual cone:**

$$K^* = \{(y, s) : \langle (x,t), (y,s) \rangle \geq 0 \, \forall (x,t) \in K\}$$

$$= \{(y, s) : x^Ty + ts \geq 0 \, \forall \|x\| \leq t\}$$

Worst case: $$x = -t\frac{y}{\|y\|}$$ (nếu $$y \neq 0$$):

$$-t\|y\| + ts \geq 0 \Rightarrow s \geq \|y\|$$

$$K^* = \{(y, s) : \|y\| \leq s\} = K$$

**SOCP cone is self-dual!**

---

**b) Verification:**

$$K^{**} = (K^*)^* = K^* = K$$ ✓

---

**c) SOCP duality:**

**Primal:**

$$
\begin{align}
\min \quad & c^Tx \\
\text{s.t.} \quad & \|A_ix + b_i\| \leq c_i^Tx + d_i
\end{align}
$$

**Dual:**

$$
\begin{align}
\max \quad & -b^Ty - d^Tz \\
\text{s.t.} \quad & A^Ty + c^Tz = c \\
& \|y_i\| \leq z_i
\end{align}
$$

Self-duality của SOCP cone → symmetric primal-dual relationship.

</details>

---

## 📝 **Bài tập 4: Minimax Duality**

Cho saddle point problem:

$$\min_{x \in X} \max_{y \in Y} f(x, y)$$

với $$f(x, y) = x^TAy + b^Tx + c^Ty$$.

**Yêu cầu:**  
a) Viết dual problem  
b) Điều kiện cho minimax = maximin  
c) Ví dụ: matrix game $$A = \begin{bmatrix} 2 & -1 \\ -1 & 1 \end{bmatrix}$$, $$X = Y = \Delta_2$$ (simplex)

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Dual problem:**

$$\max_{y \in Y} \min_{x \in X} f(x, y)$$

**Weak duality:**

$$\min_x \max_y f(x, y) \geq \max_y \min_x f(x, y)$$

---

**b) Minimax theorem (von Neumann):**

Nếu $$X, Y$$ compact convex và $$f$$ convex-concave, thì:

$$\min_x \max_y f = \max_y \min_x f$$

và tồn tại saddle point $$(x^*, y^*)$$.

---

**c) Matrix game:**

$$\min_{x \in \Delta_2} \max_{y \in \Delta_2} x^T A y$$

$$A = \begin{bmatrix} 2 & -1 \\ -1 & 1 \end{bmatrix}$$

**Inner max:**

$$\max_y x^TAy = \max\{2x_1 - x_2, -x_1 + x_2\}$$

(chọn pure strategy với payoff cao hơn)

**Outer min:**

$$\min_x \max\{2x_1 - x_2, -x_1 + x_2\}$$

Với $$x_1 + x_2 = 1$$, $$x_2 = 1 - x_1$$:

$$\max\{2x_1 - (1-x_1), -x_1 + (1-x_1)\} = \max\{3x_1 - 1, 1 - 2x_1\}$$

Intersection: $$3x_1 - 1 = 1 - 2x_1 \Rightarrow 5x_1 = 2 \Rightarrow x_1 = 0.4$$

**Nash equilibrium:** $$x^* = (0.4, 0.6)$$, value = $$0.2$$

</details>

---

## 📝 **Bài tập 5: Lagrangian Relaxation**

Cho integer program:

$$
\begin{align}
\min \quad & c^Tx \\
\text{s.t.} \quad & Ax \leq b \\
& x \in \{0, 1\}^n
\end{align}
$$

**Yêu cầu:**  
a) Viết Lagrangian relaxation  
b) Explain lower bound property  
c) Ví dụ: $$c = (1, 2)$$, $$A = [1, 1]$$, $$b = 1$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Lagrangian relaxation:**

$$L(x, \lambda) = c^Tx + \lambda^T(Ax - b)$$

$$g(\lambda) = \min_{x \in \{0,1\}^n} L(x, \lambda) = \min_{x \in \{0,1\}^n} (c + A^T\lambda)^Tx - \lambda^Tb$$

Minimize mỗi $$x_i$$ độc lập:

$$x_i^* = \begin{cases}
0 & \text{if } c_i + (A^T\lambda)_i > 0 \\
1 & \text{if } c_i + (A^T\lambda)_i < 0
\end{cases}$$

---

**b) Lower bound:**

$$\max_{\lambda \geq 0} g(\lambda) \leq p^*$$

Giải dual (easier) → bound for primal (NP-hard).

---

**c) Example:**

$$\min x_1 + 2x_2$$ s.t. $$x_1 + x_2 \leq 1$$, $$x \in \{0,1\}^2$$

**Lagrangian:**

$$L(x, \lambda) = x_1 + 2x_2 + \lambda(x_1 + x_2 - 1) = (1+\lambda)x_1 + (2+\lambda)x_2 - \lambda$$

**Dual function:**

$$g(\lambda) = \min_{x \in \{0,1\}^2} [(1+\lambda)x_1 + (2+\lambda)x_2] - \lambda$$

$$= -\lambda$$ (chọn $$x_1 = x_2 = 0$$ nếu $$\lambda < -1$$)

$$= 1 + \lambda - \lambda = 1$$ (chọn $$x_1 = 1, x_2 = 0$$ nếu $$-2 < \lambda < -1$$)

**Dual optimal:** $$\lambda^* = -1$$, $$g^* = 1$$

**Primal optimal:** $$x^* = (1, 0)$$, $$p^* = 1$$

**Strong duality!** (lucky case)

</details>

---

## 💡 **Tổng kết**

### **Duality Concepts:**

| Concept | Key Idea |
|---------|----------|
| **Perturbation** | $$\lambda^* = -dp^*/du$$ (sensitivity) |
| **Slater's condition** | Guarantees strong duality |
| **Dual cone** | $$K^* = \{y : y^Tx \geq 0 \, \forall x \in K\}$$ |
| **Minimax** | $$\min \max = \max \min$$ under convexity |
| **Lagrangian relaxation** | Relax hard constraints → dual bound |

### **When strong duality holds:**
- **LP:** Always (feasible)
- **Convex:** Slater's condition
- **SOCP/SDP:** Interior point exists
- **Non-convex:** Generally fails (duality gap)

---

## 📚 **Tài liệu Tham khảo**

1. Boyd, S., & Vandenberghe, L. (2004). *Convex Optimization*. Chapter 5.
2. Rockafellar, R. T. (1970). *Convex Analysis*. Princeton.
3. Borwein, J., & Lewis, A. (2006). *Convex Analysis and Nonlinear Optimization*.

