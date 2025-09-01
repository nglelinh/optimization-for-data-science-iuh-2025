---
layout: post
title: 10-04 Another Perspective on LP duality
chapter: '10'
order: 5
owner: Wontak Ryu
categories:
- chapter10
lang: vi
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>
In the case of duality discussed earlier, for LP, we multiplied the constraints of the primal problem by dual variables, obtained their linear combination, and then organized it to separate out the primal's objective function to obtain a bound. The separated remaining terms (something in the formula below) served as the bound for the primal problem. That is, they became the objective function of the dual problem, and the conditions created during the formula development process became the constraints of the dual problem.
Writing this partial process (the part of the above content that separates out the primal objective function to obtain a bound) as a formula, it looks like this:

>$$
>\begin{align}
>&\min_{x} &&f(x)\\\\
>&\text{subject to} &&Ax = b\\\\
>& &&Gx \leq h\\\\
>\end{align}
>$$

>$$
>\begin{align}
>& &\text{for any }u,\, v\geq 0,\\\\
>& &u^{T}(Ax-b) = 0\\\\
>&{+} &v^{T}(Gx-h)\leq 0\\\\
>&{=} &u^{T}(Ax-b) + v^{T}(Gx-h)\leq 0\\\\
>&{\approx} &f(x)+\text{something}. \\\\
>\end{align}
>$$

However, for optimization problems that are not linear programs, most cannot express the objective function as a linear combination of constraints. 

In this chapter, we examine the perspective of duality that is applicable to more universally common problems (all convex, most non-convex). We will find the duality of LP using this method called Lagrangian, and examine more detailed discussions in Chapter 11.

Looking at the equations up to the linear combination form for the primal LP problem described above, we can understand the following relationship:
>$$
>\begin{align}
>c^{T}x\geq c^{T}x+\overbrace{u^{T} \underbrace{(Ax-b)} _ {=0}+\underbrace{v^{T}} _ {\geq 0} \underbrace{(Gx-h)} _ {\leq 0}} ^ {\leq 0} := L(x,u,v).
>\end{align}
>$$

The right side of the inequality has a value less than or equal to the left side according to the conditions. Also, we define this expression as a function $$L(x, u, v)$$ for x, u, v.
Here, if we call the set satisfying the constraints of the primal LP (primal feasible set) C, we can understand the following relationship:

>$$
>\begin{align}
>C =  \{ x: Ax=b, Gx\leq h \},
>\end{align}
>$$
>$$
>\begin{align}
>f^{*}=\min_{x\in C} f(x) \geq \min_{x\in C}L(x,u,v)\geq \min_{x}L(x,u,v):=g(u,v).\\\\
>\end{align}
>$$

In other words, $$g(u,v)$$ becomes a lower bound of $$f^{*}$$ for any u or $$v$$ satisfying $$v\geq0$$.
Let's examine the lower bound value determined by $$g(u,v)$$.

>$$
>\begin{align}
g(u,v) = min_{x} c^{T}x+u^{T}(Ax-b) + v^{T}(Gx-h) \\\\
= \min_{x} (c+A^{T}u+G^{T}v)^{T}x - b^{T}u-h^{T}v \\\\
\begin{cases}= -b^{T}u-h^{T}v \qquad &\text{if }\ c = -A^{T}u-G^{T}v \\\\
-\infty \qquad &\text{otherwise}.
\end{cases}
>\end{align}
>$$


As can be seen from the equation, when $$c = -A^{T}u-G^{T}v$$ is not satisfied, it has a value of $$-\infty$$ due to the $$x$$ term.
Since we want to find the lower bound closest to $$f^{*}$$, we want to find the value that maximizes $$g(u, v)$$. This is $$-b^{T}u-h^{T}v$$, the value when $$c = -A^{T}u-G^{T}v$$ is satisfied, and this matches the Dual LP we obtained with the first method.

>$$
>\begin{align}
>f^{*} \geq g(u,v), \qquad \text{provided } v \geq 0\\\\
>\text{find the biggest lowerbound  } g(u,v)\\\\
>\max_{u,v} g(u,v)\\\\
>\text{s.t. }v \geq 0. 
>\end{align}
>$$

This method is also applicable to other types of optimization problems that are not in LP form.