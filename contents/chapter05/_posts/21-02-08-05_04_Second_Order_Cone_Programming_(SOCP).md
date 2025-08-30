---
layout: post
title: 05-04 Second-Order Cone Programming (SOCP)
chapter: "05"
order: 5
owner: "Hooncheol Shin"
---

If the inequality constraints in a general LP are replaced with second-order cone constraints (which are affine functions), the problem is called a *Second-Order Cone Program* (SOCP).

### Second-Order Cone Program

>$$
>\begin{align}
>    &\text{minimize}_{x} &&{f^T x} \\\\
>    &\text{subject to } &&{\| A_i x + b_i \|_2 \leq c_i^T x + d_i, i = 1, \dotsc, m}\\\\
>    & &&{Fx = g},\\\\
>    & \text{where } &&x \in \mathbb{R}^n \text{ is the optimization variable, } A_i  \in \mathbb{R}^{n_i \times n}, \text{ and } F \in \mathbb{R}^{p \times n}.
>\end{align} $$

### Recall: Norm cone
A *norm cone* is a convex cone in $$\mathbb{R}^{n+1}$$ defined by all points $$(x, t)$$ such that $$\| x \| \le t$$ for some norm $$\| \cdot \|$$.

>$$\left\{(x, t) : \| x \| \le t \right\} \text{, for a norm } \| \cdot \|$$

The figure below shows the norm cone for the $$l_2$$ norm $$\| \cdot \|_2$$, also called the second-order cone or ice cream cone.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_04_Norm_Cone.png" alt="[Fig1] Norm Cone [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Norm Cone [1]</figcaption>
</p>
</figure>

## QCQP and equivalent SOCP
A QCQP can be reformulated as an SOCP in certain cases, i.e., $$QCQP \subseteq SOCP$$.

### Recall: Quadratically Constrained Quadratic Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P_0 x + q_0^T x + r_0} \\\\
>    &\text{subject to } &&{(1/2)x^T P_i x + q_i^T x + r_i \leq 0}, i = 1, \dotsc, m\\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P_i \in \mathbb{S}_{+}^n \text{ for } i = 0, \dotsc, m, \text{ and } A \in \mathbb{R}^{p \times n}
>\end{align} $$
>
**Step 1.** For convenience, QCQP can be reformulated in different ways to fit SOCP structure.
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{x^T P_0 x + 2q_0^T x + r_0} \\\\
>    &\text{subject to } &&{x^T P_i x + 2q_i^T x + r_i \leq 0}, i = 1, \dotsc, m\\\\
>    & &&{Ax = b},\\\\
>    & \text{where } && P_i \in \mathbb{S}_{+}^n \text{ for } i = 0, \dotsc, m \text{, and } A \in \mathbb{R}^{\text{p x n}}.
>\end{align}\\
>$$
>

**Step 2.** Since $$P_0$$ is a positive semidefinite matrix, any $$ \tilde{P_0}$$ satisfying $$P_0 = \tilde{P_0}\tilde{P_0}$$ is also a positive semidefinite matrix. This $$\tilde{P_0}$$ can be obtained through eigendecomposition. Using this, the objective function of the QCQP can be transformed as follows:

* $$P_0 = Q_0 \Lambda_0 \Lambda_0 Q_0^T$$
* $$I = Q_0 \Lambda_0 \Lambda_0^{-1} Q_0^{-1} = Q_0 \Lambda_0^{-1} \Lambda_0 Q_0^{-1}$$

> $$
> \begin{align}
> {x^T P_0 x + 2q_0^T x + r_0} &= {x^T P_0 x + q_0^T x + x^T q_0 + q_0^T P_0^{-1} q_0 - q_0^T P_0^{-1} q_0 + r_0}\\\\
> &= {x^T Q_0 \Lambda_0 \Lambda_0 Q_0^T x} +
>      {q_0^T Q_0 \Lambda_0^{-1} \Lambda_0 Q_0^{-1} x} + {x^T Q_0 \Lambda_0 \Lambda_0^{-1} Q_0^{-1} q_0} +
>      {q_0^T Q_0 \Lambda_0^{-1} \Lambda_0^{-1} Q_0^T q_0} - {q_0^T P_0^{-1} q_0 + r_0}\\\\
> &=(\Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0)^T(\Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0) - {q_0^T P_0^{-1} q_0 + r_0}\\\\
> &=\| \Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0 \|_2^2 - {q_0^T P_0^{-1} q_0 + r_0}\\\\
> \end{align}
> $$

**Step 3.** The same procedure as in Step 2 is applied to the inequality constraint functions, and then substituted into the QCQP from Step 1.

>$$
>\begin{align}
>    &\text{minimize}_{x} &&{\| \Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0 \|_2^2 - {q_0^T P_0^{-1} q_0 + r_0}} \\\\
>    &\text{subject to } &&{\| \Lambda_i Q_i^T x + \Lambda_i^{-1} Q_i^T q_i \|_2^2 \leq {q_i^T P_i^{-1} q_i + r_i}}, i = 1, \dotsc, m\\\\
>    & &&{Ax = b}.\\\\
>\end{align}
>$$
>

**Step 4.** The term $${q_0^T P_0^{-1} q_0 + r_0}$$ in the objective function is a constant and can be omitted.
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{\| \Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0 \|_2^2} \\\\
>    &\text{subject to } &&{\| \Lambda_i Q_i^T x + \Lambda_i^{-1} Q_i^T q_i \|_2^2 \leq {q_i^T P_i^{-1} q_i + r_i} }, i = 1, \dotsc, m\\\\
>    & &&{Ax = b}.\\\\
>\end{align}
>$$

**Step 5.** Introducing a scalar variable $$t$$, the same problem as in Step 4 can be defined.
>$$
>\begin{align}
>    &\text{minimize}_{x, t} &&{t} \\\\
>    &\text{subject to } &&\lVert{\Lambda_{0} Q_0^T x + \Lambda_0^{-1} Q_0^T q_0} \rVert_2^2 \leq t\\\\
>    & &&{\| \Lambda_i Q_i^T x + \Lambda_i^{-1} Q_i^T q_i \|_2^2 \leq {q_i^T P_i^{-1} q_i + r_i} }, i = 1, \dotsc, m\\\\
>    & &&{Ax = b}.\\\\
>\end{align}
>$$

The above represents a special case of SOCP. Thus, the relationship $$QCQP \subseteq SOCP$$ holds.
