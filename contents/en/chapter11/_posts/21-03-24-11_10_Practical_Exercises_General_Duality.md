---
layout: post
title: '11-10 Practical Exercises - General Duality'
chapter: "11"
order: 11
owner: "GitHub Copilot"
lang: en
categories:
  - chapter11
lesson_type: required
redirect_from:
  - /contents/en/chapter11/11_08_Practical_Exercises_General_Duality/
---

# Practical Exercises - General Duality

The exercises are adapted from Boyd & Vandenberghe (2004), Rockafellar (1970), and Bertsekas (1999).

---

## **Part I: The Lagrangian and the Dual Function - Foundations**

### **Exercise 1: Building the Lagrangian (Boyd & Vandenberghe, Ex. 5.1)**

Consider the general problem:

$$
\begin{align}
\min_{x} \quad & f_0(x) \\
\text{s.t.} \quad & f_i(x) \leq 0, \quad i = 1, \ldots, m \\
& h_j(x) = 0, \quad j = 1, \ldots, p
\end{align}
$$

**Task:**
a) Write the Lagrangian $$L(x, \lambda, \nu)$$
b) Define the dual function $$g(\lambda, \nu)$$
c) Let $$f_0(x) = x_1^2 + x_2^2$$, $$f_1(x) = x_1 + x_2 - 1$$, $$h_1(x) = x_1 - x_2$$. Compute $$L$$ and $$g$$

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**a) Lagrangian:**

$$
L(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{j=1}^p \nu_j h_j(x)
$$

where:
- $$\lambda \in \mathbb{R}^m$$, $$\lambda \geq 0$$: dual variables for the inequality constraints
- $$\nu \in \mathbb{R}^p$$: dual variables for the equality constraints (no sign restriction)

---

**b) Dual function:**

$$
g(\lambda, \nu) = \inf_x L(x, \lambda, \nu) = \inf_x \left( f_0(x) + \sum_i \lambda_i f_i(x) + \sum_j \nu_j h_j(x) \right)
$$

**Properties:**
- $$g(\lambda, \nu)$$ is always **concave** in $$(\lambda, \nu)$$
- $$g(\lambda, \nu) \leq p^*$$ (weak duality) for every $$\lambda \geq 0$$

---

**c) Concrete computation:**

Data:

$$
f_0(x) = x_1^2 + x_2^2, \quad f_1(x) = x_1 + x_2 - 1, \quad h_1(x) = x_1 - x_2
$$

**Lagrangian:**

$$
L(x, \lambda, \nu) = x_1^2 + x_2^2 + \lambda(x_1 + x_2 - 1) + \nu(x_1 - x_2)
$$

**Find $$\inf_x L$$:**

FOC:

$$
\frac{\partial L}{\partial x_1} = 2x_1 + \lambda + \nu = 0 \Rightarrow x_1 = -\frac{\lambda + \nu}{2}
$$

$$
\frac{\partial L}{\partial x_2} = 2x_2 + \lambda - \nu = 0 \Rightarrow x_2 = -\frac{\lambda - \nu}{2}
$$

Substituting into $$L$$, we get:

$$
g(\lambda, \nu) = -\frac{\lambda^2 + \nu^2}{2} - \lambda
$$

with $$\lambda \geq 0$$.

</details>

---

### **Exercise 2: Weak Duality (Boyd & Vandenberghe, Ex. 5.2)**

Take the problem and the dual function from Exercise 1c.

**Task:**
a) Solve the primal problem
b) Solve the dual problem: $$\max_{\lambda \geq 0, \nu} g(\lambda, \nu)$$
c) Check strong duality

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**a) Solving the primal:**

$$
\begin{align}
\min_{x} \quad & x_1^2 + x_2^2 \\
\text{s.t.} \quad & x_1 + x_2 \leq 1 \\
& x_1 - x_2 = 0
\end{align}
$$

From $$x_1 = x_2$$ and $$x_1 + x_2 \leq 1$$ → $$2x_1 \leq 1$$ → $$x_1 \leq 0.5$$.

Minimize $$2x_1^2$$ → the minimum is at $$x_1 = 0$$.

