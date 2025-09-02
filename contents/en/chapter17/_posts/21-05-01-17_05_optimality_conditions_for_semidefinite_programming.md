---
layout: post
title: 17-05 Optimality conditions for semidefinite programming
chapter: '17'
order: 9
owner: Minjoo Lee
categories:
- chapter17
lang: en
---
In this section, we want to look at an example of the Primal-Dual method for SDP (semidefinite programming) problems.

## SDP (semidefinite programming)
The primal problem of SDP is defined as follows.
>$$
>\begin{align}
>    &\min_{x} && {C \cdot X} \\\\
>    &\text{subject to } && {A_i \cdot X = b_i, i = 1,...,m} \\\\
>    & &&{X \succeq 0}
>\end{align}
>$$


The dual problem of SDP is defined as follows.
>$$
>\begin{align}
>    &\max_{y} && {b^Ty} \\\\
>    &\text{subject to } && {\sum^m_{X_i=1} y_iA_i + S = C} \\\\
>    & &&{S \succeq 0}
>\end{align}
>$$

For reference, the trace inner product of $$\mathbb{S}^n$$ is denoted as follows.
> $$X \cdot S = \text{trace}(XS)$$

## Optimality conditions for SDP
The primal and dual problems of SDP can be defined using linear maps as follows.

>$$
>\begin{align}
>    &\min_{x} && {C \cdot X} & \qquad \qquad \qquad & \max_{y,S}  && {b^Ty} \\\\
>    &\text{subject to } && {\mathcal{A}(X) = b} & \qquad \qquad \qquad & \text{subject to } && {\mathcal{A}^{∗}(y) + S = C} \\\\\
>    & &&{X \succeq 0} & \qquad \qquad \qquad & &&{S \succeq 0}
>\end{align}
>$$


Here $$\mathcal{A}: \mathbb{S}^n \to \mathbb{R}^m$$ means a linear map.

Assuming strong duality is satisfied, $$X^{\star}$$ and $$(y^{\star}, S^{\star})$$ where $$(X^{\star}, y^{\star}, S^{\star})$$ is a solution are optimal solutions for primal and dual, and vice versa.

> $$
> \begin{array}{rcl}
> \mathcal{A}^∗(y) + S & = & C \\\
> \mathcal{A}(X) & = & b \\\
> XS & = & 0 \\\
> X,S & \succeq & 0
> \end{array}
> $$


## Central path for SDP
**Primal barrier problem**
>$$
>\begin{align}
>    &\min_{x} && {C \cdot X−τ \log(det(X))} \\\\
>    &\text{subject to } && {A(X) = b} 
>\end{align}
>$$


**Dual barrier problem**
>$$
>\begin{align}
>    &\max_{y, S} && {b^Ty + τ \log(det(S))} \\\\
>    &\text{subject to } && {\mathcal{A}^∗(y) + S = C} 
>\end{align}
>$$


**Primal & dual을 위한 Optimality conditions**
> $$
> \begin{array}{rcl}
> \mathcal{A}^∗(y) + S & = & C \\\
> \mathcal{A}(X) & = & b \\\
> XS & = & τI \\\
> X,S & \succ & 0
> \end{array}
> $$


## Newton step
Primal central path equations 
> $$
> \begin{array}{rcl}
> \mathcal{A}^∗(y) + \tau X^{−1} & = & C \\\
> \mathcal{A}(X) & = & b \\\
> X & \succ & 0
> \end{array}
> $$


Newton equations
> $$τX^{−1}\Delta XX^{−1} +\mathcal{A}^∗(\Delta y) = −(\mathcal{A}^∗(y) + \tau X^{−1} −C)$$
> $$\mathcal{A}(\Delta X) = −(\mathcal{A}(X)−b)$$

The central path equation and Newton equation for the dual are similarly defined including $$(y,S)$$.

## Primal-dual Newton step 
Primal central path equations 
> $$\begin{bmatrix}
\mathcal{A}^∗(y) + S - C  \\\
\mathcal{A}(X) - b \\\
XS
\end{bmatrix} =
\begin{bmatrix}
0 \\\
0 \\\
τI
\end{bmatrix}
, X, S \succ 0
$$

Newton step:
> $$\begin{bmatrix}
0 & \mathcal{A}^∗ & I \\\
\mathcal{A} & 0 & 0 \\\
S & 0 & X 
\end{bmatrix}
\begin{bmatrix}
\Delta X \\\
\Delta y \\\
\Delta S
\end{bmatrix}= −
\begin{bmatrix}
\mathcal{A}^∗(y) + s−c \\\
\mathcal{A}(x) − b \\\
XS − \tau I 
\end{bmatrix}$$

