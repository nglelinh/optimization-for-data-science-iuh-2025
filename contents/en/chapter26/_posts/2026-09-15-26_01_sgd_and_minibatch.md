---
layout: post
title: 26-01 SGD and minibatches
chapter: '26'
order: 2
owner: Nguyen Le Linh
categories:
- chapter26
lang: en
lesson_type: required
---

At the heart of every deep learning training run sits a deceptively simple statistical trick: instead of averaging the gradient over all $$n$$ training points, average it over a random minibatch of $$B$$ points. That single substitution changes optimization from a deterministic descent into a biased-free random walk—one that initially rockets downhill far faster than full-batch gradient descent, yet eventually hits a "noise ball" around the minimum unless the learning rate decays.

## Background Knowledge Map: Variance, Step-Size Schedules, and Random Reshuffling in SGD

- **Unbiasedness & Variance Scaling:** For a uniform minibatch $$S_k$$ of size $$B$$ (with replacement), $$\mathbb{E}[g_k \mid w_k] = \nabla F(w_k)$$ and $$\operatorname{Var}(g_k \mid w_k) = \frac{1}{B}\operatorname{Var}(\nabla f_I(w_k)) \le \frac{\sigma^2}{B}$$. Doubling $$B$$ halves variance but doubles work per step until GPU parallelism saturates.
- **The $$O(\sigma / \sqrt{T})$$ Ceiling:** Because constant-step SGD bounces inside a neighborhood of radius $$O(\eta \sigma^2)$$ around $$w^\star$$, decaying step sizes $$\eta_k \propto 1/\sqrt{k}$$ (or Polyak–Ruppert averaging) are required to reach $$O(1/\sqrt{T})$$ expected suboptimality on convex objectives.
- **Linear Scaling Rule & Critical Batch Size:** Increasing batch size $$B \to k B$$ reduces gradient variance by $$k$$, allowing a larger learning rate (up to the noise-dominated critical batch size $$B_{\text{crit}}$$), beyond which larger batches waste compute without speeding up convergence.
- **Random Reshuffling vs. i.i.d. Sampling:** Shuffling the dataset once per epoch (sampling without replacement) introduces negative correlation between consecutive gradients, empirically converging faster than i.i.d. sampling while avoiding adversarial cyclic ordering.

### Step-by-Step Worked Example (Read Slowly): Computing Minibatch Variance and the SGD Noise Floor

Consider a 1D finite sum $$F(w) = \frac{1}{2}\bigl(f_1(w) + f_2(w)\bigr)$$ where $$f_1(w) = \frac{1}{2}(w - 1)^2$$ and $$f_2(w) = \frac{1}{2}(w + 1)^2$$. Clearly $$F(w) = \frac{1}{2}(w^2 + 1)$$ has unique minimizer $$w^\star = 0$$ with $$F'(0) = 0$$.

1. **Compute the gradient variance right at the optimum $$w^\star = 0$$:**
   - $$f_1'(0) = -1$$ and $$f_2'(0) = +1$$, each sampled with probability $$1/2$$.
   - Mean: $$\mathbb{E}[g] = \frac{1}{2}(-1) + \frac{1}{2}(+1) = 0 = F'(0)$$ (unbiased!).
   - Variance for batch size $$B = 1$$: $$\sigma^2 = \frac{1}{2}(-1)^2 + \frac{1}{2}(+1)^2 = 1$$. Notice the noise does **not** vanish at $$w^\star$$!
2. **Compute the stationary error of constant-step SGD:** With $$w_{k+1} = w_k - \eta(w_k \pm 1) = (1 - \eta) w_k \mp \eta$$, taking expected squares gives
   $$\mathbb{E}[w_{k+1}^2] = (1 - \eta)^2 \mathbb{E}[w_k^2] + \eta^2.$$
   At steady state ($$\mathbb{E}[w_{k+1}^2] = \mathbb{E}[w_k^2] = v_\infty$$):
   $$v_\infty = \frac{\eta^2}{1 - (1 - \eta)^2} = \frac{\eta}{2 - \eta}.$$
3. **Plug in concrete numbers:**
   - With constant $$\eta = 0.2$$: $$v_\infty = \frac{0.2}{1.8} \approx 0.111$$, so SGD permanently hovers at RMS error $$\sqrt{0.111} \approx 0.333$$ around $$w^\star = 0$$.
   - Halving $$\eta$$ to $$0.05$$ shrinks the noise floor to $$v_\infty = \frac{0.05}{1.95} \approx 0.0256$$ (RMS $$\approx 0.160$$)—illustrating concretely why learning-rate decay is essential to settle into the minimum.

Empirical risk is an average. Its gradient is an average too:

$$
\nabla F(w) = \frac{1}{n}\sum_{i=1}^n \nabla f_i(w).
$$

**Stochastic gradient descent** replaces the sum by a single random index $$I_k$$ drawn (with or without replacement) from $$\{1,\ldots,n\}$$:

$$
w_{k+1} = w_k - \eta_k \nabla f_{I_k}(w_k).
$$

If $$I_k$$ is uniform and independent of $$w_k$$, the update is an **unbiased** estimator: $$\mathbb{E}[\nabla f_{I_k}(w_k)\mid w_k]=\nabla F(w_k)$$. A **minibatch** of size $$B$$ averages $$B$$ such terms. Variance drops like $$1/B$$ for independent draws; wall-clock per step grows roughly linearly in $$B$$ until you saturate a GPU. That is the fundamental trade-off.

## Rates you should be able to quote

Under standard Lipschitz / bounded-variance assumptions, SGD on a convex Lipschitz objective with step sizes $$\eta_k \propto 1/\sqrt{k}$$ (or a constant step plus averaging) satisfies

$$
\mathbb{E}\bigl[F(\bar w_T)-F^\star\bigr] = O\bigl(\sigma / \sqrt{T}\bigr)
$$

in the number of *stochastic* steps (Bubeck, *Convex Optimization: Algorithms and Complexity*, Ch. 6). Smooth strongly convex problems can reach linear rates if the noise vanishes at the minimizer, but deep nets are not strongly convex. The practical message is: **more steps with noisy gradients often beat fewer exact gradients**.

Chapter 06 already compared GD and SGD on small sums. Re-open [stochastic_gradient_demo.html](https://nglelinh.github.io/interactive_math/optimization/stochastic_gradient_demo.html) and watch a noisy path still trend downhill.

## Shuffling vs i.i.d.

Theory likes independent samples. Practice uses **random reshuffling**: permute the $$n$$ examples each epoch and walk through the permutation. Without-replacement passes often converge faster empirically; proving it is a 2010s–2020s research topic. For this course: shuffle every epoch, do not silently reuse the same order (that can cycle).

## A tiny logistic loop

```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -40, 40)))

def sgd_logistic(X, y, eta=0.1, batch=16, epochs=20):
    n, d = X.shape
    w = np.zeros(d)
    for _ in range(epochs):
        idx = np.random.permutation(n)
        for s in range(0, n, batch):
            j = idx[s:s + batch]
            p = sigmoid(X[j] @ w)
            g = X[j].T @ (p - y[j]) / len(j)
            w -= eta * g
    return w
```

Compare `batch=1`, `batch=16`, and `batch=n` (full gradient) on a synthetic two-class cloud: wall-clock to a fixed training loss, not just epochs.

### SGD and minibatches in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/sgd-minibatch_en.mp4"></video>
</div>

The m = 3 example: one GD step versus one SGD epoch, constant versus decaying steps, then the effect of the batch size.

**Question.** Given that SGD often escapes shallow basins more readily than full-batch GD, how should that affect your first choice of batch size on an overparameterized model?