**Primal solution:** $$x^* = (0, 0)$$, $$p^* = 0$$

---

**b) Solving the dual:**

$$
\max_{\lambda \geq 0, \nu} \quad -\frac{\lambda^2 + \nu^2}{2} - \lambda
$$

FOC: $$\frac{\partial g}{\partial \lambda} = -\lambda - 1 = 0$$ → $$\lambda = -1$$ (but $$\lambda \geq 0$$ → $$\lambda^* = 0$$)

$$\frac{\partial g}{\partial \nu} = -\nu = 0$$ → $$\nu^* = 0$$

**Dual solution:** $$\lambda^* = 0$$, $$\nu^* = 0$$, $$d^* = 0$$

---

**c) Strong Duality:**

$$p^* = 0 = d^*$$

**Strong duality holds!** ✓ (The problem is convex and satisfies Slater's condition)

</details>

---

## **Part II: Slater's Condition and Strong Duality**

### **Exercise 3: Checking Slater's Condition (Rockafellar, Ex. 28.3)**

For each of the following problems, check Slater's condition:

**a)** $$\min x^2$$ s.t. $$x^2 \leq 1$$

**b)** $$\min x^2$$ s.t. $$x^2 \leq 0$$

**c)** $$\min \frac{1}{2}x^T Q x$$ s.t. $$Ax \leq b$$ with $$Q \succ 0$$

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Slater's condition:** There exists a strictly feasible $$\tilde{x}$$:
- $$f_i(\tilde{x}) < 0$$ for all $$i$$
- $$h_j(\tilde{x}) = 0$$ for all $$j$$

---

**a) $$\min x^2$$ s.t. $$x^2 \leq 1$$:**

Strictly feasible: $$\tilde{x}^2 < 1$$, e.g. $$\tilde{x} = 0$$ ✓

**Slater's condition holds** → strong duality.

---

**b) $$\min x^2$$ s.t. $$x^2 \leq 0$$:**

Strictly feasible: $$\tilde{x}^2 < 0$$ → **does not exist**!

**Slater's condition does NOT hold**.

The feasible set is only $$x = 0$$ (a single point). Strong duality nevertheless still holds ($$p^* = d^* = 0$$).

---

**c) QP with $$Q \succ 0$$, $$Ax \leq b$$:**

Strictly feasible: $$A\tilde{x} < b$$ (component-wise).

**Slater holds** if $$\{x : Ax < b\} \neq \emptyset$$.

</details>

---

## **Part III: Quadratic Programming**

### **Exercise 4: A simple Quadratic Program**

**Problem:**
$$\min_x \frac{1}{2}x^2 + x \quad \text{s.t.} \quad x \geq 1$$

**Task:**
1. Rewrite the problem in standard form
2. Build the Lagrangian
3. Compute the dual function $$g(u)$$
4. Solve the dual problem
5. Compare the primal and dual solutions

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Step 1: Rewrite the problem**
$$\min_x \frac{1}{2}x^2 + x \quad \text{s.t.} \quad -x + 1 \leq 0$$

**Step 2: The Lagrangian**
$$L(x,u) = \frac{1}{2}x^2 + x + u(-x + 1) = \frac{1}{2}x^2 + (1-u)x + u$$

**Step 3: Compute the dual function**
$$g(u) = \inf_x L(x,u)$$

Derivative: $$\frac{\partial L}{\partial x} = x + (1-u) = 0$$ → $$x^* = u - 1$$

Substituting: $$g(u) = -\frac{1}{2}(u-1)^2 + u$$

**Step 4: The dual problem**
$$\max_u g(u) \quad \text{s.t.} \quad u \geq 0$$

$$g'(u) = 2 - u = 0$$ → $$u^* = 2$$

**Step 5: Compare the solutions**
- Dual optimal: $$u^* = 2$$, $$g^* = \frac{3}{2}$$
- Primal optimal: $$x^* = 1$$, $$f^* = \frac{3}{2}$$
- Strong duality: $$f^* = g^*$$ ✓

</details>

---

### **Exercise 5: QP with several constraints**

