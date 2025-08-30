---
layout: post
title: 05-05 Semidefinite Programming (SDP)
chapter: "05"
order: 6
owner: "Hooncheol Shin"
---

If the inequality constraint in a general LP is replaced by a linear matrix inequality (LMI), the problem is called a *Semidefinite Program* (SDP).

### Semidefinite Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{x_1 F_1 + \dotsb + x_n F_n + G \preceq 0} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&G, F_1, \dotsb, F_n \in \mathbb{S}^{k} \text{ and } A \in \mathbb{R}^{p \times n}.
>\end{align}$$

* If $$G, F_1, \dotsb, F_n$$ are all diagonal matrices, the above inequality constraint is equivalent to $$n$$ linear inequalities, and the SDP reduces to an LP.
* Multiple LMIs can be represented as a single LMI using block diagonal matrices:
> $$
> x_1\hat{F_1} + \dotsb + x_n\hat{F_n} + \hat{G} \preceq 0, \quad x_1\tilde{F_1} + \dotsb + x_n\tilde{F_n} + \tilde{G} \preceq 0
> $$
> is equivalent to a single LMI:
> $$
> x_1
> \begin{bmatrix}
>     \hat{F_1} & 0 \\\\
>     0 & \tilde{F_1} \\\\
> \end{bmatrix} + 
> x_2
> \begin{bmatrix}
>     \hat{F_2} & 0 \\\\
>     0 & \tilde{F_2} \\\\
> \end{bmatrix} + 
> \dotsb
> +
> x_n
> \begin{bmatrix}
>     \hat{F_n} & 0 \\\\
>     0 & \tilde{F_n} \\\\
> \end{bmatrix} + 
> \begin{bmatrix}
>     \hat{G} & 0 \\\\
>     0 & \tilde{G} \\\\
> \end{bmatrix}
> \preceq 0
> $$

## SDP in Standard form
When expressed as follows, it is called the standard form of a semidefinite program.

### Standard form SDP
>$$
>\begin{align}
>    &\text{minimize}_{X} &&{\mathrm{tr}(CX)} \\\\
>    &\text{subject to } &&{\mathrm{tr}(A_i X) = b_i, \quad i = 1, \dotsc, m} \\\\
>    & &&{X \succeq 0},\\\\
>    & \text{where } &&C, A_i \in \mathbb{S}^n, X \in \mathbb{S}^n.
>\end{align}$$

* Recall: $$\mathrm{tr}(CX) = \sum_{i,j=1}^n C_{ij}X_{ij}$$

All SDPs can be transformed into the standard form SDP through the following process.

### Converting SDPs to standard form
**Step1.**  Use a slack variable S to convert the inequality constraint into an equality constraint.
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{\sum_{l=1}^n F_l x_l+ S = -G} \\\\
>    & &&{Ax = b}\\\\
>    & &&{S \succeq 0}
>\end{align}
>$$

**Step2.** Transform the equality constraints derived in Step 1 into component-wise equations.
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{\sum_{l=1}^n (F_l x_l)_{ij} + S_{ij} = -G_{ij}, i,j = 1, \dotsc, k} \\\\
>    & &&{Ax = b}\\\\
>    & &&{S \succeq 0}
>\end{align}
>$$

**Step3.** Replace x with two nonnegative variables.
$$x = x^{+}  - x^{-}$$, where $$x^{+} \text{ and } x^{-} \succeq 0.$$
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T (x^{+}  - x^{-}) + d} \\\\
>    &\text{subject to } &&{\sum_{l=1}^n (F_l x^{+} _l)_{ij} - \sum_{l=1}^n (F_l x^{-} _l)_{ij} + S_{ij} = -G_{ij}, i,j = 1, \dotsc, k} \\\\
>    & &&{Ax^{+}  - Ax^{-} = b}\\\\
>    & &&{S \succeq 0}\\\\
>    & &&{x^{+} \text{, } x^{-} \succeq 0}.
>\end{align}
>$$

