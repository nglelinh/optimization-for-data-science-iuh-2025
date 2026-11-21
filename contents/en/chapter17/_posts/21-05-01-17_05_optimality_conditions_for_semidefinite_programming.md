---
layout: post
title: "17-05 Optimality conditions for semidefinite programming"
chapter: '17'
order: 9
owner: Minjoo Lee
categories:
- chapter17
lang: en
---

In this section we look at an example of the primal-dual method for SDP (semidefinite programming) problems.

## SDP (semidefinite programming)
The primal SDP problem is defined as follows.
>$$
>\begin{align}
>    &\min_{X} && {C \cdot X} \\\\
>    &\text{subject to } && {A_i \cdot X = b_i, i = 1,...,m} \\\\
>    & &&{X \succeq 0}
>\end{align}
>$$


The dual SDP problem is defined as follows.
>$$
>\begin{align}
>    &\max_{y} && {b^Ty} \\\\
>    &\text{subject to } && {\sum^m_{i=1} y_iA_i + S = C} \\\\
>    & &&{S \succeq 0}
>\end{align}
>$$

Recall that the trace inner product on $$\mathbb{S}^n$$ is written
> $$X \cdot S = \text{trace}(XS)$$

## Optimality conditions for SDP
The primal and dual SDP problems can be written with a linear map as follows.

>$$
>\begin{align}
>    &\min_{X} && {C \cdot X} & \qquad \qquad \qquad & \max_{y,S}  && {b^Ty} \\\\
>    &\text{subject to } && {\mathcal{A}(X) = b} & \qquad \qquad \qquad & \text{subject to } && {\mathcal{A}^{*}(y) + S = C} \\\\
>    & &&{X \succeq 0} & \qquad \qquad \qquad & &&{S \succeq 0}
>\end{align}
>$$


Here $$\mathcal{A}: \mathbb{S}^n \to \mathbb{R}^m$$ is a linear map.

Assuming strong duality holds, $$X^{\star}$$ and $$(y^{\star}, S^{\star})$$ are optimal solutions of the primal and dual problems if and only if $$(X^{\star}, y^{\star}, S^{\star})$$ satisfies the following conditions.

> $$
> \begin{array}{rcl}
> \mathcal{A}^*(y) + S & = & C \\\
> \mathcal{A}(X) & = & b \\\
> XS & = & 0 \\\
> X,S & \succeq & 0
> \end{array}
> $$


## Central path for SDP
**Primal barrier problem**
>$$
>\begin{align}
>    &\min_{X} && {C \cdot X - \tau \log\det(X)} \\\\
>    &\text{subject to } && {\mathcal{A}(X) = b} 
>\end{align}
>$$


**Dual barrier problem**
>$$
>\begin{align}
>    &\max_{y, S} && {b^Ty + \tau \log\det(S)} \\\\
>    &\text{subject to } && {\mathcal{A}^*(y) + S = C} 
>\end{align}
>$$


**Optimality conditions for the primal and dual barrier problems**
> $$
> \begin{array}{rcl}
> \mathcal{A}^*(y) + S & = & C \\\
> \mathcal{A}(X) & = & b \\\
> XS & = & \tau I \\\
> X,S & \succ & 0
> \end{array}
> $$


## Newton step
Primal central path equations 
> $$
> \begin{array}{rcl}
> \mathcal{A}^*(y) + \tau X^{-1} & = & C \\\
> \mathcal{A}(X) & = & b \\\
> X & \succ & 0
> \end{array}
> $$


Newton equations
> $$\tau X^{-1}\Delta X X^{-1} +\mathcal{A}^*(\Delta y) = -(\mathcal{A}^*(y) + \tau X^{-1} -C)$$
> $$\mathcal{A}(\Delta X) = -(\mathcal{A}(X)-b)$$

The central path equations and Newton equations for the dual, involving $$(y,S)$$, are defined similarly.

## Primal-dual Newton step 
Primal-dual central path equations 
> $$\begin{bmatrix}
\mathcal{A}^*(y) + S - C  \\\
\mathcal{A}(X) - b \\\
XS
\end{bmatrix} =
\begin{bmatrix}
0 \\\
0 \\\
\tau I
\end{bmatrix}
, \quad X, S \succ 0
$$

Newton step:
> $$\begin{bmatrix}
0 & \mathcal{A}^* & I \\\
\mathcal{A} & 0 & 0 \\\
S & 0 & X 
\end{bmatrix}
\begin{bmatrix}
\Delta X \\\
\Delta y \\\
\Delta S
\end{bmatrix}= -
\begin{bmatrix}
\mathcal{A}^*(y) + S - C \\\
\mathcal{A}(X) - b \\\
XS - \tau I 
\end{bmatrix}$$
