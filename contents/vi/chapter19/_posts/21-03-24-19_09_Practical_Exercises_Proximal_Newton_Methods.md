---
layout: post
title: 19-8 Bài Tập Thực Hành - Proximal Newton Methods
chapter: '19'
order: 9
owner: GitHub Copilot
lang: vi
categories:
- chapter19
lesson_type: required
---

# Bài Tập Thực Hành - Proximal Newton Methods

Các bài tập được tham khảo từ Lee et al. (2014) và Rakotomamonjy et al. (2016).

---

## 📝 **Bài tập 1: Proximal Newton Step**

Cho $$f(x) + g(x)$$ với $$f(x) = x^2$$, $$g(x) = |x|$$.

**Yêu cầu:**  
a) Viết proximal Newton subproblem  
b) Solve tại $$x^{(k)} = 2$$  
c) Compare với proximal gradient

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Proximal Newton:**

$$x^{(k+1)} = \arg\min_x \left\{ f(x^{(k)}) + \nabla f(x^{(k)})^T(x - x^{(k)}) + \frac{1}{2}(x - x^{(k)})^T \nabla^2 f(x^{(k)})(x - x^{(k)}) + g(x) \right\}$$

$$= \arg\min_x \left\{ \frac{H_k}{2}(x - x^{(k)})^2 + \nabla f(x^{(k)})(x - x^{(k)}) + g(x) \right\}$$

---

**b) Tại $$x^{(k)} = 2$$:**

$$\nabla f(2) = 4$$, $$\nabla^2 f(2) = 2$$

$$\min_x \left\{ (x - 2)^2 + 4(x - 2) + |x| \right\}$$

$$= \min_x \left\{ x^2 - 4x + 4 + 4x - 8 + |x| \right\}$$

$$= \min_x \left\{ x^2 - 4 + |x| \right\}$$

**Case 1:** $$x \geq 0$$: $$\min x^2 + x - 4$$, $$x^* = -0.5$$ (infeasible)

**Case 2:** $$x < 0$$: $$\min x^2 - x - 4$$, $$x^* = 0.5$$ (infeasible)

**Check boundaries:** $$x = 0$$: $$-4$$

**Optimal:** $$x^{(1)} = 0$$

---

**c) Proximal GD:**

$$x^{(k+1)} = \text{prox}_{t|·|}(x^{(k)} - t\nabla f(x^{(k)}))$$

$$= \text{prox}_{t|·|}(2 - 4t) = S_t(2 - 4t)$$

Với $$t = 0.5$$: $$S_{0.5}(0) = 0$$

**Same result!** (for this simple case)

</details>

---

## 📝 **Bài tập 2: LASSO Proximal Newton**

$$\min \frac{1}{2}\|Ax - b\|^2 + \lambda\|x\|_1$$

**Yêu cầu:**  
a) Identify active/inactive variables  
b) Apply Newton trên active set  
c) Handle sign changes

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Active set:**

$$\mathcal{A} = \{i : x_i \neq 0\}$$, $$\mathcal{I} = \{i : x_i = 0\}$$

**KKT:** $$\nabla f(x) + \lambda \cdot \text{sign}(x) = 0$$ trên $$\mathcal{A}$$

---

**b) Newton trên $$\mathcal{A}$$:**

$$\min_{x_{\mathcal{A}}} \frac{1}{2}\|A_{\mathcal{A}}x_{\mathcal{A}} - b\|^2 + \lambda\|x_{\mathcal{A}}\|_1$$

với $$\text{sign}(x_{\mathcal{A}})$$ fixed:

$$\nabla^2 f_{\mathcal{A}} \Delta x = -\nabla f_{\mathcal{A}} - \lambda \cdot \text{sign}(x_{\mathcal{A}})$$

$$\Delta x = -(A_{\mathcal{A}}^T A_{\mathcal{A}})^{-1}(A_{\mathcal{A}}^T(A_{\mathcal{A}}x - b) + \lambda \cdot \text{sign}(x_{\mathcal{A}}))$$

---

**c) Sign changes:**

Nếu $$x_i^{\text{new}} \cdot x_i^{\text{old}} < 0$$ → truncate step:

$$\alpha_{\max} = \min_i \frac{-x_i^{\text{old}}}{\Delta x_i}$$

**Safe update:** $$x^{(k+1)} = x^{(k)} + 0.99\alpha_{\max} \Delta x$$

