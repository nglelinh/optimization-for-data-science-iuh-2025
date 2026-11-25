---
layout: post
title: 23-05 Modern applications of coordinate descent
chapter: '23'
order: 6
owner: Nguyen Le Linh
categories:
- chapter23
lang: en
lesson_type: optional
---

Pathwise coordinate descent did not freeze in 2010 with `glmnet`. Over the past decade, it has evolved into the standard computational backbone for generalized linear models, safe feature-screening rules that provably discard millions of irrelevant predictors before ever touching them, nonconvex sparse penalties in `skglm`, and dual linear SVMs in `LIBLINEAR`. Whenever a modern statistical package computes a full regularization path in a fraction of a second, you are watching Chapter 23’s coordinate-wise mechanics running under the hood.

## Key ideas: Modern Extensions of Coordinate Descent

- **IRLS + Coordinate Descent for All GLMs:** `glmnet` (2023) wraps coordinate descent inside Iteratively Reweighted Least Squares: an outer loop forms a quadratic approximation (working weights and response), and the inner loop solves the weighted Lasso via active-set CD.
- **Gap-Safe Screening Rules:** Using the duality gap $$G(\beta, \theta)$$ between a primal iterate $$\beta$$ and a feasible dual vector $$\theta$$, gap-safe rules prove that any feature $$j$$ inside a safe sphere around $$\theta$$ must have $$\beta_j^\star = 0$$—eliminating it permanently from all remaining iterations with **zero** loss of exactness.
- **Working Sets Beyond $$\ell_1$$ (`skglm`):** Modern solvers extend active-set CD to nonconvex and structured penalties (MCP, SCAD, Group Lasso, Sparse-Group Lasso) by maintaining small dynamic working sets and prioritizing features with largest KKT violation.
- **Dual Coordinate Descent for Linear SVMs:** In `LIBLINEAR`, minimizing the dual SVM objective subject to box constraints $$0 \le \alpha_i \le C$$ updates one dual multiplier $$\alpha_i$$ at a time via a clipped 1D Newton step, scaling effortlessly to millions of sparse text features.

### Worked example: Gap-Safe Feature Screening in Action

Suppose we are solving Lasso $$\min_\beta \frac{1}{2}\|y - X\beta\|_2^2 + \lambda \|\beta\|_1$$ with $$\lambda = 2$$, unit-norm columns $$\|X_j\|_2 = 1$$, current primal-dual gap $$G(\beta, \theta) = 0.08$$, and feasible dual point $$\theta = r / \max(\lambda, \|X^\top r\|_\infty)$$.

1. **Compute the safe sphere radius:** The classic Gap-Safe sphere (Fercoq, Gramfort, Salmon 2015) certifies that the optimal dual variable $$\theta^\star$$ lies within Euclidean radius
   $$R = \sqrt{\frac{2 G(\beta, \theta)}{\lambda^2}} = \sqrt{\frac{2(0.08)}{2^2}} = \sqrt{0.04} = 0.2$$
   of the current dual vector $$\theta$$.
2. **Apply Cauchy–Schwarz to test feature $$j$$:** By KKT optimality, if $$|X_j^\top \theta^\star| < 1$$, then necessarily $$\beta_j^\star = 0$$. Using the triangle inequality and Cauchy–Schwarz,
   $$|X_j^\top \theta^\star| \le |X_j^\top \theta| + \|X_j\|_2 \cdot \|\theta^\star - \theta\|_2 \le |X_j^\top \theta| + (1)(0.2).$$
3. **Screen two candidate features:**
   - **Feature A** has $$|X_A^\top \theta| = 0.65$$: upper bound is $$0.65 + 0.20 = 0.85 < 1$$. **Safely screened out!** We can delete column $$A$$ immediately with mathematical certainty that $$\beta_A^\star = 0$$.
   - **Feature B** has $$|X_B^\top \theta| = 0.90$$: upper bound is $$0.90 + 0.20 = 1.10 \ge 1$$. Keep feature $$B$$ in the active pool until $$G$$ shrinks further.

Pathwise coordinate descent is the reason the Lasso is a *default button* in applied statistics rather than a research prototype. Friedman, Hastie, and Tibshirani’s **glmnet** (JSS 2010) still ships in R; scikit-learn’s `lasso_path` / `enet_path` are the same idea in Cython. This optional note updates that story to 2023–2026: glmnet for *every* GLM family, screening and working sets at a million features, and the dual CD solver that still trains linear SVMs in production.

A cyclic (or random) coordinate step on a composite objective $$f(\beta)+ \lambda\|\beta\|_1$$ is a scalar soft-threshold. The whole **regularization path** is a warm-started loop over a decreasing grid $$\lambda_1>\cdots>\lambda_T$$. That is the algorithm; the applications below are what practitioners actually run.

## 1. glmnet for all GLMs (2023)

