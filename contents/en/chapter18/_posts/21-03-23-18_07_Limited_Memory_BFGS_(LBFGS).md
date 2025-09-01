---
layout: post
title: 18-07 Limited Memory BFGS (LBFGS)
chapter: '18'
order: 8
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

## Introduction

LBFGS는 Limited-memory quasi-Newton methods의 한 예시to,써, Hessian matrix을 computation하거나 저장하기 위한 비용이 sum리적이지 않을 case, 유용하게 사용된다. 이 method은 밀도가 높은 $$n \times n$$의 Hessian matrix을 저장하는 instead of, $$n$$difference원의 vector 몇 개만을 유지하여 Hessian matrix을 추정(approximation)하는 방식이다. 

LBFGS의 algorithm은 그 이름이 시사하는 것처럼 BGFS를 basis,with, 한다. 주요한 아이디어는 Hessianto, about, 추정을 하기for, 가장 최근의 iteration들at,의 curvature information을 이용하자는 것이다. 반면 오래된 iteration들의 curvature information은 현재 iteration의 Hessian이 보이는 동향(behavior)and, 다소 distance가 있을 것이므to, 저장space을 아끼는 측면at, 사용하지 않도록 한다.

여담with, 동일한 technique을 through, 다른 quasi-Newton algorithm(가령, SR1)의 limited-memory version도 유도 가능하다 [14].

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
