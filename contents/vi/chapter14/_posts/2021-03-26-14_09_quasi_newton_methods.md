---
layout: post
title: 14-09 Quasi-Newton methods
chapter: '14'
order: 15
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

If the computation of the Hessian is too expensive or the Hessian is singular, we use quasi-Newton methods to approximate the Hessian matrix, i.e., $$\nabla^{2}f(x)$$ is replaced by $$H>0$$, and we use $$H$$ for the update:

>\begin{align}
>x^{+} = x - tH^{-1}\nabla f(x)
>\end{align}

Some features of quasi-Newton methods are as follows. For more details, see [Chapter 18]({% multilang_post_url contents/chapter18/21-03-23-18_00_Quasi_Newton_methods %}).

* The approximate Hessian $$H$$ is updated at each step. The goal is to use a relatively cheap computation for $$H^{-1}$$.
* The convergence rate is superlinear, but not as fast as Newton's method. Typically, $$n$$ steps of quasi-Newton are equivalent to one step of Newton in terms of progress.
* Many quasi-Newton methods update $$H$$ at each iteration using propagation techniques.
