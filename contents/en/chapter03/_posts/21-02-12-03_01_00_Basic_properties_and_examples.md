---
layout: post
title: 03-01 Basic properties and examples
chapter: '03'
order: 2
owner: Minjoo Lee
categories:
- chapter03
lang: en
lesson_type: required
---

Not all convex bowls have the same shape: an absolute-value V-shape $$|x|$$ has flat sides and a sharp kink, an exponential $$e^x$$ curves strictly upward everywhere yet flattens out toward $$-\infty$$, and a quadratic $$2x^2 + 3x$$ curves upward with a uniform quadratic cushion everywhere. Section 03-01 distinguishes these exact tiers—convex, strictly convex, and strongly convex—because each tier buys you a stronger uniqueness and convergence guarantee.

## Key ideas: Properties & Tiers of Convex Functions

- **Convexity:** Guarantees every local minimum is global, though the set of global minimizers may contain multiple points (e.g., a flat bottom).
- **Strict Convexity:** Eliminates flat segments so that a global minimizer, if it exists, is strictly **unique**.
- **Strong Convexity ($$m > 0$$):** Bounds curvature uniformly away from zero ($$f(x) - \frac{m}{2}\|x\|_2^2$$ is convex), unlocking linear (geometric) convergence rates for gradient descent.
- **Concavity ($$-f$$ convex):** Flips the bowl upside down—maximizing a concave function (such as log-likelihood or utility) is identical to minimizing the convex function $$-f$$.

### Worked example: Separating Convex, Strictly Convex, and Strongly Convex

Compare three 1D functions on $$\mathbb{R}$$:
1. **$$f_1(x) = |x|$$ (convex, not strictly convex):** For $$x = 1, y = 3$$, $$f_1(2) = 2 = \frac{1}{2}f_1(1) + \frac{1}{2}f_1(3)$$, so the chord coincides with the graph on $$[0, \infty)$$.
2. **$$f_2(x) = e^x$$ (strictly convex, not strongly convex):** $$f_2''(x) = e^x > 0$$ everywhere (strictly convex), but $$\inf_{x \in \mathbb{R}} e^x = 0$$, so no constant $$m > 0$$ satisfies $$f_2''(x) \ge m$$ globally.
3. **$$f_3(x) = 2x^2 + 3x$$ ($$4$$-strongly convex):** $$f_3''(x) = 4 \ge 4$$ for all $$x \in \mathbb{R}$$, meaning $$f_3(x) - \frac{4}{2}x^2 = 3x$$ is affine (hence convex) and gradient descent converges linearly.

This section covers the definition of convex functions, representative types of convex functions, and their key properties.