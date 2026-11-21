---
layout: post
title: '13-8 Practical Exercises - Duality Applications'
chapter: '13'
order: 9
owner: GitHub Copilot
lang: en
categories:
- chapter13
lesson_type: required
---

# Practical Exercises - Applications of Duality

The exercises are adapted from Boyd & Vandenberghe (2004), Rockafellar (1970), and Ben-Tal & Nemirovski (2001).

---

## 📝 **Part I: Dual Norms**

### **Exercise 1: Computing Dual Norms (Boyd & Vandenberghe, Ex. 3.7)**

Given a norm $$\|x\|$$, the dual norm is defined as:

$$
\|y\|_* = \max_{\|x\| \leq 1} y^T x
$$

**Tasks:** Find the dual norm of the following norms:

a) $$\|x\|_1 = \sum_{i=1}^n |x_i|$$  
b) $$\|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2}$$  
c) $$\|x\|_\infty = \max_i |x_i|$$  
d) $$\|x\|_p = (\sum_{i=1}^n |x_i|^p)^{1/p}$$ with $$p \geq 1$$

<details>
<summary><strong>💡 Solution</strong></summary>

**General formula:** The dual norm of $$\|\cdot\|_p$$ is $$\|\cdot\|_q$$ with $$\frac{1}{p} + \frac{1}{q} = 1$$.

---

**a) The $$\ell_1$$ norm:**

We need to find:

$$
\|y\|_* = \max_{\|x\|_1 \leq 1} y^T x = \max_{\sum_i |x_i| \leq 1} \sum_i y_i x_i
$$

**Analysis:**  
- To maximize $$\sum_i y_i x_i$$, choose $$x_i$$ with the same sign as $$y_i$$
- Constraint: $$\sum_i |x_i| \leq 1$$

Optimal solution: set $$x_j = \text{sign}(y_j)$$ with $$j = \arg\max_i |y_i|$$, and all other $$x_i$$ = 0.

Result:

$$
\|y\|_* = \max_i |y_i| = \|y\|_\infty
$$

**Conclusion:** $$(\|\cdot\|_1)_* = \|\cdot\|_\infty$$

---

**b) The $$\ell_2$$ norm:**

$$
\|y\|_* = \max_{\|x\|_2 \leq 1} y^T x
$$

By the Cauchy-Schwarz inequality:

$$
y^T x \leq \|y\|_2 \|x\|_2 \leq \|y\|_2
$$

Equality holds when $$x = \frac{y}{\|y\|_2}$$.

**Conclusion:** $$(\|\cdot\|_2)_* = \|\cdot\|_2$$ (self-dual)

---

**c) The $$\ell_\infty$$ norm:**

$$
\|y\|_* = \max_{\max_i |x_i| \leq 1} \sum_i y_i x_i
$$

Choose $$x_i = \text{sign}(y_i)$$ for every $$i$$ (since $$|x_i| \leq 1$$):

$$
\|y\|_* = \sum_i |y_i| = \|y\|_1
$$

**Conclusion:** $$(\|\cdot\|_\infty)_* = \|\cdot\|_1$$

---

**d) The general $$\ell_p$$ norm:**

By Hölder's inequality:

$$
y^T x \leq \|y\|_q \|x\|_p
$$

with $$\frac{1}{p} + \frac{1}{q} = 1$$.

Equality is attained when $$x_i = c \cdot \text{sign}(y_i) |y_i|^{q-1}$$ (with $$c$$ chosen so that $$\|x\|_p = 1$$).

**Conclusion:** $$(\|\cdot\|_p)_* = \|\cdot\|_q$$ with $$\frac{1}{p} + \frac{1}{q} = 1$$

---

**Summary table:**

