---
layout: post
title: '16-5 Practical Exercises - Duality Revisited'
chapter: '16'
order: 6
owner: GitHub Copilot
lang: en
categories:
- chapter16
lesson_type: required
published: false
---

# Practical Exercises - Duality Revisited

The exercises are adapted from Boyd & Vandenberghe (2004) and Rockafellar (1970).

---

## 📝 **Exercise 1: Perturbation Analysis**

Consider the problem:

$$
\begin{align}
\min_{x} \quad & x^2 \\
\text{s.t.} \quad & x \geq u
\end{align}
$$

**Tasks:**  
a) Find $$p^*(u)$$ (the optimal value as a function of $$u$$)  
b) Verify $$\lambda^* = \frac{dp^*}{du}$$ (the constraint $$u - x \leq 0$$ gets tighter as $$u$$ increases)  
c) Explain the economic meaning

<details>
<summary><strong>💡 Solution</strong></summary>

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

- If $$u \geq 0$$: $$x^* = u$$, $$\lambda^* = 2u = \frac{dp^*}{du}$$ ✓
- If $$u < 0$$: $$x^* = 0$$, $$\lambda^* = 0$$ ✓

**c) Meaning:** $$\lambda^*$$ is the sensitivity of the optimal cost to a change in the constraint.

</details>

---

## 📝 **Exercise 2: Strong Duality via Slater's Condition**

Consider the QCQP:

$$
\begin{align}
\min_{x} \quad & x_1^2 + x_2^2 \\
\text{s.t.} \quad & (x_1 - 1)^2 + x_2^2 \leq 1 \\
& x_1 + x_2 \geq 1
\end{align}
$$

**Tasks:**  
a) Check Slater's condition  
b) Write the dual problem  
c) Verify strong duality

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Slater's condition:**

We need to find a strictly feasible $$\tilde{x}$$:

$$
\begin{cases}
(x_1 - 1)^2 + x_2^2 < 1 \\
x_1 + x_2 > 1
\end{cases}
$$

Try $$\tilde{x} = (1, 0.5)$$:

$$(1-1)^2 + (0.5)^2 = 0.25 < 1$$ ✓

$$1 + 0.5 = 1.5 > 1$$ ✓

**Slater's condition is satisfied** → strong duality holds!

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

Primal optimal: $$x^* = (0.5, 0.5)$$, $$p^* = 0.5$$ (the disk constraint is not active because $$(0.5-1)^2 + 0.5^2 = 0.5 < 1$$)

Dual optimal: $$\lambda^* = (0, 1)$$, $$d^* = 0.5$$ (from $$g(0, \lambda_2) = \lambda_2 - \lambda_2^2/2$$, maximized at $$\lambda_2 = 1$$)

**Gap:** $$p^* - d^* = 0$$ ✓ (strong duality!)

</details>

---

## 📝 **Exercise 3: Dual Cones and Conic Duality**

Consider the second-order cone: $$K = \{(x, t) : \|x\| \leq t\}$$.

**Tasks:**  
a) Find the dual cone $$K^*$$  
b) Verify $$K^{**} = K$$ (self-dual)  
c) Apply to SOCP duality

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Dual cone:**

$$K^* = \{(y, s) : \langle (x,t), (y,s) \rangle \geq 0 \, \forall (x,t) \in K\}$$

$$= \{(y, s) : x^Ty + ts \geq 0 \, \forall \|x\| \leq t\}$$

Worst case: $$x = -t\frac{y}{\|y\|}$$ (if $$y \neq 0$$):

$$-t\|y\| + ts \geq 0 \Rightarrow s \geq \|y\|$$

$$K^* = \{(y, s) : \|y\| \leq s\} = K$$

**The SOCP cone is self-dual!**

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
\max \quad & -\sum_i (b_i^Ty_i + d_iz_i) \\
\text{s.t.} \quad & \sum_i (A_i^Ty_i + c_iz_i) = c \\
& \|y_i\| \leq z_i
\end{align}
$$

The self-duality of the SOCP cone → a symmetric primal-dual relationship.

</details>

---

## 📝 **Exercise 4: Minimax Duality**

Consider the saddle point problem:

$$\min_{x \in X} \max_{y \in Y} f(x, y)$$

with $$f(x, y) = x^TAy + b^Tx + c^Ty$$.

**Tasks:**  
a) Write the dual problem  
b) Conditions for minimax = maximin  
c) Example: the matrix game $$A = \begin{bmatrix} 2 & -1 \\ -1 & 1 \end{bmatrix}$$, $$X = Y = \Delta_2$$ (the simplex)

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Dual problem:**

$$\max_{y \in Y} \min_{x \in X} f(x, y)$$

**Weak duality:**

