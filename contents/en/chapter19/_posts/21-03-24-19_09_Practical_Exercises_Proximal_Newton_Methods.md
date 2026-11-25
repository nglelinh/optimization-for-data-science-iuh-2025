---
layout: post
title: '19-09 Practical Exercises - Proximal Newton Methods'
chapter: '19'
order: 13
owner: GitHub Copilot
lang: en
categories:
- chapter19
lesson_type: required
redirect_from:
  - /contents/en/chapter19/19_08_Practical_Exercises_Proximal_Newton_Methods/
---

When you move from 1D textbook examples to 2D or $$p$$-dimensional composite problems, the biggest practical hurdle is solving the **inner scaled proximal subproblem** $$\min_v g^T v + \frac{1}{2} v^T H v + \lambda\|x + v\|_1$$ when $$H$$ has off-diagonal entries. Before tackling the exercises below, walk through this concrete 2D warm-up showing how cyclic coordinate descent solves a coupled scaled prox in closed-form scalar steps—the exact inner loop inside `glmnet` and `QUIC`.

## Background Knowledge Map: Core Skills for the Proximal Newton Exercises

- **Formulating the Subproblem:** Extract $$\nabla g(x^k)$$ and $$H_k = \nabla^2 g(x^k)$$ cleanly, then write the composite quadratic model in either displacement form ($$v$$) or next-iterate form ($$z = x^k + v$$).
- **Solving Coupled Scaled Prox via Coordinate Descent:** Holding all coordinates $$v_j \; (j \neq i)$$ fixed turns coordinate $$i$$'s subproblem into a 1D soft-thresholding step with denominator $$H_{ii}$$.
- **Backtracking & Convergence Diagnostics:** Implement the single-prox backtracking check $$f(x + tv) \le f(x) + \alpha t \nabla g(x)^T v + \alpha(h(x + tv) - h(x))$$ and verify quadratic error contraction on log-scale plots.
- **Projected Newton Safeguards:** Recognize when binding-set diagonalization is needed for box constraints $$x \ge 0$$ to prevent Euclidean projection from destroying descent.

### Step-by-Step Worked Example (Read Slowly): One Coordinate-Descent Sweep on a Coupled 2D Scaled Prox

Suppose at $$x = (0, 0)^T$$ we must solve the coupled proximal Newton subproblem with $$\nabla g(0) = (-3, -3)^T$$, $$H = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$, and $$h(v) = |v_1| + |v_2|$$:
$$\min_{v_1, v_2} \; -3v_1 - 3v_2 + v_1^2 + v_1 v_2 + v_2^2 + |v_1| + |v_2|.$$

1. **Update coordinate $$v_1$$ (holding $$v_2 = 0$$):**
   $$\min_{v_1} \; (-3 + 1 \cdot 0)v_1 + \frac{1}{2}(2)v_1^2 + |v_1| \implies v_1 = S_{1/2}\!\left(\frac{3 - 0}{2}\right) = S_{0.5}(1.5) = 1.0.$$
2. **Update coordinate $$v_2$$ (holding $$v_1 = 1.0$$):**
   The linear term shifts to $$-3 + H_{21} v_1 = -3 + 1(1.0) = -2$$:
   $$\min_{v_2} \; -2v_2 + \frac{1}{2}(2)v_2^2 + |v_2| \implies v_2 = S_{1/2}\!\left(\frac{2}{2}\right) = S_{0.5}(1.0) = 0.5.$$
3. **Compare with the exact subproblem solution:**
   By symmetry, the exact solution satisfies $$2v^\star + v^\star - 3 + 1 = 0 \implies v_1^\star = v_2^\star = \frac{2}{3} \approx 0.667$$. Just *one* coordinate sweep brought $$(0, 0) \to (1.0, 0.5)$$, and a second sweep gives $$(0.75, 0.625)$$—converging geometrically in microseconds without ever inverting $$H$$! Now dive into the exercises below.

# Practical Exercises - Proximal Newton Methods

The exercises are adapted from Lee et al. (2014) and Rakotomamonjy et al. (2016).

