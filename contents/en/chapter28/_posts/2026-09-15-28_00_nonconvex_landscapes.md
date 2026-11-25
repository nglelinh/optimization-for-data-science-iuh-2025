---
layout: post
title: 28 Nonconvex landscapes for deep learning
chapter: '28'
order: 1
owner: Nguyen Le Linh
categories:
- chapter28
lang: en
lesson_type: required
---

For twenty-five chapters, convexity was our mathematical safety rail: every local minimum was automatically global, and finding $$\nabla F(w) = 0$$ meant the job was finished. Yet deep neural networks tear off that safety rail completely—their loss surfaces are wildly nonconvex, teeming with symmetries, flat plateaus, and exponentially many saddle points. Why, then, does simple stochastic gradient descent routinely drive a billion-parameter network straight down to near-zero training loss? Chapter 28 unpacks the modern geometry of nonconvex optimization: why saddle points outnumber bad local minima in high dimensions, how noise escapes them, why overparameterization smooths the landscape, and how the Polyak–Łojasiewicz (PL) condition recovers fast linear convergence without convexity.

## Key ideas: Navigating Nonconvex Loss Landscapes

- **First-Order vs. Second-Order Stationarity:** Without convexity, $$\nabla F(w) = 0$$ only certifies a *critical point* (minimum, maximum, or saddle). Avoiding strict saddles requires second-order stationarity: $$\nabla F(w) = 0$$ and $$\nabla^2 F(w) \succeq 0$$.
- **High-Dimensional Saddle Dominance:** In $$d$$ dimensions, a critical point is a local minimum only if all $$d$$ Hessian eigenvalues are positive—an event whose probability vanishes exponentially as $$d$$ grows. Thus the primary obstacle in deep learning is escaping **saddle points**, not bad local minima.
- **Overparameterization & Connected Solution Manifolds:** When $$d \gg n$$, global minima are no longer isolated points; they form high-dimensional connected valleys (mode connectivity), making it easy for gradient trajectories from almost any random initialization to reach a zero-loss basin.
- **Beyond Convexity — The PL Condition:** Even when $$F$$ is nonconvex with non-unique minima, the gradient-dominance inequality $$\frac{1}{2}\|\nabla F(w)\|_2^2 \ge \mu (F(w) - F^\star)$$ guarantees that every stationary point is global and restores linear convergence for plain gradient descent.

### Worked example: A Nonconvex Function with Multiple Global Minima and a Saddle

Consider the classic 1D symmetric double-well potential $$F(w) = \frac{1}{4}(w^2 - 1)^2$$.

1. **Find all critical points ($$F'(w) = 0$$):**
   $$F'(w) = w(w^2 - 1) = 0 \implies w \in \{-1,\ 0,\ +1\}.$$
2. **Classify each critical point via the second derivative $$F''(w) = 3w^2 - 1$$:**
   - At $$w = 0$$: $$F(0) = 0.25$$ and $$F''(0) = -1 < 0$$ (local maximum / strict 1D saddle—unstable!).
   - At $$w = \pm 1$$: $$F(\pm 1) = 0$$ and $$F''(\pm 1) = +2 > 0$$ (two symmetric global minima!).
3. **Check convexity vs. optimizability:** Because $$F''(0) = -1 < 0$$, $$F$$ is **nonconvex**, and the midpoint $$0 = \frac{1}{2}(-1) + \frac{1}{2}(+1)$$ has strictly higher loss ($$0.25 > 0$$) than both global minima. Yet from *any* starting point $$w_0 \ne 0$$, gradient descent slides effortlessly into one of the two global minima $$w^\star = \pm 1$$—showing why nonconvexity alone does not imply hardness!

# Nonconvex landscapes for deep learning

Convexity was the safety rail of Chapters 02–25: local minima are global, and first-order conditions certify optimality. A deep network’s training loss $$F(w)$$ is **nonconvex**. This chapter does not throw the rail away; it asks what *kind* of nonconvexity practitioners actually meet.

We will distinguish **critical points** ($$\nabla F(w)=0$$) by the inertia of the Hessian: minima, maxima, and **saddles**. We will see why high-dimensional saddles, not swampy local minima, are the usual obstruction, and why **overparameterization** (more parameters than data constraints) can make almost all minima interpolate — the modern “why does SGD work?” story at IUH depth.

EPFL CS-439 and USC CSCI 599 treat this as an advanced but expected module. We stay at the level of precise definitions plus pictures, not mean-field PDE limits.

Open [loss_function_landscapes.html](https://nglelinh.github.io/interactive_math/optimization/loss_function_landscapes.html) while you read.

## Lessons

1. Critical points and saddles
2. Escaping saddles and landscape geometry
3. Overparameterization (and a pointer to the PL condition)
4. Modern landscape case studies (optional) — mode connectivity, grokking, double descent, flat minima
5. The PL condition and modern rates (optional) — Karimi et al.; reuse of the Chapter 06 linear rate without convexity

The PL bridge from the strongly convex proofs of 06-03-04 to some nonconvex ERMs is now a lesson, not only an arXiv pointer: [28-05]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}). The 2022–2026 phenomena sit in [28-04]({% multilang_post_url contents/chapter28/2026-09-16-28_04_modern_landscapes %}).
