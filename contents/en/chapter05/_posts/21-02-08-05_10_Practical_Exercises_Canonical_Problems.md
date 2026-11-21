---
layout: post
title: '05-10 Practical Exercises - Canonical Problems'
chapter: '05'
order: 16
owner: GitHub Copilot
lang: en
categories:
- chapter05
lesson_type: required
redirect_from:
  - /contents/en/chapter05/05_08_Practical_Exercises_Canonical_Problems/
---

# Practical Exercises - Canonical Problems

The exercises are adapted from Boyd & Vandenberghe (2004) and Ben-Tal & Nemirovski (2001).

---

## 📝 **Part I: Linear Programming (LP)**

### **Exercise 1: The Diet Problem**

A person needs to plan a diet with 3 foods:
- Food 1: 2 units of protein, 1 unit of carbs, price 3 USD
- Food 2: 1 unit of protein, 2 units of carbs, price 2 USD  
- Food 3: 1 unit of protein, 1 unit of carbs, price 1.5 USD

Minimum requirement: 5 units of protein and 6 units of carbs per day.

**Tasks:**  
a) Write the LP that minimizes the cost  
b) Find the optimal solution  
c) Explain the meaning of the dual variables (shadow prices)

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Formulation:**

Variables: $$x_i$$ = amount of food $$i$$ ($$i = 1,2,3$$)

$$
\begin{align}
\min_{x} \quad & 3x_1 + 2x_2 + 1.5x_3 \\
\text{s.t.} \quad & 2x_1 + x_2 + x_3 \geq 5 \quad \text{(protein)} \\
& x_1 + 2x_2 + x_3 \geq 6 \quad \text{(carbs)} \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**Standard form (min with $$\leq$$):**

$$
\begin{align}
\min_{x} \quad & 3x_1 + 2x_2 + 1.5x_3 \\
\text{s.t.} \quad & -2x_1 - x_2 - x_3 \leq -5 \\
& -x_1 - 2x_2 - x_3 \leq -6 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

---

**b) Find the optimal solution:**

Food 3 is the cheapest per unit of nutrition, so the optimal solution uses a lot of food 3. Consider the vertex $$x = (0, 1, 4)$$ (both constraints active, $$x_1 = 0$$):

$$\text{Protein: } 0 + 1 + 4 = 5 \text{ ✓}, \qquad \text{Carbs: } 0 + 2 + 4 = 6 \text{ ✓}$$

Cost: $$3 \cdot 0 + 2 \cdot 1 + 1.5 \cdot 4 = 8$$ USD.

Optimality is confirmed by the dual in part c): there is a feasible $$\lambda$$ whose dual value equals 8.

**Optimal solution:** $$x^* = (0, 1, 4)$$, cost = 8 USD

(Note: the vertex with $$x_3 = 0$$, $$x = (\frac{4}{3}, \frac{7}{3}, 0)$$, is feasible but its cost $$\frac{26}{3} \approx 8.67 > 8$$, so it is **not** optimal.)

---

---

**c) Dual variables (Shadow prices):**

Dual problem:

$$
\max_{\lambda} \quad 5\lambda_1 + 6\lambda_2 \quad \text{s.t.} \quad A^T\lambda \leq c, \, \lambda \geq 0
$$

that is, $$2\lambda_1 + \lambda_2 \leq 3$$, $$\lambda_1 + 2\lambda_2 \leq 2$$, $$\lambda_1 + \lambda_2 \leq 1.5$$.

With $$\lambda^* = (1, \frac{1}{2})$$ (from complementary slackness: since $$x_2, x_3 > 0$$, dual constraints 2 and 3 must be tight): constraint 1 reads $$2 + 0.5 = 2.5 < 3$$ (slack, consistent with $$x_1^* = 0$$), and the dual value $$5(1) + 6(0.5) = 8$$ equals the primal value → optimal (strong duality).

**Meaning:**
- $$\lambda_1^* = 1$$: raising the protein requirement by 1 unit → cost increases by 1 USD
- $$\lambda_2^* = \frac{1}{2}$$: raising the carbs requirement by 1 unit → cost increases by 0.5 USD

Protein is "more expensive" than carbs in this setting!

</details>

---

## 📝 **Part II: Quadratic Programming (QP)**

