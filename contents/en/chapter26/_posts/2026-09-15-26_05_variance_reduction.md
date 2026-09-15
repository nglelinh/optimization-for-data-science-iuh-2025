---
layout: post
title: 26-05 Variance reduction (survey)
chapter: '26'
order: 6
owner: Nguyen Le Linh
categories:
- chapter26
lang: en
lesson_type: required
---


SGD’s $$O(1/\sqrt{T})$$ ceiling on convex finite sums is not information-theoretic destiny. If each $$f_i$$ is smooth, **variance-reduced** methods reuse old gradients so that the estimator becomes exact at a snapshot, and the noise dies as $$w$$ approaches a minimizer.

**SVRG** (Johnson & Zhang, 2013) keeps a snapshot $$\tilde w$$ and a full gradient $$\mu=\nabla F(\tilde w)$$, then steps

$$
g_k = \nabla f_{I_k}(w_k) - \nabla f_{I_k}(\tilde w) + \mu.
$$

At $$w_k=\tilde w$$ one has $$g_k=\nabla F(\tilde w)$$ exactly. Periodically refresh the snapshot (one full pass). **SAGA** (Defazio, Bach, Lacoste-Julien, 2014) stores a table of the last gradient of each $$f_i$$ and updates one row per step — more memory, no explicit inner loop.

For *strongly convex finite-sum* problems these methods can achieve linear convergence in the number of incremental steps, something vanilla SGD cannot. For **deep nets**, storing a gradient table is usually hopeless, and the empirical winner is still large-batch Adam(W) plus a schedule. Learn SVRG so that you can read Opt-for-ML notes (MIT, BU EC525) and so that you recognize when a *convex* ERM (logistic regression, linear SVM) should *not* be trained with Adam out of habit.

**One-page takeaway**

| Method | Extra memory | Typical home |
|--------|--------------|--------------|
| SGD / mini-batch | none | deep learning |
| SVRG | one snapshot + full gradient | convex finite-sum |
| SAGA | one gradient per example | medium convex ERM |
| AdamW | two EMAs | default DL |

**Exercise.** On a strongly convex ridge-logistic problem with $$n=5000$$, compare wall-clock of SVRG vs SGD to reach training gradient norm $$10^{-4}$$. Then try the same budget on a one-hidden-layer net — SVRG’s snapshot cost should look less charming.
