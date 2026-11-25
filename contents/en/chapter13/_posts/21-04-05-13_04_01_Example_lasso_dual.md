---
layout: post
title: 13-04-01 Example lasso dual
chapter: '13'
order: 6
owner: Wontak Ryu
categories:
- chapter13
lang: en
---

At first glance, the Lasso objective $$\frac{1}{2}\|y - X\beta\|_2^2 + \lambda\|\beta\|_1$$ has *no constraints*—so taking its Lagrange dual directly yields a useless constant. Yet by introducing a single dummy residual variable $$z = X\beta$$, the nonsmooth $$\ell_1$$ penalty magically flips into an $$\ell_\infty$$ polytope constraint, turning Lasso into the clean geometric problem of projecting the response vector $$y$$ onto a polytope!

## Key ideas: Anatomy of the Lasso Dual

- **Pillar 1 — Variable Splitting Creates a Nontrivial Dual:** Introducing $$z = X\beta$$ decouples the smooth quadratic fit $$\frac{1}{2}\|y-z\|_2^2$$ from the nonsmooth sparsity penalty $$\lambda\|\beta\|_1$$.
- **Pillar 2 — Conjugate of Quadratic + Conjugate of $$\ell_1$$ Norm:** Minimizing over $$z$$ yields the shifted quadratic $$\frac{1}{2}\|y\|_2^2 - \frac{1}{2}\|y-u\|_2^2$$, while minimizing over $$\beta$$ produces the indicator constraint $$\|X^T u\|_\infty \le \lambda$$.
- **Pillar 3 — Geometric Projection View:** Maximizing $$\frac{1}{2}\|y\|_2^2 - \frac{1}{2}\|y-u\|_2^2$$ over $$\|X^T u\|_\infty \le \lambda$$ is identical to finding the Euclidean projection of $$y$$ onto the dual polytope $$\mathcal{P}_\lambda = \{u : \|X^T u\|_\infty \le \lambda\}$$.
- **Pillar 4 — Primal–Dual Residual Link ($$X\beta^\star = y - u^\star$$):** Stationarity in $$z$$ gives $$u^\star = y - X\beta^\star$$, so the optimal dual vector is literally the Lasso fit's residual vector, and active features correspond to facets of $$\mathcal{P}_\lambda$$ where $$|x_j^T u^\star| = \lambda$$.

### Worked example: Solving a 2-Observation, 1-Feature Lasso via Its Dual

Let $$y = \begin{bmatrix} 3 \\ 1 \end{bmatrix}$$, $$X = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$, and $$\lambda = 2$$.

1. **Write the primal Lasso problem:**
   $$\min_{\beta \in \mathbb{R}} \frac{1}{2}\big((3-\beta)^2 + (1-\beta)^2\big) + 2|\beta|.$$
2. **Write the dual projection problem:** We minimize $$\frac{1}{2}\|y - u\|_2^2$$ subject to $$|X^T u| \le 2$$, i.e., $$-2 \le u_1 + u_2 \le 2$$.
3. **Project $$y = (3, 1)^T$$ onto the slab $$u_1 + u_2 \le 2$$:**
   - Check feasibility of $$y$$: $$3 + 1 = 4 > 2$$, so $$y$$ is outside the slab and projects onto the hyperplane $$u_1 + u_2 = 2$$ along the normal $$X = (1,1)^T$$:
     $$u^\star = y - \frac{X^T y - 2}{\|X\|_2^2} X = \begin{bmatrix} 3 \\ 1 \end{bmatrix} - \frac{4 - 2}{2}\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \end{bmatrix}.$$
4. **Recover the primal fit and $$\beta^\star$$ from $$X\beta^\star = y - u^\star$$:**
   $$X\beta^\star = \begin{bmatrix} 3 \\ 1 \end{bmatrix} - \begin{bmatrix} 2 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \end{bmatrix} \implies \beta^\star = 1.$$
5. **Verify zero duality gap:**
   - Primal objective at $$\beta^\star = 1$$: $$\frac{1}{2}((3-1)^2 + (1-1)^2) + 2|1| = \frac{1}{2}(4) + 2 = 4$$.
   - Dual objective at $$u^\star = (2,0)^T$$: $$\frac{1}{2}\|y\|_2^2 - \frac{1}{2}\|y - u^\star\|_2^2 = \frac{1}{2}(10) - \frac{1}{2}(2) = 5 - 1 = 4$$. Exact match!

Let’s look at the lasso problem for $$y \in \mathbb{R}^n, X \in \mathbb{R}^{n\times p}$$:

