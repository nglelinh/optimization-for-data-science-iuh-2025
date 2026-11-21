---
layout: post
title: 18-04 Broyden-Fletcher-Goldfarb-Shanno (BFGS) update
chapter: '18'
order: '5'
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

The idea of BFGS is the same as DFP. The only difference is that the roles of $$B$$ and $$H$$ are reversed. BFGS is derived by solving the following problem.

>Solve
>$$
>\begin{align}
>& \min_{H^+} \: \: && {\|W^{1/2} (H^+ - H) W^{1/2} \|_F} \\\\
>& \text{subject to } && {H^+ = (H^+)^T} \\\\
>&&& {H^+y = s}  \\\\
>& \text{where } && W \in \mathbb{R}^{n \; \times \; n} \text{ is nonsingular and such that } Ws_k = y_k.
>\end{align}\\\\
>$$

The derived updating formulas for $$H$$ and $$B$$ are as follows.

>$$
>B^+ = B - \frac{Bss^TB}{s^TBs} + \frac{yy^T}{y^Ts}
>$$

and

>$$
>\begin{align}
>H^+ &= H + \frac{(s-Hy)s^T}{y^Ts} + \frac{s(s-Hy)^T}{y^Ts} - \frac{(s-Hy)^Ty}{(y^Ts)^2} ss^T\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big) + \frac{ss^T}{y^Ts}
>\end{align}
>$$

BFGS also preserves positive definiteness, just like DFP. (If $$B$$ is positive definite and $$s^Ty > 0$$, then $$B^+$$ is positive definite.)

An advantage of BFGS is its self-correcting property. If the matrix $$H$$ in some iteration is a poor approximation of the inverse Hessian, $$H$$ can correct itself within a few more steps. DFP cannot correct itself when the Hessian approximation is wrong, so BFGS usually performs better [14].

### Quasi-Newton in 15 seconds

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/bfgs-vs-gd_en.mp4"></video>
</div>

BFGS builds up an approximation $$H$$ of the inverse Hessian using only gradients, so the step $$-H\nabla f$$ behaves like Newton's step without ever forming the Hessian.

### Try it yourself: BFGS vs. gradient descent

<div class="opx-explainer" data-opx="bfgs" data-lang="en"></div>
