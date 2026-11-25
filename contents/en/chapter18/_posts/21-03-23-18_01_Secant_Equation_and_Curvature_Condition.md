---
layout: post
title: 18-01 Secant Equation and Curvature Condition
chapter: '18'
order: '2'
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

In single-variable calculus, when you do not know the second derivative $$f''(x)$$, you approximate it by the slope of the secant line connecting two gradients: $$b_{k+1} = \frac{f'(x^{k+1}) - f'(x^k)}{x^{k+1} - x^k}$$. Lifting that elementary ratio to $$\mathbb{R}^n$$ yields the **secant equation** $$B_{k+1} s_k = y_k$$—a linear system that is *wildly* underdetermined in high dimensions (only $$n$$ equations for $$n(n+1)/2$$ symmetric entries) and has a positive-definite solution if and only if the **curvature condition** $$y_k^T s_k > 0$$ holds.

## Key ideas: Geometry of the Secant & Curvature Conditions

- **Multivariate Secant Equation ($$B_{k+1} s_k = y_k$$):** By Taylor's theorem, $$y_k = \nabla f(x^{k+1}) - \nabla f(x^k) = \left(\int_0^1 \nabla^2 f(x^k + \tau s_k)\,d\tau\right) s_k$$. Requiring $$B_{k+1} s_k = y_k$$ forces our Hessian model to match the exact *average* curvature along the most recent step $$s_k$$.
- **Why $$B_{k+1}$$ Is Underdetermined:** In $$\mathbb{R}^n$$, symmetry leaves $$\frac{n(n+1)}{2}$$ unknowns while $$B_{k+1} s_k = y_k$$ supplies only $$n$$ scalar equations. Different quasi-Newton updates (SR1, DFP, BFGS) differ purely in *how* they resolve the remaining $$\frac{n(n-1)}{2}$$ degrees of freedom (e.g., minimum Frobenius-norm change from $$B_k$$).
- **The Curvature Condition ($$y_k^T s_k > 0$$):** If $$B_{k+1} \succ 0$$ satisfies $$B_{k+1} s_k = y_k$$, then necessarily $$s_k^T y_k = s_k^T B_{k+1} s_k > 0$$. Conversely, whenever $$y_k^T s_k > 0$$, infinitely many SPD matrices satisfy the secant equation.
- **Line Search as the Guardian of Positive Definiteness:** For strictly convex functions, $$y_k^T s_k > 0$$ holds automatically; for nonconvex objectives, enforcing the **Wolfe curvature condition** $$\nabla f(x^{k+1})^T s_k \ge c_2 \nabla f(x^k)^T s_k$$ (with $$c_2 \in (0, 1)$$) guarantees $$y_k^T s_k \ge (c_2 - 1)\nabla f(x^k)^T s_k > 0$$ whenever $$s_k$$ is a descent direction.

### Worked example: Checking the Secant & Curvature Conditions

**Part A (Convex 2D quadratic):** Let $$f(x) = \frac{1}{2}x_1^2 + 2x_2^2 + x_1 x_2$$, so $$\nabla f(x) = \begin{bmatrix} x_1 + x_2 \\ x_1 + 4x_2 \end{bmatrix}$$. Suppose we step from $$x^0 = (1, 1)^T$$ to $$x^1 = (0, 0.5)^T$$.

1. **Compute displacement $$s_0$$ and gradient difference $$y_0$$:**
   $$s_0 = x^1 - x^0 = \begin{bmatrix} -1 \\ -0.5 \end{bmatrix}, \qquad \nabla f(x^0) = \begin{bmatrix} 2 \\ 5 \end{bmatrix}, \quad \nabla f(x^1) = \begin{bmatrix} 0.5 \\ 2 \end{bmatrix} \implies y_0 = \begin{bmatrix} -1.5 \\ -3 \end{bmatrix}.$$
