---
layout: post
title: '23-02 Example: linear regression'
chapter: '23'
order: 3
owner: Jinwoo Park
categories:
- chapter23
lang: en
---

Linear regression $$\min_\beta \frac{1}{2}\|y - X\beta\|_2^2$$ is the cleanest laboratory in optimization: every coordinate subproblem is a 1D parabola whose exact minimizer is a single inner product. Comparing full Gradient Descent, Nesterov Accelerated Gradient, and Coordinate Descent on this problem reveals a counterintuitive computational truth: one full cycle of $$p$$ coordinate updates costs $$O(np)$$—the *exact same* floating-point budget as one full gradient step—yet converges dramatically faster because each coordinate immediately benefits from the updated residual and its own local curvature $$\|X_i\|_2^2$$.

## Key ideas: Coordinate Descent Mechanics for Ordinary Least Squares

- **Partial Residual Formulation:** Fixing all coordinates except $$\beta_i$$, the residual splits as $$y - X\beta = r^{(-i)} - X_i \beta_i$$ where $$r^{(-i)} = y - \sum_{j \ne i} X_j \beta_j$$. Minimizing $$\frac{1}{2}\|r^{(-i)} - X_i \beta_i\|_2^2$$ gives the exact projection $$\beta_i^+ = \frac{X_i^\top r^{(-i)}}{\|X_i\|_2^2}$$.
- **Exact $$O(n)$$ Residual Refresh:** Never recompute $$X\beta$$ from scratch inside the inner loop (which would cost $$O(np)$$ per coordinate and $$O(np^2)$$ per cycle). Maintain $$r = y - X\beta$$ and update $$r \leftarrow r - (\beta_i^+ - \beta_i) X_i$$ in $$O(n)$$ operations.
- **Why CD Beats GD Per-Flop:** Gradient descent must use a single global step size $$\eta \le 1 / \lambda_{\max}(X^\top X)$$ dictated by the steepest coupled direction. Coordinate descent implicitly uses diagonal preconditioning $$1 / \|X_i\|_2^2$$ plus immediate Gauss–Seidel feedback.
- **Fair Benchmarking Criterion:** Comparing 1 cycle of CD ($$p$$ coordinate updates) against 1 step of GD or AGD is strictly fair in operation count because both touch every entry of $$X \in \mathbb{R}^{n \times p}$$ exactly once ($$O(np)$$ flops).

### Worked example: One Exact CD Cycle vs. One GD Step on OLS

Let $$X = \begin{pmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix}$$ (so $$X_1 = (1,1,0)^\top$$, $$X_2 = (1,0,1)^\top$$, $$\|X_1\|_2^2 = \|X_2\|_2^2 = 2$$) and $$y = (3, 1, 2)^\top$$. Note that the exact solution is $$\beta^\star = (1, 2)^\top$$ since $$X\beta^\star = (3, 1, 2)^\top = y$$. Start at $$\beta^{(0)} = (0, 0)^\top$$ with residual $$r = y = (3, 1, 2)^\top$$.

1. **Coordinate 1 update:**
   - Partial residual $$r^{(-1)} = r + \beta_1^{(0)} X_1 = (3, 1, 2)^\top$$.
   - $$\beta_1^{(1)} = \frac{X_1^\top r^{(-1)}}{\|X_1\|_2^2} = \frac{1(3) + 1(1) + 0(2)}{2} = \frac{4}{2} = 2$$.
   - Refresh residual: $$r \leftarrow (3, 1, 2)^\top - 2(1, 1, 0)^\top = (1, -1, 2)^\top$$.
