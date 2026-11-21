---
layout: post
title: "19-05 Notable examples"
chapter: '19'
order: 9
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

## Glmnet and QUIC
There are two very well-known packages built on the proximal Newton method.

* **glmnet** (Friedman et al., 2009): implements prox Newton for $$l_1$$-penalized generalized linear models. The inner problem is solved with coordinate descent.

* **QUIC** (Hsieh et al., 2011): implements prox Newton for the graphical lasso problem. It uses a factorization trick and solves the inner problem with coordinate descent.

Both packages are widely used for their respective purposes and can be regarded as state of the art.

The proximal Newton method evaluates the gradient of $$g$$ less often than proximal gradient descent. Therefore, the more expensive $$g$$ is to compute, the more advantageous proximal Newton becomes. Careful choice of the inner solver also leads to better performance.

## Example: lasso logistic regression
Let us look at the example from Lee et al. (2012).

For $$l_1$$-regularized logistic regression, the following three methods were compared:
1. FISTA: accelerated proximal gradient 2. spaRSA: spectral projected gradient method 3. PN: proximal Newton

#### Dense Hessian (n=5000, p=6000)
The first problem has a dense feature matrix $$X$$ with n = 5000 samples and p = 6000 features. Because the Hessian is dense, this is a very challenging problem. The following performance was observed.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.05_Lasso_Example1.png" alt="[Fig 1] Dense hessian X (n=5000, p=6000) [2]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Dense hessian X (n=5000, p=6000) [2]</figcaption>
</p>
</figure>

The right plot measures performance by the number of function evaluations and the left plot by time. In terms of function evaluations, PN is clearly superior.

Here most of the cost is spent computing $$g$$ and $$\nabla g$$, in particular evaluating the $$\exp$$ and $$\log$$ functions.

#### Sparse Hessian (n=542,000, p=47,000)

In the next case $$X$$ is sparse, so computing $$g$$ and $$\nabla g$$ takes less time.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.05_Lasso_Example-sparse.png" alt="[Fig 2] Sparse hessian X (n=542,000, p=47,000) [2]" width="70%">
  <figcaption style="text-align: center;">[Fig 2] Sparse hessian X (n=542,000, p=47,000) [2]</figcaption>
</p>
</figure>

## Inexact prox evaluations
When the proximal Newton method evaluates the proximal operator, the prox generally has no closed form and cannot be computed exactly. Even so, it is a very good property if the prox is computed to high accuracy.

Lee (2014) proposed stopping rules for the inner problem that guarantee global convergence and local superlinear convergence.

#### Three stopping rules
Three stopping rules for the inner optimization were compared on a graphical lasso estimation problem with n = 72 samples and p = 1255 features.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.05_Inexact_prox.png" alt="[Fig 3] Three stopping rules [2]" width="70%">
  <figcaption style="text-align: center;">[Fig 3] Three stopping rules [2]</figcaption>
</p>
</figure>

The three stopping rules are adaptive, maxiter = 10, and exact. Maxiter performs at most 10 inner iterations; exact iterates until the exact solution is found.

Since the proximal Newton method converges quadratically, the exact rule exhibits quadratic convergence. With maxiter = 10, at most 10 inner iterations are not enough to retain quadratic convergence, whereas the adaptive rule does achieve quadratic convergence and is the fastest of the three.

#### Stopping rule of the usual Newton method
In the usual Newton's method, the inner problem minimizes the quadratic approximation $$\tilde{g}_{k-1}$$ of $$g$$ at $$x^{(k-1)}$$. We choose a sequence $$\eta_k, k=1,2,3,...$$ (called the forcing sequence) and stop when the following condition holds.

> \begin{align}
\parallel \nabla \tilde{g}_{k-1}(x^{(k)}) \parallel_2 & \le \eta_k \parallel  \nabla g(x^{(k-1)})  \parallel_2 \\\\
\end{align}

This condition says that the gradient of the model at the next point is at most $$\eta_k$$ times the gradient at the current point. Here the quadratic approximation is $$\tilde{g}_{k-1}(z) = \nabla g(x^{(k-1)})^T (z-x^{(k-1)}) + \frac{1}{2} (z - x^{(k-1)})^T \nabla^2 g(x^{(k-1)}) (z - x^{(k-1)})$$.

#### Stopping rule of the proximal Newton method
Lee et al. (2012) proposed using the generalized gradient instead of the gradient for the proximal case.

> $$
> \begin{align}
\parallel G_{\tilde{f}_{k-1}/M}(x^{(k)}) \parallel_2 & \le \eta_k \parallel  G_{f/M}(x^{(k-1)})  \parallel_2
\end{align}
> $$

Here $$\tilde{f}_{k-1} = \tilde{g}_{k-1} + h$$ and $$mI \preceq \nabla^2 g \preceq MI$$.

They then proved that, if $$\eta_k$$ is chosen as follows, the inexact proximal Newton method has a local superlinear rate.

> $$
> \begin{align}
> \eta_k \le \min \left\{ \frac{m}{2},  \frac{\parallel  G_{\tilde{f}_{k-2}/M}(x^{(k-1)}) - G_{f/M}(x^{(k-1)})  \parallel_2}{\parallel  G_{f/M}(x^{(k-2)})  \parallel_2} \right\}
> \end{align}
> $$
