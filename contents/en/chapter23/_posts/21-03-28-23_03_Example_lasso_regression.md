---
layout: post
title: 23-03 Example - lasso regression
chapter: '23'
order: '4'
owner: YoungJae Choung
categories:
- chapter23
lang: en
---

When Robert Tibshirani introduced the Lasso in 1996, it was initially solved with generic quadratic programming—painfully slow once $$p$$ grew beyond a few hundred features. Everything changed when statisticians realized that the $$\ell_1$$ penalty $$\lambda \|\beta\|_1 = \lambda \sum_{i=1}^p |\beta_i|$$ is *perfectly separable* across coordinates. That single property turns every 1D coordinate subproblem into a closed-form soft-thresholding formula, allowing Coordinate Descent to solve Lasso problems with tens of thousands of predictors in milliseconds.

## Background Knowledge Map: Soft-Thresholding and Coordinate Descent for Lasso

- **Separable Composite Structure:** The Lasso objective $$\frac{1}{2}\|y - X\beta\|_2^2 + \lambda \sum_{i=1}^p |\beta_i|$$ satisfies Tseng’s theorem exactly: the smooth data-fidelity term is convex and differentiable, and the nonsmooth $$\ell_1$$ norm splits cleanly by coordinate.
- **1D Subgradient Optimality & Soft-Thresholding:** Setting $$0 \in -X_i^\top(r^{(-i)} - X_i \beta_i) + \lambda \partial |\beta_i|$$ yields the exact closed-form update $$\beta_i^+ = \frac{S_\lambda(X_i^\top r^{(-i)})}{\|X_i\|_2^2}$$, where $$S_\lambda(z) = \operatorname{sign}(z)\max(|z| - \lambda, 0)$$.
- **Automatic Zero-Locking (Sparsity):** Whenever the correlation $$|X_i^\top r^{(-i)}| \le \lambda$$, soft-thresholding snaps $$\beta_i^+$$ to *exact* zero—requiring no residual update ($$0$$ flops!) and accelerating sweeps dramatically once most features drop out.
- **Empirical Dominance Over Proximal Gradient:** Just as in OLS, one CD sweep matches one Proximal Gradient (ISTA/FISTA) step in $$O(np)$$ cost, yet CD’s Gauss–Seidel updates and per-coordinate scaling typically converge in a fraction of the iterations.

### Step-by-Step Worked Example (Read Slowly): One Coordinate Descent Cycle on a 2-Feature Lasso

Use the same design matrix $$X = \begin{pmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix}$$ ($$\|X_1\|_2^2 = \|X_2\|_2^2 = 2$$) and response $$y = (3, 1, 2)^\top$$, now with Lasso penalty $$\lambda = 2$$, starting at $$\beta^{(0)} = (0, 0)^\top$$ and $$r = (3, 1, 2)^\top$$.

1. **Update $$\beta_1$$:**
   - Correlation with partial residual: $$c_1 = X_1^\top r^{(-1)} = 1(3) + 1(1) + 0(2) = 4$$.
   - Soft-threshold by $$\lambda = 2$$: $$S_2(4) = \operatorname{sign}(4)\max(4 - 2, 0) = 2$$.
   - Divide by $$\|X_1\|_2^2 = 2$$: $$\beta_1^{(1)} = \frac{2}{2} = 1$$.
   - Refresh residual: $$r \leftarrow (3, 1, 2)^\top - 1(1, 1, 0)^\top = (2, 0, 2)^\top$$.
2. **Update $$\beta_2$$:**
   - Correlation with partial residual: $$c_2 = X_2^\top r^{(-2)} = 1(2) + 0(0) + 1(2) = 4$$.
   - Soft-threshold by $$\lambda = 2$$: $$S_2(4) = 2$$.
   - Divide by $$\|X_2\|_2^2 = 2$$: $$\beta_2^{(1)} = \frac{2}{2} = 1$$.
   - Refresh residual: $$r \leftarrow (2, 0, 2)^\top - 1(1, 0, 1)^\top = (1, 0, 1)^\top$$.
3. **Check KKT optimality at $$\beta^{(1)} = (1, 1)^\top$$:**
   - $$X_1^\top r = 1(1) + 1(0) + 0(1) = 1$$. Wait—for $$\beta_1 = 1 > 0$$, KKT requires $$X_1^\top r = \lambda = 2$$! Since $$1 < 2$$, $$\beta_1$$ will shrink on Cycle 2.
   - **Cycle 2, coordinate 1:** $$r^{(-1)} = r + 1\cdot X_1 = (2, 1, 1)^\top$$, so $$c_1 = X_1^\top r^{(-1)} = 3$$, giving $$\beta_1^{(2)} = \frac{S_2(3)}{2} = 0.5$$ and $$r \leftarrow (1.5, 0.5, 1)^\top$$.
   - **Cycle 2, coordinate 2:** $$r^{(-2)} = r + 1\cdot X_2 = (2.5, 0.5, 2)^\top$$, so $$c_2 = X_2^\top r^{(-2)} = 4.5$$, giving $$\beta_2^{(2)} = \frac{S_2(4.5)}{2} = 1.25$$ and $$r \leftarrow (1.25, 0.5, 0.75)^\top$$.
   Notice how the Lasso penalty shrinks the weaker feature $$\beta_1$$ while preserving the stronger signal $$\beta_2$$.

Let's examine the lasso regression problem, which has the form of an objective function with separated smooth and nonsmooth parts as follows.

>$$
>\min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2 + \lambda \|\beta\|_1
>$$

**Note:** $$\|\beta\|_1 = \sum_{i=1}^p | \beta_i |$$

When $$\beta_j, j \neq i$$ are fixed values, let's find $$\beta_i$$ that minimizes the given objective function.

$$
\begin{align}
&0 = \nabla_i f(\beta) = X_i^T X_i \beta_i + X_i^T(X_{-i} \beta_{-i} - y) + \lambda s_i,\\\\
&\text{where } s_i \in \partial |\beta_i| \Rightarrow \beta_i = S_{\lambda / \|X_i\|_2^2} \big( \frac{X_i^T(y-X_{-i} \beta_{-i})}{X_i^TX_i} \big)
\end{align}
$$

The solution equals a soft-thresholding function with thresholding level $$\lambda / \|X_i\|_2^2$$.

Through coordinate descent, we iteratively update $$\beta_i$$ for $$i=1,2,\dots,p,1,2,\dots$$.

## Experiment: convergence speed comparison - PG vs AGD vs CD

The graph below shows a comparison of convergence speeds for proximal gradient descent, accelerated gradient descent, and coordinate descent on a lasso regression problem with $$n=100, p=20$$. (The x-axis indicates one step (PD, AGD) or one cycle (CD).)

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/pd_vs_agd_vs_cd.png" alt="[Fig1] PD vs AGD vs CD [3]">
  <figcaption style="text-align: center;">[Fig1] PD vs AGD vs CD [3]</figcaption>
</p>
</figure>

<br><br>

As in the [linear regression case]({% multilang_post_url contents/chapter23/21-03-28-23_02_Example_linear_regression %}), coordinate descent shows superior convergence speed in the lasso regression problem. (It utilizes more information than first-order methods.)

* **Note:** In the above experiment, all methods show $$O(np)$$ flops time complexity per iteration.