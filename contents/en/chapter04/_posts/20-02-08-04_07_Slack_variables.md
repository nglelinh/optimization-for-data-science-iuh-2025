---
layout: post
title: 04-07 Slack variables
chapter: '04'
order: 8
owner: YoungJae Choung
categories:
- chapter04
lang: en
lesson_type: required
---
This section introduces slack variables, which are used to convert inequality constraints into equality constraints in convex optimization problems.

>$$
\begin{aligned}
&\min_x &&f(x) \\
&\text{subject to} &&g_{i}(x) \leq 0, i = 1, .., m\\
&&&Ax = b.\\
\end{aligned}
>$$

The above convex problem is equivalent to the following problem.

>$$
>\begin{aligned}
&\min_{x, s} &&f(x)\\
&\text{subject to} &&s_{i} \geq 0, i = 1, .., m\\
&&&g_{i}(x) + s_{i} = 0, i = 1,...m\\
&&&Ax = b.\\
\end{aligned}
$$

Note that if $$g_{i}, i = 1, \dotsc, m$$ are not affine, the above problem is no longer a convex problem.