**Problem:**
$$\min_{x,y} x^2 + y^2 \quad \text{s.t.} \quad x + y \geq 2, \quad x \geq 0, \quad y \geq 0$$

**Task:**
1. Build the full Lagrangian
2. Compute the dual function
3. Find the KKT conditions
4. Solve the problem

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Lagrangian function:**
$$L(x,y,u_1,u_2,u_3) = x^2 + y^2 + u_1(-x - y + 2) + u_2(-x) + u_3(-y)$$

**KKT conditions:**
- $$\frac{\partial L}{\partial x} = 2x - u_1 - u_2 = 0$$
- $$\frac{\partial L}{\partial y} = 2y - u_1 - u_3 = 0$$
- Complementary slackness
- Primal and dual feasibility

**Solution:** $$x^* = y^* = 1$$, $$(u_1^*, u_2^*, u_3^*) = (2, 0, 0)$$

</details>

---

## **Part IV: Support Vector Machine (SVM) Dual**

### **Exercise 6: SVM Dual Formulation (Boyd & Vandenberghe, Ex. 8.6)**

Consider the SVM problem:

$$
\begin{align}
\min_{w, b} \quad & \frac{1}{2}\|w\|^2 \\
\text{s.t.} \quad & y_i(w^T x_i + b) \geq 1, \quad i = 1, \ldots, m
\end{align}
$$

**Task:**
a) Write the Lagrangian
b) Compute the dual function $$g(\alpha)$$
c) Write the dual problem
d) With 3 points $$(1, 1, +1)$$, $$(1, -1, +1)$$, $$(-1, 0, -1)$$, find the dual optimum

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**a) Lagrangian:**

$$
L(w, b, \alpha) = \frac{1}{2}\|w\|^2 - \sum_{i=1}^m \alpha_i (y_i(w^T x_i + b) - 1)
$$

**b) Dual function:**

FOC: $$w = \sum_i \alpha_i y_i x_i$$, $$\sum_i \alpha_i y_i = 0$$

Substituting back:

$$
g(\alpha) = \sum_i \alpha_i - \frac{1}{2}\sum_{i,j} \alpha_i \alpha_j y_i y_j x_i^T x_j
$$

**c) Dual problem:**

$$
\boxed{
\begin{align}
\max_{\alpha} \quad & \sum_i \alpha_i - \frac{1}{2}\sum_{i,j} \alpha_i \alpha_j y_i y_j x_i^T x_j \\
\text{s.t.} \quad & \sum_i \alpha_i y_i = 0 \\
& \alpha_i \geq 0
\end{align}
}
$$

**d) Numerical computation:** All 3 points are support vectors. From $$w = \sum_i \alpha_i y_i x_i$$, $$\sum_i \alpha_i y_i = 0$$ and $$y_i(w^T x_i + b) = 1$$ we get $$\alpha^* = (1/4,\ 1/4,\ 1/2)$$, $$w^* = (1, 0)^T$$, $$b^* = 0$$, and dual value $$= 1 - \frac{1}{2}\|w^*\|^2 = \frac{1}{2}$$.
Decision boundary: $$x_1 = 0$$

</details>

---

## **Part V: Complementary Slackness**

### **Exercise 7: Applying Complementary Slackness**

Consider the LP:

$$
\begin{align}
\min_x \quad & c^T x \\
\text{s.t.} \quad & Ax = b \\
& x \geq 0
\end{align}
$$

**Task:**
a) Write the complementary slackness conditions
b) With $$c = \begin{bmatrix} -1 \\ -2 \end{bmatrix}$$, $$A = \begin{bmatrix} 1 & 1 \end{bmatrix}$$, $$b = 1$$, find the solution
c) Check complementary slackness

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**a) Complementary Slackness:**

$$\lambda_i^* \cdot (-x_i^*) = 0$$

**Meaning:**
- If $$x_i^* > 0$$: $$\lambda_i^* = 0$$
- If $$\lambda_i^* > 0$$: $$x_i^* = 0$$

---

**b) Solving the problem:**

$$\min \quad -x_1 - 2x_2 \quad \text{s.t.} \quad x_1 + x_2 = 1, \quad x \geq 0$$

