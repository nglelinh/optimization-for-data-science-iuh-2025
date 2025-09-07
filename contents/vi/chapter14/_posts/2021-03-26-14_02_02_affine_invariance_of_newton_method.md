---
layout: post
title: 14-02-02 Affine invariance of Newton's method
chapter: '14'
order: 6
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

One of the important properties of Newton's method is that it is affine invariant. This means that the direction of the update is independent of affine transformations of the coordinate system. For example, gradient descent is variant to affine transformations, so the convergence speed differs depending on the coordinate space.

This page derives the affine invariance property.

## Affine invariance : proof
Let $$f:\mathbb{R}^{n}\rightarrow \mathbb{R}$$ be twice differentiable, and let $$A\in \mathbb{R}^{n\times n}$$ be nonsingular. Also, define $$g(y)$$ as $$f(Ay)$$. $$g(y):=f(Ay)$$. This means that some function $$g$$ that takes $$y$$ as input has the same output as function $$f$$ that takes $$Ay$$ (affine transformed by $$A$$ with respect to $$y$$) as input. To reduce confusion about notation and gradient arguments, we define $$x:=Ay$$.

Using the chain rule to differentiate both sides once and twice, we get the following results:

>$$
>\begin{align}
>\nabla g(y) &= A^{T} \nabla f(x)\\\\
>\nabla^{2} g(y) &= A^{T}\nabla^{2}f(x)A,
>\end{align}
>$$

The Newton step of $$g$$ with respect to $$y$$ is as follows:

>$$
>\begin{align}
>y^{+}  = y-(\nabla^{2}g(y))^{-1}\nabla g(y).
>\end{align}
>$$

Here, instead of function $$g$$, if we transform and organize it in terms of function $$f$$ with respect to $$x$$, we can derive the Newton step for $$x$$ and $$f$$.

>$$
>\begin{align}
>y^{+} &= y-(A^{T}\nabla^{2}f(x)A)^{-1}A^{T} \nabla f(x)\\\\
>\Leftrightarrow y^{+} &= y-A^{-1}(\nabla^{2}f(x))^{-1}(A^{T})^{-1}A^{T} \nabla f(x)\\\\
>\Leftrightarrow Ay^{+} &= Ay-(\nabla^{2}f(x))^{-1}\nabla f(x)\\\\
>\Leftrightarrow x^{+} &= x - \nabla^{2}f(x)^{-1}\nabla f(x).
>\end{align}
>$$

This means that the Newton step is affine invariant, i.e., the updates in coordinate systems transformed by affine transformations represented by non-singular matrices are identical to each other.

Using the same method to check the affine invariance of gradient descent by deriving the step update, we can obtain the following result:

>$$
>\begin{align}
>y^{+} &= y-t_{k}\cdot \nabla g(y)\\\\
>\Leftrightarrow y^{+} &= y-t_{k}\cdot \nabla f(x)A^{T}\\\\
>\Leftrightarrow x^{+} &= x - t_{k}\cdot A\nabla f(x)A^{T}. 
>\end{align}
>$$

In the case of gradient descent, since the Hessian matrix is approximated as $$\frac{1}{t}I$$ for updates, we can see that the direction of the update changes for affine transformed coordinates.