### **Exercise 2: Portfolio Optimization**

Invest in 2 assets with:
- Expected returns: $$\mu = (0.12, 0.10)^T$$
- Covariance matrix: $$\Sigma = \begin{bmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{bmatrix}$$

**Tasks:**  
a) Write the problem of minimizing risk with target return $$r = 0.11$$  
b) Find the optimal portfolio  
c) Plot the efficient frontier

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Formulation:**

$$
\begin{align}
\min_{x} \quad & \frac{1}{2} x^T \Sigma x \\
\text{s.t.} \quad & \mu^T x = r \\
& \mathbf{1}^T x = 1 \\
& x \geq 0
\end{align}
$$

With $$r = 0.11$$:

$$
\begin{align}
\min_{x} \quad & \frac{1}{2}(0.04x_1^2 + 0.02x_1x_2 + 0.09x_2^2) \\
\text{s.t.} \quad & 0.12x_1 + 0.10x_2 = 0.11 \\
& x_1 + x_2 = 1 \\
& x_1, x_2 \geq 0
\end{align}
$$

---

**b) Solve using the constraints:**

From $$x_1 + x_2 = 1$$ and $$0.12x_1 + 0.10x_2 = 0.11$$:

$$0.12x_1 + 0.10(1-x_1) = 0.11 \Rightarrow 0.02x_1 = 0.01 \Rightarrow x_1 = 0.5$$

$$x_2 = 0.5$$

**Solution:** $$x^* = (0.5, 0.5)^T$$

**Feasibility check:** $$0.5 + 0.5 = 1$$ ✓, $$0.12(0.5) + 0.10(0.5) = 0.11$$ ✓

**Risk (variance):**

$$\sigma^2 = x^{*T} \Sigma x^* = \begin{bmatrix} 0.5 & 0.5 \end{bmatrix} \begin{bmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{bmatrix} \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix}$$

$$= \begin{bmatrix} 0.5 & 0.5 \end{bmatrix} \begin{bmatrix} 0.025 \\ 0.05 \end{bmatrix} = 0.0375$$

**Standard deviation:** $$\sigma = \sqrt{0.0375} \approx 0.194 = 19.4\%$$

---

**c) Efficient frontier:**

Vary $$r$$ from $$\min(\mu_i) = 0.10$$ to $$\max(\mu_i) = 0.12$$:

| Return $$r$$ | $$x_1$$ | $$x_2$$ | Risk $$\sigma$$ |
|-------------|---------|---------|-----------------|
| 0.10 | 0 | 1 | 0.300 |
| 0.105 | 0.25 | 0.75 | 0.238 |
| 0.11 | 0.5 | 0.5 | 0.194 |
| 0.1145 | 0.727 | 0.273 | 0.178 (minimum risk) |
| 0.115 | 0.75 | 0.25 | 0.179 |
| 0.12 | 1 | 0 | 0.200 |

**Conclusion:** The (risk, return) curve has minimum risk at $$x_1 = 0.08/0.11 \approx 0.727$$ ($$r \approx 0.1145$$). Only the branch $$r \geq 0.1145$$ is the **efficient frontier** (higher return for the same risk); points with $$r < 0.1145$$ are dominated.

</details>

---

## 📝 **Part III: QCQP and SOCP**

### **Exercise 3: Robust Least Squares (SOCP)**

Given data $$A \in \mathbb{R}^{m \times n}$$, $$b \in \mathbb{R}^m$$. Instead of ordinary least squares, consider the robust version:

$$
\min_{x} \quad \|Ax - b\|_2 + \gamma \|x\|_2
$$

where $$\gamma > 0$$ is a regularization parameter.

**Tasks:**  
a) Write it as an SOCP  
b) With $$A = \begin{bmatrix} 1 & 1 \\ 1 & -1 \\ 2 & 0 \end{bmatrix}$$, $$b = \begin{bmatrix} 2 \\ 0 \\ 3 \end{bmatrix}$$, $$\gamma = 0.1$$, find the solution

<details>
<summary><strong>💡 Solution</strong></summary>

**a) SOCP formulation:**

Let:
- $$t_1$$ sao cho $$\|Ax - b\|_2 \leq t_1$$
- $$t_2$$ sao cho $$\|x\|_2 \leq t_2$$

