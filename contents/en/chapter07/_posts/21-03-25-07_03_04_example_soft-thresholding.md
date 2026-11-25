---
layout: post
title: '07-03-04 Example: Soft-Thresholding'
chapter: '07'
order: 10
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
---

Take the Lasso problem and simplify the design matrix to the identity $$X = I$$: $$\min_\beta \frac{1}{2}\|y - \beta\|_2^2 + \lambda\|\beta\|_1$$. Not only does subgradient optimality solve this in closed form—it produces one of the most famous building blocks in modern signal processing and convex optimization: the **Soft-Thresholding Operator** $$S_\lambda(y)$$, the exact proximal operator of the $$\ell_1$$ norm that powers ISTA, FISTA, and wavelet denoising.

## Key ideas: Soft-Thresholding and Proximal Sparsity

1. **Complete Coordinate Separability**: When $$X = I$$, the objective splits into $$p$$ independent 1D problems:
   $$\min_{\beta_i \in \mathbb{R}} \quad \frac{1}{2}(y_i - \beta_i)^2 + \lambda |\beta_i|.$$
   We solve each coordinate $$\beta_i^\star$$ independently via $$0 \in (\beta_i - y_i) + \lambda \partial |\beta_i|$$.
2. **Three-Regime Closed-Form Solution**:
   $$S_\lambda(y_i) = \begin{cases} y_i - \lambda & \text{if } y_i > \lambda, \\ 0 & \text{if } |y_i| \le \lambda, \\ y_i + \lambda & \text{if } y_i < -\lambda, \end{cases}$$
   written compactly as $$S_\lambda(y_i) = \operatorname{sign}(y_i)\max(|y_i| - \lambda, 0)$$.
3. **Soft vs. Hard Thresholding**: *Hard* thresholding keeps $$y_i$$ unchanged for $$|y_i| > \lambda$$ and jumps discontinuously to $$0$$ at $$\pm\lambda$$ (nonconvex!). *Soft* thresholding is continuous everywhere—it shrinks surviving entries toward zero by $$\lambda$$, trading a tiny bias for convexity and stability.
4. **Role in Iterative Solvers (ISTA / Proximal Gradient)**: Even when $$X \neq I$$, proximal gradient descent for general Lasso simply alternates one ordinary gradient step $$z = \beta - t X^T(X\beta - y)$$ with one soft-thresholding call $$\beta^+ = S_{t\lambda}(z)$$!

### Worked example: Applying Soft-Thresholding to a Noisy Signal

Denoise the 4-entry signal $$y = (4.5,\; -0.8,\; 1.5,\; -3.2)^T$$ by solving $$\min_\beta \frac{1}{2}\|y - \beta\|_2^2 + \lambda\|\beta\|_1$$ with $$\lambda = 1.5$$.

1. **Coordinate 1 ($$y_1 = 4.5 > 1.5$$)**:
   $$\beta_1^\star = 4.5 - 1.5 = 3.0.$$
   Check optimality: $$y_1 - \beta_1^\star = 1.5 = \lambda \operatorname{sign}(3.0)$$.
2. **Coordinate 2 ($$y_2 = -0.8$$, $$|-0.8| = 0.8 \le 1.5$$)**:
   $$\beta_2^\star = 0.$$
   Check optimality: $$|y_2 - 0| = 0.8 \le 1.5$$ (subgradient $$v_2 = -0.8/1.5 \approx -0.533 \in [-1, 1]$$).
3. **Coordinate 3 ($$y_3 = 1.5$$, right on the boundary $$|1.5| = 1.5$$)**:
   $$\beta_3^\star = 1.5 - 1.5 = 0.$$
   Check optimality: $$|y_3 - 0| = 1.5 \le 1.5$$ (subgradient $$v_3 = +1 \in [-1, 1]$$).
4. **Coordinate 4 ($$y_4 = -3.2 < -1.5$$)**:
   $$\beta_4^\star = -3.2 + 1.5 = -1.7.$$
   Check optimality: $$y_4 - \beta_4^\star = -1.5 = \lambda \operatorname{sign}(-1.7)$$.
5. **Final denoised vector**: $$\beta^\star = (3.0,\; 0,\; 0,\; -1.7)^T$$ — two weak/borderline noise components snapped cleanly to exact zero!

For the simpler lasso problem with $$X=I$$:
>
\begin{equation}
\min_{\beta} \frac{1}{2} \| y-\beta \|_2^2 + \lambda \| \beta \|_1
\end{equation}

From the previous example, the subgradient optimality condition is:
>
$$
\begin{cases}
y_i-\beta_i = \lambda \cdot \text{sign}(\beta_i) &\text{if } \beta_i \neq 0 \\
 |y_i-\beta_i| \leq \lambda &\text{if } \beta_i = 0
\end{cases}
$$

From this condition, the solution $$\beta = S_{\lambda}(y)$$ can be found, where
>
$$
[S_{\lambda}(y)]_{i} = 
\begin{cases}
y_i - \lambda &\text{if }y_i > \lambda \\
0             &\text{if }-\lambda \leq y_i \leq \lambda, \quad \quad i \in \{1,2,\dots,n \} \\
y_i + \lambda &\text{if } y_i < -\lambda
\end{cases}
$$

Here, $$S_{\lambda}$$ is called the soft-thresholding operator.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_03_subgrad-6.png" alt="connection_to_convexity_geometry" width="80%" height="80%">
</p>
 <figcaption style="text-align: center;">$$\text{[Fig 1] Soft-thresholding, y (x-axis), } \beta \text{ (y-axis), } \lambda=1/2 \text{ [3]}$$ </figcaption>
</figure>