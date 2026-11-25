---
layout: post
title: 28-01 Critical points and saddles
chapter: '28'
order: 2
owner: Nguyen Le Linh
categories:
- chapter28
lang: en
lesson_type: required
---

When gradient descent slows to a crawl and $$\|\nabla F(w)\|_2 \approx 0$$, you might assume you have arrived at a valley floor. In high dimensions, that assumption is almost always wrong: you are far more likely perched on a mountain pass—a **saddle point** where the terrain slopes upward along some eigenvectors of the Hessian and downward along others. Classifying critical points cleanly through the Hessian spectrum is the first step toward designing optimizers that refuse to stall on high-dimensional passes.

## Key ideas: Hessian Spectrum and Critical-Point Taxonomy

- **Second-Order Taylor Model:** Near any critical point $$w$$ where $$\nabla F(w) = 0$$, the landscape looks locally quadratic: $$F(w + \Delta) \approx F(w) + \frac{1}{2}\Delta^\top H \Delta$$, where $$H = \nabla^2 F(w)$$ is symmetric with real eigenvalues $$\lambda_1 \le \dots \le \lambda_d$$.
- **Strict Saddles vs. Degenerate Saddles:** A critical point is a *strict saddle* if $$\lambda_{\min}(H) < 0$$—meaning there is a clear quadratic escape direction along the corresponding eigenvector. If $$\lambda_{\min}(H) = 0$$ (degenerate/monkey saddle), second derivatives are inconclusive and higher-order derivatives dictate geometry.
- **Second-Order Necessary & Sufficient Conditions:** Every local minimum satisfies $$\nabla F(w) = 0$$ and $$H \succeq 0$$ (necessary); conversely, $$\nabla F(w) = 0$$ and $$H \succ 0$$ guarantees a strict local minimum (sufficient).
- **The Saddle-to-Minimum Ratio in High Dimensions:** In random Gaussian landscapes (Dauphin et al. 2014), the fraction of critical points that are local minima shrinks like $$2^{-d}$$; nearly every high-loss critical point is a strict saddle with negative curvature waiting to be exploited.

### Worked example: Classifying All Critical Points of a 2D Nonconvex Surface

Consider $$F(x, y) = x^3 - 3x + y^2$$.

1. **Compute the gradient and set $$\nabla F(x, y) = 0$$:**
   $$\nabla F(x, y) = \begin{pmatrix} 3x^2 - 3 \\ 2y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies (x, y) \in \{(1, 0),\ (-1, 0)\}.$$
2. **Compute the Hessian matrix $$H(x, y) = \nabla^2 F(x, y)$$:**
   $$H(x, y) = \begin{pmatrix} 6x & 0 \\ 0 & 2 \end{pmatrix}.$$
3. **Classify both critical points via eigenvalues:**
   - At $$(1, 0)$$: $$H(1, 0) = \operatorname{diag}(6, 2) \succ 0$$ (eigenvalues $$6 > 0, 2 > 0$$) $$\implies$$ **strict local minimum** with $$F(1, 0) = -2$$.
   - At $$(-1, 0)$$: $$H(-1, 0) = \operatorname{diag}(-6, 2)$$ (eigenvalues $$-6 < 0, +2 > 0$$) $$\implies$$ **strict saddle point** with $$F(-1, 0) = +2$$!
4. **Identify the escape direction at $$(-1, 0)$$:** Along eigenvector $$v = (1, 0)^\top$$ (negative eigenvalue $$-6$$), stepping by $$\Delta = (\delta, 0)^\top$$ gives $$F(-1 + \delta, 0) = 2 - 3\delta^2 + \delta^3 < 2$$ for small $$\delta \ne 0$$—proving the saddle drops quadratically along $$x$$ while rising quadratically along $$y$$.

Let $$F:\mathbb{R}^d\to\mathbb{R}$$ be twice continuously differentiable. A point $$w$$ is **critical** if $$\nabla F(w)=0$$. The Hessian $$H=\nabla^2 F(w)$$ then classifies the critical point *when it is nondegenerate* (no zero eigenvalue):

- **Strict local minimum:** $$H\succ 0$$ (all eigenvalues positive).
- **Strict local maximum:** $$H\prec 0$$.
- **Strict saddle:** $$H$$ is indefinite — at least one positive and one negative eigenvalue.

If some eigenvalues vanish, the test is inconclusive (think $$w\mapsto w^3$$ or a plateau). Deep losses are full of near-degenerate directions.

**First-order methods do not see $$H$$**, but the local Taylor story still explains their behavior: along a negative-curvature direction $$u$$, $$F(w+t u)\approx F(w)+\tfrac12 t^2 u^\top H u$$ *decreases* for small $$t\neq 0$$. A saddle is not a trap for an algorithm that can move in that direction; it is a trap for algorithms that only look at $$\|\nabla F\|$$ being small and stop.

In high dimension, if eigenvalues of a “typical” Hessian at a critical point behave like a random symmetric matrix, the probability that *all* of them are positive is exponentially small. The folk theorem you should remember: **most critical points of high-dimensional generic functions are saddles, not minima**. Deep-learning losses are not generic Gaussians — but the intuition is why “getting stuck in local minima” is usually the wrong diagnosis after epoch 2.

### Saddle points in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/saddle-escape_en.mp4"></video>
</div>

GD pulled into the saddle of x² − y² + ½y⁴, sitting long with a tiny offset, escaping with noise, and why most critical points are saddles in high dimensions.

**Exercise.** For $$F(x,y)=x^2-y^2$$ (the hyperbolic paraboloid) write $$\nabla F$$ and $$H$$. Starting at $$(0,10^{-3})$$, take two gradient steps with step size $$\eta = 0.1$$. Starting at $$(0,0)$$, explain why GD with exact arithmetic never leaves.
