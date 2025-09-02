---
layout: post
title: 04-03 First order optimality condition
chapter: '04'
order: 4
owner: YoungJae Choung
categories:
- chapter04
lang: en
---
>$$
\begin{aligned}
&\min_x &&f(x) \\
&\text{subject to} &&x \in C
\end{aligned}
$$

For a convex problem where the objective function $$f$$ is differentiable, the following condition is necessary and sufficient for an optimal point $$x$$:

> $$\nabla f(x)^{T}(y-x) \geq 0 \\
> \text{ for all } y \in C$$

This is called the *first-order condition for optimality*. 

$$\nabla f(x)^{T}(y-x) = 0$$ defines a hyperplane passing through $$x$$ in set $$C$$, and $$- \nabla f(x)$$ points in the direction of movement toward the optimal point $$x$$. <br><br>

If the above condition is satisfied, 
set $$C$$ is contained in the half-space opposite to $$- \nabla f(x)$$, 
so $$x$$ is an optimal point.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter04/first-order-condition.png" alt="[Fig1] geometric interpretation of first-order condition for optimality [3]">
  <figcaption style="text-align: center;">[Fig1] geometric interpretation of first-order condition for optimality [3]</figcaption>
</p>
</figure>
<br>

### Important special case
When $$C = \mathbb{R}^n$$ (unconstrained optimization),
the optimality condition is:
> $$\nabla f(x) = 0$$

In this case, $$-\nabla f(x)$$ points toward the optimal point $$x$$, and $$\nabla f(x) = 0$$ means there is no further direction to move to decrease $$f$$ at $$x$$.
