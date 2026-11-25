---
layout: post
title: 13-06 Dual subtleties & Double dual
chapter: '13'
order: 10
owner: Wontak Ryu
categories:
- chapter13
lang: en
---

Two graduate students are asked to derive the dual of the exact same unconstrained optimization problem. Student A splits one term and obtains a dual with optimal value $$12$$; Student B splits a different linear operator and then drops a constant factor of $$\frac{1}{2}$$, obtaining a dual with optimal value $$24$$. Who is wrong? Possibly *neither*! Understanding how equivalent reformulations alter dual values—and when taking the dual of the dual brings you cleanly back to the primal—prevents subtle bugs when implementing primal-dual solvers.

## Background Knowledge Map: Navigating Dual Subtleties and Biduality

- **Pillar 1 — Equivalent Reformulations Can Shift Optimal Values:** Dropping constants, scaling the dual objective, or taking a monotone transformation (like $$\log$$) preserves the optimal dual variables $$u^\star$$, *but* breaks the identity $$f(x^\star) = g(u^\star)$$ when computing a duality gap.
- **Pillar 2 — Non-Uniqueness of Dummy-Variable Duals:** Introducing $$z = x$$ versus $$z = Ax$$ leads to structurally different dual problems with different dimensions and conditioning, even though both correspond to the same primal.
- **Pillar 3 — Linear-Constraint Double Dual via $$f^{**} = f$$:** For $$\min_x f(x)$$ s.t. $$Ax \le b, Cx = d$$, the dual is $$\max_{u\ge 0, v} -f^*(-A^Tu - C^Tv) - b^Tu - d^Tv$$. Taking its dual again yields $$f^{**}(x)$$ under the same constraints—recovering the primal whenever $$f$$ is closed and convex.
- **Pillar 4 — Nonlinear Biduality & Convexification:** Even with nonlinear convex inequalities $$h_i(x) \le 0$$, closed convexity ensures the dual of the dual is the primal; for nonconvex problems, the double dual yields the tightest convex relaxation (biconjugate envelope).

### Step-by-Step Worked Example (Read Slowly): Two Different Duals of the Same Problem & Double Dual Recovery

Consider the unconstrained quadratic $$\min_{x \in \mathbb{R}} \frac{1}{2}(2x - 4)^2 + \frac{1}{2}x^2$$. Its true primal optimum is $$x^\star = \frac{8}{5} = 1.6$$ with $$f^\star = \frac{1}{2}(-0.8)^2 + \frac{1}{2}(1.6)^2 = 0.32 + 1.28 = 1.6$$.

1. **Dual A (Split $$z = 2x - 4$$):** Minimize $$\frac{1}{2}z^2 + \frac{1}{2}x^2$$ s.t. $$z = 2x - 4$$.
   - $$L(x,z,u) = \frac{1}{2}z^2 + \frac{1}{2}x^2 + u(2x - 4 - z)$$.
   - Minimizing gives $$x = -2u$$, $$z = u$$, and $$g_A(u) = -\frac{5}{2}u^2 - 4u$$.
   - Maximizing gives $$u^\star = -\frac{4}{5} = -0.8$$ and $$g_A(u^\star) = -\frac{5}{2}(0.64) + 3.2 = 1.6 = f^\star$$.
2. **Dual B (Transformed equivalent dual):** Dropping the factor $$\frac{1}{2}$$ and flipping sign turns Dual A into $$\min_u 5u^2 + 8u$$. Its minimizer is still $$u^\star = -0.8$$ (which still recovers $$x^\star = -2u^\star = 1.6$$), *but* its optimal value is $$-3.2 \ne 1.6$$! You must never plug $$-3.2$$ directly into a duality-gap check $$f(x) - g(u)$$.
3. **Verify the double dual of $$\min_{x \ge 1} \frac{1}{2}x^2$$:**
   - Primal: $$\min_x \frac{1}{2}x^2$$ s.t. $$-x \le -1$$ ($$A = -1, b = -1$$).
   - Dual: $$\max_{u \ge 0} -\frac{1}{2}u^2 + u$$ (equivalent to $$\min_{u \ge 0} \frac{1}{2}u^2 - u$$).
   - Dual of the dual (multiplier $$x \ge 0$$ on $$-u \le 0$$): $$L_2(u,x) = \frac{1}{2}u^2 - u - xu$$ minimized over $$u$$ at $$u = 1+x$$ gives $$-\frac{1}{2}(1+x)^2$$, so maximizing over $$x \ge 0$$ recovers $$-\min_{x \ge 1}\frac{1}{2}x^2$$—the exact original primal!

## Dual subtleties
• Sometimes we can transform dual problems into equivalent problems and still call them dual problems. Also, in strong duality, we can use solutions of transformed dual problems for analyzing or computing characteristics of primal solutions.

#### [Note]
The optimal value of a transformed dual problem is not necessarily the optimal value of the primal.


• A common way to derive dual problems for unconstrained problems is to first transform the primal by adding dummy variables and equality constraints.

Generally, how to do this is ambiguous. Different choices can lead to different dual problems.


## Double dual
Let's consider a general minimization problem with linear constraints:

> $$ \min_x f(x) \text{ subject to } Ax ≤ b, Cx = d$$

The Lagrangian is as follows:
> $$L(x,u,v) = f(x) + (A^Tu + C^Tv)^Tx−b^Tu−d^Tv$$

Therefore, the dual problem is as follows:

> $$ \max_{u,v} −f^∗(−A^Tu−C^Tv)−b^Tu−d^Tv \text{ subject to } u ≥ 0 $$

#### Recall property
If $$f$$ is closed and convex, we explained earlier that the dual of the dual is the primal in this case ($$f^{∗∗} = f$$).

In fact, the connection (between dual and dual conjugate) goes much deeper beyond linear constraints.
Consider the following:

> $$ 
>\begin{align}
> & \min_x && f(x) \\
> &\text{ subject to } && h_i(x) ≤ 0, i = 1,...m \\
> &&&l_j(x) = 0, j = 1,...r
>\end{align}$$

If $$f$$ and $$h_1,...h_m$$ are closed and convex, and $$l_1,...l_r$$ are affine, then the dual of the dual is the primal.

This is provided as a minimization problem from the perspective of bifunctions.

(for more, read Chapters 29 and 30 of Rockafellar)
