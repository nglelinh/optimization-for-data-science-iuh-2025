---
layout: post
title: 05-03 Quadratically Constrained Quadratic Programming (QCQP)
chapter: '05'
order: 4
owner: Hooncheol Shin
categories:
- chapter05
lang: en
---

If the inequality constraint functions in a quadratic program are replaced with convex quadratic functions, the problem is called a *Quadratically Constrained Quadratic Program* (QCQP).

### Quadratically Constrained Quadratic Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P_0 x + q_0^T x + r_0} \\\\
>    &\text{subject to } &&{(1/2)x^T P_i x + q_i^T x + r_i \leq 0}, i = 1, \dotsc, m\\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P_i \in \mathbb{S}_{+}^n \text{ for } i = 0, \dotsc, m, \text{ and } A \in \mathbb{R}^{p \times n}.
>\end{align} $$

## QP and equivalent QCQP
If $$P_i = 0$$ for all $$i = 1, \dotsc, m$$ in the QCQP constraints, the problem reduces to a QP. Thus, QP is a special case of QCQP, and $$QP \subseteq QCQP$$.

### Recall: Quadratic Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{subject to } &&{Gx \preceq h} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P \in \mathbb{S}_{+}^n, G \in \mathbb{R}^{m \times n}, \text{ and } A \in \mathbb{R}^{p \times n}.
>\end{align} $$