---
layout: post
title: 05-01-01 Linear Programming - Simplex Algorithm
chapter: '05'
order: 3
owner: Hooncheol Shin
categories:
- chapter05
lang: en
lesson_type: required
---

A high-dimensional polytope with 1,000 constraints can easily have more vertices than atoms in the observable universe—enumerating them all is impossible. Dantzig's Simplex Algorithm solves this in breathtaking geometric style: instead of visiting every corner, it stands at one vertex, checks which adjacent edges slope strictly downhill, and walks along the polytope's skeleton until every neighboring edge goes uphill.

## Background Knowledge Map: Mechanics of the Simplex Method

1. **Basic Feasible Solutions (BFS) = Vertices**: In standard form $$Ax = b, x \ge 0$$ with $$A \in \mathbb{R}^{m \times n}$$ of full row rank $$m$$, partitioning columns into an invertible basis $$B$$ ($$m$$ columns) and nonbasic set $$N$$ ($$n - m$$ columns) sets $$x_N = 0$$ and $$x_B = B^{-1}b$$. Whenever $$x_B \ge 0$$, this algebraic partition corresponds directly to a geometric vertex of the polyhedron.
2. **Reduced Costs as Edge Slopes**: Moving a single nonbasic variable $$x_j$$ up from $$0$$ forces $$x_B = B^{-1}b - B^{-1}A_j x_j$$ and changes the objective at rate $$\bar{c}_j = c_j - c_B^T B^{-1} A_j$$. If all $$\bar{c}_j \ge 0$$, no feasible edge improves the objective and the current BFS is globally optimal.
3. **Minimum-Ratio Test (Choosing the Leaving Variable)**: Once an entering variable $$x_j$$ with $$\bar{c}_j < 0$$ is chosen, we increase $$x_j$$ as far as possible until the first basic variable hits zero: $$t^\star = \min_{i : d_i > 0} \frac{(x_B)_i}{d_i}$$ where $$d = B^{-1}A_j$$. If $$d \le 0$$, the LP is unbounded below.
4. **Degeneracy and Cycling**: If some basic variable already equals $$0$$, a pivot can take step size $$t^\star = 0$$ (changing the basis without moving in space). Bland's rule—always picking the smallest-index entering and leaving variables—guarantees finite termination without cycling.

### Step-by-Step Worked Example (Read Slowly): Executing One Exact Simplex Pivot by Hand

Minimize $$-3x_1 - 2x_2$$ subject to $$x_1 + x_2 + s_1 = 4$$, $$2x_1 + x_2 + s_2 = 6$$, with $$x_1, x_2, s_1, s_2 \ge 0$$.

1. **Start at the slack basis $$B = \{s_1, s_2\}$$, $$N = \{x_1, x_2\}$$**:
   - Here $$B = I_2$$, $$c_B = (0, 0)^T$$, so $$x_B = (s_1, s_2)^T = (4, 6)^T$$ and objective $$z = 0$$.
   - Reduced costs for $$N$$: $$\bar{c}_1 = -3 - 0 = -3 < 0$$, $$\bar{c}_2 = -2 - 0 = -2 < 0$$.
2. **Choose entering variable $$x_1$$** (most negative reduced cost, $$\bar{c}_1 = -3$$):
   - Direction vector: $$d = B^{-1} A_1 = (1, 2)^T$$.
   - Minimum-ratio test: $$\min\left(\frac{4}{1}, \frac{6}{2}\right) = \min(4, 3) = 3$$, attained by the second row ($$s_2$$).
   - Thus $$s_2$$ leaves the basis and $$x_1$$ enters at value $$x_1 = 3$$, while $$s_1 = 4 - 1(3) = 1$$ and $$z = -3(3) = -9$$.
3. **Compute reduced costs at the new basis $$B = \{s_1, x_1\}$$**:
   - Express basic variables in terms of nonbasic $$\{x_2, s_2\}$$: from $$2x_1 + x_2 + s_2 = 6$$, we get $$x_1 = 3 - \tfrac{1}{2}x_2 - \tfrac{1}{2}s_2$$.
   - Substituting into the objective: $$z = -3\bigl(3 - \tfrac{1}{2}x_2 - \tfrac{1}{2}s_2\bigr) - 2x_2 = -9 - \tfrac{1}{2}x_2 + \tfrac{3}{2}s_2$$.
   - The new reduced costs are $$\bar{c}_{x_2} = -\tfrac{1}{2} < 0$$ and $$\bar{c}_{s_2} = +\tfrac{3}{2} > 0$$, so one more pivot (bringing $$x_2$$ in and $$s_1$$ out) will reach the optimal vertex $$(x_1, x_2) = (2, 2)$$ with $$z^\star = -10$$.

The [linear program]({% multilang_post_url contents/chapter05/21-02-08-05_01_Linear_Programming_(LP) %}) from the previous lesson has a polyhedral feasible set. A remarkable geometric fact makes LP special: **if a finite optimum exists, at least one optimal point is a vertex**. The simplex algorithm walks from vertex to vertex, improving the objective, until no neighboring vertex is better.

