---
layout: post
title: 12-04 Example support vector machines
chapter: '12'
order: 5
owner: Wontak Ryu
categories:
- chapter12
lang: en
lesson_type: required
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

The support vector machine problem for non-separable sets is as follows.

>$$
>\begin{align}
>    &\min_{\beta, \beta-0, \xi} &&{\frac{1}{2} \rVert\beta\rVert_2^2 + C\sum_{i=1}^n \xi_i} \\\\
>    &\text{subject to} &&{\xi_i \ge 0, \quad i = 1, \dots, n}\\\\
>    & && y_i (x_i^T \beta + \beta-0) \ge 1 - \xi_i, \quad i = 1, \dots, n,\\\\
>&&&\text{given } y \in \{-1, 1\}^n \text{ and } X \in \mathbb{R}^{n \times p}.
>\end{align}
>$$

When the Lagrange multipliers for the two inequality constraints of the given problem are $$v^\star, w^\star \geq 0$$ respectively, the Lagrangian function is as follows.
>$$L(\beta, \beta-0, \xi, v^\star, w^\star) = \frac{1}{2} \rVert\beta\rVert_2^2 + C\sum_{i=1}^n \xi_i - \sum_{i=1}^n v_i^\star \xi_i + \sum_{i=1}^n w_i^\star (1 - \xi_i - y_i ( x_i^T \beta + \beta_0))$$

Using the above Lagrangian function, we can find the following conditions that make this problem satisfy the KKT stationarity condition. (Derive the conditions where the Lagrangian function becomes 0 when differentiated with respect to $$\beta, \beta_0, \xi$$ respectively)
>$$
>0 = \sum_{i=1}^n w_i^\star y_i, \quad \beta = \sum_{i=1}^n w_i^\star y_i x_i, \quad w^\star = C \cdot 1 - v^\star
>$$

Also, complementary slackness for the two inequality constraints is as follows.
> $$
> v_i^\star \xi_i = 0, \quad w_i^\star (1 - \xi_i - y_i (x_i^T \beta + \beta-0)) =0, \quad 1 = 1, \dots, n.
> $$

That is, at optimality, $$\beta^\star = \sum_{i=1}^n w_i^\star y_i x_i$$ is satisfied, and when $$y_i (x_i^T \beta^\star + \beta-0^\star) = 1 - \xi_i^\star$$, $$w_i^\star$$ becomes nonzero, and such point i is called **support points**.

* For a support point i where $$\xi_i^\star = 0$$, $$x_i$$ is located on the hyperplane and $$w_i^\star \in (0, C]$$.
* For a support point i where $$\xi_i^\star \neq 0$$, $$x_i$$ is located on the opposite side of the hyperplane and $$w_i^\star = C$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter12/svm.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">$$ \text{[Fig1] Illustration of support points with }\ \xi^\star \neq 0 \text{ [3]}$$ </figcaption>
</p>
</figure>

SVM문제를 최적화 하기 전, non-support points를 걸러내는데 위 방법을 이용할 수 있다 (non-support points를 걸러냄으로써 계산 효율을 높일 수 있다). 사실 KKT conditions는 이 문제의 solution을 도출하기 위한 직접적인 역할을 하지는 않지만, 우리는 이를 통해 SVM 문제를 더 잘 이해하기 위한 직관을 얻을 수 있다 [3].
