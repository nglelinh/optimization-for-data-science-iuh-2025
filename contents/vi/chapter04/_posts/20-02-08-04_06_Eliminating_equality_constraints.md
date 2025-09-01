---
layout: post
title: 04-06 Eliminating equality constraints
chapter: '04'
order: 7
owner: YoungJae Choung
categories:
- chapter04
lang: vi
---
This section explains techniques for eliminating equality constraints in convex optimization problems to simplify the feasible set or problem structure.

>$$
\begin{aligned}
&\min_{x} &&f(x)\\
&\text{subject to } &&g_{i}(x) \leq 0, i = 1, .., m\\
&&&{Ax = b}.\\
\end{aligned}
$$

For an arbitrary solution $$x_{0}$$ satisfying $$Ax_{0} = b$$ and $$\text{col}(M) = \text{null}(A)$$, any $$x$$ that satisfies the equality constraint can be expressed as follows:
>$$x = My + x_{0}$$

That is, $$Ax = A(My + x_{0}) = AMy + Ax_{0} = 0 + b = b$$. Therefore, by substituting $$My+x_{0}$$ for $$x$$ in the given problem, we can eliminate the equality constraint.

Thus, the following problem is equivalent to the original problem:

>$$
\begin{aligned}
&\min_y &&f(My+x_0)\\
&\text{subject to} &&g_{i}(My+x_{0}) \leq 0, i = 1, .., m.\\
\end{aligned}
$$

However, caution is advised when using this method for the following reasons:
1. The computation of $$M$$ is generally very expensive.
2. If $$x$$ is sparser than $$y$$, the cost of computation using $$y$$ may be higher.
