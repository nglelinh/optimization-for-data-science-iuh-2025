---
layout: post
title: 15-07 Feasibility methods
chapter: "15"
order: 13
categories:
- chapter16
owner: "Minjoo Lee"
lang: en
---

Every barrier method lesson so far quietly started with the phrase: *"Choose a strictly feasible point $$x^{(0)}$$ satisfying $$h_i(x^{(0)}) < 0$$ and $$Ax^{(0)} = b$$."* In a 500-dimensional problem with 2,000 intersecting inequalities, finding even *one* strictly feasible point can be just as hard as solving the optimization problem itself! **Phase I feasibility methods** solve this chicken-and-egg puzzle by introducing an auxiliary slack variable $$s$$ that relaxes all constraints just enough to make finding a starting point trivial—and then shrinks $$s$$ until $$s < 0$$!

## Key ideas: Phase I — Finding a Strictly Feasible Starting Point

- **Pillar 1 — Basic Phase I (Maximum Infeasibility):** Solve $$\min_{x,s} s$$ subject to $$h_i(x) \le s$$ and $$Ax = b$$. Any $$x_0$$ satisfying $$Ax_0 = b$$ paired with $$s_0 = \max_i h_i(x_0) + 1$$ is *immediately strictly feasible* for Phase I!
- **Pillar 2 — Early Termination at $$s < 0$$:** You do *not* need to solve Phase I to optimality—the very instant an iterate achieves $$s < 0$$, we have $$h_i(x) \le s < 0$$ for all $$i$$, so $$x$$ is strictly feasible for the original Phase II problem!
- **Pillar 3 — Exact Infeasibility Detection:** If the optimal Phase I value satisfies $$s^\star > 0$$, the original problem is provably infeasible; if $$s^\star = 0$$, no strictly feasible point exists (Slater's condition fails).
- **Pillar 4 — Sum-of-Infeasibilities Variant ($$\min \mathbf{1}^T s$$ s.t. $$h_i(x) \le s_i, s_i \ge 0$$):** Assigning an individual slack $$s_i$$ to each constraint diagnoses *which exact constraints* conflict when a model is infeasible.

### Worked example: Running Phase I on Two Inequality Constraints

We need a strictly feasible point for $$h_1(x) = x - 5 \le 0$$ and $$h_2(x) = -x + 1 \le 0$$ (i.e., $$1 < x < 5$$), starting from an *infeasible* initial guess $$x_0 = 0$$.

1. **Evaluate initial constraint violations at $$x_0 = 0$$:**
   - $$h_1(0) = -5$$ (satisfied), $$h_2(0) = +1$$ (violated!).
   - Maximum violation: $$\max(-5, 1) = 1$$.
2. **Construct a strictly feasible Phase I starting point $$(x_0, s_0)$$:**
   - Pick $$s_0 = \max_i h_i(x_0) + 1 = 1 + 1 = 2$$.
   - Check Phase I strict feasibility: $$h_1(0) - s_0 = -7 < 0$$ and $$h_2(0) - s_0 = -1 < 0$$! We can now launch the barrier method on Phase I.
3. **Solve the Phase I problem $$\min_{x, s} s$$ s.t. $$x - 5 \le s$$, $$1 - x \le s$$:**
   - Adding the two inequalities gives $$-4 \le 2s \implies s \ge -2$$, achieved at $$x^\star = 3, s^\star = -2$$.
   - Even better: as soon as Phase I passes $$(x, s) = (2, -0.5)$$ with $$s = -0.5 < 0$$, we stop immediately—$$x = 2$$ satisfies $$h_1(2) = -3 < 0$$ and $$h_2(2) = -1 < 0$$ and is ready for Phase II!

So far, we have implicitly assumed that the first centering step ($$t = t^{(0)}$$) starts from a strictly feasible point to compute $$x^{(0)} = x^*$$.

This means that $$x$$ is a strictly feasible point satisfying the following conditions:
>$$ h_i(x) \lt 0, \quad i = 1, \cdots, m, \quad Ax = b$$

## Maximum infeasibility
How do we find $$x$$? We can solve the following problem to find it.

>
$$\begin{align}
&\min_{x, s} \        && s \\
&\text{subject to } \ && h_i(x) \le s,& i = 1, \cdots, m \\
                      &&& Ax = b \\
\end{align}$$

The goal is to make the solution $$s$$ negative. This problem is called the **feasibility method**.

Finding a strictly feasible starting point is easy, so it can also be solved using the barrier method. That is, you can add slack variables to the inequality constraint $$h_i(x) \le s$$ and convert it to an equality constraint to solve it.

When solving this problem, high accuracy is not required; you just need to find a feasible $$(x,s)$$ with $$s < 0$$.

## Infeasibility for each inequality constraint 
You can also define and solve the problem as follows. The previous method found the maximum infeasibility for all inequalities, while this problem finds the infeasible variable $$s_i, i = 1, \cdots, m$$ for each inequality.
>
$$\begin{align}
&\min_{x, s} \        && 1^Ts \\
&\text{subject to } \ && h_i(x) \le s_i,& i = 1, \cdots, m \\
                      &&& Ax = b \\
\end{align}$$

The advantage of this method is that by looking at the solution $$s$$, you can tell if the problem is infeasible. That is, if any element of $$s$$ is greater than or equal to 0, the corresponding constraint is not satisfied.