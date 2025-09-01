---
layout: post
title: 10-02 Duality in general LPs
chapter: '10'
order: 3
owner: Wontak Ryu
categories:
- chapter10
lang: en
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

In [10-01]({% multilang_post_url contents/chapter10/21-03-22-10_01_Lower_Bounds_in_Linear_Programs %}), we examined the primal and dual of LP problems with single-dimensional variables. In 10-02, we want to examine the dual for LPs in general form.

The general form of LP is as follows:

Given $$c\in\mathbb{R}^{n},\, A\in\mathbb{R}^{m\times n},\, b\in\mathbb{R}^{m},\, G\in\mathbb{R}^{r\times n},\, h\in\mathbb{R}^{r}$$,

>$$
>\begin{align}
>&\min_{x} &&c^{T}x\\\\
>&\text{subject to} &&Ax = b\\\\
>& &&Gx \leq h.\\\\
>\end{align}
>$$

Similar to the example in 10-01, we define dual variables $$u, v$$ equal in number to the number of constraints,
and can define the objective function of the dual problem and constraints as the sum of products of constraints and each dual variable. 

>$$
>\begin{align}
>& &u^{T}(Ax-b) = 0\\\\
>&{+} &v^{T}(Gx-h)\leq 0\\\\
>&{=} &u^{T}(Ax-b) + v^{T}(Gx-h)\leq 0.\\\\
>\end{align}
>$$

Remember that the dual variable $$u$$ for equality has no constraints, while $$v$$ is a dual variable for inequality and thus has the additional constraint of being positive.
By organizing the last equation to represent the objective function of the primal LP, we get the dual LP.

>$$
>\begin{align}
>u^{T}(Ax-b) + v^{T}(Gx-h)\leq 0 \\\\
>\underbrace{(-A^{T}u-G^{T}v)^{T}}_{=c^{T}}x\geq-b^{T}u-h^{T}v \\\\
>\text{Lower bound is} -b^{T}u-h^{T}v \\\\ 
>\text{for } x \text{ primal feasible, and any u, v satisfies,} \\\\
>c = -A^{T}u-G^{T}v \\\\
>v\geq 0. \\\\
>\end{align}
>$$

That is, when $$c = -A^{T}u-G^{T}v$$, the optimal value of the primal has a lower bound of $$-b^{T}u-h^{T}v$$.

Consequently, the dual LP can be defined as follows.

>$$
>\begin{align}
>&\max_{u,v} &&-b^{T}u-h^{T}v \\\\
>&\text{subject to} &&c = -A^{T}u-G^{T}v \\\\
>& &&v\geq 0.
>\end{align}
>$$

