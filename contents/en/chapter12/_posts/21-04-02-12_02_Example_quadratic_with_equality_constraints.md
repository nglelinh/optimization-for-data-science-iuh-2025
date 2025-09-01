---
layout: post
title: 12-02 Example quadratic with equality constraints
chapter: '12'
order: 3
owner: Wontak Ryu
categories:
- chapter12
lang: en
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

A [quadratic program]() with only equality constraints is as follows.
>$$
>\begin{align}
>    &\min_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{subject to} &&{Ax = b},\\\\
>&\text{where } &&P \in \mathbb{S}_{+}^n \text{ and } A \in \mathbb{R}^{\text{p x n}}.
>\end{align}
>$$

This problem is convex and has no inequality constraints, so it satisfies Slater's condition (Strong duality). If the primal & dual solutions are $$x^\star, \nu^\star$$, then by KKT conditions they satisfy the following conditions [1].

* Stationarity: $$Px^\star + q + A^T\nu^\star = 0$$
* Complementary Slackness: Since there are no inequality constraints, this does not need to be considered.
* Primal & dual feasibility: $$Ax^\star = b$$

These conditions can be concisely expressed using a block matrix, which is called the KKT matrix [3].
> $$
> \begin{bmatrix}
>     P       & A^T  \\\\
>     A       & 0  \\\\
> \end{bmatrix}
> \begin{bmatrix}
>     x^\star  \\\\
>     \nu^\star  \\\\
> \end{bmatrix}
> =
> \begin{bmatrix}
>     -q  \\\\
>     b  \\\\
> \end{bmatrix}
> $$

Solving this matrix equation gives the primal & dual solutions for the given problem.

An interesting fact is that this problem can also be seen as computing the Newton step for an equality constrained problem [3]. For the problem $$min_x f(x) \text{ subject to } Ax = b$$, if we set P, q, r as follows, then the objective function of the quadratic program becomes identical to the second-order Taylor expansion of $$f(x)$$.<br/>
> $$P = \nabla^2 f(x^{(k-1)})$$, $$q = \nabla f(x^{(k-1)})$$, $$r = f(x^{(k-1)})$$