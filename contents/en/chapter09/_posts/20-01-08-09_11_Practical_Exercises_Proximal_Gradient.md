---
layout: post
title: '09-11 Practical Exercises - Proximal Gradient'
chapter: '09'
order: 13
owner: GitHub Copilot
lang: en
categories:
- chapter09
lesson_type: required
---

Derivations on paper make proximal operators look effortless, but true fluency comes from computing them by hand across diverse geometries: $$\ell_1$$ shrinkage on vectors, singular-value thresholding on matrices, FISTA momentum updates, and dual proximal mappings via Moreau's decomposition. The five practical exercises below are modeled on Parikh & Boyd (2014) and Beck & Teboulle (2009) to build genuine muscle memory across every corner of Chapter 09.

## Key ideas: Essential Identities for Solving Proximal Exercises

- **Pillar 1 — First-Order Optimality of the Prox Map:** $$z = \operatorname{prox}_{t h}(y) \iff \frac{1}{t}(y - z) \in \partial h(z)$$. This single subdifferential inclusion lets you derive any closed-form proximal operator in three lines without guessing.
- **Pillar 2 — Moreau's Identity (Primal–Dual Proximal Bridge):** For any closed proper convex $$h$$ and its Fenchel conjugate $$h^\star$$, $$y = \operatorname{prox}_{t h}(y) + t \operatorname{prox}_{h^\star / t}(y / t)$$. Whenever $$h$$ is a norm $$\|\cdot\|$$, $$h^\star$$ is the indicator of the dual-norm unit ball, turning any norm prox into a simple projection!
- **Pillar 3 — Spectral / Orthogonally Invariant Prox:** If $$h(X) = \phi(\sigma(X))$$ depends only on the singular values of matrix $$X = U \operatorname{diag}(\sigma) V^\top$$, then $$\operatorname{prox}_{t h}(X) = U \operatorname{diag}(\operatorname{prox}_{t \phi}(\sigma)) V^\top$$—immediately yielding SVT for the nuclear norm.
- **Pillar 4 — Dual Proximal Gradient:** When the primal objective is strongly convex with linear constraints, the Lagrange dual becomes smooth with Lipschitz gradient, allowing proximal gradient (or FISTA) to solve the dual directly.

### Worked example: Deriving Soft-Thresholding via Moreau's Identity

Let $$h(x) = \lambda \|x\|_1$$ on $$\mathbb{R}^n$$ with $$t = 1$$, and compute $$\operatorname{prox}_{\lambda \|\cdot\|_1}(y)$$ using Moreau's identity instead of case-by-case differentiation.

1. **Identify the Fenchel conjugate $$h^\star(u)$$:**
   For $$h(x) = \lambda \|x\|_1$$, the dual norm of $$\|\cdot\|_1$$ is $$\|\cdot\|_\infty$$, so $$h^\star(u) = I_{\{ \|u\|_\infty \le \lambda \}}(u)$$ ($$0$$ if $$\|u\|_\infty \le \lambda$$, and $$+\infty$$ otherwise).
2. **Compute $$\operatorname{prox}_{h^\star}(y)$$:**
   Since $$h^\star$$ is an indicator of the box $$[-\lambda, \lambda]^n$$, its proximal operator is simply coordinatewise clipping onto $$[-\lambda, \lambda]$$:
   $$[\operatorname{prox}_{h^\star}(y)]_j = \operatorname{clip}(y_j, -\lambda, \lambda) = \min(\lambda,\; \max(-\lambda, y_j)).$$
3. **Apply Moreau's identity $$\operatorname{prox}_h(y) = y - \operatorname{prox}_{h^\star}(y)$$:**
   $$[\operatorname{prox}_{\lambda \|\cdot\|_1}(y)]_j = y_j - \operatorname{clip}(y_j, -\lambda, \lambda) = \begin{cases} y_j - \lambda & y_j > \lambda, \\ 0 & |y_j| \le \lambda, \\ y_j + \lambda & y_j < -\lambda. \end{cases}$$
4. **Numerical check with $$y = (2, -1, 0.5)^\top$$ and $$\lambda = 1$$:**
   $$\operatorname{clip}(y, -1, 1) = (1, -1, 0.5)^\top \implies \operatorname{prox}_h(y) = (2, -1, 0.5)^\top - (1, -1, 0.5)^\top = (1, 0, 0)^\top.$$
   Notice how Moreau's identity gives you an instant visual picture of soft-thresholding: it is literally the residual left over after clipping $$y$$ to the box $$[-\lambda, \lambda]^n$$!

# Practical Exercises - Proximal Gradient

The exercises are adapted from Parikh & Boyd (2014) and Beck & Teboulle (2009).

---

## 📝 **Exercise 1: LASSO with Soft-Thresholding**

Given the LASSO: $$\min \frac{1}{2}\|Ax - b\|^2 + \lambda\|x\|_1$$ with $$A = I$$, $$b = (2, -1, 0.5)^T$$, $$\lambda = 1$$.

**a)** Write the proximal operator  
**b)** Compute the soft-thresholding  
**c)** Iterate from $$x^{(0)} = 0$$

<details>
<summary><strong>💡 Solution</strong></summary>

**Proximal operator:**