Maximize $$x_1 + 2x_2$$ subject to $$x_1 + x_2 = 1$$.

**Primal solution:** $$x^* = (0, 1)^T$$, $$p^* = -2$$

**Dual solution:** $$\nu^* = -2$$, $$\lambda^* = (1, 0)^T$$

**c) Check:**
- $$\lambda_1^* \cdot 0 = 0$$ ✓
- $$\lambda_2^* \cdot (-1) = 0$$ ✓

</details>

---

### **Exercise 8: Duality Gap Analysis (Bertsekas, Ex. 6.1.2)**

Consider the problem (note: $$x(x-2) = x^2 - 2x$$ is a convex function):

$$
\min_{x \in [0,2]} \quad x(x-2)
$$

**Task:**
a) Solve the primal problem
b) Write the Lagrangian and find the dual function
c) Solve the dual problem
d) Compute the duality gap

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**a) Solving the primal:**

$$f(x) = x^2 - 2x = (x-1)^2 - 1$$

The minimum is at $$x = 1$$ in $$[0, 2]$$: $$p^* = -1$$

---

**b) Lagrangian:**

Rewrite: $$\min_x x^2 - 2x$$ s.t. $$-x \leq 0$$, $$x - 2 \leq 0$$

$$L(x, \lambda_1, \lambda_2) = x^2 - 2x - \lambda_1 x + \lambda_2(x - 2)$$

**c) Dual analysis:**

Minimizing over $$x$$: $$x = \frac{2 + \lambda_1 - \lambda_2}{2}$$, so $$g(\lambda_1, \lambda_2) = -\frac{(2 + \lambda_1 - \lambda_2)^2}{4} - 2\lambda_2$$. Over $$\lambda \geq 0$$, $$g$$ is maximized at $$\lambda_1 = \lambda_2 = 0$$: $$d^* = g(0, 0) = -1$$.

**d) Duality gap:**

Gap $$= p^* - d^* = -1 - (-1) = 0$$. The problem is convex and satisfies Slater's condition (e.g. $$x = 1$$ satisfies both constraints strictly), so strong duality holds. The solution $$x^* = 1$$ lies in the interior, neither constraint is active, so $$\lambda^* = 0$$ (consistent with complementary slackness).

</details>

---

## **Part VI: Norm Approximation and Related Problems**

### **Exercise 9: Norm Approximation (Boyd & Vandenberghe, Ex. 5.3)**

**Problem:**
$$\min_x \lVert Ax - b \rVert$$

where the norm is $$\ell_1, \ell_2,$$ or $$\ell_\infty$$.

**Task:**
1. Reformulate as a constrained problem
2. Derive the dual for each case
3. Compare the dual problems

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Case 1: $$\ell_1$$ norm**

$$\min_{x,t} \mathbf{1}^T t \quad \text{s.t.} \quad -t \leq Ax - b \leq t$$

Dual:
$$\max_{\lambda,\mu} -b^T(\lambda - \mu) \quad \text{s.t.} \quad A^T(\lambda - \mu) = 0, \quad \lambda + \mu = \mathbf{1}, \quad \lambda,\mu \geq 0$$

---

**Case 2: $$\ell_2$$ norm**

$$\min_{x,t} t \quad \text{s.t.} \quad \lVert Ax - b \rVert_2 \leq t$$

Dual:
$$\max_{\nu} -b^T \nu \quad \text{s.t.} \quad A^T \nu = 0, \quad \lVert \nu \rVert_2 \leq 1$$

---

**Case 3: $$\ell_\infty$$ norm**

$$\min_{x,t} t \quad \text{s.t.} \quad -t\mathbf{1} \leq Ax - b \leq t\mathbf{1}$$

Dual:
$$\max_{\lambda,\mu} -b^T(\lambda - \mu) \quad \text{s.t.} \quad A^T(\lambda - \mu) = 0, \quad \lVert \lambda - \mu \rVert_1 \leq 1$$

</details>

---

### **Exercise 10: Entropy Maximization (Boyd & Vandenberghe, Ex. 5.4)**

**Problem:**
$$\max_x -\sum_{i=1}^n x_i \log x_i \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$