Interactive tableau: [simplex demo](https://github.com/nglelinh/interactive_math/blob/main/linear-programming/simplex_optimization_demo.html) in `nglelinh/interactive_math`.

<div class="content-box insight-box">
<strong>Key insight:</strong> gradient methods wander through the interior. Simplex stays on the skeleton of the polyhedron and only evaluates corners. That is why a 1950s algorithm still solves many of the LPs behind blending, routing, and SVM duals.
</div>

## Standard form

Most textbooks implement simplex on an equality form with nonnegative variables:

$$
\begin{align}
\underset{x}{\text{minimize}} \quad & c^\top x \\
\text{subject to} \quad & Ax = b, \\
& x \succeq 0,
\end{align}
$$

where $$A \in \mathbb{R}^{m \times n}$$ has full row rank $$m$$, $$b \succeq 0$$, and $$n > m$$. Inequality constraints $$Gx \preceq h$$ are converted by adding nonnegative **slack** variables. Free variables are split as a difference of two nonnegative variables.

A **basis** is a set of $$m$$ linearly independent columns of $$A$$. Write $$A = [A_B \; A_N]$$ after permuting columns, and split $$x = (x_B, x_N)$$. The corresponding **basic solution** is

$$
x_B = A_B^{-1} b, \qquad x_N = 0.
$$

If $$x_B \succeq 0$$, the point is a **basic feasible solution (BFS)** — geometrically, a vertex of the feasible polyhedron.

## Reduced costs and a pivot

From $$Ax = b$$ we can eliminate the basic variables:

$$
x_B = A_B^{-1}b - A_B^{-1}A_N x_N.
$$

Substitute into the objective:

$$
c^\top x = c_B^\top A_B^{-1}b + \bar{c}_N^\top x_N, \qquad \bar{c}_N^\top := c_N^\top - c_B^\top A_B^{-1}A_N.
$$

The vector $$\bar{c}_N$$ contains the **reduced costs**. Because $$x_N \succeq 0$$:

- if $$\bar{c}_N \succeq 0$$, no feasible increase of a nonbasic variable can decrease the objective — the BFS is **optimal**;
- if some $$\bar{c}_j < 0$$, we may increase that nonbasic coordinate (it **enters** the basis) and drive one basic variable to zero (it **leaves**). The ratio test picks the leaving index so that $$x_B$$ stays nonnegative.

One such exchange is a **pivot**. After a finite number of pivots (assuming a rule that prevents cycling, e.g. Bland’s rule), simplex either reports optimality or detects an unbounded ray ($$Ax = 0$$, $$x \succeq 0$$, $$c^\top x < 0$$).

## A two-variable walk-through

Maximize $$3x_1 + 2x_2$$ (equivalently minimize $$-3x_1-2x_2$$) subject to

$$
\begin{align}
x_1 + x_2 &\le 4, \\
2x_1 + x_2 &\le 6, \\
x_1, x_2 &\ge 0.
\end{align}
$$

Vertices of the feasible polygon are $$(0,0)$$, $$(3,0)$$, $$(2,2)$$, and $$(0,4)$$. Objective values: $$0$$, $$9$$, $$10$$, $$8$$. Simplex can start at the origin and pivot to $$(3,0)$$ then $$(2,2)$$, where both reduced costs are nonnegative. The same conclusion is immediate from the figure: the level lines of $$3x_1+2x_2$$ last touch the polygon at $$(2,2)$$.

## Why we still teach it in a data-science course

- **Modeling check.** If you can put a problem in LP standard form, you already know it is convex and that a vertex solution exists.
- **Duality preview.** Reduced costs are dual slacks. Complementary slackness in [Chapter 12]({% multilang_post_url contents/chapter12/21-04-02-12_00_KKT_conditions %}) is the optimality certificate simplex is hunting.
- **Solvers.** Production codes (HiGHS, Gurobi, `scipy.optimize.linprog`) use revised simplex and/or interior-point methods. You will rarely code a tableau, but you should recognize an infeasible vs unbounded return.

**Complexity note.** Klee–Minty cubes show that some pivot rules take exponentially many steps in the worst case. In practice, simplex is often fast; interior-point methods (Chapters 15–17) have polynomial worst-case guarantees and dominate some large sparse LPs. For data-science models that are *already* LPs or QPs — diet problems, maximum-margin SVM duals, basis pursuit — you typically call a modeling layer such as CVXPY (see the DCP lab in this chapter) rather than pivoting by hand.

### The simplex method in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/simplex-pivots_en.mp4"></video>
</div>

Walking the vertices of the lesson's LP: entering variable, ratio test, pivots, the dual solution, and an unbounded problem.

## Exercises

1. Convert $$x_1 - x_2 \le 3$$, $$x_1 \ge 0$$, $$x_2$$ free into standard form.
2. Starting from $$(0,0)$$ in the example above, compute the first entering variable if you always pick the most negative reduced cost.
3. Give a 2-D LP that is feasible and unbounded, and explain how the ratio test fails.

Further reading: Boyd & Vandenberghe, Appendix B; Nocedal & Wright, Ch. 13; the CMU canonical-problems notes linked from the [README]({{ site.baseurl }}/).
