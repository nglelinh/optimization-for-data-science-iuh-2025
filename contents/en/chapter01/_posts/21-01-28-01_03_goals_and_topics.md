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

## Goals
The goal of this course is to develop the following abilities:

* Recognize when a given problem is a convex optimization problem
* Formulate a given situation as a convex optimization problem
* Select the most appropriate algorithm to solve a defined convex optimization problem

## Topics
To achieve these goals, the following topics will be covered:

* Convex sets, functions, optimization problems
* Examples and applications
* Algorithms

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

As shown above, for the 2D fused lasso problem, Specialized ADMM performs best among the three methods. However, for other problems, the other two methods may outperform Specialized ADMM. In later chapters, we will analyze various algorithms and problems to learn how to select the most appropriate algorithm.
