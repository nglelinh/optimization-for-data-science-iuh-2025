---
layout: post
title: "19-06 Proximal quasi-Newton methods"
chapter: '19'
order: 10
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

As problems grow larger, computing the Hessian becomes very expensive. **Proximal quasi-Newton methods** avoid computing the Hessian $$H^{(k-1)} = \nabla^2 g(x^{(k-1)})$$ at each step, while still achieving a superlinear or linear convergence rate.

## Proximal quasi-Newton method
* Lee (2014) proposed updating the Hessian approximation in the BFGS style. This method works very well and has a local superlinear convergence rate.
* Tseng and Yun (2009) proposed approximating the Hessian blockwise. This works only when $$f = g + h$$ can be split into parts in which $$h$$ depends on only some of the optimization variables. Computing the Hessian blockwise is much faster. This method has a linear convergence rate.

Quasi-Newton methods are useful not only when the Hessian is hard to compute, but also in ill-conditioned problems where the Hessian is singular or nearly singular.

#### References
* J. Lee and Y. Sun and M. Saunders (2014), "Proximal Newton-type methods for minimizing composite functions"
* P. Tseng and S. Yun (2009), "A coordinate gradient descent method for nonsmooth separable minimization"
