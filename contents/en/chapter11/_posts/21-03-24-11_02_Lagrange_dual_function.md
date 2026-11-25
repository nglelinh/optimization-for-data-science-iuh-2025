---
layout: post
title: 11-02 Lagrange dual function
chapter: '11'
order: 3
owner: Wontak Ryu
categories:
- chapter11
lang: en
lesson_type: required
---

Once you form the Lagrangian $$L(x, u, v)$$, how do you turn it into a concrete lower bound on $$f^\star$$ that does not depend on $$x$$? You simply drop all constraints and take the unconstrained infimum over $$x$$: $$g(u, v) = \inf_x L(x, u, v)$$. This **Lagrange dual function** is one of the cleanest miracles in mathematics: even when the original primal problem is nonconvex and NP-hard, $$g(u, v)$$ is *guaranteed* to be a concave function of $$(u, v)$$ that lower-bounds $$f^\star$$ everywhere!

## Key ideas: Properties & Computation of the Dual Function

- **Pillar 1 — Universal Lower-Bound Inequality:** For any $$u \ge 0$$ and $$v$$, $$f^\star = \min_{x \in C} f(x) \ge \min_{x \in C} L(x, u, v) \ge \inf_x L(x, u, v) = g(u, v)$$. Notice the two distinct relaxations: first replacing $$f$$ by $$L \le f$$ on $$C$$, then enlarging the minimization domain from $$C$$ to all of $$\mathbb{R}^n$$.
- **Pillar 2 — Guaranteed Concavity:** Because $$L(x, u, v)$$ is affine in $$(u, v)$$ for each fixed $$x$$, $$g(u, v) = \inf_x L(x, u, v)$$ is the pointwise infimum of affine functions—hence **always concave**, with a convex effective domain $$\operatorname{dom}(g) = \{(u, v) : g(u, v) > -\infty\}$$.
- **Pillar 3 — Quadratic Program (QP) Duals ($$Q \succ 0$$ vs. $$Q \succeq 0$$):** For $$\frac{1}{2}x^\top Q x + c^\top x$$ subject to $$Ax = b, x \ge 0$$, when $$Q \succ 0$$ the unique minimizer $$x = -Q^{-1}(c - u + A^\top v)$$ gives a closed-form concave quadratic $$g(u, v)$$. When $$Q \succeq 0$$ is singular, $$g(u, v)$$ is finite *only* when $$c - u + A^\top v \in \operatorname{col}(Q)$$, using the Moore–Penrose pseudoinverse $$Q^+$$!
- **Pillar 4 — Connection to Fenchel Conjugates:** For linear constraints $$Ax = b, Gx \le h$$, $$g(u, v) = -f^\star(-A^\top v - G^\top u) - b^\top v - h^\top u$$, showing that computing a dual function is mathematically equivalent to computing the Fenchel conjugate $$f^\star$$ of the objective.

### Worked example: Computing $$g(u, v)$$ for a Positive Definite vs. Singular QP

Minimize $$f(x_1, x_2) = \frac{1}{2}(x_1^2 + \alpha x_2^2) - 2x_1 - 4x_2$$ subject to $$x_1 + x_2 = 1$$ (with equality multiplier $$v \in \mathbb{R}$$).

1. **Case A — Strictly Positive Definite ($$\alpha = 2$$, so $$Q = \operatorname{diag}(1, 2) \succ 0$$):**
   - Lagrangian: $$L(x, v) = \frac{1}{2}x_1^2 + x_2^2 - 2x_1 - 4x_2 + v(x_1 + x_2 - 1)$$.
   - Stationarity in $$x$$: $$x_1 - 2 + v = 0 \implies x_1 = 2 - v$$; $$2x_2 - 4 + v = 0 \implies x_2 = 2 - \frac{v}{2}$$.
   - Substitute back:
     $$g(v) = -\frac{1}{2}(2 - v)^2 - \left(2 - \frac{v}{2}\right)^2 - v = -\frac{3}{4}v^2 + 3v - 6.$$
   - Note $$g(v)$$ is finite for *all* $$v \in \mathbb{R}$$ and strictly concave ($$g''(v) = -3/2 < 0$$)!
2. **Case B — Positive Semidefinite / Singular ($$\alpha = 0$$, so $$Q = \operatorname{diag}(1, 0) \succeq 0$$):**
   - Lagrangian: $$L(x, v) = \frac{1}{2}x_1^2 + (v - 2)x_1 + (v - 4)x_2 - v$$.
   - Minimize over $$x_2 \in \mathbb{R}$$: linear in $$x_2$$, so bounded below **if and only if** $$v - 4 = 0 \implies v = 4$$!
   - At $$v = 4$$, minimize over $$x_1$$: $$x_1 = 2 - 4 = -2$$, giving $$g(4) = \frac{1}{2}(-2)^2 + 2(-2) - 4 = 2 - 4 - 4 = -6$$.
   - Thus $$g(v) = -6$$ if $$v = 4$$, and $$-\infty$$ otherwise—illustrating how singularity of $$Q$$ creates an implicit equality constraint on the dual variable!

Let $$C$$ be the primal feasible set and $$f^*$$ the primal optimal value. Minimizing $$L(x,u,v)$$ over all $$x$$ yields the following lower bound.

>
$$
\begin{equation}
f^* \geq \min_{x \in C} L(x,u,v) \geq \min_x L(x,u,v) := g(u,v)
\end{equation}
$$

Here, $$g(u,v)$$ is called the Lagrange dual function and provides a lower bound on $$f^*$$ for any dual feasible $$u\geq 0$$, $$v$$.

