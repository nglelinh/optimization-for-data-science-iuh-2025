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

Picture yourself descending a misty mountain valley shaped like a long, narrow banana. Gradient descent looks only at the local slope under your boots and zig-zags endlessly from wall to wall. Newton's method surveys the entire bowl's exact curvature—computing all $$n(n+1)/2$$ second derivatives and inverting an $$n \times n$$ Hessian at every step—which is miraculous in $$n = 10$$ dimensions and completely infeasible in $$n = 50{,}000$$ dimensions. **Quasi-Newton methods** pull off one of the greatest bargains in numerical optimization: using *only* the gradients you already compute, they build a running low-rank portrait of the curvature that achieves superlinear convergence at $$O(n^2)$$ (or even $$O(n)$$) cost per step.

## Key ideas: Why Quasi-Newton Sits Between GD and Newton

- **The Curvature–Cost Trade-Off:** First-order methods cost $$O(n)$$ per step but suffer slow linear convergence $$O(\kappa \log(1/\epsilon))$$ when the condition number $$\kappa = L/\mu$$ is large. Exact Newton eliminates $$\kappa$$-dependence (quadratic local convergence) but pays $$O(n^3)$$ to factor $$\nabla^2 f(x)$$.
- **Learning Curvature from Gradient Differences:** Every step $$s_k = x^{k+1} - x^k$$ produces a gradient change $$y_k = \nabla f(x^{k+1}) - \nabla f(x^k)$$, which reveals the directional curvature $$\nabla^2 f(x^k)\, s_k \approx y_k$$ for free.
- **Low-Rank Symmetric Updates ($$O(n^2)$$ per step):** Instead of recomputing a Hessian from scratch, methods like SR1, DFP, and BFGS apply a rank-1 or rank-2 update to the current approximation $$B_k$$ (or directly to its inverse $$H_k = B_k^{-1}$$), avoiding $$O(n^3)$$ matrix inversions altogether.
- **Superlinear Convergence Without Second Derivatives:** Under mild smoothness and Wolfe line-search conditions, BFGS attains *superlinear* convergence—closing the gap between linear gradient descent and quadratic Newton while never differentiating twice.

### Worked example: Comparing GD, Newton, and Quasi-Newton on an Ill-Conditioned Bowl

Consider $$f(x) = \frac{1}{2}(x_1^2 + 100 x_2^2)$$ starting at $$x^0 = (10, 1)^T$$ (exact optimum $$x^\star = (0, 0)$$, condition number $$\kappa = 100$$). Here $$\nabla f(x^0) = (10, 100)^T$$ and $$f(x^0) = 100$$.

1. **Exact-line-search Gradient Descent step:**
   Along $$p_{\text{GD}} = -\nabla f(x^0) = (-10, -100)^T$$, the exact optimal step size is:
   $$t^\star = \frac{p^T p}{p^T Q p} = \frac{100 + 10{,}000}{100 + 1{,}000{,}000} = \frac{10{,}100}{1{,}000{,}100} \approx 0.0101.$$
   Thus $$x^1_{\text{GD}} \approx (9.899, -0.010)^T$$, with $$f(x^1_{\text{GD}}) \approx 49.0$$—barely halving the loss because $$x_1$$ moved by only $$1\%$$!
2. **Exact Newton step:**
   Using $$Q^{-1} = \operatorname{diag}(1, 0.01)$$, $$p_{\text{N}} = -Q^{-1}\nabla f(x^0) = (-10, -1)^T$$, reaching $$x^1_{\text{N}} = (0, 0)$$ in **one step**—at the price of knowing and inverting $$Q$$.
3. **Quasi-Newton intuition (2 steps without knowing $$Q$$):**
   Starting from $$H_0 = I$$, the first step $$s_0 = x^1_{\text{GD}} - x^0 \approx (-0.101, -1.010)^T$$ observes $$y_0 = \nabla f(x^1) - \nabla f(x^0) \approx (-0.101, -101.0)^T$$. Instantly, the ratio $$y_{0,2}/s_{0,2} = 100$$ tells the BFGS update that the $$x_2$$ direction is $$100\times$$ steeper than $$x_1$$, reshaping $$H_1$$ so the *very next* step points straight to $$(0, 0)$$—solving this $$2$$-variable quadratic exactly in $$2$$ gradient evaluations!

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