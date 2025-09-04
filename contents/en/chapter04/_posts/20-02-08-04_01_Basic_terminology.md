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
