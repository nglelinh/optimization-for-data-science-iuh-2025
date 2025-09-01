---
layout: post
title: '08-01-07 Example: Intersection of sets'
chapter: '08'
order: 9
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---


Suppose we want to find the intersection point of several closed convex sets.

First, let’s define $$f_i(x)$$ as the distance from a point $$x$$ to the set $$C_i$$, and $$f(x)$$ as the maximum distance from $$x$$ to all sets $$C_i, i=1,...,m$$:
>
$$ \begin{align}
f_i(x) & = \mathbb{dist}(x, C_i), i=1,...,m \\
f(x) & = \max_{1,...,m}\text{ }f_i(x)
\end{align} $$

Using these two functions, the problem of finding the intersection of convex sets can be formulated as the following minimization problem:

>
$$ \begin{align}
min_{x}\text{ }f(x)
\end{align} $$

The problem of finding the intersection point of convex sets is equivalent to finding the point $$x$$ that minimizes the maximum distance $$f(x)$$ to the sets $$C_i$$. In this case, the objective function $$f(x)$$ is convex. If all sets have a common intersection point, then $$f^* = 0$$ and the optimal point is $$x^* \in C_1 \cap C_2 \cap ... \cap C_m$$.

## Gradient of distance function

In [the previous section]({% multilang_post_url contents/chapter07/21-03-25-07_03_05_example_distance_to_convex_set %}), we defined the distance to a convex set as $$dist(x, C_i) = \min_{y \in C} \lVert y-x \rVert _2$$, and saw that the gradient of this function is:

>
$$ \begin{align}
\partial dist(x,C) = \frac{x-P_C(x)}{ \Vert x-P_C(x) \Vert_2}
\end{align} $$

Here, $$P_C(x)$$ is the projection of the point $$x$$ onto the set $$C$$.

## Subdifferential of finite pointwise maximum

Finite pointwise maximum 함수 $$f(x)=max_{i=1,...,m}\text{ }f_i(x)$$에 대한 subdifferential은 다음과 같이 정의 된다. 

>
$$ \begin{align}
\partial f(x) = \text{conv}\left(\bigcup_{i:f_i(x)=f(x)} \partial f_i(x)\right)
\end{align} $$

즉, $$x$$의 subdifferential은 그 지점의 모든 subdifferential $$\partial f_i(x), i=1,...,m$$의 합집합에 대한 convex hull로 정의된다. 

만약 $$f_i(x) = f(x)$$ 이고 $$g_i \in \partial f_i(x)$$이라면 $$g_i \in \partial f(x)$$이다.

## Deriving subgradient updating steps

[이전 장]({% multilang_post_url contents/chapter07/21-03-25-07_03_05_example_distance_to_convex_set %})에서 보았던 $$dist(x, C_i)$$는 다음과 같은 subgradient를 가진다.

>$$Recall:$$
$$ \begin{align}
g_i = \nabla f_i(x) = \frac{x-P_{C_i}(x)}{ \Vert x-P_{C_i}(x) \Vert_2}
\end{align} $$

만약 컨벡스 집합의 교차점이 있다면 우리는 $$f^*=0$$임을 바로 알 수 있기에 Polyak step sizes를 사용할 수 있다. 위 subgradient 수식을 보면 $$x-P_{c_i}(x)$$가 정규화된 형태이므로 $$ \Vert g \Vert_2^{2}=1$$이다. 결국 Polyak step size $$t_k = \{\frac{f^{(k-1)}-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}}\}$$에 우리가 알고 있는 값을 대입하면 다음과 같은 subgradient method 공식을 도출할 수 있다.

>
$$ \begin{align}
x^{(k)} & = x^{(k-1)} - t_{k}⋅g_{k-1} \\
& = x^{(k-1)} - \frac{f^{(k-1)}-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}} \frac{x^{(k-1)}-P_{C_i}(x)}{ \Vert x^{(k-1)}-P_{C_i}(x) \Vert_2}  \\
& = x^{(k-1)} - f(x^{k-1}) \frac{x^{(k-1)}-P_{C_i}(x)}{ \Vert x^{(k-1)}-P_{C_i}(x) \Vert_2}
\end{align} $$


여기서 Polyak size인 $$f(x^{(k-1)})$$는 $$dist(x_i^{(k-1)}, C_i) =  \Vert x^{(k-1)}-P_{C_i}(x) \Vert_2$$ 이므로 subgradient method는 아래와 같이 정리된다.

>
$$ \begin{align}
x^{(k)} = P_{C_i}(x^{(k-1)})
\end{align} $$

이 문제는 그림으로 표현하면 각 스텝에서 가장 가까운 컨벡스 함수에 projection을 반복하는 형태이다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter08/08_01_projection.png" alt="projection" width="60%" height="60%">
</p>
  <figcaption style="text-align: center;">[Fig 2] Alternating Projection Algorithm [10]</figcaption>
</figure>