**Task:**
1. Convert to a minimization problem
2. Build the Lagrangian
3. Compute the dual function
4. Find the optimal solution

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Conversion:**
$$\min_x \sum_{i=1}^n x_i \log x_i \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$

**Lagrangian function:**
$$L(x,\nu,\lambda) = \sum_{i=1}^n x_i \log x_i + \nu^T(Ax - b) - \lambda^T x$$

**Optimality conditions:**
$$\frac{\partial L}{\partial x_i} = \log x_i + 1 + (A^T \nu)_i - \lambda_i = 0$$

Suy ra: $$x_i = e^{-(A^T \nu)_i + \lambda_i - 1}$$

**Complementary slackness:**
Since $$x_i = e^{\cdots} > 0$$, we have $$\lambda_i = 0$$: $$x_i = e^{-(A^T \nu)_i - 1}$$. Dual function: $$g(\nu) = -b^T \nu - \sum_{i=1}^n e^{-(A^T \nu)_i - 1}$$; solve $$\max_\nu g(\nu)$$ (unconstrained) and substitute back to obtain $$x^*$$.

</details>

---

## **Part VII: Concrete Computations with Lagrange Multipliers**

### **Exercise 11: Portfolio Optimization with Dual Variables**

**Problem:** An investor with 100 million VND wants to invest in 3 assets with:
- Expected returns: $$r = (12\%, 8\%, 5\%)^T$$
- Risk covariance matrix: $$\Sigma = \begin{bmatrix} 0.04 & 0.01 & 0 \\ 0.01 & 0.02 & 0 \\ 0 & 0 & 0.01 \end{bmatrix}$$

Problem: $$\min_x \frac{1}{2}x^T \Sigma x$$ s.t. $$r^T x \geq 10\%$$, $$\mathbf{1}^T x = 1$$, $$x \geq 0$$

**Task:**
a) Write the Lagrangian with all constraints
b) Derive the KKT conditions
c) Solve for the optimal allocation $$x^*$$
d) Compute the dual variables and explain their economic meaning

<details markdown="1">
<summary><strong>Step-by-step solution</strong></summary>

**a) Lagrangian:**

$$
L(x, \lambda_1, \nu, \lambda_2) = \frac{1}{2}x^T \Sigma x - \lambda_1(r^T x - 0.1) + \nu(\mathbf{1}^T x - 1) - \lambda_2^T x
$$

with $$\lambda_1, \lambda_2 \geq 0$$.

---

**b) KKT conditions:**

**Stationarity:**
$$\nabla_x L = \Sigma x - \lambda_1 r + \nu \mathbf{1} - \lambda_2 = 0$$

**Primal feasibility:**
- $$r^T x \geq 0.1$$
- $$\mathbf{1}^T x = 1$$  
- $$x \geq 0$$

**Dual feasibility:**
$$\lambda_1, \lambda_2 \geq 0$$

**Complementary slackness:**
- $$\lambda_1(r^T x - 0.1) = 0$$
- $$\lambda_{2i} x_i = 0$$ for all $$i$$

---

**c) Solving the problem:**

Assume the return constraint is active ($$r^T x = 0.1$$) and all $$x_i > 0$$ (no short positions).

From complementary slackness: $$\lambda_2 = 0$$.

From stationarity:
$$\Sigma x = \lambda_1 r - \nu \mathbf{1}$$

$$
\begin{bmatrix} 0.04 & 0.01 & 0 \\ 0.01 & 0.02 & 0 \\ 0 & 0 & 0.01 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \lambda_1 \begin{bmatrix} 0.12 \\ 0.08 \\ 0.05 \end{bmatrix} - \nu \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}
$$

Combined with:
- $$x_1 + x_2 + x_3 = 1$$
- $$0.12x_1 + 0.08x_2 + 0.05x_3 = 0.1$$

**Solving the system:**

From equation 3: $$0.01x_3 = 0.05\lambda_1 - \nu$$

From the 2 constraints:
$$x_3 = 1 - x_1 - x_2$$
$$0.12x_1 + 0.08x_2 + 0.05(1 - x_1 - x_2) = 0.1$$
$$0.07x_1 + 0.03x_2 = 0.05$$

