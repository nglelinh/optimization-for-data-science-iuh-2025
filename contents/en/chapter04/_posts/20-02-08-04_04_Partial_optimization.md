---
layout: post
title: 04-04 Partial optimization
chapter: '04'
order: 5
owner: YoungJae Choung
categories:
- chapter04
lang: en
---

Suppose you are designing a supply chain with two kinds of decisions: *strategic* decisions (where to build warehouses, $$x$$) and *operational* decisions (how much to ship from each warehouse once built, $$y$$). If you optimize the shipping plan $$y$$ for every candidate warehouse layout $$x$$, does the resulting cost-as-a-function-of-$$x$$ remain convex? Remarkably, yes—partial minimization over a convex block of variables always preserves convexity, letting you eliminate auxiliary variables cleanly or reveal the hidden hinge-loss structure of models like Support Vector Machines.

## Background Knowledge Map: Partial Minimization and Variable Elimination

1. **Convexity Preservation Under Infimal Projection**: If $$f(x, y)$$ is *jointly convex* in $$(x, y)$$ and $$C$$ is a convex set, then the marginal function $$g(x) = \inf_{y \in C} f(x, y)$$ is convex in $$x$$ (provided $$g(x) > -\infty$$). Geometrically, the epigraph of $$g$$ is the projection of the convex epigraph of $$f$$ onto the $$(x, t)$$ subspace, and linear projections of convex sets are always convex.
2. **Equivalence of Joint and Two-Stage Problems**: Minimizing $$f(x, y)$$ jointly over $$(x, y)$$ with constraints on $$y$$ is equivalent to first minimizing over $$y$$ (treating $$x$$ as fixed) to obtain $$g(x)$$, and then minimizing $$g(x)$$ over $$x$$. You can run this trick in *both* directions: eliminate variables to get a compact unconstrained form (like SVM hinge loss), or introduce variables to smooth out a nonsmooth objective (like epigraph variables).
3. **Why Joint Convexity Is Essential**: It is *not* enough for $$f(x, y)$$ to be convex in $$x$$ for each fixed $$y$$ and convex in $$y$$ for each fixed $$x$$ (separate convexity). For example, $$f(x, y) = xy$$ is linear in each variable separately, yet not jointly convex. Always verify joint convexity before projecting out $$y$$.
4. **Canonical ML Example — Soft-Margin SVM**: Introducing slack variables $$\xi_i \ge 0$$ converts the nonsmooth hinge loss $$\max(0, 1 - y_i(w^T x_i + b))$$ into linear inequalities $$\xi_i \ge 1 - y_i(w^T x_i + b)$$ and $$\xi_i \ge 0$$. Minimizing out $$\xi_i$$ analytically recovers the exact hinge-loss objective.

### Step-by-Step Worked Example (Read Slowly): Eliminating a Variable in a Coupled Quadratic Program

Consider the jointly convex quadratic function $$f(x, y) = x^2 + 2xy + 2y^2 - 4y$$ over $$(x, y) \in \mathbb{R}^2$$. Let us compute the reduced objective $$g(x) = \min_{y \in \mathbb{R}} f(x, y)$$ and verify both problems yield the same solution.

1. **Verify joint convexity**: The Hessian of $$f(x, y)$$ is
   $$\nabla^2 f(x, y) = \begin{bmatrix} 2 & 2 \\ 2 & 4 \end{bmatrix}.$$
   Its leading principal minors are $$2 > 0$$ and $$\det = 2(4) - 2^2 = 4 > 0$$, so $$\nabla^2 f \succ 0$$ and $$f$$ is strictly jointly convex.
2. **Minimize over $$y$$ for fixed $$x$$**: Differentiate with respect to $$y$$ and set to zero:
   $$\frac{\partial f}{\partial y} = 2x + 4y - 4 = 0 \implies y^\star(x) = 1 - \frac{x}{2}.$$
3. **Substitute $$y^\star(x)$$ back into $$f(x, y)$$ to form $$g(x)$$**:
   $$\begin{aligned} g(x) &= x^2 + 2x\left(1 - \frac{x}{2}\right) + 2\left(1 - \frac{x}{2}\right)^2 - 4\left(1 - \frac{x}{2}\right) \\ &= x^2 + 2x - x^2 + 2\left(1 - x + \frac{x^2}{4}\right) - 4 + 2x \\ &= \frac{1}{2}x^2 + 2x - 2. \end{aligned}$$
   Notice that $$g''(x) = 1 > 0$$, confirming $$g(x)$$ is convex (this is the Schur complement of the $$y$$-block!).
4. **Minimize $$g(x)$$ and recover $$(x^\star, y^\star)$$**: Setting $$g'(x) = x + 2 = 0$$ gives $$x^\star = -2$$, and substituting into $$y^\star(x)$$ gives $$y^\star = 1 - (-2)/2 = 2$$. The optimal value is $$g(-2) = \frac{1}{2}(4) + 2(-2) - 2 = -4$$. Checking directly in $$f(-2, 2)$$: $$(-2)^2 + 2(-2)(2) + 2(2)^2 - 4(2) = 4 - 8 + 8 - 8 = -4$$, an exact match.

[Reminder: ]({% multilang_post_url contents/chapter03/21-02-12-03_02_operations_that_preserve_convexity %})
If $$C$$ is a convex set and $$f$$ is convex in $$(x,y)$$, then $$g(x) = \min_{y \in C} f(x, y)$$ is convex in $$x$$.

Thus, partial optimization in a convex problem constructed with multivariate functions preserves convexity.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter04/partial-optimization.png" alt="[Fig1] partial optimization of a convex problem [3]">
  <figcaption style="text-align: center;">[Fig1] partial optimization of a convex problem [3]</figcaption>
</p>
</figure>
<br>

### Example: hinge form of SVMs

For a non-separable set, the SVM problem is defined as:
>$$
\begin{aligned}
&\min_{\beta, \beta_{0}, \xi} &&\frac{1}{2}\|\beta\|_2^2 + C \sum_{i=1}^{n} \xi_{i} \\
&\text{subject to} &&{\xi}_{i} \ge 0, \\ 
&&&y_{i}(x_{i}^T \beta + \beta_{0}) \ge 1 - {\xi}_{i}, \\
&&&i = 1, .., n \\
\end{aligned}
$$

The above constraints can be expressed as a single constraint:
> $$
\begin{aligned}
{\xi}_{i} \ge \max\{0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})\} \\
\end{aligned}
$$

In this case, $$\max\{0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})\}$$ is the minimum value for $$\xi_{i}$$, and we can define $$\tilde{f}$$ as:

> $$
\begin{aligned}
\frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} {\xi}_{i} &\ge \frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} \max({0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})})\\
&= \min\{\frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} \xi_{i} \quad | \quad \xi_{i} \ge 0, \ y_{i}(x_{i}^T \beta + \beta_{0}) \ge 1 - \xi_{i}, \ i = 1, .., n\} \\
&= \tilde{f}(\beta, \beta_{0}) \\
\end{aligned}
$$


By using the simplified $$\tilde{f}$$ as the objective function, a more straightforward solution can be obtained. In the given problem, $$\xi$$ has been eliminated, and it has also been transformed from a constrained problem to an unconstrained problem.

>$$
\begin{aligned}
\min_{\beta, \beta_0} \frac{1}{2} \|\beta\|_2^2 + C \sum_{i=1}^{n} \max\{0, 1 - y_{i} (x_{i}^{T} \beta + \beta_{0}) \}
\end{aligned}
$$