| Primal norm | Dual norm | Relation |
|--------------|------------|---------|
| $$\|\cdot\|_1$$ | $$\|\cdot\|_\infty$$ | $$p=1, q=\infty$$ |
| $$\|\cdot\|_2$$ | $$\|\cdot\|_2$$ | Self-dual |
| $$\|\cdot\|_\infty$$ | $$\|\cdot\|_1$$ | $$p=\infty, q=1$$ |
| $$\|\cdot\|_p$$ | $$\|\cdot\|_q$$ | $$1/p + 1/q = 1$$ |

</details>

---

### **Exercise 2: Verifying the Dual Norm Property**

With $$x = (3, 4)^T$$ and $$y = (0.6, 0.8)^T$$:

**Tasks:**  
a) Compute $$\|x\|_1$$, $$\|x\|_2$$, $$\|x\|_\infty$$  
b) Compute $$\|y\|_1$$, $$\|y\|_2$$, $$\|y\|_\infty$$  
c) Verify: $$y^T x \leq \|y\|_* \|x\|$$ for each pair of norms

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Norms of $$x = (3,4)$$:**

$$
\begin{align}
\|x\|_1 &= |3| + |4| = 7 \\
\|x\|_2 &= \sqrt{3^2 + 4^2} = \sqrt{25} = 5 \\
\|x\|_\infty &= \max(|3|, |4|) = 4
\end{align}
$$

---

**b) Norms of $$y = (0.6, 0.8)$$:**

$$
\begin{align}
\|y\|_1 &= 0.6 + 0.8 = 1.4 \\
\|y\|_2 &= \sqrt{0.6^2 + 0.8^2} = \sqrt{0.36 + 0.64} = 1 \\
\|y\|_\infty &= \max(0.6, 0.8) = 0.8
\end{align}
$$

---

**c) Verifying the inequality:**

Compute $$y^T x$$:

$$
y^T x = 0.6 \times 3 + 0.8 \times 4 = 1.8 + 3.2 = 5
$$

**Case 1:** $$\|x\|_1$$ and $$\|y\|_\infty$$ (since $$(\|\cdot\|_1)_* = \|\cdot\|_\infty$$)

$$
y^T x = 5 \leq \|y\|_\infty \|x\|_1 = 0.8 \times 7 = 5.6
$$

✓ Satisfied

---

**Case 2:** $$\|x\|_2$$ and $$\|y\|_2$$ (self-dual)

$$
y^T x = 5 \leq \|y\|_2 \|x\|_2 = 1 \times 5 = 5
$$

✓ Equality (since $$y = \frac{x}{\|x\|_2}$$)

---

**Case 3:** $$\|x\|_\infty$$ and $$\|y\|_1$$ (since $$(\|\cdot\|_\infty)_* = \|\cdot\|_1$$)

$$
y^T x = 5 \leq \|y\|_1 \|x\|_\infty = 1.4 \times 4 = 5.6
$$

✓ Satisfied

</details>

---

## 📝 **Part II: Conjugate Functions**

### **Exercise 3: Computing Conjugate Functions (Rockafellar, Ex. 12.B)**

The conjugate of a function $$f(x)$$ is defined as:

$$
f^*(y) = \sup_x (y^T x - f(x))
$$

**Tasks:** Compute the conjugate of:

a) $$f(x) = \frac{1}{2}x^T Q x$$ with $$Q \succ 0$$  
b) $$f(x) = \|x\|_2$$  
c) $$f(x) = e^x$$ (with $$x \in \mathbb{R}$$)  
d) $$f(x) = I_C(x)$$ (the indicator function of the set $$C$$)

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Quadratic function $$f(x) = \frac{1}{2}x^T Q x$$:**

$$
f^*(y) = \sup_x \left( y^T x - \frac{1}{2} x^T Q x \right)
$$

**FOC:** $$\nabla_x (y^T x - \frac{1}{2}x^T Q x) = y - Qx = 0$$

$$
x^* = Q^{-1} y
$$

Substituting:

