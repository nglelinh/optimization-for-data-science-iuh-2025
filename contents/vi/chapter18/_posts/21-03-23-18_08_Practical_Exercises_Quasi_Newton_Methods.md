---
layout: post
title: 18-8 Bài Tập Thực Hành - Quasi-Newton Methods
chapter: '18'
order: 9
owner: GitHub Copilot
lang: vi
categories:
- chapter18
lesson_type: required
---

# Bài Tập Thực Hành - Quasi-Newton Methods

Các bài tập được tham khảo từ Nocedal & Wright (2006).

---

## 📝 **Bài tập 1: BFGS Update**

Cho $$f(x) = x_1^2 + 4x_2^2$$, $$x^{(k)} = (2, 1)$$, $$x^{(k+1)} = (1.6, 0.7)$$.

**Yêu cầu:**  
a) Tính $$s^{(k)} = x^{(k+1)} - x^{(k)}$$, $$y^{(k)} = \nabla f(x^{(k+1)}) - \nabla f(x^{(k)})$$  
b) Apply BFGS update: $$H_{k+1} = H_k - \frac{H_k y y^T H_k}{y^T H_k y} + \frac{ss^T}{y^Ts}$$  
c) Verify $$H_{k+1}y = s$$ (secant condition)

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Compute $$s, y$$:**

$$s = (1.6, 0.7) - (2, 1) = (-0.4, -0.3)$$

$$\nabla f(x) = (2x_1, 8x_2)$$

$$\nabla f(x^{(k)}) = (4, 8)$$, $$\nabla f(x^{(k+1)}) = (3.2, 5.6)$$

$$y = (3.2, 5.6) - (4, 8) = (-0.8, -2.4)$$

---

**b) BFGS update (start $$H_0 = I$$):**

$$y^Ts = (-0.8)(-0.4) + (-2.4)(-0.3) = 0.32 + 0.72 = 1.04$$

$$H_0 y = (-0.8, -2.4)$$

$$y^T H_0 y = 0.64 + 5.76 = 6.4$$

$$H_1 = I - \frac{yy^T}{6.4} + \frac{ss^T}{1.04}$$

$$= I - \frac{1}{6.4}\begin{bmatrix} 0.64 & 1.92 \\ 1.92 & 5.76 \end{bmatrix} + \frac{1}{1.04}\begin{bmatrix} 0.16 & 0.12 \\ 0.12 & 0.09 \end{bmatrix}$$

$$\approx \begin{bmatrix} 1.05 & 0.11 \\ 0.11 & 0.19 \end{bmatrix}$$

---

**c) Verify secant:**

$$H_1 y = \begin{bmatrix} 1.05 & 0.11 \\ 0.11 & 0.19 \end{bmatrix} \begin{bmatrix} -0.8 \\ -2.4 \end{bmatrix} \approx \begin{bmatrix} -0.4 \\ -0.3 \end{bmatrix} = s$$ ✓

</details>

---

## 📝 **Bài tập 2: SR1 vs BFGS**

SR1 update: $$H_{k+1} = H_k + \frac{(s - H_k y)(s - H_k y)^T}{(s - H_k y)^T y}$$

**Yêu cầu:**  
a) Compare stability với BFGS  
b) Khi nào SR1 fails?  
c) Tính SR1 cho data từ Bài tập 1

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Stability:**

- **BFGS:** Always positive definite (if $$y^Ts > 0$$)
- **SR1:** Có thể singular/indefinite

**b) SR1 fails khi:**

$$(s - H_k y)^T y \approx 0$$ → division by zero

**Skip update** nếu $$|(s - H_k y)^T y| < \epsilon \|s\| \|y\|$$

---

**c) SR1 update:**

$$s - H_0 y = (-0.4, -0.3) - (-0.8, -2.4) = (0.4, 2.1)$$

$$(s - H_0 y)^T y = 0.4(-0.8) + 2.1(-2.4) = -0.32 - 5.04 = -5.36$$

$$H_1^{\text{SR1}} = I + \frac{1}{-5.36}\begin{bmatrix} 0.16 & 0.84 \\ 0.84 & 4.41 \end{bmatrix}$$

