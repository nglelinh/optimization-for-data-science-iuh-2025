---
layout: post
title: 14-03 Newton decrement
chapter: '14'
order: 7
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

In this chapter, we define the Newton decrement and examine its meaning.

For the optimization problem below, the Newton decrement at $$x$$ is defined as $$\lambda(x)$$:

>\begin{align}
>\min_{x} \quad f(x),\\\\
>\end{align}
>\begin{align}
>\lambda(x) = (\nabla f(x)^{T}(\nabla^{2}f(x))^{-1}\nabla f(x))^{1/2}.
>\end{align}

## Characteristics of Newton decrement
First, the Newton decrement is related to the difference between the function $$f(x)$$ and the minimum of its quadratic approximation. Calculating this difference gives:
>$$\begin{align}
>f(x)-&\min_{y} \big( f(x)+\nabla f(x)^{T}(y-x)+\frac{1}{2}(y-x)^{T}\nabla^{2}f(x)(y-x)\big),\\\\
>f(x)-&\bigg( f(x) + \nabla^{T}f(x)\big( -(\nabla^{2} f(x) )^{-1} \nabla f(x)\big) + \frac{1}{2}\big( -(\nabla^{2}f(x))^{-1} \nabla f(x) \big)^{T} \nabla ^{2}f(x) \big( -(\nabla^{2}f(x))^{-1}\nabla f(x) \big) \bigg) \\\\ 
>&= \frac{1}{2}\nabla f(x)^{T}(\nabla^{2} f(x) )^{-1}\nabla f(x) = \frac{1}{2}\lambda(x)^{2}.
>\end{align}$$

Thus, $$\frac{1}{2}\lambda^{2}(x)$$ can be considered an approximate bound for the suboptimality gap $$f(x)-f^{\star}$$.

Second, the Newton direction in Newton's method for each iteration is $$v = -(\nabla^{2}f(x))^{-1}\nabla f(x)$$, and the Newton decrement is the length of the Newton step in the norm defined by the Hessian $$\nabla^{2}f(x)$$.

Alternatively, this can be viewed as a type of Mahalanobis distance [[Wikipedia](https://en.wikipedia.org/wiki/Mahalanobis_distance)], where the new step $$y$$ is the observation, the current position $$x$$ is the mean, and the Hessian of $$f(x)$$ is the covariance. The Mahalanobis distance measures the distance from a point to the mean in the direction of the covariance of the distribution.

If we consider the definition of Mahalanobis distance as the distance between a point and the mean of a distribution divided by the standard deviation in that direction, the Newton decrement represents the distance of the new step from the current position, with the Hessian serving as the covariance of the distribution.

Third, the Newton decrement can be expressed in terms of the increment and the Hessian. Starting from the step update in Newton's method, we have:
>\begin{align}
>x^{+} &= x-\big(\nabla^{2} f(x) \big)^{-1} \nabla f(x) &\\ 
>\end{align}
>\begin{align}
>\Delta x_{nt} &= -\big(\nabla^{2} f(x) \big)^{-1} \nabla f(x) &\\
>\end{align}
>\begin{align}
>\nabla f(x)^{T} \Delta x_{nt} &= -\lambda (x)^{2}
>\end{align}

Utilizing these relations, the Newton decrement can also be expressed as:
>\begin{align}
>\lambda(x) = (\Delta x_{nt}^{T}\nabla^{2} f(x) \Delta x_{nt})^{1/2}.
>\end{align}


Finally, like the Newton step, the Newton decrement is also affine invariant. In other words, for any nonsingular matrix, if the function $$g(y) = f(Ay)$$ is defined, then at $$x = Ay$$, it holds that $$\lambda_{g(y)} = \lambda_{f(x)}$$.