$$
f^*(y) = y^T Q^{-1} y - \frac{1}{2} (Q^{-1}y)^T Q (Q^{-1}y)
$$

$$
= y^T Q^{-1} y - \frac{1}{2} y^T Q^{-1} y = \frac{1}{2} y^T Q^{-1} y
$$

**Result:** $$\boxed{f^*(y) = \frac{1}{2} y^T Q^{-1} y}$$

**Fenchel's inequality:**

$$
\frac{1}{2}x^T Q x + \frac{1}{2}y^T Q^{-1} y \geq x^T y
$$

---

**b) Euclidean norm $$f(x) = \|x\|_2$$:**

$$
f^*(y) = \sup_x (y^T x - \|x\|_2)
$$

**Analysis:**
- If $$\|y\|_2 \leq 1$$: we can take $$x$$ along the direction of $$y$$ with $$\|x\| \to \infty$$, but $$y^Tx - \|x\| \leq 0$$
- If $$\|y\|_2 > 1$$: $$y^T x - \|x\|_2 \to \infty$$ for $$x = ty$$ with $$t \to \infty$$

**Result:**

$$
\boxed{f^*(y) = \begin{cases}
0 & \text{if } \|y\|_2 \leq 1 \\
\infty & \text{if } \|y\|_2 > 1
\end{cases}} = I_{\|y\|_2 \leq 1}(y)
$$

---

**c) Exponential function $$f(x) = e^x$$:**

$$
f^*(y) = \sup_x (yx - e^x)
$$

**FOC:** $$y - e^x = 0 \Rightarrow x^* = \ln y$$

(A solution exists only if $$y > 0$$)

Substituting:

$$
f^*(y) = y \ln y - e^{\ln y} = y \ln y - y
$$

**Result:**

$$
\boxed{f^*(y) = \begin{cases}
y \ln y - y & \text{if } y > 0 \\
0 & \text{if } y = 0 \\
\infty & \text{if } y < 0
\end{cases}}
$$

---

**d) Indicator function $$f(x) = I_C(x)$$:**

$$
f^*(y) = \sup_x (y^T x - I_C(x)) = \sup_{x \in C} y^T x
$$

**Result:** $$\boxed{f^*(y) = \sup_{x \in C} y^T x}$$ (the support function of $$C$$)

**Specific examples:**
- $$C = \{x : \|x\|_2 \leq 1\}$$: $$f^*(y) = \|y\|_2$$
- $$C = \mathbb{R}^n_+$$: $$f^*(y) = I_{\{y \leq 0\}}(y)$$

</details>

---

### **Exercise 4: Fenchel's Inequality (Boyd & Vandenberghe, Ex. 3.33)**

Let $$f(x) = \frac{1}{2}\|x\|^2$$, $$x = (1, 2)^T$$ and $$y = (3, 1)^T$$.

**Tasks:**  
a) Compute $$f(x)$$ and $$f^*(y)$$  
b) Compute $$x^T y$$  
c) Verify Fenchel's inequality: $$f(x) + f^*(y) \geq x^T y$$

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Compute $$f(x)$$ and $$f^*(y)$$:**

$$
f(x) = \frac{1}{2}(1^2 + 2^2) = \frac{1}{2}(1 + 4) = 2.5
$$

For $$f(x) = \frac{1}{2}\|x\|^2$$ we have $$Q = I$$, so:

$$
f^*(y) = \frac{1}{2}\|y\|^2 = \frac{1}{2}(3^2 + 1^2) = \frac{1}{2}(9 + 1) = 5
$$

---

**b) Compute $$x^T y$$:**

$$
x^T y = 1 \times 3 + 2 \times 1 = 5
$$

---

**c) Verify Fenchel:**

$$
f(x) + f^*(y) = 2.5 + 5 = 7.5 \geq 5 = x^T y
$$

✓ Satisfied

**Gap:** $$7.5 - 5 = 2.5$$

