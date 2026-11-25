---
layout: post
title: 04-01 Basic terminology
chapter: '04'
order: 2
owner: YoungJae Choung
categories:
- chapter04
lang: en
lesson_type: required
---

Before a pilot can fly by instruments, every dial on the cockpit panel needs an unambiguous name. In convex optimization, confusing the *domain* with the *feasible set*, or an *optimal value* with an *optimal point*, leads directly to broken proofs and silent modeling bugs. This lesson builds the exact vocabulary—feasible points, optimal values, active constraints, and local versus global minimizers—that every subsequent theorem in convex analysis relies on.

## Key ideas: Core Vocabulary of Convex Programs

1. **Implicit Domain vs. Feasible Set**: Every problem starts with the implicit intersection of function domains $$D = \operatorname{dom}(f) \cap \bigcap_i \operatorname{dom}(g_i) \cap \bigcap_j \operatorname{dom}(h_j)$$. The *feasible set* $$C \subseteq D$$ further filters $$D$$ to points satisfying all inequalities $$g_i(x) \le 0$$ and affine equalities $$h_j(x) = 0$$.
2. **Optimal Value $$f^\star$$ vs. Optimal Points $$x^\star$$**: The optimal value $$f^\star = \inf_{x \in C} f(x)$$ always exists in $$\mathbb{R} \cup \{-\infty, +\infty\}$$ (with $$+\infty$$ for infeasible problems and $$-\infty$$ for unbounded-below problems). However, an *attaining* optimal point $$x^\star \in C$$ with $$f(x^\star) = f^\star$$ need not exist—for example, minimizing $$e^{-x}$$ over $$\mathbb{R}$$ has $$f^\star = 0$$ with no finite minimizer.
3. **Active vs. Inactive Inequality Constraints**: At a feasible point $$x$$, an inequality $$g_i(x) \le 0$$ is *active* (binding) if $$g_i(x) = 0$$ and *inactive* (strictly satisfied) if $$g_i(x) < 0$$. Active constraints are the walls you are actually pressed against at the optimum; inactive constraints can be locally ignored without moving $$x^\star$$.
4. **Local vs. Global Optimality under Convexity**: A point $$x$$ is locally optimal if it minimizes $$f$$ inside some ball $$\|y - x\|_2 \le R$$ intersected with $$C$$. Because every line segment connecting a local minimizer to a strictly better feasible point stays inside $$C$$ and has objective values bounded by convexity, any local minimizer of a convex problem is automatically globally optimal.

### Worked example: Dissecting Domain, Feasibility, and Active Constraints

Consider the one-dimensional convex optimization problem:
$$\text{minimize} \quad f(x) = -\ln(x) + \frac{1}{2}x^2 \quad \text{subject to} \quad g_1(x) = x - 2 \le 0, \quad g_2(x) = \frac{1}{2} - x \le 0.$$

1. **Identify the implicit domain $$D$$**: The logarithm requires $$x > 0$$, while $$x^2$$ and both constraints are defined on all of $$\mathbb{R}$$. Therefore $$D = (0, +\infty)$$.
2. **Determine the feasible set $$C$$**: Constraint $$g_1(x) \le 0$$ gives $$x \le 2$$, and constraint $$g_2(x) \le 0$$ gives $$x \ge \frac{1}{2}$$. Intersecting with $$D$$ yields the closed interval $$C = [\tfrac{1}{2}, 2]$$.
3. **Verify convexity and locate the unconstrained minimizer**: On $$D$$, $$f'(x) = -\frac{1}{x} + x$$ and $$f''(x) = \frac{1}{x^2} + 1 > 0$$, so $$f$$ is strictly convex. Setting $$f'(x) = 0$$ gives $$x = \frac{1}{x} \implies x^2 = 1$$. Since $$x \in D = (0, \infty)$$, the unique unconstrained minimizer is $$x^\star = 1$$.
4. **Check feasibility, optimal value, and active constraints**: Since $$1 \in [\tfrac{1}{2}, 2]$$, $$x^\star = 1$$ is feasible and achieves the global optimal value $$f^\star = -\ln(1) + \frac{1}{2}(1)^2 = 0.5$$. Evaluating the constraints at $$x^\star = 1$$ gives $$g_1(1) = 1 - 2 = -1 < 0$$ and $$g_2(1) = \frac{1}{2} - 1 = -0.5 < 0$$, so **both inequality constraints are inactive** at the optimum.
5. **Contrast with a shifted constraint**: If we tighten $$g_1$$ to $$g_1(x) = x - 0.8 \le 0$$, then $$x = 1$$ becomes infeasible. Because $$f'(x) = x - 1/x < 0$$ on $$[0.5, 0.8]$$, $$f$$ is strictly decreasing on the feasible interval, so the new optimum is $$x^\star = 0.8$$ with $$g_1(0.8) = 0$$ (**active**) and $$g_2(0.8) = -0.3 < 0$$ (**inactive**).

