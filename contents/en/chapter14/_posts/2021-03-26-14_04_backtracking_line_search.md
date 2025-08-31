---
layout: post
title: 14-04 Backtracking line search
chapter: "14"
order: 8
owner: "Minjoo Lee"
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

So far, we have examined pure Newton's method. However, this method does not guarantee convergence, so we use backtracking line search to ensure convergence in the damped Newton's method.

## Damped Newton's method
The pure Newton's method iteratively applies the following update (here $$t=1$$):

>\begin{align}
>x^{+} = x -t(\nabla^{2}f(x))^{-1}\nabla f(x).
>\end{align}

Damped Newton's method uses backtracking line search. If the function value at the updated position is greater than the quadratic approximation, we shrink the step size $$t$$:

>$$\begin{align}
>&\text{with parameters }0<\alpha \leq \frac{1}{2}, 0<\beta<1, \\
>&\text{while } f(x+tv)>f(x)+\alpha t \nabla f(x)^{T}v\\
>&\text{shrink }t=\beta t
>\end{align}$$

Here, $$v=-(\nabla^{2}f(x))^{-1}\nabla f(x)$$ and $$\nabla f(x)^{T}v = -\lambda^{2}(x)$$.

## Example: logistic regression
As an example, for logistic regression with n = 500, p = 100, we compare the convergence rate of gradient descent and Newton's method with backtracking line search.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/2.jpeg" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig 1] Logistic regression [3]</figcaption>
</p>
</figure>


Newton's method shows a much faster convergence rate than gradient descent. From the next chapter, we will examine this convergence rate.