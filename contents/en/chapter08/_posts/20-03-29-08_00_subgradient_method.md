---
layout: post
title: '08 Subgradient Method'
chapter: '08'
order: 1
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

Picture yourself hiking down a foggy mountain ridge whose terrain is not a smooth granite dome, but a folded landscape of razor-sharp V-shaped valleys and intersecting cliff faces. In smooth calculus, a compass needle pointing opposite the gradient always aims locally downhill; on a sharp crease, however, no single tangent plane exists, and the naive gradient compass breaks down completely. The **subgradient method**—pioneered in the Soviet optimization school by Naum Shor, Boris Polyak, and Arkadi Nemirovski in the 1960s and 1970s—is the minimalist yet remarkably resilient toolkit that lets us navigate these nonsmooth convex landscapes without ever differentiating across a kink.

## Background Knowledge Map: Navigating Nonsmooth Convex Landscapes

- **Pillar 1 — Subgradients & Supporting Hyperplanes:** At a kink where a convex function $$f$$ fails to be differentiable, a subgradient $$g \in \partial f(x)$$ defines a global linear underestimator $$f(y) \ge f(x) + g^\top (y - x)$$. Rather than requiring local smoothness, this single inequality is strong enough to pull iterates closer to the optimal set in Euclidean distance.
- **Pillar 2 — Non-Monotonic Progress & Best-Iterate Tracking:** Unlike gradient descent, a negative subgradient $$-g$$ is not guaranteed to be a descent direction; the objective $$f(x^{(k)})$$ can temporarily increase even for tiny step sizes. Consequently, the method relies on tracking the running best iterate $$f_{\text{best}}^{(k)} = \min_{0 \le i \le k} f(x^{(i)})$$ and measuring progress via distance to $$x^\star$$.
- **Pillar 3 — Step-Size Geometry (Fixed, Diminishing, and Polyak):** Because subgradients do not necessarily vanish as $$x^{(k)} \to x^\star$$ (think of $$|x|$$ whose subgradient has magnitude $$1$$ arbitrarily close to $$0$$), step sizes must either shrink slowly ($$\sum t_k = \infty, \sum t_k^2 < \infty$$) or adapt using known optimal values (Polyak's rule) to prevent perpetual oscillation.
- **Pillar 4 — Complexity Frontier ($$O(1/\varepsilon^2)$$):** Under only convexity and $$G$$-Lipschitz continuity, the subgradient method achieves $$\varepsilon$$-suboptimality in $$O(G^2 R^2 / \varepsilon^2)$$ iterations. This rate is information-theoretically optimal for black-box nonsmooth convex optimization, motivating the structured composite methods (proximal gradient) studied in Chapter 09.

### Step-by-Step Worked Example (Read Slowly): One Subgradient Step Can Increase $$f$$ Yet Shrink Distance to $$x^\star$$

Consider the nonsmooth convex function on $$\mathbb{R}^2$$ given by $$f(x_1, x_2) = |x_1| + 2|x_2|$$, whose unique minimizer is $$x^\star = (0, 0)$$ with $$f^\star = 0$$.

1. **Choose a starting point on a kink:** Let $$x^{(0)} = (1, 0)$$. Here $$f(x^{(0)}) = |1| + 2|0| = 1$$, and the squared distance to the optimum is $$\|x^{(0)} - x^\star\|_2^2 = 1^2 + 0^2 = 1$$.
2. **Compute the subdifferential at $$x^{(0)} = (1, 0)$$:** Since $$x_1 = 1 > 0$$, the first coordinate has unique derivative $$1$$. Since $$x_2 = 0$$, the subdifferential of $$2|x_2|$$ is the interval $$[-2, 2]$$. Hence $$\partial f(1, 0) = \{ (1, v) : v \in [-2, 2] \}$$.
3. **Pick a valid subgradient and take a step:** Select $$g^{(0)} = (1, 2) \in \partial f(1, 0)$$ and step size $$t_1 = 0.25$$. The update yields:
   $$x^{(1)} = (1, 0) - 0.25(1, 2) = (0.75, -0.5).$$
4. **Compare objective value vs. distance to $$x^\star$$:**
   - New objective value: $$f(x^{(1)}) = |0.75| + 2|-0.5| = 0.75 + 1.0 = 1.75 > 1 = f(x^{(0)})$$. The function value *strictly increased*!
   - New squared distance to $$x^\star$$: $$\|x^{(1)} - x^\star\|_2^2 = 0.75^2 + (-0.5)^2 = 0.5625 + 0.25 = 0.8125 < 1 = \|x^{(0)} - x^\star\|_2^2$$.
5. **Key takeaway:** Even though the objective rose from $$1$$ to $$1.75$$, the iterate moved strictly closer to the true minimizer $$x^\star$$ in Euclidean norm—the exact geometric miracle that powers every convergence proof in Chapter 08.

In this section, we will look at the subgradient method, which can be applied to convex functions that may not be differentiable, using the concept of subgradients. We will also explore the convergence properties and rate of the subgradient method with examples.

## Modern applications (2022–2026)

An optional companion lesson places the same (projected, stochastic) subgradient loop in adversarial PGD / RobustBench, Fairlearn rate constraints, and nonsmooth ReLU training. See [08-09 Modern applications of the subgradient method]({% multilang_post_url contents/chapter08/2026-09-16-08_09_modern_applications %}). When the finite-sum objective *is* smooth, the $$O(1/\sqrt{T})$$ noise floor of this chapter’s stochastic method can be removed by SVRG / SAGA — that lesson is [26-05]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %}), next to the SGD track.