## Convex Optimization Basics

Let's review the basic terminology used in convex optimization problems. A convex optimization problem is defined as:

>$$
\begin{aligned}
&\text{minimize}_{x \in D} &&{f(x)} \\
&\text{subject to} &&{g_{i}(x) \leq 0, \quad i = 1, \dotsc, m} \\
&&&{h_{j}(x) = 0, \quad j = 1, \dotsc, r},\\\\
\end{aligned}
$$

>where $$f$$ and $$g_{i}$$, $$i=1,\dotsc, m$$ are all convex,
>$$h_j, j = 1, \dotsc, r$$ are all affine,
>and the optimization domain is $$D = dom(f) \cap \bigcap_{i=1}^{m} dom(g_{i}) \cap  \bigcap_{j=1}^r dom(h_{j})$$.

* $$f$$ is called the **criterion** or **objective function**.
* $$g_{i}(x)$$ is called the **inequality constraint function**.
* $$h_{j}(x)$$ is called the **equality constraint function**.
* If $$x \in D$$ and $$g_{i}(x) \leq 0$$ for all $$i$$ and $$h_{j}(x) = 0$$ for all $$j$$, then $$x$$ is a **feasible point**.
* For all feasible points $$x$$, the minimum value of $$f(x)$$ is called the **optimal value**, denoted as $$f^{\star}$$.
* If $$x$$ is feasible and $$f(x) = f^{\star}$$, then $$x$$ is called **optimal**, a **solution**, or a **minimizer**.
* If $$x$$ is feasible and $$f(x) \le f^{\star} + \epsilon$$, then $$x$$ is called **$$\epsilon$$-suboptimal**.
* If $$x$$ is feasible and $$g_i(x) = 0$$, then $$g_i$$ is **active** at $$x$$.
* A convex minimization problem can be converted to a concave maximization problem.

>$$
\begin{aligned}
&\text{maximize}_{x \in D} &&-f(x)\\
&\text{subject to} &&g_{i}(x) \leq 0, i = 1, .., m\\
&&&h_{j}(x) = 0, j = 1, \dotsc, r,\\\\
\end{aligned}
$$

>where $$f$$ and $$g_{i}$$, $$i=1,\dotsc, m$$ are all convex,
>$$h_j, j = 1, \dotsc, r$$ are all affine,
>and the optimization domain is $$D = dom(f) \cap \bigcap_{i=1}^{m} dom(g_{i}) \cap  \bigcap_{j=1}^r dom(h_{j})$$.

### Feasible Set

A feasible set (also known as a feasible region or solution space) is the set of all feasible points. It represents all the choices that are allowed by the problem's conditions.

The feasible set, often denoted by $$S$$ or $$\mathcal{F}$$, is defined as:

> $$ S = \{ \mathbf{x} \in X \mid g_i(\mathbf{x}) \le 0 \text{ for all } i=1, \dots, m, \text{ and } h_j(\mathbf{x}) = 0 \text{ for all } j=1, \dots, r \} $$

### Properties of Feasible Sets

1.  **Convexity:** If all inequality constraint functions $g_i(\mathbf{x})$ are convex and all equality constraint functions $h_j(\mathbf{x})$ are affine (linear), then the feasible set $S$ is a **convex set**. This property is crucial in convex optimization, as it guarantees that any local optimum is also a global optimum.
2.  **Boundedness:** A feasible set can be **bounded** (enclosed within a finite region) or **unbounded** (extending infinitely in some direction).
3.  **Empty Set:** It is possible for the feasible set to be empty ($S = \emptyset$). This means there are no points that satisfy all the given constraints, and the optimization problem is said to be **infeasible**.
4.  **Polytope/Polyhedron** (**Đa hình / Đa diện**): In linear programming, if the feasible set is non-empty and bounded, it is called a **polytope**. If it is non-empty but potentially unbounded, it is called a **polyhedron**. Both are convex sets.
5.  **Vertices (Extreme Points):** For linear programming problems, if an optimal solution exists, it can always be found at one of the vertices (also known as extreme points or corner points) of the feasible set. This is the basis for algorithms like the Simplex method.