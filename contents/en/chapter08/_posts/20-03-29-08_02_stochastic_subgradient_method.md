---
layout: post
title: '08-02 Stochastic Subgradient Method'
chapter: '08'
order: 11
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

When your objective is a sum over ten million training examples—as in large-scale support vector machines or empirical risk minimization—computing a single full subgradient requires reading the entire dataset before taking even one tiny step. The **stochastic subgradient method** breaks this bottleneck by replacing the full sum of subgradients with a single randomly (or cyclically) sampled component subgradient. You trade a clean deterministic step for a noisy, cheap step—and in massive-scale machine learning, that trade-off is almost always a decisive win.

## Background Knowledge Map: From Deterministic to Stochastic Subgradients

- **Pillar 1 — Finite-Sum Optimization Structure:** Modern statistical learning minimizes $$f(x) = \sum_{i=1}^m f_i(x)$$ (or $$\frac{1}{m}\sum_{i=1}^m f_i(x)$$), where each $$f_i$$ is a convex, possibly nonsmooth loss (such as hinge loss or absolute error) on a single datum.
- **Pillar 2 — Unbiased Stochastic Oracles:** Drawing an index $$i_k \in \{1, \dots, m\}$$ uniformly at random and returning $$g_{i_k} \in \partial f_{i_k}(x)$$ satisfies $$\mathbb{E}[m \, g_{i_k} \mid x] \in \partial f(x)$$. Even though $$g_{i_k}$$ may point far from the full subgradient, its conditional expectation is an exact subgradient of the full objective.
- **Pillar 3 — Cost-Per-Step vs. Variance Trade-off:** Each stochastic iteration is $$m\times$$ cheaper than a batch subgradient step, allowing rapid early progress when iterates are far from $$x^\star$. Near $$x^\star$$, however, gradient noise across components persists even at the exact optimum, requiring diminishing step sizes to converge.
- **Pillar 4 — Cyclic vs. Randomized Sampling:** Practitioners either cycle deterministically through $$i = 1, \dots, m$$ (cyclic/incremental subgradient) or sample randomly (stochastic subgradient). Randomization avoids adversarial ordering effects and yields tighter expected convergence rates in $$m$$.

### Step-by-Step Worked Example (Read Slowly): Comparing Full vs. Stochastic Subgradient on a 2-Term Sum

Minimize $$f(x) = f_1(x) + f_2(x) = |x - 2| + |x + 2|$$ (optimal set is $$x^\star \in [-2, 2]$$ with $$f^\star = 4$$) starting from $$x^{(0)} = 4$$ with step size $$t = 1$$.

1. **Full (batch) subgradient at $$x^{(0)} = 4$$:**
   - $$g_1(4) = +1$$ (from $$|x - 2|$$) and $$g_2(4) = +1$$ (from $$|x + 2|$$).
   - Full subgradient: $$g(4) = 1 + 1 = 2$$ (requires evaluating *both* terms).
   - Batch step: $$x^{(1)}_{\text{batch}} = 4 - 1 \cdot 2 = 2$$, reaching the optimal set immediately at cost $$2$$ evaluations.
2. **Stochastic subgradient at $$x^{(0)} = 4$$:**
   - Sample $$i_1 \in \{1, 2\}$$ uniformly; either way $$g_{i_1}(4) = +1$$ (cost: $$1$$ evaluation).
   - Update: $$x^{(1)}_{\text{stoch}} = 4 - 1 \cdot 1 = 3$$.
3. **Observe what happens inside the optimal set at $$x = 0$$:**
   - Full subgradient: $$g_1(0) + g_2(0) = -1 + 1 = 0$$ (batch method stops completely!).
   - Stochastic subgradient: $$g_1(0) = -1$$ with probability $$1/2$$ and $$g_2(0) = +1$$ with probability $$1/2$$. Notice $$\mathbb{E}[g_{i}(0)] = 0$$ (unbiased!), yet $$\mathbb{E}[\|g_i(0)\|^2] = 1 > 0$$—showing visually why stochastic methods bounce around $$x^\star$$ unless $$t_k \to 0$$.

The stochastic subgradient method is similar to stochastic gradient descent, but replaces the gradient with a subgradient.