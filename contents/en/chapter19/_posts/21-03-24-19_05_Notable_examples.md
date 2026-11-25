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

Two of the most widely downloaded statistical software packages in history—**glmnet** (for $$\ell_1$$-penalized generalized linear models) and **QUIC** (for sparse inverse covariance estimation, or Graphical Lasso)—are not mysterious black boxes; both are pure, textbook instances of **Proximal Newton** paired with fast coordinate descent for the inner quadratic subproblem! Seeing how each one builds its local quadratic model reveals why proximal Newton crushed first-order competitors on real statistical benchmarks.

## Key ideas: Inside `glmnet` and `QUIC`

- **IRLS Meets Lasso (`glmnet`):** For $$\ell_1$$-penalized logistic regression, the second-order Taylor expansion of the negative log-likelihood around $$\beta^k$$ is literally a *weighted least-squares* (Lasso) objective with diagonal weights $$W_{ii} = p_i(1 - p_i)$$, solved rapidly by warm-started cyclic coordinate descent.
- **Matrix-Valued Proximal Newton (`QUIC`):** Graphical Lasso minimizes $$-\log\det\Theta + \operatorname{tr}(S\Theta) + \lambda\|\Theta\|_1$$ over $$\Theta \succ 0$$. Its Hessian is the Kronecker operator $$\Theta^{-1} \otimes \Theta^{-1}$$; QUIC exploits Cholesky factors $$W = \Theta^{-1}$$ to run coordinate descent on the free active set of off-diagonal entries without ever forming the $$p^2 \times p^2$$ Hessian!
- **Active-Set Shrinking:** In both `glmnet` and `QUIC`, KKT conditions identify coordinates that are guaranteed to remain zero (the "fixed set"), allowing coordinate descent to work solely on the tiny free set of nonzero parameters.
- **Why PN Beats FISTA & SpaRSA on Logistic Lasso:** When the data matrix $$X$$ is large or correlated, FISTA must recompute full exponentials $$e^{X\beta}$$ hundreds of times; `glmnet` evaluates exponentials only a handful of outer Newton iterations while letting cheap linear coordinate updates do the heavy lifting.

### Worked example: One `glmnet` Outer Iteration for $$\ell_1$$ Logistic Regression

Consider 1D $$\ell_1$$-penalized logistic regression with $$\lambda = 0.2$$ on two data points $$(a_1, y_1) = (1, 1)$$ and $$(a_2, y_2) = (-1, 0)$$:
$$f(\beta) = \underbrace{\sum_{i=1}^2 \Big[\log(1 + e^{a_i \beta}) - y_i a_i \beta\Big]}_{g(\beta)} + \underbrace{0.2|\beta|}_{h(\beta)}.$$

1. **Evaluate probabilities, gradient, and Hessian at $$\beta^0 = 0$$:**
   - Predicted probabilities: $$p_1 = p_2 = \frac{1}{1 + e^0} = 0.5$$.
   - IRLS weights: $$w_1 = w_2 = p_i(1 - p_i) = 0.25$$.
   - Gradient: $$g'(0) = (p_1 - y_1)a_1 + (p_2 - y_2)a_2 = (0.5 - 1)(1) + (0.5 - 0)(-1) = -1.0$$.
   - Hessian: $$H(0) = w_1 a_1^2 + w_2 a_2^2 = 0.25(1) + 0.25(1) = 0.5$$.
2. **Form the `glmnet` inner weighted-Lasso subproblem:**
   $$v^{(1)} = \arg\min_v \; g'(0) v + \frac{1}{2} H(0) v^2 + 0.2|0 + v| = \arg\min_v \; -v + 0.25 v^2 + 0.2|v|.$$
3. **Solve via soft-thresholding:**
   For $$v > 0$$, $$-1 + 0.5v + 0.2 = 0 \implies v^{(1)} = \frac{0.8}{0.5} = +1.6$$.
4. **Verify decrease at $$\beta^1 = 1.6$$:**
   - $$f(0) = 2\ln 2 \approx 1.3863$$.
   - $$f(1.6) = 2\ln(1 + e^{-1.6}) + 0.2(1.6) \approx 2(0.1839) + 0.32 = 0.6878 < 1.3863$$ $$\checkmark$$!
   (Exact optimum is $$\beta^\star = \ln(9) \approx 2.1972$$ with $$f(\beta^\star) \approx 0.6502$$—just one `glmnet` step captured $$95\%$$ of the total objective reduction!)

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
