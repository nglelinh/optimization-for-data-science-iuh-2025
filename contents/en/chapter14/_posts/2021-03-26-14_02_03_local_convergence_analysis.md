---
layout: post
title: 14-02-03 Local convergence analyisis
order: 7
owner: Minjoo Lee
categories:
- chapter14
lang: en
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
});
</script>

The second important property of Newton's method is that convergence is guaranteed near the solution when certain conditions are satisfied. This is called local convergence. Since the pure Newton's method we have discussed from [14-01]({% multilang_post_url contents/chapter14/2021-03-26-14_01_newton_method %}) does not guarantee convergence, we later devise the damped Newton's method that ensures convergence by adjusting the step size using the same backtracking line search covered in [Chapter 6]({% multilang_post_url contents/chapter06/21-03-20-06_00_gradient_descent %}), and analyze its convergence.


>Theorem: Let $$F : \mathbb{R}^{n}\, \rightarrow  \, \mathbb{R}^{n}$$ be continuously differentiable, and let $$x^{\star} \in \mathbb{R}^{n}$$ be a root of function $$F$$, i.e., $$F(x^{\star})=0$$.
>If $$F^{'}(x^{\star})$$ is non-singular, then the following (a) and (b) are satisfied: \\
>(a) If there exists a positive $$\delta$$ (>0) such that $$\| x^{(0)}-x^{\star} \|<\delta$$ and Newton's method is defined, then the following equation (converges superlinearly) is satisfied:
>\begin{align}
>\lim_{ k \rightarrow \infty } \frac{ \|\| x^{ (k+1) }-x^{ \star } \|\| } { \|\| x^{ (k) }-x^{ \star } \|\| } =0.
>\end{align} \\
>(b) If $$F^{'}$$ is Lipschitz continuous near $$x^{\star}$$, then there exists a positive K (>0) such that the following equation (quadratic convergence) is satisfied:
>\begin{align}
>\|\|x^{ (k+1) } - x^{ \star }\|\| \leq K \|\| x^{ (k) }-x^{ \star }\|\|^{2}.
>\end{align}

## Proof of (a)
>We organize $$F(x^{\star})$$ up to 1st order using Taylor expansion. Since 2nd order and higher terms are bounded by a constant multiple of the norm of the 1st order term, we can represent it using little-o notation as follows:
>\begin{align}
>0=F(x^{\star}) = F(x^{k}) +\nabla F(x^{k})(x^{\star}-x^{k})+o(\|\|x^{k}-x^{\star}\|\|).\\
>\end{align}
>Multiply both sides by $$\nabla F(x^{k})^{-1}$$ and organize. Since little-o is treated as a constant term, it can be ignored.
>\begin{align}
>x^{k}-x^{\star}-\nabla F(x^{k})^{-1} F(x^{k}) = o(\|\|x^{k}-x^{\star}\|\|).
>\end{align}
>Using Newton's method $$x^{k+1}=x^{k}-\nabla F(x^{k})^{-1}F(x^{k})$$, we can obtain the following result:
>\begin{align}
>x^{k+1}-x^{\star}=o(\|\|x^{k}-x^{\star}\|\|),
>\end{align}
>Therefore, when $$x^{k} \neq x^{\star}$$, we can prove (a) using the limit-definition of little-o [[wikipedia](https://en.wikipedia.org/wiki/Big_O_notation)].

>\begin{align}
>\lim_{k\rightarrow \infty} \frac{\|\|x^{k+1}-x^{\star}\|\|}{\|\|x^{k}-x^{\star}\|\|} = \lim_{k\rightarrow \infty}\frac{o(\|\|x^{k}-x^{\star}\|\|)}{\|\|x^{k}-x^{\star}\|\|}.
>\end{align}

## Proof of (b)
The process is identical to proving that the convergence rate in the Damped phase of [[14-05]({% multilang_post_url contents/chapter14/2021-03-26-14_05_convergence_analysis %})] is quadratic. Therefore, it is omitted.

## Example : divergence case
We briefly examine an example where convergence is not guaranteed with pure Newton's method.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/1_.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig 1] pure Newton's method applied on root finding : divergence case </figcaption>
</p>
</figure>

[image-link](https://slideplayer.com/slide/4998677/)

As shown in the figure, depending on the initial point $$x_0$$, the solution can diverge.
