---
layout: post
title: 04-03 Optimality conditions
chapter: '04'
order: 4
owner: YoungJae Choung
categories:
- chapter04
lang: en
lesson_type: required
---

In single-variable calculus, you learn one reflex: set $$f'(x) = 0$$. The moment constraints enter the picture, that reflex breaks—a ball resting against the wall of a tilted bowl stops moving even though gravity still pulls downhill! The first-order optimality condition for constrained convex optimization replaces "$$f'(x) = 0$$" with a sharper geometric law: at the optimum, no feasible direction points downhill.

## Key ideas: First-Order Variational Optimality

1. **Feasible Directions and the Variational Inequality**: For a differentiable convex function $$f$$ over a convex set $$C$$, a point $$x^\star \in C$$ is globally optimal if and only if $$\nabla f(x^\star)^T (y - x^\star) \ge 0$$ for all $$y \in C$$. Because $$y - x^\star$$ is the direction toward any other feasible point, the directional derivative along every feasible ray must be nonnegative.
2. **Normal Cone Geometry**: Rewriting the inequality as $$(-\nabla f(x^\star))^T (y - x^\star) \le 0$$ for all $$y \in C$$ means that the negative gradient $$-\nabla f(x^\star)$$ makes an obtuse (or right) angle with every feasible displacement—equivalently, $$-\nabla f(x^\star) \in N_C(x^\star)$$, the normal cone of $$C$$ at $$x^\star$$.
3. **Recovering Classic Special Cases**:
   - *Unconstrained* ($$C = \mathbb{R}^n$$): $$y - x^\star$$ can point in any direction, forcing $$\nabla f(x^\star) = 0$$.
   - *Affine equality* ($$C = \{x : Ax = b\}$$): feasible displacements lie in $$\operatorname{null}(A)$$, forcing $$\nabla f(x^\star) \perp \operatorname{null}(A)$$, i.e., $$\nabla f(x^\star) = A^T \nu$$ for some Lagrange multiplier $$\nu$$.
   - *Nonnegative orthant* ($$C = \mathbb{R}^n_+$$): yields the complementarity triad $$x^\star \ge 0$$, $$\nabla f(x^\star) \ge 0$$, and $$x_i^\star \nabla_i f(x^\star) = 0$$.
4. **Necessity AND Sufficiency**: In nonconvex optimization, $$\nabla f(x^\star)^T (y - x^\star) \ge 0$$ is only necessary (saddle points satisfy it too). Convexity supplies the global linear underestimator $$f(y) \ge f(x^\star) + \nabla f(x^\star)^T(y - x^\star)$$, immediately upgrading the condition to both necessary and sufficient for global optimality.

### Worked example: Certifying Optimality on the Nonnegative Orthant

Minimize $$f(x_1, x_2) = (x_1 + 1)^2 + (x_2 - 2)^2$$ subject to $$x_1 \ge 0,\; x_2 \ge 0$$ (so $$C = \mathbb{R}^2_+$$).

1. **Compute the gradient**:
   $$\nabla f(x) = \begin{bmatrix} 2(x_1 + 1) \\ 2(x_2 - 2) \end{bmatrix}.$$
2. **Apply the nonnegative orthant optimality conditions** ($$x_i \ge 0$$, $$\nabla_i f(x) \ge 0$$, $$x_i \nabla_i f(x) = 0$$):
   - For $$i = 1$$: since $$x_1 \ge 0$$, we always have $$2(x_1 + 1) \ge 2 > 0$$. Complementary slackness $$x_1 \cdot 2(x_1 + 1) = 0$$ forces $$x_1^\star = 0$$.
   - For $$i = 2$$: setting $$\nabla_2 f(x) = 2(x_2 - 2) = 0$$ gives $$x_2^\star = 2 \ge 0$$, which satisfies all three conditions ($$2 \ge 0$$, $$0 \ge 0$$, $$2 \cdot 0 = 0$$).
3. **Evaluate the gradient at $$x^\star = (0, 2)$$**:
   $$\nabla f(0, 2) = \begin{bmatrix} 2 \\ 0 \end{bmatrix}, \quad -\nabla f(0, 2) = \begin{bmatrix} -2 \\ 0 \end{bmatrix}.$$
4. **Verify the variational inequality directly for every $$y \in \mathbb{R}^2_+$$**:
   $$\nabla f(x^\star)^T (y - x^\star) = 2(y_1 - 0) + 0(y_2 - 2) = 2y_1 \ge 0 \quad \text{since } y_1 \ge 0.$$
   Geometrically, the negative gradient $$(-2, 0)$$ pushes straight into the left wall $$x_1 = 0$$, so the feasible set completely blocks any further descent.

## First order optimality condition

For more background on convex functions, see [Chapter 3: Key Properties of Convex Functions]({% multilang_post_url contents/chapter03/21-02-12-03_01_03_key_properties_of_convex_functions %}).

>$$
\begin{aligned}
&\min_x &&f(x) \\
&\text{subject to} &&x \in C
\end{aligned}
$$

