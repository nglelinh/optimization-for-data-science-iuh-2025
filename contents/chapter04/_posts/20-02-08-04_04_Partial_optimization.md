---
layout: post
title: 04-04 Partial optimization
chapter: "04"
order: 5
owner: "YoungJae Choung"
---
[Reminder: ]({% post_url contents/chapter03/21-02-12-03_02_operations_that_preserve_convexity %})
If $$C$$ is a convex set and $$f$$ is convex in $$(x,y)$$, then $$g(x) = \min_{y \in C} f(x, y)$$ is convex in $$x$$.

Thus, partial optimization in a convex problem constructed with multivariate functions preserves convexity.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter04/partial-optimization.png" alt="[Fig1] partial optimization of a convex problem [3]">
  <figcaption style="text-align: center;">[Fig1] partial optimization of a convex problem [3]</figcaption>
</p>
</figure>
<br>

#### Example: hinge form of SVMs
For a non-separable set, the SVM problem is defined as:
>$$
\begin{aligned}
&\min_{\beta, \beta_{0}, \xi} &&\frac{1}{2}\|\beta\|_2^2 + C \sum_{i=1}^{n} \xi_{i} \\
&\text{subject to} &&{\xi}_{i} \ge 0, \\ 
&&&y_{i}(x_{i}^T \beta + \beta_{0}) \ge 1 - {\xi}_{i}, \\
&&&i = 1, .., n \\
\end{aligned}
$$

The above constraints can be expressed as a single constraint:
> $$
\begin{aligned}
{\xi}_{i} \ge \max\{0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})\} \\
\end{aligned}
$$

In this case, $$\max\{0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})\}$$ is the minimum value for $$\xi_{i}$$, and we can define $$\tilde{f}$$ as:

> $$
\begin{aligned}
\frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} {\xi}_{i} &\ge \frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} \max({0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})})\\
&= \min\{\frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} \xi_{i} \quad | \quad \xi_{i} \ge 0, \ y_{i}(x_{i}^T \beta + \beta_{0}) \ge 1 - \xi_{i}, \ i = 1, .., n\} \\
&= \tilde{f}(\beta, \beta_{0}) \\
\end{aligned}
$$


By using the simplified $$\tilde{f}$$ as the objective function, a more straightforward solution can be obtained. In the given problem, $$\xi$$ has been eliminated, and it has also been transformed from a constrained problem to an unconstrained problem.

>$$
\begin{aligned}
\min_{\beta, \beta_0} \frac{1}{2} \|\beta\|_2^2 + C \sum_{i=1}^{n} \max\{0, 1 - y_{i} (x_{i}^{T} \beta + \beta_{0}) \}
\end{aligned}
$$
