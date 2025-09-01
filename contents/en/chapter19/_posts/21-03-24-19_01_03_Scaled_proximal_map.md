---
layout: post
title: 19-01-03 Scaled proximal map
chapter: '19'
order: 5
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

**Proximal newton method**를 **proximal gradient descent**and, 같은 형식with, 다시 작성solution 볼 수 있다.

## Scaled proximal map
if, $$H \succ 0$$라고 하면 **scaled proximal map**은 as follows: 정의된다.

> \begin{align}
\text{prox}_{t}(x) = \underset{z}{\text{argmin}}  \frac{1}{2} \parallel x - z \parallel_H^2 + h(z)
\end{align}

여기서 $$\parallel x\parallel_H^2 = x^THx$$with, $$H\text{-norm}$$이다.  $$H = \frac{1}{t} I$$일 when, 일반적인 **unscaled proximal map**이 된다.

generally, **scaled proximal map**는 usually,의 prox보다 좋은 성질을 갖고 있다.

* **uniqueness** : solution가 하나만 존재하는 성질 ($$H \succ 0$$이므to, strictly convex optimization problem이기 because of, 만족된다.)
* **non-expansiveness** :  팽창하지 않는 성질 (scaled proximal map이 non-expansive 성질을 갖는 projection operator의 일반화이기 because of, 만족된다.)

#### [reference] Projection operator의 non-expansiveness
두 점 $$x$$, $$y$$and, convex set $$C$$to, about, projection operator $$P_c$$about, non-expansiveness란 $$\parallel P_c(x) - P_c(y) \parallel_2 \le \parallel x - y \parallel_2$$를 만족한다는 것을 의미한다. that is,,  $$P_c$$는 Lipschitz-1을 만족하며 $$C$$가 convex일 case,to,만 만족한다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.01_03_projection_operator.png" alt="[Fig 1] Projection onto a convex set C [3]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Projection onto a convex set C [3]</figcaption>
</p>
</figure>

## Proximal newton update
**Scaled proximal map**을 using,서 Proximal newton update를 다시 expressing,보면 as follows:.

> $$
> \begin{align}
> z^{+} & = \underset{z}{\text{argmin}} \nabla g(x)^T (z - x)^T v + \frac{1}{2} (z - x)^T H (z - x) + h(z) \\\\
> & =\underset{z}{\text{argmin}} \ \frac{1}{2} \parallel x - H^{-1} \nabla g(x) - z \parallel_H^2 + h(z)
> \end{align}
> $$

다르게 표현하면 as follows:.

> $$
> \begin{align}
> z^{(k)} & = \text{prox}_{H^{(k-1)}} ( x^{(k-1)} - (H^{(k-1)})^{-1} \nabla g (x^{(k-1)}) ) \\\\
> x^{(k)} & =x^{(k-1)} + t_k (z^{(k)} - x^{(k-1)} )
> \end{align}
> $$

직관적with, $$g$$about,서 newton step을 수행하고, $$H^{(k-1)}$$about, scaled prox operator를 applying,서 그 directionwith, 이동한다는 것을 의미한다.

이from, 다음and, 같은 사항을 알 수 있다.

* $$h(z) = 0$$일when, proximal operator는 identity function가 되여 일반적인 Newton update가 된다.
* $$H^{(k+1)}$$를 $$\frac{1}{r_k} I$$to, 대체하고 $$t_k = 1$$to, 두면 step size $$r_k$$about, proximal gradient update를 구할 수 있다.
* Prox의 어려움은 $$h$$뿐만 아니라 $$g$$의 hessian의 구조according to, 달라진다. for example, $$H$$가 diagonal이거나 banded이면 dense한 $$H$$일 case,to, 비solution problem가 매우 쉬워진다.

therefore,,  proximal Newton method는 proximal gradient descentand, Newton's method를 둘 다 일반화한 것임을 알 수 있다.
