---
layout: post
title: 17 Primal-Dual Interior-Point Methods
chapter: '17'
order: 1
owner: Minjoo Lee
categories:
- chapter17
lang: en
---

In this chapter, we will examine the **Primal-Dual Interior-Point Method**, which improves performance by reducing the centering step of the Barrier method we learned earlier to a single step.

The **Primal-Dual Interior-Point Method** relaxes the constraint that the centering step must be feasible and uses the root finding version of Newton's Method to approximate nonlinear equations with linear equations to find solutions, making it faster and more accurate than the Barrier method.

## References and further readings
* S. Boyd and L. Vandenberghe (2004), “Convex optimization,” Chapter 11
* S. Wright (1997), “Primal-dual interior-point methods,” Chapters 5 and 6
* J. Renegar (2001), “A mathematical view of interior-point methods”
* Y. Nesterov and M. Todd (1998), “Primal-dual interior-point methods for self-scaled cones.” SIAM J. Optim.