---
layout: post
title: 18-07 Limited Memory BFGS (LBFGS)
chapter: '18'
order: 8
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

## Introduction

LBFGS is an example of Limited-memory quasi-Newton methods, and is useful when the cost of computing or storing the Hessian matrix is not reasonable. This method estimates (approximates) the Hessian matrix by maintaining only a few $$n$$-dimensional vectors instead of storing a dense $$n \times n$$ Hessian matrix. 

The LBFGS algorithm is based on BFGS, as its name suggests. The main idea is to use curvature information from the most recent iterations to estimate the Hessian. On the other hand, curvature information from older iterations is not used to save storage space, as it may be somewhat distant from the behavior shown by the Hessian of the current iteration.

As a side note, limited-memory versions of other quasi-Newton algorithms (e.g., SR1) can also be derived using the same technique [14].

## LBFGS

LBFGS를 본격적with, 설명하기to, 앞서 BFGS methodabout, 다시 let's look at. 각 stepat, BFGS는 as follows: $$x$$를 업데이트 한다.
>$$
>x^+ = x - t H \nabla f, \\\\
>\text{where } t \text{ is the step length and } H \text{ is updated at every iteration by means of the formula, }\\\\
>\text{     }\\\\
>H^+ =  \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big) + \frac{ss^T}{y^Ts}.\\\\
>$$

$$H$$to, about, 업데이트 식을 이용하면 $$H^+q, q \in \mathbb{R}^n$$를 임의의 scalar $$\alpha, \beta \in \mathbb{R}$$and, 임의의 vector $$p, s \in \mathbb{R}^n$$를 using, 표현할 수 있다. 

>$$
>\begin{align}
>H^+q &=  \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big)q + \frac{ss^Tq}{y^Ts}\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) \underbrace{H \\big( q - \frac{s^T q}{y^Ts} y \big)}_{p} + \underbrace{\frac{s^Tq}{y^Ts}}_{\alpha} s\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) p + \alpha s\\\\
> &= p - \underbrace{\frac{y^Tp}{y^Ts}}_{\beta}s + \alpha s \\\\
> &= p + (\alpha - \beta) s,\\\\
>& \text{where } \alpha = \frac{s^Tq}{y^Ts}, q^+ = q - \alpha y, p = Hq, \beta = \frac{y^Tp}{y^Ts}.
>\end{align}\\\\
>$$

$$H$$가 k번의 BFGS update를 through, 얻이진다고 할when,, $$Hq= -H\nabla f(x)$$는 length k의 iteration문 2개to, computation할 수 있다 (아래 algorithm reference). 단, 메모리의 효율적인 사용을 for, 가장 최근 $m$개 iterationsat,의 curvature information만을 이용한다. ($$k \ge m$$)

## Algorithm
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter18/algorithm_quasi-newton.png" alt="[Fig1] The algorithm of LBFGS [3]" width="90%">
  <figcaption style="text-align: center;">[Fig1] The algorithm of LBFGS [3]</figcaption>
</p>
</figure>

usually, inverse Hessian approximation $$H_k$$는 dense하며, variable의 개수가 많은 case, 저장 및 operation 비용이 매우 높아지게 된다. 반면 LBFGS는 $$H_k \nabla f_k$$을 연속한 vectorsumand, vectorproductwith, obtaining,냄with,써 $$H_k$$의 computation 및 유지를 위한 비용problem를 완화시킬 수 있다. 뿐만 아니라 이 computationto, 사용되는 initial Hessian approximation $$H^{0,k}$$는 usually, (실전at, 매우 effect,적with, 작동한다고 검증된) identity matrixto, 어떤 constant를 product한 형태($$H^{0,k} = \gamma_k I$$)를 띄기 because of, 유지 및 computationto, 그다지 큰 비용이 발생하지 않는다 ([14]의 7.2).
> $$
> H^{0,k} = \gamma_k I, \\\\
> \text{where } \: \gamma_k = \frac{s^T_{k-1}y_{k-1}}{y^T_{k-1}y_{k-1}}.
> $$

* **Note:** $$H^{0,k}$$는 매 iteration마다 다르게 선택될 수 있다.