**When is there equality?** When $$y \in \partial f(x)$$, i.e. $$y = \nabla f(x) = x$$.

For $$x = (1,2)$$ we have $$\nabla f(x) = (1,2) \neq (3,1) = y$$, so there is no equality.

</details>

---

## 📝 **Part III: LASSO Dual**

### **Exercise 5: Constructing the LASSO Dual (Boyd & Vandenberghe, Ex. 6.15)**

The primal LASSO problem:

$$
\min_x \frac{1}{2}\|Ax - b\|^2 + \lambda \|x\|_1
$$

**Tasks:**
a) Write the dual problem  
b) Explain the relationship between primal and dual variables  
c) With $$A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}$$, $$b = \begin{bmatrix} 1 \\ 1 \\ 3 \end{bmatrix}$$, $$\lambda = 0.5$$, find the dual solution

<details>
<summary><strong>💡 Solution</strong></summary>

**a) The dual problem:**

LASSO primal:

$$
\min_x \frac{1}{2}\|Ax - b\|^2 + \lambda \|x\|_1
$$

**Method 1: via the Lagrangian**

Rewrite with the auxiliary variable $$r = Ax - b$$:

$$
\begin{align}
\min_{x,r} \quad & \frac{1}{2}\|r\|^2 + \lambda \|x\|_1 \\
\text{s.t.} \quad & Ax - r = b
\end{align}
$$

Lagrangian:

$$
L(x, r, \nu) = \frac{1}{2}\|r\|^2 + \lambda \|x\|_1 + \nu^T(Ax - r - b)
$$

Minimize over $$x$$:

$$
\min_x \left( \lambda \|x\|_1 + \nu^T A x \right) = \begin{cases}
0 & \text{if } \|A^T \nu\|_\infty \leq \lambda \\
-\infty & \text{otherwise}
\end{cases}
$$

Minimize over $$r$$:

$$
\min_r \left( \frac{1}{2}\|r\|^2 - \nu^T r \right) = -\frac{1}{2}\|\nu\|^2
$$

**Dual function:**

$$
g(\nu) = -\frac{1}{2}\|\nu\|^2 - \nu^T b
$$

with the constraint $$\|A^T \nu\|_\infty \leq \lambda$$.

**The dual problem:**

$$
\boxed{
\begin{align}
\min_{\nu} \quad & \frac{1}{2}\|\nu\|^2 + \nu^T b \\
\text{s.t.} \quad & \|A^T \nu\|_\infty \leq \lambda
\end{align}
}
$$

(Converting max to min)

---

**b) Primal-dual relationship:**

From the KKT conditions:
- $$r^* = \nu^*$$ (residual dual = dual variable)
- If $$|(A^T \nu^*)_i| < \lambda$$: $$x_i^* = 0$$
- If $$|(A^T \nu^*)_i| = \lambda$$: $$x_i^* \neq 0$$ (in the active set)

**Recovering the primal from the dual:**

$$
x^* = \text{(solution of the problem restricted to the active set)}
$$

---

**c) Numerical solution:**

Data:

$$
A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}, \quad
b = \begin{bmatrix} 1 \\ 1 \\ 3 \end{bmatrix}, \quad
\lambda = 0.5
$$

**The dual problem:**

$$
\begin{align}
\min_{\nu} \quad & \frac{1}{2}(\nu_1^2 + \nu_2^2 + \nu_3^2) + \nu_1 + \nu_2 + 3\nu_3 \\
\text{s.t.} \quad & \max(|\nu_1 + \nu_3|, |\nu_2 + \nu_3|) \leq 0.5
\end{align}
$$

**Solving:**

FOC (if the constraint is inactive):

$$
\nu_1 + 1 = 0 \Rightarrow \nu_1 = -1 \\
\nu_2 + 1 = 0 \Rightarrow \nu_2 = -1 \\
\nu_3 + 3 = 0 \Rightarrow \nu_3 = -3
$$

