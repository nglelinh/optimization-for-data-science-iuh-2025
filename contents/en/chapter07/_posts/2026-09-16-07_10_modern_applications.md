---
layout: post
title: 07-10 Modern applications of the subgradient
chapter: '07'
order: 17
owner: Nguyen Le Linh
categories:
- chapter07
lang: en
lesson_type: optional
---

# Modern applications of the subgradient

This optional lesson does **not** redo the calculus of Chapter 07. It shows where the same objects — a vector $$g$$ satisfying $$f(y)\ge f(x)+g^\top(y-x)$$, the set $$\partial f(x)$$, and the stationarity test $$0\in\partial f(x^\star)$$ — appear in CS and data-science work from about 2022 to 2026. After reading it you should be able to name a nonsmooth loss or regularizer in a deployed pipeline, write the inclusion that characterises a minimiser, and point to a paper rather than a slogan.

## Why the subgradient is not a historical footnote

ReLU networks, $$\ell_1$$ feature selection, pinball (quantile) losses, and Huber-type robust fits are all **nonsmooth convex or path-differentiable** pieces. Automatic differentiation in PyTorch or JAX still returns a vector at a kink; the right language for that vector is a **conservative field**, which agrees with a subgradient on convex pieces and with a Clarke element almost everywhere. If you only remember “the gradient is zero at a min,” you cannot debug a Lasso support, a dead ReLU, or a quantile fit.

## 1. ReLU networks and nonsmooth automatic differentiation

The rectifier $$\operatorname{ReLU}(t)=\max\{t,0\}$$ has

$$
\partial\operatorname{ReLU}(t)=\begin{cases}\{0\} & t<0,\\ [0,1] & t=0,\\ \{1\} & t>0.\end{cases}
$$

A deep net composed of affine maps and ReLUs is Lipschitz and semialgebraic, hence **path-differentiable**. Bolte and Pauwels (2021) showed that the object backprop actually implements is a *conservative set-valued field*: it obeys a chain rule even though the Clarke subdifferential of a ReLU program need not. Bolte, Boustany, Pauwels, and Pesquet (2022) then proved a **nonsmooth cheap-gradient principle** for reverse-mode AD and showed that computing *two distinct Clarke subgradients* of a simple ReLU net is NP-hard — so production frameworks are not being lazy when they pick one element of $$\partial\operatorname{ReLU}(0)$$ (usually $$0$$). Blondel and Roulet (2024) organise the same story as *differentiable programming*: you design the program so that a conservative derivative exists, then you train with SGD.

**Course link.** The calculus rules in [07-02-02 Subgradient calculus]({% multilang_post_url contents/chapter07/21-03-25-07_02_02_subgradient_calculus %}) (sums, maxima, composition with affine maps) are exactly the rules a ReLU computational graph uses. The optimality test $$0\in\partial f(x)$$ is what a convex last-layer problem (for example a linear SVM or a Lasso head) still has to satisfy.

## 2. Lasso, elastic net, and modern GLM paths

The Lasso

$$
\min_\beta\ \tfrac12\|y-X\beta\|_2^2+\lambda\|\beta\|_1
$$

is the running example of this chapter: stationarity is $$X^\top(y-X\beta)=\lambda v$$ with $$v\in\partial\|\beta\|_1$$, i.e. $$v_j=\operatorname{sign}(\beta_j)$$ on the support and $$|v_j|\le 1$$ off it ([07-03-03 Lasso optimality]({% multilang_post_url contents/chapter07/21-03-25-07_03_03_example_lasso_optimality_condition %})). That inclusion is still how `glmnet` and `skglm` decide which coordinates are zero.

Tay, Narasimhan, and Hastie (2023) extended elastic-net paths in **glmnet 4.1+** to *all* GLM families and to stratified Cox models — the workhorse for polygenic scores, survival analysis, and high-dimensional clinical prediction. Bertrand, Klopfenstein, Bannier, Gidel, and Massias (2022) released **skglm**, a scikit-learn solver that uses working sets and dual-gap tests (again, subdifferential inclusions) to fit sparse GLMs with millions of features in seconds. Guha, Ndiaye, and Huo (2023) then used the Lasso homotopy — the same active-set jumps you see from $$\partial\|\cdot\|_1$$ — to compute **conformal prediction sets** for sparse GLMs without refitting at every candidate response.

