---
layout: post
title: '22-01 Last time: ADMM'
chapter: '22'
order: 2
owner: YoungJae Choung
categories:
- chapter22
lang: vi
---


## Last time: ADMM
Let's consider the following optimization problem
> $$\begin{align}
> &\min_{x,z} &&f(x) + g(z)\\\\
> &\text{ subject to } &&Ax + Bz = c 
> \end{align}$$

Converting this to Augmented Lagrangian form gives us the following. (for some $$ρ > 0$$)
> $$ L_ρ(x, z, u) = f(x) + g(z) + u^T(Ax + Bz − c) + \frac{ρ}{2} \| Ax + Bz − c \|^2_2$$

The above equation becomes Strongly Convex with the addition of $$\frac{ρ}{2} \| Ax + Bz − c \|^2_2$$, and this can be transformed into a form useful for parallel processing as shown in the following equation.
* For detailed proof, please refer to the content of the previous chapter.
ADMM: for $$k = 1, 2, 3, . . .$$
> $$x^{(k)} = argmin_{x} L_ρ(x, z^{(k−1)}, u^{(k−1)})$$
> $$z^{(k)} = argmin_{z} L_ρ(x^{(k)}  , z, u^{(k−1)})$$
> $$u^{(k)} = u^{(k−1)} + ρ(Ax^{(k)} + Bz^{(k)} − c)$$
 
## ADMM in scaled form
Let's change the dual variable $$u$$ to the scaled variable $$w = u/ρ$$. Here, the ADMM step can be computed as follows.

> $$x^{(k)} = argmin_{x} f(x) + \frac{ρ}{2} \| Ax + Bz^{(k−1)} − c + w^{(k−1)} \|^2_2$$
> $$z^{(k)} = argmin_{z} g(z) + \frac{ρ}{2} \| Ax^{(k)} + Bz − c + w^{(k−1)} \|^2_2$$ 
> $$w^{(k)} = w^{(k−1)} + Ax^{(k)} + Bz^{(k)} − c$$
