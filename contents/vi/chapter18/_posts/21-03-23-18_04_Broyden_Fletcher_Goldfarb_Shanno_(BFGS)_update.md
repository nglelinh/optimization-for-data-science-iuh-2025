---
layout: post
title: 18-04 Broyden-Fletcher-Goldfarb-Shanno (BFGS) update
chapter: '18'
order: 5
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

The idea of BFGS is the same as DFP. The only difference is that the roles of B and H are reversed.

BFGS is derived by solving the following problem.

>Solve
>$$
>\begin{align}
>& \min_{H^+} \: \: && {\|W^{1/2} (H^+ - H) W^{1/2} \|_F} \\\\
>& \text{subject to } && {H^+ = (H^+)^T} \\\\
>&&& {H^+s = y}  \\\\
>& \text{where } && W \in \mathbb{R}^{n \; \times \;n} \text{ is nonsingular and such that } Ws_k = y_k.
>\end{align}\\\\
>$$

The derived updating formulas for $$H$$ and $$B$$ are as follows.

>$$
> B^+ = B - \frac{Bss^TB}{s^TBs} + \frac{yy^T}{y^Ts}
>$$

and

>$$
>\begin{align}
>H^+ &= H + \frac{(s-Hy)s^T}{y^Ts} + \frac{s(s-Hy)^T}{y^Ts} - \frac{(s-Hy)^Ty}{(y^Ts)^2} ss^T\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big) + \frac{ss^T}{y^Ts} 
>\end{align}
>$$

BFGS also, DFP처럼 positive definiteness를 유지한다. (if, $$B$$가 positive definite이고 $$s^Ty > 0$$이면 $$B^+$$는 positive definite이다.)

BFGS의 특장점은 self-correcting property를 지니고 있다는 것이다. if, matrix $$H$$가 부정확하게 추정되어 iteration의 속도가 느려지게 되면 Hessian approximation이 단 몇 step 만to, 이를 바to,잡는 경향성을 보인다. 반면 DFP는 잘못된 Hessian approximation의 추정about, effect,적with, 바to,잡지 못하므to, 실전at,는 usually, BFGS의 성능이 더 좋은 편이다 [14].