---
layout: post
title: Proximal gradient descent and acceleration
chapter: '09'
order: 1
owner: Kyeongmin Woo
categories:
- chapter09
lang: en
---

In Chapter 08, we hit a seemingly immovable speed limit: black-box subgradient methods need $$O(1/\varepsilon^2)$$ iterations to reach accuracy $$\varepsilon$$. Yet almost every nonsmooth problem in statistics, signal processing, and imaging—Lasso, nuclear-norm matrix completion, constrained least squares—is not an opaque black box at all. It is a **composite** sum $$f(x) = g(x) + h(x)$$ of a smooth loss $$g$$ and a simple structured regularizer $$h$$. Chapter 09 shows how splitting those two pieces apart restores the smooth $$O(1/\varepsilon)$$ rate via **proximal gradient descent**, and then launches all the way to the optimal $$O(1/\sqrt{\varepsilon})$$ first-order rate via **Nesterov / FISTA acceleration**.

## Key ideas: The Composite Optimization Architecture

- **Pillar 1 — Composite Splitting ($$f = g + h$$):** Instead of throwing away the smoothness of $$g$$ just because $$h$$ has kinks, we approximate *only* $$g$$ by its local quadratic majorizer while keeping $$h$$ completely exact inside every iteration.
- **Pillar 2 — The Proximal Operator ($$\operatorname{prox}_{t h}$$):** Defined as $$\operatorname{prox}_{t h}(y) = \arg\min_z \left\{\frac{1}{2t}\|z - y\|_2^2 + h(z)\right\}$$, the prox map acts as a generalized projection: it balances staying close to the gradient-descent proposal $$y = x - t\nabla g(x)$$ against minimizing $$h(z)$$, often in closed form (e.g., soft-thresholding for $$\ell_1$$).
- **Pillar 3 — Generalized Gradient & $$O(1/\varepsilon)$$ Recovery:** Defining the generalized gradient $$G_t(x) = \frac{1}{t}(x - \operatorname{prox}_{t h}(x - t\nabla g(x)))$$ turns the proximal step into $$x^+ = x - t G_t(x)$$, unifying ordinary gradient descent, projected gradient descent, and ISTA under one $$O(1/\varepsilon)$$ convergence proof.
- **Pillar 4 — Nesterov Momentum & FISTA ($$O(1/\sqrt{\varepsilon})$$):** Adding an extrapolated look-ahead point $$v^{(k)} = x^{(k-1)} + \frac{k-2}{k+1}(x^{(k-1)} - x^{(k-2)})$$ before applying the proximal gradient step accelerates the rate from $$O(1/k)$$ to $$O(1/k^2)$$ at practically zero extra per-iteration cost.

### Worked example: Seeing Why Splitting $$g + h$$ Beats a Raw Subgradient Step

Consider the 1D composite problem $$f(x) = g(x) + h(x) = \frac{1}{2}(x - 1)^2 + 2|x|$$ ($$L = 1$$ for $$\nabla g(x) = x - 1$$). Since $$0 \in (0 - 1) + 2[-1, 1] = [-3, 1]$$, the exact minimizer is $$x^\star = 0$$. Start at $$x^{(0)} = 0.5$$ with step size $$t = 1/L = 1$$.

1. **Gradient step on the smooth part $$g(x) = \frac{1}{2}(x - 1)^2$$:**
   - $$\nabla g(0.5) = 0.5 - 1 = -0.5$$.
   - Intermediate point: $$y = x^{(0)} - t \nabla g(x^{(0)}) = 0.5 - 1(-0.5) = 1.0$$.
2. **Proximal step on the nonsmooth part $$h(x) = 2|x|$$ (soft-thresholding with threshold $$t\lambda = 1 \cdot 2 = 2$$):**
   $$x^{(1)} = S_{2}(1.0) = \operatorname{sign}(1.0)\max(|1.0| - 2,\; 0) = 0.$$
3. **Compare with a raw subgradient step from $$x^{(0)} = 0.5$$:**
   - Full subgradient at $$0.5$$ is $$(0.5 - 1) + 2 = +1.5$$.
   - With $$t = 1$$, a raw subgradient step lands at $$0.5 - 1.5 = -1.0$$ (overshooting $$0$$ completely and *increasing* $$f$$ from $$1.125$$ to $$4.0$$!).
   - Proximal gradient snapped directly to the exact sparse solution $$x^\star = 0$$ in **one iteration**.

# Proximal gradient descent and acceleration

This chapter introduces proximal gradient descent and acceleration techniques for optimization problems involving composite functions.

## Overview
- Proximal gradient descent is used for problems where the objective can be split into a differentiable part and a non-differentiable part.
- Acceleration methods, such as Nesterov's acceleration and FISTA, can improve convergence rates.

## Structure
- Section 1: Proximal gradient descent
- Section 2: Convergence analysis
- Section 3: Matrix completion example
- Section 4: Special cases
- Section 5: Acceleration methods — start at the Distill-style picture in [09-05]({% multilang_post_url contents/chapter09/20-01-08-09_05_acceleration %}), then the FISTA algebra in 09-05-01; the stochastic / constant-$$\beta$$ cousin is [26-02]({% multilang_post_url contents/chapter26/2026-09-15-26_02_momentum_and_nesterov %})

Refer to each section for details and mathematical formulations.

## Modern applications (2022–2026)

An optional companion lesson follows the same proximal-gradient / FISTA template into PnP imaging, FISTA-Net / pFISTA-DR unrolling, and production elastic-net paths. See [09-06 Modern applications of proximal GD and acceleration]({% multilang_post_url contents/chapter09/2026-09-16-09_06_modern_applications %}).
