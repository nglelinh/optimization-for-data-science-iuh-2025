---
layout: post
title: 29-03 ADMM versus data-parallel and FedAvg
chapter: '29'
order: 4
owner: Nguyen Le Linh
categories:
- chapter29
lang: en
lesson_type: required
---


[Chapter 21]({{ site.baseurl }}/contents/en/chapter21/) studies the **alternating direction method of multipliers**. In consensus form one solves

$$
\min_{x_1,\ldots,x_P,z} \sum_{p=1}^P f_p(x_p) \quad\text{subject to}\quad x_p=z,
$$

by an augmented-Lagrangian saddle: primal $$x_p$$-updates (often proximal), a $$z$$-average, and a dual ascent on the residuals. When each $$f_p$$ is convex and the steps are exact, ADMM has a mature convergence theory and is the right tool for **structured convex** splits (distributed Lasso, consensus QP, some SDP relaxations).

Data-parallel SGD and FedAvg live in a different design space:

| | ADMM (Ch.21) | Data-parallel SGD | FedAvg |
|--|--------------|-------------------|--------|
| Typical $$f$$ | convex, often composite | nonconvex ERM / deep net | nonconvex, *heterogeneous* local ERM |
| What is averaged | primal $$z$$ and duals | **gradients** (or synced weights) each step | **weights** after $$E$$ local steps |
| Dual variables | yes, residuals drive consensus | no | no |
| Scarce resource | iterations of a modest-sized convex problem | interconnect bandwidth every step | **rounds** (devices sleep, Wi-Fi) |
| Certificate | duality gap / residual | none (nonconvex) | none |

Calling FedAvg “ADMM without the dual” hides the point: FedAvg *intentionally* lets clients drift, then averages parameters. ADMM *penalizes* disagreement every iteration. Use ADMM when you can write a convex consensus program and want residuals you can monitor. Use data-parallel SGD when you are training one shared net on a cluster you control. Use FedAvg when the data cannot move and communication is expensive.

A practical IUH lab: three clients, one convex logistic objective split by samples — solve with (i) ADMM consensus and (ii) FedAvg with $$E\in\{1,5\}$$. Compare training loss versus *communication rounds*, not versus local gradient evaluations.

**Question.** In what scenarios might a projection-free or splitting method (Frank–Wolfe, ADMM) still beat data-parallel SGD on a cluster — even in 2026?
