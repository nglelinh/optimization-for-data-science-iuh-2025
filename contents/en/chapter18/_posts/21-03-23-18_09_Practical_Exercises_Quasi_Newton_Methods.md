---
layout: post
title: '18-09 Practical Exercises - Quasi-Newton Methods'
chapter: '18'
order: 10
owner: GitHub Copilot
lang: en
categories:
- chapter18
lesson_type: required
redirect_from:
  - /contents/en/chapter18/18_08_Practical_Exercises_Quasi_Newton_Methods/
---

Quasi-Newton methods look deceptively tidy in matrix notation, yet a single sign error in $$y^T s$$ or a forgotten Wolfe curvature check can turn a positive-definite BFGS matrix into an uphill ascent step. These practical exercises—adapted from Nocedal & Wright—walk you through hand-verifying secant updates, checking positive definiteness, and implementing L-BFGS. Before starting Exercise 1, run through this quick warm-up proving *why* the Wolfe curvature condition is the exact mathematical lock that keeps $$y^T s > 0$$ alive on nonconvex functions.

## Key ideas: Essential Skills for the Quasi-Newton Exercises

- **Matrix Update Fluency:** Be comfortable computing rank-1 (SR1) and rank-2 (DFP, BFGS) updates both on $$B_k$$ and directly on $$H_k$$, and verifying the secant identity $$H_{k+1} y_k = s_k$$ as an arithmetic sanity check.
- **Curvature Condition & Wolfe Line Search:** Understand how Armijo sufficient decrease prevents overly long steps while the Wolfe curvature condition prevents overly short steps *and* guarantees $$y_k^T s_k > 0$$.
- **Two-Loop L-BFGS Implementation:** Translate the $$O(mn)$$ backward/forward dot-product loops into clean vector code without forming any $$n \times n$$ matrices.
- **Empirical Rate Diagnosis:** Distinguish linear convergence (GD), superlinear convergence (BFGS), and quadratic convergence (Newton) from log-error plots on Rosenbrock and ill-conditioned quadratics.

### Worked example: Why Wolfe Curvature Guarantees $$y^T s > 0$$

Consider the nonconvex 1D double-well potential $$f(x) = x^4 - 2x^2$$ ($$f'(x) = 4x^3 - 4x$$) at $$x^0 = 0.5$$, where $$f'(0.5) = -1.5 < 0$$, so $$p = +1$$ is a descent direction. Set Wolfe parameters $$c_1 = 0.1, \; c_2 = 0.9$$.

1. **Test a short step $$\alpha = 0.1$$ (passes Armijo, fails Wolfe curvature):**
   At $$x^1 = 0.5 + 0.1 = 0.6$$, $$f'(0.6) = 4(0.216) - 2.4 = -1.536$$.
   - Check Armijo: $$f(0.6) = -0.5904 \le f(0.5) + 0.1(0.1)(-1.5) = -0.4375 - 0.015 = -0.4525$$ $$\checkmark$$.
   - Check curvature: $$s = 0.1$$, $$y = f'(0.6) - f'(0.5) = -1.536 - (-1.5) = -0.036 \implies y^T s = -0.0036 < 0$$!
   Armijo *accepted* this step, yet BFGS would break because $$f$$ is still concave at $$x = 0.6$$!
2. **Test $$\alpha = 0.5$$ (passes both Armijo and Wolfe curvature):**
   At $$x^1 = 1.0$$, $$f'(1.0) = 0$$.
   - Check Wolfe curvature: $$f'(1.0) \cdot p = 0 \ge c_2 f'(0.5) \cdot p = 0.9(-1.5) = -1.35$$ $$\checkmark$$.
   - Check $$y^T s$$ automatically:
     $$y^T s = \alpha \big(f'(x^1) - f'(x^0)\big) p \ge \alpha (c_2 - 1) f'(x^0) p = 0.5(-0.1)(-1.5) = +0.075 > 0.$$
   (Actual value: $$y^T s = (0 - (-1.5))(0.5) = +0.75 > 0$$.)
3. **Takeaway for the exercises:**
   Whenever a Wolfe line search succeeds on a descent direction, $$y^T s > 0$$ is guaranteed *even on nonconvex functions*—ensuring your BFGS update in the exercises below remains strictly positive definite!

# Practical Exercises - Quasi-Newton Methods

The exercises are adapted from Nocedal & Wright (2006). Throughout, $$H_k$$ denotes the approximation of the **inverse** Hessian.

---

## 📝 **Exercise 1: BFGS Update**

Given $$f(x) = x_1^2 + 4x_2^2$$, $$x^{(k)} = (2, 1)$$, $$x^{(k+1)} = (1.6, 0.7)$$.

**Tasks:**  
a) Compute $$s^{(k)} = x^{(k+1)} - x^{(k)}$$, $$y^{(k)} = \nabla f(x^{(k+1)}) - \nabla f(x^{(k)})$$  
b) Apply the BFGS update of the inverse Hessian: $$H_{k+1} = \left(I - \rho s y^T\right) H_k \left(I - \rho y s^T\right) + \rho s s^T$$, $$\rho = \frac{1}{y^Ts}$$  
c) Verify $$H_{k+1}y = s$$ (secant condition)

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Compute $$s, y$$:**

