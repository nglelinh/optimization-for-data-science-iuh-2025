---
layout: post
title: 05-04 Second-Order Cone Programming (SOCP)
chapter: '05'
order: 10
owner: Hooncheol Shin
categories:
- chapter05
lang: en
---

Picture an upside-down ice-cream cone standing in 3D space: $$\{(u, t) : \|u\|_2 \le t\}$$. That clean geometric shape—the *second-order (Lorentz) cone*—unlocks a surprisingly vast slice of modern engineering. From robust linear programming under ellipsoidal uncertainty to rocket landing trajectories (used in SpaceX's powered-descent guidance!), Second-Order Cone Programming (SOCP) handles Euclidean norm constraints natively and fast.

## Key ideas: Inside the Second-Order Cone

1. **Standard SOCP Structure**: An SOCP minimizes a linear objective $$f^T x$$ subject to affine equalities $$Fx = g$$ and second-order cone constraints $$\|A_i x + b_i\|_2 \le c_i^T x + d_i$$. Equivalently, the affine map $$(A_i x + b_i,\; c_i^T x + d_i)$$ must belong to the norm cone $$\mathcal{Q}_{n_i + 1} = \{(u, t) : \|u\|_2 \le t\}$$.
2. **Subsuming LP, QP, and QCQP**:
   - Setting $$A_i = 0, b_i = 0$$ yields scalar linear inequalities $$0 \le c_i^T x + d_i$$ (LP).
   - Using the hyperbolic identity $$u^T u \le s t \iff \left\|\begin{bmatrix} 2u \\ s - t \end{bmatrix}\right\|_2 \le s + t$$ (for $$s, t \ge 0$$) converts every convex quadratic objective or inequality into a rotated second-order cone constraint (QP and QCQP).
3. **Robust Linear Programming as an SOCP**: Suppose a linear constraint $$a^T x \le b$$ must hold for *every* uncertain vector $$a$$ inside an ellipsoid $$\mathcal{E} = \{\bar{a} + Pu : \|u\|_2 \le 1\}$$. Taking the worst case gives $$\sup_{\|u\|_2 \le 1} (\bar{a} + Pu)^T x = \bar{a}^T x + \|P^T x\|_2 \le b$$—an exact SOCP constraint!
4. **Why SOCPs Are Fast**: Even though SOCPs are far more expressive than LPs, primal–dual interior-point solvers handle Lorentz cones with a simple 2-parameter self-concordant barrier $$-\ln(t^2 - \|u\|_2^2)$$, scaling to hundreds of thousands of variables.

### Worked example: Rewriting a Robust Linear Constraint as an SOCP

Suppose a chemical blend $$x = (x_1, x_2)^T \ge 0$$ must satisfy $$a_1 x_1 + a_2 x_2 \le 10$$ for *all* uncertain coefficients $$a = (a_1, a_2)^T$$ within a Euclidean ball of radius $$r = 0.5$$ around the nominal vector $$\bar{a} = (2, 3)^T$$, i.e., $$\|a - \bar{a}\|_2 \le 0.5$$.

1. **Express the worst-case left-hand side**: Write $$a = \bar{a} + 0.5 u$$ with $$\|u\|_2 \le 1$$. Then
   $$\max_{\|u\|_2 \le 1} (\bar{a} + 0.5 u)^T x = \bar{a}^T x + 0.5 \max_{\|u\|_2 \le 1} (u^T x) = 2x_1 + 3x_2 + 0.5\|x\|_2.$$
   (By Cauchy–Schwarz, the maximum occurs at $$u = x / \|x\|_2$$.)
2. **Write the exact SOCP constraint**:
   $$\|0.5 I_2 x\|_2 \le -2x_1 - 3x_2 + 10,$$
   matching $$\|A_1 x + b_1\|_2 \le c_1^T x + d_1$$ with $$A_1 = 0.5 I_2$$, $$b_1 = 0$$, $$c_1 = (-2, -3)^T$$, $$d_1 = 10$$.
3. **Test a candidate point $$x = (2, 1.5)$$**:
   - Nominal usage: $$2(2) + 3(1.5) = 4 + 4.5 = 8.5 \le 10$$ (nominally feasible with 1.5 margin).
   - Worst-case uncertainty buffer: $$0.5\sqrt{2^2 + 1.5^2} = 0.5\sqrt{6.25} = 0.5(2.5) = 1.25$$.
   - Total worst-case usage: $$8.5 + 1.25 = 9.75 \le 10$$, so $$x = (2, 1.5)$$ is **robustly feasible** against every perturbation in the ball!

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
