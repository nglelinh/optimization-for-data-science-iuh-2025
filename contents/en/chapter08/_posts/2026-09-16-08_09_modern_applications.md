---
layout: post
title: 08-09 Modern applications of the subgradient method
chapter: '08'
order: 17
owner: Nguyen Le Linh
categories:
- chapter08
lang: en
lesson_type: optional
redirect_from:
  - /contents/en/chapter08/08_11_modern_applications/
---

If you thought the subgradient method was a 1970s relic replaced by Adam and second-order solvers, look inside today's adversarial robustness benchmarks, algorithmic fairness pipelines, and nonsmooth empirical risk trainers: the exact projected stochastic subgradient loop from Chapter 08 is running at their core. Whenever an engineer crafts an $$\ell_\infty$$ adversarial perturbation or enforces a demographic parity constraint on a black-box classifier, the workhorse iteration is still $$x^{(k+1)} = P_C(x^{(k)} - \alpha_k g^{(k)})$$.

## Background Knowledge Map: Why Subgradient Loops Power 2022–2026 ML Pipelines

- **Pillar 1 — Nonsmooth Empirical Risk & Conservative Fields:** Hinge losses, quantile (pinball) losses, and ReLU networks are non-differentiable on sets of measure zero, yet autograd engines (PyTorch/JAX) routinely return a single conservative-field / subgradient element and step along it with stochastic schedules.
- **Pillar 2 — Projected PGD on $$\ell_p$$ Threat Balls:** Adversarial training solves a min-max saddle problem whose inner maximization projects subgradient (or signed-gradient) steps onto an $$\ell_\infty$$ box or $$\ell_2$$ ball—literally projected subgradient ascent on the perturbation $$\delta$$.
- **Pillar 3 — Lagrangian Fairness & Rate Constraints:** Enforcing group-fairness bounds (such as equalized odds in Fairlearn) introduces Lagrange multipliers $$\lambda \ge 0$$ updated via projected exponentiated/subgradient ascent while the learner minimizes the reweighted classification loss.
- **Pillar 4 — Precision Regime Fit:** In adversarial attacks (7–40 PGD steps) and statistical learning (where generalization error dominates optimization error below $$\varepsilon \sim 10^{-2}$$), the $$O(1/\varepsilon^2)$$ rate is not a liability—cheap per-step cost and simple projections are what matter most.

### Step-by-Step Worked Example (Read Slowly): Two Projected Subgradient Steps for an $$\ell_\infty$$ Adversarial Perturbation

Suppose a linear classifier has score $$s(\delta) = w^\top (x_0 + \delta)$$ with $$w = (3, -1)^\top$$, and an adversary wants to maximize $$L(\delta) = |w^\top \delta|$$ (equivalently minimize $$-L(\delta)$$) inside the $$\ell_\infty$$ threat ball $$C = \{ \delta \in \mathbb{R}^2 : \|\delta\|_\infty \le 0.3 \}$$, starting from $$\delta^{(0)} = (0.1, 0.1)^\top$$ with step size $$\alpha = 0.2$$.

1. **Iteration 1 at $$\delta^{(0)} = (0.1, 0.1)^\top$$:**
   - Compute $$w^\top \delta^{(0)} = 3(0.1) - 1(0.1) = 0.2 > 0$$, so $$L(\delta^{(0)}) = 0.2$$.
   - Subgradient of $$L$$ is $$g^{(0)} = \operatorname{sign}(0.2)\, w = (3, -1)^\top$$.
   - Unconstrained ascent step: $$\tilde{\delta}^{(1)} = (0.1, 0.1) + 0.2(3, -1) = (0.7, -0.1)$$.
   - Project onto $$C = [-0.3, 0.3]^2$$ (coordinatewise clip):
     $$\delta^{(1)} = (\operatorname{clip}(0.7, -0.3, 0.3),\; \operatorname{clip}(-0.1, -0.3, 0.3)) = (0.3, -0.1).$$
   - New objective: $$L(\delta^{(1)}) = |3(0.3) - (-0.1)| = 1.0$$.
2. **Iteration 2 at $$\delta^{(1)} = (0.3, -0.1)^\top$$:**
   - Since $$w^\top \delta^{(1)} = 1.0 > 0$$, $$g^{(1)} = (3, -1)^\top$$.
   - Unconstrained ascent step: $$\tilde{\delta}^{(2)} = (0.3, -0.1) + 0.2(3, -1) = (0.9, -0.3)$$.
   - Project onto $$[-0.3, 0.3]^2$$: $$\delta^{(2)} = (0.3, -0.3)$$, achieving $$L(\delta^{(2)}) = |0.9 + 0.3| = 1.2$$—the exact maximum over the $$\ell_\infty$$ ball!

# Modern applications of the subgradient method

Chapter 08 analyses the iteration $$x^{k+1}=x^k-\alpha_k g^k$$ with $$g^k\in\partial f(x^k)$$, its projected cousin, and the stochastic variant. This optional lesson maps those three templates onto pipelines that were standard or newly standardised between about 2022 and 2026. We do not re-prove the $$O(1/\varepsilon^2)$$ rate; we show why a practitioner still runs a (projected, stochastic) subgradient step.

## 1. Nonsmooth empirical risk: hinge, Huber, and ReLU training