**Takeaway.** Soft-thresholding is not a homework trick; it is the proximal map of $$\lambda\|\cdot\|_1$$ and the reason a coordinate can be certified inactive.

## 3. Pinball loss, quantiles, and distribution-free intervals

The pinball (check) loss $$\rho_\tau(r)=\tau r_+ +(1-\tau)(-r)_+$$ is convex and piecewise linear. A sample quantile is a minimiser of $$\sum_i\rho_\tau(y_i-x_i^\top\beta)$$; the subgradient with respect to the residual is $$\tau$$ above zero, $$\tau-1$$ below, and $$[\tau-1,\tau]$$ at a kink. Conformalised quantile regression (Romano, Patterson, and Candès, 2019) wraps that nonsmooth fit in a calibration step; Angelopoulos and Bates (2023) is the 2023 handbook used in vision and NLP pipelines that need a **90% interval**, not a point. The 2023 ICML path-following work above is the sparse, high-dimensional cousin.

## 4. A five-line check you can run

The following snippet prints a subgradient of $$\|x\|_1$$ and of ReLU at the origin — the two kinks students meet first.

```python
import numpy as np

def subgrad_l1(x):
    g = np.sign(x)
    g[x == 0] = 0.0  # one element of [-1, 1]
    return g

def relu_elem(t, kink=0.0):
    return 0.0 if t < 0 else (1.0 if t > 0 else kink)

x = np.array([1.2, 0.0, -0.4])
print(subgrad_l1(x), relu_elem(0.0))
```

Changing the kink value does not change the convex inequality; it *does* change a deep net’s backward pass. That is the conservative-field story in miniature.

## What to remember

The subgradient is the certificate that a nonsmooth convex model is optimal, and a conservative selection of it is what modern autodiff actually differentiates. When a paper says “we train a ReLU net / a Lasso-GLM / a quantile head,” the first-order object is the one defined in this chapter.

**Question.** If a Lasso coordinate satisfies $$|X_j^\top(y-X\hat\beta)|<\lambda$$, why can you delete column $$j$$ without changing $$\hat\beta$$? How is that the same geometry as a ReLU unit that stays off?

## Sources

- Bolte, J., & Pauwels, E. (2021). Conservative set valued fields, automatic differentiation, stochastic gradient methods and deep learning. *Mathematical Programming*, 188, 19–51. [doi:10.1007/s10107-020-01501-5](https://doi.org/10.1007/s10107-020-01501-5)
- Bolte, J., Boustany, R., Pauwels, E., & Pesquet, B. (2022). On the complexity of nonsmooth automatic differentiation. [arXiv:2206.01730](https://arxiv.org/abs/2206.01730)
- Blondel, M., & Roulet, V. (2024). *The Elements of Differentiable Programming*. [arXiv:2403.14606](https://arxiv.org/abs/2403.14606)
- Tay, J. K., Narasimhan, B., & Hastie, T. (2023). Elastic net regularization paths for all generalized linear models. *Journal of Statistical Software*, 106(1), 1–31. [doi:10.18637/jss.v106.i01](https://doi.org/10.18637/jss.v106.i01)
- Bertrand, Q., Klopfenstein, Q., Bannier, P.-A., Gidel, G., & Massias, M. (2022). Beyond L1: Faster and better sparse models with skglm. *NeurIPS*.
- Guha, E. K., Ndiaye, E., & Huo, X. (2023). Conformalization of sparse generalized linear models. *ICML*, PMLR 202.
- Angelopoulos, A. N., & Bates, S. (2023). Conformal prediction: A gentle introduction. *Foundations and Trends in Machine Learning*, 16(4).
- Romano, Y., Patterson, E., & Candès, E. J. (2019). Conformalized quantile regression. *NeurIPS*. (background for the pinball + calibration pipeline)
