---
layout: post
title: 18-01 Secant Equation and Curvature Condition
chapter: '18'
order: 2
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

## Secant Equation
앞서 $$B$$는 $$\nabla^2 f(x)$$를 approximation하는 matrix이라고 했다. matrix $$B$$가 Hessian $$\nabla^2 f(x)$$and, 비슷한 성질을 갖기 for,서는 secant equation이라는 condition,을 만족solution야 한다. $$x^{k+1} = x^k + s^k$$이고 $$f$$가 두 번 이image 미분 가능할 when,, $$\nabla f(x^k + s^k)$$to, about, first-order Taylor expansion은 true Hessian이 다음의 성질을 가짐을 보인다.

>$$\nabla f(x^k + s^k)  \approx \nabla f(x^k) + \nabla^2 f(x^k) s^k$$

이when, $$\nabla^2 f(x^k)$$to, about, approximation matrix을 $$B^{k+1}$$이라 한다. 이 matrix은 다음의 등식을 만족시킨다.

>$$\nabla f(x^k + s^k)  = \nabla f(x^k) + B^{k+1} s^k$$

$$x^{k+1} = x^k + s^k, y^k = \nabla f(x^{k + 1})  - \nabla f(x^k)$$이면 위 등식은 아래and, 같이 정리되고, 이를 secant equation이라 부른다.

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

1. $$B^+$$ is symmetric: Hessianto, about, 추정이기 because,이다.
2. $$B^+$$  close to $$B$$: 유일한 $$B^+$$를 결정하기 위한 condition,. $$B$$가 이미 유용한 정보를 가지고 있으므to, secant equation을 만족하는 $$B^+$$ 중at, $$B$$and, 최about, 가까운 matrix을 고른다.
3. $$B$$ is positive definite $$\Rightarrow B^+$$ is positive definite: Global optimum을 보장하기 for,서 problem의 convexity를 유지한다. (reference: [Analyzing the hessian](https://web.stanford.edu/group/sisl/k12/optimization/MO-unit4-pdfs/4.10applicationsofhessians.pdf))

## Curvature Condition
$$B^+$$가 positive definite이면서 $$B^+ s = y$$라는 것은 다음의 in fact,을 암시한다.
>$$s^T y = s^T B^+ s > 0.$$

(reference: [positive definite in WikiPedia](https://en.wikipedia.org/wiki/Positive-definite_matrix))

여기서 $$s^T y > 0$$을 curvature condition이라 부른다. Curvature condition을 만족하면, secant equation $$B^+ s = y$$은 always, solution($$B^+$$)을 갖는다.