Tay, Narasimhan, and Hastie, *Elastic Net Regularization Paths for All Generalized Linear Models*, *Journal of Statistical Software* 106(1):1–31, 2023, [doi:10.18637/jss.v106.i01](https://doi.org/10.18637/jss.v106.i01), extend glmnet 4.x beyond the built-in Gaussian / binomial / Poisson / Cox families. Any GLM with a smooth log-likelihood now gets a cyclical elastic-net path. Version 4.1 (same codebase, 2021–2023 docs at [glmnet.stanford.edu](https://glmnet.stanford.edu/)) adds `(start, stop)` survival data, strata, and sparse $$X$$.

This is the paper to cite when a student asks “we learned Lasso on least squares — does CD still win for logistic, Cox, or a custom GLM?” Yes, because the IRLS / proximal-Newton outer loop reduces each step to a *weighted* least-squares Lasso, and that inner problem is exactly the coordinate descent you already coded in 23-03.

## 2. scikit-learn paths and gap-safe screening

`sklearn.linear_model.lasso_path` and `enet_path` (current docs: scikit-learn 1.5–1.9) run Fortran-order coordinate descent with **gap-safe screening rules**: once the duality gap certifies that a coordinate stays at zero, it is dropped for the rest of that $$\lambda$$. The 2025–2026 maintenance PRs (e.g. precomputing residuals and column norms across a path) are not new mathematics; they are the reason a leukemia microarray with $$p\sim 10^4$$ genes still fits a 100-point path in seconds. When you write `LassoCV`, you are running Chapter 23, not Adam.

## 3. skglm: working sets beyond $$\ell_1$$ (NeurIPS 2022)

Bertrand, Klopfenstein, Blondel, Vaiter, Gramfort, and Massias, *Beyond L1: Faster and Better Sparse Models with skglm*, NeurIPS 2022, [paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/fe5c31e525e9a26a1426ab0b589f42fe-Abstract-Conference.html), push coordinate descent past the glmnet feature set. **Working sets** iteratively enlarge a small active set; Anderson acceleration (Bertrand & Massias, 2021) gives a practical speedup that Nesterov-on-CD often does not. The package handles MCP / SCAD, group and multitask norms, and custom data-fits — the “nonconvex penalties” bullet already on the 23-00 landing page, now with software you can `pip install`. Genomics, vision dictionaries, and M/EEG inverse problems are the running applications in the paper; the optimization claim is that CD plus working sets still dominates full-gradient proximal methods once $$p$$ is in the millions.

## 4. Dual coordinate descent for linear SVMs

Hsieh, Chang, Lin, Keerthi, and Sundararajan (ICML 2008) trained a linear SVM by dual coordinate descent; **LIBLINEAR** is still the solver behind `sklearn.svm.LinearSVC` and a large fraction of industrial text classifiers. Each dual coordinate is a clipped 1-D quadratic. Nothing about that algorithm became obsolete because transformers arrived: bag-of-words logistic / SVM baselines, click models, and high-dimensional tabular GLMs are still CD’s home turf. Use AdamW (Chapter 26) for a deep net; use glmnet / LIBLINEAR / skglm when the model is *generalized linear and sparse*.

```python
# Pathwise CD is one library call — the algorithm is Chapter 23
from sklearn.linear_model import lasso_path
from sklearn.datasets import make_regression
X, y = make_regression(n_samples=400, n_features=80, n_informative=8, noise=8.0)
alphas, coefs, _ = lasso_path(X, y, eps=1e-3)
# coefs.shape == (n_features, n_alphas); count how late each feature enters
```

**Exercise.** On `make_regression` with $$p=200$$, $$n=150$$, five informative features, plot the glmnet / `lasso_path` coefficients against $$-\log\lambda$$. Then fit the same path with skglm (or a hand-rolled cyclic soft-threshold if you skip the extra dependency) and check that the *support* agrees on the cross-validated $$\lambda$$. Finally, train `LinearSVC` on a bag-of-words subset of 20-newsgroups and report wall-clock versus a mini-batch Adam logistic net with the same $$\ell_2$$ ball. CD should win on the linear model; Adam should win only after you add a hidden layer.

## Sources

- J. Friedman, T. Hastie, R. Tibshirani, *J. Stat. Softw.* 33(1), 2010 — glmnet pathwise CD.
- J. K. Tay, B. Narasimhan, T. Hastie, *J. Stat. Softw.* 106(1):1–31, 2023 — elastic-net paths for all GLMs.
- Q. Bertrand et al., NeurIPS 2022 — skglm, working sets, nonconvex sparse models.
- C.-J. Hsieh et al., ICML 2008 — dual CD for linear SVMs (LIBLINEAR).
- scikit-learn user guide, *Coordinate descent* / gap-safe screening (v1.5+).
- S. J. Wright, *Math. Programming* 151:3–34, 2015 — survey of CD algorithms.
