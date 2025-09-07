---
layout: post
title: 24-04 Relaxations
chapter: '24'
order: 5
owner: YoungJae Choung
categories:
- chapter24
lang: en
---

For relaxation, specific conditions must be satisfied, and Convex relaxation and Lagrangian relaxation methods can be utilized. Let's examine the detailed content.

## Conditions for Relaxations
If a general optimization problem is defined as follows:
> $$\min_{x \in X} f(x)$$

The relaxation of this problem is defined as follows when represented as an arbitrary optimization problem:

> $$\begin{align}
> &\min_{x \in Y} \: g(x)\\\\
> &\text{such that}\\\\
> &\text{① } X \subset Y \quad \text{ and}\\\\ 
> &\text{② } g(x) \leq f(x) \text{ for all } x \in X 
> \end{align}$$ 

If the objective functions $$f(x)$$ and $$g(x)$$ are different, both conditions must be satisfied, and if they are the same, only condition ① needs to be satisfied.
By these two conditions, the optimal value of the relaxation becomes a lower bound of the optimal value of the original problem.

## Convex relaxations
When the given problem is as follows:
> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } && x \in C \\\\
> &&&x_j \in \mathbb{Z}, \quad j \in J \\\\
>\end{align} $$
>$$\begin{align}
> \text{where f is convex } f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \in \mathbb{R}^n 
> \quad \text{and} \quad J \in \lbrace 1 \dotsc n \rbrace \\
> \end{align}
> $$

convex relaxation can be expressed as follows:
> $$
> \begin{align}
> &\min_{x} && f(x) \\\\
> &\text{subject to } && x \in C \\\\
>\end{align} $$
>$$\begin{align}
>\text{where f is convex } f: \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \in \mathbb{R}^n 
>\text{and} \quad J \in \lbrace 1 \dotsc n \rbrace \\
>\end{align}
>$$


## Lagrangian relaxations
$$X$$가 convex and, integer constraints를 모두 포함할 when,, as follows: problem를 정의 할 수 있다. 

> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } &&Ax \leq b \\\\
> &&& x_{j} \in \mathbb{Z} \quad x \in X 
> \end{align}
> $$

이 when,, constraints를 objectiveto, 더하여, 어떤 $$u \geq 0$$to, about, Lagrangian relaxation을 하면, as follows:.

> $$
> \begin{align}
> L(u) = &\min_{x} &&f(x) + u^{\top}(Ax-b) \\\\
> &\text{subject to } &&x \in X
> \end{align}
> $$

Lagrangian form을 through,서 constraint set이 확장되었고, feasible $$x$$about, $$Ax \leq b$$을 만족하므to,, always, $$f(x) + u^{\top}(Ax - b) \leq f(x), u \geq 0$$이 성립한다. therefore, $$L(u)$$는 임의의 $$u \geq 0$$about,서 lower bound이고, 최선의 lower bound는 dual problem $$\max_{u \geq 0} L(u)$$을 solution결함with,써 obtaining,낼 수 있다. $$L(u)$$는 convex function의 point-wise minimization이기 because of, concave optimization problem이 된다는 것을 기억하자.

앞서 언급되었던 Facility location problemto, Lagrangian relaxation을 applying, 보면, unconstrained $$v$$about, 다음 식을 푸는 problemto, 변형된다.

> $$
> \begin{align}
> L(u) = &\min_{x} && \sum_{i = 1}^{n} f_{j}y_{j} + \sum_{i = 1}^{m}\sum_{j = 1}^{n}(c_{ij} - v_{i})x_{ij} + \sum_{i = 1}^{m} v_{i} \\\\
> &\text{subject to } && x_{ij} \leq y_{j} \quad i = 1 \dotsc m, \quad j = 1 \dotsc n \\\\
> &&& x_{ij}, y_{j} \in \lbrace 0, 1 \rbrace \quad  i = 1 \dotsc m, \quad j = 1 \dotsc n 
> \end{align}
> $$

각각의 $$v$$about, Lagrange relaxation $$L(v)$$는 쉽게 풀릴 수 있다 :
> $$ x_{ij}(v) =\begin{cases}1 & \text{if} \quad c_{ij} - v_{i} < 0 \quad \text{and}  \quad \sum_{l} (c_{lj} - v_{l})^{-} + f_{j} < 0 \\\\
> 0 & \text{otherwise.} \end{cases}$$
> $$ y_{j}(v) =\begin{cases}1 & \text{if } \quad \sum_{l} (c_{lj} - v_{l})^{-} + f_{j} < 0 \\\\
> 0 & \text{otherwise.} \end{cases} $$

이는 lower bound $$L(v)$$ and, heuristic primal solution을 도출 할 수 있도록 한다. also, $$-L(v)$$의 부분미분(subdifferential)을 사용한다면 computation도 쉬워진다. subgradient method를 using, $$\max_{v} L(v)$$를 $$\min_{v} -L(v)$$ to, transformation시켜서 problem를 풀어갈 수 있다.
