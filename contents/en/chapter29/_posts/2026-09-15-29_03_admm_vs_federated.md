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

If you already learned Consensus ADMM in Chapter 21, a sharp question should immediately occur to you: both Consensus ADMM and FedAvg solve $$\min_w \sum_{p=1}^P f_p(w)$$ across distributed workers without sharing raw data—so why didn’t federated deep learning just use ADMM? Putting the two algorithms side by side reveals one of optimization’s clearest design trade-offs: ADMM maintains per-client dual variables that *provably cancel client drift* on convex problems, while FedAvg stays stateless so millions of intermittent, nonconvex mobile devices can drop in and out without ever storing stale dual multipliers.

## Key ideas: Consensus ADMM vs. Data-Parallel SGD vs. FedAvg

- **Dual Memory Kills Client Drift (ADMM):** In Consensus ADMM, each worker $$p$$ minimizes $$f_p(x_p) + \frac{\rho}{2}\|x_p - z + u_p\|_2^2$$. The dual variable $$u_p$$ remembers the exact gradient discrepancy $$\nabla f_p(z^\star)$$ at the global optimum, guaranteeing convergence to the *exact* global minimizer $$z^\star$$ even under extreme non-IID heterogeneity!
- **Why Statelessness Matters in Cross-Device FL:** Cross-device federated learning involves millions of phones where any given device may appear once a week. Maintaining fresh per-client dual state $$u_p$$ becomes stale or impossible—favoring stateless FedAvg.
- **Exact Subproblem Cost vs. Cheap Local SGD:** Classical ADMM assumes each worker solves (or closely approximates) its proximal subproblem $$\arg\min_{x_p} f_p(x_p) + \frac{\rho}{2}\|x_p - z + u_p\|_2^2$$, which is fast for convex GLMs or cross-silo hospitals but expensive for deep neural nets compared to a few local SGD steps.
- **Three-Way Decision Matrix:** Use **Data-Parallel SGD** on fast datacenter GPUs; use **Consensus ADMM** on convex or cross-silo (10–50 always-on institutions) problems with strong heterogeneity; use **FedAvg** (or FedProx/FedAdam) on large-scale, nonconvex, intermittent device fleets.

### Worked example: How ADMM’s Dual Variable Cures the Exact Drift That Broke FedAvg

Return to the exact 2-client non-IID problem from Lesson 29-02 where FedAvg drifted away from $$w^\star = 0.6$$:
$$f_1(x) = 2(x - 1)^2, \qquad f_2(x) = \frac{1}{2}(x + 1)^2, \qquad z^\star = 0.6.$$
Check whether $$z = 0.6$$ is a **fixed point** of Consensus ADMM (with $$\rho = 1$$)!

1. **Compute the optimal scaled dual variables $$u_1^\star, u_2^\star$$ at consensus $$x_1 = x_2 = z = 0.6$$:**
   At stationarity of $$f_p(x_p) + \frac{\rho}{2}(x_p - z + u_p)^2$$, we need $$f_p'(z) + \rho u_p^\star = 0 \implies u_p^\star = -f_p'(z)/\rho$$:
   - Client 1: $$f_1'(0.6) = 4(0.6 - 1) = -1.6 \implies u_1^\star = +1.6$$.
   - Client 2: $$f_2'(0.6) = (0.6 + 1) = +1.6 \implies u_2^\star = -1.6$$.
   Notice $$u_1^\star + u_2^\star = 0$$!
2. **Now run one full ADMM round from $$z = 0.6,\ u_1 = 1.6,\ u_2 = -1.6$$:**
   - Client 1 minimizes $$2(x_1 - 1)^2 + \frac{1}{2}(x_1 - 0.6 + 1.6)^2 = 2(x_1 - 1)^2 + \frac{1}{2}(x_1 + 1)^2$$:
     $$4(x_1 - 1) + (x_1 + 1) = 0 \implies 5x_1 = 3 \implies x_1^+ = 0.6!$$
   - Client 2 minimizes $$\frac{1}{2}(x_2 + 1)^2 + \frac{1}{2}(x_2 - 0.6 - 1.6)^2 = \frac{1}{2}(x_2 + 1)^2 + \frac{1}{2}(x_2 - 2.2)^2$$:
     $$(x_2 + 1) + (x_2 - 2.2) = 0 \implies 2x_2 = 1.2 \implies x_2^+ = 0.6!$$
   - Server consensus update: $$z^+ = \frac{x_1^+ + x_2^+}{2} = 0.6$$!
3. **Key Insight:** Even when both clients solve their local subproblems *all the way to exact optimality*, the dual variables $$u_1^\star = +1.6$$ and $$u_2^\star = -1.6$$ exert exact counter-forces that hold both clients pinned at $$z^\star = 0.6$$—zero drift!

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
