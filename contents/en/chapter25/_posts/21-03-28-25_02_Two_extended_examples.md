---
layout: post
title: 25-02 Two extended examples
chapter: '25'
order: 7
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

For decades, statisticians treated exact $$\ell_0$$ subset selection and breakdown-proof Least Median of Squares regression as mathematically ideal but computationally untouchable—forcing everyone to settle for convex surrogates like Lasso or Huber loss. The two extended case studies in this section overturn that folklore. By combining modern MIP formulations with warm starts from continuous first-order optimization, we can now solve both classical statistical NP-hard problems to certified global optimality (or tight provable MIP gaps) on real datasets.

## Background Knowledge Map: Bridging Statistical Estimation and Modern MIP

- **Exact Combinatorial Regularization (Best Subset Selection):** Instead of shrinking coefficients via $$\ell_1$$ (Lasso), binary indicators $$z_j \in \{0, 1\}$$ enforce $$\|\beta\|_0 \le k$$ directly—eliminating shrinkage bias on truly active predictors.
- **High-Breakdown Robustness (Least Median / Quantile of Squares):** Minimizing the $$q$$-th smallest squared residual resists up to nearly $$50\%$$ adversarial outliers, unlike OLS (0% breakdown) or even $$\ell_1$$ regression under leverage points.
- **Discrete First-Order Warm Starts:** Projected gradient descent onto the nonconvex $$k$$-sparse set (iterative hard thresholding) runs in milliseconds and hands the MIP solver a high-quality primal incumbent $$U$$ before Branch and Cut even starts.
- **Certified Optimality Gaps:** Even when proving exact $$0\%$$ optimality takes longer on noisy $$p \gg n$$ datasets, the MIP dual bound immediately tells the statistician how close the warm-start solution is to the unattainable global optimum.

### Step-by-Step Worked Example (Read Slowly): Contrasting $$\ell_0$$ Exact Selection vs. $$\ell_1$$ Shrinkage on 2 Features

Suppose $$X = I_2$$ (two orthonormal features) and $$y = (3, 1)^\top$$, so minimizing $$\frac{1}{2}\|y - \beta\|_2^2$$ gives OLS $$\hat{\beta}_{\text{OLS}} = (3, 1)^\top$$. We want a **1-sparse** model ($$k = 1$$).

1. **Exact Best Subset Selection ($$\|\beta\|_0 \le 1$$):**
   - Keeping only $$\beta_1$$: $$\hat{\beta} = (3, 0)^\top$$, squared error $$\frac{1}{2}(0^2 + 1^2) = 0.5$$.
   - Keeping only $$\beta_2$$: $$\hat{\beta} = (0, 1)^\top$$, squared error $$\frac{1}{2}(3^2 + 0^2) = 4.5$$.
   - Optimal exact 1-sparse estimate: $$\hat{\beta}_{\text{BSS}} = (3, 0)^\top$$—zero bias on the active feature!
2. **Lasso ($$\ell_1$$ surrogate) tuned to be 1-sparse:**
   - To zero out $$\beta_2 = 1$$, we must set $$\lambda \ge 1$$.
   - At $$\lambda = 1$$, soft-thresholding yields $$\hat{\beta}_{\text{Lasso}} = (S_1(3), S_1(1))^\top = (2, 0)^\top$$, which shrinks the true signal from $$3$$ down to $$2$$ (squared error $$\frac{1}{2}(1^2 + 1^2) = 1.0$$—double the error of BSS!).
3. **Insight:** This exact bias–sparsity gap is why Bertsimas, King, and Mazumder (2016) revived MIP for Best Subset Selection.

In this section, we will present two examples of Mixed Integer Programming.

* Best subset selection
* Least mean squares