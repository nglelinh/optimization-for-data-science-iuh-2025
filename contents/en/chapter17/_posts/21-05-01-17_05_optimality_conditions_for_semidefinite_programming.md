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

Step up from vectors $$x \ge 0$$ to symmetric positive semidefinite matrices $$X \succeq 0$$, and suddenly optimization can certify polynomial nonnegativity, compute Lovász theta numbers of graphs, design robust control Lyapunov functions, and relax NP-hard combinatorial problems like MAX-CUT. Yet the primal-dual interior-point machinery carries over with astonishing elegance: the vector inner product $$c^T x$$ becomes the trace inner product $$C \cdot X = \operatorname{tr}(CX)$$, and complementarity $$x_i s_i = 0$$ becomes the matrix equation $$XS = 0$$—with one fascinating twist caused by non-commutativity of matrices.

## Background Knowledge Map: Lifting Interior-Point Theory to the PSD Cone

- **Trace Inner Product & Self-Dual Cone:** On the space $$\mathbb{S}^n$$ of symmetric $$n \times n$$ matrices with inner product $$\langle A, B \rangle = \operatorname{tr}(AB)$$, the PSD cone $$\mathbb{S}_+^n$$ is self-dual: $$X \succeq 0 \iff \operatorname{tr}(XS) \ge 0$$ for all $$S \succeq 0$$.
- **Matrix Complementarity ($$XS = 0$$):** For $$X, S \succeq 0$$, $$\operatorname{tr}(XS) = 0$$ is equivalent to the matrix product $$XS = 0$$, meaning $$X$$ and $$S$$ share an eigenbasis with disjoint supports of positive eigenvalues ($$\operatorname{rank}(X) + \operatorname{rank}(S) \le n$$).
- **Slater's Condition & Strong Duality Subtlety:** Unlike LP, where feasibility implies strong duality, SDPs can exhibit positive duality gaps or unattained optima unless strict feasibility ($$\exists X \succ 0$$ or $$\exists S \succ 0$$) holds.
- **Symmetrizing the Newton Step (AHO, HRVW/KSH/M, NT Directions):** Perturbing complementarity to $$XS = \mu I$$ gives a nonsymmetric linearization $$X\Delta S + \Delta X\, S = \mu I - XS$$. Because $$\Delta X, \Delta S$$ must stay symmetric, SDP solvers apply a similarity symmetrization $$H_P(M) = \frac{1}{2}(P M P^{-1} + P^{-T} M^T P^T)$$, giving rise to the classical Alizadeh–Haeberly–Overton, Helmberg–Rendl–Vanderbei–Wolkowicz, and Nesterov–Todd search directions.

### Step-by-Step Worked Example (Read Slowly): Computing an Exact $$2 \times 2$$ SDP Central Path

Consider the $$2 \times 2$$ primal-dual SDP with $$C = \operatorname{diag}(1, 2)$$, $$A_1 = I_2$$, and $$b_1 = 2$$:
$$\min_{X \succeq 0} \; X_{11} + 2X_{22} \quad \text{s.t.} \quad X_{11} + X_{22} = 2, \qquad \max_{y \in \mathbb{R}} \; 2y \quad \text{s.t.} \quad S = \begin{bmatrix} 1 - y & 0 \\ 0 & 2 - y \end{bmatrix} \succeq 0.$$

1. **Find the exact optimal primal-dual pair:**
   Dual feasibility $$S \succeq 0$$ requires $$1 - y \ge 0$$ and $$2 - y \ge 0$$, so $$y^\star = 1$$ with dual optimal value $$2$$ and $$S^\star = \operatorname{diag}(0, 1)$$. Primal optimality forces $$X^\star S^\star = 0 \implies X_{22}^\star = 0$$ and $$X_{12}^\star = 0$$, so $$X^\star = \operatorname{diag}(2, 0)$$ with primal value $$2$$.
2. **Write the perturbed complementarity equations $$XS = \mu I_2$$:**
   Since $$S$$ is diagonal and strictly positive definite for $$y < 1$$, $$X = \mu S^{-1}$$ is also diagonal:
   $$X(\mu) = \begin{bmatrix} \frac{\mu}{1 - y} & 0 \\ 0 & \frac{\mu}{2 - y} \end{bmatrix}.$$
3. **Enforce primal feasibility $$\operatorname{tr}(X(\mu)) = 2$$ at $$\mu = 0.5$$:**
   $$\frac{0.5}{1 - y} + \frac{0.5}{2 - y} = 2 \implies \frac{3 - 2y}{(1 - y)(2 - y)} = 4 \implies 4y^2 - 10y + 5 = 0.$$
   Selecting the strictly dual-feasible root $$y < 1$$:
   $$y(0.5) = \frac{10 - \sqrt{100 - 80}}{8} = \frac{5 - \sqrt{5}}{4} \approx 0.690983.$$
4. **Verify interior positivity and exact duality gap:**
   $$S(0.5) \approx \operatorname{diag}(0.309017, \; 1.309017) \succ 0, \qquad X(0.5) \approx \operatorname{diag}(1.618034, \; 0.381966) \succ 0.$$
   Check: $$\operatorname{tr}(X(0.5)) = 2.000000$$, $$X(0.5)S(0.5) = 0.5\, I_2$$, and the duality gap is $$C \cdot X - 2y = 2.381966 - 1.381966 = 1.000000 = n\mu$$ identically!

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