**Step4.** Define $$X, C, \tilde{A}, \tilde{b}$$.

* All the blanks are zero.

> $$
> X = 
> \begin{bmatrix}
> diag(x^{+})\\\\
>  & diag(x^{-})\\\\
> && s_{11}\\\\
> &&& s_{12}\\\\
> &&&&\dotsc\\\
> &&&&&s_{ij}\\\\
> &&&&&&\dotsc \\\
> &&&&&&&s_{kk}\\\\
> \end{bmatrix}
> ,$$
> $$
> C = 
> \begin{bmatrix}
> diag(c)\\\\
> & -diag(c) &\\\\
> & & O_{k^2 \text{ x } k^2}\\\\
> \end{bmatrix}
> ,$$
> $$
> P_{ij} = 
> \begin{bmatrix}
> (F_1)_{ij}\\\\
> &(F_2)_{ij}\\\\
> &&\dotsc\\\\
> &&&(F_n)_{ij}\\\\
> &&&&-(F_1)_{ij}\\\\
> &&&&&-(F_2)_{ij}\\\\
> &&&&&&\dotsc\\\\
> &&&&&&&-(F_n)_{ij}\\\\
> &&&&&&&&0&\\\\
> &&&&&&&&&\dotsc\\\\
> &&&&&&&&&&1 \phantom{1} (\text{ij th position})\\\\
> &&&&&&&&&&&\dotsc\\\\
> &&&&&&&&&&&&0\\\\
> \end{bmatrix}
> ,$$
>
> $$
> Q_{i}= 
> \begin{bmatrix}
> diag(A_i)\\\\
> &-diag(A_i)\\\\
> &&O_{k^2 \text{ x } k^2}\\\\
> \end{bmatrix}
> $$
> ($$A_i$$ is ith row of A),
> $$
> \tilde{A} = 
> \begin{bmatrix}
> P_{11}\\\\
> \dotsc\\\\
> P_{kk}\\\\
> Q_{1}\\\\
> \dotsc\\\\
> Q_{p}\\\\
> \end{bmatrix}
> -G_{ij} = \mathrm{tr}(P_{ij}X)
> ,$$
>
> $$
> b_i = \mathrm{tr}(Q_iX)
> $$,
>
> $$
> \tilde{b} = 
> \begin{bmatrix}
> -G_{11}\\\\
> \dotsc\\\\
> -G_{kk}\\\\
> b_{1}\\\\
> \dotsc\\\\
> b_{p}\\\\
> \end{bmatrix}
> $$.

**Step5.** Substitute the problem from *Step3* with $$X, C, \tilde{A}, \tilde{b}$$.

>$$
>\begin{align}
>    &\text{minimize}_{X} &&{\mathrm{tr}(CX)} \\\\
>    &\text{subject to } &&{\mathrm{tr}(\tilde{A}_iX) = \tilde{b}_i, \quad i=1,\dotsc,k^2+p} \\\\
>    & &&{X \succeq 0}.
>\end{align}
>$$

## SOCP and equivalent SDP
By using the Schur complement[[8](https://en.wikipedia.org/wiki/Schur_complement)], the inequality constraint of SOCP can be expressed in such a way that SOCP is transformed into a special case of SDP. That is, there is a relationship of inclusion: SOCP $$\subseteq$$ SDP.

### Recall: Second-Order Cone Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{f^T x} \\\\
>    &\text{subject to } &&{\| A_i x + b_i \|_2 \leq c_i^T x + d_i, i = 1, \dotsc, m}\\\\
>    & &&{Fx = g}.
>\end{align}
>$$

### SOCP to SDP by Schur complement
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{f^T x} \\\\
>    &\text{subject to } 
>    &&
>    \begin{bmatrix}
>    (c_i^T x + d)I    & A_i x + b_i \\\\
>    (A_i x + b_i)^T & c_i^T x + d \\\\
>    \end{bmatrix} \succeq 0, i = 1, \dotsc, m\\\\
>    & &&{Fx = g}.
>\end{align}
>$$