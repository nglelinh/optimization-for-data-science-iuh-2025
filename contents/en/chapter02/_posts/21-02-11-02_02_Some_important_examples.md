---
layout: post
title: 02-02 Some important examples
chapter: '02'
order: 8
owner: Wontak Ryu
categories:
- chapter02
lang: en
lesson_type: required
---

Just as a chemist learns the periodic table before synthesizing new molecules, an optimization practitioner memorizes a compact catalog of canonical convex sets. Almost every real-world feasible region—whether it is a probability distribution over classes, an uncertainty ellipsoid around a noisy forecast, or a covariance matrix constraint—is built directly from these standard shapes.

## Background Knowledge Map: The Essential Catalog of Convex Sets

- **Linear & Polyhedral Shapes:** Hyperplanes, halfspaces, polyhedra ($$Ax \preceq b, Cx = d$$), and probability simplexes—the geometry of linear programming and categorical probabilities.
- **Norm-Induced & Ellipsoidal Shapes:** Euclidean balls, $$\ell_1/\ell_\infty$$ norm balls, and ellipsoids—central to regularization (Lasso vs. Ridge) and robust uncertainty sets.
- **Conic Shapes:** Norm cones (second-order / Lorentz cones), normal cones, and positive semidefinite cones $$\mathbb{S}_+^n$$—the backbone of SOCP and SDP.
- **Recognizing Structure Fast:** Identifying which canonical set a constraint matches immediately tells you which solver class (LP, QP, SOCP, SDP) can handle it natively.

### Step-by-Step Worked Example (Read Slowly): Testing One Vector Across Three Canonical Convex Sets

Test the point $$x = (0.6, 0.4)^T \in \mathbb{R}^2$$ against three fundamental convex sets:

1. **Probability simplex $$\Delta_2 = \{x \in \mathbb{R}^2 : x_1 + x_2 = 1,\; x_1, x_2 \ge 0\}$$:**
   Both coordinates are nonnegative and $$0.6 + 0.4 = 1$$, so $$x \in \Delta_2$$.
2. **Unit $$\ell_1$$ norm ball $$B_1 = \{x : |x_1| + |x_2| \le 1\}$$:**
   $$\|x\|_1 = |0.6| + |0.4| = 1.0 \le 1$$, so $$x$$ lies exactly on the boundary of $$B_1$$.
3. **Unit $$\ell_2$$ Euclidean ball $$B_2 = \{x : \|x\|_2 \le 1\}$$:**
   $$\|x\|_2 = \sqrt{0.6^2 + 0.4^2} = \sqrt{0.36 + 0.16} = \sqrt{0.52} \approx 0.7211 < 1$$, so $$x$$ lies strictly in the interior of $$B_2$$ (reflecting the geometric inclusion $$B_1 \subset B_2$$).

This section reviews major examples of convex sets.

* Trivial ones: empty set, point, line, line segment, ray
* Hyperplane: $$\{x : a^T x = b\}$$, for given $$a, b$$, $$a \ne 0$$
* Halfspace: $$\{x : a^T x \le b \}$$ for $$a \ne 0$$
* Affine space: $$\{x : Ax = b\}$$, for given $$A, b$$
* Euclidean ball & ellipsoid
* Norm ball: $$\{x : \| x \| \le r\}$$, for given norm $$\|·\|$$, radius $$r$$
* Convex cone: norm cone, normal cone, positive semidefinite cone