Check the constraint:

$$
\max(|-1 - 3|, |-1 - 3|) = 4 > 0.5
$$

Not satisfied! The constraint must be active.

**Assume** both constraints are active: $$\nu_1 + \nu_3 = \nu_2 + \nu_3 = -0.5$$ (by symmetry, $$\nu_1 = \nu_2 = a$$ and $$\nu_3 = -0.5 - a$$).

Substitute into the objective: $$\min_a \; \frac{1}{2}\left[2(a+1)^2 + (2.5 - a)^2\right]$$ (since $$\frac{1}{2}\|\nu\|^2 + \nu^Tb = \frac{1}{2}\|\nu + b\|^2 - \frac{1}{2}\|b\|^2$$).

Derivative: $$2(a+1) - (2.5 - a) = 0 \Rightarrow a = \frac{1}{6}$$.

**Dual solution:**

$$
\nu^* = \left(\tfrac{1}{6}, \tfrac{1}{6}, -\tfrac{2}{3}\right)^T, \qquad \tfrac{1}{2}\|\nu^*\|^2 + \nu^{*T}b = \tfrac{1}{4} - \tfrac{5}{3} = -\tfrac{17}{12}
$$

that is, the dual value (of the max problem) is $$\frac{17}{12} \approx 1.4167$$.

**Check against the primal:** $$x^* = \left(\tfrac{7}{6}, \tfrac{7}{6}\right)$$ gives $$Ax^* - b = \left(\tfrac{1}{6}, \tfrac{1}{6}, -\tfrac{2}{3}\right) = \nu^*$$ ✓ (indeed $$r^* = \nu^*$$), and the primal value is $$\frac{1}{2}\|r^*\|^2 + \lambda\|x^*\|_1 = \frac{1}{4} + 0.5 \cdot \frac{7}{3} = \frac{17}{12}$$ ✓. There is no duality gap.

</details>

---

## 📝 **Part IV: Dual Cones**

### **Exercise 6: Computing Dual Cones (Boyd & Vandenberghe, Ex. 2.36)**

The dual cone of $$K$$ is defined as:

$$
K^* = \{ y : y^T x \geq 0, \forall x \in K \}
$$

**Tasks:** Find the dual cone of:

a) $$K = \mathbb{R}^n_+ = \{x : x \geq 0\}$$  
b) $$K = \{(t, x) : \|x\|_2 \leq t\}$$ (second-order cone)  
c) $$K = \mathbb{S}^n_+$$ (positive semidefinite cone)

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Nonnegative orthant $$K = \mathbb{R}^n_+$$:**

We need to find $$y$$ such that $$y^T x \geq 0$$ for all $$x \geq 0$$.

**Analysis:** take $$x = e_i$$ (the $$i$$-th basis vector):

$$
y^T e_i = y_i \geq 0
$$

This must hold for all $$i$$ → $$y \geq 0$$.

**Conclusion:** $$\boxed{K^* = \mathbb{R}^n_+}$$ (self-dual)

---

**b) Second-order cone:**

$$
K = \{(t, x) : t \in \mathbb{R}, x \in \mathbb{R}^{n-1}, \|x\|_2 \leq t\}
$$

We need to find $$(s, y)$$ such that:

$$
st + y^T x \geq 0, \quad \forall \|x\|_2 \leq t
$$

**Worst case:** $$x = -\frac{t}{\|y\|_2} y$$ (if $$y \neq 0$$)

$$
st - t\|y\|_2 = t(s - \|y\|_2) \geq 0
$$

This must hold for all $$t > 0$$ → $$s \geq \|y\|_2$$.

**Conclusion:** $$\boxed{K^* = K}$$ (self-dual)

---

**c) PSD cone $$K = \mathbb{S}^n_+$$:**

We need to find $$Y$$ such that:

$$
\text{tr}(Y X) \geq 0, \quad \forall X \succeq 0
$$

