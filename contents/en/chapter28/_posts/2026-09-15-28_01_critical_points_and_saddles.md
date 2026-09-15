---
layout: post
title: 28-01 Critical points and saddles
chapter: '28'
order: 2
owner: Nguyen Le Linh
categories:
- chapter28
lang: en
lesson_type: required
---


Let $$F:\mathbb{R}^d\to\mathbb{R}$$ be twice continuously differentiable. A point $$w$$ is **critical** if $$\nabla F(w)=0$$. The Hessian $$H=\nabla^2 F(w)$$ then classifies the critical point *when it is nondegenerate* (no zero eigenvalue):

- **Strict local minimum:** $$H\succ 0$$ (all eigenvalues positive).
- **Strict local maximum:** $$H\prec 0$$.
- **Strict saddle:** $$H$$ is indefinite — at least one positive and one negative eigenvalue.

If some eigenvalues vanish, the test is inconclusive (think $$w\mapsto w^3$$ or a plateau). Deep losses are full of near-degenerate directions.

**First-order methods do not see $$H$$**, but the local Taylor story still explains their behavior: along a negative-curvature direction $$u$$, $$F(w+t u)\approx F(w)+\tfrac12 t^2 u^\top H u$$ *decreases* for small $$t\neq 0$$. A saddle is not a trap for an algorithm that can move in that direction; it is a trap for algorithms that only look at $$\|\nabla F\|$$ being small and stop.

In high dimension, if eigenvalues of a “typical” Hessian at a critical point behave like a random symmetric matrix, the probability that *all* of them are positive is exponentially small. The folk theorem you should remember: **most critical points of high-dimensional generic functions are saddles, not minima**. Deep-learning losses are not generic Gaussians — but the intuition is why “getting stuck in local minima” is usually the wrong diagnosis after epoch 2.

**Exercise.** For $$F(x,y)=x^2-y^2$$ (the hyperbolic paraboloid) write $$\nabla F$$ and $$H$$. Starting at $$(0,10^{-3})$$, take two gradient steps. Starting at $$(0,0)$$, explain why GD with exact arithmetic never leaves.
