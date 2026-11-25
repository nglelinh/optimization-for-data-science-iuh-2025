---
layout: post
title: '08-01-08 Projected Subgradient Method'
chapter: '08'
order: 10
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

Real-world optimization problems rarely live in unconstrained $$\mathbb{R}^n$$: probabilities must sum to one and stay nonnegative, portfolio weights face leverage caps, and adversarial perturbations must stay inside an $$\ell_p$$ ball. The **projected subgradient method** handles such constraints with disarming elegance: take an ordinary subgradient step as if no constraints existed, and if you step outside the feasible set $$C$$, snap right back to the nearest point inside $$C$$ via Euclidean projection. Surprisingly, this projection step never hurts the convergence rate—in fact, it strictly helps!

## Background Knowledge Map: Constrained Nonsmooth Optimization via Projection

- **Pillar 1 — Euclidean Projection Operator $$P_C(y)$$:** Defined as $$P_C(y) = \arg\min_{x \in C} \frac{1}{2}\|x - y\|_2^2$$, the projection onto a nonempty closed convex set $$C$$ always exists and is unique. For simple sets (boxes, Euclidean balls, half-spaces, simplices), $$P_C$$ has a fast closed-form or $$O(n \log n)$$ algorithm.
- **Pillar 2 — Nonexpansiveness (Why Projection Only Helps):** Because $$C$$ is convex, Euclidean projection is nonexpansive: for any $$y \in \mathbb{R}^n$$ and any feasible $$x^\star \in C$$, $$\|P_C(y) - x^\star\|_2^2 \le \|y - x^\star\|_2^2$$ (in fact, $$\|P_C(y) - x^\star\|_2^2 \le \|y - x^\star\|_2^2 - \|y - P_C(y)\|_2^2$$).
- **Pillar 3 — Unchanged Basic Inequality & $$O(1/\varepsilon^2)$$ Rate:** Applying nonexpansiveness to $$y = x^{(k)} - t_k g^{(k)}$$ yields $$\|x^{(k+1)} - x^\star\|_2^2 \le \|x^{(k)} - t_k g^{(k)} - x^\star\|_2^2$$, so the exact same basic inequality and convergence rates (fixed, diminishing, and Polyak) carry over verbatim from the unconstrained setting.
- **Pillar 4 — Computational Bottleneck:** Each iteration costs one subgradient evaluation plus one projection $$P_C$$. The method is therefore ideal when $$P_C$$ is cheap, whereas complex polyhedra or semidefinite cones motivate projection-free methods (Frank–Wolfe) or dual decomposition.

### Step-by-Step Worked Example (Read Slowly): Projected Subgradient on a Box Constraint

Minimize $$f(x_1, x_2) = |x_1 - 2| + |x_2 + 1|$$ subject to the unit box $$C = [-1, 1] \times [-1, 1]$$. Notice the unconstrained minimum $$(2, -1)$$ lies outside $$C$$, while the constrained minimum is $$x^\star = (1, -1)$$ with $$f^\star = 1$$.

1. **Initialize at $$x^{(0)} = (0, 0) \in C$$** with step size $$t_1 = 1.5$$. Here $$f(0, 0) = |-2| + |1| = 3$$, and $$\|x^{(0)} - x^\star\|_2^2 = 1^2 + 1^2 = 2$$.
2. **Compute a subgradient at $$x^{(0)} = (0, 0)$$:**
   - Since $$x_1 - 2 = -2 < 0$$, $$\partial_{x_1} |x_1 - 2| = \{-1\}$$.
   - Since $$x_2 + 1 = 1 > 0$$, $$\partial_{x_2} |x_2 + 1| = \{+1\}$$.
   - Hence $$g^{(0)} = (-1, 1)$$.
3. **Take the unconstrained subgradient step:**
   $$y^{(1)} = x^{(0)} - t_1 g^{(0)} = (0, 0) - 1.5(-1, 1) = (1.5, -1.5).$$
   Notice $$y^{(1)} \notin C$$ (both coordinates exceed the box bounds $$[-1, 1]$$), and its squared distance to $$x^\star = (1, -1)$$ is $$(1.5 - 1)^2 + (-1.5 + 1)^2 = 0.25 + 0.25 = 0.50$$.
4. **Project onto the box $$C = [-1, 1]^2$$ (coordinatewise clipping):**
   $$x^{(1)} = P_C(1.5, -1.5) = (\min(1, \max(-1, 1.5)),\; \min(1, \max(-1, -1.5))) = (1, -1).$$
5. **Verify nonexpansiveness:** After projection, $$\|x^{(1)} - x^\star\|_2^2 = 0 < 0.50 = \|y^{(1)} - x^\star\|_2^2$$. The projection not only restored feasibility—it landed directly on the exact constrained optimum $$x^\star = (1, -1)$$!

The method described in the previous example is called the projected subgradient method. This algorithm can be used for convex problems with constraints.

If we denote the domain that satisfies the constraints as the set $$C$$, then a constrained convex problem is defined as follows:

>
$$ \begin{align}
\min_x \text{ }f(x) \quad \text{subject to } x \in C
\end{align} $$

By using the projected subgradient method, such problems can be solved relatively easily. The projected subgradient method is similar to the standard subgradient method, but at each iteration, the result is projected onto the set $$C$$.

>
$$ \begin{align}
x^{(k)} = P_c(x^{(k-1)} - t_k \cdot g^{(k-1)}), \quad k = 1,2,3,...
\end{align} $$

If projection is possible, this method has the same convergence properties and rate as the subgradient method.

One thing to note about the projected subgradient method is that even if $$C$$ is a simple convex set, if the projection operation $$P_c$$ is difficult, the overall problem also becomes hard to solve. Typically, the following sets $$C$$ are relatively easy to project onto:

- Affine images: {$$Ax=b : x \in \mathbb{R}^{n}$$}
- Solution set of linear system: {$$x: Ax=b$$}
- Nonnegative orthant: $$\mathbb{R}_+^{n} =  $${$$x: x\ge 0$$}
- Some norm balls: {$$x: \lVert x \rVert _p \le 1 $$} for $$p=1,2,\infty$$
- Some simple polyhedra and simple cones
