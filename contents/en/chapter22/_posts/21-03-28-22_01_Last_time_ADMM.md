---
layout: post
title: '22-01 Last time: ADMM'
chapter: '22'
order: 2
owner: YoungJae Choung
categories:
- chapter22
lang: en
---


## Last time: ADMM
다음and, 같은 optimization problem를 고려solution보자
> $$\begin{align}
> &\min_{x,z} &&f(x) + g(z)\\\\
> &\text{ subject to } &&Ax + Bz = c 
> \end{align}$$

이를 Augmented Lagrangian 형식with, 바꾸어 보면 아래and, 같다. (for some $$ρ > 0$$)
> $$ L_ρ(x, z, u) = f(x) + g(z) + u^T(Ax + Bz − c) + \frac{ρ}{2} \| Ax + Bz − c \|^2_2$$

위 식은 $$\frac{ρ}{2} \| Ax + Bz − c \|^2_2$$가 추가 됨with, Strongly Convex가 되며, 이를 다음 수식and, 같이 병렬 처리to, 유용한 형태to,  바꿀 수 있다.
* 자세한 증명은 앞장의 내용을 please refer to.
ADMM: for $$k = 1, 2, 3, . . .$$
> $$x^{(k)} = argmin_{x} L_ρ(x, z^{(k−1)}, u^{(k−1)})$$
> $$z^{(k)} = argmin_{z} L_ρ(x^{(k)}  , z, u^{(k−1)})$$
> $$u^{(k)} = u^{(k−1)} + ρ(Ax^{(k)} + Bz^{(k)} − c)$$
 
## ADMM in scaled form
dual variable $$u$$를 scaled variable $$w = u/ρ$$to, 바꾸어 보자. 여기서 ADMM step은 as follows: computation 가능하다.

> $$x^{(k)} = argmin_{x} f(x) + \frac{ρ}{2} \| Ax + Bz^{(k−1)} − c + w^{(k−1)} \|^2_2$$
> $$z^{(k)} = argmin_{z} g(z) + \frac{ρ}{2} \| Ax^{(k)} + Bz − c + w^{(k−1)} \|^2_2$$ 
> $$w^{(k)} = w^{(k−1)} + Ax^{(k)} + Bz^{(k)} − c$$