The problem becomes:

$$
\begin{align}
\min_{x, t_1, t_2} \quad & t_1 + \gamma t_2 \\
\text{s.t.} \quad & \|Ax - b\|_2 \leq t_1 \\
& \|x\|_2 \leq t_2
\end{align}
$$

This is an **SOCP** with 2 second-order cone constraints.

**Standard SOCP form:**

$$
\begin{align}
\min \quad & c^T y \\
\text{s.t.} \quad & \|A_i y + b_i\|_2 \leq c_i^T y + d_i, \quad i = 1, \ldots, k
\end{align}
$$

---

**b) Numerical solution:**

Data:

$$A = \begin{bmatrix} 1 & 1 \\ 1 & -1 \\ 2 & 0 \end{bmatrix}, \quad b = \begin{bmatrix} 2 \\ 0 \\ 3 \end{bmatrix}, \quad \gamma = 0.1$$

**Analytical approach (approximate):**

Gradient of $$f(x) = \|Ax-b\|_2 + \gamma\|x\|_2$$:

$$\nabla f(x) = \frac{A^T(Ax-b)}{\|Ax-b\|_2} + \gamma \frac{x}{\|x\|_2}$$

(Complicated because $$f$$ is non-smooth at $$x = 0$$ and at $$Ax = b$$)

**Method 1: approximate by regularized LS with a closed form:**

Approximate by $$\min \|Ax-b\|_2^2 + \gamma^2\|x\|_2^2$$:

$$x_{\text{ridge}} = (A^TA + \gamma^2 I)^{-1} A^T b$$

Compute:

$$A^TA = \begin{bmatrix} 1 & 1 & 2 \\ 1 & -1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & -1 \\ 2 & 0 \end{bmatrix} = \begin{bmatrix} 6 & 0 \\ 0 & 2 \end{bmatrix}$$

$$A^TA + 0.01I = \begin{bmatrix} 6.01 & 0 \\ 0 & 2.01 \end{bmatrix}$$

$$A^Tb = \begin{bmatrix} 1 & 1 & 2 \\ 1 & -1 & 0 \end{bmatrix} \begin{bmatrix} 2 \\ 0 \\ 3 \end{bmatrix} = \begin{bmatrix} 8 \\ 2 \end{bmatrix}$$

Solving: $$x_{\text{ridge}} = \left(\frac{8}{6.01}, \frac{2}{2.01}\right) \approx (1.331, 0.995)^T$$, with $$f(x_{\text{ridge}}) \approx 0.744$$.

**Method 2: numerical solution of the original SOCP** (directly solving $$\min \|Ax-b\|_2 + 0.1\|x\|_2$$):

$$x^* \approx (1.326, 0.983)^T, \qquad f(x^*) \approx 0.743$$

(The two solutions are close but not identical, because the original problem uses the $$\ell_2$$ norm rather than its square.)

</details>

---

## 📝 **Part IV: Semidefinite Programming (SDP)**

### **Exercise 4: Matrix Completion**

Given a matrix $$M \in \mathbb{R}^{3 \times 3}$$ with some missing entries. Known:

$$M_{11} = 4, \quad M_{12} = 2, \quad M_{22} = 5, \quad M_{23} = 1$$

Find the completed positive semidefinite matrix $$X$$ with the smallest trace.

**Tasks:**  
a) Write the SDP  
b) Find the solution

<details>
<summary><strong>💡 Solution</strong></summary>

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

The matrix:

$$X = \begin{bmatrix} 4 & 2 & x_{13} \\ 2 & 5 & 1 \\ x_{13} & 1 & x_{33} \end{bmatrix}$$

---

**b) Solution:**

**PSD condition:** all principal minors are $$\geq 0$$.

**Minor 1×1:** $$4 > 0$$ ✓

**Minor 2×2:** 

$$\begin{vmatrix} 4 & 2 \\ 2 & 5 \end{vmatrix} = 20 - 4 = 16 > 0$$ ✓

**Minor 3×3 (determinant):**

$$\det(X) = 4(5x_{33} - 1) - 2(2x_{33} - x_{13}) + x_{13}(2 - 5x_{13})$$

$$= 20x_{33} - 4 - 4x_{33} + 2x_{13} + 2x_{13} - 5x_{13}^2$$

