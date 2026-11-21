---
layout: post
title: 18-01 Secant Equation and Curvature Condition
chapter: '18'
order: '2'
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

# Secant Equation

As mentioned earlier, $$B$$ is a matrix that approximates $$\nabla^2 f(x)$$. For the matrix $$B$$ to have properties similar to the Hessian $$\nabla^2 f(x)$$, it must satisfy a condition called the secant equation.

When $$x^{k+1} = x^k + s^k$$ and $$f$$ is twice differentiable, the first-order Taylor expansion of $$\nabla f(x^k + s^k)$$ shows that the true Hessian has the following property.

>$$
>\nabla f(x^k + s^k) \approx \nabla f(x^k) + \nabla^2 f(x^k) s^k
>$$

Here, we call the approximation matrix of $$\nabla^2 f(x^k)$$ as $$B^{k+1}$$. This matrix satisfies the following equation.

>$$
>\nabla f(x^k + s^k) = \nabla f(x^k) + B^{k+1} s^k
>$$

If $$x^{k+1} = x^k + s^k$$ and $$y^k = \nabla f(x^{k+1}) - \nabla f(x^k)$$, the equation above can be rearranged as follows, and this is called the secant equation.

>$$
>B^{k+1} s^k = y^k
>$$

# The Intuition of the Secant Equation

When $$x$$ is the horizontal axis and $$\nabla f(x)$$ is the vertical axis, $$B^{k+1}$$ equals the slope of the line through the two points $$(x^k, \nabla f(x^k))$$ and $$(x^{k+1}, \nabla f(x^{k+1}))$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter18/intuition_of_secant_eq.png" alt="[Fig1] The intuition of the secant equation" width="70%">
  <figcaption style="text-align: center;">[Fig1] The intuition of the secant equation</figcaption>
</p>
</figure>

# Conditions to Determine the Matrix $$B^+$$

Starting from the current matrix $$B$$, there are three conditions for computing the next matrix $$B^+$$.

1. $$B^+$$ is symmetric: because it is an approximation of the Hessian.
2. $$B^+$$ is close to $$B$$: a condition that determines a unique $$B^+$$. Since $$B$$ already contains useful information, we choose the matrix closest to $$B$$ among those $$B^+$$ that satisfy the secant equation.
3. $$B$$ is positive definite $$\Rightarrow B^+$$ is positive definite: to guarantee a global optimum, we maintain the convexity of the problem. (reference: [Analyzing the Hessian](https://web.stanford.edu/group/sisl/k12/optimization/MO-unit4-pdfs/4.10applicationsofhessians.pdf))

# Curvature Condition

The fact that $$B^+$$ is positive definite and $$B^+ s = y$$ implies the following.

>$$
>s^T y = s^T B^+ s > 0.
>$$

(reference: [Positive-definite matrix on Wikipedia](https://en.wikipedia.org/wiki/Positive-definite_matrix))

Here, $$s^T y > 0$$ is called the curvature condition. If the curvature condition is satisfied, the secant equation $$B^+ s = y$$ always has a solution $$B^+$$.
