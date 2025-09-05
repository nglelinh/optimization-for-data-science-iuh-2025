---
layout: post
title: 14-06-01 Definition of self-concordant functions
chapter: '14'
order: 11
owner: Minjoo Lee
categories:
- chapter14
lang: en
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
    });
</script>
## Self-concordant on $$R$$
A convex function $$f : R \rightarrow R$$ is defined as self-concordant when it satisfies the following equation:
>$$\begin{align}
>\|f^{'''}(x)\| \leq 2f^{''}(x)^{3/2} \qquad \text{for all }x\in \text{dom }f.
>\end{align}$$

As simple examples, linear functions ($$ax+b$$) and (convex) quadratic functions are self-concordant because their third derivative values are 0.

## Self-concordant on $$R^{n}$$
A function $$f : R^{n}\rightarrow R$$ is defined as self-concordant when it is self-concordant for any line segment within the domain, that is, for all line segments included in the domain. For example, for all $$x\in dom\, f$$ and all $$v$$, when $$g(t) = f(x+tv)$$ is defined, if $$g(t)$$ is self-concordant, then f is defined as a self-concordant function in the domain of $$\mathbb{R}^{n}$$.

## Example of self-concordance function

1) $$f : \mathbb{R}^{n}_{++}\rightarrow \mathbb{R}$$, $$f(x) = -\sum^{n}_{i=1}log(x_{i})$$.

It can be easily verified that $$f(t) = -\log{t}$$. Furthermore, the sum of self-concordant functions is also self-concordant. When there are self-concordant functions $$f_{1}, f_{2} : R\rightarrow R$$, the sum of self-concordant functions is also self-concordant as shown below.[3]
>$$\begin{align}
>|f_{1}^{'''}(x)+f_{2}^{'''}(x)|  \leq & |f^{'''}_{1}(x)|+|f^{'''}_{2}(x)|\\\\
> \leq &2\big( f^{''}_{1}(x)^{3/2}+f^{''}_{2}(x)^{3/2}\big)\\\\
>\leq &2\big( f^{''}_{1}(x)+f^{''}_{2}(x) \big)^{3/2}.
>\end{align}$$

The last step uses the following property:
>$$\begin{align}
>(u^{3/2}+v^{3/2})^{2/3} \leq u+v, \qquad u, v \geq 0.
>\end{align}$$

