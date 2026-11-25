---
layout: post
title: 19-01 Proximal Newton method
chapter: '19'
order: 2
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

If you already know proximal gradient descent (Chapter 9), you are literally one matrix away from the **proximal Newton method**. Proximal gradient approximates the smooth function $$g$$ at each step by a *round, isotropic bowl* $$\frac{1}{2t}\|z - x\|_2^2$$; proximal Newton replaces that isotropic sphere with the *true elliptical bowl* $$\frac{1}{2}(z - x)^T \nabla^2 g(x)(z - x)$$. That geometric upgrade—from spheres to curvature-matched ellipsoids—is the unifying thread of Section 19-01.

## Key ideas: From Spherical to Ellipsoidal Proximal Models

- **Local Quadratic Approximation of $$g$$:** Proximal gradient replaces $$g(z)$$ by $$g(x) + \nabla g(x)^T(z - x) + \frac{1}{2t}\|z - x\|_2^2$$; proximal Newton replaces $$\frac{1}{t} I$$ by the local Hessian $$H = \nabla^2 g(x)$$.
- **Exact Preservation of $$h$$:** Neither method linearizes the nonsmooth part $$h(z)$$; keeping $$h(z)$$ exact inside the subproblem preserves sparsity, low-rank structure, or constraint feasibility at every iteration.
- **The Scaled Proximal Operator:** Completing the square in the proximal Newton subproblem rewrites the update compactly as $$x^+ = \operatorname{prox}_H(x - H^{-1}\nabla g(x))$$, mirroring proximal gradient's $$x^+ = \operatorname{prox}_{t h}(x - t \nabla g(x))$$.
- **Why Ellipsoidal Geometry Matters:** When features are strongly correlated or differently scaled, isotropic spheres bounce back and forth across valleys; Hessian-shaped ellipsoids point straight down the ravine toward the nonsmooth optimum.

### Worked example: Spherical vs. Ellipsoidal Model at the Origin

Consider $$g(x) = \frac{1}{2}(x_1^2 + 100 x_2^2) - 2x_1 - 200 x_2$$ and $$h(x) = |x_1| + |x_2|$$ at $$x^0 = (0, 0)^T$$. Here $$\nabla g(0) = (-2, -200)^T$$ and $$\nabla^2 g(0) = \operatorname{diag}(1, 100)$$.

1. **Exact optimum (for reference):**
   Stationarity gives $$x_1 - 2 + \operatorname{sign}(x_1) = 0 \implies x_1^\star = 1$$ and $$100x_2 - 200 + \operatorname{sign}(x_2) = 0 \implies x_2^\star = 1.99$$.
2. **Spherical model (Proximal Gradient with $$t = 1/L = 0.01$$):**
   $$x^0 - t\nabla g(0) = (0.02, 2.00)^T \xrightarrow{S_{0.01}} x^1_{\text{PG}} = (0.01, 1.99)^T.$$
   Coordinate $$x_2$$ hits $$1.99$$ immediately, but $$x_1$$ only reaches $$0.01$$ ($$1\%$$ of the way to $$x_1^\star = 1$$!).
3. **Ellipsoidal model (Proximal Newton with $$H = \operatorname{diag}(1, 100)$$):**
   Compute the Newton target $$x^0 - H^{-1}\nabla g(0) = (2, 2)^T$$ and apply $$\operatorname{prox}_H$$:
   $$z_1 = S_{1/1}(2) = 1.00, \qquad z_2 = S_{1/100}(2) = 1.99.$$
   In one ellipsoidal step, *both* coordinates hit the exact optimum $$(1.00, 1.99)^T$$ simultaneously!

In this section, we will review the **proximal gradient method** and examine how the **proximal newton method** emerged from it.

We will also examine the definition of the **proximal newton method** and the scaled proximal map that has good properties such as uniqueness and non-expansiveness compared to the general proximal map.

### Proximal Newton vs. proximal gradient (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/prox-newton_en.mp4"></video>
</div>

Proximal gradient uses a scalar step; proximal Newton minimises the quadratic model with the true Hessian plus $$\lambda\|x\|_1$$, so it needs far fewer iterations.

### Try it yourself: proximal gradient vs proximal Newton

<div class="opx-explainer" data-opx="pn" data-lang="en"></div>
