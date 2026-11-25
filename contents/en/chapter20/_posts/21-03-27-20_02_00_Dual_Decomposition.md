---
layout: post
title: 20-02 Dual Decomposition
chapter: '20'
order: 4
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

When an optimization problem has millions of variables spread across hundreds of machines, departments, or sensors, the objective $$\sum_{i=1}^B f_i(x_i)$$ is often naturally separable—only a handful of shared resource or consistency constraints $$Ax = b$$ tie everything together. **Dual decomposition** (pioneered by Everett and Dantzig–Wolfe in the 1960s) uses Lagrange multipliers as a lightweight coordination bus: every worker solves its own private subproblem in parallel, and a coordinator updates the shared dual prices from the aggregate mismatch.

## Key ideas: The Architecture of Dual Decomposition

- **Block-Separable Objective, Coupled Constraints:** Minimizing $$\sum_{i=1}^B f_i(x_i)$$ subject to $$\sum_{i=1}^B A_i x_i = b$$ (or $$\le b$$) cannot be parallelized directly in primal space because changing $$x_1$$ forces $$x_2, \dots, x_B$$ to adjust.
- **Lagrangian Decoupling:** Moving the coupling constraint into the Lagrangian $$\sum_{i=1}^B \big(f_i(x_i) + u^T A_i x_i\big) - u^T b$$ breaks the primal minimization into $$B$$ completely independent subproblems for any fixed price vector $$u$$.
- **Broadcast–Gather Communication Pattern:** Each iteration needs only one broadcast of $$u$$ from the coordinator and one gather of local contributions $$A_i x_i^{(k)}$$—protecting local privacy (workers never share $$f_i$$) and scaling horizontally across clusters.
- **Price-Adjustment Economics:** If aggregate usage $$\sum_i A_i x_i^{(k)}$$ exceeds $$b$$, the dual price $$u$$ rises, discouraging consumption on the next round; if it falls short, $$u$$ drops—automatically steering the decentralized system toward equilibrium.

### Worked example: Parallelizing a Coupled 2-Block Quadratic

Minimize $$f_1(x_1) + f_2(x_2) = (x_1 - 4)^2 + 2(x_2 - 3)^2$$ subject to $$x_1 + x_2 = 4$$.

1. **Write the independent worker subproblems given broadcast price $$u$$:**
   - Worker 1: $$x_1(u) = \arg\min_{x_1} (x_1 - 4)^2 + u x_1 \implies 2(x_1 - 4) + u = 0 \implies x_1(u) = 4 - \frac{u}{2}$$.
   - Worker 2: $$x_2(u) = \arg\min_{x_2} 2(x_2 - 3)^2 + u x_2 \implies 4(x_2 - 3) + u = 0 \implies x_2(u) = 3 - \frac{u}{4}$$.
2. **Run one coordinator round from $$u^0 = 0$$ with step size $$t = 1$$:**
   - Workers compute in parallel: $$x_1^1 = 4, \; x_2^1 = 3$$.
   - Coordinator gathers sum: $$4 + 3 = 7 > 4$$ (excess demand $$+3$$!).
   - Coordinator raises price: $$u^1 = 0 + 1(7 - 4) = 3$$.
3. **Observe Round 2 at $$u^1 = 3$$:**
   - Worker 1 responds: $$x_1^2 = 4 - 1.5 = 2.5$$.
   - Worker 2 responds: $$x_2^2 = 3 - 0.75 = 2.25$$.
   - Aggregate mismatch dropped by $$75\%$$ (from $$+3$$ down to $$2.5 + 2.25 - 4 = +0.75$$), heading straight to the exact equilibrium $$u^\star = 4, \; x_1^\star = 2, \; x_2^\star = 2$$!

In this section, we examine techniques for decomposing problems using duality.