2. **Coordinate 2 update (using the refreshed residual!):**
   - Partial residual $$r^{(-2)} = r + \beta_2^{(0)} X_2 = (1, -1, 2)^\top$$.
   - $$\beta_2^{(1)} = \frac{X_2^\top r^{(-2)}}{\|X_2\|_2^2} = \frac{1(1) + 0(-1) + 1(2)}{2} = \frac{3}{2} = 1.5$$.
   - Refresh residual: $$r \leftarrow (1, -1, 2)^\top - 1.5(1, 0, 1)^\top = (-0.5, -1, 0.5)^\top$$.
   - Loss after 1 CD cycle: $$\frac{1}{2}\|r\|_2^2 = \frac{1}{2}(0.25 + 1 + 0.25) = 0.75$$.
3. **Compare with 1 Gradient Descent step:** Here $$X^\top X = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$ has $$L = \lambda_{\max} = 3$$, so the optimal safe GD step is $$\eta = 1/3$$.
   - Gradient at $$0$$: $$-X^\top y = -(4, 5)^\top$$.
   - $$\beta_{\text{GD}}^{(1)} = \frac{1}{3}(4, 5)^\top = (1.333, 1.667)^\top$$, residual $$y - X\beta_{\text{GD}}^{(1)} = (0, -0.333, 0.333)^\top$$, loss $$= 0.111$$.
   Now imagine rescaling column 1 by $$10$$: $$L$$ explodes by $$100\times$$, forcing GD to crawl at $$\eta \approx 1/200$$ along column 2, while CD’s coordinate-wise division by $$\|X_i\|_2^2$$ remains completely unaffected!

Let's define the linear regression problem as follows.

> $$\min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2,$$
> $$\text{given } y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^{n \times p} \text{ with columns } X_1, \dots, X_p.$$

When $$\beta_j,\: j \neq i$$ are fixed values, let's find $$\beta_i$$ that minimizes the given objective function.
($$-i$$ means the remaining terms excluding $$i$$. - In the case of $$X$$, the remaining columns excluding the $$i$$-th column.)

$$\begin{align}
0 &= \nabla_i f(\beta)\\\\
&= X_i^T (X\beta - y)\\\\
&= X_i^T (X_i \beta_i + X_{-i} \beta_{-i} - y)\\\\
\Rightarrow\\\\
&\beta_i = \frac{X_i^T (y - X_{-i} \beta_{-i})}{X_i^T X_i}
\end{align}$$

Through coordinate descent, we iterate and update $$\beta_i$$ for $$i=1,2,\dots,p,1,2,\dots$$.

## Experiment: Convergence speed comparison - GD vs AGD vs CD

The graph below shows the convergence speeds of coordinate descent, gradient descent, and accelerated gradient descent for a linear regression problem with $$n=100, p=20$$. (The k on the horizontal axis represents one step (GD, AGD) or one cycle (CD).)

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/gd_vs_agd_vs_cd.png" alt="[Fig1] GD vs AGD vs CD [3]">
  <figcaption style="text-align: center;">[Fig1] GD vs AGD vs CD [3]</figcaption>
</p>
</figure>
<br/>

According to the above results, coordinate descent shows significantly better convergence speed than AGD, which is optimal among first-order methods. Why can this phenomenon occur? To conclude, coordinate descent can achieve performance that far surpasses AGD because it utilizes more information than first-order methods. This is because coordinate descent uses the latest information updated in the previous step at each step within one cycle. (That is, CD is not a first-order method.)

### Q. Then, is it fair to compare one cycle of CD with one step of GD in the above experiment?

**A. Yes.** The CD update formula introduced earlier can be modified to have a time complexity of $$O(n)$$ per step. Then, the time complexity of one cycle for CD becomes $$O(np)$$, which has the same time complexity as one step of GD.

* **Gradient descent update:** $$\beta \leftarrow \beta + tX^T(y-X\beta)$$, the time complexity of the $$X\beta$$ operation becomes $$O(np)$$ flops.

### Coordinate descent: one coordinate at a time (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/coordinate-descent_en.mp4"></video>
</div>

Coordinate descent minimises exactly along one coordinate at a time, drawing a staircase path; correlated coordinates make the stairs small.

### Try it yourself: coordinate descent vs gradient descent

<div class="opx-explainer" data-opx="cd" data-lang="en"></div>
