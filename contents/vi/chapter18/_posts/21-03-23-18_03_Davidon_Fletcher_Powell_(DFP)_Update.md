---
layout: post
title: 18-03 Davidon-Fletcher-Powell (DFP) Update
chapter: '18'
order: 4
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

The DFP update is a method that updates $$H (=B^{-1})$$ with a rank-2 symmetric matrix.

>$$H^+ = H + auu^T + bvv^T.$$

If $$H^+$$ computed through the DFP update satisfies the secant equation, then $$s-Hy$$ can be expressed as a linear combination of $$u$$ and $$v$$. (reference: by the secant equation, $$B^+ s =y \Leftrightarrow H^+ y = s$$)

>$$H^+y = Hy + auu^Ty + bvv^Ty = Hy + (au^Ty)u + (bv^Ty)v = s$$
>
>$$\Rightarrow s - Hy = (au^Ty)u + (bv^Ty)v$$

Setting $$u=s, v=Hy$$ and solving for $$a$$ and $$b$$, we derive the updating formula for $$H$$.
>$$
> H^+ = H - \frac{Hyy^TH}{y^THy} + \frac{ss^T}{y^Ts}
>$$

Similar to the SR1 update, we can derive the updating formula for $$B$$ using the [Sherman–Morrison formula](https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula).

>$$
>\begin{align}
>B^+ &= B + \frac{(y-Bs)y^T}{y^Ts} + \frac{y(y-Bs)^T}{y^Ts} - \frac{(y-Bs)^Ts}{(y^Ts)^2} yy^T\\\\
> &= \big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big) + \frac{yy^T}{y^Ts} 
>\end{align}
>$$

If $$B$$ is positive definite, then $$\big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big)$$ becomes positive semidefinite. In this case, if $$\frac{yy^T}{y^Ts}$$ is positive definite, then $$B^+ = \big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big) + \frac{yy^T}{y^Ts}$$ is guaranteed to be positive definite. This solves the problem of maintaining positive definiteness that was raised with SR1.

## DFP Update - Alternate Derivation

Recall: if the curvature condition ($$y^Ts > 0, y,s \in \mathbb{R}^n$$) is satisfied, then there exists a symmetric positive definite matrix that satisfies the secant equation.

The DFP update can also be derived by solving the problem of minimizing the weighted Frobenius norm between matrix $$B^+$$ and $$B$$ where $$B^+$$ 1. satisfies symmetry and 2. satisfies the secant equation. (Each different matrix norm corresponds to each different Quasi-Newton method. Among them, the norm that makes it easy to solve this problem while also making it work as a scale-invariant optimization method is the weighted Frobenius norm.)

>Solve
>$$
>\begin{align}
>& \min_{B^+} \: \: && {\|W^{1/2} (B^+ - B) W^{1/2} \|_F} \\\\
>& \text{subject to } && {B^+ = (B^+)^T} \\\\
>    &&& {B^+s = y}  \\\\
>& \text{where } && W \in \mathbb{R}^{n \; \times \;n} \text{ is nonsingular and such that } Wy_k = s_k.
>\end{align}\\\\
>$$

***reference**:

* Frobenius norm: The Frobenius norm of matrix $$A$$ is defined as follows.
$$
\| A \|_{F}  \doteq ( \sum_{i,j} A_{i,j}^2 )^{1/2}
$$

* Weighted Frobenius norm: The weighted Frobenius norm of matrix $$A$$ with weight matrix $$W(W \succ 0)$$ is defined as follows. 
$$
\|A\|_W \doteq \| W^{1/2} A W^{1/2} \|_F
$$