$$= 16x_{33} - 5x_{13}^2 + 4x_{13} - 4$$

For $$\det(X) \geq 0$$: $$16x_{33} \geq 5x_{13}^2 - 4x_{13} + 4$$

**Minimize $$\text{tr}(X) = 4 + 5 + x_{33} = 9 + x_{33}$$:**

We need to minimize $$x_{33}$$ subject to PSD.

From PSD, we need:

$$x_{33} \geq \frac{5x_{13}^2 - 4x_{13} + 4}{16}$$

Minimize RHS over $$x_{13}$$:

$$\frac{d}{dx_{13}}\left(\frac{5x_{13}^2 - 4x_{13} + 4}{16}\right) = \frac{10x_{13} - 4}{16} = 0$$

$$x_{13}^* = 0.4$$

$$x_{33}^{\min} = \frac{5(0.4)^2 - 4(0.4) + 4}{16} = \frac{0.8 - 1.6 + 4}{16} = \frac{3.2}{16} = 0.2$$

**Solution:**

$$X^* = \begin{bmatrix} 4 & 2 & 0.4 \\ 2 & 5 & 1 \\ 0.4 & 1 & 0.2 \end{bmatrix}, \quad \text{tr}(X^*) = 9.2$$

**Check:** $$\det(X^*) = 16(0.2) - 5(0.16) + 1.6 - 4 = 0$$ (rank-deficient, but $$\succeq 0$$ ✓)

</details>

---

## 📝 **Part V: Putting It Together**

### **Exercise 5: Choosing the Right Formulation**

For each problem, identify the standard class (LP, QP, QCQP, SOCP, SDP):

**a)** $$\min c^T x$$ s.t. $$Ax = b$$, $$\|x\|_\infty \leq 1$$

**b)** $$\min \|Ax - b\|_1$$

**c)** $$\min x^TQx$$ s.t. $$\|Ax - b\|_2 \leq \delta$$ (with $$Q \succeq 0$$)

**d)** $$\min \text{tr}(X)$$ s.t. $$X \succeq yy^T$$, $$X \succeq 0$$

<details>
<summary><strong>💡 Solution</strong></summary>

**a) $$\min c^Tx$$ s.t. $$Ax = b$$, $$\|x\|_\infty \leq 1$$:**

$$\|x\|_\infty \leq 1 \Leftrightarrow -1 \leq x_i \leq 1$$ (linear constraints)

→ **Linear Programming (LP)**

---

**b) $$\min \|Ax - b\|_1$$:**

$$\|Ax - b\|_1 = \sum_i |r_i|$$ with $$r = Ax - b$$

Let $$t_i \geq |r_i|$$:

$$
\begin{align}
\min \quad & \sum_i t_i \\
\text{s.t.} \quad & -t_i \leq (Ax - b)_i \leq t_i
\end{align}
$$

→ **Linear Programming (LP)**

---

**c) $$\min x^TQx$$ s.t. $$\|Ax - b\|_2 \leq \delta$$ (with $$Q \succeq 0$$):**

- Objective: quadratic
- Constraint: second-order cone ($$\ell_2$$ norm)

→ **Second-Order Cone Programming (SOCP)**

(Or QCQP if written as $$\|Ax-b\|_2^2 \leq \delta^2$$)

---

**d) $$\min \text{tr}(X)$$ s.t. $$X \succeq yy^T$$, $$X \succeq 0$$:**

- Objective: linear trong $$X$$
- Constraint: $$X \succeq yy^T$$ → $$X - yy^T \succeq 0$$ (PSD constraint)

→ **Semidefinite Programming (SDP)**

</details>

---

## 💡 **Summary**

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

### **When to use what:**
- **LP:** when everything is linear
- **QP:** risk minimization, LS with regularization
- **SOCP:** Robust optimization, $$\ell_2$$ constraints
- **SDP:** Matrix variables, combinatorial relaxation

---

## 📚 **References**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 4.

2. **Ben-Tal, A., & Nemirovski, A.** (2001). *Lectures on Modern Convex Optimization*. SIAM.

3. **Lobo, M. S., et al.** (1998). "Applications of Second-Order Cone Programming". *Linear Algebra and Applications*.

