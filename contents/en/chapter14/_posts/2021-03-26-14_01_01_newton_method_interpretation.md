---
layout: post
title: 14-01-01 Newton's method interpretation
chapter: '14'
order: 3
owner: Minjoo Lee
categories:
- chapter14
lang: en
---

Why does the formula $$x^+ = x - (\nabla^2 f(x))^{-1}\nabla f(x)$$ look like a matrix-scaled gradient? Because it isn't a heuristic rescaling at all—it is the exact minimizer of the best quadratic bowl tangent to $$f$$ at your current position $$x$$. Seeing both Gradient Descent and Newton's method as "minimize a local quadratic surrogate" unifies first-order and second-order optimization into one crystal-clear geometric picture.

## Key ideas: Surrogate Minimization Geometry

- **Pillar 1 — Second-Order Taylor Surrogate:** Near $$x$$, $$f_{\text{approx}}(y) = f(x) + \nabla f(x)^T(y-x) + \frac{1}{2}(y-x)^T \nabla^2 f(x)(y-x)$$ matches $$f$$'s value, slope, and curvature at $$x$$.
- **Pillar 2 — Exact Minimization of the Surrogate:** Setting $$\nabla_y f_{\text{approx}}(y) = \nabla f(x) + \nabla^2 f(x)(y-x) = 0$$ immediately yields the Newton update $$y = x - (\nabla^2 f(x))^{-1}\nabla f(x)$$.
- **Pillar 3 — Gradient Descent as a Spherical Surrogate:** Replacing $$\nabla^2 f(x)$$ with $$\frac{1}{t}I$$ approximates the terrain by a perfectly round paraboloid, whose minimizer is $$y = x - t\nabla f(x)$$.
- **Pillar 4 — Curvature-Matching Advantage:** When $$f$$'s level sets are elongated ellipses rather than circles, the true quadratic surrogate captures the eccentricity and aims straight at the center of the ellipse.

### Worked example: Building and Minimizing the Local Quadratic Surrogate

Let $$f(x) = x^4 - 4x + 5$$ at $$x = 2$$. We construct both the Newton surrogate and a Gradient Descent surrogate (with $$t = \frac{1}{50}$$).

1. **Evaluate derivatives at $$x = 2$$:**
   - $$f(2) = 16 - 8 + 5 = 13$$,
   - $$f'(2) = 4(2)^3 - 4 = 28$$,
   - $$f''(2) = 12(2)^2 = 48$$.
2. **Write the exact local quadratic surrogate:**
   $$f_{\text{approx}}(y) = 13 + 28(y - 2) + \frac{1}{2}(48)(y - 2)^2 = 13 + 28(y - 2) + 24(y - 2)^2.$$
3. **Minimize $$f_{\text{approx}}(y)$$:** Set $$f'_{\text{approx}}(y) = 28 + 48(y - 2) = 0$:
   $$y_{\text{NT}} = 2 - \frac{28}{48} = 2 - \frac{7}{12} = \frac{17}{12} \approx 1.4167.$$
   (Note: the true minimum of $$f$$ is at $$x^\star = 1$$, so one Newton step cuts the distance to $$x^\star$$ by more than half, from $$1.0$$ to $$0.4167$$.)
4. **Compare with the GD surrogate ($$\frac{1}{t} = 50$$):**
   $$y_{\text{GD}} = 2 - \frac{28}{50} = 1.44.$$
   Here $$\frac{1}{t} = 50$$ happened to be close to $$f''(2) = 48$$; had we picked a conservative $$t = 0.005$$ ($$\frac{1}{t} = 200$$), GD would only reach $$2 - 0.14 = 1.86$$.

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
});
</script>

This page examines how the update step discussed earlier is derived from the quadratic approximation of the original function $$f$$. We also compare it with the gradient descent update step covered in [Chapter 6]({% multilang_post_url contents/chapter06/21-03-20-06_00_gradient_descent %}).

## Newton's method update step
The second-order Taylor approximation (quadratic approximation) of function $$f$$ is as follows:

