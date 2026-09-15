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


# Nonconvex landscapes for deep learning

Convexity was the safety rail of Chapters 02–25: local minima are global, and first-order conditions certify optimality. A deep network’s training loss $$F(w)$$ is **nonconvex**. This chapter does not throw the rail away; it asks what *kind* of nonconvexity practitioners actually meet.

We will distinguish **critical points** ($$\nabla F(w)=0$$) by the inertia of the Hessian: minima, maxima, and **saddles**. We will see why high-dimensional saddles, not swampy local minima, are the usual obstruction, and why **overparameterization** (more parameters than data constraints) can make almost all minima interpolate — the modern “why does SGD work?” story at IUH depth.

EPFL CS-439 and USC CSCI 599 treat this as an advanced but expected module. We stay at the level of precise definitions plus pictures, not mean-field PDE limits.

Open [loss_function_landscapes.html](https://nglelinh.github.io/interactive_math/optimization/loss_function_landscapes.html) while you read.

## Lessons

1. Critical points and saddles
2. Escaping saddles and landscape geometry
3. Overparameterization (and a pointer to the PL condition)

Further reading: Karimi, Nutini, Schmidt, *Linear Convergence … under the Polyak–Łojasiewicz condition*, [arXiv:1608.04636](https://arxiv.org/abs/1608.04636) — the simplest bridge from the strongly convex proofs you already know to some nonconvex ERMs.
