---
layout: post
title: 20-02-01 Dual Decomposition with Equality Constraint
chapter: '20'
order: 5
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

Equality constraints $$\sum_{i=1}^B A_i x_i = b$$ are the backbone of network flow conservation, consensus averaging, and power-grid balance: supply must equal demand *exactly*, with no slack allowed. Because the dual variable $$u \in \mathbb{R}^m$$ is unconstrained in sign, dual decomposition with equality constraints runs pure unconstrained dual ascent—letting each block $$i$$ solve its own subproblem $$f_i(x_i) + u^T A_i x_i$$ in parallel while the coordinator nudges $$u$$ proportionally to the exact imbalance $$\sum_i A_i x_i - b$$.

## Key ideas: Equality-Constrained Dual Decomposition

- **Column-Block Partitioning:** Splitting $$x = (x_1, \dots, x_B)$$ and $$A = [A_1, \dots, A_B]$$ rewrites $$Ax = \sum_{i=1}^B A_i x_i$$, exposing the additive structure of $$u^T Ax$$ inside the Lagrangian.
- **Unconstrained Dual Price $$u \in \mathbb{R}^m$$:** Unlike inequality constraints, equality multipliers can be positive (penalizing oversupply) or negative (penalizing undersupply), so no projection step is needed on $$u$$.
- **Exact Residual as Dual Ascent Direction:** Gathering $$A_i x_i^{(k)}$$ from each worker produces $$r^{(k)} = \sum_{i=1}^B A_i x_i^{(k)} - b$$, giving the update $$u^{(k)} = u^{(k-1)} + t_k r^{(k)}$$.
- **Limitation on Non-Strictly Convex Blocks:** If any block $$f_i$$ is linear or piecewise-linear, $$x_i^{(k)}$$ can jump discontinuously between extreme points as $$u$$ crosses a kink, causing persistent oscillation unless ergodic averaging or an augmented Lagrangian is used.

### Worked example: Three-Node Weighted Equality Balance

Minimize $$\frac{1}{2}x_1^2 + x_2^2 + \frac{3}{2}x_3^2$$ subject to $$x_1 + 2x_2 + x_3 = 6$$ (so $$A_1 = 1, A_2 = 2, A_3 = 1, b = 6$$).

1. **Derive the three parallel block updates for any $$u \in \mathbb{R}$$:**
   - Block 1: $$\min \frac{1}{2}x_1^2 + u x_1 \implies x_1(u) = -u$$.
   - Block 2: $$\min x_2^2 + 2u x_2 \implies 2x_2 + 2u = 0 \implies x_2(u) = -u$$.
   - Block 3: $$\min \frac{3}{2}x_3^2 + u x_3 \implies 3x_3 + u = 0 \implies x_3(u) = -\frac{u}{3}$$.
2. **Compute the safe step size using strong convexity:**
   Here $$d = \min(1, 2, 3) = 1$$ and $$\|A\|_2^2 = 1^2 + 2^2 + 1^2 = 6$$, so $$t = \frac{1}{6}$$ is guaranteed safe (exact dual Lipschitz constant is $$1 + 2(1) + \frac{1}{3} = \frac{10}{3}$$, so even $$t = 0.3$$ is exact!).
3. **Trace two iterations from $$u^0 = 0$$ with $$t = 0.25$$:**
   - **Iter 1:** $$x^{(1)} = (0, 0, 0)^T \implies r^{(1)} = 0 - 6 = -6 \implies u^1 = 0 + 0.25(-6) = -1.5$$.
   - **Iter 2:** $$x^{(2)} = (1.5, \; 1.5, \; 0.5)^T \implies A x^{(2)} = 1.5 + 3.0 + 0.5 = 5.0 \implies r^{(2)} = 5.0 - 6 = -1.0$$.
   - $$u^2 = -1.5 + 0.25(-1.0) = -1.75$$ (exact optimum is $$u^\star = -1.8, \; x^\star = (1.8, 1.8, 0.6)^T$$!).
   In just 2 parallel rounds, the equality residual dropped from $$-6.0$$ to $$-1.0$$!

Consider the following problem.
>$$\begin{equation}
>\min_x \sum_{i=1}^B f_i(x_i) \quad \text{ subject to } \quad Ax = b
>\end{equation}$$

Suppose the variable $$x$$ is split into $$B$$ blocks, $$x = (x_1,\dots,x_B) \in \mathbb{R}^n, \text{ where } x_i \in \mathbb{R}^{n_i}$$, and the matrix $$A$$ is likewise split into $$B$$ column blocks, $$A = [A_1, \dots, A_B], \text{ where } A_i \in \mathbb{R}^{m \times n_i}$$. Then, for a fixed $$u$$, the minimization over $$x$$ separates into $$B$$ independent problems:
> $$
> \begin{alignat}{1}
> & \quad x^+ \in \arg\min_x \sum_{i=1}^B f_i(x_i) + u^T Ax  \\
> \Longleftrightarrow & \quad x_i^+ \in \arg\min_{x_i} f_i(x_i) + u^T A_ix_i, \quad i=1,\dots, B
> \end{alignat}
> $$

### Dual decomposition algorithm:

> $$
> \begin{alignat}{1}
> x_i^{(k)} & \in \arg \min_{x_i} f_i(x_i) + (u^{(k-1)})^T A_i x_i, \quad i=1,\dots,B  \\
> u^{(k)}   & = u^{(k-1)} + t_k \left(\sum_{i=1}^B A_i x_i^{(k)} - b \right)
> \end{alignat}
> $$

The two steps above can be read as follows.
* The first equation is the **broadcast** step: the current $$u$$ is sent to each of the $$B$$ processors, and each processor finds its own optimal $$x_i$$ in parallel.
* The second equation is the **gather** step: $$A_i x_i$$ is collected from each processor and the global dual variable $$u$$ is updated.

The two steps are repeated for $$k=1,2,3,\dots$$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter20/decomposition.png" alt="[Fig 1] Broadcast and Gather" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Broadcast and Gather</figcaption>
</p>
</figure>

### Dual decomposition: prices and agents (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/dual-decomposition_en.mp4"></video>
</div>

Each agent solves its own small problem given a price $$\nu$$, and dual ascent raises or lowers $$\nu$$ according to the constraint violation $$\sum_i x_i-c$$.

### Try it yourself: set the price

<div class="opx-explainer" data-opx="dd" data-lang="en"></div>
