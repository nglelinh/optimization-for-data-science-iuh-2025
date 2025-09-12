---
layout: post
title: 19-01-02 Proximal Newton method
chapter: '19'
order: 4
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

In the previous section, we explained that the **proximal newton method** is a method that wants to use the local hessian $$\nabla^2 g(x)$$ instead of the spherical curvature $$\frac{1}{t} I$$ in the **proximal gradient descent** formula. The proximal newton method is an old idea that is being studied in statistics under the term local score.

Now let's look at how the **proximal newton method** can be formulated.

## Algorithm
The Proximal gradient descent algorithm consists of the process of finding the direction $$v$$ of the next step and then optimizing the step size $$t_k$$. 

* Step 1: Starting from the starting point $$x^{(0)}$$, iterate the following process. ($$k=1,2,3,...$$) 

* Step 2: Find the direction $$v$$ of the next step.

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

### Next position view
위의 식을 direction $$v$$이 아닌 다음 position인 $$z$$의 관점at, 표현하면 as follows:.

> $$
> \begin{align}
> z^{(k)} & = \underset{z}{\text{argmin}} \ \nabla g(x^{(k-1)})^T (z - x^{(k-1)})^T + \frac{1}{2} (z - x^{(k-1)})^T H^{(k-1)} (z - x^{(k-1)}) + h(z) \\\\
> x^{(k)} & =x^{(k-1)} + t_k (z^{(k)} - x^{(k-1)} )
> \end{align}
> $$

직관적with, 첫번째 stepat, 목적 function를 minimization 하는 surrogate point인 $$z$$를 구한다. 그런 다음, $$x^{(k-1)}$$at, $$z$$의 directionwith, 이동but, always, $$z$$to, 이동하게 되는 것은 아니다.