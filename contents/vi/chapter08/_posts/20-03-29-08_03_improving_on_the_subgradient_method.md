---
layout: post
title: '08-03 Improving on the Subgradient Method'
chapter: '08'
order: 16
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

The subgradient method is advantageous because it can be used for nondifferentiable convex functions, making it more general. However, its convergence rate is $$O(1/\epsilon^{2})$$, which is much slower than the convergence rate of gradient descent, $$O(1/\epsilon)$$.

Is there a way to combine the strengths of gradient descent and the subgradient method? In the next section, we will learn about the proximal gradient descent method, which combines the advantages of both algorithms.