> $$ \min_\beta \frac{1}{2} \| y-X\beta \|^2_2 + \lambda\| \beta \|_1$$
> 
> $$f(\beta) = \frac{1}{2} \| y - X\beta \|^2_2 +  \lambda\| \beta \|_1$$
> 
> $$L(\beta) = f(\beta)$$
> 
>  $$ \min_\beta L(\beta) = f^{\star}$$

The dual function of the above is constant (= $$f^*$$). Therefore, we can transform the primal problem as follows:

> $$ \min_{\beta,z} \frac{1}{2} \| y-z \|^2_2 + \lambda \| \beta \|_1 \text{ subject to } z = X\beta$$

The dual function of the transformed problem is:
> $$\begin{align}
> g(u) &= \min_{\beta,z} \frac{1}{2} \| y-z \|^2_2 + \lambda \| \beta \|_1 + u^T(z-X\beta) \\
> &= \frac{1}{2} \| y \|^2_2 - \frac{1}{2} \| y-u \|^2_2 - I_{\{ v : \| v \|_\infty \leq 1 \}}(X^Tu/\lambda) \\
> \end{align}$$
> 

#### [Proof]
> $$\begin{align}
> g(u) &= \min_{\beta,z} \frac{1}{2} \| y-z \|^2_2 + \lambda \| \beta \|_1 + u^T(z-X\beta) \\
> &= \underbrace{ \left( \min_z \frac{1}{2} \| y - z \|^2_2 + u^Tz \right)}_{(1)} + \underbrace{\left( \min_\beta  \lambda \| \beta \|_1 + u^TX\beta \right)}_{(2)} \\
> \end{align}$$
> 
> $$ z^{\star} = y - u$$
> 
> $$\begin{align}
> (1) \cdots \left( \min_z \frac{1}{2} \| y - z \|^2_2 + u^Tz \right)
> &= \frac{1}{2} \| u \|^2_2 + u^T(y - u) \\
> &= -\frac{1}{2} \| y - u \|^2_2 + \frac{1}{2} \| y \|^2_2 \\
> \end{align}$$
> $$\begin{align}
> (2) \cdots \left( \min_\beta  \lambda \| \beta \|_1 + u^TX\beta \right) 
> &= - \lambda \max_\beta \frac{u^Tx}{\lambda} \beta - \| \beta \|_2 \\
> &= - \lambda \left( \| \frac{u^Tx}{\lambda} \|_\infty \leq 1 \right) \\
> &= - \lambda \left( \| u^Tx \|_\infty \leq \lambda \right) \\
> \end{align}$$
> \therefore g(u) = -\frac{1}{2} \| y - u \|^2_2 + \frac{1}{2} \| y \|^2_2 + - \lambda \left( \| u^Tx \|_\infty \leq \lambda \right)
> = \frac{1}{2} \| y \|^2_2 - \frac{1}{2} \| y-u \|^2_2 - I_{\{ v : \| v \|_\infty \leq 1 \}}(X^Tu/\lambda)

Therefore, the lasso dual problem is:

> $$ \max_u \frac{1}{2} ( \| y \|^2_2 - \| y-u \|^2_2 ) \text{ subject to } \| X^Tu \|_\infty \leq \lambda$$

This is equivalent to:

> $$ \min_u \| y-u \|^2_2 \text{ subject to } \| X^Tu \|_\infty \leq \lambda$$

### [Check]
Slater’s condition is satisfied, so strong duality holds.
> $$ \text{strong duality } \implies (\beta^{\star}, z^{\star})$$
> 
> $$ \text{ must minimize  } L( \beta, z, u^{\star} ) \text{ over } -u, \beta, z$$

### [note]
The optimal value in the previous problem is not the optimal lasso objective value.
However, the dual solution $$u$$ and the lasso solution $$\beta$$ satisfy $$X\beta = y-u$$.

This is satisfied by the KKT stationarity condition $$z$$ (i.e., $$z-y + \beta = 0$$).

Therefore, lasso satisfies the dual residual.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter13/Conjugate_LassoDual_Example.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig2] Lasso Dual [1]</figcaption>
</p>
</figure>

### The lasso dual as a projection (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/lasso-dual_en.mp4"></video>
</div>

The dual asks for $$u$$ with $$\|A^Tu\|_\infty\le\lambda$$. The coordinates where this constraint is tight are exactly the nonzeros of the primal solution.

### Try it yourself: lasso primal and dual

<div class="opx-explainer" data-opx="ld" data-lang="en"></div>
