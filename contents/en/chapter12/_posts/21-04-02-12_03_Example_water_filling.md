---
layout: post
title: 12-03 Example water-filling
chapter: '12'
order: 4
owner: Wontak Ryu
categories:
- chapter12
lang: en
---

Imagine you are a wireless communications engineer with 1 watt of total transmission power to distribute across $$n$$ parallel radio channels, each corrupted by a different background noise level $$\alpha_i > 0$$. By Shannon's capacity theorem, allocating power $$x_i \ge 0$$ to channel $$i$$ yields throughput $$\log(\alpha_i + x_i)$$. Should you dump all power into the cleanest channel, or spread it equally? Applying the KKT conditions produces one of the most iconic physical metaphors in all of engineering: **water-filling**—pour a unit volume of water into a vessel whose floor height in bin $$i$$ is $$\alpha_i$$, and the water depth in each bin *is* the exact optimal power $$x_i^\star$$!

## Key ideas: The KKT Anatomy of Water-Filling

- **Pillar 1 — Convexity & Slater's Condition:** Minimizing $$-\sum_{i=1}^n \log(\alpha_i + x_i)$$ over the simplex $$x \ge 0, \mathbf{1}^\top x = 1$$ is strictly convex (since $$-\log$$ is strictly convex) and satisfies Slater's condition (take $$x_i = 1/n > 0$$), so KKT is both necessary and sufficient for the unique global optimum.
- **Pillar 2 — Stationarity Gives the Water Level $$w = 1/\nu^\star$$:** Differentiating $$L(x, \lambda, \nu) = -\sum \log(\alpha_i + x_i) - \lambda^\top x + \nu(\mathbf{1}^\top x - 1)$$ gives $$-\frac{1}{\alpha_i + x_i^\star} - \lambda_i^\star + \nu^\star = 0 \implies \lambda_i^\star = \nu^\star - \frac{1}{\alpha_i + x_i^\star} \ge 0$$.
- **Pillar 3 — Complementary Slackness Splits Flooded vs. Dry Channels:** From $$\lambda_i^\star x_i^\star = 0$$:
  - If channel $$i$$ receives positive power ($$x_i^\star > 0$$), then $$\lambda_i^\star = 0 \implies \alpha_i + x_i^\star = \frac{1}{\nu^\star}$$ (all active channels share the *same* water surface height $$w = 1/\nu^\star$$!).
  - If channel $$i$$ is too noisy ($$\alpha_i \ge 1/\nu^\star$$), then $$x_i^\star = 0$$ (it stays completely dry!).
- **Pillar 4 — Closed-Form Solution via 1D Root-Finding:** Combining both cases gives $$x_i^\star = \max\!\left(0,\; \frac{1}{\nu^\star} - \alpha_i\right)$$, reducing an $$n$$-dimensional nonlinear optimization problem to finding a single scalar water level $$w = 1/\nu^\star$$ such that $$\sum_{i=1}^n \max(0, w - \alpha_i) = 1$$!

### Worked example: Computing Exact Water-Filling Powers Across 3 Channels

Allocate total power $$\sum_{i=1}^3 x_i = 1$$ across three channels with noise floors $$\alpha_1 = 0.2,\; \alpha_2 = 0.5,\; \alpha_3 = 1.0$$.

1. **Test if all 3 channels are flooded ($$w > \alpha_3 = 1.0$$):**
   - If $$w > 1.0$$, total water volume would be $$(w - 0.2) + (w - 0.5) + (w - 1.0) > 0.8 + 0.5 + 0 = 1.3 > 1.0$$! Too much water—Channel 3 must stay **dry** ($$x_3^\star = 0$$)!
2. **Test if Channels 1 and 2 are flooded ($$0.5 < w \le 1.0$$):**
   - Total water volume: $$(w - 0.2) + (w - 0.5) = 1.0 \implies 2w - 0.7 = 1.0 \implies 2w = 1.7 \implies w^\star = 0.85$$.
   - Check the bracket: $$0.5 < 0.85 \le 1.0$$ (exact fit!).
