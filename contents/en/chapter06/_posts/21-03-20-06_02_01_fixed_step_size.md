---
layout: post
title: 06-02-01 Fixed step size
chapter: '06'
order: 6
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

Fixed step-size gradient descent—setting $$t_k = t$$ once and never touching it again—is the simplest possible optimizer. Yet that single number $$t$$ walks a razor's edge: nudge it slightly too high and your iterates explode exponentially; set it too low and you watch the loss crawl at a snail's pace. This lesson pins down the exact mathematical boundary between convergence, oscillation, and divergence.

## Key ideas: Stability and Speed of Fixed Step Sizes

1. **The Sufficient-Decrease Guarantee ($$t \le 1/L$$)**: When $$\nabla f$$ is $$L$$-Lipschitz, every step with $$t \le 1/L$$ guarantees $$f(x_{k+1}) \le f(x_k) - \frac{t}{2}\|\nabla f(x_k)\|_2^2$$. Setting $$t = 1/L$$ maximizes this worst-case guaranteed single-step drop.
2. **The Exact Stability Limit ($$t < 2/L$$)**: On a quadratic $$f(x) = \frac{1}{2}x^T Q x$$, the error along the steepest eigenvector scales by $$(1 - tL)$$ per step. For $$1/L < t < 2/L$$, the iterates oscillate across the valley but still decay ($$|1 - tL| < 1$$); at $$t = 2/L$$ they bounce forever; for $$t > 2/L$$ they diverge exponentially.
3. **Why $$t = 1/L$$ Can Still Be Slow**: On ill-conditioned bowls like $$f(x) = \frac{1}{2}(10x_1^2 + x_2^2)$$, the steep coordinate forces $$t \le 0.1$$, so the flat coordinate only shrinks by $$(1 - 0.1) = 0.9$$ per iteration—requiring $$\approx 22$$ steps just to cut the flat error by $$10\times$$.
4. **When Fixed Step Size Is Preferred**: Whenever $$L$$ is cheap to compute (e.g., $$L = \|X\|_2^2$$ in least squares or $$L = \frac{1}{4}\|X\|_2^2$$ in logistic regression), fixed $$t = 1/L$$ eliminates line-search overhead and is easy to parallelize.

### Worked example: Mapping All Four Regimes on $$f(x) = \frac{1}{2}(10x_1^2 + x_2^2)$$

For $$f(x_1, x_2) = \frac{1}{2}(10x_1^2 + x_2^2)$$ starting at $$x^{(0)} = (1, 1)$$, we have $$\nabla f(x) = (10x_1, x_2)$$, so $$L = 10$$ and $$m = 1$$. Watch the first two iterates under four different fixed step sizes:

1. **Too small ($$t = 0.01 \ll 1/L$$)**:
   - $$x^{(1)} = (0.90, 0.99)$$, $$x^{(2)} = (0.81, 0.9801)$$. Completely monotone, but $$x_2$$ barely moves (1% per step).
2. **Standard safe choice ($$t = 1/L = 0.10$$)**:
   - $$x^{(1)} = (0,\; 0.90)$$, $$x^{(2)} = (0,\; 0.81)$$. Exact zero along $$x_1$$ in one step, steady 10% decay along $$x_2$$.
3. **Oscillatory but convergent ($$t = 0.18 \in (1/L, 2/L)$$)** — close to optimal $$t^\star = \frac{2}{11} \approx 0.1818$$:
   - $$x^{(1)} = (1 - 1.8,\; 1 - 0.18) = (-0.80,\; 0.82)$$, $$x^{(2)} = (0.64,\; 0.6724)$$. Despite zig-zagging in $$x_1$$, both coordinates shrink by $$\approx 0.82$$—**nearly twice as fast** as $$t = 0.10$$ along the slow axis!
4. **Divergent ($$t = 0.25 > 2/L = 0.20$$)**:
   - $$x^{(1)} = (-1.50,\; 0.75)$$, $$x^{(2)} = (+2.25,\; 0.5625)$$, $$x^{(3)} = (-3.375,\; 0.4219)$$. Exponential blow-up along $$x_1$$!

The simplest way to choose the step size in gradient descent is to use a fixed value for all iterations: $$t_k = t$$ for $$k = 1, 2, 3, ...$$. However, the convergence and behavior depend heavily on the choice of $$t$$.

For example, in the figure below, gradient descent is applied to $$f(x) = (10 x_1^2 + x_2^2) / 2$$ with different step sizes:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_02_01_gradientdescent4.png" alt="gradientdescent4" width="100%" height="100%">
  <figcaption style="text-align: center;">[Fig 1] Step size scenarios [3]</figcaption>
</p>
</figure>

* In case A, the step size $$t$$ is too large, causing divergence after 8 steps. The minimum cannot be reached.
* In case B, the step size $$t$$ is too small, so convergence is very slow and the minimum is not reached even after 100 steps.
* In case C, the step size is "appropriate," and convergence is achieved in about 40 steps. (How to find this "appropriate" value is discussed later in this chapter.)

### Step size: stable, too large, too small (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/gd-step-sizes_en.mp4"></video>
</div>

On a stretched bowl, a step that is too large zig-zags or diverges, and one that is too small crawls. Backtracking and exact line search pick the step for you.

### Try it yourself: step size

<div class="opx-explainer" data-opx="gd" data-lang="en"></div>
