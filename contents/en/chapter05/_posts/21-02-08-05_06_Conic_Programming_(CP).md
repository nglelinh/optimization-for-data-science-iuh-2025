---
layout: post
title: 05-06 Conic Programming (CP)
chapter: '05'
order: 7
owner: Hooncheol Shin
categories:
- chapter05
lang: en
---

If the inequality constraint in a general LP is replaced by a generalized inequality constraint, the problem is called a *Conic Program* (CP).

#### Conic Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{Fx + g \preceq_K 0} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&c, x \in \mathbb{R}^{n}, A \in \mathbb{R}^{p \times n}, \text{and } b \in \mathbb{R}^{p}.
>\end{align}$$

* $$F: \mathbb{R}^n \rightarrow Y$$ is a linear map, $$g \in Y$$, for Euclidean space $$Y$$.
* LP is the special case when $$K = \mathbb{R}_{+}^n$$, i.e., LP $$\subseteq$$ CP.
* SDP is the special case when $$K = \mathbb{S}_{+}^n$$, i.e., SDP $$\subseteq$$ CP.