---
layout: post
title: 14-01-01 Newton's method interpretation
order: 3
owner: Minjoo Lee
categories:
- chapter14
lang: en
---
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

We want to find the input $$y$$ that minimizes this $$f_{approx}$$, i.e., the quadratic approximation. Since $$f_{approx}$$ is convex, the input $$y$$ that makes the gradient of the above equation equal to zero will minimize $$f_{approx}$$. This result becomes the step update formula in Newton's method. Remember that the differentiation in the equation below is with respect to y.

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
