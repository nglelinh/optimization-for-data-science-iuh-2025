---
layout: post
title: 19-01-02 Proximal Newton method
chapter: '19'
order: 4
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

before, 절at, **proximal newton method**는 **proximal gradient descent** 식at, spherical curvature인 $$\frac{1}{t} I$$ instead, local hessian인 $$\nabla^2 g(x)$$를 사용하고자 하는 method임을 설명했다. Proximal newton method는 오래 전to, 나온 아이디어to, 통계학at,는 local score란 용어to, 연구되고 있다.

이제 **proximal newton method**가 어떻게 formulation될 수 있는지 let's look at.

## Algorithm
Proximal gradient descent algorithm은 다음 step의 direction인 $$v$$를 구한 후 step size인 $$t_k$$를 optimization하는 processwith, 이루어져 있다. 

* 1step : 시작점 $$x^{(0)}$$at, 시작solution서 다음 process을 iteration한다. ($$k=1,2,3,...$$) 

* 2step : 다음 step의 direction인 $$v$$를 구한다.

> \begin{align}
v^{(k)} & = \underset{v}{\text{argmin}} \ \nabla g(x^{(k-1)})^T v + \frac{1}{2} v^T H^{(k-1)} v + h(x^{(k-1)} + v)
\end{align}
여기서 $$H^{(k-1)} = \nabla^2 g(x^{(k-1)})$$은 $$x^{(k-1)}$$at,의 Hessian이다.

* 3step : $$v^{(k)}$$ directionwith, step을 이동하기 for, step size를 optimization한다. 

> \begin{align}
x^{(k)} & =x^{(k-1)} + t_k v^{(k)}
\end{align}

$$t_k$$는 step sizeto, $$t_k=1$$이면 pure proximal Newton method이다.

Backtracking line search를 through, step size를 optimization하는 process이 있다는 점은 proximal gradient descent methodand, 다른 점이다.

#### Next position view
위의 식을 direction $$v$$이 아닌 다음 position인 $$z$$의 관점at, 표현하면 as follows:.

> $$
> \begin{align}
> z^{(k)} & = \underset{z}{\text{argmin}} \ \nabla g(x^{(k-1)})^T (z - x^{(k-1)})^T + \frac{1}{2} (z - x^{(k-1)})^T H^{(k-1)} (z - x^{(k-1)}) + h(z) \\\\
> x^{(k)} & =x^{(k-1)} + t_k (z^{(k)} - x^{(k-1)} )
> \end{align}
> $$

직관적with, 첫번째 stepat, 목적 function를 minimization 하는 surrogate point인 $$z$$를 구한다. 그런 다음, $$x^{(k-1)}$$at, $$z$$의 directionwith, 이동but, always, $$z$$to, 이동하게 되는 것은 아니다.