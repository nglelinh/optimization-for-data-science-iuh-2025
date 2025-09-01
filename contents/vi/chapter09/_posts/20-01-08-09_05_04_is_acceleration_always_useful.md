---
layout: post
title: '09-05-04 Is acceleration always useful?'
chapter: '09'
order: 10
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

# Is acceleration always useful?

Acceleration methods such as FISTA can achieve faster convergence rates in theory, but in practice, acceleration is not always beneficial.

## When acceleration may not help
- If the problem is ill-conditioned, acceleration can cause oscillations or instability.
- For some non-smooth problems, acceleration may not improve convergence.
- The "Nesterov ripples" phenomenon can cause non-monotonic behavior in the objective value.

## Practical advice
- Use acceleration methods when the problem is well-conditioned and smooth.
- Monitor convergence and stability when applying acceleration.
- If instability occurs, consider switching to standard proximal gradient methods.