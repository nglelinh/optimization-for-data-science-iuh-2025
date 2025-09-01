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

Relaxation을 for,서는 특정 condition,이 성립이 되어야 하며, Convex relaxationand, Lagrangian relaxation method을 활용할 수 있다. 자세한 내용을 let's examine.

## Conditions for Relaxations
일반적인 optimization problem이 as follows: 정의된다면,
> $$\min_{x \in X} f(x)$$

이 problem의 relaxation은 임의의 optimization problemwith, representing,었을 when,, as follows: 정의된다.

> $$\begin{align}
> &\min_{x \in Y} \: g(x)\\\\
> &\text{such that}\\\\
> &\text{① } X \subset Y \quad \text{ and}\\\\ 
> &\text{② } g(x) \leq f(x) \text{ for all } x \in X 
> \end{align}$$ 

objective function $$f(x)$$ and, $$g(x)$$가 달라지면 두 condition, 모두 만족solution야 하고, 같다면 condition, ①만 만족solution도 될 것이다.
두 condition,by,, relaxationat,의 optimal value는 original problemat,의 optimal value의 lower bound가 된다.

## Convex relaxations
주어진 problem가 다음and, 같을 when,,
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

convex relaxation을 아래and, 같이 표현할 수 있다.
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
