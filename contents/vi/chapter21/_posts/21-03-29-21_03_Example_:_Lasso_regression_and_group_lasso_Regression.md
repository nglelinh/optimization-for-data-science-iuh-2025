---
layout: post
title: 21-03 Example - Lasso regression and group lasso Regression
chapter: '21'
order: 4
owner: Hooncheol Shin
categories:
- chapter21
lang: vi
---

## Lasso regression
Let's solve the Lasso regression problem using ADMM.

Given $$y\in \mathbb{R}^{n}, X\in \mathbb{R}^{n\times p}$$, the Lasso problem is:
>$$
>\begin{align}
>\min_{\beta}\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda||\beta||_{1}
>\end{align}
>$$

In previous chapters, we have solved the Lasso problem using various methods, including [proximal gradient descent (ISTA)]({% multilang_post_url contents/chapter09/20-01-08-09_01_proximal_gradient_descent %}), [accelerated proximal gradient descent (FISTA)]({% multilang_post_url contents/chapter09/20-01-08-09_05_03_example_FISTA %}), [barrier method]({% multilang_post_url contents/chapter15/21-03-28-15_barrier_method %}), and [primal-dual interior-point method]({% multilang_post_url contents/chapter17/21-05-01-17_primal_dual_interior_point_method %}). 

As with deriving the dual formulation, the performance of the ADMM algorithm depends on how we set up the auxiliary variables. Among many ways to set auxiliary variables, the following form is known to be one of the most effective:
>$$
>\begin{align}
>&\min_{\beta, \alpha} &&||y-X\beta||^{2}_{2}+\lambda||\alpha||_{1}\\\\
>&\text{subject to} &&\beta-\alpha= 0.
>\end{align}
>$$

## ADMM Updates

The ADMM updates for this formulation are derived as follows. The $$\beta$$ update involves a quadratic function, so we can find the minimum by differentiation. The $$\alpha$$ update is similar to the problem covered in [Chapter 7 (07-03-04)]({% multilang_post_url contents/chapter07/21-03-25-07_03_04_example_soft-thresholding %}), which has a soft-thresholding solution.
>$$
>\begin{align}
>\beta^{+} &= \underset{\beta}{\operatorname{argmin}}\frac{1}{2}||y-X\beta||^{2}_{2}+\frac{\rho}{2}||\beta-\alpha+w||^{2}_{2}\\\\
>&= (X^{T}X+\rho I)^{-1}(X^{T}y+\rho (\alpha-w))\\\\
>\alpha^{+} &= \underset{\alpha}{\operatorname{argmin}}\lambda||\alpha||_{1}+\frac{\rho}{2}||\beta^{+}-\alpha+w||^{2}_{2}\\\\
>&= S_{\frac{\lambda}{\rho}}(\beta^{+}+w)\\\\
>w^{+} &=w+\beta^{+}-\alpha^{+}
>\end{align}
>$$

## Key Properties

This result has the following characteristics:

* The matrix $$X^{T}X+\rho I$$ is always invertible regardless of $$X$$ since $$\rho>0$$.
* If we precompute the factorization (typically Cholesky factorization) in $$O(p^{3})$$ flops, then the $$\beta$$ update takes $$O(p^{2})$$ flops.
* The $$\alpha$$ update applies the soft-thresholding operator $$S_{t}$$, which is identical to the content in [07-03-04]({% multilang_post_url contents/chapter07/21-03-25-07_03_04_example_soft-thresholding %}).
* The ADMM steps are "almost" equivalent to repeatedly soft-thresholding ridge regression coefficients.
* Different values of $$\rho$$ produce different results.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/lasso.png" alt="[Fig 1] Comparison of various algorithms for lasso regression (50 instances with n = 100, p = 20) [3]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Comparison of various algorithms for lasso regression (50 instances with n = 100, p = 20) [3]</figcaption>
</p>
</figure>


## Performance Comparison

[Fig 1] compares the convergence of various algorithms for the Lasso regression problem. All algorithms have the same computational complexity per iteration. As can be seen from the convergence speed in the graph, ADMM has similar convergence speed to proximal gradient descent (black). Accelerated proximal gradient descent (red) has "Nesterov ripples" but shows slightly faster convergence speed. We can also confirm that ADMM shows different convergence speeds according to the $$\rho$$ value. Coordinate descent (green), which will be discussed later in [Chapter 23]({% multilang_post_url contents/chapter23/21-03-28-23_Coordinate_Descent %}), uses more information about the problem and therefore has faster convergence speed compared to other methods. The disadvantage of coordinate descent is that there are conditions required for its application.

If the $$\rho$$ value is set too large, the weight of minimizing the objective function $$f+g$$ becomes small, and if the $$\rho$$ value is set too small, feasibility decreases. Therefore, setting an appropriate $$\rho$$ value is important. For detailed information, see [BPCPE] discussed in the [Chapter 21 reference papers]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %}).

## Group Lasso Regression

Similarly, let's examine solving the Group Lasso regression problem with ADMM. The Group Lasso regression problem is defined as follows for $$y\in \mathbb{R}^{n}, X\in \mathbb{R}^{n \times p}$$:

>$$
>\begin{align}
>\min_{\beta}\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda\sum^{G}_{g=1} c_{g}||\beta_{(g)}||_{2}.
>\end{align}
>$$

As with Lasso regression, we can reformulate the problem:
>$$
>\begin{align}
>&\min_{\beta,\alpha} &&\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda\sum^{G}_{g=1} c_{g}||\alpha_{(g)}||_{2}\\\\
>&\text{subject to} &&\beta-\alpha=0.
>\end{align}
>$$

The ADMM steps are as follows:
>$$
>\begin{align}
>\beta^{+} &= (X^{T}X+\rho I)^{-1}(X^{T}y+\rho (\alpha-w))\\\\
>\alpha^{+} &= R_{c_{g}\frac{\lambda}{\rho}}(\beta^{+}_{(g)}+w_{(g)})\qquad \text{g = 1,...G}\\\\
>w^{+} &=w+\beta^{+}-\alpha^{+}
>\end{align}
>$$

## Properties of Group Lasso ADMM

This result has the following characteristics:

* The matrix $$X^{T}X+\rho I$$ is always invertible regardless of $$X$$ since $$\rho>0$$.
* If we precompute the factorization (typically Cholesky factorization) in $$O(p^{3})$$ flops, then the $$\beta$$ update takes $$O(p^{2})$$ flops.
* The $$\alpha$$ update applies the group soft-thresholding operator $$R_{t}$$, which is defined as follows:

>\begin{align}
>R_{t}(x) = (1-\frac{x}{\lVert x \rVert_{2}})_{+}x
>\end{align}

