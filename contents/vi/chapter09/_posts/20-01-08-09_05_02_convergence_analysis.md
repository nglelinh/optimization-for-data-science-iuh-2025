---
layout: post
title: '09-05-02 Convergence analysis'
chapter: '09'
order: 8
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

# Convergence analysis

In this section, we analyze the convergence of the accelerated proximal gradient method.

## Convergence Theorem
Suppose $$g$$ is convex and differentiable, $$h$$ is convex, and $$\nabla g$$ is Lipschitz continuous with constant $$L > 0$$. Then, the accelerated proximal gradient method with fixed step size $$t \le 1/L$$ satisfies the following:

> $$f(x^{(k)}) - f^* \le \frac{2L \lVert x^{(0)} - x^* \rVert^2_2}{(k+1)^2}$$

This means the convergence rate is $$O(1/k^2)$$, which is faster than the standard proximal gradient method.

## Backtracking line search
The backtracking line search for the accelerated proximal gradient method is similar to that for the standard proximal gradient method, but the step size is chosen adaptively.

For more details, refer to Beck and Teboulle (2009), "A Fast Iterative Shrinkage-Thresholding Algorithm for Linear Inverse Problems" (FISTA).
