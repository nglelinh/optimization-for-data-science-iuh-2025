---
layout: post
title: 12 KKT Conditions
chapter: '12'
order: 1
owner: Wontak Ryu
categories:
- chapter12
lang: en
---

In unconstrained calculus, finding the minimum of a smooth convex function reduces to a single famous equation: $$\nabla f(x^\star) = 0$$. The moment you add inequality constraints $$h_i(x) \le 0$$ and equality constraints $$l_j(x) = 0$$, however, the minimum often sits pinned against a boundary where $$\nabla f(x^\star) \neq 0$$! How do you recognize an optimal point when the terrain hits a wall? The **Karush–Kuhn–Tucker (KKT) conditions**—first discovered by William Karush in his 1939 master's thesis and independently rediscovered by Harold Kuhn and Albert Tucker in 1951—provide the exact four-part algebraic fingerprint of optimality for constrained optimization.

## Background Knowledge Map: The Four Pillars of the KKT System

- **Pillar 1 — Stationarity (Force Balance at the Optimum):** $$0 \in \partial f(x^\star) + \sum_{i=1}^m u_i^\star \partial h_i(x^\star) + \sum_{j=1}^r v_j^\star \partial l_j(x^\star)$$. Geometrically, the downhill pull $$-\nabla f(x^\star)$$ is exactly cancelled by a nonnegative combination of the outward normal vectors $$\nabla h_i(x^\star)$$ of active walls and the normals $$\nabla l_j(x^\star)$$ of equality surfaces.
- **Pillar 2 — Complementary Slackness ($$u_i^\star h_i(x^\star) = 0$$):** Either constraint $$i$$ is active ($$h_i(x^\star) = 0$$, exerting a restoring force $$u_i^\star \ge 0$$), or constraint $$i$$ is strictly inactive ($$h_i(x^\star) < 0$$, forcing its price $$u_i^\star = 0$$). An untouched wall can never push on the solution!
- **Pillar 3 — Primal & Dual Feasibility:** The primal point must respect all constraints ($$h_i(x^\star) \le 0,\; l_j(x^\star) = 0$$), and inequality multipliers must push *inward* rather than pull outward ($$u_i^\star \ge 0$$).
- **Pillar 4 — Necessity vs. Sufficiency:** Under strong duality, KKT is *necessary* for any optimal primal–dual pair (even for nonconvex differentiable problems). For *convex* problems, KKT is *always sufficient* for global optimality—and when Slater's condition holds, KKT is **both necessary and sufficient**!

### Step-by-Step Worked Example (Read Slowly): Solving a Constrained Convex Problem Directly via KKT

Minimize $$f(x) = (x - 3)^2$$ subject to $$h(x) = x - 1 \le 0$$ (i.e., $$x \le 1$$).

1. **Write all four KKT conditions for $$(x^\star, u^\star)$$:**
   - Stationarity: $$2(x^\star - 3) + u^\star = 0 \implies u^\star = 6 - 2x^\star$$.
   - Complementary slackness: $$u^\star (x^\star - 1) = 0$$.
   - Primal feasibility: $$x^\star \le 1$$.
   - Dual feasibility: $$u^\star \ge 0$$.
2. **Case 1 — Inactive wall ($$u^\star = 0$$):** Stationarity gives $$x^\star = 3$$, which violates primal feasibility $$3 \le 1$$. Eliminate Case 1!
3. **Case 2 — Active wall ($$x^\star - 1 = 0 \implies x^\star = 1$$):**
   - Stationarity gives $$u^\star = 6 - 2(1) = 4$$.
   - Dual feasibility check: $$u^\star = 4 \ge 0$$ (satisfied!).
   - Primal feasibility check: $$1 - 1 = 0 \le 0$$ (satisfied!).
4. **Conclusion:** Because the problem is convex, $$(x^\star, u^\star) = (1, 4)$$ satisfies all four KKT conditions and is certified globally optimal—with the multiplier $$u^\star = 4$$ literally equaling the restoring force needed to hold the ball against the wall $$x = 1$$!

When the primal problem is convex, the Karush–Kuhn–Tucker (KKT) conditions become sufficient conditions for primal & dual optimal points with zero duality gap. Additionally, when the objective function and constraint functions of the primal problem are differentiable and satisfy strong duality, the primal & dual optimal points always satisfy the KKT conditions. KKT conditions hold a very important position in optimization. These conditions allow some special problems to be solved analytically, and many convex optimization algorithms can be interpreted as methods for solving KKT conditions [1]. In this chapter, we will learn about the definition and properties of KKT conditions and look at some examples based on them.

*As a side note*, KKT conditions were originally introduced to the world by Harold W. Kuhn and Albert W. Tucker in 1951, and at that time they were called KT (Kuhn-Tucker) conditions. Later, scholars discovered that the necessary conditions for this problem had been addressed by William Karush's master's thesis in 1939, and from then on, Karush's name was included and they became known as KKT (Karush–Kuhn–Tucker) conditions [3].

## Modern applications (2022–2026)

An optional companion lesson reads the same KKT system in cvxpylayers / Theseus, SVM support vectors, electricity LMPs, and binding fairness constraints. See [12-07 Modern applications of the KKT conditions]({% multilang_post_url contents/chapter12/2026-09-16-12_07_modern_applications %}).