---

## 📝 **Exercise 1: Proximal Newton Step**

Given $$f(x) + g(x)$$ with $$f(x) = x^2$$, $$g(x) = |x|$$.

**Tasks:**  
a) Write the proximal Newton subproblem  
b) Solve it at $$x^{(k)} = 2$$  
c) Compare with proximal gradient

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Proximal Newton:**

$$x^{(k+1)} = \arg\min_x \left\{ f(x^{(k)}) + \nabla f(x^{(k)})^T(x - x^{(k)}) + \frac{1}{2}(x - x^{(k)})^T \nabla^2 f(x^{(k)})(x - x^{(k)}) + g(x) \right\}$$

$$= \arg\min_x \left\{ \frac{H_k}{2}(x - x^{(k)})^2 + \nabla f(x^{(k)})(x - x^{(k)}) + g(x) \right\}$$

---

**b) At $$x^{(k)} = 2$$:**

$$\nabla f(2) = 4$$, $$\nabla^2 f(2) = 2$$

$$\min_x \left\{ (x - 2)^2 + 4(x - 2) + |x| \right\}$$

$$= \min_x \left\{ x^2 - 4x + 4 + 4x - 8 + |x| \right\}$$

$$= \min_x \left\{ x^2 - 4 + |x| \right\}$$

**Case 1:** $$x \geq 0$$: $$\min x^2 + x - 4$$, the unconstrained minimizer is $$x = -0.5$$ (infeasible)

**Case 2:** $$x < 0$$: $$\min x^2 - x - 4$$, the unconstrained minimizer is $$x = 0.5$$ (infeasible)

**Check the boundary:** $$x = 0$$: $$-4$$

**Optimal:** $$x^{(1)} = 0$$

---

**c) Proximal GD:**

$$x^{(k+1)} = \text{prox}_{t|·|}(x^{(k)} - t\nabla f(x^{(k)}))$$

$$= \text{prox}_{t|·|}(2 - 4t) = S_t(2 - 4t)$$

With $$t = 0.5$$: $$S_{0.5}(0) = 0$$

**Same result!** (for this simple case)

</details>

---

## 📝 **Exercise 2: LASSO Proximal Newton**

$$\min \frac{1}{2}\|Ax - b\|^2 + \lambda\|x\|_1$$

**Tasks:**  
a) Identify the active/inactive variables  
b) Apply Newton on the active set  
c) Handle sign changes

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Active set:**

$$\mathcal{A} = \{i : x_i \neq 0\}$$, $$\mathcal{I} = \{i : x_i = 0\}$$

**KKT:** $$\nabla f(x) + \lambda \cdot \text{sign}(x) = 0$$ on $$\mathcal{A}$$

---

**b) Newton on $$\mathcal{A}$$:**

$$\min_{x_{\mathcal{A}}} \frac{1}{2}\|A_{\mathcal{A}}x_{\mathcal{A}} - b\|^2 + \lambda\|x_{\mathcal{A}}\|_1$$

with $$\text{sign}(x_{\mathcal{A}})$$ fixed:

$$\nabla^2 f_{\mathcal{A}} \Delta x = -\nabla f_{\mathcal{A}} - \lambda \cdot \text{sign}(x_{\mathcal{A}})$$

$$\Delta x = -(A_{\mathcal{A}}^T A_{\mathcal{A}})^{-1}(A_{\mathcal{A}}^T(A_{\mathcal{A}}x - b) + \lambda \cdot \text{sign}(x_{\mathcal{A}}))$$

---

**c) Sign changes:**

If $$x_i^{\text{new}} \cdot x_i^{\text{old}} < 0$$ → truncate the step:

$$\alpha_{\max} = \min_{i:\, x_i^{\text{old}} \Delta x_i < 0} \frac{-x_i^{\text{old}}}{\Delta x_i}$$

**Safe update:** $$x^{(k+1)} = x^{(k)} + 0.99\,\min(1, \alpha_{\max}) \Delta x$$

</details>