2. **Verify the curvature condition:**
   $$y_0^T s_0 = (-1.5)(-1) + (-3)(-0.5) = 1.5 + 1.5 = 3.0 > 0.$$
   Because $$y_0^T s_0 > 0$$, an SPD secant matrix exists—for example, the true Hessian $$Q = \begin{bmatrix} 1 & 1 \\ 1 & 4 \end{bmatrix}$$ satisfies $$Q s_0 = \begin{bmatrix} -1.5 \\ -3 \end{bmatrix} = y_0$$, and even the diagonal matrix $$D = \operatorname{diag}(1.5, 6)$$ satisfies $$D s_0 = y_0$$!

**Part B (Nonconvex breakdown):** Now test $$g(x) = x^3 - 3x$$ ($$g'(x) = 3x^2 - 3$$) from $$x^0 = -1$$ to $$x^1 = 0$$.
- $$s_0 = 1$$, $$y_0 = g'(0) - g'(-1) = -3 - 0 = -3$$.
- Here $$y_0^T s_0 = -3 < 0$$ because $$g$$ is *concave* on $$[-1, 0]$$. No positive-definite $$B_1 > 0$$ can satisfy $$B_1(1) = -3$$, which is why BFGS either relies on a Wolfe line search to avoid this region or skips the update.

# Secant Equation

As mentioned earlier, $$B$$ is a matrix that approximates $$\nabla^2 f(x)$$. For the matrix $$B$$ to have properties similar to the Hessian $$\nabla^2 f(x)$$, it must satisfy a condition called the secant equation.

When $$x^{k+1} = x^k + s^k$$ and $$f$$ is twice differentiable, the first-order Taylor expansion of $$\nabla f(x^k + s^k)$$ shows that the true Hessian has the following property.

>$$
>\nabla f(x^k + s^k) \approx \nabla f(x^k) + \nabla^2 f(x^k) s^k
>$$

Here, we call the approximation matrix of $$\nabla^2 f(x^k)$$ as $$B^{k+1}$$. This matrix satisfies the following equation.

>$$
>\nabla f(x^k + s^k) = \nabla f(x^k) + B^{k+1} s^k
>$$

If $$x^{k+1} = x^k + s^k$$ and $$y^k = \nabla f(x^{k+1}) - \nabla f(x^k)$$, the equation above can be rearranged as follows, and this is called the secant equation.

>$$
>B^{k+1} s^k = y^k
>$$

# The Intuition of the Secant Equation

When $$x$$ is the horizontal axis and $$\nabla f(x)$$ is the vertical axis, $$B^{k+1}$$ equals the slope of the line through the two points $$(x^k, \nabla f(x^k))$$ and $$(x^{k+1}, \nabla f(x^{k+1}))$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter18/intuition_of_secant_eq.png" alt="[Fig1] The intuition of the secant equation" width="70%">
  <figcaption style="text-align: center;">[Fig1] The intuition of the secant equation</figcaption>
</p>
</figure>

# Conditions to Determine the Matrix $$B^+$$

Starting from the current matrix $$B$$, there are three conditions for computing the next matrix $$B^+$$.

1. $$B^+$$ is symmetric: because it is an approximation of the Hessian.
2. $$B^+$$ is close to $$B$$: a condition that determines a unique $$B^+$$. Since $$B$$ already contains useful information, we choose the matrix closest to $$B$$ among those $$B^+$$ that satisfy the secant equation.
3. $$B$$ is positive definite $$\Rightarrow B^+$$ is positive definite: to guarantee a global optimum, we maintain the convexity of the problem. (reference: [Analyzing the Hessian](https://web.stanford.edu/group/sisl/k12/optimization/MO-unit4-pdfs/4.10applicationsofhessians.pdf))

# Curvature Condition

The fact that $$B^+$$ is positive definite and $$B^+ s = y$$ implies the following.

>$$
>s^T y = s^T B^+ s > 0.
>$$

(reference: [Positive-definite matrix on Wikipedia](https://en.wikipedia.org/wiki/Positive-definite_matrix))

Here, $$s^T y > 0$$ is called the curvature condition. If the curvature condition is satisfied, the secant equation $$B^+ s = y$$ always has a solution $$B^+$$.
