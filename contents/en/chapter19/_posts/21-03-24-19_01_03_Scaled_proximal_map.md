---
layout: post
title: "19-01-03 Scaled proximal map"
chapter: '19'
order: 5
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

The **proximal Newton method** can be rewritten in the same form as **proximal gradient descent**.

## Scaled proximal map
If $$H \succ 0$$, the **scaled proximal map** is defined as follows.

> \begin{align}
\text{prox}_{H}(x) = \underset{z}{\text{argmin}}  \frac{1}{2} \parallel x - z \parallel_H^2 + h(z)
\end{align}

Here $$\parallel x\parallel_H^2 = x^THx$$ is the squared $$H\text{-norm}$$. When $$H = \frac{1}{t} I$$, this becomes the usual **unscaled proximal map**.

In general, the **scaled proximal map** has the same nice properties as the ordinary prox.

* **uniqueness**: the solution is unique (this holds because $$H \succ 0$$ makes the problem strictly convex).
* **non-expansiveness**: the map does not expand distances (this holds because the scaled proximal map generalizes the projection operator, which is non-expansive).

#### [Note] Non-expansiveness of the projection operator
For two points $$x$$, $$y$$ and the projection operator $$P_C$$ onto a convex set $$C$$, non-expansiveness means $$\parallel P_C(x) - P_C(y) \parallel_2 \le \parallel x - y \parallel_2$$. In other words, $$P_C$$ is 1-Lipschitz, which holds whenever $$C$$ is convex.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.01_03_projection_operator.png" alt="[Fig 1] Projection onto a convex set C [3]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Projection onto a convex set C [3]</figcaption>
</p>
</figure>

## Proximal Newton update
Using the **scaled proximal map**, the proximal Newton update can be rewritten as follows.

> $$
> \begin{align}
> z^{+} & = \underset{z}{\text{argmin}} \ \nabla g(x)^T (z - x) + \frac{1}{2} (z - x)^T H (z - x) + h(z) \\\\
> & =\underset{z}{\text{argmin}} \ \frac{1}{2} \parallel x - H^{-1} \nabla g(x) - z \parallel_H^2 + h(z)
> \end{align}
> $$

Equivalently:

> $$
> \begin{align}
> z^{(k)} & = \text{prox}_{H^{(k-1)}} ( x^{(k-1)} - (H^{(k-1)})^{-1} \nabla g (x^{(k-1)}) ) \\\\
> x^{(k)} & =x^{(k-1)} + t_k (z^{(k)} - x^{(k-1)} )
> \end{align}
> $$

Intuitively, we take a Newton step on $$g$$, apply the scaled prox operator with respect to $$H^{(k-1)}$$, and move in that direction.

From this we see the following.

* When $$h(z) = 0$$, the proximal operator is the identity, and we recover the ordinary Newton update.
* If we replace $$H^{(k-1)}$$ by $$\frac{1}{r_k} I$$ and set $$t_k = 1$$, we obtain the proximal gradient update with step size $$r_k$$.
* The difficulty of the prox depends not only on $$h$$ but also on the structure of the Hessian of $$g$$. For example, if $$H$$ is diagonal or banded, the problem is much easier than when $$H$$ is dense.

Thus, the proximal Newton method generalizes both proximal gradient descent and Newton's method.
