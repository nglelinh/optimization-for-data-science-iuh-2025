---
layout: post
title: 13-06 Dual subtleties & Double dual
chapter: '13'
order: 10
owner: Wontak Ryu
categories:
- chapter13
lang: en
---

## Dual subtleties
• Sometimes we can transform dual problems into equivalent problems and still call them dual problems. Also, in strong duality, we can use solutions of transformed dual problems for analyzing or computing characteristics of primal solutions.

#### [Note]
The optimal value of a transformed dual problem is not necessarily the optimal value of the primal.


• A common way to derive dual problems for unconstrained problems is to first transform the primal by adding dummy variables and equality constraints.

Generally, how to do this is ambiguous. Different choices can lead to different dual problems.


## Double dual
Let's consider a general minimization problem with linear constraints:

> $$ \min_x f(x) \text{ subject to } Ax ≤ b, Cx = d$$

The Lagrangian is as follows:
> $$L(x,u,v) = f(x) + (A^Tu + C^Tv)^Tx−b^Tu−d^Tv$$

Therefore, the dual problem is as follows:

> $$ \max_{u,v} −f^∗(−A^Tu−C^Tv)−b^Tu−d^Tv \text{ subject to } u ≥ 0 $$

#### Recall property
If $$f$$ is closed and convex, we explained earlier that the dual of the dual is the primal in this case ($$f^{∗∗} = f$$).

In fact, the connection (between dual and dual conjugate) goes much deeper beyond linear constraints.
Consider the following:

> $$ 
>\begin{align}
> & \min_x && f(x) \\
> &\text{ subject to } && h_i(x) ≤ 0, i = 1,...m \\
> &&&l_j(x) = 0, j = 1,...r
>\end{align}$$

If $$f$$ and $$h_1,...h_m$$ are closed and convex, and $$l_1,...l_r$$ are affine, then the dual of the dual is the primal.

This is provided as a minimization problem from the perspective of bifunctions.

(for more, read Chapters 29 and 30 of Rockafellar)