**Eigenvalue analysis:** $$X = \sum_i \lambda_i v_i v_i^T$$ with $$\lambda_i \geq 0$$:

$$
\text{tr}(Y X) = \sum_i \lambda_i v_i^T Y v_i \geq 0
$$

This must hold for all $$\lambda_i \geq 0$$ → $$v_i^T Y v_i \geq 0$$ for all $$v_i$$ → $$Y \succeq 0$$.

**Conclusion:** $$\boxed{K^* = \mathbb{S}^n_+}$$ (self-dual)

</details>

---

### **Exercise 7: Verifying Cone Properties**

Let $$x = (2, 1, 1)^T$$ and $$y = (1.5, 0.5, 0.5)^T$$.

**Tasks:**
a) Is $$x$$ in the SOC?  
b) Is $$y$$ in the SOC?  
c) Compute $$y^T x$$ and verify the dual cone property

<details>
<summary><strong>💡 Solution</strong></summary>

**SOC:** $$K = \{(t, x) \in \mathbb{R} \times \mathbb{R}^2 : \|x\|_2 \leq t\}$$

Write $$x = (t, u)$$ with $$t = 2$$, $$u = (1, 1)$$.

---

**a) Check $$x$$:**

$$
\|(1, 1)\|_2 = \sqrt{2} \approx 1.414 \leq 2
$$

✓ $$x \in K$$

---

**b) Check $$y$$:**

$$
\|(0.5, 0.5)\|_2 = \frac{\sqrt{2}}{2} \approx 0.707 \leq 1.5
$$

✓ $$y \in K$$

---

**c) Dual cone property:**

Since $$K$$ is self-dual: $$y \in K^* = K$$

So for every $$x \in K$$: $$y^T x \geq 0$$.

$$
y^T x = 1.5 \times 2 + 0.5 \times 1 + 0.5 \times 1 = 3 + 0.5 + 0.5 = 4 \geq 0
$$

✓ Satisfied

</details>

---

## 📝 **Part V: SDP Duality**

### **Exercise 8: SDP Primal-Dual (Ben-Tal & Nemirovski, Ex. 4.3)**

The primal SDP problem:

$$
\begin{align}
\min_{X} \quad & \text{tr}(C X) \\
\text{s.t.} \quad & \text{tr}(A_i X) = b_i, \quad i = 1, \ldots, m \\
& X \succeq 0
\end{align}
$$

**Tasks:**  
a) Write the dual problem  
b) Explain strong duality  
c) With $$C = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$, $$A_1 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$$, $$b_1 = 1$$, find the solution

<details>
<summary><strong>💡 Solution</strong></summary>

**a) The dual problem:**

Lagrangian:

$$
L(X, y) = \text{tr}(CX) - \sum_i y_i (\text{tr}(A_i X) - b_i)
$$

$$
= \text{tr}\left( \left(C - \sum_i y_i A_i\right) X \right) + \sum_i y_i b_i
$$

Minimize over $$X \succeq 0$$:

$$
\min_{X \succeq 0} \text{tr}(MX) = \begin{cases}
0 & \text{if } M \succeq 0 \\
-\infty & \text{otherwise}
\end{cases}
$$

with $$M = C - \sum_i y_i A_i$$.

**The dual problem:**

$$
\boxed{
\begin{align}
\max_{y} \quad & \sum_i y_i b_i \\
\text{s.t.} \quad & C - \sum_i y_i A_i \succeq 0
\end{align}
}
$$

---

**b) Strong Duality:**

Slater condition: there exists $$\tilde{X} \succ 0$$ with $$\text{tr}(A_i \tilde{X}) = b_i$$.

Then: **strong duality** $$p^* = d^*$$ holds and a dual optimal solution exists.

