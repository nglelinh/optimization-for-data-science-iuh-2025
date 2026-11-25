---
layout: post
title: 02 Convex Sets
chapter: '02'
order: 1
owner: Wontak Ryu
categories:
- chapter02
lang: en
---

Imagine a warehouse robot navigating between two valid storage configurations $$x$$ and $$y$$: if the feasible region of collision-free states is *convex*, then the straight-line blend $$\theta x + (1-\theta)y$$ is automatically collision-free at every intermediate step. Chapter 02 develops the complete geometric language of convex sets—from lines and hyperplanes to cones, generalized inequalities, and separating hyperplanes—that underpins every feasibility proof and duality theorem in optimization.

## Background Knowledge Map: The Geometric Roadmap of Chapter 02

- **Primitive Building Blocks (Affine, Convex, Conic):** Distinguish unconstrained linear combinations (affine sets), weighted averages (convex sets), and nonnegative scalings (convex cones).
- **Canonical Feasible Regions:** Master the core library of convex sets—hyperplanes, halfspaces, Euclidean balls, ellipsoids, polyhedra, simplexes, and the positive semidefinite cone $$\mathbb{S}_+^n$$.
- **Convexity-Preserving Calculus:** Prove complex feasible sets are convex effortlessly via intersections, affine images/preimages, and perspective maps rather than brute-force algebraic checks.
- **Separation & Duality Geometry:** Separating and supporting hyperplanes and dual cones $$K^*$$ turn geometric disjointness into linear optimality certificates (the root of Lagrange duality).

### Step-by-Step Worked Example (Read Slowly): Solid Disk vs. Hollow Circle

Compare the unit disk $$D = \{x \in \mathbb{R}^2 : \|x\|_2 \le 1\}$$ and the unit circle $$S = \{x \in \mathbb{R}^2 : \|x\|_2 = 1\}$$ using endpoints $$x = (1, 0)^T$$ and $$y = (0, 1)^T$$.

1. **Form the midpoint ($$\theta = 0.5$$):**
   $$m = 0.5 x + 0.5 y = (0.5, 0.5)^T.$$
2. **Compute its Euclidean norm:**
   $$\|m\|_2 = \sqrt{0.5^2 + 0.5^2} = \sqrt{0.5} \approx 0.7071.$$
3. **Conclude convexity:**
   - For $$D$$, $$\|m\|_2 \approx 0.7071 \le 1$$ (in fact, by the triangle inequality, $$\|\theta x + (1-\theta)y\|_2 \le \theta\|x\|_2 + (1-\theta)\|y\|_2 \le 1$$ for all $$x, y \in D$$), proving $$D$$ is **convex**.
   - For $$S$$, $$\|m\|_2 \neq 1 \implies m \notin S$$, proving the hollow circle $$S$$ is **nonconvex**.

In this chapter, we will study the concept of convex sets, which form the foundation of convex optimization.

### Background
Convex optimization refers to techniques for finding maxima or minima by defining problems using convex functions.
Convex sets are closely related to convex functions in two main ways:

* Convex functions are defined over convex sets. The domain and range of a function are defined as convex sets, and the main properties of convex functions are determined by these sets.
* If you can transform an optimization problem into one involving a convex function, it becomes easier to solve. Sometimes, it is difficult to determine whether a problem is defined by a convex function. In such cases, you can check whether the epigraph of the function is a convex set to determine if the function is convex.

### Content
In this chapter, we will cover the definition and examples of convex sets, their main properties, and operations that preserve convexity.

See also the optional [02-07 Applications and recent developments]({% multilang_post_url contents/chapter02/2026-09-16-02_07_Applications_Recent %}) on simplices, Wasserstein balls, and fairness polytopes.