>$$
>\begin{align}
>f(y)	\approx f(x) + \nabla f(x)^{T}(y-x) +\frac{1}{2}(y-x)^{T}\nabla^{2}f(x)(y-x),\\\\
>f_{approx}(y)	= f(x) + \nabla f(x)^{T}(y-x) +\frac{1}{2}(y-x)^{T}\nabla^{2}f(x)(y-x).
>\end{align}
>$$

Here, $$y$$ is the next step's $$x$$ value, which is $$x^{+}$$. We also define the quadratic approximation as $$f_{approx}$$.

We want to find the input $$y$$ that minimizes this $$f_{approx}$$, i.e., the quadratic approximation. It is a quadratic in $$y$$ with Hessian $$\nabla^2 f(x)$$, so it is convex when $$\nabla^2 f(x) \succeq 0$$. If $$\nabla^2 f(x) \succ 0$$, it is strictly convex and has a unique minimizer: the $$y$$ that makes its gradient zero. (If the Hessian is only positive semidefinite, the model may have no minimizer or infinitely many.) This result becomes the step update formula in Newton's method. Remember that the differentiation in the equation below is with respect to y.

>$$
>\begin{align}
>\nabla f_{approx}(y)	&= \nabla f(x) +\frac{1}{2} \Big((\nabla^{2} f(x))^{T}(y-x)+(y-x)^{T}\nabla^{2}f(x)\Big)\\\\
>&=\nabla f(x) +\nabla^{2} f(x)(y-x)\\\\
>& = 0,\\\\
>\Leftrightarrow y &= x-(\nabla^{2}f(x))^{-1}\nabla f(x).
>\end{align}
>$$

## Gradient descent update step
In gradient descent, we use the second-order Taylor approximation terms of function $$f$$, but for the second-order term, we assume it as the identity matrix divided by $$t$$, rather than the actual second derivative result.

>$$
>\begin{align}
>f(y)	\approx f(x) + \nabla f(x)^{T}(y-x) +\frac{1}{2t}\|{y-x}\|_{2}^{2},\\\\
>f_{approx}(y)	= f(x) + \nabla f(x)^{T}(y-x) +\frac{1}{2t}\|{y-x}\|_{2}^{2}.\\\\
>\end{align}
>$$

Similar to Newton's method, we can determine the $$y$$ value where the gradient of the above approximation is zero, i.e., $$x^{+}$$.
>$$
>\begin{align}
>\nabla f(y) &= \nabla f(x) + \frac{1}{t}(y-x), \\\\
> &= 0,\\\\
>y &= x-t\nabla f(x).
>\end{align}
>$$

This result is identical to the step update of gradient descent.

For detailed information about gradient descent, refer to the [gradient descent chapter]({% multilang_post_url contents/chapter06/21-03-20-06_00_gradient_descent %}).

## Example
As an example, for the function $$f = (10x_{1}^{2}+x_{2}^{2})/2+5log(1+e^{-x_{1}-x_{2}})$$, we assume taking steps of approximately equal length. That is, we set the step size in gradient descent to match the update magnitude of Newton's method at each iteration, and compare the convergence directions of gradient descent (black) and Newton's method (blue) according to their steps.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/gd.jpeg" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig 1] Comparison between gradient descent(black) and Newton's method(blue)[3]</figcaption>
</p>
</figure>

As can be seen in Fig 1, gradient descent assumes the second derivative term as a constant multiplied by the identity matrix when calculating the gradient, so it converges perpendicularly to the tangent direction of the contour lines, and shows slower convergence speed compared to Newton's method. The remaining chapters will cover the properties, characteristics, convergence, examples, etc. of Newton's method.

### Newton's method: 1D, 2D, and when it fails (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/newton-parabola_en.mp4"></video>
</div>

Each step minimizes the quadratic model $$f(x_k)+f'(x_k)(x-x_k)+\tfrac12 f''(x_k)(x-x_k)^2$$, so $$x_{k+1}=x_k-f'(x_k)/f''(x_k)$$.
