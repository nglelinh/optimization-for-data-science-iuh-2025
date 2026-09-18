---
layout: post
title: 26-05 Variance reduction — SVRG and SAGA
chapter: '26'
order: 6
owner: Nguyen Le Linh
categories:
- chapter26
lang: en
lesson_type: required
---


SGD’s $$O(1/\sqrt{T})$$ ceiling on a convex Lipschitz finite sum is not an information-theoretic destiny. It is the price of using an *unbiased but noisy* gradient whose variance stays order-one even as $$w$$ sits at a minimizer. **Variance-reduced** methods reuse old gradients so that the estimator becomes exact at a snapshot (or in a table), and the noise dies as $$w$$ approaches a minimizer. This lesson is the Opt-for-ML core — SVRG and SAGA — at IUH depth: enough algebra to see *why* the variance vanishes, enough algorithm to implement, and a clear “do not train ResNets this way” boundary.

You already met the noisy path in [26-01]({% multilang_post_url contents/chapter26/2026-09-15-26_01_sgd_and_minibatch %}) and the batch-versus-stochastic cartoon in [08-02-04]({% multilang_post_url contents/chapter08/20-03-29-08_02_04_batch_vs_stochastic_methods %}). Re-open [stochastic_gradient_demo.html](https://nglelinh.github.io/interactive_math/optimization/stochastic_gradient_demo.html) and watch the path jitter *after* it has reached the bowl: that leftover jitter is the disease this page treats.

## The finite-sum problem, and why SGD cannot go linear

Empirical risk is an average,

$$
F(w)=\frac{1}{n}\sum_{i=1}^n f_i(w),\qquad
\nabla F(w)=\frac{1}{n}\sum_{i=1}^n \nabla f_i(w).
$$

A single-example SGD step uses $$g_k=\nabla f_{I_k}(w_k)$$. If $$I_k$$ is uniform and independent of $$w_k$$, then $$\mathbb{E}[g_k\mid w_k]=\nabla F(w_k)$$ — unbiased — but

$$
\mathbb{E}\bigl[\|g_k-\nabla F(w_k)\|_2^2\mid w_k\bigr]
$$

need not go to zero as $$w_k\to w^\star$$. Even at a minimizer, $$\nabla f_i(w^\star)$$ can be a large vector that merely *averages* to zero (think of a well-specified linear model whose residuals still have variance). Bounded-variance SGD on a convex Lipschitz objective therefore stalls at $$O(1/\sqrt{T})$$ in function values. Strong convexity does not save you if the noise floor is constant: the iterates bounce in a ball of radius proportional to $$\eta\sigma$$.

Full-batch gradient descent *does* go linear under strong convexity (Chapter 06), but each step costs $$n$$ gradients. Variance reduction asks for the linear rate at a cost closer to one gradient per step.

## The control-variate idea

Pick any snapshot $$\tilde w$$ at which you are willing to compute the *full* gradient $$\mu=\nabla F(\tilde w)$$ once. For a random index $$I$$ the vector

$$
g(w)=\nabla f_I(w)-\nabla f_I(\tilde w)+\mu
$$

is still unbiased for $$\nabla F(w)$$:

$$
\mathbb{E}[g(w)]
=\nabla F(w)-\nabla F(\tilde w)+\nabla F(\tilde w)
=\nabla F(w).
$$

When $$w=\tilde w$$ one has $$g(\tilde w)=\mu=\nabla F(\tilde w)$$ *exactly* — the noise is zero at the snapshot. When $$w$$ is close to $$\tilde w$$ and each $$\nabla f_i$$ is Lipschitz, $$\nabla f_I(w)-\nabla f_I(\tilde w)$$ is small, so the variance of $$g$$ is small. That is a **control variate**: we subtract a correlated copy of the noise and add back its mean.

## SVRG (Johnson & Zhang, 2013)

SVRG refreshes the snapshot on an outer loop and walks with the control variate on an inner loop.

**Outer loop** $$s=0,1,\ldots,S-1$$

1. Set the snapshot $$\tilde w\leftarrow w$$ and compute $$\mu\leftarrow\nabla F(\tilde w)$$ (one full pass, $$n$$ gradients).
2. **Inner loop** $$t=0,1,\ldots,m-1$$: draw $$I$$ uniformly, set
   $$
   g\leftarrow\nabla f_I(w)-\nabla f_I(\tilde w)+\mu,\qquad
   w\leftarrow w-\eta g.
   $$
3. Optionally average the inner path, or keep the last $$w$$, and return to step 1.

A standard choice is $$m=\Theta(n)$$ inner steps, so the *amortized* cost is a small constant times one gradient per step: one full gradient every $$m$$ steps, plus two stochastic gradients per inner step. Memory beyond the parameter vector is one snapshot $$\tilde w$$ and one vector $$\mu$$ — $$O(d)$$, independent of $$n$$.

**Theorem (sketch, strongly convex finite-sum).** If each $$f_i$$ is $$L$$-smooth and $$F$$ is $$\mu$$-strongly convex, a sufficiently small constant $$\eta$$ and $$m\gtrsim L/\mu$$ yield

$$
\mathbb{E}\bigl[F(\tilde w_{s+1})-F^\star\bigr]
\le \rho\,\mathbb{E}\bigl[F(\tilde w_s)-F^\star\bigr]
$$

with $$\rho<1$$ independent of the horizon. The number of incremental gradients to $$\varepsilon$$-accuracy is $$O\bigl((n+\kappa)\log(1/\varepsilon)\bigr)$$, $$\kappa=L/\mu$$. Vanilla SGD cannot write a $$\log(1/\varepsilon)$$ of this kind while the noise floor is constant.

The proof is a Lyapunov argument: the inner-loop noise is controlled by $$\|w-\tilde w\|$$, which itself shrinks as the snapshot improves. You are not asked to reproduce the constants; you are asked to point at the line $$g=\nabla f_I(w)-\nabla f_I(\tilde w)+\mu$$ and say why the variance dies.

## SAGA (Defazio, Bach, Lacoste-Julien, 2014)

SAGA removes the outer loop by storing a **table** $$g^{(1)},\ldots,g^{(n)}$$ of the last gradient seen for each $$f_i$$. Initialise $$g^{(i)}\leftarrow\nabla f_i(w_0)$$ (or zeros, with a short burn-in) and keep a running average $$\bar g=\frac1n\sum_i g^{(i)}$$.

At each step: draw $$I$$, compute the fresh gradient $$\nabla f_I(w)$$, set

$$
g\leftarrow \nabla f_I(w)-g^{(I)}+\bar g,
$$

then write $$g^{(I)}\leftarrow\nabla f_I(w)$$, update $$\bar g$$ in $$O(d)$$ by the rank-one change, and step $$w\leftarrow w-\eta g$$.

The same control-variate algebra applies, now with a *stale per-example* snapshot instead of a common $$\tilde w$$. There is no periodic full pass. The price is memory: $$n$$ gradient vectors, $$O(nd)$$, or $$O(n)$$ scalars for linear models where $$\nabla f_i(w)=(x_i^\top w-y_i)x_i$$ and it is enough to store the residual. That is why `sklearn.linear_model.LogisticRegression(solver="saga")` is a production default on medium convex ERM, and why SAGA is hopeless as a *deep-net* optimizer — you will not store a gradient table for ImageNet.

**SAG** (Schmidt, Le Roux, Bach) is the biased older sibling: it uses the table average *without* the $$+\nabla f_I(w)-g^{(I)}$$ correction. SAGA’s extra correction restores unbiasedness and simplifies the proof; prefer SAGA unless you are reading the 2013 SAG paper.

## A tiny SVRG loop

```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -40.0, 40.0)))

def svrg_logistic(X, y, lam=1e-3, eta=0.1, inner=None, epochs=20):
    n, d = X.shape
    inner = n if inner is None else inner
    w = np.zeros(d)
    for _ in range(epochs):
        p = sigmoid(X @ w)
        mu = X.T @ (p - y) / n + lam * w          # full gradient
        w_snap = w.copy()
        for _t in range(inner):
            i = np.random.randint(n)
            xi, yi = X[i], y[i]
            g = (sigmoid(xi @ w) - yi) * xi + lam * w
            g_snap = (sigmoid(xi @ w_snap) - yi) * xi + lam * w_snap
            w = w - eta * (g - g_snap + mu)
    return w
```

Compare wall-clock — not epochs — against the minibatch SGD of 26-01 on a strongly convex ridge-logistic problem with $$n=5000$$, target $$\|\nabla F(w)\|_2\le 10^{-4}$$. Then spend the same budget on a one-hidden-layer net: the snapshot cost stays $$n$$ backward passes, the table-of-gradients fantasy of SAGA becomes impossible, and AdamW from 26-04 will look like the grown-up choice.

## What to use when

| Method | Extra memory | Cost per step (amortized) | Typical home | Linear rate on SC finite-sum? |
|--------|--------------|---------------------------|--------------|-------------------------------|
| SGD / mini-batch | none | $$1$$ (or $$B$$) gradients | deep learning | no (noise floor) |
| SVRG | one snapshot + $$\mu$$ | $$\approx 3$$ gradients | convex finite-sum, research code | yes |
| SAGA | one gradient per example | $$1$$ gradient | medium convex ERM (`solver="saga"`) | yes |
| AdamW | two EMAs | $$1$$ minibatch | default DL | not the point |

Learn SVRG so that you can read Opt-for-ML notes (MIT 6.7220, BU EC525) and so that you recognize when a *convex* ERM — logistic regression, linear SVM, a Lasso smoother — should *not* be trained with Adam out of habit. Mini-batch Adam still wins on deep nets because (i) storing or refreshing full gradients is the wrong complexity class, (ii) the landscape is not strongly convex, and (iii) the hardware wants large, regular kernels, not a random $$I$$ with a snapshot subtract.

A last neighbouring idea, not assessed: **SARAH** / **SPIDER** replace the control variate by a recursive estimator that can be tighter in theory; **FedAvg** in Chapter 29 is *not* variance reduction in this sense (it averages models, not control variates), though SCAFFOLD’s control variates are the federated cousin of SVRG.

**Exercise 1.** Prove unbiasedness of the SVRG estimator in one line, then exhibit a two-example quadratic where vanilla SGD’s variance at $$w^\star$$ is positive while SVRG’s variance at the snapshot is zero.

**Exercise 2.** On ridge-logistic with $$n=5000$$, plot training gradient norm versus *number of $$f_i$$ gradients* for SGD, SVRG, and (if memory allows) SAGA. Mark the SVRG snapshot passes. Then plot the same curves versus wall-clock. Which $$x$$-axis changes the winner?

**Question.** The control variate $$g$$ is unbiased for every $$w$$, not only at $$\tilde w$$. Why, then, must we still refresh the snapshot — what happens to $$\mathrm{Var}(g)$$ if we freeze $$\tilde w$$ and let $$w$$ walk far away?
