---
layout: post
title: 11-03 Lagrange dual problem
chapter: '11'
order: 4
owner: Wontak Ryu
categories:
- chapter11
lang: en
lesson_type: required
---

Every dual-feasible pair $$(u, v)$$ with $$u \ge 0$$ hands us a guaranteed lower bound $$g(u, v) \le f^\star$$. Naturally, we want the *tightest* possible lower bound—so we define the **Lagrange dual problem** $$\max_{u, v} \{ g(u, v) : u \ge 0 \}$$. Even if the primal problem is a bumpy, multi-modal nonconvex quartic with traps everywhere, this dual problem is a clean **convex optimization problem** (maximizing a concave function over a convex cone), giving us a tractable way to compute rigorous lower bounds!

## Background Knowledge Map: Structure & Geometry of the Lagrange Dual Problem

- **Pillar 1 — Always a Convex Optimization Problem:** Maximizing the concave function $$g(u, v)$$ over the convex set $$\{(u, v) : u \ge 0\}$$ (equivalently minimizing $$-g(u, v)$$) is *always* convex, regardless of whether the primal is convex, discrete, or nonconvex.
- **Pillar 2 — Weak Duality ($$g^\star \le f^\star$$):** Since $$g(u, v) \le f^\star$$ for all $$u \ge 0, v \in \mathbb{R}^r$$, taking the supremum over $$u \ge 0, v$$ gives $$g^\star \le f^\star$$ unconditionally. The nonnegative difference $$f^\star - g^\star \ge 0$$ is the **optimal duality gap**.
- **Pillar 3 — Implicit Domain Constraints:** When $$g(u, v) = -\infty$$ outside some set (as in LPs or singular QPs), making those domain conditions explicit turns $$\max_{u \ge 0} g(u, v)$$ into a standard constrained convex program.
- **Pillar 4 — Nonconvex Primal Caveat (Strict Duality Gap):** For nonconvex problems (like a double-well quartic on a constrained interval), the dual finds the best supporting hyperplane to the primal's nonconvex optimal-value curve—which can sit strictly below $$f^\star$$ ($$g^\star < f^\star$$), yielding a valuable lower bound but not necessarily the exact primal optimum.

### Step-by-Step Worked Example (Read Slowly): Computing a Strict Duality Gap on a Nonconvex Problem

Consider the nonconvex discrete-domain optimization problem:
$$\min_{x \in \{0, 2\}}\; f(x) = x - 2 \quad \text{s.t.} \quad 1 - x \le 0 \text{ (i.e., } x \ge 1\text{)}.$$

1. **Solve the primal directly:** Between the two domain points $$\{0, 2\}$$, only $$x^\star = 2$$ satisfies $$x \ge 1$$, giving:
   $$f^\star = f(2) = 2 - 2 = 0.$$
2. **Form the Lagrangian $$L(x, u) = (x - 2) + u(1 - x)$$ for $$u \ge 0$$:**
   - At $$x = 0$$: $$L(0, u) = -2 + u$$.
   - At $$x = 2$$: $$L(2, u) = 0 - u = -u$$.
3. **Compute the concave Lagrange dual function $$g(u) = \min_{x \in \{0, 2\}} L(x, u)$$:**
   $$g(u) = \min\{ -2 + u,\; -u \}, \qquad u \ge 0.$$
   As the pointwise minimum of two affine functions, $$g(u)$$ is concave even though the primal domain $$\{0, 2\}$$ is nonconvex!
4. **Solve the Lagrange dual problem $$\max_{u \ge 0} g(u)$$:**
   Equate the increasing line $$-2 + u$$ and the decreasing line $$-u$$:
   $$-2 + u = -u \implies 2u = 2 \implies u^\star = 1 \ge 0, \qquad g^\star = g(1) = -1.$$
5. **Measure the strict duality gap:** $$f^\star - g^\star = 0 - (-1) = 1 > 0$$! Geometrically, the dual automatically solved the *convex relaxation* $$x \in [0, 2]$$ (where $$x = 1$$ achieves $$f(1) = -1$$), showing concretely why nonconvexity can leave a strict gap $$g^\star < f^\star$$.

Consider the following optimization problem:
>
$$
\begin{alignat}{1}
\min_x & \quad f(x)  \\
s.t.   & \quad h_i(x) \leq 0, i=1,\dots,m  \\
       & \quad l_j(x) = 0, j=1,\dots,r
\end{alignat}
$$

The dual function $$g(u,v)$$ satisfies $$f^* \geq g(u,v)$$ for all $$u\geq 0$$ and $$v$$. Therefore, we can obtain the best lower bound by maximizing $$g(u,v)$$ over all feasible $$u$$ and $$v$$. This is called the Lagrange dual problem. 
>
$$
\begin{alignat}{1}
\max_{u,v} & \quad g(u,v)   \\
           s.t. & \quad u \geq 0
\end{alignat}
$$

Here, if we denote the dual optimal value as $$g^*$$, then $$f^* \geq g^*$$. This is called weak duality. This property always holds even when the primal problem is not convex. Moreover, the dual problem is always a convex optimization problem, even when the primal problem is not convex.

By definition, $$g$$ is concave with respect to $$(u,v)$$, and $$u \geq 0$$ is a convex constraint. Therefore, the dual problem corresponds to a concave maximization problem. 
>
\begin{alignat}{1}
 g(u,v) & = \min_x \{ f(x) + \sum_{i=1}^m u_i h_i(x) + \sum_{j=1}^r v_j l_j(x) \}  \\ 
        & = - \underbrace{\max_x \{ -f(x) - \sum_{i=1}^m u_i h_i(x) - \sum_{j=1}^r v_j l_j(x) \}}_{\text{pointwise maximum of convex functions in $(u,v)$}}
\end{alignat}




## Example: nonconvex quartic minimization
Let us minimize the function $$f(x)=x^4 - 50 x^2 + 100 x$$ subject to $$x \geq -4.5$$.


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter11/dual-gen_13.png" width="70%">
  <figcaption style="text-align: center;">[Fig 4] Example of nonconvex quadratic minimization</figcaption>
</p>
</figure>

In this case, the dual function $$g$$ is as follows: 
>
$$
\begin{equation}
 g(u) = \min_{i=1,2,3} \{F_i^4(u) - 50 F_i^2(u) + 100 F_i(u) \}
\end{equation}
$$

where, for $$i=1,2,3$$, 
>
$$
\begin{alignat}{1}
F_i(u) = & \frac{- a_i}{12\cdot 2^{1/3}} \left( 432(100-u)-(432^2(100-u)^2 - 4\cdot 1200^3)^{1/2} \right )^{1/3} \\ 
           & - 100 \cdot 2^{1/3} \frac{1}{\left( 432(100-u)-(432^2(100-u)^2 - 4\cdot 1200^3)^{1/2} \right )^{1/3}}
\end{alignat}
$$

and $$a_1=1, a_2 = (-1+i\sqrt{3})/2, a_3 = (-1-i \sqrt{3})/2$$.
While it is difficult to determine whether $$g$$ is concave just by looking at the function, we can know that $$g$$ is concave under the convexity property of duality.
