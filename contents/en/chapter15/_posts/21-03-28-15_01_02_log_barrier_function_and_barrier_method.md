---
layout: post
title: 15-01-02 Log barrier function & barrier method
chapter: '15'
order: 4
owner: Minjoo Lee
categories:
- chapter15
lang: en
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>
Before introducing the barrier method, let's first see how the indicator function can be approximated by a barrier function.

## Approximation of indicator function
In the following figure, you can see the indicator function and the barrier function. The dotted line is the indicator function $$I_C$$, and the solid lines are the barrier function $$\phi(x) = -1/t\log(-x)$$ for $$t = 0.5, 1, 2$$. The barrier function smoothly approximates the indicator function, and when $$t=2$$, it provides the best approximation.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_function_01.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">$$\text{[Fig 1] barrier function }\phi(x) = -1/t\log(-x) [1]$$</figcaption>
</p>
</figure>


## Logarithmic barrier function
Suppose $$h_1, \cdots , h_m : \mathbb{R}^n \to \mathbb{R}$$ are convex and twice differentiable. For the set $$ \{x : h_i(x) \lt 0, i = 1, \cdots , m \}$$, the following function is called the logarithmic barrier function.

>
\begin{align}
\phi(x) = - \sum_{i=1}^{m} \log(-h_i(x))
\end{align}

Here, the set is assumed to be the interior of the feasible set $$C$$ and is non-empty.

## Barrier method

Using the barrier function, the original problem can be approximated as follows. Here, $$t\gt 0$$.
>
$$\begin{align}
&\min_{x}           && f(x) + \frac{1}{t} \phi(x) & \qquad      & \min_{x} && tf(x) + \phi(x) \\
&\text{subject to } && Ax = b                     & \iff \qquad & \text{subject to } && Ax = b \\
\end{align}$$

이와 같이 정의된 문제를 newton's method로 푸는 방법을 **barrier method**라고 한다.
