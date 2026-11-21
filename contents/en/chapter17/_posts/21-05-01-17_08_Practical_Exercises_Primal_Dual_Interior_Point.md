---
layout: post
title: '17-7 Practical Exercises - Primal-Dual Interior Point'
chapter: '17'
order: 8
owner: GitHub Copilot
lang: en
categories:
- chapter17
lesson_type: required
---

# Practical Exercises - Primal-Dual Interior Point Methods

The exercises are adapted from Wright (1997) and Nesterov & Nemirovskii (1994).

---

## 📝 **Exercise 1: Primal-Dual Central Path for an LP**

Consider the LP:

$$
\begin{align}
\min \quad & x_1 + 2x_2 \\
\text{s.t.} \quad & x_1 + x_2 = 3 \\
& x_1, x_2 \geq 0
\end{align}
$$

**Tasks:**  
a) Write the KKT conditions  
b) Derive the perturbed KKT conditions with parameter $$\mu$$  
c) Compute the central path $$x(\mu)$$ for $$\mu = 1, 0.1, 0.01$$

<details>
<summary><strong>💡 Solution</strong></summary>

**a) KKT conditions:**

$$
\begin{align}
\nabla f + A^T\nu - \lambda &= 0 \quad \text{(stationarity)} \\
Ax &= b \quad \text{(primal feasibility)} \\
x &\geq 0, \, \lambda \geq 0 \quad \text{(dual feasibility)} \\
\lambda_i x_i &= 0 \quad \text{(complementarity)}
\end{align}
$$

With the data:

$$
\begin{align}
\begin{bmatrix} 1 \\ 2 \end{bmatrix} + \nu \begin{bmatrix} 1 \\ 1 \end{bmatrix} - \begin{bmatrix} \lambda_1 \\ \lambda_2 \end{bmatrix} &= 0 \\
x_1 + x_2 &= 3 \\
\lambda_1 x_1 = \lambda_2 x_2 &= 0
\end{align}
$$

---

**b) Perturbed KKT (central path conditions):**

Replace complementarity $$\lambda_i x_i = 0$$ with:

$$\lambda_i x_i = \mu \quad \forall i$$

$$
\begin{cases}
1 + \nu - \lambda_1 = 0 \\
2 + \nu - \lambda_2 = 0 \\
x_1 + x_2 = 3 \\
\lambda_1 x_1 = \mu \\
\lambda_2 x_2 = \mu
\end{cases}
$$

---

**c) Solve for central path:**

From (1): $$\lambda_1 = 1 + \nu$$  
From (2): $$\lambda_2 = 2 + \nu$$  
From (4): $$x_1 = \frac{\mu}{1 + \nu}$$  
From (5): $$x_2 = \frac{\mu}{2 + \nu}$$  

Substitute into (3):

$$\frac{\mu}{1+\nu} + \frac{\mu}{2+\nu} = 3$$

$$\mu\left(\frac{1}{1+\nu} + \frac{1}{2+\nu}\right) = 3$$

$$\mu \cdot \frac{(2+\nu) + (1+\nu)}{(1+\nu)(2+\nu)} = 3$$

$$\mu \cdot \frac{3 + 2\nu}{(1+\nu)(2+\nu)} = 3$$

$$(1+\nu)(2+\nu) = \mu(1 + \frac{2\nu}{3})$$

Solve quadratic: $$\nu^2 + 3\nu + 2 = \mu + \frac{2\mu\nu}{3}$$

**For $$\mu = 1$$:**

$$\nu^2 + 3\nu + 2 = 1 + \frac{2\nu}{3}$$

$$\nu^2 + \frac{7\nu}{3} + 1 = 0$$

$$\nu = \frac{-7/3 \pm \sqrt{49/9 - 4}}{2} \in \{-0.566, -1.768\}$$

Only the root with $$\nu > -1$$ gives $$\lambda_1, \lambda_2 > 0$$, so we take $$\nu \approx -0.566$$, and $$x_1 = \frac{1}{1-0.566} \approx 2.30$$, $$x_2 = \frac{1}{2-0.566} \approx 0.70$$ (check: $$x_1 + x_2 = 3$$ ✓).