3. **Read off the optimal powers and KKT multipliers ($$\nu^\star = 1/w^\star = 1/0.85 = 20/17 \approx 1.1765$$):**
   - $$x_1^\star = 0.85 - 0.2 = 0.65$$, $$\lambda_1^\star = 0$$.
   - $$x_2^\star = 0.85 - 0.5 = 0.35$$, $$\lambda_2^\star = 0$$.
   - $$x_3^\star = 0$$, $$\lambda_3^\star = \nu^\star - \frac{1}{1.0} = \frac{20}{17} - 1 = \frac{3}{17} > 0$$.
4. **Verify all KKT conditions:** $$x^\star \ge 0$$, $$0.65 + 0.35 + 0 = 1$$, $$\lambda^\star \ge 0$$, $$\lambda_i^\star x_i^\star = 0$$ for all $$i$$, and $$\alpha_1 + x_1^\star = \alpha_2 + x_2^\star = 0.85$$—confirming exact global optimality!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Suppose we have the following convex optimization problem.

>$$
>\begin{align}
>    &\min_{x} &&{- \sum_{i=1}^n \log(\alpha_i + x_i)} \\\\
>    &\text{subject to} &&{x \succeq 0, 1^Tx = 1},\\\\
>&\text{where } \alpha_i > 0.
>\end{align}
>$$

This problem is about allocating power to n communication channels and arose in information theory. The variable $$x_i$$ represents the output of the transmitter allocated to the i-th channel, and $$\log(\alpha_i + x_i)$$ represents the capacity or communication rate of that channel. That is, this problem is to determine how much power should be allocated to each channel to maximize the total communication rate [1].

Let the Lagrange multipliers for the inequality constraint $$x^\star \succeq 0$$ and equality constraint $$1^Tx^\star = 1$$ be $$\lambda^\star \in \mathbb{R}^n$$ and $$\nu^\star \in \mathbb{R}$$ respectively. The KKT conditions for the given problem are as follows.
>$$
>\begin{align}
>x^\star \succeq 0, \\\\
>1^Tx^\star = 1, \\\\
>\lambda^\star \succeq 0, \\\\
>\lambda_i^\star x_i^\star = 0, \text{    } i = 1, \dots, n, \\\\
> -1 / (\alpha_i + x_i^\star) - \lambda_i^\star + \nu^\star = 0,  \text{    } i= 1, \dots, n.
>\end{align}
> $$

Using the equations obtained from KKT conditions, we can find $$x^\star, \lambda^\star, \nu^\star$$ analytically. First, we eliminate $$\lambda^\star$$ from the equations using it as a slack variable.
>$$
>\begin{align}
>x^\star \succeq 0, \\\\
>1^Tx^\star = 1, \\\\
>x_i^\star(\nu^\star - 1 / (\alpha_i + x_i^\star)) = 0, \text{    } i = 1, \dots, n, \\\\
> \nu^\star \ge 1/(\alpha_i + x_i^\star),  \text{    } i= 1, \dots, n.
>\end{align}
> $$

This is organized as follows by stationarity and complementary slackness.
> $$
> x_i^\star = 
> \begin{cases}
> 1 / \nu^\star - \alpha_i &\nu^\star < 1/\alpha_i \ \\\\
> 0 &\nu^\star \ge 1/\alpha_i\\\\
> \end{cases}
> = \max\{0, 1/\nu^\star - \alpha_i \}, \quad i = 1, \dots, n.
> $$

Also, by the condition $$1^T x^\star = 1$$, $$x_i^\star, i = 1, \dots, n$$ sum to 1.
> $$
> \sum_{i=1}^n \max\{0, 1/\nu^\star - \alpha_i \} = 1.
> $$

The left side of the equation is a piecewise-linear increasing function of $$1/\nu^\star$$, so this equation has a unique solution for fixed $$\alpha_i$$.

This solution method is called water-filling. When $$\alpha_i$$ is the ground level for patch $$i$$, this problem can be thought of as pouring water into each region so that the water level becomes $$1/\nu^\star$$ as shown in the figure below. We pour water until the total amount of water becomes 1.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl}}/img/chapter_img/chapter12/water-fill.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Illustration of water-filling algorithm [1]</figcaption>
</p>
</figure>

### KKT through water-filling in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/kkt-water-filling_en.mp4"></video>
</div>

Solving water-filling with α = (0.1, 0.4, 0.8, 1.2) through the four KKT conditions, reading the meaning of λ, and three wrong guesses that KKT rules out.
