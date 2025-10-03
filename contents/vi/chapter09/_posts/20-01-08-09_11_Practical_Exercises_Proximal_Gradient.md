---
layout: post
title: 09-11 Bài Tập Thực Hành - Proximal Gradient
chapter: '09'
order: 12
owner: GitHub Copilot
lang: vi
categories:
- chapter09
lesson_type: required
---

# Bài Tập Thực Hành - Proximal Gradient

Các bài tập được tham khảo từ Parikh & Boyd (2014) và Beck & Teboulle (2009).

---

## 📝 **Bài tập 1: LASSO với Soft-Thresholding**

Cho LASSO: $$\min \frac{1}{2}\|Ax - b\|^2 + \lambda\|x\|_1$$ với $$A = I$$, $$b = (2, -1, 0.5)^T$$, $$\lambda = 1$$.

**a)** Viết proximal operator  
**b)** Tính soft-thresholding  
**c)** Iterate từ $$x^{(0)} = 0$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Proximal operator:**

$$\text{prox}_{t\lambda\|\cdot\|_1}(y) = S_\lambda(y)$$

**Soft-thresholding:**

$$S_\lambda(y_i) = \begin{cases}
y_i - \lambda & \text{if } y_i > \lambda \\
0 & \text{if } |y_i| \leq \lambda \\
y_i + \lambda & \text{if } y_i < -\lambda
\end{cases}$$

**Với $$A = I$$:**

$$x^{(1)} = S_1(b) = (1, 0, 0)^T$$

Converged in 1 step!

</details>

---

## 📝 **Bài tập 2: Matrix Completion**

Minimize $$\|X\|_*$$ s.t. $$X_{ij} = M_{ij}$$ for observed entries.

**a)** Viết proximal gradient với $$f(X) = \frac{1}{2}\|P_\Omega(X - M)\|_F^2$$  
**b)** Tính proximal operator của nuclear norm  
**c)** Apply SVD soft-thresholding

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Proximal operator of nuclear norm:**

$$\text{prox}_{t\|\cdot\|_*}(Y) = U S_t(\Sigma) V^T$$

với $$Y = U\Sigma V^T$$ (SVD), $$S_t(\sigma_i) = \max(\sigma_i - t, 0)$$.

**Update:**

$$X^{(k+1)} = \text{prox}_{t\|\cdot\|_*}(X^{(k)} - t\nabla f(X^{(k)}))$$

$$\nabla f(X) = P_\Omega(X - M)$$

</details>

---

## 📝 **Bài tập 3: Accelerated Proximal Gradient (FISTA)**

Cho $$f(x) + g(x)$$ với $$f$$ smooth, $$g$$ non-smooth.

**a)** Viết FISTA update  
**b)** So sánh convergence rate với proximal GD  
**c)** Apply to LASSO

<details>
<summary><strong>💡 Lời giải</strong></summary>

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

**$$k^2$$ speedup!**

</details>

---

## 📝 **Bài tập 4: Proximal Operators**

Tính proximal operator cho:

**a)** $$g(x) = \|x\|_2$$  
**b)** $$g(x) = I_C(x)$$ (indicator của convex set $$C$$)  
**c)** $$g(x) = \frac{1}{2}x^TQx$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

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

## 📝 **Bài tập 5: Dual Proximal Gradient**

Cho $$\min Ax = b, x \geq 0$$ $$c^Tx$$.

**a)** Viết dual problem  
**b)** Apply proximal gradient trên dual  
**c)** Recover primal solution

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Dual:**

$$\max_\nu \quad g(\nu) = -b^T\nu$$

s.t. $$A^T\nu \leq c$$

**Proximal gradient trên dual:**

$$\nu^{(k+1)} = \Pi_{\{A^T\nu \leq c\}}(\nu^{(k)} + t b)$$

**Recover primal:**

$$x^{(k)} = \arg\min_x L(x, \nu^{(k)})$$

</details>

---

## 💡 **Tổng kết**

| Method | Convergence | Key Feature |
|--------|-------------|-------------|
| Proximal GD | $$O(1/k)$$ | Handles non-smooth $$g$$ |
| FISTA | $$O(1/k^2)$$ | Accelerated |
| Dual Proximal | $$O(1/k)$$ | Constraints via dual |

### **Proximal Operators:**

| Function | Proximal Operator |
|----------|-------------------|
| $$\|\cdot\|_1$$ | Soft-thresholding |
| $$\|\cdot\|_2$$ | Block soft-thresholding |
| $$\|\cdot\|_*$$ | SVD soft-thresholding |
| $$I_C$$ | Projection $$\Pi_C$$ |
| Quadratic | Matrix inversion |

---

## 📚 **Tài liệu Tham khảo**

1. Parikh, N., & Boyd, S. (2014). "Proximal Algorithms". Foundations and Trends.
2. Beck, A., & Teboulle, M. (2009). "A Fast Iterative Shrinkage-Thresholding Algorithm" (FISTA).
3. Combettes, P. L., & Pesquet, J.-C. (2011). "Proximal Splitting Methods".
