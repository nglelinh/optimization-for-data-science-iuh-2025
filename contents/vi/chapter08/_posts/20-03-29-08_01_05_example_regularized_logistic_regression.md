---
layout: post
title: '08-01-05 Example: Regularized Logistic Regression'
chapter: '08'
order: 7
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Suppose $$(x_i, y_i) \in \mathbb{R}^p \times \{0, 1\}$$ for $$i=1,...,n$$. The logistic regression loss is defined as:
>
\begin{align}
f(\beta) = \sum_{i=1}^n\big(-y_ix_i^T\beta + \log(1+\exp(x_i^T\beta))\big)
\end{align}

This function is a finite sum of a linear function and a log-sum-exp function, so it is a differentiable convex function.

Now, the regularization problem for $$\beta$$ is formulated as:

>
\begin{align}
\min_{\beta} \text{ } f(\beta) + \lambda \cdot P(\beta)
\end{align}

Here, $$P(\beta)$$ can be defined as $$\Vert \beta \Vert _2^2$$ (ridge penalty) or $$\Vert \beta \Vert _1$$ (lasso penalty).

The loss function with ridge penalty remains a differentiable convex function, but the loss function with lasso penalty becomes a nondifferentiable convex function. For these two loss functions, we can apply gradient descent for ridge and the subgradient method for lasso, and by plotting the objective function value at iteration $$k$$, we can observe the convergence characteristics of both methods.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter08/08_01_grad_vs_subgrad.png" alt="grad_vs_subgrad" width="90%" height="90%">
</p>
  <figcaption style="text-align: center;">[Fig 1] Gradient descent vs Subgradient method [3]</figcaption>
</figure>

This experiment shows that gradient descent converges much faster than the subgradient method.
