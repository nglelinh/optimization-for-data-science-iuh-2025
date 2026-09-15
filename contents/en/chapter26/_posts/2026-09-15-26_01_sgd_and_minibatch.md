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

**Question.** Given that SGD often escapes shallow basins more readily than full-batch GD, how should that affect your first choice of batch size on an overparameterized model?
