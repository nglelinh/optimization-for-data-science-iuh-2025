---
layout: post
title: "19-01-01 Reminder - proximal gradient descent"
chapter: '19'
order: 3
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

Before looking at the **proximal Newton method** that we study in this chapter, let us first review **proximal gradient descent**.

For details, see [09 Proximal Gradient Descent and Acceleration]({% multilang_post_url contents/chapter09/20-01-08-09_proximal_gradient_descent_and_acceleration %}).

## Proximal gradient descent
**Proximal gradient descent** works on problems of the following form.

>$$f(x) = g(x) + h(x)$$

* $$g$$ is convex and differentiable. (**dom**$$(g) = \mathbb{R}^n$$)
* $$h$$ is convex, non-differentiable, and "simple".


#### Algorithm
Proximal gradient descent starts from an initial point $$x^{(0)}$$ and repeats the following update.

>$$x^{(k)} = \text{prox}_{t_k}(x^{(k-1)} - t_k \nabla g(x^{(k-1)}) ),\quad k=1,2,3,...$$

Here $$\text{prox}_{t}(\cdot)$$ is the proximal operator associated with $$h$$.

> \begin{align}
\text{prox}_{t}(x) = \underset{z}{\text{argmin}}  \frac{1}{2t} \parallel x - z \parallel_2^2 + h(z)
\end{align}

The update can also be written in a standardized form using the generalized gradient $$G_{t}$$.

> \begin{align}
> x^{(k)} = x^{(k-1)} - t_k \cdot G_{t_k}(x^{(k-1)}), \space \space \text{where} \space G_{t}(x) = \frac{x-\text{prox}_{t} (x - t \nabla g(x))}{t} \\\\
> \end{align}

#### Performance
* The performance of **proximal gradient descent** depends on $$h$$. If $$h$$ is a complicated function, and in particular if its prox has no closed form, then each minimization requires a lot of computation and the method can be very slow.

* It has the same convergence rate as gradient descent on $$g$$. However, since the prox operator is evaluated at every iteration, the method is only useful when the prox can be computed efficiently.

## Motivation
In **proximal gradient descent**, the differentiable function $$g$$ is approximated by its second-order Taylor expansion, the non-differentiable function $$h$$ is added to it to form the objective, and this objective is minimized repeatedly. This can be written as the following quadratic problem.

For the detailed derivation, see [09-01 Proximal gradient descent]({% multilang_post_url contents/chapter09/20-01-08-09_01_proximal_gradient_descent %}).

> $$
> \begin{align}
x^+ & = \underset{z}{\text{argmin}}  \, \frac{1}{2t} \parallel x - t \nabla g(x) - z \parallel_2 ^2 + h(z) \\\\
> & = \underset{z}{\text{argmin}} \ \nabla g(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2 + h(z) \\\\
> \end{align}
> $$

The first and second terms of the second expression come from the second-order Taylor approximation of $$g$$: we drop the constant term $$g(x)$$ and (as in gradient descent) replace the Hessian $$\nabla^2 g(x)$$ with $$\frac{1}{t} I$$ (spherical curvature).

The following figure shows how $$g$$ is minimized through this quadratic approximation in each update step of proximal gradient descent.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.01_01_proximal_gradient_descent.png" alt="[Fig 1] Proximal gradient descent updates [3]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Proximal gradient descent updates [3]</figcaption>
</p>
</figure>

The difference between gradient descent and Newton's method is whether the local Hessian $$\nabla^2 g(x)$$ is used in the quadratic approximation. So what happens if we use $$\nabla^2 g(x)$$ instead of $$\frac{1}{t} I$$ in the expression above?

This is exactly the idea behind the **proximal Newton method**, which we describe in the next section.
