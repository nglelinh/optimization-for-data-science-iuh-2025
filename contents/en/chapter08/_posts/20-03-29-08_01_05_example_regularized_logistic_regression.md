---
layout: post
title: '08-01-05 Example: Regularized Logistic Regression'
chapter: '08'
order: 7
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

In modern high-dimensional statistics—from predicting disease risk from 50,000 genetic markers to scoring ad clicks across millions of sparse features—plain logistic regression quickly overfits. Adding an $$\ell_1$$ penalty $$\lambda \|\beta\|_1$$ simultaneously regularizes the model and drives irrelevant coefficients to exact zero, turning classification into automatic feature selection. Because $$\|\beta\|_1$$ has sharp creases along every coordinate axis, smooth gradient descent can no longer be applied directly—making $$\ell_1$$-regularized logistic regression a classic proving ground for the subgradient method.

## Key ideas: Anatomy of $$\ell_1$$-Regularized Logistic Regression

- **Pillar 1 — Smooth Log-Loss (Negative Log-Likelihood):** The data-fidelity term $$f(\beta) = \sum_{i=1}^n (-y_i x_i^\top \beta + \log(1 + e^{x_i^\top \beta}))$$ is convex and infinitely differentiable, with gradient $$\nabla f(\beta) = \sum_{i=1}^n (p_i(\beta) - y_i) x_i$$, where $$p_i(\beta) = \frac{1}{1 + e^{-x_i^\top \beta}}$$ is the predicted probability.
- **Pillar 2 — Nonsmooth Sparsity Inducer ($$\lambda \|\beta\|_1$$):** The $$\ell_1$$ norm has subdifferential $$\partial \|\beta\|_1 = \{ v \in \mathbb{R}^p : v_j = \operatorname{sign}(\beta_j) \text{ if } \beta_j \neq 0,\; v_j \in [-1, 1] \text{ if } \beta_j = 0 \}$$. By additivity of subdifferentials, $$\partial(f + \lambda \|\cdot\|_1)(\beta) = \nabla f(\beta) + \lambda \partial \|\beta\|_1$$.
- **Pillar 3 — Why Subgradient Struggles to Produce Exact Zeros:** Unlike proximal soft-thresholding (Chapter 09), a raw subgradient step $$\beta^{(k)} = \beta^{(k-1)} - t_k(\nabla f(\beta^{(k-1)}) + \lambda v^{(k-1)})$$ rarely lands *exactly* on $$\beta_j = 0$$; instead, inactive coordinates jitter back and forth around zero at amplitude $$O(t_k \lambda)$$.
- **Pillar 4 — Lipschitz Constant of the Composite Objective:** Because $$|p_i(\beta) - y_i| \le 1$$, the smooth gradient is globally bounded by $$\sum_{i=1}^n \|x_i\|_2$$, and every subgradient of $$\lambda \|\beta\|_1$$ has norm at most $$\lambda \sqrt{p}$$. Thus the entire objective is globally $$G$$-Lipschitz with $$G \le \sum_{i=1}^n \|x_i\|_2 + \lambda\sqrt{p}$$.

### Worked example: One Subgradient Update on a 2-Sample Logistic Model

Consider $$n = 2$$ data points in $$\mathbb{R}^2$$: $$(x_1, y_1) = ((1, 0)^\top, 1)$$ and $$(x_2, y_2) = ((0, 1)^\top, 0)$$, with regularization $$\lambda = 0.5$$ and objective $$F(\beta) = \sum_{i=1}^2 (-y_i x_i^\top \beta + \log(1 + e^{x_i^\top \beta})) + 0.5(|\beta_1| + |\beta_2|)$$.

1. **Initialize at $$\beta^{(0)} = (0, 0)^\top$$:**
   - Linear predictors: $$x_1^\top \beta^{(0)} = 0$$, $$x_2^\top \beta^{(0)} = 0$$.
   - Predicted probabilities: $$p_1 = p_2 = \frac{1}{1 + e^0} = 0.5$$.
   - Initial objective: $$F(0, 0) = 2\log(2) + 0 \approx 1.3863$$.
2. **Compute the smooth gradient $$\nabla f(\beta^{(0)})$$:**
   $$\nabla f(0, 0) = (0.5 - 1)\begin{pmatrix}1\\0\end{pmatrix} + (0.5 - 0)\begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}-0.5 \\ 0.5\end{pmatrix}.$$
3. **Choose a subgradient of $$\lambda \|\beta\|_1$$ at $$\beta^{(0)} = (0, 0)^\top$$:**
   Any $$v \in [-1, 1]^2$$ is valid. Notice that choosing $$v = (1, -1)^\top$$ gives $$\nabla f(0,0) + 0.5 v = (-0.5, 0.5)^\top + (0.5, -0.5)^\top = (0, 0)^\top$$!
4. **Pause and notice the optimality miracle:** Because $$0 \in \partial F(0, 0)$$, $$\beta^\star = (0, 0)^\top$$ is *already* the exact global minimizer when $$\lambda = 0.5$$!
5. **What if we carelessly picked $$v = (0, 0)^\top \in \partial \|\beta^{(0)}\|_1$$?** With step size $$t_1 = 0.2$$, we would move to $$\beta^{(1)} = (0, 0) - 0.2(-0.5, 0.5) = (0.1, -0.1)$$, where $$F(0.1, -0.1) = (-0.1 + \log(1+e^{0.1})) + \log(1+e^{-0.1}) + 0.5(0.2) \approx 0.6444 + 0.6444 + 0.1 = 1.3888 > 1.3863$$. This demonstrates both how subgradient choice matters at kinks and why proximal methods are preferred for exact sparsity.

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
