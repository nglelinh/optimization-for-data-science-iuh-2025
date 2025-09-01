---
layout: post
title: '09-04 Special cases'
chapter: '09'
order: 5
owner: Kyeongmin Woo
categories:
- chapter09
lang: en
---

# Special cases

Proximal gradient descent is also called composite gradient descent or generalized gradient descent.

Why is it called **"generalized”**? The reason is that Proximal gradient descent encompasses all of the following special cases:

- $$h = 0 \to$$ gradient descent
- $$h = I_C \to$$ projected gradient descent 
- $$g = 0 \to$$ proximal minimization algorithm

Therefore, all these algorithms have a convergence rate of $$O(1/\epsilon)$$.

## Projected gradient descent
When $$I_C(x)$$ is the indicator function of a closed convex set $$C \in \mathbb{R}^n$$, the problem of minimizing $$g(x)$$ over the set $$C$$ can be reformulated as follows. (Note: $$C$$ must be a closed set so that the projection is well-defined.)

> $$ \min_{x \in C} g(x) \iff \min_x g(x) + I_C(x)$$
>
> $$I_C(x) = 
>\begin{cases}
>0, & x \in C \\
>\infty, & x \notin C
>\end{cases}$$

At this time, the proximal mapping is defined as follows.

> $$
>\begin{align}
>\text{prox}_t(x)  
>&= \underset{z}{\text{argmin}} \frac{1}{2t} \lVert x−z \rVert_2^2 + I_C(z) \\
>& = \underset{z \in C}{\text{argmin}} \lVert x−z \rVert_2^2
>\end{align} $$

As a result, the proximal mapping $$\text{prox}_t(x) = P_C(x)$$ is the projection operator onto $$C$$.

The proximal gradient update step is: $$x^+ = P_C (x−t \nabla g(x) )$$. In other words, after performing the gradient descent update, you project onto $$C$$.

In the figure below, the pink rectangle is the feasible set $$C$$, and the current position is the upper of the two points below the rectangle. After taking a gradient descent step, you move outside $$C$$, so you project back onto $$C$$ to return inside the feasible set.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/projected_gradient_descent.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Fig1] Projected Gradient Descent [3]]</figcaption>
</p>
</figure>

## Proximal minimization algorithm

Consider the problem of minimizing a convex function $$h$$ as follows. Here, $$h$$ does not need to be differentiable and $$g(x) = 0$$.
>
\begin{align}
\min_x h(x)
\end{align}

The proximal mapping is defined as:
> $$
\begin{align}
x^{(k)} &= \text{prox}_{t_k} \big(x^{(k-1)} - t_k \nabla g ( x^{(k-1)} ) \big) , \qquad k = 1, 2, 3, ... \\
&= \text{prox}_{t_k} \big(x^{(k-1)} \big) ,  \qquad \qquad \qquad \qquad \; k = 1, 2, 3, ... \\
\end{align} $$

Therefore, the proximal gradient update step is:
> $$x^+ = \underset{z}{\text{argmin}} \frac{1}{2t} \lVert x−z \rVert_2^2 + h(z)$$

This proximal gradient method, defined only by $$h$$ with $$g = 0$$, is called the **proximal minimization algorithm (PMA)**. This method is faster than subgradient methods, but if the proximal mapping does not have a closed form, it cannot be implemented.

## What happens if we can't evaluate prox?
Theoretically, when applying proximal gradient to $$f = g + h$$, it is assumed that the prox function can be computed exactly. That is, it is assumed that the minimum can be found exactly via the proximal mapping.
>  $$\text{prox}_t(x )= \underset{z}{\text{argmin}} \frac{1}{2t} \lVert x−z \rVert_2^2 + h(z)$$

In general, it is not clear what happens if the minimum is only approximated.
However, if the error in approximating the prox operator can be precisely controlled, it has been shown that the original convergence rate can be maintained. (Schmidt et al. (2011), Convergence rates of inexact proximal-gradient methods for convex optimization)

In practice, if prox can be computed approximately, it will be performed with high accuracy.
