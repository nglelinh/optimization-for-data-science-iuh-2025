---
layout: post
title: 16 Duality Revisited
chapter: '16'
order: 1
owner: Minjoo Lee
categories:
- chapter16
lang: en
---

You have already met Lagrange duality in Chapter 11, KKT conditions in Chapter 12, and log-barrier interior-point methods in Chapter 15. Why pause right here to *revisit* duality before entering Chapter 17? Because the barrier method solves only the primal problem while treating dual variables as a byproduct—whereas **Primal-Dual Interior-Point Methods** update primal and dual variables *simultaneously* on equal footing, and that symmetry only becomes transparent when you see Lagrangian min-max duality, perturbed KKT conditions, and Fenchel conjugates working together as one unified machine.

## Key ideas: Why Duality Is Revisited Before Primal-Dual IPMs

- **Pillar 1 — Min–Max Saddle-Point Symmetry:** Writing the primal as $$\min_x \max_{u \ge 0, v} L(x, u, v)$$ and the dual as $$\max_{u \ge 0, v} \min_x L(x, u, v)$$ puts primal and dual variables on symmetric footing and explains weak duality in one line.
- **Pillar 2 — Self-Symmetry of Barrier Problems:** Taking the Lagrange dual of the LP barrier problem recovers the *exact* barrier problem of the dual LP—revealing why primal-dual path-following is naturally symmetric.
- **Pillar 3 — Exact vs. Perturbed KKT Systems:** Comparing KKT optimality ($$u_i h_i = 0$$) with barrier KKT optimality ($$u_i h_i = -1/t$$) directly defines the nonlinear residual vector $$r_t(x, u, v) = 0$$ that Chapter 17 solves with Newton's method.
- **Pillar 4 — Fenchel Duality for Structured Problems:** The Fenchel pair $$\min_x f(x) + g(Ax) \leftrightarrow \max_v -f^*(A^T v) - g^*(-v)$$ gives an algebraic shortcut for composite ML losses, regularizers, and optimal transport.

### Worked example: Seeing the Saddle-Point Min–Max Identity on a 1D LP

Consider the 1D LP $$\min_x 2x$$ subject to $$x \ge 3$$ (i.e., $$h(x) = 3 - x \le 0$$). Its Lagrangian is $$L(x, u) = 2x + u(3 - x) = (2 - u)x + 3u$$ for $$u \ge 0$$.

1. **Primal via $$\min_x \max_{u \ge 0} L(x, u)$$:**
   - If $$x < 3$$, $$3 - x > 0$$ so $$\max_{u \ge 0} L(x, u) = +\infty$$ (infeasible penalty!).
   - If $$x \ge 3$$, $$3 - x \le 0$$ so the maximum over $$u \ge 0$$ is attained at $$u = 0$$, giving $$2x$$.
   - Minimizing $$2x$$ over $$x \ge 3$$ yields $$x^\star = 3, p^\star = 6$$.
2. **Dual via $$\max_{u \ge 0} \min_x L(x, u)$$:**
   - If $$u \ne 2$$, $$(2 - u)x$$ can be driven to $$-\infty$$, so $$\min_x L(x, u) = -\infty$$.
   - If $$u = 2$$, $$L(x, 2) = 6$$ for all $$x$$, giving $$u^\star = 2, d^\star = 6$$.
3. **Saddle-point verification at $$(x^\star, u^\star) = (3, 2)$$:**
   For every $$x \in \mathbb{R}$$ and every $$u \ge 0$$,
   $$L(3, u) = 6 + u(0) = 6 \le L(3, 2) = 6 \le (2 - 2)x + 6 = L(x, 2).$$
   $$(3, 2)$$ is an exact saddle point!

In this chapter, we organize essential background knowledge about duality before covering the Primal-Dual Interior-Point method. The Primal-Dual Interior-Point method can be viewed as an extension of the Barrier method, and the concept of duality emerges as a key topic in the process of developing the content.

## References and further readings

* O. Guler (2010), “Foundations of Optimization”, Chapter 11.
* J. Renegar (2001), “A mathematical view of interior-point methods in convex optimization,” Chapters 2 and 3.
* S. Wright (1997), “Primal-dual interior-point methods”, Chapters 5 and 6.