$$\min_x \max_y f(x, y) \geq \max_y \min_x f(x, y)$$

---

**b) Minimax theorem (von Neumann):**

If $$X, Y$$ are compact convex sets and $$f$$ is convex-concave, then:

$$\min_x \max_y f = \max_y \min_x f$$

and a saddle point $$(x^*, y^*)$$ exists.

---

**c) Matrix game:**

$$\min_{x \in \Delta_2} \max_{y \in \Delta_2} x^T A y$$

$$A = \begin{bmatrix} 2 & -1 \\ -1 & 1 \end{bmatrix}$$

**Inner max:**

$$\max_y x^TAy = \max\{2x_1 - x_2, -x_1 + x_2\}$$

(choose the pure strategy with the higher payoff)

**Outer min:**

$$\min_x \max\{2x_1 - x_2, -x_1 + x_2\}$$

With $$x_1 + x_2 = 1$$, $$x_2 = 1 - x_1$$:

$$\max\{2x_1 - (1-x_1), -x_1 + (1-x_1)\} = \max\{3x_1 - 1, 1 - 2x_1\}$$

Intersection: $$3x_1 - 1 = 1 - 2x_1 \Rightarrow 5x_1 = 2 \Rightarrow x_1 = 0.4$$

**Nash equilibrium:** $$x^* = (0.4, 0.6)$$, value = $$0.2$$

</details>

---

## 📝 **Exercise 5: Lagrangian Relaxation**

Consider the integer program:

$$
\begin{align}
\min \quad & c^Tx \\
\text{s.t.} \quad & Ax \leq b \\
& x \in \{0, 1\}^n
\end{align}
$$

**Tasks:**  
a) Write the Lagrangian relaxation  
b) Explain the lower bound property  
c) Example: $$c = (-1, -2)$$, $$A = [1, 1]$$, $$b = 1$$

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Lagrangian relaxation:**

$$L(x, \lambda) = c^Tx + \lambda^T(Ax - b)$$

$$g(\lambda) = \min_{x \in \{0,1\}^n} L(x, \lambda) = \min_{x \in \{0,1\}^n} (c + A^T\lambda)^Tx - \lambda^Tb$$

Minimize over each $$x_i$$ independently:

$$x_i^* = \begin{cases}
0 & \text{if } c_i + (A^T\lambda)_i > 0 \\
1 & \text{if } c_i + (A^T\lambda)_i < 0
\end{cases}$$

---

**b) Lower bound:**

$$\max_{\lambda \geq 0} g(\lambda) \leq p^*$$

Solving the dual (easier) → a bound for the primal (NP-hard).

---

**c) Example:**

$$\min -x_1 - 2x_2$$ s.t. $$x_1 + x_2 \leq 1$$, $$x \in \{0,1\}^2$$

**Primal optimal:** $$x^* = (0, 1)$$, $$p^* = -2$$

**Lagrangian** (with $$\lambda \geq 0$$):

$$L(x, \lambda) = -x_1 - 2x_2 + \lambda(x_1 + x_2 - 1) = (\lambda - 1)x_1 + (\lambda - 2)x_2 - \lambda$$

**Dual function:**

$$g(\lambda) = \min(0, \lambda - 1) + \min(0, \lambda - 2) - \lambda = \begin{cases} \lambda - 3 & 0 \leq \lambda \leq 1 \\ -2 & 1 \leq \lambda \leq 2 \\ -\lambda & \lambda \geq 2 \end{cases}$$

**Dual optimal:** $$\lambda^* \in [1, 2]$$, $$d^* = -2 = p^*$$

**Strong duality!** (a lucky case; in general the relaxation only gives a lower bound $$d^* \leq p^*$$)

</details>

---

## 💡 **Summary**

### **Duality Concepts:**

| Concept | Key Idea |
|---------|----------|
| **Perturbation** | $$\lambda^* = -dp^*/du$$ for constraints $$f_i(x) \leq u_i$$ (sensitivity) |
| **Slater's condition** | Guarantees strong duality |
| **Dual cone** | $$K^* = \{y : y^Tx \geq 0 \, \forall x \in K\}$$ |
| **Minimax** | $$\min \max = \max \min$$ under convexity |
| **Lagrangian relaxation** | Relax hard constraints → dual bound |

### **When strong duality holds:**
- **LP:** Always (if feasible)
- **Convex:** Slater's condition
- **SOCP/SDP:** An interior point exists
- **Non-convex:** Generally fails (duality gap)

---

## 📚 **References**

1. Boyd, S., & Vandenberghe, L. (2004). *Convex Optimization*. Chapter 5.
2. Rockafellar, R. T. (1970). *Convex Analysis*. Princeton.
3. Borwein, J., & Lewis, A. (2006). *Convex Analysis and Nonlinear Optimization*.