</details>

---

## 📝 **Bài tập 3: Semismooth Newton**

Cho $$F(x) = \nabla f(x) + \partial g(x) \ni 0$$.

**Yêu cầu:**  
a) Define generalized Jacobian  
b) Apply to $$g(x) = \|x\|_1$$  
c) Show superlinear convergence

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Generalized Jacobian:**

$$\partial F(x) = \nabla^2 f(x) + \partial^2 g(x)$$

với $$\partial^2 g$$ là set-valued second derivative.

---

**b) For $$g(x) = \|x\|_1$$:**

$$\partial g(x)_i = \begin{cases}
\text{sign}(x_i) & \text{if } x_i \neq 0 \\
[-1, 1] & \text{if } x_i = 0
\end{cases}$$

$$\partial^2 g(x)_i = \begin{cases}
0 & \text{if } x_i \neq 0 \\
\{0\} \cup \{\infty \cdot \text{sign}\} & \text{if } x_i = 0
\end{cases}$$

**Newton direction:** Chọn element from $$\partial F(x)$$.

---

**c) Convergence:**

**Semismooth:** $$\|F(x + d) - F(x) - V_x d\| = o(\|d\|)$$

với $$V_x \in \partial F(x)$$.

**Result:** Superlinear convergence như smooth Newton!

</details>

---

## 📝 **Bài tập 4: Regularization Path**

Track solution $$x^*(\lambda)$$ khi $$\lambda$$ varies.

**Yêu cầu:**  
a) Derive path derivative $$\frac{dx^*}{d\lambda}$$  
b) Predict new solution  
c) Apply warm-start

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Implicit differentiation:**

KKT: $$\nabla f(x^*) + \lambda v^* = 0$$ với $$v^* \in \partial g(x^*)$$

Differentiate w.r.t. $$\lambda$$:

$$\nabla^2 f(x^*) \frac{dx^*}{d\lambda} + v^* + \lambda \frac{dv^*}{d\lambda} = 0$$

On active set ($$v^*$$ smooth):

$$\frac{dx^*}{d\lambda} = -(\nabla^2 f)^{-1} v^*$$

---

**b) Prediction:**

$$x^*(\lambda + \Delta\lambda) \approx x^*(\lambda) + \frac{dx^*}{d\lambda} \Delta\lambda$$

$$= x^*(\lambda) - (\nabla^2 f)^{-1} v^* \Delta\lambda$$

---

**c) Warm-start:**

Use prediction as initial point for $$\lambda + \Delta\lambda$$.

**Fewer iterations needed!**

</details>

---

## 📝 **Bài tập 5: Adaptive Regularization**

Adjust $$\lambda$$ trong inner loop.

**Yêu cầu:**  
a) Levenberg-Marquardt style: $$\nabla^2 f + \mu I$$  
b) Choose $$\mu$$ based on reduction ratio  
c) Compare với fixed Hessian

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Modified subproblem:**

$$\min_d \left\{ \frac{1}{2}d^T(\nabla^2 f + \mu I)d + \nabla f^T d + g(x + d) \right\}$$

$$\mu > 0$$ ensures PD.

---

**b) Trust region logic:**

$$\rho = \frac{\text{actual reduction}}{\text{predicted reduction}}$$

- $$\rho > 0.75$$: decrease $$\mu$$ (closer to Newton)
- $$\rho < 0.25$$: increase $$\mu$$ (closer to GD)

---

**c) Benefits:**

**Fixed Hessian:** May fail if $$\nabla^2 f$$ indefinite.

**Adaptive $$\mu$$:** Guaranteed descent, robust.

</details>

---

## 💡 **Tổng kết**

| Method | Key Feature | Best for |
|--------|-------------|----------|
| Proximal Newton | Quadratic model + prox | $$\ell_1$$, group sparsity |
| Active set | Fix signs, smooth Newton | LASSO path |
| Semismooth | Generalized Jacobian | Non-differentiable |
| Regularized | $$\nabla^2 f + \mu I$$ | Ill-conditioned |

---

## 📚 **Tài liệu Tham khảo**

1. Lee, J. D., et al. (2014). "Proximal Newton-type methods". *NeurIPS*.
2. Rakotomamonjy, A., et al. (2016). "Efficient Proximal Newton". *ICML*.

