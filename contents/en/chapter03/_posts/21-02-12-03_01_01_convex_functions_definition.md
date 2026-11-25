---
layout: post
title: 03-01-01 Definition
chapter: '03'
order: 3
owner: Minjoo Lee
categories:
- chapter03
lang: en
---

Why do machine learning practitioners add a tiny $$\ell_2$$ weight-decay term $$\frac{\lambda}{2}\|w\|_2^2$$ to an already convex loss function? Because upgrading a function from *convex* to *strongly convex* transforms both its geometry and its algorithmics: the minimizer becomes unique, the solution becomes stable under data perturbations, and gradient descent accelerates from slow $$O(1/k)$$ convergence to exponential $$O(\rho^k)$$ convergence.

## Key ideas: The Exact Hierarchy of Convexity

- **Domain Convexity Requirement:** A function $$f$$ cannot be convex unless its domain $$\text{dom}\,f$$ is first a convex set—never skip checking $$\text{dom}\,f$$!
- **Convex vs. Strictly Convex:** Replacing $$\le$$ with $$<$$ for all $$x \neq y$$ and $$\theta \in (0, 1)$$ rules out linear segments on the graph and guarantees at most one global minimizer.
- **$$m$$-Strong Convexity:** $$f(x) - \frac{m}{2}\|x\|_2^2$$ is convex (for smooth $$f$$, $$\nabla^2 f(x) \succeq m I$$), placing a uniform quadratic lower envelope under every point of the graph.
- **Strict Inclusion Chain:** $$\text{Strongly Convex} \implies \text{Strictly Convex} \implies \text{Convex}$$, and neither arrow reverses in general.

### Worked example: Why $$x^4$$ Is Strictly Convex but Not Strongly Convex

Compare $$f(x) = x^4$$ and $$g(x) = x^4 + x^2$$ on $$\mathbb{R}$$.

1. **Test $$f(x) = x^4$$:**
   $$f''(x) = 12x^2.$$
   - For all $$x \neq 0$$, $$f''(x) > 0$$, and $$f''$$ vanishes only at the isolated point $$x = 0$$ (no flat interval exists), so $$f$$ is **strictly convex**.
   - However, $$\inf_{x \in \mathbb{R}} f''(x) = f''(0) = 0$$, so there is **no** $$m > 0$$ with $$12x^2 \ge m$$ for all $$x$$. Thus $$f(x) = x^4$$ is **not strongly convex** (it is too flat at the origin!).
2. **Test the regularized function $$g(x) = x^4 + x^2$$:**
   $$g''(x) = 12x^2 + 2 \ge 2 \quad \text{for all } x \in \mathbb{R}.$$
   Adding $$x^2$$ lifts the curvature floor from $$0$$ to $$m = 2$$, making $$g$$ **$$2$$-strongly convex** everywhere.

## Convex function

A function $$f:\mathbb{R}^n \rightarrow \mathbb{R}$$ is convex if its domain is a convex set and for any two points $$x, y \in \text{dom}f$$, the function satisfies:

> $$f(\theta x+(1-\theta)y) \le \theta f(x)+(1-\theta)f(y)$$,
>
> with $$0 \le \theta \le 1$$, for all $$x,y \in \text{dom} f$$

This means that for any two points $$x, y$$, the value of $$f$$ at their convex combination is less than or equal to the convex combination of their function values. Geometrically, the graph of $$f$$ lies below the line segment connecting the points $$(x, f(x))$$ and $$(y, f(y))$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/convex_function2.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Convex Function [2]</figcaption>
</p>
</figure>


## Strictly convex
A function $$f:\mathbb{R}^n \rightarrow \mathbb{R}$$ is strictly convex if for any two distinct points $$x, y \in \text{dom}f$$ and $$0 < \theta < 1$$:

> $$f(\theta x+(1-\theta)y)<\theta f(x)+(1-\theta)f(y)$$,
>
> with $$0<\theta<1$$, $$x \neq y$$, for all $$x, y \in \text{dom}f$$

## Strongly convex
A function $$f$$ is strongly convex if $$f - \frac{m}{2}\| x \|_{2}^{2}$$, with $$m > 0$$, is convex.

### [Note] strongly convex ⇒ strictly convex ⇒ convex

## Concave function
A function $$f$$ is concave if $$-f$$ is convex.

All affine functions $$f(x) = a^T x+b$$ satisfy:
> $$
\begin{aligned}
f(\theta x+(1-\theta)y) &= a^T (\theta x+(1-\theta)y) +b \\
&= \theta a^T x + (1-\theta) a^T y + \theta b + (1-\theta) b \\
&= \theta f(x)+(1-\theta)f(y) \\
\end{aligned} 
$$
> $$\text{for all } x,y \in \text{dom} f, \text{with } 0 \le \theta \le 1$$

That is, affine functions are always convex, and simultaneously concave.

### Four ways to check convexity in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/convexity-tests_en.mp4"></video>
</div>

The chord and Jensen on x² (the 1 and 3 example), the tangent below the graph, second derivatives and the Hessian, epigraph and sublevel sets, contrasted with the W-shaped x⁴ − 3x².
