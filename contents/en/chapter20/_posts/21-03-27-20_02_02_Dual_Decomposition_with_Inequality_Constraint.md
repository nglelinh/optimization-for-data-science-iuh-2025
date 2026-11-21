---
layout: post
title: "20-02-02 Dual Decomposition with Inequality Constraint"
chapter: '20'
order: 6
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

Consider the following problem. The difference from the previous one is that the constraint is an inequality.
> $$
> \begin{equation}
> \min_x \sum_{i=1}^B f_i(x_i) \quad \text{subject to} \quad \sum_{i=1}^B A_i x_i \leq b
> \end{equation}
> $$

## Dual decomposition (projected subgradient method) 
For this problem the dual variable must always be nonnegative, i.e. $$u \geq 0$$. Therefore, when computing the next value of $$u$$, we project it onto the nonnegative orthant.

> $$
> \begin{alignat}{1}
> x_i^{(k)} & \in \arg \min_{x_i} f_i(x_i) + (u^{(k-1)})^T A_i x_i, \quad i=1,\dots,B  \\
> u^{(k)}   & = \left( u^{(k-1)} + t_k \left(\sum_{i=1}^B A_i x_i^{(k)} - b \right) \right)_+
> \end{alignat}
> $$

Here $$u_{+}$$ denotes the nonnegative part of $$u$$, i.e. $$(u_+)_i = \max \left\{0,u_i \right\}, i=1,\dots,m$$.
These steps are repeated for $$k=1,2,3,\dots$$

#### Price coordination interpretation
In general, dual decomposition problems can be interpreted from the viewpoint of price coordination as follows. (Vandenberghe)
> * There are $$B$$ independent units, and each unit decides its own decision variable $$x_i$$.
> * Each constraint represents a limit on a resource shared by the $$B$$ units, and the dual variable $$u_j$$ is the price of resource $$j$$.
> * The dual variables are updated as
 \begin{equation}
 u_j^{+} = (u_j - t s_j)_{+}, \quad  j=1,\dots,m
 \end{equation}
>
> $$\quad$$ where $$s=b-\sum_{i=1}^B A_ix_i$$ is the slack: \\
> $$\qquad$$ - if $$s_j < 0$$, resource $$j$$ is over-utilized, so the price $$u_j$$ is increased; \\
> $$\qquad$$ - if $$s_j > 0$$, resource $$j$$ is under-utilized, so the price $$u_j$$ is decreased; \\
> $$\qquad$$ - the price is never allowed to become negative.
