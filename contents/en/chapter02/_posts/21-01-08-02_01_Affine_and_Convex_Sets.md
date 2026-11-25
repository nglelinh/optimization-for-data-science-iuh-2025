---
layout: post
title: 02-01 Affine and Convex Sets
chapter: '02'
order: 2
owner: Wontak Ryu
categories:
- chapter02
lang: en
lesson_type: required
---

Not all combinations of two vectors are created equal. Depending on which restrictions we place on the scalar weights $$\theta_1, \theta_2$$, combining the exact same pair of points traces out an infinite line (affine), a bounded bridge (convex), or an unbounded wedge (conic). Section 02-01 lays out this three-tier geometric hierarchy that classifies every linear and conic constraint in optimization.

## Background Knowledge Map: Three Weight Rules, Three Geometric Worlds

- **Affine Combinations ($$\sum \theta_i = 1$$):** Weights can be negative, extending infinitely in both directions; models linear equality constraints $$Ax = b$$.
- **Convex Combinations ($$\sum \theta_i = 1,\; \theta_i \ge 0$$):** Nonnegative probability weights that stay strictly between the generating points; models bounded mixtures and feasible polytopes.
- **Conic Combinations ($$\theta_i \ge 0$$):** Drop the sum-to-one rule while keeping nonnegativity; models scale-invariant cones such as $$\mathbb{R}_+^n$$, second-order cones, and $$\mathbb{S}_+^n$$.
- **Nested Inclusion:** Every affine set is convex, and every convex cone is convex—knowing which tier a constraint belongs to immediately unlocks stronger structural theorems.

### Step-by-Step Worked Example (Read Slowly): One Pair of Points Under Three Combination Rules

Let $$x_1 = (1, 0)^T$$ and $$x_2 = (0, 2)^T$$.

1. **Affine combination ($$\theta_1 = 2, \theta_2 = -1$$, sum $$= 1$$):**
   $$2x_1 - x_2 = 2(1, 0)^T - (0, 2)^T = (2, -2)^T.$$
   Because $$\theta_2 < 0$$, this point lies outside the segment connecting $$x_1$$ and $$x_2$$, yet remains on the infinite line through them.
2. **Convex combination ($$\theta_1 = 0.5, \theta_2 = 0.5$$, nonnegative and sum $$= 1$$):**
   $$0.5x_1 + 0.5x_2 = (0.5, 1)^T,$$
   the exact midpoint of the line segment from $$x_1$$ to $$x_2$$.
3. **Conic combination ($$\theta_1 = 2, \theta_2 = 3$$, nonnegative, sum $$= 5 \neq 1$$):**
   $$2x_1 + 3x_2 = (2, 6)^T,$$
   which stays inside the nonnegative first quadrant (the conic hull of $$x_1, x_2$$) while scaling beyond the line segment.

In this chapter, we will explore the concepts and definitions centered around convex sets. We introduce three types of sets: the most basic is the affine set, and by imposing additional constraints on the affine set, we define the convex set and the cone.

Interestingly, these sets can be thought of as collections of many lines (line), line segments, or rays. An affine set is formed by gathering many lines, a convex set by gathering many line segments, and a cone by gathering many rays. This perspective makes it easier to understand these concepts. Also, a cone is sometimes called a nonnegative homogeneous set, which refers to the property that it extends only in one direction from the origin, helping to clarify the naming.
