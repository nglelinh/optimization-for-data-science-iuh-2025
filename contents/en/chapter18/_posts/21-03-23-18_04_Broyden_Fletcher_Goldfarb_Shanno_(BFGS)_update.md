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

In 1970, four researchers working independently—Charles Broyden, Roger Fletcher, Donald Goldfarb, and David Shanno—published the exact same algebraic twist on DFP: instead of applying the rank-2 formula to $$H$$ (and inverting to get $$B$$), apply it to $$B$$ (and invert to get $$H$$). That seemingly innocent symmetry swap created **BFGS**, widely regarded as the most effective general-purpose smooth unconstrained optimization algorithm of the past half-century, famous for its remarkable ability to self-correct bad Hessian estimates on the fly.

## Key ideas: Why BFGS Is the Gold Standard of Quasi-Newton Methods

- **Exact Algebraic Duality with DFP:** Swapping $$(B, s, y) \leftrightarrow (H, y, s)$$ in the DFP formula immediately produces the BFGS Hessian update $$B^+ = B - \frac{B s s^T B}{s^T B s} + \frac{y y^T}{y^T s}$$ and its Sherman–Morrison–Woodbury inverse $$H^+ = (I - \rho s y^T) H (I - \rho y s^T) + \rho s s^T$$, where $$\rho = 1/(y^T s)$$.
- **Minimum-Change Principle on $$H^+$$:** Whereas DFP minimizes the weighted Frobenius change in $$B$$, BFGS minimizes $$\|W^{1/2}(H^+ - H)W^{1/2}\|_F$$ subject to symmetry and $$H^+ y = s$$ (with $$W s = y$$), directly stabilizing the *inverse* operator used to generate search steps.
- **Hereditary Positive Definiteness:** For any $$v \neq 0$$, letting $$w = (I - \rho y s^T) v$$ gives $$v^T H^+ v = w^T H w + \rho (v^T s)^2 > 0$$ whenever $$H \succ 0$$ and $$\rho = (y^T s)^{-1} > 0$$—an even cleaner congruence proof than DFP's.
- **Superior Self-Correction Property:** When $$H_k$$ has an erroneously large eigenvalue along a step direction, BFGS corrects it in a single update (whereas DFP can take many steps to shrink it), making BFGS far more robust with inexact Wolfe line searches.

### Worked example: Computing Both $$B_1$$ and $$H_1$$ in BFGS and Checking $$B_1 H_1 = I$$

Use the exact same inputs as the DFP lesson so you can compare them directly: $$B_0 = H_0 = I_2$$, $$s = (1, 0)^T$$, $$y = (2, 1)^T$$, $$\rho = \frac{1}{y^T s} = \frac{1}{2}$$.

1. **Compute $$B_1^{\text{BFGS}}$$:**
   With $$s^T B_0 s = 1$$ and $$y^T s = 2$$:
   $$B_1^{\text{BFGS}} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} - \frac{1}{1}\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} + \frac{1}{2}\begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 1.5 \end{bmatrix}.$$
   Verify secant equation: $$B_1^{\text{BFGS}} s = (2, 1)^T = y$$ $$\checkmark$$.
2. **Compute $$H_1^{\text{BFGS}}$$ via the congruence formula:**
   First form $$V = I - \rho s y^T = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} - \frac{1}{2}\begin{bmatrix} 2 & 1 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & -0.5 \\ 0 & 1 \end{bmatrix}$$.
   Since $$H_0 = I$$:
   $$H_1^{\text{BFGS}} = V V^T + \rho s s^T = \begin{bmatrix} 0.25 & -0.5 \\ -0.5 & 1 \end{bmatrix} + \begin{bmatrix} 0.5 & 0 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 0.75 & -0.5 \\ -0.5 & 1.0 \end{bmatrix}.$$
3. **Verify exact inverse consistency $$B_1^{\text{BFGS}} H_1^{\text{BFGS}} = I_2$$:**
   $$\begin{bmatrix} 2 & 1 \\ 1 & 1.5 \end{bmatrix}\begin{bmatrix} 0.75 & -0.5 \\ -0.5 & 1.0 \end{bmatrix} = \begin{bmatrix} 1.5 - 0.5 & -1 + 1 \\ 0.75 - 0.75 & -0.5 + 1.5 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \quad \checkmark$$
4. **Compare directly against DFP:**
   Notice $$H_1^{\text{BFGS}} = \begin{bmatrix} 0.75 & -0.5 \\ -0.5 & 1.0 \end{bmatrix}$$ differs from $$H_1^{\text{DFP}} = \begin{bmatrix} 0.7 & -0.4 \\ -0.4 & 0.8 \end{bmatrix}$$ even after a *single* step from $$I_2$$! Their difference is a pure rank-1 matrix $$\begin{bmatrix} 0.05 & -0.1 \\ -0.1 & 0.2 \end{bmatrix} = 0.2 \begin{bmatrix} -0.5 \\ 1 \end{bmatrix}\begin{bmatrix} -0.5 & 1 \end{bmatrix}$$—which leads directly into the Broyden class!

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

### BFGS vs. gradient descent (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/bfgs-vs-gd_en.mp4"></video>
</div>

BFGS builds up an approximation $$H$$ of the inverse Hessian using only gradients, so the step $$-H\nabla f$$ behaves like Newton's step without ever forming the Hessian.

### Try it yourself: BFGS vs. gradient descent

<div class="opx-explainer" data-opx="bfgs" data-lang="en"></div>
