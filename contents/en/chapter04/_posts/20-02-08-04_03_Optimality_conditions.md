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

## First order optimality condition

For more background on convex functions, see [Chapter 3: Key Properties of Convex Functions]({% multilang_post_url contents/chapter03/20-02-08-03_01_key_properties_of_convex_functions %}).

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

In this case, $$-\nabla f(x)$$ points toward the optimal point $$x$$, and $$\nabla f(x) = 0$$ means there is no further direction to move to decrease $$f$$ at $$x$$.

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
- Eigenvalues: $$\lambda_1 = \frac{6 + \sqrt{12}}{2} > 0$$, $$\lambda_2 = \frac{6 - \sqrt{12}}{2} > 0$$
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
| **Sufficient condition** | Not available for unconstrained | $$\nabla f(x^*) = 0$$ and $$\nabla^2 f(x^*) \succ 0$$ |
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
