---
layout: post
title: 24-04 Relaxations
chapter: '24'
order: '5'
owner: YoungJae Choung
categories:
- chapter24
lang: en
---

For relaxation, specific conditions must be satisfied, and Convex relaxation and Lagrangian relaxation methods can be utilized. Let's examine the detailed content.

## Conditions for Relaxations

If a general optimization problem is defined as follows:

>$$\min_{x \in X} f(x)$$

The relaxation of this problem is defined as follows when represented as an arbitrary optimization problem:

>$$
>\begin{align}
>&\min_{x \in Y} \: g(x)\\\\
>&\text{such that}\\\\
>&\text{① } X \subset Y \quad \text{ and}\\\\
>&\text{② } g(x) \leq f(x) \text{ for all } x \in X
>\end{align}
>$$

If the objective functions $$f(x)$$ and $$g(x)$$ are different, both conditions must be satisfied, and if they are the same, only condition ① needs to be satisfied. By these two conditions, the optimal value of the relaxation becomes a lower bound of the optimal value of the original problem.

## Convex relaxations

When the given problem is as follows:

>$$
>\begin{align}
>&\min_{x} &&f(x) \\\\
>&\text{subject to } && x \in C \\\\
>&&&x_j \in \mathbb{Z}, \quad j \in J \\\\
>\end{align}
>$$
>
>$$
>\begin{align}
>\text{where } f \text{ is convex, } f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \subseteq \mathbb{R}^n
>\quad \text{and} \quad J \subseteq \{1, \dotsc, n\}
>\end{align}
>$$

The convex relaxation can be expressed as follows:

>$$
>\begin{align}
>&\min_{x} && f(x) \\\\
>&\text{subject to } && x \in C \\\\
>\end{align}
>$$
>
>$$
>\begin{align}
>\text{where } f \text{ is convex, } f: \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \subseteq \mathbb{R}^n
>\end{align}
>$$

## Lagrangian relaxations

When $$X$$ includes both convex and integer constraints, we can define the problem as follows:

>$$
>\begin{align}
>&\min_{x} &&f(x) \\\\
>&\text{subject to } &&Ax \leq b \\\\
>&&& x_{j} \in \mathbb{Z}, \quad x \in X
>\end{align}
>$$

In this case, by adding constraints to the objective and performing Lagrangian relaxation for some $$u \geq 0$$, we get:

>$$
>\begin{align}
>L(u) = &\min_{x} &&f(x) + u^{\top}(Ax-b) \\\\
>&\text{subject to } &&x \in X
>\end{align}
>$$

Through the Lagrangian form, the constraint set is expanded, and since feasible $$x$$ satisfies $$Ax \leq b$$, we always have $$f(x) + u^{\top}(Ax - b) \leq f(x)$$ for $$u \geq 0$$. Therefore, $$L(u)$$ is a lower bound for any $$u \geq 0$$, and the best lower bound can be obtained by solving the dual problem $$\max_{u \geq 0} L(u)$$. Remember that since $$L(u)$$ is the point-wise minimum of convex functions, it becomes a concave optimization problem.

Applying Lagrangian relaxation to the previously mentioned Facility location problem, it transforms into a problem of solving the following equation for unconstrained $$v$$:

>$$
>\begin{align}
>L(u) = &\min_{x} && \sum_{j = 1}^{n} f_{j}y_{j} + \sum_{i = 1}^{m}\sum_{j = 1}^{n}(c_{ij} - v_{i})x_{ij} + \sum_{i = 1}^{m} v_{i} \\\\
>&\text{subject to } && x_{ij} \leq y_{j} \quad i = 1, \dotsc, m, \quad j = 1, \dotsc, n \\\\
>&&& x_{ij}, y_{j} \in \{0, 1\} \quad i = 1, \dotsc, m, \quad j = 1, \dotsc, n
>\end{align}
>$$

For each $$v$$, the Lagrange relaxation $$L(v)$$ can be easily solved:

>$$
>x_{ij}(v) =\begin{cases}
>1 & \text{if } c_{ij} - v_{i} < 0 \text{ and } \sum_{l} (c_{lj} - v_{l})^{-} + f_{j} < 0 \\\\
>0 & \text{otherwise}
>\end{cases}
>$$
>
>$$
>y_{j}(v) =\begin{cases}
>1 & \text{if } \sum_{l} (c_{lj} - v_{l})^{-} + f_{j} < 0 \\\\
>0 & \text{otherwise}
>\end{cases}
>$$

From this lower bound $$L(v)$$, we can also derive heuristic primal solutions. Also, using the subdifferential of $$-L(v)$$ makes computation easier. Using the subgradient method, we can solve the problem by transforming $$\max_{v} L(v)$$ to $$\min_{v} -L(v)$$.