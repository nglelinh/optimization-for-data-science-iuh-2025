---
layout: post
title: 13-04-03 Shifting linear transformations
chapter: '13'
order: 8
owner: Wontak Ryu
categories:
- chapter13
lang: en
---

Consider fused-lasso or total-variation denoising: $$\min_x \frac{1}{2}\|x - y\|_2^2 + \lambda\|Dx\|_1$$, where $$D$$ is a finite-difference matrix. Because $$D$$ sits *inside* the nonsmooth $$\ell_1$$ norm, you cannot apply coordinate-wise soft-thresholding directly to $$x$$. Duality performs a neat sleight of hand: by introducing $$z = Dx$$, it migrates the matrix out of the nonsmooth term $$g$$ and attaches its transpose $$D^T$$ to the smooth conjugate $$f^*$$—turning a hard nonsmooth problem into a smooth quadratic over a simple box!

## Key ideas: Migrating Linear Maps via Duality

- **Pillar 1 — The Linear-Composition Bottleneck:** Even when $$f$$ and $$g$$ are each simple to minimize alone, composing a nonsmooth $$g$$ with a linear operator $$A$$ (as in $$g(Ax)$$) couples coordinates and breaks closed-form proximal steps.
- **Pillar 2 — Splitting $$Ax = z$$ Transfers $$A$$ to $$A^T$$:** Forming $$L(x,z,u) = f(x) + g(z) + u^T(z - Ax)$$ pairs $$x$$ with $$A^T u$$ and $$z$$ with $$-u$$, producing the Fenchel dual $$\max_u -f^*(A^T u) - g^*(-u)$$.
- **Pillar 3 — Smoothness Swap:** When $$f$$ is strongly convex (so $$f^*$$ is smooth) and $$g(\cdot) = \|\cdot\|$$ is a norm, the dual $$\max_{\|u\|_*\le 1} -f^*(A^T u)$$ is a *smooth* maximization over a simple dual-norm ball—ideal for projected gradient or L-BFGS.
- **Pillar 4 — Primal Recovery via Conjugate Gradient:** Once $$u^\star$$ is found, $$x^\star = \nabla f^*(A^T u^\star)$$ reconstructs the primal solution directly.

### Worked example: 1D Total-Variation Denoising via Shifting $$D$$

Minimize $$f(x) + g(Dx) = \frac{1}{2}\|x - y\|_2^2 + \|Dx\|_1$$ for $$y = \begin{bmatrix} 0 \\ 4 \end{bmatrix}$$ and $$D = \begin{bmatrix} -1 & 1 \end{bmatrix}$$ (so $$Dx = x_2 - x_1$$).

1. **Compute conjugates:**
   - $$f^*(w) = \frac{1}{2}\|w\|_2^2 + y^T w$$ (minimizer $$x = y + w$$).
   - $$g^*(-u) = I_{\{|u| \le 1\}}(u)$$ for scalar $$u \in \mathbb{R}$$.
2. **Shift $$D$$ to $$f^*$$ in the dual:** Since $$D^T u = \begin{bmatrix} -u \\ u \end{bmatrix}$$,
   $$-f^*(D^T u) = -\frac{1}{2}\big((-u)^2 + u^2\big) - \big(0(-u) + 4u\big) = -u^2 - 4u.$$
   The dual problem is $$\max_{|u| \le 1} (-u^2 - 4u)$$.
3. **Solve the 1D box-constrained quadratic:** The unconstrained peak of $$-u^2 - 4u$$ is at $$u = -2$$. Clipping to $$[-1, 1]$$ gives $$u^\star = -1$$, with dual value $$-(-1)^2 - 4(-1) = 3$$.
4. **Recover $$x^\star = y + D^T u^\star$$:**
   $$x^\star = \begin{bmatrix} 0 \\ 4 \end{bmatrix} + \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 1 \\ 3 \end{bmatrix}.$$
5. **Verify strong duality:** Primal value at $$x^\star = (1,3)^T$$ is $$\frac{1}{2}((1-0)^2 + (3-4)^2) + |3-1| = 1 + 2 = 3$$, matching the dual value $$3$$!

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

#### [Example]
Norms and their dual norms are related as follows: $$\| \cdot \|, \| \cdot \|^*$$, the problems 

> $$ \min_x f(x) +\| Ax \|$$
> 
> $$ \max_u -f^*(A^Tu) \text{ subject to } \| u \|^* \leq 1$$

The first expression is the primal, and the second is the dual, which can be solved directly.