For example, in the figure below

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter11/dual-gen_7.png" width="70%">
  <figcaption style="text-align: center;">[Fig 2] Example of Lagrangian dual function[1]</figcaption>
</p>
</figure>


* The dashed horizontal line indicates the function $$f^*$$.
* The dual variable is $$\lambda$$.
* The solid line indicates $$g(\lambda)$$.



## Example: Quadratic Program
###  1) Positive Definite ($$Q \succ 0$$)

Consider the following quadratic problem (here $$Q \succ 0$$)
>
$$
\begin{alignat}{1}
\min_x  & \quad \frac{1}{2}x^T Q x + c^T x \\\\
       s.t. & \quad Ax = b, \\\\
            & \quad x \geq 0
\end{alignat}
$$

Then,

#### Lagrangian:
>
$$
\begin{equation}
L(x,u,v) = \frac{1}{2}x^T Q x + c^T x - u^Tx + v^T (Ax-b)
\end{equation}
$$

#### Lagrangian dual function:

From the expression above, to minimize the Lagrangian function, differentiate with respect to $$x$$ and find $$x^*$$ such that the derivative is zero.
\begin{equation}
Qx - (c-u+A^T v) = 0,
\end{equation}
That is,
\begin{equation}
Qx = (c-u+A^T v)
\end{equation}
Since $$Q$$ is positive definite, its inverse exists, so we can find $$x^*$$ as $$x^* = Q^{-1}(c - u + A^Tv)$$. Therefore, substituting $$x^*$$ into the Lagrangian function, we obtain the following.

$$
\begin{alignat}{1}
& (c - u + A^T v)^T (Q^{-1})^T Q Q^{-1}(c - u + A^T v) - (c - u + A^T v)^T Q^{-1} (c - u + A^T v) - b^T v \\\
= & (c - u + A^T v)^T Q^{-1}(c - u + A^T v) - (c - u + A^T v)^T Q^{-1} (c - u + A^T v) - b^T v \\\
= & -\frac{1}{2} (c-u+A^Tv)^T Q^{-1} (c-u+A^T v) - b^T v
\end{alignat}
$$

Therefore,
>
$$
\begin{equation}
g(u,v) = \min_x L(x,u,v) = -\frac{1}{2} (c-u+A^Tv)^T Q^{-1} (c-u+A^T v) - b^T v
\end{equation}
$$

For all $$u \geq 0$$ and $$v$$, this corresponds to a lower bound on the primal optimum $$f^*$$.

### 2) Positive Semidefinite ($$Q \succeq 0$$)
For the same problem as above, but this time if $$Q \succeq 0$$,

#### Lagrangian:
>
$$
\begin{equation}
L(x,u,v) = \frac{1}{2}x^T Q x + c^T x - u^Tx + v^T (Ax-b)
\end{equation}
$$

#### Lagrangian dual function:
As in the case when $$Q$$ is positive definite, we need to find $$x^*$$ that satisfies the following equation.

$$
\begin{equation}
Qx = (c-u+A^T v)
\end{equation}
$$
At this point, since $$Q$$ is positive semi-definite, its inverse may not exist. Therefore, we need to consider the following two cases.

(1) $$c-u+A^T v \in col(Q)$$. In this case, there exists $$x^*$$ satisfying $$Qx = (c-u+A^T v)$$, which can be found using the generalized inverse $$Q^+$$ (the Moore-Penrose pseudo-inverse, $$Q^+ = (Q^TQ)^{-1}Q^T$$).
(2) $$c-u+A^T v \notin col(Q)$$. In this case, there is no $$x^*$$ satisfying $$Qx = (c-u+A^T v)$$, meaning there is no $$x^*$$ that minimizes $$L(x,u,v)$$, and the minimum of $$L(x,u,v)$$ is $$-\infty$$.

From these two cases, the Lagrangian dual function can be summarized as follows.
>
$$
g(u,v) =
\begin{cases}
-\frac{1}{2} (c-u+A^T v)^T Q^{+} (c - u + A^T v) - b^T v  & \text{if $c-u+A^T v \perp \text{null}(Q)$} \\\\
-\infty  & \text{otherwise}
\end{cases}
$$

For all $$u\geq 0$$, $$v$$ with $$c-u+A^Tv \perp \text{null}(Q)$$, $$g(u,v)$$ is a nontrivial lower bound on $$f^*$$.

## Example: Quadratic Program in 2D

For example, in the following figure, $$f(x_1,x_2)$$ is a quadratic function over variables greater than 0 ($$x\ge0$$), and the dual function $$g(u_1,u_2)$$ is a quadratic function over variables greater than 0 ($$u\ge0$$).

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter11/dual-gen_10.png" width="70%">
  <figcaption style="text-align: center;">[Fig 3] Example of quadratic program in 2D</figcaption>
</p>
</figure>

* The blue point is the optimal dual value, and the red point is the optimal primal value.
* For all $$u>0$$, the dual function $$g(u)$$ provides a lower bound on $$f^*$$.
* The maximum of the dual function $$g(u)$$ matches exactly the value $$f^*$$.

### The dual function is a lower bound (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/dual-lower-bound_en.mp4"></video>
</div>

For every $$\lambda\ge 0$$ the minimum of the Lagrangian, $$g(\lambda)=\min_x L(x,\lambda)$$, is a lower bound on $$p^*$$. The dual problem maximises that bound.

### Try it yourself: slide the multiplier

<div class="opx-explainer" data-opx="d1" data-lang="en"></div>