**For $$\mu = 0.1$$:** $$\nu \approx -0.9656$$, $$x \approx (2.90, 0.097)$$.

**For $$\mu = 0.01$$:** $$\nu \approx -0.9967$$, $$x \approx (2.99, 0.010)$$.

**As $$\mu \to 0$$:** $$x^* \to (3, 0)$$ (the primal optimal solution), $$\nu^* \to -1$$

</details>

---

## 📝 **Exercise 2: Newton Step for the Primal-Dual System**

Consider the LP from Exercise 1. At $$(x, \lambda, \nu)^{(k)}$$, solve the Newton system:

$$
\begin{bmatrix}
0 & A^T & -I \\
A & 0 & 0 \\
\Lambda & 0 & X
\end{bmatrix}
\begin{bmatrix}
\Delta x \\
\Delta \nu \\
\Delta \lambda
\end{bmatrix}
=
-\begin{bmatrix}
r_d \\
r_p \\
r_c
\end{bmatrix}
$$

where $$\Lambda = \text{diag}(\lambda)$$, $$X = \text{diag}(x)$$.

**Tasks:**  
a) Write the residuals $$r_d, r_p, r_c$$  
b) Simplify the system by eliminating $$\Delta\lambda$$  
c) Compute $$\Delta x$$ for $$x = (1, 1)$$, $$\lambda = (2, 3)$$, $$\nu = -1$$, $$\mu = 0.5$$

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Residuals:**

$$
\begin{align}
r_d &= \nabla f + A^T\nu - \lambda = \begin{bmatrix} 1 \\ 2 \end{bmatrix} + \nu \begin{bmatrix} 1 \\ 1 \end{bmatrix} - \begin{bmatrix} \lambda_1 \\ \lambda_2 \end{bmatrix} \\
r_p &= Ax - b = x_1 + x_2 - 3 \\
r_c &= \Lambda X e - \mu e = \begin{bmatrix} \lambda_1 x_1 - \mu \\ \lambda_2 x_2 - \mu \end{bmatrix}
\end{align}
$$

---

**b) Eliminate $$\Delta\lambda$$:**

From row 3: $$\Lambda \Delta x + X \Delta\lambda = -r_c$$

$$\Delta\lambda = -X^{-1}(\Lambda \Delta x + r_c)$$

Substitute into row 1:

$$A^T \Delta\nu - \Delta\lambda = -r_d$$

$$A^T \Delta\nu + X^{-1}(\Lambda \Delta x + r_c) = -r_d$$

$$\Lambda X^{-1} \Delta x + A^T \Delta\nu = -r_d - X^{-1}r_c$$

Combined with row 2:

$$
\begin{bmatrix}
\Lambda X^{-1} & A^T \\
A & 0
\end{bmatrix}
\begin{bmatrix}
\Delta x \\
\Delta \nu
\end{bmatrix}
=
\begin{bmatrix}
-r_d - X^{-1}r_c \\
-r_p
\end{bmatrix}
$$

---

**c) Numerical computation:**

$$x = (1, 1)$$, $$\lambda = (2, 3)$$, $$\nu = -1$$, $$\mu = 0.5$$

$$r_d = \begin{bmatrix} 1-1-2 \\ 2-1-3 \end{bmatrix} = \begin{bmatrix} -2 \\ -2 \end{bmatrix}$$

$$r_p = 1 + 1 - 3 = -1$$

$$r_c = \begin{bmatrix} 2 \cdot 1 - 0.5 \\ 3 \cdot 1 - 0.5 \end{bmatrix} = \begin{bmatrix} 1.5 \\ 2.5 \end{bmatrix}$$

$$\Lambda X^{-1} = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$$

$$-r_d - X^{-1}r_c = \begin{bmatrix} 2 \\ 2 \end{bmatrix} - \begin{bmatrix} 1.5 \\ 2.5 \end{bmatrix} = \begin{bmatrix} 0.5 \\ -0.5 \end{bmatrix}$$