Combining the 3 stationarity equations with the 2 constraints (5 linear equations, 5 unknowns) and solving exactly:

$$
x^* = \begin{bmatrix} 7/12 \\ 11/36 \\ 1/9 \end{bmatrix} \approx \begin{bmatrix} 0.583 \\ 0.306 \\ 0.111 \end{bmatrix}, \quad \lambda_1^* = \frac{13}{36} \approx 0.361, \quad \nu^* = \frac{61}{3600} \approx 0.017
$$

**Check:**
- Return: $$0.12 \cdot \frac{7}{12} + 0.08 \cdot \frac{11}{36} + 0.05 \cdot \frac{1}{9} = 0.1$$ ✓, weights sum to $$1$$ ✓, all $$x_i > 0$$ ✓ (the assumption holds)
- Risk: $$\frac{1}{2}x^{*T}\Sigma x^* = \frac{23}{2400} \approx 0.00958$$

---

**d) Economic interpretation:**

- $$\lambda_1^* \approx 0.361$$: **Shadow price of the return constraint**
- Raising the required return from 10% to 11% increases the risk by about $$0.361 \times 0.01 \approx 0.0036$$
- $$\nu^* \approx 0.017$$: **Sensitivity to the budget constraint**
- Relaxing $$\mathbf{1}^T x = 1$$ to $$1 + \delta$$ (small $$\delta$$) changes the optimal risk by about $$-\nu^* \delta$$

- $$\lambda_2 = 0$$: No asset is at the short-selling boundary

**Optimal allocation:** about 58.3% in asset 1, 30.6% in asset 2, 11.1% in asset 3 (i.e. about 58.3 / 30.6 / 11.1 million VND).

</details>

---

### **Exercise 12: Optimal Production with Lagrange Multipliers**

**Problem:** A company makes 2 products, A and B:
- Profit: A = 40 thousand/unit, B = 30 thousand/unit
- Limited resources:
  - Labor: 2A + B ≤ 100 hours
  - Material: A + 2B ≤ 80 kg
  - Machines: A ≤ 40 units

Problem: $$\max_{x_1, x_2} 40x_1 + 30x_2$$ subject to the constraints above.

**Task:**
a) Convert to a minimization and write the Lagrangian
b) Find the optimal solution using KKT
c) Compute the shadow price of each resource
d) If 10 extra labor hours can be bought at 8 thousand/hour, should we buy them?

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**a) Converting to minimization:**

$$\min_{x_1, x_2} -40x_1 - 30x_2$$
$$\text{s.t.} \quad 2x_1 + x_2 \leq 100, \quad x_1 + 2x_2 \leq 80, \quad x_1 \leq 40, \quad x_1, x_2 \geq 0$$

**Lagrangian:**

$$
L(x, \lambda) = -40x_1 - 30x_2 + \lambda_1(2x_1 + x_2 - 100) + \lambda_2(x_1 + 2x_2 - 80) + \lambda_3(x_1 - 40)
$$

---

**b) KKT conditions:**

**Stationarity:**
$$\frac{\partial L}{\partial x_1} = -40 + 2\lambda_1 + \lambda_2 + \lambda_3 = 0$$
$$\frac{\partial L}{\partial x_2} = -30 + \lambda_1 + 2\lambda_2 = 0$$

**Complementary slackness:**
$$\lambda_1(2x_1 + x_2 - 100) = 0$$
$$\lambda_2(x_1 + 2x_2 - 80) = 0$$
$$\lambda_3(x_1 - 40) = 0$$

**Observation:** The vertex $$(40, 20)$$ makes **all three** constraints active at once: $$2(40) + 20 = 100$$, $$40 + 2(20) = 80$$, $$x_1 = 40$$. This is a degenerate vertex.

Comparing the vertices of the feasible region: $$(0, 0) \to 0$$, $$(0, 40) \to 1200$$, $$(40, 20) \to 2200$$, $$(40, 0) \to 1600$$.

**Optimal solution:** $$x_1^* = 40$$, $$x_2^* = 20$$, profit $$40(40) + 30(20) = 2200$$ thousand

