---
layout: post
title: 13-04-03 Shifting linear transformations
chapter: '13'
order: 8
owner: Wontak Ryu
categories:
- chapter13
lang: vi
---

The dual formulation helps with shifting linear transformations between parts of the objective function and other domains.

Let’s look at the following:
> $$ \min_x f(x) + g(Ax)$$

The following expression is equivalent:
> $$min_{x,z} f(x) + g(z) \text { subject to } Ax = z$$

This leads to the following dual process:
> $$\text {g(u)} = \min_{x,z} f(x) + g(z) + u^T(z - Ax)$$
> $$\qquad  = -\max_{x} (A^T u)^T x - f(x) - \max_{z} (-u)^T z - g(z)  $$
> $$\qquad = -\ f^* (A^T u) - g^* (-u) $$

And the dual is:
> $$\max_u -f^*(A^Tu) - g^*(-u)$$

##### [Example]
Norms and their dual norms are related as follows: $$\| \cdot \|, \| \cdot \|^*$$, the problems 

> $$ \min_x f(x) +\| Ax \|$$
> 
> $$ \max_u -f^*(A^Tu) \text{ subject to } \| u \|^* \leq 1$$

The first expression is the primal, and the second is the dual, which can be solved directly.