System:

$$
\begin{bmatrix}
2 & 0 & 1 \\
0 & 3 & 1 \\
1 & 1 & 0
\end{bmatrix}
\begin{bmatrix}
\Delta x_1 \\
\Delta x_2 \\
\Delta \nu
\end{bmatrix}
=
\begin{bmatrix}
0.5 \\
-0.5 \\
1
\end{bmatrix}
$$

Solving the system: $$\Delta x = (0.8, 0.2)$$, $$\Delta\nu = -1.1$$ (check: $$2(0.8) - 1.1 = 0.5$$, $$3(0.2) - 1.1 = -0.5$$, $$0.8 + 0.2 = 1$$ ✓)

</details>

---

## 📝 **Exercise 3: Mehrotra Predictor-Corrector**

Mehrotra's algorithm combines predictor and corrector steps:

**Predictor:** $$\mu = 0$$ (affine scaling)  
**Corrector:** $$\mu = \sigma \cdot \frac{x^T\lambda}{n}$$ with $$\sigma \in (0, 1)$$

**Tasks:**  
a) Explain the intuition behind the 2 steps  
b) Compute $$\sigma$$ from the predictor step  
c) Apply to the LP from Exercise 1

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Intuition:**

**Predictor (affine):** Aim toward optimal set ($$\mu = 0$$), aggressive move.

**Corrector (centering):** Pull back toward central path, ensure feasibility and good convergence.

**Adaptive $$\sigma$$:** Based on predictor quality:
- Good predictor → small $$\sigma$$ (more aggressive)
- Bad predictor → large $$\sigma$$ (more conservative)

---

**b) Computing $$\sigma$$:**

After affine step $$(\tilde{x}, \tilde{\lambda})$$:

$$\tilde{\mu} = \frac{\tilde{x}^T\tilde{\lambda}}{n}$$

$$\sigma = \left(\frac{\tilde{\mu}}{\mu}\right)^3$$

(cubic heuristic for fast convergence)

---

**c) Example:**

Current: $$x = (2, 1)$$, $$\lambda = (1, 2)$$, $$\mu = \frac{2 \cdot 1 + 1 \cdot 2}{2} = 2$$

**Predictor ($$\mu_{\text{aff}} = 0$$):**

$$\tilde{x} = (2.5, 0.5)$$, $$\tilde{\lambda} = (0.5, 1.5)$$

$$\tilde{\mu} = \frac{2.5 \cdot 0.5 + 0.5 \cdot 1.5}{2} = \frac{2}{2} = 1$$

$$\sigma = \left(\frac{1}{2}\right)^3 = 0.125$$

**Corrector:** Target $$\mu_{\text{new}} = 0.125 \cdot 2 = 0.25$$

Small $$\sigma$$ → aggressive reduction!

</details>

---

## 📝 **Exercise 4: Infeasible Start**

Consider an infeasible start $$(x^{(0)}, \lambda^{(0)}, \nu^{(0)})$$ that does not satisfy $$Ax = b$$.

**Tasks:**  
a) Modify the residuals to handle infeasibility  
b) Show convergence to primal-dual feasibility  
c) Apply to the LP with $$x^{(0)} = (1, 1)$$ (infeasible for $$x_1 + x_2 = 3$$)

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Modified residuals:**

Allow primal infeasibility $$r_p = Ax - b \neq 0$$ initially.

Newton system remains:

$$
\begin{bmatrix}
0 & A^T & -I \\
A & 0 & 0 \\
\Lambda & 0 & X
\end{bmatrix}
\begin{bmatrix}
\Delta x \\
\Delta \nu \\
\Delta \lambda
\end{bmatrix}
=
-\begin{bmatrix}
r_d \\
r_p \\
r_c
\end{bmatrix}
$$

As iterations progress, $$\|r_p\| \to 0$$.

---

**b) Convergence:**

