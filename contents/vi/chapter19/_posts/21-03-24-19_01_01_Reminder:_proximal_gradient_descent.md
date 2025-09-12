---
layout: post
title: 19-01-01 Reminder - proximal gradient descent
chapter: '19'
order: 3
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

Before examining the **Proximal newton method** that we will learn in this chapter, let's first review **Proximal gradient descent**.

For detailed information, see [09 Proximal Gradient Descent and Acceleration]({% multilang_post_url contents/chapter09/20-01-08-09_proximal_gradient_descent_and_acceleration %}) see.

## Proximal gradient descent
**Proximal gradient descent** works on the following problem.

>$$f(x) = g(x) + h(x)$$

* $$g$$ is convex and differentiable. (**dom**$$(g) = \mathbb{R}^n$$)
* $$h$$ is convex and non-differentiable and "simple".


### Algorithm
Proximal gradient descent는 시작점 $$x^{(0)}$$at, 시작solution서 다음 process을 iteration한다.

>$$x^{(k)} = \text{prox}_{t_k}(x^{(k-1)} - t_k \nabla g(x^{(k-1)}) ),k=1,2,3,...$$

여기서 $$\text{prox}_{t}(\cdot)$$는 $$h$$and, association,된 proximal operator 이다.

> \begin{align}
\text{prox}_{t}(x) = \underset{z}{\text{argmin}}  \frac{1}{2t} \parallel x - z \parallel_2^2 + h(z)
\end{align}

Update 식은 generalized gradient $$G_{t}$$를 using,서 표준화된 형태to, 표현할 수도 있다.

> \begin{align}
> x^{(k)} = x^{(k-1)} - t_k \cdot G_{t_k}(x^{(k-1)}), \space \space \text{where} \space G_{t}(x) = \frac{x-\text{prox}_{t} (x - t \nabla g(x))}{t} \\\\
> \end{align}

### Performance
* **Proximal gradient descent**의 성능은 $$h$$according to, 달라질 수 있다. if,, $$h$$가 복잡한 function이고 particularly, closed form이 아니라면 minimize할 when, computation을 많이 solution야 하므to, 성능이 매우 떨어질 수 있다.

* also,, $$g$$function의 convergence rateand, 같은 convergence 속도를 갖는다. 단, iteration할 when,마다 prox operator를 실행하기 because of, prox computation이 효율적인 case,to,만 유용하다.

## Motivation
**Proximal gradient descent**at,는 미분 가능한 function $$g$$를 Taylor 2difference식with, approximation하고 여기to, 미분이 되지 않는 function인 $$h$$를 더하여 목적 functionto, 정의한 후 이를 iteration적with, minimization한다. therefore,, as follows: 2difference 식with, 정리solution 볼 수 있다.

식to, 전개되는 자세한 process은 [09-01 Proximal gradient descent]({% multilang_post_url contents/chapter09/20-01-08-09_01_proximal_gradient_descent %}) reference.

> $$
> \begin{align}
x^+ & = \underset{z}{\text{argmin}}  \, \frac{1}{2t} \parallel x - t \nabla g(x) - z \parallel_2 ^2 + h(z) \\\\
> & = \underset{z}{\text{argmin}} \ \nabla g(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2 + h(z) \\\\
> \end{align}
> $$

두번째 식의 1항and, 2항은 $$g$$의 Taylor 2difference approximation식with, from, 유도할 수 있는데, first, constant항 $$g(x)$$은 제거하고 (gradient descentat,and, 마찬가지to,) Hessian $$\nabla^2 g(x)$$을 $$\frac{1}{t} I$$(spherical curvature)to, 대체solution서 구할 수 있다.

다음 그림at,는 proximal gradient descent의 update stepat, $$g$$를 2difference approximation식with, minimization 하는 process을 showing,주고 있다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.01_01_proximal_gradient_descent.png" alt="[Fig 1] Proximal gradient descent updates [3]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Proximal gradient descent updates [3]</figcaption>
</p>
</figure>

Gradient descentand, newton's method의 difference이점는 2difference approximation를 할 when, function의 local hessian인 $$\nabla^2 g(x)$$를 사용하는지 여부이다. 그렇다면, 위의 식at, $$\frac{1}{t} I$$ instead, $$\nabla^2 g(x)$$를 사용하면 어떻게 될까?

이것이 바to, 다음 절at, 설명하게 될 **proximal newton method**가 나오게 된 background,이다.
