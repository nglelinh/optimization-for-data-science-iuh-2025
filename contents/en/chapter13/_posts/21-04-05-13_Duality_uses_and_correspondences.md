---
layout: post
title: 13 Duality uses and correspondences
chapter: "13"
order: 1
owner: "Wontak Ryu"
categories:
- chapter13
lang: en
---

Imagine you are auditing a complex supply-chain optimizer that claims its current routing plan is "within 1% of the theoretical best possible cost." Without knowing the true optimal cost $$f^\star$$—which nobody has ever computed—how could you possibly verify that claim? Duality is the mathematical lens that hands you an indisputable lower bound from a mirror-image problem, turning an unknowable optimum into a certifiable bracket and revealing hidden geometric correspondences between norms, functions, and cones.

## Key ideas: The Architecture of Duality Correspondences

- **Pillar 1 — Primal-Dual Certificates (Why Bounds Matter):** Every feasible dual point $$(u,v)$$ yields a lower bound $$g(u,v) \le f^\star$$. Paired with any feasible primal point $$x$$, the gap $$f(x) - g(u,v)$$ certifies suboptimality without ever knowing $$f^\star$$.
- **Pillar 2 — Dual Norms & Geometric Pairing:** Measuring a primal vector in one norm $$\|\cdot\|$$ automatically induces a dual norm $$\|\cdot\|_*$$ that measures linear functionals (gradients, prices, dual variables) against the primal unit ball.
- **Pillar 3 — Fenchel Conjugates as Function Mirrors:** The conjugate $$f^*(y) = \max_x (y^T x - f(x))$$ translates convex objectives—including nonsmooth norms and indicator constraints—into dual objectives cleanly, separating optimal values ($$x^\star$$) from conjugates ($$f^*$$).
- **Pillar 4 — Dual Cones as Generalized Nonnegativity:** Replacing componentwise inequalities $$x \ge 0$$ with conic memberships $$Ax \in K$$ generalizes Lagrange multipliers from nonnegative vectors to dual-cone certificates $$u \in K^*$$.

### Worked example: Bracketing an Unknown Optimum via Duality

Consider minimizing the 1D convex objective $$f(x) = \frac{1}{2}x^2 - 4x$$ subject to $$x \ge 1$$ (written as $$h(x) = 1 - x \le 0$$).

1. **Form the Lagrangian:** Introduce dual variable $$u \ge 0$:
   $$L(x, u) = \frac{1}{2}x^2 - 4x + u(1 - x) = \frac{1}{2}x^2 - (4+u)x + u.$$
2. **Minimize over $$x$$ to get the dual function $$g(u)$$:** Setting $$\frac{\partial L}{\partial x} = x - (4+u) = 0$$ gives $$x(u) = 4 + u$$. Substituting back:
   $$g(u) = \frac{1}{2}(4+u)^2 - (4+u)^2 + u = -\frac{1}{2}(4+u)^2 + u.$$
3. **Evaluate a feasible primal-dual pair:** Take primal feasible $$x = 3$$ (since $$3 \ge 1$$) and dual feasible $$u = 1$$ (since $$u \ge 0$$).
   - Primal value: $$f(3) = \frac{1}{2}(9) - 12 = -7.5$$.
   - Dual value: $$g(1) = -\frac{1}{2}(25) + 1 = -11.5$$.
   - Certified duality gap: $$f(3) - g(1) = -7.5 - (-11.5) = 4.0$$, guaranteeing $$f^\star \in [-11.5, -7.5]$$.
4. **Check zero gap at optimality:** At $$x^\star = 4$$ and $$u^\star = 0$$, we get $$f(4) = -8$$ and $$g(0) = -8$$, closing the gap to $$0$$ and confirming global optimality.

In this chapter, we will learn about the uses of Duality and related correspondences through examples.

### [Notice]

In this chapter, the optimal solution $$x^{\star}$$ and the conjugate $$x^{*}$$ of $$x$$ are distinguished and denoted as such.

## Modern applications (2022–2026)

An optional companion lesson attaches 2022–2026 uses to the same correspondences: dual norms in RobustBench, the Lasso dual in skglm screening, conjugates in Clarabel / CVXPY, and dual cones in α,β-CROWN. See [13-07 Modern uses of conjugates, dual norms, and dual cones]({% multilang_post_url contents/chapter13/2026-09-16-13_07_modern_applications %}).
