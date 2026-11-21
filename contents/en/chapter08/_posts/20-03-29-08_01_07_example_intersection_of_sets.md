---
layout: post
title: "08-01-07 Example: Intersection of sets"
chapter: '08'
order: 9
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

Suppose we want to find a point in the intersection of several closed convex sets.

First, let $$f_i(x)$$ be the distance from a point $$x$$ to the set $$C_i$$, and let $$f(x)$$ be the maximum of the distances from $$x$$ to all the sets $$C_i, i=1,...,m$$:
>
$$ \begin{align}
f_i(x) & = \mathbb{dist}(x, C_i), \quad i=1,...,m \\
f(x) & = \max_{i=1,...,m}\text{ }f_i(x)
\end{align} $$

Using these two functions, the problem of finding a point in the intersection of the convex sets can be formulated as the following minimization problem:

>
$$ \begin{align}
\min_{x}\text{ }f(x)
\end{align} $$

Finding a point in the intersection of the convex sets is equivalent to finding the point $$x$$ that minimizes the maximum distance $$f(x)$$ to the sets $$C_i$$. In this case, the objective function $$f(x)$$ is convex. If the sets have a common point, then $$f^* = 0$$ and the optimal point is $$x^* \in C_1 \cap C_2 \cap ... \cap C_m$$.

## Gradient of distance function

In [the previous section]({% multilang_post_url contents/chapter07/21-03-25-07_03_05_example_distance_to_convex_set %}), we defined the distance to a convex set as $$dist(x, C_i) = \min_{y \in C} \lVert y-x \rVert _2$$, and saw that its gradient is:

>
$$ \begin{align}
\partial dist(x,C) = \frac{x-P_C(x)}{ \Vert x-P_C(x) \Vert_2}
\end{align} $$

Here, $$P_C(x)$$ is the projection of the point $$x$$ onto the set $$C$$.

## Subdifferential of finite pointwise maximum

The subdifferential of the finite pointwise maximum function $$f(x)=\max_{i=1,...,m}\text{ }f_i(x)$$ is given by

>
$$ \begin{align}
\partial f(x) = \text{conv}\left(\bigcup_{i:f_i(x)=f(x)} \partial f_i(x)\right)
\end{align} $$

That is, the subdifferential of $$f$$ at $$x$$ is the convex hull of the union of the subdifferentials $$\partial f_i(x)$$ of all the functions $$f_i$$ that attain the maximum at $$x$$.

In particular, if $$f_i(x) = f(x)$$ and $$g_i \in \partial f_i(x)$$, then $$g_i \in \partial f(x)$$.

## Deriving subgradient updating steps

As we saw in [the previous section]({% multilang_post_url contents/chapter07/21-03-25-07_03_05_example_distance_to_convex_set %}), $$dist(x, C_i)$$ has the following subgradient:

>$$\text{Recall:}$$
$$ \begin{align}
g_i = \nabla f_i(x) = \frac{x-P_{C_i}(x)}{ \Vert x-P_{C_i}(x) \Vert_2}
\end{align} $$

If the convex sets have a common point, we know right away that $$f^*=0$$, so we can use Polyak step sizes. Since $$x-P_{C_i}(x)$$ is normalized in the subgradient above, $$ \Vert g \Vert_2^{2}=1$$. Substituting these known values into the Polyak step size $$t_k = \frac{f(x^{(k-1)})-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}}$$, we obtain the following subgradient method update (here $$i$$ is an index of a set farthest from $$x^{(k-1)}$$, i.e. $$f_i(x^{(k-1)}) = f(x^{(k-1)})$$):

>
$$ \begin{align}
x^{(k)} & = x^{(k-1)} - t_{k}\cdot g^{(k-1)} \\
& = x^{(k-1)} - \frac{f(x^{(k-1)})-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}} \frac{x^{(k-1)}-P_{C_i}(x^{(k-1)})}{ \Vert x^{(k-1)}-P_{C_i}(x^{(k-1)}) \Vert_2}  \\
& = x^{(k-1)} - f(x^{(k-1)}) \frac{x^{(k-1)}-P_{C_i}(x^{(k-1)})}{ \Vert x^{(k-1)}-P_{C_i}(x^{(k-1)}) \Vert_2}
\end{align} $$

Here the Polyak step size is $$f(x^{(k-1)}) = dist(x^{(k-1)}, C_i) =  \Vert x^{(k-1)}-P_{C_i}(x^{(k-1)}) \Vert_2$$, so the subgradient method simplifies to:

>
$$ \begin{align}
x^{(k)} = P_{C_i}(x^{(k-1)})
\end{align} $$

In pictures, at each step the iterate is projected onto the set that is farthest from it, and this is repeated.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter08/08_01_projection.png" alt="projection" width="60%" height="60%">
</p>
  <figcaption style="text-align: center;">[Fig 2] Alternating Projection Algorithm [10]</figcaption>
</figure>
