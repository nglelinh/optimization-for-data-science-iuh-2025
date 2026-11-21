---
layout: post
title: 03-08 Applications and recent developments
chapter: '03'
order: 16
owner: Nguyen Le Linh
categories:
- chapter03
lang: en
lesson_type: optional
---

Convex functions are the objectives you can trust: a local minimizer is global, and the first-order lower bound $$f(y)\ge f(x)+\nabla f(x)^\top(y-x)$$ is a supporting hyperplane of the epigraph. This lesson shows three places where that geometry is still doing work in 2021–2025 machine learning — even when the *full* deep network is nonconvex.

## Cross-entropy, log-sum-exp, and calibration

For a fixed feature map, multiclass logistic regression is convex in the last-layer weights. With logits $$z\in\mathbb{R}^C$$ and one-hot label $$y$$,

$$
\ell(z,y) = -z_y + \log\sum_{c=1}^C e^{z_c}
$$

is convex in $$z$$ because log-sum-exp is convex and increasing in each coordinate, and $$-z_y$$ is affine. Composition rules from 03-02 are exactly the certificate. Softmax probabilities are $$\nabla$$ of log-sum-exp; the conjugate of log-sum-exp is the negative entropy on the simplex (03-03). That is why temperature scaling — replacing $$z$$ by $$z/T$$ and fitting a single scalar $$T$$ on a validation set — is a *convex* one-dimensional problem.

Guo et al. (2017) popularized temperature scaling as a post-hoc calibration map. Minderer, Djolonga, Romijnders, Hubis, Zhai, Houlsby, Tran, and Lucic (*Revisiting the Calibration of Modern Neural Networks*, [NeurIPS 2021](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html); [arXiv:2106.07998](https://arxiv.org/abs/2106.07998)) re-measured calibration on a large grid of modern image models, including Vision Transformers and MLP-Mixer, and found that several recent non-convolutional architectures are *better* calibrated than the overconfident CNNs of the previous generation. The optimization content for this course is smaller than the empirical claim: the loss you already know is convex in the logits, and a one-parameter temperature is a convex recalibration.

## Neural collapse: when a nonconvex net meets a convex last layer

After interpolation, trained classifiers often enter a *terminal phase* in which last-layer features collapse to their class means, those means form a simplex ETF, and the classifier aligns with the means (Papyan, Han, and Donoho, [PNAS 2020](https://www.pnas.org/doi/10.1073/pnas.2015509117)). Zhu, Ding, Zhou, and coauthors ([NeurIPS 2021](https://papers.nips.cc/paper/2021/hash/f92586a25bb3145facd64ab20fd554ff-Abstract.html)) analyzed an unconstrained-feature model that *isolates* the last layer: features and classifier weights are free variables, the loss is cross-entropy plus weight decay. In that model the landscape is benign — ETF configurations are the only global minimizers, and other critical points are strict saddles with negative curvature.

The lesson for Chapter 03 is not “deep nets are convex.” It is that the *convex* piece you can name (cross-entropy in the last-layer activations and weights, plus a Euclidean regularizer) already explains a surprising amount of the geometry people measure at the end of training. When a paper says the last layer “collapses,” translate it as: the convex last-layer problem, given free features, wants a highly symmetric configuration.

## Contrastive losses and convex surrogates

Self-supervised contrastive learning (SimCLR, CLIP, and their successors) typically minimizes an InfoNCE-style loss. For an anchor representation $$u$$, a positive $$v_+$$, and negatives $$v_1,\ldots,v_K$$,

$$
\ell = -\log \frac{e^{u^\top v_+/\tau}}{e^{u^\top v_+/\tau} + \sum_{k=1}^K e^{u^\top v_k/\tau}}.
$$

As a function of the *similarities* (or of $$u$$ with the $$v$$’s held fixed), this is again a log-sum-exp of linear forms, hence convex in $$u$$. The overall deep network is not convex, but every inner contrastive head is a convex classification problem on the hypersphere. Wang and Isola (*Understanding Contrastive Representation Learning through Alignment and Uniformity*, [ICML 2020](https://proceedings.mlr.press/v119/wang20k.html)) decompose the asymptotic InfoNCE objective into an alignment term (pull positives together) and a uniformity term (spread features on the sphere). The 2020 date sits just before the requested window; the same loss is the default in 2022–2026 vision–language models, including the CLIP-style setups against which Lion was later compared (Chapter 06).

## A three-line check you can do in NumPy

Convexity of log-sum-exp is not an abstract slogan. The following snippet checks the Jensen inequality on random logits — the definition from 03-01.

```python
import numpy as np

def lse(z):
    m = np.max(z)
    return m + np.log(np.sum(np.exp(z - m)))

rng = np.random.default_rng(0)
z1, z2 = rng.normal(size=5), rng.normal(size=5)
t = 0.3
lhs = lse((1 - t) * z1 + t * z2)
rhs = (1 - t) * lse(z1) + t * lse(z2)
print(lhs, "<=", rhs, "?", lhs <= rhs + 1e-12)
```

If this ever fails on finite floats after the standard max-shift, you have a bug, not a counterexample.

## What to carry forward

When you write a loss, ask whether it is convex in the *last* argument the solver sees (logits, similarities, linear predictors). If it is, composition rules and conjugates from this chapter apply, even if the feature map in front is a Transformer. Calibration, neural collapse, and contrastive heads are three different stories with the same convex atom: log-sum-exp.

## Sources

1. M. Minderer et al., “Revisiting the Calibration of Modern Neural Networks,” NeurIPS 2021. [abstract](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html) · [arXiv:2106.07998](https://arxiv.org/abs/2106.07998)
2. V. Papyan, X. Y. Han, and D. L. Donoho, “Prevalence of neural collapse…,” *PNAS* 2020. [DOI](https://www.pnas.org/doi/10.1073/pnas.2015509117)
3. Z. Zhu, T. Ding, J. Zhou, et al., “A Geometric Analysis of Neural Collapse with Unconstrained Features,” NeurIPS 2021. [abstract](https://papers.nips.cc/paper/2021/hash/f92586a25bb3145facd64ab20fd554ff-Abstract.html)
4. T. Wang and P. Isola, “Understanding Contrastive Representation Learning through Alignment and Uniformity,” ICML 2020. [PMLR](https://proceedings.mlr.press/v119/wang20k.html)
