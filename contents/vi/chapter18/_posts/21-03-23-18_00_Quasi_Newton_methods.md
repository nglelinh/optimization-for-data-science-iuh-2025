---
layout: post
title: 18-00 Quasi-Newton methods
chapter: '18'
order: 1
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

In the mid-1950s, physicist W.C. Davidon, who was working at Argonne National Laboratory, was solving optimization problems with large computational requirements using coordinate descent methods. Unfortunately, due to the instability of computers at the time, system crashes frequently occurred before computations could be completed, and frustrated by this, Davidon decided to find methods that could improve computational speed. This led to the birth of the first Quasi-Newton algorithm. This became a catalyst for dramatic progress in nonlinear optimization, and subsequently, various follow-up studies on this method emerged over the next 20 years.

Ironically, [Davidon's research](http://www.math.mcgill.ca/dstephens/680/Papers/Davidon91.pdf) was not published at the time and remained as a technical report for more than 30 years. It was finally published in the [first issue of SIAM Journal on Optimization](https://epubs.siam.org/toc/sjope8/1/1) in 1991.

Quasi-Newton methods require only the gradient of the objective function at each iteration. This has much less computational burden than Newton methods that require second derivatives, and moreover shows superlinear convergence, making it a sufficiently attractive method [14]. 

## Motivation for Quasi-Newton methods

Consider the following unconstrained, smooth optimization problem:
> $$
> \min_x \: f(x), \\\\
> \text{where } f \text{ is twice differentiable, and } dom \; f = \mathbb{R}^n.
> $$

The update methods for x in Gradient descent method and Newton's method for the above problem are as follows:
>**Gradient descent method:**
>$$
>x^+ = x - t \nabla f(x)
>$$

>**Newton's method:**
>$$
>x^+ = x - t \nabla^2 f(x)^{-1} \nabla f(x)
>$$

Newton's method has the advantage of showing quadratic convergence rate ($$O(\log \log 1/ \epsilon)$$), but there are problems with significantly high computational costs in the following two processes: 

* Computing the Hessian $$\nabla^2 f(x)$$: Computing and storing the Hessian matrix requires $$O(n^2)$$ memory. This is not suitable performance for handling high-dimensional functions. (reference: [Hessian matrix](https://en.wikipedia.org/wiki/Hessian_matrix#Use_in_optimization) in Wikipedia)
* Solving the equation $$\nabla^2 f(x) p = -\nabla f(x)$$: To solve this equation, we must compute the inverse matrix of the Hessian $$\nabla^2 f(x)$$. (reference: [Computational complexity of Matrix algebra](https://en.wikipedia.org/wiki/Computational_complexity_of_mathematical_operations#Matrix_algebra) in Wikipedia)

Quasi-Newton methods use an approximation $$B$$ instead of $$\nabla^2 f(x)$$.
>**Quasi-Newton method:**
>$$
>x^+ = x + tp \\\\
>\text{where } Bp = -\nabla f(x).
>$$

Here, B should be easy to compute, and it should also be easy to solve the equation $$Bp = g$$. 

## Quasi-Newton Algorithm
The Quasi-Newton algorithm is as follows:

* Pick initial $$x^0$$ and $$B^0$$
* For $$k = 0, 1, \dots$$
    * Solve $$B^k p^k = - \nabla f(x^k)$$
    * Pick $$t_k$$ and let $$x^{k+1} = x^{k} + t_k p^k$$
    * Update $$B^k$$ to $$B^{k+1}$$
* End for

A major characteristic of this method is updating $$B$$ so that we can gradually approach the optimal point. That is, the method of obtaining the next step $$B^+$$ from $$B$$ will be the main topic of discussion in this chapter. (**Note:** For convenience, we will use the two notations $$B^{k+1}, B^k$$ and $$B^+, B$$ interchangeably.)