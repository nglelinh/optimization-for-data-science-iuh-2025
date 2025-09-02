---
layout: post
title: 06-01 Gradient Descent
chapter: '06'
order: 2
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

Gradient descent is the simplest algorithm for solving unconstrained convex and differentiable optimization problems.

> $$\min_x f(x),$$
> where $$f$$ is differentiable and $$dom(f) = \mathbb{R}^n$$.

The optimal value is $$f^* = \min_x f(x)$$, and the optimizer is $$x^*$$.

### Gradient Descent Method
Gradient descent starts from an initial point $$x^{(0)} \in \mathbb{R}^n$$ and iteratively updates as follows until a stopping criterion is met:
> $$x^{(k)} = x^{(k-1)} - t_k \nabla f(x^{(k-1)}), \quad k = 1, 2, 3, ...$$, $$t_k > 0$$

Pseudocode:
> **Given a starting point** $$x \in dom(f)$$ <br>
> **Repeat**  <br>
> 1. Determine descent direction $$\Delta x = -\nabla f(x)$$. <br>
> 2. Line search: choose step size $$t > 0$$. <br>
> 3. Update $$x = x + t \Delta x$$. <br>
> **Until** stopping criterion is satisfied <br>

### Examples

The figure below shows gradient descent on a convex function. In this case, the local minimum is also the global minimum.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_01_gradientdescent1.png" alt="gradientdescent1" width="80%" height="80%">
  <figcaption style="text-align: center;">[Fig 1] Gradient descent in convex functions[3]</figcaption>
</p>
</figure>

The next figure shows gradient descent on a non-convex function. Here, the initial point determines which local minimum is reached.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_01_gradientdescent2.png" alt="gradientdescent2" width="80%" height="80%">
  <figcaption style="text-align: center;">[Fig 2] Gradient descent in non-convex functions[3]</figcaption>
</p>
</figure>

## Gradient Descent Interpretation
Gradient descent can be interpreted as choosing the next point by minimizing a quadratic approximation of the function.

For a function $$f$$, the second-order Taylor expansion around $$x$$ is:
>$$f(y) \approx f(x) + \nabla f(x)^T (y - x) +  \frac{1}{2} \nabla^2 f(x)  \|y - x\|_2^2$$

If we approximate the Hessian $$\nabla^2 f(x)$$ by $$\frac{1}{t}I$$, then:
>$$f(y) \approx f(x) + \nabla f(x)^T (y - x) +  \frac{1}{2t}  \|y - x\|_2^2$$
where $$t$$ is the step size.

Thus, in gradient descent, the function is approximated by a quadratic function whose Hessian matrix has eigenvalues equal to the reciprocal of the step size. The term $$f(x) + \nabla f(x)^T (y - x)$$ represents a linear approximation of $$f$$, and $$\frac{1}{2t}  \|y - x\|_2^2$$ serves as a proximity term indicating how close $$y$$ is to $$x$$.

The next position is chosen as the minimum of this approximated quadratic function. Setting the gradient of $$f(y)$$ to zero to find the next position $$y = x^+$$ leads to:

> $$x^+ = x - t \nabla f(x)$$

In the illustration below, the blue dot represents the current position $$x$$, and the red dot represents the next position $$y$$. The curve below is the actual function $$f$$, and the curve above is the quadratic approximation of $$f$$. Hence, the red dot indicates the minimum of the quadratic approximation.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_01_gradientdescent3.png" alt="gradientdescent3" width="80%" height="80%">
  <figcaption style="text-align: center;">$$ \text{[Fig 3] Gradient descent algorithm : red dot is } x^+ \text{ and blue dot } x \text{ [3]} $$</figcaption>
</p>
</figure>

The proximity of the next position $$y$$ to the current position $$x$$ is influenced by the weight of the proximity term $$\frac{1}{2t}$$. A smaller $$t$$ results in a larger weight for the proximity term, leading to smaller steps. This process can be expressed as:

> \begin{align}
x^+ = \underset{y}{\arg \min} \ f(x) + \nabla f(x)^T (y - x) + \frac{1}{2t} \parallel y - x \parallel_2^2
\end{align}