$$s = (1.6, 0.7) - (2, 1) = (-0.4, -0.3)$$

$$\nabla f(x) = (2x_1, 8x_2)$$

$$\nabla f(x^{(k)}) = (4, 8)$$, $$\nabla f(x^{(k+1)}) = (3.2, 5.6)$$

$$y = (3.2, 5.6) - (4, 8) = (-0.8, -2.4)$$

---

**b) BFGS update (start with $$H_0 = I$$):**

$$y^Ts = (-0.8)(-0.4) + (-2.4)(-0.3) = 0.32 + 0.72 = 1.04$$, so $$\rho = 1/1.04 \approx 0.9615$$

$$I - \rho s y^T = \begin{bmatrix} 0.692 & -0.923 \\ -0.231 & 0.308 \end{bmatrix}$$

$$H_1 = (I - \rho s y^T)(I - \rho y s^T) + \rho s s^T$$

$$\approx \begin{bmatrix} 1.331 & -0.444 \\ -0.444 & 0.148 \end{bmatrix} + \begin{bmatrix} 0.154 & 0.115 \\ 0.115 & 0.087 \end{bmatrix} \approx \begin{bmatrix} 1.485 & -0.328 \\ -0.328 & 0.234 \end{bmatrix}$$

---

**c) Verify the secant condition:**

$$H_1 y = \begin{bmatrix} 1.485 & -0.328 \\ -0.328 & 0.234 \end{bmatrix} \begin{bmatrix} -0.8 \\ -2.4 \end{bmatrix} \approx \begin{bmatrix} -0.4 \\ -0.3 \end{bmatrix} = s$$ ✓

(Remark: the simpler formula $$H - \frac{Hyy^TH}{y^THy} + \frac{ss^T}{y^Ts}$$ is the DFP update of the inverse Hessian; it also satisfies the secant condition, giving $$H_1 \approx \begin{bmatrix} 1.054 & -0.185 \\ -0.185 & 0.187 \end{bmatrix}$$ here.)

</details>

---

## 📝 **Exercise 2: SR1 vs BFGS**

SR1 update: $$H_{k+1} = H_k + \frac{(s - H_k y)(s - H_k y)^T}{(s - H_k y)^T y}$$

**Tasks:**  
a) Compare stability with BFGS  
b) When does SR1 fail?  
c) Compute SR1 for the data of Exercise 1

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Stability:**

- **BFGS:** always positive definite (if $$y^Ts > 0$$)
- **SR1:** may be singular/indefinite

**b) SR1 fails when:**

$$(s - H_k y)^T y \approx 0$$ → division by zero

**Skip the update** if $$|(s - H_k y)^T y| < \epsilon \|s - H_k y\| \|y\|$$

---

**c) SR1 update:**

$$s - H_0 y = (-0.4, -0.3) - (-0.8, -2.4) = (0.4, 2.1)$$

$$(s - H_0 y)^T y = 0.4(-0.8) + 2.1(-2.4) = -0.32 - 5.04 = -5.36$$

$$H_1^{\text{SR1}} = I + \frac{1}{-5.36}\begin{bmatrix} 0.16 & 0.84 \\ 0.84 & 4.41 \end{bmatrix}$$

$$\approx \begin{bmatrix} 0.970 & -0.157 \\ -0.157 & 0.177 \end{bmatrix}$$

It satisfies the secant condition $$H_1 y = s$$. Here it happens to stay positive definite (its determinant is about $$0.147 > 0$$), but SR1 does **not** guarantee this in general, and its denominator can be negative or near zero.

</details>

---

## 📝 **Exercise 3: L-BFGS for Large-Scale Problems**

L-BFGS stores the $$m$$ most recent $$(s, y)$$ pairs instead of the full $$H_k$$.

**Tasks:**  
a) Derive the two-loop recursion  
b) Compute $$H_k \nabla f$$ with $$m = 2$$ stored pairs  
c) Estimate the memory: $$n = 10^6$$, $$m = 10$$

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Two-loop recursion:**

