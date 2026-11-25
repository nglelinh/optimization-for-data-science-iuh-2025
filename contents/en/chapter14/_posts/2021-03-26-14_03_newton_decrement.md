---
layout: post
title: 14-03 Newton decrement
chapter: '14'
order: 9
owner: Minjoo Lee
categories:
- chapter14
lang: en
---

In gradient descent, people often stop when $$\|\nabla f(x)\|_2 \le \epsilon$$. That stopping rule has a fatal flaw: if you rescale your units by $$1000$$, $$\|\nabla f(x)\|_2$$ changes by $$1000$$ even though you haven't moved an inch closer to $$x^\star$$! The **Newton decrement** $$\lambda(x) = (\nabla f(x)^T (\nabla^2 f(x))^{-1} \nabla f(x))^{1/2}$$ fixes this completely: it measures the suboptimality gap in the function's own curvature metric, making it dimensionless and affine invariant.

## Background Knowledge Map: Four Faces of the Newton Decrement

- **Pillar 1 — Quadratic Suboptimality Estimate:** The drop achieved by minimizing the local quadratic model equals exactly $$\frac{1}{2}\lambda(x)^2$$, making $$\frac{1}{2}\lambda(x)^2 \le \epsilon$$ Newton's natural stopping criterion.
- **Pillar 2 — Hessian-Norm Step Length:** Because $$\Delta x_{\text{nt}} = -H^{-1}\nabla f(x)$$, we have $$\lambda(x) = (\Delta x_{\text{nt}}^T H \Delta x_{\text{nt}})^{1/2} = \|\Delta x_{\text{nt}}\|_H$$—the Mahalanobis length of the Newton step.
- **Pillar 3 — Directional Derivative Link:** Along the Newton direction, $$\nabla f(x)^T \Delta x_{\text{nt}} = -\lambda(x)^2 \le 0$$, which enters directly into the Armijo backtracking condition $$f(x + t\Delta x_{\text{nt}}) \le f(x) - \alpha t \lambda(x)^2$$.
- **Pillar 4 — Affine Invariance:** Under $$g(y) = f(Ay)$$, the factors $$A$$ and $$A^T$$ cancel inside $$\lambda_g(y)$$, guaranteeing $$\lambda_g(y) = \lambda_f(Ay)$$ regardless of coordinate scaling.

### Step-by-Step Worked Example (Read Slowly): Computing $$\lambda(x)$$ and Checking Its Exact Suboptimality Bound

Let $$f(x_1, x_2) = 2x_1^2 + x_1 x_2 + x_2^2 - 5x_1 - 3x_2$$ at $$x = (0, 0)^T$$.

1. **Compute gradient and Hessian at $$x = (0,0)^T$$:**
   $$\nabla f(0,0) = \begin{bmatrix} -5 \\ -3 \end{bmatrix}, \qquad H = \nabla^2 f(x) = \begin{bmatrix} 4 & 1 \\ 1 & 2 \end{bmatrix}.$$
2. **Invert $$H$$ and find the Newton step $$\Delta x_{\text{nt}}$$:**
   - $$\det(H) = 8 - 1 = 7 \implies H^{-1} = \frac{1}{7}\begin{bmatrix} 2 & -1 \\ -1 & 4 \end{bmatrix}$$.
   - $$\Delta x_{\text{nt}} = -H^{-1}\nabla f(0,0) = -\frac{1}{7}\begin{bmatrix} 2(-5) - (-3) \\ -(-5) + 4(-3) \end{bmatrix} = -\frac{1}{7}\begin{bmatrix} -7 \\ -7 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$.
3. **Compute $$\lambda(x)^2$$ in two ways:**
   - Via directional derivative: $$\lambda(0,0)^2 = -\nabla f(0,0)^T \Delta x_{\text{nt}} = -((-5)(1) + (-3)(1)) = 8$$, so $$\lambda(0,0) = \sqrt{8} \approx 2.828$$.
   - Via Hessian norm: $$\Delta x_{\text{nt}}^T H \Delta x_{\text{nt}} = \begin{bmatrix} 1 & 1 \end{bmatrix}\begin{bmatrix} 4 & 1 \\ 1 & 2 \end{bmatrix}\begin{bmatrix} 1 \\ 1 \end{bmatrix} = 5 + 3 = 8$$. Exact match!
