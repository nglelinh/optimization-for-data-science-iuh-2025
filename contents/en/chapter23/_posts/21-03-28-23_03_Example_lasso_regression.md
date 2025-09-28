---
layout: post
title: 23-03 Example: lasso regression
chapter: '23'
order: '4'
owner: YoungJae Choung
categories:
- chapter23
lang: en
---

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