---
layout: post
title: 17-7 Bài Tập Thực Hành - Primal-Dual Interior Point
chapter: '17'
order: 8
owner: GitHub Copilot
lang: vi
categories:
- chapter17
lesson_type: required
---

# Bài Tập Thực Hành - Primal-Dual Interior Point Methods

Các bài tập được tham khảo từ Wright (1997) và Nesterov & Nemirovskii (1994).

---

## 📝 **Bài tập 1: Primal-Dual Central Path cho LP**

Cho LP:

$$
\begin{align}
\min \quad & x_1 + 2x_2 \\
\text{s.t.} \quad & x_1 + x_2 = 3 \\
& x_1, x_2 \geq 0
\end{align}
$$

**Yêu cầu:**  
a) Viết KKT conditions  
b) Derive perturbed KKT với parameter $$\mu$$  
c) Tính central path $$x(\mu)$$ cho $$\mu = 1, 0.1, 0.01$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) KKT conditions:**

$$
\begin{align}
\nabla f + A^T\nu - \lambda &= 0 \quad \text{(stationarity)} \\
Ax &= b \quad \text{(primal feasibility)} \\
x &\geq 0, \, \lambda \geq 0 \quad \text{(dual feasibility)} \\
\lambda_i x_i &= 0 \quad \text{(complementarity)}
\end{align}
$$

Với data:

$$
\begin{align}
\begin{bmatrix} 1 \\ 2 \end{bmatrix} + \nu \begin{bmatrix} 1 \\ 1 \end{bmatrix} - \begin{bmatrix} \lambda_1 \\ \lambda_2 \end{bmatrix} &= 0 \\
x_1 + x_2 &= 3 \\
\lambda_1 x_1 = \lambda_2 x_2 &= 0
\end{align}
$$

---

**b) Perturbed KKT (central path conditions):**

Replace complementarity $$\lambda_i x_i = 0$$ với:

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

Từ (1): $$\lambda_1 = 1 + \nu$$  
Từ (2): $$\lambda_2 = 2 + \nu$$  
Từ (4): $$x_1 = \frac{\mu}{1 + \nu}$$  
Từ (5): $$x_2 = \frac{\mu}{2 + \nu}$$  

Substitute vào (3):

$$\frac{\mu}{1+\nu} + \frac{\mu}{2+\nu} = 3$$

$$\mu\left(\frac{1}{1+\nu} + \frac{1}{2+\nu}\right) = 3$$

$$\mu \cdot \frac{(2+\nu) + (1+\nu)}{(1+\nu)(2+\nu)} = 3$$

$$\mu \cdot \frac{3 + 2\nu}{(1+\nu)(2+\nu)} = 3$$

$$(1+\nu)(2+\nu) = \mu(1 + \frac{2\nu}{3})$$

Solve quadratic: $$\nu^2 + 3\nu + 2 = \mu + \frac{2\mu\nu}{3}$$

**For $$\mu = 1$$:**

$$\nu^2 + 3\nu + 2 = 1 + \frac{2\nu}{3}$$

$$\nu^2 + \frac{7\nu}{3} + 1 = 0$$

$$\nu = \frac{-7/3 \pm \sqrt{49/9 - 4}}{2} \approx -0.5$$

$$x_1 = \frac{1}{1-0.5} = 2$$, $$x_2 = \frac{1}{2-0.5} = 0.67$$

**For $$\mu \to 0$$:** $$x^* \to (3, 0)$$ (primal optimal), $$\nu^* \to -1$$

</details>

---

## 📝 **Bài tập 2: Newton Step for Primal-Dual System**

Cho LP từ Bài tập 1. Tại $$(x, \lambda, \nu)^{(k)}$$, solve Newton system:

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

với $$\Lambda = \text{diag}(\lambda)$$, $$X = \text{diag}(x)$$.

**Yêu cầu:**  
a) Viết residuals $$r_d, r_p, r_c$$  
b) Simplify system bằng cách eliminate $$\Delta\lambda$$  
c) Compute $$\Delta x$$ cho $$x = (1, 1)$$, $$\lambda = (2, 3)$$, $$\nu = -1$$, $$\mu = 0.5$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

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

Substitute vào row 1:

$$A^T \Delta\nu - \Delta\lambda = -r_d$$

$$A^T \Delta\nu + X^{-1}(\Lambda \Delta x + r_c) = -r_d$$

$$\Lambda X^{-1} \Delta x + A^T \Delta\nu = -r_d - X^{-1}r_c$$

Combined với row 2:

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

Solve: $$\Delta x \approx (0.5, 0.17)$$, $$\Delta\nu \approx 0.33$$

</details>

---

## 📝 **Bài tập 3: Mehrotra Predictor-Corrector**

Mehrotra's algorithm combines predictor và corrector steps:

**Predictor:** $$\mu = 0$$ (affine scaling)  
**Corrector:** $$\mu = \sigma \cdot \frac{x^T\lambda}{n}$$ với $$\sigma \in (0, 1)$$

**Yêu cầu:**  
a) Explain intuition cho 2 steps  
b) Compute $$\sigma$$ từ predictor step  
c) Apply to LP từ Bài tập 1

<details>
<summary><strong>💡 Lời giải</strong></summary>

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

## 📝 **Bài tập 4: Infeasible Start**

Cho infeasible start $$(x^{(0)}, \lambda^{(0)}, \nu^{(0)})$$ không satisfy $$Ax = b$$.

**Yêu cầu:**  
a) Modify residuals để handle infeasibility  
b) Show convergence đến primal-dual feasibility  
c) Apply to LP với $$x^{(0)} = (1, 1)$$ (infeasible cho $$x_1 + x_2 = 3$$)

<details>
<summary><strong>💡 Lời giải</strong></summary>

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

After 1 Newton step: $$x^{(1)} = (1.5, 1.5)$$, $$r_p = 0$$ (feasible!)

Then continue as standard primal-dual IPM.

</details>

---

## 📝 **Bài tập 5: Self-Concordance and Polynomial Complexity**

Interior point methods có polynomial complexity nhờ self-concordant barriers.

**Yêu cầu:**  
a) Define self-concordance  
b) Show $$\phi(x) = -\sum \log x_i$$ is self-concordant  
c) Explain why this gives $$O(\sqrt{n} \log(1/\epsilon))$$ iterations

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Self-concordance:**

$$\phi$$ is self-concordant if:

$$|\phi'''(x)[h, h, h]| \leq 2(\phi''(x)[h, h])^{3/2} \quad \forall h$$

**Ý nghĩa:** Third derivative controlled by second derivative.

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

**Key:** $$\nu = 1$$ (barrier parameter for simplex) → $$O(\sqrt{n})$$ Newton steps per barrier reduction.

**Total:** $$O(\sqrt{n} \log(1/\epsilon))$$ iterations.

**Polynomial!** (vs exponential for simplex method)

</details>

---

## 💡 **Tổng kết**

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

## 📚 **Tài liệu Tham khảo**

1. Wright, S. J. (1997). *Primal-Dual Interior-Point Methods*. SIAM.
2. Nesterov, Y., & Nemirovskii, A. (1994). *Interior-Point Polynomial Algorithms*.
3. Mehrotra, S. (1992). "On the Implementation of a Primal-Dual IPM". *SIAM Journal*.

