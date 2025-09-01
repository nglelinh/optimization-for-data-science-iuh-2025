---
layout: post
title: 12-01 Karush-Kuhn-Tucker conditions
chapter: '12'
order: 2
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

Let us consider the following general optimization problem.

>$$
>\begin{align}
>    &\min_{x} &&{f(x)} \\\\
>    &\text{subject to } &&{h_i(x) \le 0, \text{ } i=1,\dots,m} \\\\
>    & &&{l_j(x) = 0, \text{ } j=1,\dots,r}.\\\\
>\end{align}
>$$

The **Karush–Kuhn–Tucker (KKT) conditions** or **KKT conditions** consist of the following conditions [3].

* $$0 \in \partial \big( f(x) + \sum_{i=1}^{m} \lambda_i h_i(x) + \sum_{j=1}^{r} \nu_j l_j(x) \big)$$ (Stationarity): When $$\lambda, \nu$$ are fixed, the subdifferential with respect to $$x$$ contains 0. 
* $$\lambda_i \cdot h_i(x) = 0 \text{ for all } i$$ (Complementary Slackness):  At least one of $$\lambda_i$$ and $$h_i$$ has value 0.
* $$h_i(x) \le 0, l_j(x) = 0 \text{ for all } i, j$$ (Primal Feasibility): Indicates whether the constraints of the primal problem are satisfied.
* $$\lambda_i \ge 0 \text{ for all } i$$ (Dual Feasibility): Indicates whether the constraints of the dual problem are satisfied.

## Sufficiency
For a convex primal problem, when there exist $$x^\star, \lambda^\star, \nu^\star$$ that satisfy the KKT conditions, the following process shows that $$x^\star, \lambda^\star, \nu^\star$$ are primal & dual solutions with zero duality gap.

>$$
>\begin{align}
>    g(\lambda^\star, \nu^\star) &= \min_x L(x, \lambda^\star, \nu^\star) \\\\
>                                &= L(x^\star, \lambda^\star, \nu^\star) \\\\
>                                &= f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) \\\\
>                                &= f(x^\star)
>\end{align}
>$$

1. $$L(x,\lambda^\star,\nu^\star) = f(x) + \sum_{i=1}^{m} \lambda_i^\star h_i(x) + \sum_{j=1}^{r} \nu_j^\star l_j(x)$$ is a convex function. (sum of convex functions) 
2. $$0 \in \partial \big( f(x^\star) + \sum_{i=1}^{m} \lambda_i^\star h_i(x^\star) + \sum_{j=1}^{r} \nu_j^\star l_j(x^\star) \big)$$therefore $$\min_x L(x, \lambda^\star, \nu^\star) = L(x^\star, \lambda^\star, \nu^\star)$$.
3. By complementary slackness and primal feasibility, $$f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) = f(x^\star)$$.

## Necessity
When $$x^\star, \lambda^\star, \nu^\star$$ are primal & dual solutions with zero duality gap (for example, satisfying Slater's condition), all the inequalities below become equalities, so in this problem $$x^\star, \lambda^\star, \nu^\star$$ satisfy the KKT conditions.
>$$
>\begin{align}
>    f(x^\star) &= g(\lambda^\star, \nu^\star) \\\\
>                   &= \min_x  \big( f(x) + \sum_{i=1}^{m} \lambda_i^\star h_i(x) + \sum_{j=1}^{r} \nu_j^\star l_j(x) \big) \\\\
>                   &\le f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) \\\\
>                   &\le f(x^\star)
>\end{align}
>$$

1. $$f(x^\star) = g(\lambda^\star, \nu^\star)$$ means zero duality gap.
2. To satisfy $$f(x^\star) + \sum_{i=1}^m \underbrace{\lambda_i^\star h_i(x^\star)}_{0} + \sum_{j=1}^r \underbrace{\nu_j^\star l_j(x^\star)}_{0} = f(x^\star)$$, complementary slackness and primal feasibility must be satisfied.
3. If $$f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) = f(x^\star)$$ is satisfied, all inequalities in the above derivation become equalities.

## Putting it together
In summary, KKT conditions are:

* Sufficient conditions for primal & dual solutions with zero duality gap.
* If strong duality holds, they become necessary conditions for primal & dual solutions.

That is, for problems that satisfy strong duality, the following relationship holds.
>$$
>\begin{align}
>    x^\star, \lambda^\star, \nu^\star \text{ are primal and dual solutions} \\\\
>    \Leftrightarrow x^\star, \lambda^\star, \nu^\star \text{ satisfy the KKT conditions} \\\\
>\end{align}
>$$