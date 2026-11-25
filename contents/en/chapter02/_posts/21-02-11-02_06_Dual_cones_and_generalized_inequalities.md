---
layout: post
title: 02-06 Dual cones and generalized inequalities
chapter: '02'
order: 14
owner: Wontak Ryu
categories:
- chapter02
lang: en
---

Every cone $$K$$ casts a shadow—its **dual cone** $$K^*$$, consisting of all directions that make an acute (or right) angle with every vector in $$K$$. Why does this geometric shadow matter? Because in vector optimization and conic duality, Lagrange multipliers for a conic constraint $$x \in K$$ must live in $$K^*$$, and strictly positive dual weights $$\lambda \succ_{K^*} 0$$ sweep out Pareto-optimal frontiers by turning multi-objective problems into scalar objectives.

## Background Knowledge Map: Dual Cones & Cone-Ordered Duality

- **Dual Cone Definition ($$K^* = \{y : y^T x \ge 0 \;\forall x \in K\}$$):** Always a closed convex cone—even if the original set $$K$$ was not convex!
- **Inclusion Reversal (Narrow Cone $$\leftrightarrow$$ Wide Dual):** Shrinking $$K$$ relaxes the inner-product constraints on $$y$$, making $$K^*$$ strictly larger ($$K_1 \subseteq K_2 \implies K_2^* \subseteq K_1^*$$).
- **Self-Dual Cones ($$K^* = K$$):** The nonnegative orthant $$\mathbb{R}_+^n$$, the $$\ell_2$$ second-order cone, and the PSD cone $$\mathbb{S}_+^n$$ are all self-dual—the symmetry that powers primal-dual interior-point methods.
- **Scalarizing Vector Objectives:** Multiplying a vector constraint or objective by $$\lambda \in K^*$$ converts cone inequalities into ordinary scalar inequalities without reversing their direction.

### Step-by-Step Worked Example (Read Slowly): Computing the Dual of a Narrow 2D Wedge

Find the dual cone $$K^*$$ of the narrow first-quadrant wedge $$K = \text{cone}\{(1, 0)^T,\; (1, 1)^T\}$$.

1. **Test against the extreme rays of $$K$$:** Any $$x \in K$$ is $$x = \alpha(1, 0)^T + \beta(1, 1)^T$$ with $$\alpha, \beta \ge 0$$. Thus $$y^T x \ge 0$$ for all $$x \in K$$ if and only if $$y$$ has nonnegative inner product with both generators:
   - $$y^T (1, 0)^T = y_1 \ge 0$$.
   - $$y^T (1, 1)^T = y_1 + y_2 \ge 0$$ (i.e., $$y_2 \ge -y_1$$).
2. **Write $$K^*$$ explicitly:**
   $$K^* = \{(y_1, y_2) \in \mathbb{R}^2 : y_1 \ge 0,\; y_1 + y_2 \ge 0\}.$$
3. **Observe the width reversal:** While $$K$$ has an opening angle of only $$45^\circ$$ (between $$0^\circ$$ and $$45^\circ$$), $$K^*$$ opens across $$135^\circ$$ (from $$-45^\circ$$ to $$90^\circ$$)—for instance, $$y = (1, -1)^T \in K^*$$ even though $$y \notin K$$.

This section discusses dual cones paired with cones, and dual generalized inequalities. Using dual generalized inequalities allows comparison using scalar inner products, making comparisons much easier.