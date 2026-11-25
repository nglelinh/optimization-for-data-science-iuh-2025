---
layout: post
title: 04-02 Convex solution sets
chapter: '04'
order: 3
owner: YoungJae Choung
categories:
- chapter04
lang: en
lesson_type: required
---

When an optimization solver returns a solution, a natural engineering question immediately follows: *is this the only optimal answer, or is there an entire family of equally good designs?* In nonconvex optimization, optimal solutions can be scattered like isolated islands across space. In convex optimization, however, the geometry of the optimal solution set $$X_{\mathrm{opt}}$$ obeys a strict law: it is always a single connected convex region—and under strict convexity, it shrinks to at most one point.

## Key ideas: Geometry of the Optimal Solution Set

1. **Convexity of Sublevel Sets**: For any convex function $$f$$ and threshold $$\alpha$$, the sublevel set $$S_\alpha = \{x : f(x) \le \alpha\}$$ is convex. The optimal solution set is simply the intersection of the feasible set $$C$$ with the lowest non-empty sublevel set: $$X_{\mathrm{opt}} = C \cap \{x : f(x) \le f^\star\}$$. Because the intersection of convex sets is convex, $$X_{\mathrm{opt}}$$ is guaranteed to be convex.
2. **Flat Valleys and Non-Unique Solutions**: Whenever a convex objective has flat directions aligned with the feasible set—such as a linear objective parallel to a face of a polytope, or an $$\ell_1$$-regularized regression with collinear features—any convex combination $$\theta x + (1-\theta)y$$ of two minimizers stays feasible and achieves the exact same optimal value $$f^\star$$.
3. **Strict Convexity and Uniqueness**: A function is strictly convex if $$f(\theta x + (1-\theta)y) < \theta f(x) + (1-\theta)f(y)$$ for all $$x \neq y$$ and $$\theta \in (0, 1)$$. If two distinct optimal points existed, their midpoint would be feasible and have strictly lower objective value than $$f^\star$$, contradicting optimality. Hence strict convexity guarantees $$|X_{\mathrm{opt}}| \le 1$$.
4. **Why Uniqueness Matters in Practice**: In statistics and machine learning (such as Ridge vs. Lasso regression), adding a small strictly convex regularizer $$\frac{\lambda}{2}\|x\|_2^2$$ turns a flat solution face into a unique minimizer, stabilizing parameter estimates and making solutions continuous with respect to data perturbations.

### Worked example: Comparing a Convex Solution Face vs. a Unique Minimizer

Compare two convex programs over the unit simplex $$C = \{x \in \mathbb{R}^2 : x_1 \ge 0,\; x_2 \ge 0,\; x_1 + x_2 = 1\}$$:
- **Problem A (Convex, not strictly convex)**: $$\min_{x \in C} f_A(x) = (x_1 + x_2 - 1)^2 + 3(x_1 + x_2)$$.
- **Problem B (Strictly convex)**: $$\min_{x \in C} f_B(x) = x_1^2 + 3x_2^2$$.

1. **Analyze Problem A**: On the simplex $$C$$, every feasible point satisfies $$x_1 + x_2 = 1$$. Substituting this into $$f_A$$ gives $$f_A(x) = 0^2 + 3(1) = 3$$ for every $$x \in C$$. Therefore $$f_A^\star = 3$$ and the optimal solution set is the entire line segment
   $$X_{\mathrm{opt}}^A = \{(t, 1 - t) : 0 \le t \le 1\},$$
   which is a convex set with infinitely many points. Notice that if you take two minimizers $$x = (1, 0)$$ and $$y = (0, 1)$$, their midpoint $$z = (0.5, 0.5)$$ satisfies $$z \in C$$ and $$f_A(z) = 3 = f_A^\star$$.
2. **Analyze Problem B**: The Hessian of $$f_B$$ is $$\nabla^2 f_B(x) = \operatorname{diag}(2, 6) \succ 0$$, so $$f_B$$ is strictly convex. Substitute $$x_2 = 1 - x_1$$ with $$x_1 \in [0, 1]$$:
   $$f_B(x_1, 1 - x_1) = x_1^2 + 3(1 - x_1)^2 = 4x_1^2 - 6x_1 + 3.$$
   Setting the derivative $$8x_1 - 6 = 0$$ gives $$x_1^\star = \frac{3}{4} \in [0, 1]$$ and $$x_2^\star = \frac{1}{4}$$.
3. **Verify strict-convexity contradiction on any second point**: At $$x^\star = (\tfrac{3}{4}, \tfrac{1}{4})$$, $$f_B^\star = \frac{9}{16} + 3\cdot\frac{1}{16} = \frac{12}{16} = 0.75$$. Try another feasible point $$y = (\tfrac{1}{2}, \tfrac{1}{2})$$: $$f_B(y) = 0.25 + 0.75 = 1.00 > 0.75$$. Their midpoint $$z = (\tfrac{5}{8}, \tfrac{3}{8})$$ gives $$f_B(z) = \frac{25 + 27}{64} = \frac{52}{64} = 0.8125 < \frac{0.75 + 1.00}{2} = 0.875$$, illustrating the strict Jensen drop that forbids a second distinct minimizer.

Let's understand the properties of convex solution sets. <br>
Let $$X_{opt}$$ denote the set of solutions to a convex problem:

>$$
\begin{aligned}
X_{opt} =
&\text{arg}\min_x &&f(x) \\
&\text{subject to} &&g_{i}(x) \leq 0, i = 1, .., m \\
&&&h_{j}(x) = 0, j = 1, .., r  \\\\
\end{aligned}
$$

## Key property 1
> $$X_{opt}$$ is a convex set.

### Proof
> If $$x$$ and $$y$$ are solutions:
> 1. The domain set $$D$$ is convex, so for $$0 \le t \le 1$$, $$tx+ (1-t)y \in D$$.
> 2. $$g_i, i=1,\dotsc,m$$ and $$h_j, j=1, \dotsc,r$$ are convex and affine functions, so the following conditions hold:
    $$
    \begin{aligned}
       g_{i}(tx + (1-t)y) \leq tg_i(x) + (1-t)g_i(y) \leq 0, \\
       h_{j}(tx + (1-t)y) = th_j(x) + (1-t)h_j(y) = 0 \\
    \end{aligned}
    $$
> 3. $$f$$ is a convex function, so:
    >
    >\begin{aligned}
    >  f(tx+(1-t)y) &\leq tf(x) + (1-t)f(y) \\
    >  = tf^{\star} + (1-t) f^{\star} \\
    >  = f^{\star}
    >\end{aligned}
    >where $$f^{\star} - $$ minimum value.
    >Thus, $$tx + (1-t)y$$ is also a solution.

### Geometric interpretation
In a convex function, any local optimum is also a global optimum. <br>
If the solution set contains multiple elements, it must look like the following:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter04/multiple-optima.png" alt="[Fig1] geometric interpretation of convexity of the solution set">
  <figcaption style="text-align: center;">[Fig1] geometric interpretation of convexity of the solution set</figcaption>
</p>
</figure>
<br>

## Key property 2
>If $$f$$ is strictly convex, then the solution is unique. That is, $$X_{opt}$$ contains only one element.

$$f$$ being strictly convex means that $$f$$ always satisfies the following property:
>$$f(tx + (1-t)y) < tf(x) + (1-t)f(y),$$
>
>$$\text{where } 0 < t < 1, x \neq y, \text{ and } x, y \in \text{dom } f.$$

That is, $$f$$ is downward convex with no flat segments, and the solution of $$f$$ is unique.