**KKT Conditions:**
1. Primal feasible: $$\text{tr}(A_i X^*) = b_i$$, $$X^* \succeq 0$$
2. Dual feasible: $$C - \sum_i y_i^* A_i \succeq 0$$
3. Complementary slackness: $$\text{tr}((C - \sum_i y_i^* A_i) X^*) = 0$$

---

**c) Specific solution:**

Data:

$$
C = I_2, \quad A_1 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \quad b_1 = 1
$$

**Primal:**

$$
\begin{align}
\min_{X} \quad & x_{11} + x_{22} \\
\text{s.t.} \quad & x_{11} = 1 \\
& X \succeq 0
\end{align}
$$

From $$x_{11} = 1$$ and $$X \succeq 0$$:

$$
X = \begin{bmatrix} 1 & x_{12} \\ x_{12} & x_{22} \end{bmatrix} \succeq 0
$$

PSD → $$\det(X) = x_{22} - x_{12}^2 \geq 0$$ → $$x_{22} \geq x_{12}^2 \geq 0$$.

Minimize $$1 + x_{22}$$ → $$x_{22}^* = 0$$, $$x_{12}^* = 0$$.

**Primal solution:**

$$
X^* = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \quad p^* = 1
$$

---

**Dual:**

$$
\begin{align}
\max_{y_1} \quad & y_1 \\
\text{s.t.} \quad & I - y_1 \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \succeq 0
\end{align}
$$

$$
\begin{bmatrix} 1-y_1 & 0 \\ 0 & 1 \end{bmatrix} \succeq 0 \Rightarrow 1-y_1 \geq 0 \Rightarrow y_1 \leq 1
$$

Maximize → $$y_1^* = 1$$, $$d^* = 1$$.

**Conclusion:** $$p^* = d^* = 1$$. Strong duality! ✓

</details>

---

## 💡 **Summary and Strategy**

### **Dual Norms:**
- Remember: $$(\|\cdot\|_p)_* = \|\cdot\|_q$$ with $$1/p + 1/q = 1$$
- $$\ell_1 \leftrightarrow \ell_\infty$$, $$\ell_2$$ is self-dual
- Use: $$y^T x \leq \|y\|_* \|x\|$$

### **Conjugate Functions:**
- Definition: $$f^*(y) = \sup_x (y^Tx - f(x))$$
- Fenchel: $$f(x) + f^*(y) \geq x^Ty$$
- Equality when $$y \in \partial f(x)$$
- $$f^{**} = f$$ if $$f$$ is closed and convex

### **LASSO Dual:**
- Primal: $$\min \frac{1}{2}\|Ax-b\|^2 + \lambda\|x\|_1$$
- Dual: $$\min \frac{1}{2}\|\nu\|^2 + \nu^Tb$$ s.t. $$\|A^T\nu\|_\infty \leq \lambda$$
- The dual is smaller ($$m$$ variables vs $$n$$ variables) if $$m < n$$

### **Dual Cones:**
- Definition: $$K^* = \{y : y^Tx \geq 0, \forall x \in K\}$$
- Self-dual: $$\mathbb{R}^n_+$$, SOC, $$\mathbb{S}^n_+$$
- $$K^{**} = K$$ if $$K$$ is closed and convex

### **SDP Duality:**
- Strong duality if Slater holds
- Complementary slackness: $$\text{tr}(MX) = 0$$ with $$M \succeq 0$$, $$X \succeq 0$$

---

## 📚 **References**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 3, 5, 6.

2. **Rockafellar, R. T.** (1970). *Convex Analysis*. Princeton University Press.

3. **Ben-Tal, A., & Nemirovski, A.** (2001). *Lectures on Modern Convex Optimization*. SIAM.

4. **Borwein, J. M., & Lewis, A. S.** (2006). *Convex Analysis and Nonlinear Optimization* (2nd ed.). Springer.

5. **Hiriart-Urruty, J.-B., & Lemaréchal, C.** (2001). *Fundamentals of Convex Analysis*. Springer.

