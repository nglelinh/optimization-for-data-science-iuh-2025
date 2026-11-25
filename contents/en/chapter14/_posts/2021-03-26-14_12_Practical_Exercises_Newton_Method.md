---
layout: post
title: '14-12 Practical Exercises - Newton''s Method'
chapter: "14"
order: 20
owner: "GitHub Copilot"
lang: en
categories:
  - chapter14
lesson_type: required
redirect_from:
  - /contents/en/chapter14/14_11_Practical_Exercises_Newton_Method/
---

Mastering Newton's method means being able to move effortlessly between algebra and computation: assembling gradients and Hessians cleanly, solving linear systems without unnecessary matrix inversions, checking self-concordance inequalities by hand, and formulating KKT block systems for equality constraints. Use this structured playbook and warm-up derivation before tackling the full exercise set below.

## Key ideas: Exercise-Solving Playbook for Chapter 14

- **Pillar 1 — Matrix Calculus Discipline:** For $$f(x) = \frac{1}{2}x^T Q x + c^T x$$ with symmetric $$Q$$, $$\nabla f(x) = Qx + c$$ and $$\nabla^2 f(x) = Q$$; for log-sum-exp or logistic losses, express $$\nabla^2 f(x) = X^T W X$$ to see positive semidefiniteness immediately.
- **Pillar 2 — Newton Decrement & Stopping Rules:** Always verify $$\lambda(x)^2 = -\nabla f(x)^T \Delta x_{\text{nt}} > 0$$ as a built-in sign check—if you ever get a negative value for a convex function, you dropped a minus sign!
- **Pillar 3 — Verifying Self-Concordance:** For multivariate functions, restrict to a line $$g(t) = f(x + tv)$$ and check $$|g'''(t)| \le 2 g''(t)^{3/2}$$ (or decompose $$f$$ into known self-concordant sums and affine compositions).
- **Pillar 4 — KKT Systems for Equality Constraints:** Write $$\nabla^2 f(x)\,\Delta x + A^T w = -\nabla f(x)$$ and $$A\Delta x = 0$$; eliminate $$\Delta x = -H^{-1}(\nabla f + A^T w)$$ via the Schur complement $$A H^{-1} A^T w = -A H^{-1}\nabla f$$ when $$H$$ is easily invertible.

### Worked example: Computing a Newton Step for 1D Logistic Regression

Consider the regularized logistic loss $$f(w) = \ln(1 + e^{-w}) + \frac{1}{2}w^2$$ at $$w = 0$$.

1. **Compute the sigmoid probability $$p(w) = \frac{1}{1 + e^w}$$ and derivatives:**
   - $$f'(w) = -\frac{e^{-w}}{1 + e^{-w}} + w = -\frac{1}{1 + e^w} + w$$.
   - $$f''(w) = \frac{e^w}{(1 + e^w)^2} + 1 = p(w)(1 - p(w)) + 1$$.
2. **Evaluate at $$w = 0$$ (where $$p(0) = 0.5$$):**
   - $$f'(0) = -0.5 + 0 = -0.5$$.
   - $$f''(0) = (0.5)(0.5) + 1 = 1.25 = \frac{5}{4}$$.
3. **Compute Newton step and Newton decrement:**
   - $$\Delta w_{\text{nt}} = -\frac{-0.5}{1.25} = +0.4$$.
   - $$\lambda(0)^2 = -f'(0)\Delta w_{\text{nt}} = -(-0.5)(0.4) = 0.20 \implies \lambda(0) \approx 0.4472$$.
   - Predicted quadratic drop: $$\frac{1}{2}\lambda(0)^2 = 0.10$$.
4. **Verify actual drop at $$w^{(1)} = 0.4$$:**
   - $$f(0) = \ln 2 \approx 0.6931$$.
   - $$f(0.4) = \ln(1 + e^{-0.4}) + \frac{1}{2}(0.16) \approx 0.5130 + 0.0800 = 0.5930$$.
   - Actual drop: $$0.6931 - 0.5930 = 0.1001$$—matching the quadratic prediction $$0.10$$ to three decimal places!

# Practical Exercises - Newton's Method

The exercises are adapted from Boyd & Vandenberghe (2004), Nocedal & Wright (2006), and Bertsekas (1999).

---

## **Part I: Basic Newton's Method**

### **Exercise 1: Newton Step Computation (Boyd & Vandenberghe, Ex. 9.1)**

Consider the objective function:

$$
f(x) = \frac{1}{2}x^T Q x + c^T x
$$

where $$Q \succ 0$$.

**Task:**
a) Compute the gradient $$\nabla f(x)$$ and the Hessian $$\nabla^2 f(x)$$
b) At $$x = (1, 2)^T$$, compute the Newton step $$\Delta x_{nt}$$
c) Compute the Newton decrement $$\lambda(x) = \sqrt{\nabla f(x)^T (\nabla^2 f(x))^{-1} \nabla f(x)}$$
d) With $$Q = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$, $$c = \begin{bmatrix} -1 \\ -1 \end{bmatrix}$$, compute all of the quantities above

<details markdown="1">
<summary><strong>Solution</strong></summary>

**a) Gradient and Hessian:**

$$
\nabla f(x) = Qx + c
$$

$$
\nabla^2 f(x) = Q
$$

(The Hessian does not depend on $$x$$ because $$f$$ is quadratic)

---

**b) Newton step:**

The Newton step is defined as:

$$
\Delta x_{nt} = -(\nabla^2 f(x))^{-1} \nabla f(x) = -Q^{-1}(Qx + c)
$$

---

**c) Newton decrement:**

$$
\lambda(x) = \sqrt{\nabla f(x)^T (\nabla^2 f(x))^{-1} \nabla f(x)}
$$

$$
= \sqrt{(Qx+c)^T Q^{-1} (Qx+c)}
$$

---

**d) Numerical computation:**

Data:

$$
Q = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}, \quad
c = \begin{bmatrix} -1 \\ -1 \end{bmatrix}, \quad
x = \begin{bmatrix} 1 \\ 2 \end{bmatrix}
$$

**Compute $$Q^{-1}$$:**

$$
\det(Q) = 2 \times 2 - 1 \times 1 = 3
$$

$$
Q^{-1} = \frac{1}{3}\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}
$$

**Gradient at $$x$$:**

$$
\nabla f(x) = Qx + c = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \end{bmatrix} + \begin{bmatrix} -1 \\ -1 \end{bmatrix}
$$

$$
= \begin{bmatrix} 4 \\ 5 \end{bmatrix} + \begin{bmatrix} -1 \\ -1 \end{bmatrix} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}
$$

**Newton step:**

$$
\Delta x_{nt} = -Q^{-1} \nabla f(x) = -\frac{1}{3}\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} 3 \\ 4 \end{bmatrix}
$$

$$
= -\frac{1}{3}\begin{bmatrix} 6-4 \\ -3+8 \end{bmatrix} = -\frac{1}{3}\begin{bmatrix} 2 \\ 5 \end{bmatrix} = \begin{bmatrix} -2/3 \\ -5/3 \end{bmatrix}
$$

**Newton decrement:**

$$
\lambda^2(x) = \nabla f(x)^T Q^{-1} \nabla f(x)
$$

$$
= \begin{bmatrix} 3 & 4 \end{bmatrix} \frac{1}{3}\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} 3 \\ 4 \end{bmatrix}
$$

$$
= \frac{1}{3}\begin{bmatrix} 3 & 4 \end{bmatrix} \begin{bmatrix} 2 \\ 5 \end{bmatrix} = \frac{1}{3}(6 + 20) = \frac{26}{3}
$$

$$
\lambda(x) = \sqrt{\frac{26}{3}} \approx 2.944
$$

**Optimal solution:**

Since $$f$$ is quadratic, Newton's method converges in 1 step:

$$
x^+ = x + \Delta x_{nt} = \begin{bmatrix} 1 \\ 2 \end{bmatrix} + \begin{bmatrix} -2/3 \\ -5/3 \end{bmatrix} = \begin{bmatrix} 1/3 \\ 1/3 \end{bmatrix}
$$

Check: $$\nabla f(x^*) = Q x^* + c = 0$$ → $$x^* = -Q^{-1}c$$:

$$
x^* = -\frac{1}{3}\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} -1 \\ -1 \end{bmatrix} = \frac{1}{3}\begin{bmatrix} -1 \\ -1 \end{bmatrix} = \begin{bmatrix} 1/3 \\ 1/3 \end{bmatrix}
$$

✓ Correct!

</details>

---

### **Exercise 2: Newton's Method for Logistic Regression (Nocedal & Wright, Ex. 8.1)**

Consider the logistic regression problem:

$$
\min_x \sum_{i=1}^m \log(1 + e^{-y_i (a_i^T x)})
$$

with data $$(a_i, y_i)$$ where $$y_i \in \{-1, +1\}$$.

**Task:**
a) Compute the gradient $$\nabla f(x)$$
b) Compute the Hessian $$\nabla^2 f(x)$$
c) Prove that $$\nabla^2 f(x) \succeq 0$$ (the function is convex)
d) With data $$m=3$$, $$n=2$$:
   - $$a_1 = (1, 1)^T$$, $$y_1 = +1$$
   - $$a_2 = (1, -1)^T$$, $$y_2 = +1$$
   - $$a_3 = (-1, 0)^T$$, $$y_3 = -1$$
   
   Compute the Newton step at $$x = (0, 0)^T$$

<details markdown="1">
<summary><strong>Solution</strong></summary>

**a) Gradient:**

Define $$\phi(z) = \log(1 + e^{-z})$$; then:

$$
f(x) = \sum_{i=1}^m \phi(y_i a_i^T x)
$$

$$
\phi'(z) = \frac{-e^{-z}}{1 + e^{-z}} = -\frac{1}{1 + e^z}
$$

$$
\nabla f(x) = \sum_{i=1}^m \phi'(y_i a_i^T x) \cdot y_i a_i = -\sum_{i=1}^m \frac{y_i a_i}{1 + e^{y_i a_i^T x}}
$$

---

**b) Hessian:**

$$
\phi''(z) = \frac{e^z}{(1 + e^z)^2}
$$

$$
\nabla^2 f(x) = \sum_{i=1}^m \phi''(y_i a_i^T x) \cdot y_i^2 a_i a_i^T = \sum_{i=1}^m \frac{a_i a_i^T}{(1 + e^{y_i a_i^T x})^2} \cdot e^{y_i a_i^T x}
$$

Simplifying (since $$y_i^2 = 1$$):

$$
\nabla^2 f(x) = \sum_{i=1}^m w_i a_i a_i^T
$$

where $$w_i = \frac{e^{y_i a_i^T x}}{(1 + e^{y_i a_i^T x})^2} > 0$$.

---

**c) Proof of convexity:**

$$\nabla^2 f(x) = \sum_{i=1}^m w_i a_i a_i^T$$ with $$w_i > 0$$.

For every $$v \in \mathbb{R}^n$$:

$$
v^T (\nabla^2 f(x)) v = \sum_{i=1}^m w_i (a_i^T v)^2 \geq 0
$$

→ $$\nabla^2 f(x) \succeq 0$$ → $$f$$ is convex ✓

---

**d) Numerical computation at $$x = (0,0)$$:**

**Gradient:**

At $$x = 0$$: $$a_i^T x = 0$$ for all $$i$$.

$$
\nabla f(0) = -\sum_{i=1}^3 \frac{y_i a_i}{1 + e^0} = -\frac{1}{2}\sum_{i=1}^3 y_i a_i
$$

$$
= -\frac{1}{2}\left( (+1)\begin{bmatrix} 1 \\ 1 \end{bmatrix} + (+1)\begin{bmatrix} 1 \\ -1 \end{bmatrix} + (-1)\begin{bmatrix} -1 \\ 0 \end{bmatrix} \right)
$$

$$
= -\frac{1}{2}\begin{bmatrix} 1+1+1 \\ 1-1+0 \end{bmatrix} = -\frac{1}{2}\begin{bmatrix} 3 \\ 0 \end{bmatrix} = \begin{bmatrix} -1.5 \\ 0 \end{bmatrix}
$$

**Hessian:**

$$w_i = \frac{e^0}{(1+e^0)^2} = \frac{1}{4}$$ for all $$i$$.

$$
\nabla^2 f(0) = \frac{1}{4}\sum_{i=1}^3 a_i a_i^T
$$

$$
= \frac{1}{4}\left( \begin{bmatrix} 1 \\ 1 \end{bmatrix}\begin{bmatrix} 1 & 1 \end{bmatrix} + \begin{bmatrix} 1 \\ -1 \end{bmatrix}\begin{bmatrix} 1 & -1 \end{bmatrix} + \begin{bmatrix} -1 \\ 0 \end{bmatrix}\begin{bmatrix} -1 & 0 \end{bmatrix} \right)
$$

$$
= \frac{1}{4}\left( \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} + \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} + \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \right) = \frac{1}{4}\begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}
$$

**Newton step:**

$$
\Delta x_{nt} = -(\nabla^2 f(0))^{-1} \nabla f(0)
$$

$$
= -\frac{4}{1}\begin{bmatrix} 1/3 & 0 \\ 0 & 1/2 \end{bmatrix} \begin{bmatrix} -1.5 \\ 0 \end{bmatrix} = 4\begin{bmatrix} 0.5 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \end{bmatrix}
$$

</details>

---

## **Part II: Backtracking Line Search**

### **Exercise 3: Armijo Condition (Boyd & Vandenberghe, Ex. 9.3)**

Consider the function $$f(x) = x^2$$ and the point $$x = 2$$.

**Task:**
a) Compute the gradient $$\nabla f(x)$$ and the Hessian $$\nabla^2 f(x)$$
b) Compute the Newton direction $$\Delta x_{nt}$$
c) With Armijo parameters $$\alpha = 0.3$$, $$\beta = 0.5$$, find a step size $$t$$ satisfying the Armijo condition:

$$
f(x + t \Delta x) \leq f(x) + \alpha t \nabla f(x)^T \Delta x
$$

d) Draw an illustrative graph

<details markdown="1">
<summary><strong>Solution</strong></summary>

**a) Gradient and Hessian:**

$$
\nabla f(x) = 2x, \quad \nabla^2 f(x) = 2
$$

At $$x = 2$$:

$$
\nabla f(2) = 4, \quad \nabla^2 f(2) = 2
$$

---

**b) Newton direction:**

$$
\Delta x_{nt} = -\frac{\nabla f(x)}{\nabla^2 f(x)} = -\frac{4}{2} = -2
$$

---

**c) Backtracking line search:**

Armijo condition:

$$
f(x + t \Delta x) \leq f(x) + \alpha t \nabla f(x)^T \Delta x
$$

Substituting the numbers:

$$
(2 + t(-2))^2 \leq 4 + 0.3 \cdot t \cdot 4 \cdot (-2)
$$

$$
(2 - 2t)^2 \leq 4 - 2.4t
$$

$$
4 - 8t + 4t^2 \leq 4 - 2.4t
$$

$$
4t^2 - 5.6t \leq 0
$$

$$
t(4t - 5.6) \leq 0
$$

Since $$t > 0$$, we need $$4t - 5.6 \leq 0$$ → $$t \leq 1.4$$.

**Backtracking:**

Try $$t = 1$$:

$$
f(2 - 2 \cdot 1) = f(0) = 0
$$

$$
4 + 0.3 \cdot 1 \cdot (-8) = 4 - 2.4 = 1.6
$$

$$0 \leq 1.6$$ ✓ Satisfied!

**Result:** $$t = 1$$ (full Newton step)

---

**d) Geometric interpretation:**

- $$f(x)$$ is the parabola $$y = x^2$$
- At $$x = 2$$, the Newton step $$\Delta x = -2$$ points to the minimum $$x^* = 0$$
- The full step $$t = 1$$ takes us to the optimal solution in a single step
- The Armijo condition guarantees sufficient decrease

**Graph:**

```
f(x) = x²

     4 |     • (2, 4)
       |    /
       |   /
       |  /
     1 |_/__________
       |/      
     0 •------------ x
      0  1   2
         ↑
      Newton step
      takes us to x=0
```

Armijo line: $$y = 4 - 2.4t$$ (the scaled-down tangent line with slope $$\alpha \nabla f \Delta x$$)

</details>

---

## **Part III: Convergence Analysis**

### **Exercise 4: Quadratic Convergence (Nocedal & Wright, Theorem 3.5)**

Consider Newton's method for a strongly convex function $$f$$ with:
- $$m I \preceq \nabla^2 f(x) \preceq M I$$
- $$\nabla^2 f$$ Lipschitz with constant $$L$$

**Task:**
a) Prove that Newton's method converges quadratically near the solution
b) Compute concretely for $$f(x) = \frac{1}{2}x^T Q x$$ with $$Q = \begin{bmatrix} 4 & 0 \\ 0 & 1 \end{bmatrix}$$
c) Compare with gradient descent

<details markdown="1">
<summary><strong>Solution</strong></summary>

**a) Proof of quadratic convergence:**

<div class="textbook-theorem" markdown="1">
**Theorem:** If $$f$$ is strongly convex and $$\nabla^2 f$$ is Lipschitz continuous with constant $$L$$, then there exists $$\delta > 0$$ such that whenever $$\|x^{(k)} - x^*\| < \delta$$:

$$
\|x^{(k+1)} - x^*\| \leq \frac{L}{2m} \|x^{(k)} - x^*\|^2
$$
</div>

**Proof (sketch):**

Newton iteration:

$$
x^{(k+1)} = x^{(k)} - (\nabla^2 f(x^{(k)}))^{-1} \nabla f(x^{(k)})
$$

Taylor expansion at $$x^*$$:

$$
\nabla f(x^{(k)}) = \nabla f(x^*) + \int_0^1 \nabla^2 f(x^* + t(x^{(k)} - x^*)) (x^{(k)} - x^*) dt
$$

Since $$\nabla f(x^*) = 0$$:

$$
\nabla f(x^{(k)}) = \int_0^1 \nabla^2 f(x^* + t(x^{(k)} - x^*)) (x^{(k)} - x^*) dt
$$

Newton step:

$$
x^{(k+1)} - x^* = x^{(k)} - x^* - (\nabla^2 f(x^{(k)}))^{-1} \nabla f(x^{(k)})
$$

Using the Lipschitz property of $$\nabla^2 f$$:

$$
\|\nabla^2 f(x) - \nabla^2 f(y)\| \leq L \|x - y\|
$$

After a careful estimate:

$$
\|x^{(k+1)} - x^*\| \leq \frac{L}{2m} \|x^{(k)} - x^*\|^2
$$

**Meaning:** The error is squared at every iteration! (quadratic convergence)

---

**b) Computation with $$Q = \text{diag}(4, 1)$$:**

$$
f(x) = \frac{1}{2}x^T Q x = 2x_1^2 + \frac{1}{2}x_2^2
$$

**Parameters:**
- $$m = \lambda_{\min}(Q) = 1$$
- $$M = \lambda_{\max}(Q) = 4$$
- $$L = 0$$ (Hessian constant → $$\nabla^2 f(x) = Q$$)

**Convergence:**

With $$L = 0$$, Newton's method converges in **1 step** (because $$f$$ is quadratic)!

From any $$x^{(0)}$$:

$$
x^{(1)} = x^{(0)} - Q^{-1} (Qx^{(0)}) = x^{(0)} - x^{(0)} = 0 = x^*
$$

---

**c) Comparison with Gradient Descent:**

**GD with step size $$t = \frac{2}{m + M} = \frac{2}{5} = 0.4$$:**

$$
x^{(k+1)} = x^{(k)} - 0.4 \nabla f(x^{(k)})
$$

**Convergence rate:**

$$
\|x^{(k+1)} - x^*\| \leq \left(\frac{M - m}{M + m}\right) \|x^{(k)} - x^*\| = \frac{3}{5} \|x^{(k)} - x^*\|
$$

**Linear convergence** with ratio $$0.6$$.

**Comparison:**

| Method | Convergence | Iterations to $$10^{-6}$$ |
|--------|-------------|---------------------------|
| Newton | Quadratic | 1 (quadratic function) |
| GD | Linear ($$0.6^k$$) | $$k = 28$$ ($$0.6^{27} \approx 1.03 \times 10^{-6}$$) |

Newton is **much faster**!

</details>

---

## **Part IV: Affine Invariance**

### **Exercise 5: Affine Invariance Property (Boyd & Vandenberghe, Ex. 9.20)**

Affine invariance of Newton's method: if $$f$$ is transformed by an affine change of variables, Newton's method is unaffected.

**Task:**
a) Prove: if $$\tilde{x} = Ax + b$$ with $$A$$ invertible, and $$\tilde{f}(\tilde{x}) = f(A^{-1}(\tilde{x} - b))$$, then the Newton step is unchanged
b) Illustrate with a concrete example

<details markdown="1">
<summary><strong>Solution</strong></summary>

**a) Proof of affine invariance:**

**Problem transformation:**

Original: $$\min_x f(x)$$
New: $$\min_{\tilde{x}} \tilde{f}(\tilde{x})$$ with $$\tilde{x} = Ax + b$$.

**Gradient of $$\tilde{f}$$:**

By the chain rule:

$$
\nabla \tilde{f}(\tilde{x}) = A^{-T} \nabla f(x)
$$

(with $$x = A^{-1}(\tilde{x} - b)$$)

**Hessian of $$\tilde{f}$$:**

$$
\nabla^2 \tilde{f}(\tilde{x}) = A^{-T} \nabla^2 f(x) A^{-1}
$$

**Newton step in the new coordinates:**

$$
\Delta \tilde{x}_{nt} = -(\nabla^2 \tilde{f}(\tilde{x}))^{-1} \nabla \tilde{f}(\tilde{x})
$$

$$
= -(A \nabla^2 f(x)^{-1} A^T)(A^{-T} \nabla f(x))
$$

$$
= -A \nabla^2 f(x)^{-1} \nabla f(x) = A \Delta x_{nt}
$$

**Relationship:**

$$
\Delta \tilde{x}_{nt} = A \Delta x_{nt}
$$

In the original coordinates:

$$
x^{(k+1)} = x^{(k)} + \Delta x_{nt}
$$

In the new coordinates:

$$
\tilde{x}^{(k+1)} = \tilde{x}^{(k)} + \Delta \tilde{x}_{nt} = A x^{(k)} + b + A \Delta x_{nt} = A x^{(k+1)} + b
$$

**Conclusion:** The Newton trajectory is **unchanged** under affine transformations!

---

**b) Illustrative example:**

$$
f(x) = x_1^2 + 4x_2^2
$$

**Transformation:** $$\tilde{x} = Ax$$ with $$A = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}$$

$$
\tilde{f}(\tilde{x}) = \tilde{x}_1^2 + \tilde{x}_2^2
$$

(It turns the ellipse into a circle!)

**From $$x^{(0)} = (2, 1)^T$$:**

**Original coordinates:**
- $$\nabla f = (4, 8)^T$$
- $$\nabla^2 f = \text{diag}(2, 8)$$
- $$\Delta x = -(2, 1)^T$$
- $$x^{(1)} = (0, 0)^T$$ ✓

**New coordinates:** $$\tilde{x}^{(0)} = (2, 2)^T$$
- $$\nabla \tilde{f} = (4, 4)^T$$
- $$\nabla^2 \tilde{f} = 2I$$
- $$\Delta \tilde{x} = -(2, 2)^T$$
- $$\tilde{x}^{(1)} = (0, 0)^T$$ ✓

**Same result!** The number of iterations does not change.

</details>

---

## **Part V: Real-World Problem**

### **Exercise 6: Optimal Control (Bertsekas, Ex. 2.3.5)**

Discrete-time optimal control problem:

$$
\min_{u_0,\ldots,u_{N-1}} \sum_{k=0}^{N-1} \left( x_k^T Q x_k + u_k^T R u_k \right) + x_N^T Q_f x_N
$$

with dynamics:

$$
x_{k+1} = A x_k + B u_k, \quad x_0 = \bar{x}
$$

**Task:**
a) Write the problem as an unconstrained QP
b) Compute the gradient and Hessian
c) Apply Newton's method with $$N = 3$$, $$Q = I$$, $$R = I$$, $$Q_f = I$$, $$A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$$, $$B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$, $$\bar{x} = (1, 0)^T$$

<details markdown="1">
<summary><strong>Solution</strong></summary>

**a) Formulation:**

**Decision variable:** $$z = (u_0, u_1, u_2)^T \in \mathbb{R}^{3}$$ (since $$u_k \in \mathbb{R}$$)

**Express $$x_k$$ in terms of $$u$$:**

$$
\begin{align}
x_1 &= Ax_0 + Bu_0 \\
x_2 &= Ax_1 + Bu_1 = A^2 x_0 + AB u_0 + B u_1 \\
x_3 &= A^3 x_0 + A^2 B u_0 + AB u_1 + B u_2
\end{align}
$$

**Compact form:** $$x_k = \Phi_k x_0 + \sum_{j=0}^{k-1} \Psi_{kj} u_j$$

**Objective function:**

$$
f(u) = \sum_{k=0}^{N-1} (x_k^T Q x_k + u_k^T R u_k) + x_N^T Q_f x_N
$$

$$
= \frac{1}{2} u^T H u + g^T u + \text{const}
$$

where $$H$$ and $$g$$ are computed from the dynamics.

---

**b) Gradient and Hessian:**

Since $$f$$ is a QP:

$$
\nabla f(u) = Hu + g
$$

$$
\nabla^2 f(u) = H
$$

**Newton step:**

$$
\Delta u = -H^{-1}(Hu + g) = -u - H^{-1}g
$$

(Converges in 1 step!)

---

**c) Numerical computation with $$N=3$$:**

Data:

$$
A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}, \quad
B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}, \quad
x_0 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}
$$

**Compute the dynamics:**

$$
x_1 = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} + \begin{bmatrix} 0 \\ 1 \end{bmatrix} u_0 = \begin{bmatrix} 1 \\ u_0 \end{bmatrix}
$$

$$
x_2 = A x_1 + B u_1 = \begin{bmatrix} 1 + u_0 \\ u_0 + u_1 \end{bmatrix}
$$

$$
x_3 = A x_2 + B u_2 = \begin{bmatrix} 1 + 2u_0 + u_1 \\ u_0 + u_1 + u_2 \end{bmatrix}
$$

**Objective function ($$Q = R = Q_f = I$$):**

$$
f = \sum_{k=0}^2 (\|x_k\|^2 + u_k^2) + \|x_3\|^2
$$

$$
= (1^2 + u_0^2) + ((1)^2 + (u_0)^2 + u_1^2) + \ldots
$$

Expanding and differentiating: $$\nabla f(0) = (6, 2, 0)^T$$, $$\nabla^2 f = \begin{bmatrix} 18 & 8 & 2 \\ 8 & 8 & 2 \\ 2 & 2 & 4 \end{bmatrix}$$. Newton step from $$u = 0$$: $$\Delta u = -(\nabla^2 f)^{-1}\nabla f(0)$$.

**Result:**

Optimal control: $$u^* = (-2/5,\ 4/35,\ 1/7)^T \approx (-0.4,\ 0.114,\ 0.143)^T$$, $$f^* = 102/35 \approx 2.914$$

Newton's method converges in 1 iteration because the problem is a QP.

</details>

---

## **Summary and Strategy**

### **Newton Method:**
- **Newton step:** $$\Delta x = -(\nabla^2 f(x))^{-1} \nabla f(x)$$
- **Newton decrement:** $$\lambda(x) = \sqrt{\nabla f(x)^T (\nabla^2 f(x))^{-1} \nabla f(x)}$$
- **Stopping criterion:** $$\lambda^2(x)/2 < \epsilon$$

### **Backtracking Line Search:**
- **Armijo condition:** $$f(x + t\Delta x) \leq f(x) + \alpha t \nabla f(x)^T \Delta x$$
- **Parameters:** $$\alpha \in (0, 0.5)$$, $$\beta \in (0, 1)$$
- **Typical:** $$\alpha = 0.3$$, $$\beta = 0.8$$

### **Convergence:**
- **Quadratic convergence:** $$\|x^{(k+1)} - x^*\| \leq C \|x^{(k)} - x^*\|^2$$
- **Near optimal:** Close to $$x^*$$, Newton's method is very fast
- **Quadratic function:** Converges in 1 step

### **Affine Invariance:**
- Newton's method does not depend on the choice of coordinates
- The number of iterations is unchanged under affine transformations
- **Benefit:** No preconditioning needed

### **When to use Newton:**
- Smooth functions ($$\nabla^2 f$$ exists)
- Near the solution (fast convergence)
- Moderate dimension (the Hessian is $$n \times n$$)
- High accuracy is required

---

## **References**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 9.

2. **Nocedal, J., & Wright, S. J.** (2006). *Numerical Optimization* (2nd ed.). Springer. Chapters 3, 6.

3. **Bertsekas, D. P.** (1999). *Nonlinear Programming* (2nd ed.). Athena Scientific. Chapter 1.

4. **Nesterov, Y.** (2004). *Introductory Lectures on Convex Optimization*. Springer. Chapter 2.

5. **Dennis, J. E., & Schnabel, R. B.** (1996). *Numerical Methods for Unconstrained Optimization and Nonlinear Equations*. SIAM.