**KKT multipliers:** Since $$x_1^*, x_2^* > 0$$, stationarity gives:

$$2\lambda_1 + \lambda_2 + \lambda_3 = 40$$
$$\lambda_1 + 2\lambda_2 = 30$$

Let $$\lambda_2 = s$$: $$\lambda_1 = 30 - 2s$$, $$\lambda_3 = 3s - 20$$. The condition $$\lambda \geq 0$$ gives $$20/3 \leq s \leq 15$$, so the multipliers are **not unique** (because of degeneracy). For example:
- $$s = 20/3$$: $$\lambda = (50/3,\ 20/3,\ 0)$$
- $$s = 10$$: $$\lambda = (10,\ 10,\ 10)$$
- $$s = 15$$: $$\lambda = (0,\ 15,\ 25)$$

Every choice gives the dual value $$100\lambda_1 + 80\lambda_2 + 40\lambda_3 = 2200$$ ✓ (strong duality).

---

**c) Shadow prices (Dual variables):**

Because the multipliers are not unique, each shadow price is only meaningful **in one direction**:
- **Labor:** $$\lambda_1 \in [0,\ 50/3]$$. Losing 1 labor hour lowers profit by about $$50/3 \approx 16.7$$ thousand, but **adding** 1 hour raises profit by **0**.
- **Material:** $$\lambda_2 \in [20/3,\ 15]$$. Adding 1 kg raises profit by about $$20/3 \approx 6.7$$ thousand; removing 1 kg lowers it by about 15 thousand.
- **Machines:** $$\lambda_3 \in [0,\ 25]$$. Relaxing $$x_1 \leq 40$$ by 1 unit raises profit by **0** (labor immediately becomes the limit); tightening it costs about 25 thousand.

---

**d) Decision on buying labor:**

With 110 labor hours, the constraints $$x_1 \leq 40$$ and $$x_1 + 2x_2 \leq 80$$ still keep the solution at $$(40, 20)$$, and profit stays at 2200 thousand. The shadow price **for an increase** in labor is 0.

Cost: $$10 \times 8 = 80$$ thousand; benefit: 0.

**Conclusion:** ❌ **DO NOT BUY.** Buying 10 hours loses 80 thousand. The real bottlenecks are material and machines.

**Note:** At a degenerate vertex, the derivative of the optimal profit with respect to a resource differs on the two sides, so always check the range in sensitivity analysis before using a shadow price.

</details>

---

## **Summary of Strategy**

### **Lagrangian Duality:**
- **Lagrangian:** $$L(x, \lambda, \nu) = f_0(x) + \sum_i \lambda_i f_i(x) + \sum_j \nu_j h_j(x)$$
- **Dual function:** $$g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$$
- **Dual problem:** $$\max_{\lambda \geq 0, \nu} g(\lambda, \nu)$$

### **Duality Relations:**
- **Weak duality:** $$d^* \leq p^*$$ always holds
- **Strong duality:** $$d^* = p^*$$ (requires Slater's condition)
- **Duality gap:** $$p^* - d^* \geq 0$$

### **Complementary Slackness:**
- $$\lambda_i^* f_i(x^*) = 0$$ for all $$i$$
- Active constraints may have $$\lambda_i^* > 0$$
- Inactive constraints have $$\lambda_i^* = 0$$

### **When to use the dual:**
- The dual problem is easier to solve
- Sensitivity analysis is needed (shadow prices)
- Algorithm efficiency (interior point methods)
- Fewer variables (as in SVM: $$m < n$$)

---

## **References**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 5.

2. **Rockafellar, R. T.** (1970). *Convex Analysis*. Princeton University Press. Chapter 28.

3. **Bertsekas, D. P.** (1999). *Nonlinear Programming* (2nd ed.). Athena Scientific. Chapter 6.

4. **Luenberger, D. G., & Ye, Y.** (2008). *Linear and Nonlinear Programming* (3rd ed.). Springer.

5. **Bazaraa, M. S., Sherali, H. D., & Shetty, C. M.** (2006). *Nonlinear Programming: Theory and Algorithms* (3rd ed.). Wiley.
