---
layout: post
title: 26 Stochastic and adaptive methods for ML
chapter: '26'
order: 1
owner: Nguyen Le Linh
categories:
- chapter26
lang: en
lesson_type: required
---

Imagine training a modern language model on a trillion tokens using classical full-batch gradient descent: before taking even a *single* parameter update, you would have to run a forward and backward pass across the entire internet. Modern machine learning lives in a completely different regime—one where gradients are noisy estimates computed on tiny minibatches, curvature varies by six orders of magnitude across layers, and wall-clock time is bounded by GPU memory bandwidth rather than iteration count. Chapter 26 builds the complete optimization stack of modern ML from first principles: from SGD and momentum, through AdaGrad and AdamW, to variance-reduced finite-sum solvers and 2024–2026 optimizers like SAM, Sophia, and Muon.

## Key ideas: The Modern Stochastic & Adaptive Optimization Stack

- **Finite-Sum Structure & Minibatch Noise:** Empirical risk $$F(w) = \frac{1}{n}\sum_{i=1}^n f_i(w)$$ turns exact gradients into $$O(n)$$ bottlenecks. Minibatching replaces exactness with an unbiased stochastic gradient whose variance scales as $$\sigma^2 / B$$, trading asymptotic precision for massive throughput.
- **Inertia & Acceleration (Momentum / Nesterov):** Exponentially averaging past gradients damps oscillations across high-curvature ravines while amplifying consistent motion along flat valleys, reducing condition-number dependence from $$\kappa$$ to $$\sqrt{\kappa}$$ on quadratics.
- **Diagonal Adaptive Preconditioning (AdaGrad → AdamW):** Rescaling each coordinate by the inverse square root of accumulated squared gradients equalizes learning speeds across sparse tokens and dense hidden layers, while decoupling weight decay (AdamW) prevents adaptive rescaling from distorting regularization.
- **Variance Reduction (SVRG / SAGA) & Second-Order / Matrix Preconditioning:** For finite-sum convex problems, control variates kill the noise floor to recover linear convergence; in deep learning, sharpness-aware updates (SAM), diagonal Hessians (Sophia), and orthogonalized matrix steps (Muon) push beyond diagonal AdamW.

### Worked example: Why 10 Noisy Steps Beat 1 Exact Step

Suppose $$F(w) = \frac{1}{4}\sum_{i=1}^4 f_i(w)$$ where $$f_i(w) = \frac{1}{2}(w - y_i)^2$$ with data $$y = (2, 4, 6, 8)$$. The exact minimizer is $$w^\star = \bar{y} = 5$$, and the full gradient is $$F'(w) = w - 5$$. Start at $$w_0 = 0$$ with step size $$\eta = 0.2$$.

1. **One full-batch GD step (costs 4 gradient evaluations):**
   - Full gradient: $$F'(0) = 0 - 5 = -5$$.
   - Update: $$w_1^{\text{GD}} = 0 - 0.2(-5) = 1.0$$. Remaining distance to optimum: $$|1.0 - 5| = 4.0$$.
2. **Four single-example SGD steps (exact same budget: 4 gradient evaluations!):** Walk through the shuffled pass $$(y_1, y_2, y_3, y_4) = (2, 8, 4, 6)$$ with $$\eta = 0.2$$:
   - Step 1 ($$y = 2$$): $$w_1 = 0 - 0.2(0 - 2) = 0.4$$.
   - Step 2 ($$y = 8$$): $$w_2 = 0.4 - 0.2(0.4 - 8) = 0.4 + 1.52 = 1.92$$.
   - Step 3 ($$y = 4$$): $$w_3 = 1.92 - 0.2(1.92 - 4) = 1.92 + 0.416 = 2.336$$.
   - Step 4 ($$y = 6$$): $$w_4 = 2.336 - 0.2(2.336 - 6) = 2.336 + 0.7328 = 3.0688$$!
3. **Compare progress per gradient evaluation:** For the *exact same* 4 sample evaluations, full-batch GD reached $$w = 1.0$$ (error $$4.0$$), whereas 1 epoch of SGD already reached $$w = 3.0688$$ (error $$1.9312$$)—cutting the distance to $$w^\star$$ more than twice as fast!

# Stochastic and adaptive methods for ML

Chapters 06–09 treated **full-batch** first-order methods: one gradient (or proximal step) that sees every training pair. Modern machine learning almost never does that. This chapter is the 2026 default stack for empirical risk minimization

$$
\min_w F(w) = \frac{1}{n}\sum_{i=1}^n f_i(w), \qquad f_i(w) = \ell\bigl(h_w(x_i), y_i\bigr).
$$

You already met a cousin in [06-05 Stochastic gradient descent]({% multilang_post_url contents/chapter06/21-03-20-06_05_stochastic_gradient_descent %}) and the stochastic subgradient notes in Chapter 08. Here we treat SGD and minibatches as *the* algorithm, then add the two ingredients every deep-learning library ships: **momentum / Nesterov** and **diagonal adaptive scaling** (AdaGrad → RMSProp intuition → Adam → AdamW). A last required lesson develops variance reduction (SVRG / SAGA) so you know when the convex theory is sharper than Adam.

## Why a separate chapter

Full-batch gradient descent on ImageNet or a language-model corpus is not a step-size problem — it is a *memory and wall-clock* problem. An unbiased (or nearly unbiased) gradient estimator built from one example or a minibatch of size $$B\ll n$$ lets us take many more parameter steps per hour. The price is noise. Adaptive methods spend that noise on a per-coordinate learning rate; momentum spends it on a velocity that remembers consistent directions.

Peer syllabi that treat this as core rather than a remark: MIT 6.7220 (S25), EPFL CS-439, USC CSCI 599, BU EC525.

## Lessons

1. SGD and minibatches — estimators, shuffling, the $$O(1/\sqrt{T})$$ story
2. Momentum and Nesterov — heavy ball vs look-ahead; Distill-style intuition
3. AdaGrad to Adam — diagonal preconditioning
4. AdamW and training practice — decoupled weight decay, schedules, clipping
5. Variance reduction — SVRG and SAGA as first-class finite-sum methods, and when mini-batch Adam still wins
6. Modern adaptive optimizers (optional seminar) — SAM, Sophia, Muon against the AdamW baseline

Interactive SGD cartoons sit in [`interactive_math/optimization`](https://github.com/nglelinh/interactive_math/tree/main/optimization). The Distill-style momentum lesson is [26-02]({% multilang_post_url contents/chapter26/2026-09-15-26_02_momentum_and_nesterov %}) (pair with the FISTA picture in [09-05]({% multilang_post_url contents/chapter09/20-01-08-09_05_acceleration %})). SAM, Muon, and Sophia stay **further reading** — not assessed this term — but they now have a dedicated optional seminar: [26-06]({% multilang_post_url contents/chapter26/2026-09-16-26_06_modern_optimizers %}).
