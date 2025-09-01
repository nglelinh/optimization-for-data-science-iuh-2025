---
layout: post
title: 20-04-03 ADMM in Scaled Form
chapter: '20'
order: 11
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

ADMM은 dual variable $$u$$를 $$w=u/\rho$$to, 바꾸어서 scaled formwith, 표현할 수 있다. 그러면, ADMM step은 as follows: 나타낼 수 있다. 
> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg\min_x f(x) + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c + w^{(k-1)} \rVert_2^2  \\
> z^{(k)} & = \arg\min_z g(x) + \frac{\rho}{2} \lVert Ax^{(k)} + Bz - c + w^{(k-1)} \rVert_2^2  \\
> w^{(k)} & = w^{(k-1)} + Ax^{(k)} + Bz^{(k)} - c 
> \end{alignat}
> $$

위의 식은 다음의 process을 through, 원래 식and, 같다는 것을 알 수 있다.

> $$
> \begin{align}
> x^{(k)} & = \arg\min_x f(x) + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c + w^{(k-1)} \rVert_2^2  \\
> & = \arg\min_x f(x)  + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c \rVert_2^2  + 2 \frac{\rho}{2} w^{(k-1)} (Ax + Bz^{(k-1)} - c)  + \lVert w^{(k-1)} \rVert_2^2 \\
> & = \arg\min_x f(x)  + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c \rVert_2^2  + u^{(k-1) } (Ax + Bz^{(k-1)} - c) \\
> \end{align}
> $$


여기서, $$w^{(k)}$$은  $$k$$번째 residual의 sumwith, 볼 수도 있다.

> $$
> \begin{equation}
> w^{(k)} = w^{(0)} + \sum_{i=1}^k (Ax^{(i)} + Bz^{(i)} - c) 
> \end{equation}
> $$