Regularised logistic regression in [08-01-05]({% multilang_post_url contents/chapter08/20-03-29-08_01_05_example_regularized_logistic_regression %}) is already a subgradient-method example. The same loop trains a linear SVM (hinge), a robust regressor (Huber / quantile), or the last layer of a frozen encoder. For a full ReLU net the loss is no longer convex, but the *implemented* backward pass is still a conservative selection of a subgradient (Bolte and Pauwels, 2021). Their convergence-in-values result is precisely a justification of **stochastic subgradient descent as libraries run it**, not of an idealised Clarke-critical-point oracle.

On convex finite-sum problems the picture is kinder: diminishing or Polyak steps from this chapter remain the textbook guarantee, and 2022–2024 work on adaptive / parameter-free steps (DoG, Polyak restarts) is a direct descendant of [08-01-06 Polyak step sizes]({% multilang_post_url contents/chapter08/20-03-29-08_01_06_polyak_step_sizes %}).

## 2. Projected PGD and adversarial $$\ell_p$$ training

Madry-style adversarial training solves, at each minibatch, a constrained inner problem

$$
\max_{\|\delta\|_p\le\varepsilon}\ \ell\bigl(h_w(x+\delta),y\bigr)
$$

by **projected gradient / subgradient ascent** on $$\delta$$ and a descent step on $$w$$. The projection onto the $$\ell_\infty$$ or $$\ell_2$$ ball is the operator in [08-01-08 Projected subgradient]({% multilang_post_url contents/chapter08/20-03-29-08_01_08_projected_subgradient_method %}). Croce and Hein (2020) showed that a poorly tuned inner PGD *overestimates* robustness; their parameter-free ensemble **AutoAttack** (APGD + FAB + Square) became the default test. Croce et al. (2021) packaged that test as **RobustBench**, which is still the public leaderboard for $$\ell_\infty$$ and $$\ell_2$$ robustness through 2025. The dual-norm story (the support function of the attack ball) is Chapter 13; the *algorithm* is this chapter’s projected method.

## 3. Fairness and other rate constraints

Many production constraints are **nonsmooth rates**: demographic parity, equalised odds, recall floors, churn caps. They look like $$\mathbb{P}(\hat y=1\mid A=a)\le \alpha$$ — indicator averages, hence piecewise constant. Cotter, Jiang, Gupta, and co-authors (JMLR 2019) introduced a **proxy-Lagrangian** two-player game: one player takes gradient steps on a smooth surrogate, the other enforces the original rate by a (sub)gradient method on multipliers. Agarwal, Beygelzimer, Dudík, Langford, and Wallach (2018) reduce fair classification to a sequence of cost-sensitive problems; the **Fairlearn** library (Weerts, Dudík, Edgar, Jalali, Lutz, and Madaio, 2023, *JMLR*) ships that reduction as `ExponentiatedGradient` and is what a 2024–2026 sklearn stack actually calls.

The inner weighted ERM is often solved by a subgradient or SGD step on a hinge or logistic loss. The outer multiplier update is a subgradient step on a constraint residual. That is the algorithm of this chapter, twice.

## 4. Mini-example: projected step on an $$\ell_\infty$$ ball

```python
import numpy as np

def proj_linf(delta, eps):
    return np.clip(delta, -eps, eps)

def pgd_inner(x, g, eps, alpha=0.01, steps=10):
    delta = np.zeros_like(x)
    for _ in range(steps):
        delta = proj_linf(delta + alpha * g(x + delta), eps)
    return delta
```

Replace `g` by a minibatch gradient of the loss and you have the inner loop of adversarial training. Replace the ball by a probability simplex or a fairness polytope and you have the projected method of Section 08-01-08.

## What to remember

If the objective or the constraint is a max, an $$\ell_1$$, a hinge, or an empirical rate, first-order training *is* a subgradient method (possibly projected, possibly stochastic). Acceleration and prox maps (Chapter 09) are upgrades you earn after the composite structure is visible; they do not replace this loop on a raw rate constraint.

**Question.** Why is a constant step size theoretically uncomfortable for a nonsmooth convex rate constraint, and why do fairness reductions still use one in practice?

## Sources

- Bolte, J., & Pauwels, E. (2021). Conservative set valued fields, automatic differentiation, stochastic gradient methods and deep learning. *Mathematical Programming*, 188, 19–51.
- Croce, F., & Hein, M. (2020). Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks. *ICML*, PMLR 119.
- Croce, F., Andriushchenko, M., Sehwag, V., Debenedetti, E., Flammarion, N., Chiang, M., Mittal, P., & Hein, M. (2021). RobustBench: A standardized adversarial robustness benchmark. *NeurIPS Datasets and Benchmarks*. Leaderboard: [robustbench.github.io](https://robustbench.github.io/)
- Cotter, A., Jiang, H., Gupta, M., Wang, S., Narayan, T., You, S., & Sridharan, K. (2019). Optimization with non-differentiable constraints with applications to fairness, recall, churn, and other goals. *JMLR*, 20(172).
- Agarwal, A., Beygelzimer, A., Dudík, M., Langford, J., & Wallach, H. (2018). A reductions approach to fair classification. *ICML*, PMLR 80.
- Weerts, H., Dudík, M., Edgar, R., Jalali, A., Lutz, R., & Madaio, M. (2023). Fairlearn: Assessing and improving fairness of AI systems. *JMLR*, 24(257). [https://fairlearn.org](https://fairlearn.org)
