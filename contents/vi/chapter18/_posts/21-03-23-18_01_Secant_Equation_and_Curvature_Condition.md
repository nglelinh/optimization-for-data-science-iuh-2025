---
layout: post
title: 18-01 Secant Equation and Curvature Condition
chapter: '18'
order: 2
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

## Secant Equation
As mentioned earlier, $$B$$ is a matrix that approximates $$\nabla^2 f(x)$$. For matrix $$B$$ to have similar properties to the Hessian $$\nabla^2 f(x)$$, it must satisfy a condition called the secant equation. When $$x^{k+1} = x^k + s^k$$ and $$f$$ is twice differentiable, the first-order Taylor expansion of $$\nabla f(x^k + s^k)$$ shows that the true Hessian has the following property.

>$$\nabla f(x^k + s^k)  \approx \nabla f(x^k) + \nabla^2 f(x^k) s^k$$

Here, we call the approximation matrix of $$\nabla^2 f(x^k)$$ as $$B^{k+1}$$. This matrix satisfies the following equation.

>$$\nabla f(x^k + s^k)  = \nabla f(x^k) + B^{k+1} s^k$$

If $$x^{k+1} = x^k + s^k, y^k = \nabla f(x^{k + 1})  - \nabla f(x^k)$$, then the above equation can be rearranged as follows, and this is called the secant equation.

>$$
>B^{k+1} s^k = y^k
>$$

## The Intuition of Secant Equation

$$x$$axis은 $$x^k$$를, $$y$$axis은 $$\nabla f(x^k)$$를 나타낸다고 할when, $$B^{k+1}$$은 $$(x^k, \nabla f(x^k))$$and, $$(x^{k+1}, \nabla f(x^{k+1}))$$를 통and,하는 직선의 기울기and, 같다. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter18/intuition_of_secant_eq.png" alt="[Fig1] The intuition of secant equation" width="70%">
  <figcaption style="text-align: center;">[Fig1] The intuition of secant equation</figcaption>
</p>
</figure>

## Conditions to Determine $$B^+$$
matrix $$B$$를 basis,with, computation된 $$B^+$$는 다음의 3가지 condition,을 만족solution야한다.

1. $$B^+$$ is symmetric: Because it is an approximation of the Hessian.
2. $$B^+$$ close to $$B$$: A condition to determine a unique $$B^+$$. Since $$B$$ already contains useful information, we choose the matrix closest to $$B$$ among those $$B^+$$ that satisfy the secant equation.
3. $$B$$ is positive definite $$\Rightarrow B^+$$ is positive definite: To guarantee global optimum, we maintain the convexity of the problem. (reference: [Analyzing the hessian](https://web.stanford.edu/group/sisl/k12/optimization/MO-unit4-pdfs/4.10applicationsofhessians.pdf))

## Curvature Condition
The fact that $$B^+$$ is positive definite and $$B^+ s = y$$ implies the following fact.
>$$s^T y = s^T B^+ s > 0.$$

(reference: [positive definite in WikiPedia](https://en.wikipedia.org/wiki/Positive-definite_matrix))

Here, $$s^T y > 0$$ is called the curvature condition. If the curvature condition is satisfied, the secant equation $$B^+ s = y$$ always has a solution ($$B^+$$).
