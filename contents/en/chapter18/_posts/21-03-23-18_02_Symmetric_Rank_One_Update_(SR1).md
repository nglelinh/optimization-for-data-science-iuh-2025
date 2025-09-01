---
layout: post
title: 18-02 Symmetric Rank-One Update (SR1)
chapter: '18'
order: 3
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

SR1 update는 rank-1의 symmetric matrixto, $$B$$를 업데이트 함with,써 $$B^+$$가 symmetry를 유지하고 secant equation을 계속solution서 만족하게끔 업데이트하는 method이다. Rank-1의 symmetric matrix가 $$a \in \left\{-1, 1\right\}$$and, $$u \in \mathbb{R^n}$$의 productwith, 분solution된다고 하면 update form은 다음and, 같을 것이다.

>$$B^+ = B + auu^T.$$

## Key Observation
$$a$$and, $$u$$는 $$B^+$$가 secant equation을 만족하게끔 선택되어야 한다. thus, secant equation $$y = B^+s$$to, 위at, 소개한 update form을 대입solution보자.

>$$y = B^+s \Rightarrow y = Bs + (au^Ts)u. \quad \text{--- (1)}$$

$$(au^Ts)$$는 scalar이므to, $$u$$는 $$y-Bs$$and, 임의의 scalar $$\delta$$and,의 productwith,도 표현할 수 있을 것이다 $$\big( u = \delta(y - Bs) \big)$$. (1)의 $$u$$를 $$\delta(y - Bs)$$with, 치환solution보자.

>$$y-Bs = a\delta^2 \big[ s^T(y - Bs) \big] (y -Bs),$$

위 등식을 만족하는 파라미터 $$\delta$$and, $$a$$는 as follows:.

>$$a = \text{sign} \big[ s^T (y - Bs) \big], \quad \delta = \pm | s^T(y-Bs) |^{-1/2}. \quad \text{--- (2)}$$

## The Only SR1 Updating Formula
Key observationat, 얻은 정보를 utilizing, 유일한 형태의  SR1 update를 유도할 수 있다 ([14]의 6.2). <br/>
$$\big( u = \delta (y - Bs)$$ and, (2)를 $$B^+ = B + auu^T$$to, 대입. $$\big)$$

>$$
>B^+ = B + \frac{(y-Bs)(y-Bs)^T}{(y-Bs)^Ts}.
>$$
>

## The Update Formula for the Inverse Hessian Approximation

$$x^+$$를 구하기 for,서는 $$B^{-1}$$의 computation이 필요solution진다.

>$$x^+ = x + tp = x - tB^{-1}\nabla f(x)$$

$$B$$ instead of, $$B^{-1}$$를 업데이트 할 수 있다면 매번 $$B^{-1}$$을 computation하기 위한 비용을 줄일 수 있지 않을까?

[Sherman–Morrison formula](https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula)를 이용하면 유도process을 through, $$B^{-1}$$ also, 동일한 형태to, 업데이트 할 수 있다는 것을 알 수 있다. ($$H = B^{-1}$$)

>$$
>H^+ = H + \frac{(s-Hy)(s-Hy)^T}{(s-Hy)^Ty}.
>$$

## Shortcomings of SR1

SR1 은 아주 간단하다는 장점이 있지만 두 가지 치명적인 단점을 가지고 있다.

1. $$(y-Bs)^Ts$$가 0to, 가까워지면 업데이트to, 실패할 수 있다.
2. $$B$$and, $$H$$의 positive definiteness를 유지하지 못한다.

이 뒤의 절at,는 SR1의 단점을 보완한 method들을 소개한다. 