$$\text{prox}_{t\lambda\|\cdot\|_1}(y) = S_{t\lambda}(y)$$

**Soft-thresholding:**

$$S_\lambda(y_i) = \begin{cases}
y_i - \lambda & \text{if } y_i > \lambda \\
0 & \text{if } |y_i| \leq \lambda \\
y_i + \lambda & \text{if } y_i < -\lambda
\end{cases}$$

**With $$A = I$$ (and $$t = 1$$):**

$$x^{(1)} = S_1(b) = (1, 0, 0)^T$$

Converged in 1 step!

</details>

---

## 📝 **Exercise 2: Matrix Completion**

Minimize $$\|X\|_*$$ s.t. $$X_{ij} = M_{ij}$$ for the observed entries.

**a)** Write proximal gradient with $$f(X) = \frac{1}{2}\|P_\Omega(X - M)\|_F^2$$  
**b)** Compute the proximal operator of the nuclear norm  
**c)** Apply SVD soft-thresholding

<details>
<summary><strong>💡 Solution</strong></summary>

**Proximal operator of the nuclear norm:**

$$\text{prox}_{t\|\cdot\|_*}(Y) = U S_t(\Sigma) V^T$$

where $$Y = U\Sigma V^T$$ (SVD), $$S_t(\sigma_i) = \max(\sigma_i - t, 0)$$.

**Update:**

$$X^{(k+1)} = \text{prox}_{t\|\cdot\|_*}(X^{(k)} - t\nabla f(X^{(k)}))$$

$$\nabla f(X) = P_\Omega(X - M)$$

</details>

---

## 📝 **Exercise 3: Accelerated Proximal Gradient (FISTA)**

Given $$f(x) + g(x)$$ with $$f$$ smooth and $$g$$ non-smooth.

**a)** Write the FISTA update  
**b)** Compare the convergence rate with proximal GD  
**c)** Apply it to LASSO

<details>
<summary><strong>💡 Solution</strong></summary>

**FISTA:**

$$
\begin{align}
y^{(k)} &= x^{(k)} + \frac{k-1}{k+2}(x^{(k)} - x^{(k-1)}) \\
x^{(k+1)} &= \text{prox}_{tg}(y^{(k)} - t\nabla f(y^{(k)}))
\end{align}
$$

**Convergence:**
- Proximal GD: $$O(1/k)$$
- FISTA: $$O(1/k^2)$$

**A $$k^2$$ speedup!**

</details>

---

## 📝 **Exercise 4: Proximal Operators**

Compute the proximal operator of:

**a)** $$g(x) = \|x\|_2$$  
**b)** $$g(x) = I_C(x)$$ (indicator of a convex set $$C$$)  
**c)** $$g(x) = \frac{1}{2}x^TQx$$

<details>
<summary><strong>💡 Solution</strong></summary>

**a) $$\ell_2$$ norm:**

$$\text{prox}_{t\|\cdot\|_2}(y) = \begin{cases}
\left(1 - \frac{t}{\|y\|}\right)y & \text{if } \|y\| > t \\
0 & \text{otherwise}
\end{cases}$$

**b) Indicator function:**

$$\text{prox}_{tI_C}(y) = \Pi_C(y)$$ (projection onto $$C$$)

**c) Quadratic:**

$$\text{prox}_{tg}(y) = (I + tQ)^{-1}y$$

</details>

---

## 📝 **Exercise 5: Dual Proximal Gradient**

Given $$\min c^Tx$$ s.t. $$Ax = b, x \geq 0$$.

**a)** Write the dual problem  
**b)** Apply proximal gradient to the dual  
**c)** Recover the primal solution

<details>
<summary><strong>💡 Solution</strong></summary>

**Dual:**

$$\max_\nu \quad g(\nu) = b^T\nu$$

s.t. $$A^T\nu \leq c$$

**Proximal gradient on the dual (projected gradient ascent):**

$$\nu^{(k+1)} = \Pi_{\{A^T\nu \leq c\}}(\nu^{(k)} + t b)$$

**Recover the primal:**

$$x^{(k)} = \arg\min_x L(x, \nu^{(k)})$$

</details>

---

## 💡 **Summary**

| Method | Convergence | Key Feature |
|--------|-------------|-------------|
| Proximal GD | $$O(1/k)$$ | Handles non-smooth $$g$$ |
| FISTA | $$O(1/k^2)$$ | Accelerated |
| Dual Proximal | $$O(1/k)$$ | Constraints via the dual |

### **Proximal Operators:**

| Function | Proximal Operator |
|----------|-------------------|
| $$\|\cdot\|_1$$ | Soft-thresholding |
| $$\|\cdot\|_2$$ | Block soft-thresholding |
| $$\|\cdot\|_*$$ | SVD soft-thresholding |
| $$I_C$$ | Projection $$\Pi_C$$ |
| Quadratic | Matrix inversion |

---

## 📚 **References**

1. Parikh, N., & Boyd, S. (2014). "Proximal Algorithms". Foundations and Trends.
2. Beck, A., & Teboulle, M. (2009). "A Fast Iterative Shrinkage-Thresholding Algorithm" (FISTA).
3. Combettes, P. L., & Pesquet, J.-C. (2011). "Proximal Splitting Methods".
