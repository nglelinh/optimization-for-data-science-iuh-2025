---
layout: post
title: 08-01-08 Projected Subgradient Method
chapter: "08"
order: 10
owner: "Kyeongmin Woo"
---

The method described in the previous example is called the projected subgradient method. This algorithm can be used for convex problems with constraints.

If we denote the domain that satisfies the constraints as the set $$C$$, then a constrained convex problem is defined as follows:

>
$$ \begin{align}
\min_x \text{ }f(x) \quad \text{subject to } x \in C
\end{align} $$

By using the projected subgradient method, such problems can be solved relatively easily. The projected subgradient method is similar to the standard subgradient method, but at each iteration, the result is projected onto the set $$C$$.

>
$$ \begin{align}
x^{(k)} = P_c(x^{(k-1)} - t_k \cdot g^{(k-1)}), \quad k = 1,2,3,...
\end{align} $$

If projection is possible, this method has the same convergence properties and rate as the subgradient method.

One thing to note about the projected subgradient method is that even if $$C$$ is a simple convex set, if the projection operation $$P_c$$ is difficult, the overall problem also becomes hard to solve. Typically, the following sets $$C$$ are relatively easy to project onto:

- Affine images: {$$Ax=b : x \in \mathbb{R}^{n}$$}
- Solution set of linear system: {$$x: Ax=b$$}
- Nonnegative orthant: $$\mathbb{R}_+^{n} =  $${$$x: x\ge 0$$}
- Some norm balls: {$$x: \lVert x \rVert _p \le 1 $$} for $$p=1,2,\infty$$
- Some simple polyhedra and simple cones