$$\approx \begin{bmatrix} 0.97 & -0.16 \\ -0.16 & 0.18 \end{bmatrix}$$

**Not positive definite!** (SR1 characteristic)

</details>

---

## 📝 **Bài tập 3: L-BFGS for Large-Scale**

L-BFGS stores $$m$$ recent $$(s, y)$$ pairs thay vì full $$H_k$$.

**Yêu cầu:**  
a) Derive two-loop recursion  
b) Compute $$H_k \nabla f$$ với $$m = 2$$ stored pairs  
c) Estimate memory: $$n = 10^6$$, $$m = 10$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

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

**b) Example với $$m = 2$$:**

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

**c) Memory:**

**Full BFGS:** $$n^2$$ entries → $$10^{12}$$ floats ≈ **8 TB**

**L-BFGS:** $$2mn$$ entries → $$2 \cdot 10 \cdot 10^6 = 2 \times 10^7$$ floats ≈ **160 MB**

**$$50,000\times$$ reduction!**

</details>

---

## 📝 **Bài tập 4: Convergence Rate**

**Yêu cầu:**  
a) Newton: $$\|x^{(k+1)} - x^*\| \leq C\|x^{(k)} - x^*\|^2$$ (quadratic)  
b) BFGS: $$\|x^{(k+1)} - x^*\| \leq C\|x^{(k)} - x^*\|^p$$ với $$p = ?$$  
c) Compare iterations cần thiết

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Newton:**

**Quadratic:** $$p = 2$$, $$C \approx \frac{\|\nabla^3 f\|}{2\|\nabla^2 f^{-1}\|}$$

From $$\epsilon$$: $$\log\log(1/\epsilon)$$ iterations

---

**b) BFGS:**

**Superlinear:** $$p = 1 + o(1)$$ (between linear and quadratic)

$$\|H_k - \nabla^2 f^{-1}\| \to 0$$ → eventually quadratic-like

---

**c) Iteration count (to $$10^{-10}$$):**

| Method | Rate | Iterations |
|--------|------|------------|
| GD | Linear ($$0.9^k$$) | ~230 |
| BFGS | Superlinear | ~15 |
| Newton | Quadratic | ~5 |

**BFGS: Good balance!**

</details>

---

## 📝 **Bài tập 5: Practical Implementation**

**Yêu cầu:**  
a) Khi nào skip BFGS update?  
b) Scaling $$H_0$$  
c) Line search requirements

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Skip update khi:**

$$y^Ts \leq \epsilon_s \|s\|^2$$ (curvature condition violated)

**Reason:** Maintain positive definiteness

---

**b) Initial Hessian approximation:**

$$H_0 = \gamma I$$ với $$\gamma = \frac{y_{k-1}^T s_{k-1}}{y_{k-1}^T y_{k-1}}$$

**Adaptive scaling** based on most recent curvature.

---

**c) Line search:**

**Strong Wolfe conditions:**

1. $$f(x + \alpha d) \leq f(x) + c_1 \alpha \nabla f^T d$$ (sufficient decrease)
2. $$|\nabla f(x + \alpha d)^T d| \leq c_2 |\nabla f^T d|$$ (curvature)

With $$c_1 = 10^{-4}$$, $$c_2 = 0.9$$.

**Ensures $$y^Ts > 0$$!**

</details>

---

## 💡 **Tổng kết**

| Method | Storage | Rate | Best for |
|--------|---------|------|----------|
| Newton | $$O(n^2)$$ | Quadratic | Small $$n$$ |
| BFGS | $$O(n^2)$$ | Superlinear | Medium $$n$$ |
| L-BFGS | $$O(mn)$$ | Superlinear | Large $$n$$ |
| SR1 | $$O(n^2)$$ | Superlinear | Non-PD ok |

---

## 📚 **Tài liệu Tham khảo**

1. Nocedal, J., & Wright, S. J. (2006). *Numerical Optimization*. Springer. Chapter 6.
2. Liu, D. C., & Nocedal, J. (1989). "On the Limited Memory BFGS Method".

