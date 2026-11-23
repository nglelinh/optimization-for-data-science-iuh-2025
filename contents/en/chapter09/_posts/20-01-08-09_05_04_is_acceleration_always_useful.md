---
layout: post
title: '09-05-04 Is acceleration always useful?'
chapter: '09'
order: 10
owner: Kyeongmin Woo
categories:
- chapter09
lang: en
---

# Is acceleration always useful?

Acceleration methods such as FISTA can achieve faster convergence rates in theory, but in practice, acceleration is not always beneficial.

## When acceleration may not help
- If the problem is well-conditioned (small condition number $$\kappa = L/\mu$$), plain proximal gradient already converges fast, at a linear rate. Acceleration gains little, and the momentum can even make it a bit slower. For example, on a 2D lasso with $$\kappa = 3$$, ISTA needs 14 iterations and FISTA needs 16.
- Acceleration helps most when the problem is ill-conditioned (large $$\kappa$$). There, plain proximal gradient is slow, and FISTA cuts the number of iterations by a large factor. The price is that the objective value can oscillate.
- With a non-smooth $$g$$, or when $$\nabla g$$ has no useful Lipschitz constant, the $$O(1/k^2)$$ guarantee does not apply.
- The "Nesterov ripples" phenomenon makes the objective value non-monotonic: it can go up for some iterations before it goes down again.

## Practical advice
- Use acceleration when the smooth part is ill-conditioned; that is where it pays off most.
- When the problem is well-conditioned, plain proximal gradient is often enough.
- Monitor the objective value. If the ripples are large, use a restart scheme (reset $$t_k = 1$$ when the objective goes up) instead of giving up acceleration.
