---
layout: post
title: 24 Mixed Integer Programming (part I)
chapter: '24'
order: 1
owner: YoungJae Choung
categories:
- chapter24
lang: en
---

Up through Chapter 23, every variable lived in a smooth, connected continuum—you could always nudge a weight by $$0.001$$ and ask the gradient which way is downhill. The real world is rarely so forgiving: you cannot build $$0.37$$ of a warehouse, assign $$0.6$$ of a pilot to a flight, or select $$0.4$$ of a feature in a clinical diagnostic model. The moment even a subset of decision variables is forced to take discrete integer values, convexity shatters and gradients lose their local authority. Mixed Integer Programming (MIP) is the mathematical discipline that tames this combinatorial cliff—not by brute-force enumeration, but by pairing clever continuous relaxations with systematic tree search.

## Background Knowledge Map: Entering the World of Mixed Integer Programming

- **Discrete vs. Continuous Coupling:** A Mixed Integer Program optimizes an objective over both continuous variables $$x \in \mathbb{R}^p$$ and integer variables $$y \in \mathbb{Z}^q$$. Even when the objective and constraints are linear, restricting $$y$$ to $$\mathbb{Z}^q$$ renders the feasible set nonconvex and NP-hard in general.
- **Modeling Power of Binary Variables:** Restricting $$y_j \in \{0, 1\}$$ lets you encode logical implications ("if facility $$i$$ is open, then customer $$j$$ can be served"), cardinality caps ("pick at most $$k$$ features"), and piecewise-linear or indicator constraints inside algebraic inequalities.
- **Primal–Dual Bounding Framework:** Because local optimality no longer implies global optimality, MIP solvers maintain two opposing fences: an incumbent feasible integer solution giving an upper bound (for minimization) and a tractable relaxation giving a certified lower bound.
- **Relaxation + Branching Synergy:** Solving the continuous LP/convex relaxation yields a fractional solution; splitting the feasible region around a fractional variable (Branch and Bound) progressively tightens the gap until the primal and dual bounds meet.

### Step-by-Step Worked Example (Read Slowly): Why Rounding an LP Relaxation Can Fail

Consider the 2-variable integer linear program:
$$\max_{x_1, x_2 \in \mathbb{Z}_{\ge 0}} x_1 + 5 x_2 \quad \text{subject to} \quad x_1 + 10 x_2 \le 20,\quad x_1 \le 2.$$

1. **Solve the LP relaxation (dropping integrality):** To maximize $$x_1 + 5x_2$$, push $$x_2$$ as high as possible. Setting $$x_1 = 0$$ allows $$x_2 = 20 / 10 = 2$$, giving objective $$10$$. Pushing $$x_1 = 2$$ forces $$x_2 = 18 / 10 = 1.8$$, giving $$2 + 5(1.8) = 11$$. Thus the LP optimum is $$x_{\text{LP}} = (2, 1.8)^\top$$ with value $$11$$.
2. **Try naive rounding:**
   - Rounding $$x_2 = 1.8$$ **up** to $$2$$ gives $$(2, 2)$$—**infeasible**, since $$2 + 10(2) = 22 > 20$$!
   - Rounding $$x_2 = 1.8$$ **down** to $$1$$ gives $$(2, 1)$$—feasible, with objective $$2 + 5(1) = 7$$.
3. **Find the true integer optimum:** Setting $$x_1 = 0, x_2 = 2$$ is feasible ($$0 + 20 \le 20$$) and achieves objective $$0 + 5(2) = 10 > 7$$!
   Notice that the true integer optimum $$(0, 2)$$ is **not** any simple rounding of $$(2, 1.8)$$—showing why MIP requires systematic branching and bounding rather than post-hoc rounding.

This chapter introduces the definition, relationships, and examples of Mixed Integer Programming, and presents methods for finding optimal solutions by indirectly utilizing relaxation to find solutions for Integer programming.

## 2026 applications (optional)

Assignment, knapsack, and facility location are not museum pieces: crew pairing (MIPLIB air05), last-mile routing with learned demand, and warehouse / edge-GPU siting reuse the 24-02 templates. A second industry — learning to branch inside branch-and-bound — grew around those models after NeurIPS 2019. See [24-06 Modern applications of mixed-integer models]({% multilang_post_url contents/chapter24/2026-09-16-24_06_modern_applications %}). Feature selection, neural-net verification, and optimal trees wait for Chapter 25.