Each Newton step reduces $$\|(r_d, r_p, r_c)\|$$ quadratically near solution.

**Infeasible primal-dual:** Both $$x$$ and $$(\lambda, \nu)$$ converge simultaneously.

---

**c) Example:**

$$x^{(0)} = (1, 1)$$, $$r_p = 1 + 1 - 3 = -1$$

After one full Newton step ($$\alpha = 1$$), for example $$x^{(1)} = (1.5, 1.5)$$, we get $$r_p = 0$$ (feasible!), because $$A\Delta x = -r_p$$. (With a damped step $$\alpha < 1$$, $$r_p$$ is only reduced by a factor $$1-\alpha$$.)

Then continue as standard primal-dual IPM.

</details>

---

## 📝 **Exercise 5: Self-Concordance and Polynomial Complexity**

Interior point methods have polynomial complexity thanks to self-concordant barriers.

**Tasks:**  
a) Define self-concordance  
b) Show $$\phi(x) = -\sum \log x_i$$ is self-concordant  
c) Explain why this gives $$O(\sqrt{n} \log(1/\epsilon))$$ iterations

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Self-concordance:**

$$\phi$$ is self-concordant if:

$$|\phi'''(x)[h, h, h]| \leq 2(\phi''(x)[h, h])^{3/2} \quad \forall h$$

**Meaning:** the third derivative is controlled by the second derivative.

---

**b) Log barrier:**

$$\phi(x) = -\sum_{i=1}^n \log x_i$$

$$\phi'(x) = -\sum \frac{1}{x_i} e_i$$

$$\phi''(x) = \sum \frac{1}{x_i^2} e_i e_i^T = \text{diag}(1/x_1^2, \ldots, 1/x_n^2)$$

$$\phi'''(x)[h, h, h] = -\sum \frac{2}{x_i^3} h_i^3$$

Check:

$$|\phi'''[h,h,h]| = 2\sum \frac{|h_i|^3}{x_i^3} \leq 2\left(\sum \frac{h_i^2}{x_i^2}\right)^{3/2}$$

$$= 2(\phi''[h,h])^{3/2}$$ ✓

---

**c) Polynomial complexity:**

Self-concordance → Newton step has predictable damping.

**Key idea:** the barrier parameter of $$\phi(x) = -\sum_{i=1}^n \log x_i$$ on the orthant $$\mathbb{R}^n_+$$ is $$\vartheta = n$$. Each iteration reduces $$\mu$$ by a factor $$\left(1 - \frac{1}{\sqrt{\vartheta}}\right)$$ with only $$O(1)$$ Newton steps, so $$O(\sqrt{\vartheta}\log(1/\epsilon)) = O(\sqrt{n}\log(1/\epsilon))$$ iterations are needed to bring $$\mu$$ below $$\epsilon$$.

**Total:** $$O(\sqrt{n} \log(1/\epsilon))$$ iterations.

**Polynomial!** (versus the worst-case exponential complexity of the simplex method)

</details>

---

## 💡 **Summary**

### **Primal-Dual IPM Components:**

| Component | Purpose |
|-----------|---------|
| **Central path** | Smooth trajectory to optimum |
| **Perturbed KKT** | $$\lambda x = \mu e$$ replaces complementarity |
| **Newton system** | Solve 3×3 block system |
| **Predictor-Corrector** | Balance progress vs centering |
| **Infeasible start** | Handle infeasibility gracefully |

### **Complexity:**

- **Per iteration:** $$O(n^3)$$ (matrix factorization)
- **Total iterations:** $$O(\sqrt{n} \log(1/\epsilon))$$
- **Overall:** $$O(n^{3.5} \log(1/\epsilon))$$ for LP

---

## 📚 **References**

1. Wright, S. J. (1997). *Primal-Dual Interior-Point Methods*. SIAM.
2. Nesterov, Y., & Nemirovskii, A. (1994). *Interior-Point Polynomial Algorithms*.
3. Mehrotra, S. (1992). "On the Implementation of a Primal-Dual IPM". *SIAM Journal*.

