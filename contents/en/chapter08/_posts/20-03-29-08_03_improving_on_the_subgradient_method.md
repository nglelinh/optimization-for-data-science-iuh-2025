---
layout: post
title: '08-03 Improving on the Subgradient Method'
chapter: '08'
order: 16
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

At first glance, the $$O(1/\varepsilon^2)$$ convergence rate of the subgradient method sounds like bad news: needing one million iterations for three digits of accuracy feels painfully slow compared to the $$O(1/\varepsilon)$$ rate of smooth gradient descent (and $$O(1/\sqrt{\varepsilon})$$ with Nesterov acceleration). Yet Nemirovski and Yudin proved that *no* general black-box subgradient method can beat $$O(1/\varepsilon^2)$$! So how do we break the barrier? Not by inventing a cleverer black-box step size, but by **opening the black box**—separating the smooth, differentiable physics of the problem from its simple nonsmooth geometry.

## Background Knowledge Map: Breaking the $$O(1/\varepsilon^2)$$ Barrier

- **Pillar 1 — The Black-Box Lower Bound:** Treating $$f(x)$$ as an opaque oracle that only returns $$(f(x), g)$$ forces a worst-case rate of $$\Omega(1/\varepsilon^2)$$. Speedups are mathematically impossible unless the algorithm exploits additional structure in $$f$$.
- **Pillar 2 — Composite Splitting ($$f = g + h$$):** Almost every nonsmooth problem in statistics and machine learning—Lasso, elastic net, nuclear-norm matrix completion, constrained regression—splits naturally into a smooth $$L$$-Lipschitz-gradient loss $$g(x)$$ plus a simple nonsmooth regularizer or indicator $$h(x)$$.
- **Pillar 3 — Proximal Gradient Descent (Chapter 09 Preview):** Instead of linearizing the nonsmooth part $$h$$ with a subgradient, proximal gradient linearizes *only* $$g$$ and solves the exact regularized subproblem $$\operatorname{prox}_{t h}(x - t \nabla g(x))$$, immediately recovering the smooth $$O(1/\varepsilon)$$ rate!
- **Pillar 4 — Smoothing & Mirror/Bundle Alternatives:** When $$h$$ lacks a cheap proximal operator, alternative escape routes include Nesterov smoothing (approximating a max-function by log-sum-exp to achieve $$O(1/\varepsilon)$$) and cutting-plane / bundle methods (storing past subgradients to build a piecewise-linear lower model of $$f$$).

### Step-by-Step Worked Example (Read Slowly): Iteration-Count Comparison Across Three Speed Limits

Suppose a convex problem has scale constants normalized to $$1$$, and we want suboptimality $$\varepsilon = 10^{-4}$$ (four digits of accuracy).

1. **Black-box subgradient method ($$O(1/\varepsilon^2)$$):**
   $$K_{\text{subgrad}} \approx \frac{1}{(10^{-4})^2} = 10^8 = 100{,}000{,}000 \text{ iterations}.$$
2. **Proximal gradient descent on $$g + h$$ ($$O(1/\varepsilon)$$):**
   $$K_{\text{prox}} \approx \frac{1}{10^{-4}} = 10^4 = 10{,}000 \text{ iterations}$$
   —a **$$10{,}000\times$$ speedup** purely from handling $$h$$ via its proximal operator instead of a subgradient!
3. **Accelerated proximal gradient / FISTA ($$O(1/\sqrt{\varepsilon})$$):**
   $$K_{\text{FISTA}} \approx \frac{1}{\sqrt{10^{-4}}} = 10^2 = 100 \text{ iterations}$$
   —a **$$1{,}000{,}000\times$$ speedup** over plain subgradient!
4. **Takeaway:** This six-order-of-magnitude gap explains the entire arc from Chapter 08 to Chapter 09: use subgradient methods when $$f$$ is genuinely unstructured or you only need coarse accuracy ($$\varepsilon \sim 10^{-2}$$), and switch to proximal/accelerated methods the moment $$f$$ splits into $$g + h$$.

The subgradient method is advantageous because it can be used for nondifferentiable convex functions, making it more general. However, its convergence rate is $$O(1/\epsilon^{2})$$, which is much slower than the convergence rate of gradient descent, $$O(1/\epsilon)$$.

Is there a way to combine the strengths of gradient descent and the subgradient method? In the next section, we will learn about the proximal gradient descent method, which combines the advantages of both algorithms.