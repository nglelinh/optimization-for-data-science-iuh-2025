---
layout: post
title: "19-03 When would we use proximal Newton?"
chapter: '19'
order: 7
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

When is the proximal Newton method a good choice?

To understand when it is useful, let us compare the proximal Newton method with proximal gradient descent on the following problem.

**Problem**: $$\min_x g(x) + h(x)$$

## Proximal gradient descent vs. proximal Newton

| **Proximal gradient descent** |**Proximal Newton** | 
| -------- | -------- |
| Minimizes $$\frac{1}{2} \parallel b - x \parallel_2^2 + h(x)$$ at each step | Minimizes $$b^T x + x^T A x + h(x)$$ at each step | 
| The prox operator is usually available in closed form | The prox operator usually has no closed form |
| Cheap iterations | Very expensive iterations (more expensive than Newton's method) | 
| Convergence rate of gradient descent <br> $$O(1/\epsilon)$$ | Convergence rate of Newton's method <br> $$O(\log \log 1/\epsilon)$$ | 

The two methods look similar, but they actually do very different things.

Therefore, the proximal Newton method is worth using when we have a fast inner optimizer for the scaled prox problem (quadratic $$+\ h$$), so that very few outer iterations are needed. When $$h$$ is a separable function, the most commonly used inner optimizer is coordinate descent.