---

## 📝 **Exercise 3: Semismooth Newton**

Given $$F(x) = \nabla f(x) + \partial g(x) \ni 0$$.

**Tasks:**  
a) Define the generalized Jacobian  
b) Apply it to $$g(x) = \|x\|_1$$  
c) Show superlinear convergence

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Generalized Jacobian:**

$$\partial F(x) = \nabla^2 f(x) + \partial^2 g(x)$$

where $$\partial^2 g$$ is a set-valued second derivative (informal notation; in practice one works with the generalized Jacobian of the proximal-map residual).

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

**Newton direction:** choose an element of $$\partial F(x)$$.

---

**c) Convergence:**

**Semismooth:** $$\|F(x + d) - F(x) - V_x d\| = o(\|d\|)$$

with $$V_x \in \partial F(x)$$.

**Result:** superlinear convergence, as for the smooth Newton method!

</details>

---

## 📝 **Exercise 4: Regularization Path**

Track the solution $$x^*(\lambda)$$ as $$\lambda$$ varies.

**Tasks:**  
a) Derive the path derivative $$\frac{dx^*}{d\lambda}$$  
b) Predict the new solution  
c) Apply warm-start

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Implicit differentiation:**

KKT: $$\nabla f(x^*) + \lambda v^* = 0$$ with $$v^* \in \partial g(x^*)$$

Differentiate with respect to $$\lambda$$:

$$\nabla^2 f(x^*) \frac{dx^*}{d\lambda} + v^* + \lambda \frac{dv^*}{d\lambda} = 0$$

On the active set ($$v^* = \text{sign}(x^*)$$ is locally constant, so $$\frac{dv^*}{d\lambda} = 0$$):

$$\frac{dx^*_{\mathcal{A}}}{d\lambda} = -(\nabla^2 f_{\mathcal{A}\mathcal{A}})^{-1} v^*_{\mathcal{A}}$$

---

**b) Prediction:**

$$x^*(\lambda + \Delta\lambda) \approx x^*(\lambda) + \frac{dx^*}{d\lambda} \Delta\lambda$$

$$= x^*(\lambda) - (\nabla^2 f)^{-1} v^* \Delta\lambda$$

---

**c) Warm-start:**

Use the prediction as the initial point for $$\lambda + \Delta\lambda$$.

**Fewer iterations needed!**

</details>

---

## 📝 **Exercise 5: Adaptive Regularization**

Adjust the regularization in the inner loop.

**Tasks:**  
a) Levenberg-Marquardt style: $$\nabla^2 f + \mu I$$  
b) Choose $$\mu$$ based on the reduction ratio  
c) Compare with a fixed Hessian

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Modified subproblem:**

$$\min_d \left\{ \frac{1}{2}d^T(\nabla^2 f + \mu I)d + \nabla f^T d + g(x + d) \right\}$$

$$\mu > 0$$ ensures positive definiteness.

---

**b) Trust-region logic:**

$$\rho = \frac{\text{actual reduction}}{\text{predicted reduction}}$$

- $$\rho > 0.75$$: decrease $$\mu$$ (closer to Newton)
- $$\rho < 0.25$$: increase $$\mu$$ (closer to GD)

---

**c) Benefits:**

**Fixed Hessian:** may fail if $$\nabla^2 f$$ is indefinite.

**Adaptive $$\mu$$:** guaranteed descent, robust.

</details>

---

## 💡 **Summary**

| Method | Key Feature | Best for |
|--------|-------------|----------|
| Proximal Newton | Quadratic model + prox | $$\ell_1$$, group sparsity |
| Active set | Fix signs, smooth Newton | LASSO path |
| Semismooth | Generalized Jacobian | Non-differentiable |
| Regularized | $$\nabla^2 f + \mu I$$ | Ill-conditioned |

---

## 📚 **References**

1. Lee, J. D., et al. (2014). "Proximal Newton-type methods". *NeurIPS*.
2. Rakotomamonjy, A., et al. (2016). "Efficient Proximal Newton". *ICML*.
