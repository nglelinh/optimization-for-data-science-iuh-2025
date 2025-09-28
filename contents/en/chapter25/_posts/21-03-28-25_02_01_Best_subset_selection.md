---
layout: post
title: 25-02-01 Best subset selection
chapter: '25'
order: '8'
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

Best subset selection, one of the representative examples of Integer Programming, is a problem of selecting k entries from $$p$$ entries.

## Best subset selection

When $$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n×p}$$ and $$y \in \mathbb{R}^{n}$$, the best subset selection problem is as follows:

>$$
>\begin{align}
>\min_{\beta} & \quad \frac{1}{2} \| y - X\beta \|^{2} \\
>\text{subject to } & \quad \| \beta \|_{0} \leq k \\
>\end{align}
>$$

Here, $$\| \beta \|_{0}$$ is the number of nonzero entries in $$\beta$$. Previously in earlier chapters, we defined this type of problem as a Lasso problem and made $$\beta$$ sparse using the $$l_1$$ norm. In this problem, it is defined as a problem that constrains the number of non-zero entries using the $$l_0$$ norm, but since the constraint condition $$\| \beta \|_{0} \leq k$$ is non-convex, the problem cannot be solved with the convex optimization techniques we have learned so far.

### Integer programming formulation

Then let's reformulate this problem with Integer programming.

>$$
>\begin{align}
>\min_{\beta, z} & \quad \frac{1}{2} \| y - X\beta \|^{2} \\
>\text{subject to } & \quad |\beta_{i}| \leq M_{i} \cdot z_{i} \quad i = 1, \dotsc, p \\
>& \quad \sum_{i = 1}^{p} z_{i} \leq k \\
>& \quad z_{i} \in \{0, 1\} \quad i = 1, \dotsc, p \\
>\end{align}
>$$

By introducing binary variables $$z_i$$ and making the sum of $$z_i$$ less than $$k$$, we made the above problem equivalent to the original problem. $$M_i$$ is a value that bounds $$|\beta_{i}|$$ known in advance, which can be computed from preprocessing $$X$$ and $$y$$. Now that we have defined the problem as Integer Programming, we can solve it using Integer Programming techniques.

## A clever way to get good feasible solutions

Let's generalize the problem and explain the algorithm. Let's say the objective function $$g : \mathbb{R}^{p} \to \mathbb{R}$$ is smooth and convex, and $$\nabla g$$ is L-Lipschitz.

>$$\min_{\beta} g(\beta) \quad \text{subject to} \quad \| \beta \|_{0} \le k$$

In the case of best subset selection, $$g(\beta) = \frac{1}{2} \| X\beta - y \|^2_2$$.

### Observation

Through the function $$H_k(u)$$ defined as follows, we can obtain the k largest entries from $$u \in \mathbb{R}^p$$.

>$$H_k(u) = \underset{\beta : \| \beta \|_{0} \le k}{\text{argmin}} \| \beta - u \|^2_2$$

Here, the function $$H_k(u)$$ is hard thresholding. Also, it can be seen as projecting $$u$$ onto the set $$\beta$$.

### Discrete first-order algorithm

Now let's define an algorithm using gradient descent and the function $$H_k(u)$$.

1. Start with $$\beta^{(0)}$$
2. for $$k = 0, 1, ..$$
   - $$\beta^{(i+1)} = H_k \left(\beta^{(i)} - \frac{1}{L} \nabla g(\beta^{(i)})\right)$$
   - end for

By iterating the above process, we converge to $$\beta^{(i)} \to \bar{\beta}$$. This can be called a local solution to the above minimization problem.

>$$\bar{\beta} = H_k \left(\bar{\beta} - \frac{1}{L} \nabla g(\bar{\beta})\right)$$

As a result, the algorithm can be seen as a proximal gradient algorithm. This is because the function $$H_k(u)$$ plays the role of a proximal operator.

## Computational results

### Mixed integer programming gap

Let's look at the experimental results of the subset selection problem in the figure below. In the left graph, the upper bound becomes optimal, while the lower bound slowly rises and meets the upper bound, at which point we know it is optimal. This is because there is no method to check whether the solution is optimal in linear programming, and we can know it is optimal when the upper bound and lower bound become equal. (For reference, the difference between the upper bound and lower bound is called the mixed integer programming gap.)

The right figure shows the same experimental results, showing how the mixed integer programming gap decreases. The orange graph represents the mixed integer programming gap, which is the difference between the upper bound and lower bound, and it gradually decreases.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_03_subset_results1.png" alt="[Fig1] Dataset n=350, p = 64, k=6 [3]">
  <figcaption style="text-align: center;">[Fig1] Dataset n=350, p = 64, k=6 [3]</figcaption>
</p>
</figure>

### Cold and Warm Starts

The next figure shows that warm start performs much better overall than cold start.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_04_subset_results2.png" alt="[Fig2] Cold and Warm Starts [3]">
  <figcaption style="text-align: center;">[Fig2] Cold and Warm Starts [3]</figcaption>
</p>
</figure>

### Sparsity Detection

The next figure compares the sparsity of MIP (Mixed Integer Programming), Lasso, Step regression, and Sparsenet. As a result, we can see that MIP produces the most sparse results.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_05_subset_results3.png" alt="[Fig3] Sparsity Detection (synthetic database) [3]">
  <figcaption style="text-align: center;">[Fig3] Sparsity Detection (synthetic database) [3]</figcaption>
</p>
</figure>