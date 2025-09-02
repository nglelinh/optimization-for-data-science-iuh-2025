---
layout: post
title: 15-07 Feasibility methods
chapter: "15"
order: 13
categories:
- chapter16
owner: "Minjoo Lee"
---

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