4. **Verify the suboptimality gap:** Since $$f$$ is quadratic, $$x^\star = (1,1)^T$$ with $$f(1,1) = 2 + 1 + 1 - 5 - 3 = -4$$, and $$f(0,0) - f(1,1) = 0 - (-4) = 4 = \frac{1}{2}\lambda(0,0)^2$$!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

In this chapter, we define the Newton decrement and examine its meaning.

For the optimization problem below, the Newton decrement at $$x$$ is defined as $$\lambda(x)$$:

>\begin{align}
>\min_{x} \quad f(x),\\\\
>\end{align}
>\begin{align}
>\lambda(x) = (\nabla f(x)^{T}(\nabla^{2}f(x))^{-1}\nabla f(x))^{1/2}.
>\end{align}

## Characteristics of Newton decrement
First, the Newton decrement is related to the difference between the function $$f(x)$$ and the minimum of its quadratic approximation. Calculating this difference gives:
>$$\begin{align}
>f(x)-&\min_{y} \big( f(x)+\nabla f(x)^{T}(y-x)+\frac{1}{2}(y-x)^{T}\nabla^{2}f(x)(y-x)\big),\\\\
>f(x)-&\bigg( f(x) + \nabla f(x)^{T}\big( -(\nabla^{2} f(x) )^{-1} \nabla f(x)\big) + \frac{1}{2}\big( -(\nabla^{2}f(x))^{-1} \nabla f(x) \big)^{T} \nabla ^{2}f(x) \big( -(\nabla^{2}f(x))^{-1}\nabla f(x) \big) \bigg) \\\\ 
>&= \frac{1}{2}\nabla f(x)^{T}(\nabla^{2} f(x) )^{-1}\nabla f(x) = \frac{1}{2}\lambda(x)^{2}.
>\end{align}$$

Thus, $$\frac{1}{2}\lambda^{2}(x)$$ can be considered an approximate bound for the suboptimality gap $$f(x)-f^{\star}$$.

Second, the Newton direction in Newton's method for each iteration is $$v = -(\nabla^{2}f(x))^{-1}\nabla f(x)$$, and the Newton decrement is the length of the Newton step in the norm defined by the Hessian $$\nabla^{2}f(x)$$.

Alternatively, this can be viewed as a type of Mahalanobis distance [[Wikipedia](https://en.wikipedia.org/wiki/Mahalanobis_distance)], where the new step $$y$$ is the observation, the current position $$x$$ is the mean, and the Hessian of $$f$$ at $$x$$ plays the role of the inverse covariance (precision) matrix. The Mahalanobis distance measures the distance from a point to the mean after scaling by the standard deviation in each direction.

If we consider the definition of Mahalanobis distance as the distance between a point and the mean of a distribution divided by the standard deviation in that direction, the Newton decrement represents the distance of the new step from the current position, with the Hessian playing the role of the inverse covariance matrix.

Third, the Newton decrement can be expressed in terms of the increment and the Hessian. Starting from the step update in Newton's method, we have:
>\begin{align}
>x^{+} &= x-\big(\nabla^{2} f(x) \big)^{-1} \nabla f(x) &\\ 
>\end{align}
>\begin{align}
>\Delta x_{nt} &= -\big(\nabla^{2} f(x) \big)^{-1} \nabla f(x) &\\
>\end{align}
>\begin{align}
>\nabla f(x)^{T} \Delta x_{nt} &= -\lambda (x)^{2}
>\end{align}

Utilizing these relations, the Newton decrement can also be expressed as:
>\begin{align}
>\lambda(x) = (\Delta x_{nt}^{T}\nabla^{2} f(x) \Delta x_{nt})^{1/2}.
>\end{align}


Finally, like the Newton step, the Newton decrement is also affine invariant. In other words, for any nonsingular matrix, if the function $$g(y) = f(Ay)$$ is defined, then at $$x = Ay$$, it holds that $$\lambda_{g(y)} = \lambda_{f(x)}$$.

### The Newton decrement in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/newton-decrement_en.mp4"></video>
</div>

½λ² as the drop of the quadratic model, compared with f − f* on eˣ − 2x and on the log-sum-exp function, then λ versus ‖∇f‖ as a stopping rule under a change of variables.