For a convex problem where the objective function $$f$$ is **differentiable**, the following condition is necessary and sufficient for an optimal point $$x$$:

> $$\nabla f(x)^{T}(y-x) \geq 0 \\
> \text{ for all } y \in C$$

This is called the *first-order condition for optimality*. 

$$\nabla f(x)^{T}(y-x) = 0$$ defines a hyperplane passing through $$x$$ in set $$C$$, and $$- \nabla f(x)$$ points in the direction of movement toward the optimal point $$x$$. <br><br>

If the above condition is satisfied, 
set $$C$$ is contained in the half-space opposite to $$- \nabla f(x)$$, 
so $$x$$ is an optimal point.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter04/first-order-condition.png" alt="[Fig1] geometric interpretation of first-order condition for optimality [3]">
  <figcaption style="text-align: center;">[Fig1] geometric interpretation of first-order condition for optimality [3]</figcaption>
</p>
</figure>
<br>

### Important special case
When $$C = \mathbb{R}^n$$ (unconstrained optimization),
the optimality condition is:
> $$\nabla f(x) = 0$$

In this case every direction in $$\mathbb{R}^n$$ is feasible. Whenever $$\nabla f(x) \ne 0$$, the direction $$-\nabla f(x)$$ is a descent direction (it decreases $$f$$ locally, although it need not point straight at a minimizer), so $$\nabla f(x) = 0$$ means there is no direction left that decreases $$f$$ at $$x$$.

---


## Mathematical Foundation

While first-order conditions use the gradient $$\nabla f(x)$$, second-order conditions utilize the **Hessian matrix**:

$$H_f(x) = \nabla^2 f(x) = \begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}$$

The Hessian captures the **curvature** of the function at point $$x$$, providing information about the local shape of the objective function.

## Second-Order Optimality Conditions

Consider the unconstrained optimization problem:
$$\min_x f(x)$$

where $$f: \mathbb{R}^n \to \mathbb{R}$$ is twice continuously differentiable.

### Necessary Conditions (Second-Order)

If $$x^*$$ is a local minimum of $$f$$, then:

1. **First-order necessary condition**: $$\nabla f(x^*) = 0$$
2. **Second-order necessary condition**: $$\nabla^2 f(x^*) \succeq 0$$ (positive semidefinite)

### Sufficient Conditions (Second-Order)

If at point $$x^*$$:

1. $$\nabla f(x^*) = 0$$ (first-order condition)
2. $$\nabla^2 f(x^*) \succ 0$$ (positive definite)

Then $$x^*$$ is a **strict local minimum** of $$f$$.

## Understanding Positive Definiteness

A symmetric matrix $$A$$ is:
- **Positive definite** ($$A \succ 0$$) if $$v^T A v > 0$$ for all $$v \neq 0$$
- **Positive semidefinite** ($$A \succeq 0$$) if $$v^T A v \geq 0$$ for all $$v$$

**Practical tests for positive definiteness:**
1. **Eigenvalue test**: All eigenvalues are positive
2. **Leading principal minors**: All leading principal minors are positive
3. **Cholesky decomposition**: $$A = L L^T$$ exists with $$L$$ lower triangular

## Geometric Interpretation

The second-order conditions provide information about the **curvature** at the critical point:

- **$$\nabla^2 f(x^*) \succ 0$$**: The function curves upward in all directions → **strict local minimum**
- **$$\nabla^2 f(x^*) \prec 0$$**: The function curves downward in all directions → **strict local maximum**  
- **$$\nabla^2 f(x^*) \succeq 0$$**: Non-negative curvature → **possible minimum**
- **Indefinite Hessian**: Mixed curvature → **saddle point**

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter04/second-order-conditions.png" alt="Second-order optimality conditions visualization" width="80%" height="80%">
 <figcaption style="text-align: center;">[Fig1] Geometric interpretation of second-order conditions</figcaption>
</p>
</figure>

## Detailed Examples

### Example 1: Quadratic Function
Consider $$f(x_1, x_2) = x_1^2 + 2x_2^2 + x_1 x_2$$

**Step 1: Find critical points**
$$\nabla f(x) = \begin{bmatrix} 2x_1 + x_2 \\ 4x_2 + x_1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

Solving: $$x^* = (0, 0)$$

**Step 2: Compute Hessian**
$$\nabla^2 f(x) = \begin{bmatrix} 2 & 1 \\ 1 & 4 \end{bmatrix}$$

**Step 3: Check positive definiteness**
- Eigenvalues: $$\lambda_1 = \frac{6 + \sqrt{8}}{2} = 3 + \sqrt{2} > 0$$, $$\lambda_2 = \frac{6 - \sqrt{8}}{2} = 3 - \sqrt{2} > 0$$
- Leading principal minors: $$2 > 0$$, $$\det = 8 - 1 = 7 > 0$$

**Conclusion**: $$\nabla^2 f(0,0) \succ 0$$ → $$(0,0)$$ is a strict local minimum.

