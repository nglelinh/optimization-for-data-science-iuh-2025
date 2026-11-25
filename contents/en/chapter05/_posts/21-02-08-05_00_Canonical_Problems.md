---
layout: post
title: 05 Canonical Problems
chapter: '05'
order: 1
owner: Hooncheol Shin
categories:
- chapter05
lang: en
---

Walk into an ER with a broken wrist and the triage doctor immediately classifies the fracture before ordering a cast—different injuries need different instruments. Convex optimization works the same way: instead of writing a bespoke algorithm for every new problem, practitioners classify models into a nested hierarchy of *canonical forms*—LP, QP, QCQP, SOCP, SDP, and general Conic Programs—each matched to battle-tested, polynomial-time solvers.

## Background Knowledge Map: The Nested Hierarchy of Convex Programs

1. **The Russian-Doll Inclusion Chain**: Every Linear Program (LP) is a special case of a Quadratic Program (QP), which is a special case of a Quadratically Constrained Quadratic Program (QCQP), which embeds into a Second-Order Cone Program (SOCP), which embeds into a Semidefinite Program (SDP), all unified under Conic Programming (CP): $$\mathrm{LP} \subset \mathrm{QP} \subset \mathrm{QCQP} \subset \mathrm{SOCP} \subset \mathrm{SDP} \subset \mathrm{CP}$$.
2. **Expressiveness vs. Computational Cost**: Moving rightward in the hierarchy lets you model richer geometry (polyhedra $$\to$$ ellipsoids $$\to$$ Lorentz ice-cream cones $$\to$$ positive semidefinite matrices), at the price of heavier per-iteration linear algebra. Choosing the *simplest* canonical class that captures your problem can mean a 100× speedup.
3. **Solver Specialization**: LP and QP solvers exploit sparse linear factorizations and active-set/simplex warm starts; SOCP and SDP solvers use primal–dual interior-point methods over self-concordant cone barriers (such as Clarabel, ECOS, or MOSEK).
4. **Canonicalization Bridges Modeling and Solving**: Modeling frameworks like CVXPY automatically rewrite high-level mathematical expressions (like $$\|Ax - b\|_2 + \lambda\|x\|_1$$) into one of these standard cone classes so the user never has to hand-code barrier derivatives.

### Step-by-Step Worked Example (Read Slowly): Classifying One Engineering Model Across the Hierarchy

Suppose a portfolio manager chooses asset weights $$x \in \mathbb{R}^2$$ satisfying $$x_1 + x_2 = 1$$ and $$x_1, x_2 \ge 0$$, with expected return vector $$\mu = (0.08, 0.05)^T$$ and covariance matrix $$\Sigma = \begin{bmatrix} 0.04 & 0.01 \\ 0.01 & 0.02 \end{bmatrix}$$. Watch how changing a single risk term shifts the canonical class:

1. **Linear objective only (LP)**: Maximizing expected return $$\min_x -\mu^T x$$ subject to $$x_1 + x_2 = 1, x \ge 0$$ has a linear objective and linear constraints. Optimal vertex: $$x^\star = (1, 0)$$ with return $$8\%$$.
2. **Adding variance penalty (QP)**: Minimizing $$\frac{1}{2}x^T \Sigma x - \mu^T x$$ keeps linear constraints and adds a convex quadratic objective ($$\Sigma \succ 0$$ since $$0.04 > 0$$ and $$\det \Sigma = 0.0008 - 0.0001 = 0.0007 > 0$$). This is a **QP**.
3. **Capping portfolio variance (QCQP / SOCP)**: Requiring $$x^T \Sigma x \le 0.0225$$ while maximizing $$\mu^T x$$ adds a convex quadratic inequality (**QCQP**). Factoring $$\Sigma = L L^T$$ rewrites it as $$\|L^T x\|_2 \le 0.15$$, a **Second-Order Cone (SOCP)** constraint.
4. **Testing a specific point**: At $$x = (0.5, 0.5)$$, expected return is $$0.5(0.08) + 0.5(0.05) = 0.065$$ and variance is $$0.25(0.04) + 2(0.25)(0.01) + 0.25(0.02) = 0.01 + 0.005 + 0.005 = 0.020 \le 0.0225$$, confirming feasibility for the QCQP/SOCP risk cap.

# Canonical Problems

In [Chapter 1](/chapter01/2021/01/07/optimization_problems/), we learned that a convex optimization problem is defined as follows:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_00_optimization_problem.png" alt="[Fig1] Convex Optimization Problem in standard form [3]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Convex Optimization Problem in standard form [3]</figcaption>
</p>
</figure>

* The domain set is convex
* The objective function $$ f $$ and the inequality constraint function $$ g_i $$ are convex
* The equality constraint function $$ h_j $$ is affine

Depending on the type of objective and constraint functions, optimization problems are classified into several categories. In this chapter, we will learn about six major subclasses:

- Linear Programming (LP)
- Quadratic Programming (QP)
- Quadratically Constrained Quadratic Programming (QCQP)
- Second-Order Cone Programming (SOCP)
- Semidefinite Programming (SDP)
- Conic Programming (CP)

These problems have the following inclusion relationships and become more general as you move down the list:

$$ LP \subseteq QP \subseteq QCQP \subseteq SOCP \subseteq SDP \subseteq CP $$
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_00_canonical_problems.jpeg" alt="[Fig2] Canonical Problems" width="90%">
  <figcaption style="text-align: center;">[Fig2] Canonical Problems</figcaption>
</p>
</figure>

After the taxonomy and the DCP lab, the optional [05-08 Applications and recent developments]({% multilang_post_url contents/chapter05/2026-09-16-05_08_Applications_Recent %}) points at Clarabel, portfolio QPs, SDP verification, and unrolled sparse recovery.