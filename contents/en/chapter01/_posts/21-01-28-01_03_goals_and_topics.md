---
layout: post
title: 01-03 Goals and Topics
chapter: '01'
order: 4
owner: Kyeongmin Woo
categories:
- chapter01
lang: en
lesson_type: required
---

Knowing the definition of convexity is only the first mile; the real superpower of this course is *recognizing* hidden convexity in applied problems and matching each problem structure to the right algorithm. A naive general-purpose solver might take 10,000 iterations on an image-denoising problem that a tailored ADMM or proximal splitting method solves to high accuracy in 20 iterations.

## Background Knowledge Map: The Three Pillars of Mastering Convex Optimization

- **Recognition & Reformulation (Modeling):** Spotting when a seemingly nonconvex problem (such as fractional programming or $$\ell_1$$-regularized regression) can be transformed into an equivalent LP, QP, SOCP, or SDP.
- **Duality & Optimality Theory:** Using Lagrange duality and KKT conditions to derive analytical optimality certificates, sensitivity analyses, and stopping criteria (duality gaps).
- **Algorithm–Structure Matching:** Selecting among first-order methods (gradient, proximal, coordinate descent), operator splitting (ADMM), and second-order interior-point methods based on dimension $$n$$, smoothness, and desired accuracy.
- **Practical Trade-Offs:** Balancing per-iteration cost (cheap matrix-vector products vs. expensive linear solves) against iteration count and wall-clock time.

### Step-by-Step Worked Example (Read Slowly): 1D Total Variation (TV) Denoising by Hand

Consider a 3-pixel noisy signal $$y = (0, 0, 3)^T$$ with regularization weight $$\lambda = 1$$:
$$\min_{x \in \mathbb{R}^3} \; F(x) = \frac{1}{2}\left[(x_1 - 0)^2 + (x_2 - 0)^2 + (x_3 - 3)^2\right] + |x_2 - x_1| + |x_3 - x_2|.$$

1. **Test two extremes to build intuition:**
   - No smoothing ($$x = y = (0, 0, 3)^T$$): $$F(y) = 0 + 0 + 3 = 3.0$$.
   - Total flattening ($$x = (1, 1, 1)^T$$): $$F(1,1,1) = \frac{1}{2}(1 + 1 + 4) + 0 = 3.0$$.
2. **Solve for a piecewise-constant jump $$x_1 = x_2 = a < b = x_3$$:**
   With $$x_1 = x_2 = a$$ and $$x_3 = b > a$$, the TV penalty simplifies to $$b - a$$, so
   $$F(a, a, b) = a^2 + \frac{1}{2}(b - 3)^2 + (b - a).$$
3. **Set partial derivatives to zero:**
   $$\frac{\partial F}{\partial a} = 2a - 1 = 0 \implies a^* = 0.5, \qquad \frac{\partial F}{\partial b} = (b - 3) + 1 = 0 \implies b^* = 2.0.$$
4. **Verify strict improvement:** At $$x^* = (0.5, 0.5, 2.0)^T$$, $$a^* < b^*$$ holds and
   $$F(x^*) = \frac{1}{2}(0.25 + 0.25 + 1.0) + (0 + 1.5) = 0.75 + 1.5 = 2.25 < 3.0.$$
   Notice how TV denoising pulls the outlier down from $$3$$ to $$2$$ while preserving a crisp jump edge instead of blurring the signal linearly.

## Goals
The goal of this course is to develop the following abilities:

* Recognize when a given problem is a convex optimization problem
* Formulate a given situation as a convex optimization problem
* Select the most appropriate algorithm to solve a defined convex optimization problem

## Topics
To achieve these goals, the following topics will be covered:

* Convex sets, functions, optimization problems
* Examples and applications
* Algorithms (gradient, proximal, Newton, interior-point, ADMM, …)
* 2026 modern track on this site: SGD / Adam / AdamW (Ch.26), autodiff (Ch.27), nonconvex landscapes (Ch.28), data-parallel SGD and FedAvg (Ch.29)

In particular, the main focus will be on algorithms.

## Algorithms
There are many different methods for solving optimization problems. The performance of each method depends on the properties of the problem being solved. To choose the most efficient algorithm, a deep understanding of both the problem and the algorithms is required. Let's look at an example: total variation denoising.

### Example: Total variation denoising

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/2d_fused_lasso.png" alt="2D Fused Lasso" width="70%">
  <figcaption style="text-align: center;">[Fig1] Total Variation Denoising [3]</figcaption>
</p>
</figure>

Suppose you receive a noisy image (middle), and you want to remove the noise to obtain a solution (right) close to the true image (left). If each pixel value is $$y_i, i = 1, ..., n$$, this problem can be formulated as the following optimization problem, commonly called the 2D fused lasso or 2D total variation denoising problem:

>$$\min_{\theta} \frac{1}{2} \sum_{i=1}^n (y_i - \theta_{i})^2 + \lambda \sum_{(i,j) \in E} \vert \theta_i - \theta_j \vert$$

* E: the set of edges between all neighboring $$\theta$$
* $$\frac{1}{2} \sum_{i=1}^n (y_i - \theta_{i})^2$$: Least squares loss. Forces $$\theta$$ to be close to $$y$$
* $$\sum_{(i,j) \in E} \vert \theta_i - \theta_j \vert$$: Total variation smoothing. Used when the change between neighboring pixels is not large (piecewise constant). Choosing the right smoothing method requires careful consideration of the problem's characteristics. (For more details on total variation smoothing, see Chapter 6.1.2 and 6.3 in Reference 1.)

The convex optimization problem above can be solved using the [Specialized ADMM](http://stanford.edu/~boyd/admm.html) algorithm, which yields the solution on the right after 20 iterations.

### Specialized ADMM, 20 iterations
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/result1.png" alt="Result1" width="50%">
  <figcaption style="text-align: center;">[Fig2] Specialized ADMM Result [3]</figcaption>
</p>
</figure>

### Proximal gradient descent, 1000 iterations
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/result2.png" alt="Result2" width="50%">
  <figcaption style="text-align: center;">[Fig3] Proximal Gradient Descent Result [3]</figcaption>
</p>
</figure>

### Coordinate descent, 10K cycles
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/result3.png" alt="Result3" width="50%">
  <figcaption style="text-align: center;">[Fig4] Coordinate Descent Result [3]</figcaption>
</p>
</figure>

As shown above, for the 2D fused lasso problem, Specialized ADMM performs best among the three methods. However, for other problems, the other two methods may outperform Specialized ADMM. In later chapters, we will analyze various algorithms and problems to learn how to select the most appropriate algorithm — including, after the classical spine, the 2026 modern-track chapters on this site.
