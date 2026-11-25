---
layout: post
title: '08-02-04 Batch vs Stochastic Methods'
chapter: '08'
order: 15
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

If you plot the objective value of batch versus stochastic subgradient on a real logistic regression problem, you immediately see a classic crossing-curves story: in the first few passes over the data, the stochastic curve plummets while the batch curve barely budges; later on, the stochastic curve flattens into a noisy jitter floor while the batch curve steadily grinds past it to higher accuracy. Understanding *why* those two curves cross is the key to choosing the right method—and to designing hybrid schedules like mini-batching or increasing batch sizes.

## Key ideas: The Two Regimes of Batch vs. Stochastic Optimization

- **Pillar 1 — Early Transient Regime (Signal Dominates Noise):** Far from $$x^\star$$, almost all data points agree on the rough direction toward the optimum. Paying $$m$$ evaluations to average $$m$$ nearly identical subgradients is wasteful; taking $$m$$ cheap stochastic steps makes dramatically faster progress per pass over the data.
- **Pillar 2 — Asymptotic Accuracy Regime (Noise Dominates Signal):** Near $$x^\star$$, individual component subgradients cancel each other out ($$\sum g_i \approx 0$$) while each individual $$\|g_i\|$$ remains large. Batch averaging eliminates this variance cleanly, whereas a stochastic method must shrink $$t_k \to 0$$ to suppress it, slowing convergence.
- **Pillar 3 — Mini-Batching as a Continuous Dial:** Averaging $$b$$ sampled subgradients ($$1 \le b \le m$$) reduces step variance by a factor of $$b$$ while keeping iteration cost $$m/b$$ times smaller than full batch—and maps cleanly onto vectorized GPU/SIMD hardware.
- **Pillar 4 — Practical Hybrid Strategy:** Start with small batches (or pure stochastic steps) to burn through the initial distance $$R$$ in a handful of epochs, then increase batch size or anneal the step size once the objective enters the noise floor.

### Worked example: Computing the Exact Crossover Point Between Batch and Stochastic Progress

Suppose we minimize $$\frac{1}{m}\sum_{i=1}^m f_i(x)$$ with $$m = 1{,}000$$ samples, $$R = 10$$, $$G = 1$$, and measure computational cost in **epochs** (1 epoch = $$1{,}000$$ component subgradient evaluations).

1. **Batch subgradient cost for accuracy $$\varepsilon$$:**
   - Each batch iteration costs $$1$$ full epoch.
   - Using the standard bound $$\varepsilon \approx \frac{RG}{\sqrt{K_{\text{batch}}}}$$, reaching $$\varepsilon = 0.5$$ requires:
     $$K_{\text{batch}} = \left(\frac{10 \cdot 1}{0.5}\right)^2 = 400 \text{ epochs}.$$
2. **Stochastic subgradient cost for the same accuracy $$\varepsilon = 0.5$$:**
   - Each epoch performs $$m = 1{,}000$$ updates, so $$E$$ epochs correspond to $$K_{\text{stoch}} = 1{,}000 E$$ updates.
   - Using the normalized randomized bound $$\varepsilon \approx \frac{RG}{\sqrt{K_{\text{stoch}}}}$$, reaching $$\varepsilon = 0.5$$ requires:
     $$K_{\text{stoch}} = 400 \text{ updates} = \frac{400}{1{,}000} = 0.4 \text{ epochs}!$$
3. **Now compare at high precision when the smooth/batch method exploits extra structure (or variance reduction) vs. fixed-step stochastic:**
   - If the stochastic step size is kept fixed at $$t = 0.05$$ (noise floor $$\approx G^2 t / 2 = 0.025$$), then for $$\varepsilon = 0.5$$ stochastic wins by $$1{,}000\times$$ in epochs, whereas for $$\varepsilon = 0.001$$ the fixed-step stochastic method *never* reaches the target while batch (or diminishing-step) keeps descending. This exact tension motivates variance-reduced and adaptive batch-size methods in modern ML.

The convergence properties of batch and stochastic methods are as follows:

Generally, the stochastic method quickly approaches the optimal point in the early stages, but may not converge as well near the optimal point. In contrast, the batch method converges more slowly but approaches the optimal point more accurately.

The figure below compares the convergence of batch and stochastic methods for [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression) (without regularization):

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter08/08_02_stochastic_vs_batch.png" alt="stochastic_vs_batch" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">[Fig 3] Batch vs Stochastic Gradient Descent [2]</figcaption>
</figure>

When each $$f_i$$ is smooth, the leftover jitter of the stochastic curve near the optimum is exactly the noise floor that [26-05 SVRG and SAGA]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %}) removes — without paying a full-batch gradient at every step.