```
q = ∇f(x_k)
for i = k-1, ..., k-m:
    α_i = ρ_i s_i^T q
    q = q - α_i y_i
r = H_0 q  (often H_0 = γI)
for i = k-m, ..., k-1:
    β = ρ_i y_i^T r
    r = r + s_i(α_i - β)
return r = H_k ∇f
```

---

**b) Example with $$m = 2$$:**

$$\{(s_1, y_1), (s_2, y_2)\}$$, $$\rho_i = \frac{1}{y_i^T s_i}$$

**Loop 1 (backward):**

$$\alpha_2 = \rho_2 s_2^T \nabla f$$, $$q_1 = \nabla f - \alpha_2 y_2$$

$$\alpha_1 = \rho_1 s_1^T q_1$$, $$q_0 = q_1 - \alpha_1 y_1$$

**Initialize:** $$r_0 = \gamma q_0$$

**Loop 2 (forward):**

$$\beta_1 = \rho_1 y_1^T r_0$$, $$r_1 = r_0 + s_1(\alpha_1 - \beta_1)$$

$$\beta_2 = \rho_2 y_2^T r_1$$, $$r_2 = r_1 + s_2(\alpha_2 - \beta_2)$$

$$d = -r_2$$

---

**c) Memory (64-bit floats):**

**Full BFGS:** $$n^2$$ entries → $$10^{12}$$ floats ≈ **8 TB**

**L-BFGS:** $$2mn$$ entries → $$2 \cdot 10 \cdot 10^6 = 2 \times 10^7$$ floats ≈ **160 MB**

**$$50{,}000\times$$ reduction!**

</details>

---

## 📝 **Exercise 4: Convergence Rate**

**Tasks:**  
a) Newton: $$\|x^{(k+1)} - x^*\| \leq C\|x^{(k)} - x^*\|^2$$ (quadratic)  
b) BFGS: $$\|x^{(k+1)} - x^*\| \leq C_k\|x^{(k)} - x^*\|$$ with $$C_k \to 0$$ — what is the order?  
c) Compare the number of iterations needed

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Newton:**

**Quadratic:** $$p = 2$$, with $$C \propto \frac{M}{2m}$$ ($$M$$: Lipschitz constant of the Hessian, $$m$$: strong convexity constant)

For accuracy $$\epsilon$$: about $$\log\log(1/\epsilon)$$ iterations

---

**b) BFGS:**

**Superlinear:** $$p = 1 + o(1)$$ (between linear and quadratic)

$$\|H_k - \nabla^2 f^{-1}\| \to 0$$ along the iterates → eventually quadratic-like

---

**c) Iteration count (to reach $$10^{-10}$$, illustrative):**

| Method | Rate | Iterations |
|--------|------|------------|
| GD | Linear ($$0.9^k$$) | ~220 |
| BFGS | Superlinear | ~15 |
| Newton | Quadratic | ~5 |

**BFGS: a good balance!**

</details>

---

## 📝 **Exercise 5: Practical Implementation**

**Tasks:**  
a) When should the BFGS update be skipped?  
b) Scaling of $$H_0$$  
c) Line search requirements

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Skip the update when:**

$$y^Ts \leq \epsilon_s \|s\|^2$$ (curvature condition violated)

**Reason:** maintain positive definiteness

---

**b) Initial Hessian approximation:**

$$H_0 = \gamma I$$ with $$\gamma = \frac{y_{k-1}^T s_{k-1}}{y_{k-1}^T y_{k-1}}$$

**Adaptive scaling** based on the most recent curvature.

---

**c) Line search:**

**Strong Wolfe conditions:**

1. $$f(x + \alpha d) \leq f(x) + c_1 \alpha \nabla f^T d$$ (sufficient decrease)
2. $$|\nabla f(x + \alpha d)^T d| \leq c_2 |\nabla f^T d|$$ (curvature)

With $$c_1 = 10^{-4}$$, $$c_2 = 0.9$$.

**Ensures $$y^Ts > 0$$!**

</details>

---

## 💡 **Summary**

| Method | Storage | Rate | Best for |
|--------|---------|------|----------|
| Newton | $$O(n^2)$$ | Quadratic | Small $$n$$ |
| BFGS | $$O(n^2)$$ | Superlinear | Medium $$n$$ |
| L-BFGS | $$O(mn)$$ | Superlinear | Large $$n$$ |
| SR1 | $$O(n^2)$$ | Superlinear | Non-PD is acceptable |

---

## 📚 **References**

1. Nocedal, J., & Wright, S. J. (2006). *Numerical Optimization*. Springer. Chapter 6.
2. Liu, D. C., & Nocedal, J. (1989). "On the Limited Memory BFGS Method".
