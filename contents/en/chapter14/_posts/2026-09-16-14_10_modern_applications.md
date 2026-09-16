---
layout: post
title: 14-10 Modern applications of Newton's method (2022–2026)
chapter: '14'
order: 16
owner: Nguyen Le Linh
categories:
- chapter14
lang: en
lesson_type: optional
---

Newton's method in this chapter is the exact local quadratic model

$$
x^{+} = x - t\, \bigl(\nabla^2 f(x)\bigr)^{-1}\nabla f(x),
$$

together with the Newton decrement, affine invariance, and self-concordance that make the theory honest. Full Hessians of language models are not stored, yet the *same idea* — precondition by curvature, then take a damped step — is how several 2022–2026 systems beat a well-tuned Adam baseline. This lesson is a survey, not an assessed algorithm zoo: you should be able to point to the Hessian (or a diagonal / Kronecker stand-in) in each story and say what was thrown away to make the step cheap.

The four snapshots below are chosen because they are real deployments or refereed measurements, not folklore. They sit next to Chapter 26's remark that Sophia is further reading there; here we unpack *why* a Newton-style preconditioner can be cheaper than it looks.

## Sophia: a diagonal Hessian for language-model pre-training

Liu, Li, Hall, Liang, and Ma (ICLR 2024) introduce **Sophia** (*Second-order Clipped Stochastic Optimization*). The update is an exponential moving average of stochastic gradients divided by an exponential moving average of a *diagonal* Hessian estimate, followed by coordinate-wise clipping. The Hessian is refreshed only every handful of steps, so the average wall-clock overhead is small. Two estimators appear in the paper: a Hutchinson estimator that uses Hessian–vector products, and a Gauss–Newton–Bartlett estimator that draws a label from the model's predictive distribution and uses the squared gradient of that resampled loss — biased, but nonnegative and cheap.

On GPT-style models from 125M to 1.5B parameters, Sophia matches Adam's validation perplexity in about half the steps and, because the per-step cost is comparable, in about half the compute and wall-clock time. The theory (in a simplified strongly convex setting) says the runtime need not depend on the condition number once each coordinate is scaled by its own curvature — exactly the affine-invariance intuition from [14-02-02]({% multilang_post_url contents/chapter14/2021-03-26-14_02_02_affine_invariance_of_newton_method %}), restricted to a diagonal group.

The clipping parameter is the engineering counterpart of a trust region: when the local Hessian is stale or indefinite, a raw Newton step can explode; a coordinate clip restores the “damped Newton” discipline you already saw with backtracking. Official code lives at [Liuhong99/Sophia](https://github.com/Liuhong99/Sophia). Read this at survey depth: you are not expected to re-derive the Bartlett estimator, but you should be able to write the update and explain why a *diagonal* Hessian is the only object that still fits in GPU memory next to a 1B-parameter model.

## K-FAC for transformers, convnets, and graphs

Kronecker-Factored Approximate Curvature (K-FAC; Martens & Grosse, 2015) approximates the Fisher / generalised Gauss–Newton matrix of a layer as a Kronecker product, which is the curvature of the *expected* loss rather than a raw Hessian, but it is the object Newton-type methods actually invert in deep learning. Eschenhagen, Immer, Turner, Schneider, and Hennig (NeurIPS 2023) give the missing framework for *weight-sharing* layers — the linear maps inside convolutions, recurrent cells, graph networks, and transformers. They distinguish **K-FAC-expand** (the historical KFC-style factorisation) from **K-FAC-reduce**, prove exactness of each flavour on deep linear networks in the matching sharing regime, and show that both reach a fixed validation target on a GNN and a Vision Transformer in roughly 50–75% of the first-order step count, with a comparable wall-clock gain.

This is Newton with a structured inverse: you still solve a linear system against an approximate Hessian, but the Kronecker factors keep the solve at the size of an activation covariance rather than the size of the weight matrix. If Sophia is “Newton on the diagonal,” K-FAC is “Newton on a Kronecker algebra.” The pedagogical question is the same as in the self-concordant analysis: *what curvature are you willing to compute, and what invariance do you keep?*

## Newton–Cholesky for generalised linear models in scikit-learn

Not every modern Newton story is a language model. scikit-learn 1.2 (2022) added `solver="newton-cholesky"` to its GLM estimators (`PoissonRegressor`, `GammaRegressor`, `TweedieRegressor`), later extended to binary logistic regression. The solver performs Newton–Raphson steps — equivalently, iteratively reweighted least squares — and factors the explicit Hessian by Cholesky. The documentation is unusually honest for a library: the method is the right default when $$n_{\text{samples}} \gg n_{\text{features}}$$ (especially one-hot categoricals with rare levels), and memory is quadratic in the number of features because the Hessian is *formed*.

This is the Chapter 14 algorithm without approximation. The IRLS Hessian of a GLM is a Gram matrix $$X^\top W X$$ with a diagonal weight $$W$$ that depends on the current mean; Cholesky is the numerically stable way to apply $$(\nabla^2 f)^{-1}$$. Students who only meet Newton on a whiteboard should run

```python
from sklearn.linear_model import PoissonRegressor
PoissonRegressor(solver="newton-cholesky", alpha=1e-4).fit(X, y)
```

and compare iteration counts with `solver="lbfgs"`. When the design is tall and skinny, exact Newton is not a luxury — it is the production solver.

## What to keep from the survey

AdaHessian (Yao, Gholami, Shen, Keutzer, Mahoney, AAAI 2021) is the immediate precursor of Sophia: a Hutchinson diagonal with Adam-style moments. SOAP and Shampoo (Chapter 18) replace the diagonal by a Kronecker or eigenbasis preconditioner and are cousins, not competitors. Full Newton remains the right tool on GLMs, kernel methods of moderate size, and the centering steps of the barrier / primal-dual methods in Chapters 15 and 17.

A useful exam sentence: *modern second-order ML is almost never “form $$\nabla^2 f$$ and factor it”; it is “estimate a structured curvature, damp or clip the step, and amortise the estimate over many iterations.”* The exceptions — Newton–Cholesky GLMs — prove the rule by being the cases where forming the Hessian is still cheaper than walking with a first-order method.

## Sources

- H. Liu, Z. Li, D. Hall, P. Liang, T. Ma, “Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training,” ICLR 2024. [arXiv:2305.14342](https://arxiv.org/abs/2305.14342)
- R. Eschenhagen, A. Immer, R. Turner, F. Schneider, P. Hennig, “Kronecker-Factored Approximate Curvature for Modern Neural Network Architectures,” NeurIPS 2023.
- Z. Yao, A. Gholami, S. Shen, K. Keutzer, M. W. Mahoney, “ADAHESSIAN: An Adaptive Second Order Optimizer for Machine Learning,” AAAI 2021.
- scikit-learn 1.2 release notes and `newton-cholesky` solver documentation (2022–); GLM PR [#24637](https://github.com/scikit-learn/scikit-learn/pull/24637).
