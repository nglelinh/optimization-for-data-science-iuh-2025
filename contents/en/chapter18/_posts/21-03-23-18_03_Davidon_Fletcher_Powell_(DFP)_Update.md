---
layout: post
title: 18-03 Davidon-Fletcher-Powell (DFP) Update
chapter: '18'
order: 4
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

DFP update는 rank-2의 symmetric matrixto, $$H (=B^{-1})$$를 업데이트 하는 method이다.

>$$H^+ = H + auu^T + bvv^T.$$

DFP update를 through, computation된 $$H^+$$가 secant equation을 만족한다면, $$s-Hy$$은 $$u$$and, $$v$$의 linear combinationwith, 표현할 수 있다. (reference: secant equationby,, $$B^+ s =y \Leftrightarrow H^+ y = s$$)

>$$H^+y = Hy + auu^Ty + bvv^Ty = Hy + (au^Ty)u + (bv^Ty)v = s$$
>
>$$\Rightarrow s - Hy = (au^Ty)u + (bv^Ty)v$$

$$u=s, v=Hy$$to, 두고 aand, babout, 풀면 $$H$$to, about, updating formula가 유도된다.
>$$
> H^+ = H - \frac{Hyy^TH}{y^THy} + \frac{ss^T}{y^Ts}
>$$

SR1 updateat,and, 마찬가지to, [Sherman–Morrison formula](https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula)를 using, $$B$$to, about, updating formula를 유도할 수 있다.

>$$
>\begin{align}
>B^+ &= B + \frac{(y-Bs)y^T}{y^Ts} + \frac{y(y-Bs)^T}{y^Ts} - \frac{(y-Bs)^Ts}{(y^Ts)^2} yy^T\\\\
> &= \big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big) + \frac{yy^T}{y^Ts} 
>\end{align}
>$$

if, $$B$$가 positive definite이면 $$\big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big)$$는 positive semidefinite이 된다. 이when, $$\frac{yy^T}{y^Ts}$$가 positive definite이면 $$B^+ = \big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big) + \frac{yy^T}{y^Ts}$$는 positive definite임이 보장된다. 이to,써 SR1at, 제기 되었던 positive definiteness의 지속성 problem가 solution결된다.

## DFP Update - Alternate Derivation

Recall: curvature condition($$y^Ts > 0, y,s \in \mathbb{R}^n$$)을 만족하면 secant equation을 만족하는 symmetric positive definite matrix가 존재한다.

DFP update는 1. symmetry를 만족하고, 2. secant equation을 만족하는 matrix $$B^+$$and, $$B$$의 weighted Frobenius norm을 minimization 시키는 problem를 푸는 것with,도 유도된다. (각각의 다른 matrix norm은 각각의 다른 Quasi-Newton methodand, connection,된다. 그 중at, 이 problem의 solution을 구하기 쉽게 하면서도 scale-invariant optimization methodto, 작동하게끔 하는 norm이 바to, weighted Frobenius norm이다.)

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

* Frobenius norm: matrix $$A$$to, about, Frobenius norm은 as follows: 정의된다.
$$
\| A \|_{F}  \doteq ( \sum_{i,j} A_{i,j}^2 )^{1/2}
$$

* Weighted Frobenius norm: 가중치 matrix $$W(W \succ 0)$$to, about, matrix $$A$$의 weighted Frobenius norm은 as follows: 정의된다. 
$$
\|A\|_W \doteq \| W^{1/2} A W^{1/2} \|_F
$$