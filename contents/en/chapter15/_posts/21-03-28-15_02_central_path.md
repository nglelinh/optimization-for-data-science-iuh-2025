---
layout: post
title: 15-02 Central path
chapter: '15'
order: 6
owner: Minjoo Lee
categories:
- chapter15
lang: en
---

Picture a hiker standing at the exact geographic center of a fenced valley ($$t \to 0^+$$) who slowly turns up the pull of gravity toward the lowest corner ($$t \to \infty$$). The smooth, curving trail they trace through the middle of the valley—never scraping a fence until the very last moment—is the **central path** $$\{x^*(t) : t > 0\}$$.

## Background Knowledge Map: Geometry of the Central Path

- **Pillar 1 — Definition of the Central Path:** For each $$t > 0$$, $$x^*(t) = \arg\min_{Ax=b} \big(tf(x) + \phi(x)\big)$$ is the unique minimizer (under strict convexity of $$tf + \phi$$); varying $$t \in (0, \infty)$$ sweeps out a smooth 1D curve in $$\mathbb{R}^n$$.
- **Pillar 2 — Analytic Center Anchor ($$t \to 0^+$$):** At $$t = 0$$, $$x^*(0)$$ minimizes $$\phi(x)$$ alone—the **analytic center** of the feasible set, maximally balanced away from all constraint walls.
- **Pillar 3 — Geometric Tangency Condition:** At every point $$x^*(t)$$ on the central path (for an LP $$\min c^T x$$), the optimality condition $$t c + \nabla \phi(x^*(t)) = 0$$ means the objective hyperplane $$c^T x = c^T x^*(t)$$ is *tangent* to the barrier level curve $$\phi(x) = \phi(x^*(t))$$.
- **Pillar 4 — Convergence to the Optimal Face ($$t \to \infty$$):** As $$t \to \infty$$, $$x^*(t)$$ converges to the optimal solution $$x^\star$$ (and if the optimum is a non-unique face, it converges specifically to the analytic center of the optimal face!).

### Step-by-Step Worked Example (Read Slowly): Tracing an Exact Closed-Form Central Path on an LP

Consider the 1D LP $$\min x$$ subject to $$0 \le x \le 1$$ (so $$h_1(x) = -x$$, $$h_2(x) = x - 1$$, true optimum $$x^\star = 0$$).

1. **Write the central-path optimality equation $$\frac{d}{dx}\big(tx - \log x - \log(1-x)\big) = 0$$:**
   $$t - \frac{1}{x} + \frac{1}{1-x} = 0 \implies t x(1-x) - (1-x) + x = 0 \implies t x^2 - (t + 2)x + 1 = 0.$$
2. **Solve the quadratic formula (selecting the root in $$(0, 1)$$):**
   $$x^*(t) = \frac{(t + 2) - \sqrt{(t + 2)^2 - 4t}}{2t} = \frac{t + 2 - \sqrt{t^2 + 4}}{2t}.$$
3. **Check both endpoints of the central path:**
   - **As $$t \to 0^+$$:** $$\sqrt{t^2 + 4} \approx 2 + \frac{t^2}{4}$$, so $$x^*(t) \approx \frac{t}{2t} = 0.5$$—the exact analytic center of $$[0, 1]$$!
   - **At $$t = 2$$:** $$x^*(2) = \frac{4 - \sqrt{8}}{4} = 1 - \frac{\sqrt{2}}{2} \approx 0.293$$.
   - **As $$t \to \infty$$:** $$\sqrt{t^2 + 4} \approx t + \frac{2}{t}$$, so $$x^*(t) \approx \frac{2}{2t} = \frac{1}{t} \to 0 = x^\star$$!

If we denote the solution to the following barrier problem ($$t > 0$$) as $$x^*(t)$$, then the **central path** is the set $$\{x^*(t) | t > 0 \}$$.

>$$\begin{align}
> &\min_{x} \ &&  tf(x) + \phi(x) \\
> &\text{subject to } \ && Ax = b \\
> \end{align}$$

Given suitable conditions, the **central path** set forms a smooth path in $$\mathbb{R}^n$$, and as $$t \to \infty$$, $$x^*(t) \to x^*$$, where $$x^*$$ is the solution to the original problem.

The **central path** is a set of solutions obtained by gradually redefining the problem for new values of $$t$$, moving from the interior toward the boundary when it is difficult to find the optimal solution at the boundary directly.

## Example: central path for an LP
Let's find the central path for the following LP problem.
>$$\begin{align*}
>&\min_{x} \ && c^Tx \\
>&\text{subject to } \ && a_i^Tx \le b_i, \quad i = 1, \cdots , 6 \\
>\end{align*}$$

In the following figure, the dotted line represents the logarithmic barrier function $$\phi$$. <br>

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_central_path_02.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig 1] Central path [1]</figcaption>
</p>
</figure>

You can see that as $$t \to \infty$$, the central path converges to the optimal $$x^*$$. At this point, the hyperplane $$c^Tx = c^Tx(t)$$ is the tangent to the level curve of $$\phi$$ passing through $$c^Tx(t)$$.

### The central path to the optimal vertex (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/central-path_en.mp4"></video>
</div>

As $$t$$ grows, the solution $$x^*(t)$$ of the barrier problem slides along the central path to the optimal vertex.

### Try it yourself: slide along the central path

<div class="opx-explainer" data-opx="barrier" data-lang="en"></div>