### Example 2: Non-Convex Function
Consider $$f(x_1, x_2) = x_1^4 + x_2^4 - 2x_1^2 - 2x_2^2$$

**Step 1: Find critical points**
$$\nabla f(x) = \begin{bmatrix} 4x_1^3 - 4x_1 \\ 4x_2^3 - 4x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

Critical points: $$(0,0)$$, $$(\pm 1, 0)$$, $$(0, \pm 1)$$, $$(\pm 1, \pm 1)$$

**Step 2: Analyze $$(0,0)$$**
$$\nabla^2 f(0,0) = \begin{bmatrix} -4 & 0 \\ 0 & -4 \end{bmatrix} \prec 0$$

**Conclusion**: $$(0,0)$$ is a strict local maximum.

**Step 3: Analyze $$(1,1)$$**
$$\nabla^2 f(1,1) = \begin{bmatrix} 8 & 0 \\ 0 & 8 \end{bmatrix} \succ 0$$

**Conclusion**: $$(1,1)$$ is a strict local minimum.

### Example 3: Saddle Point
Consider $$f(x_1, x_2) = x_1^2 - x_2^2$$

**Analysis at $$(0,0)$$:**
- $$\nabla f(0,0) = (0,0)$$ ✓
- $$\nabla^2 f(0,0) = \begin{bmatrix} 2 & 0 \\ 0 & -2 \end{bmatrix}$$ (indefinite)

**Conclusion**: $$(0,0)$$ is a saddle point (neither minimum nor maximum).

## Constrained Optimization: Second-Order Conditions

For constrained problems:
$$\min_x f(x) \text{ subject to } h_i(x) = 0, \, i = 1,\ldots,m$$

The **bordered Hessian** of the Lagrangian is used:
$$\mathcal{L}(x,\lambda) = f(x) + \sum_{i=1}^m \lambda_i h_i(x)$$

**Second-order sufficient condition**: The bordered Hessian has the correct inertia (number of negative eigenvalues equals the number of constraints).

## Comparison: First vs Second-Order Conditions

| Aspect | First-Order | Second-Order |
|--------|-------------|--------------|
| **Information** | Gradient (slope) | Hessian (curvature) |
| **Necessary condition** | $$\nabla f(x^*) = 0$$ | $$\nabla f(x^*) = 0$$ and $$\nabla^2 f(x^*) \succeq 0$$ |
| **Sufficient condition (unconstrained)** | Not sufficient for general $$f$$ (sufficient if $$f$$ is convex) | $$\nabla f(x^*) = 0$$ and $$\nabla^2 f(x^*) \succ 0$$ |
| **Strength** | Weaker | Stronger |
| **Computational cost** | $$O(n)$$ | $$O(n^2)$$ |
| **Distinguishes** | Critical points | Minima, maxima, saddle points |

## Interactive Visualization

Explore how second-order conditions work in practice:

<div style="text-align: center; margin: 20px 0;">
    <a href="../second_order_conditions_interactive.html" target="_blank" 
       style="display: inline-block; padding: 12px 24px; background-color: #e74c3c; color: white; text-decoration: none; border-radius: 6px; font-weight: bold; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
        🎯 Launch Second-Order Conditions Explorer
    </a>
</div>

The interactive tool demonstrates:
- **Hessian eigenvalue analysis** for different function types
- **Visual classification** of critical points (minimum, maximum, saddle)
- **Contour plots** showing local curvature behavior
- **Step-by-step calculations** for second-order tests

### The first-order optimality condition in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/first-order-optimality_en.mp4"></video>
</div>

∇f(x*)ᵀ(y − x*) ≥ 0 on a triangle: checking at the vertices, the normal cone, projected gradient, a vertex solution, and the 9 stationary points of the nonconvex example.

## Summary and Key Takeaways

Second-order optimality conditions provide **stronger characterization** of optimal points:

### **Key Results:**
1. **Necessary conditions**: $$\nabla f(x^*) = 0$$ and $$\nabla^2 f(x^*) \succeq 0$$
2. **Sufficient conditions**: $$\nabla f(x^*) = 0$$ and $$\nabla^2 f(x^*) \succ 0$$
3. **Classification power**: Can distinguish between minima, maxima, and saddle points

### **Practical Importance:**
- **Algorithm design**: Foundation for Newton-type methods
- **Convexity analysis**: Essential for verifying convex functions
- **Robustness**: Stronger guarantees than first-order conditions alone
- **Optimization theory**: Bridge between local and global optimality

### **Computational Considerations:**
- **Cost**: $$O(n^2)$$ storage and computation for Hessian
- **Approximation**: Quasi-Newton methods reduce computational burden
- **Numerical stability**: Eigenvalue computations require careful implementation

Understanding second-order conditions is essential for advanced optimization theory and the development of efficient numerical algorithms. They provide the mathematical foundation for many modern optimization methods and offer deeper insights into the structure of optimization problems.
