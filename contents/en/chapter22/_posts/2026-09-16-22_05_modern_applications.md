---
layout: post
title: 22-05 Modern applications of Frank–Wolfe
chapter: '22'
order: 6
owner: Nguyen Le Linh
categories:
- chapter22
lang: en
lesson_type: optional
redirect_from:
  - /contents/en/chapter22/22_06_modern_applications/
---

Why would a 1956 algorithm still sit inside 2026 machine learning libraries alongside PyTorch and JAX? Because modern ML repeatedly runs into structured feasible sets—marginal polytopes of sequence labellings, optimal transport couplings, and sparse explanation masks—where projecting onto the constraint set is intractable, yet maximizing a linear score over it is an exact dynamic program or sorting operation. Modern Frank–Wolfe variants (Block-Coordinate FW, Blended Pairwise Conditional Gradients, and stochastic FW) turn those fast combinatorial oracles directly into scalable solvers.

## Background Knowledge Map: Why Projection-Free Optimization Thrives in Modern ML

- **Block-Coordinate Frank–Wolfe (BCFW):** In structural SVMs, the dual constraint set is a Cartesian product of $$n$$ exponential-size marginal polytopes (one per training sequence). BCFW updates a single randomly chosen block per step, reducing $$n$$ expensive Viterbi calls per iteration to just **one**, while keeping $$O(1/k)$$ convergence.
- **Combinatorial Oracles as Linear Minimizers:** Many classic computer science algorithms—Viterbi decoding, Hungarian matching, minimum spanning trees, and 1D quantile sorting—are exact LMOs for convex hulls of combinatorial structures, plugging directly into Frank–Wolfe without relaxation.
- **Structured Sparsity in Model Interpretability:** Constraining saliency masks or sparse neural perturbations to $$k$$-sparse polytopes or $$\ell_1$$ balls naturally yields compact explanations where the iteration count $$k$$ directly caps the number of active atoms.
- **Modern Acceleration (BPCG & Lazy Oracles):** Blended Pairwise Conditional Gradients (BPCG) and lazified LMOs reuse cached atoms to avoid calling the expensive linear oracle on most steps, delivering order-of-magnitude wall-clock speedups over classical FW.

### Step-by-Step Worked Example (Read Slowly): One Block-Coordinate Frank–Wolfe (BCFW) Step

Suppose a structured prediction dual problem has $$n = 2$$ decoupled simplex blocks $$x = (x^{(1)}, x^{(2)}) \in \Delta_2 \times \Delta_2$$, with objective $$f(x^{(1)}, x^{(2)}) = \frac{1}{2}(x_1^{(1)} - 0.7)^2 + \frac{1}{2}(x_1^{(2)} - 0.2)^2$$. Start at $$x_0^{(1)} = (0, 1)^\top$$, $$x_0^{(2)} = (1, 0)^\top$$.

1. **Sample one block uniformly:** Suppose iteration $$k = 1$$ samples block $$i = 1$$ (leaving block 2 untouched—saving 50% of oracle calls here, or $$99.9\%$$ when $$n = 1000$$).
2. **Compute the block partial gradient:**
   $$\nabla_1 f(x_0) = \bigl(x_1^{(1)} - 0.7,\ 0\bigr)^\top = (-0.7,\ 0)^\top.$$
3. **Call the block LMO on $$\Delta_2$$:** Minimize $$\langle (-0.7, 0), s \rangle$$ over $$s \in \Delta_2$$, which picks $$s^{(1)} = (1, 0)^\top$$.
4. **Update only block 1 with exact line search:** Along $$d^{(1)} = s^{(1)} - x_0^{(1)} = (1, -1)^\top$$, we minimize $$\frac{1}{2}((0 + \gamma) - 0.7)^2$$, giving $$\gamma = 0.7$$.
   $$x_1^{(1)} = (1 - 0.7)(0, 1)^\top + 0.7(1, 0)^\top = (0.7, 0.3)^\top, \qquad x_1^{(2)} = (1, 0)^\top.$$
5. **Observe the computational win:** Block 1 hit its exact optimum in a single local LMO call without ever touching block 2’s gradient or oracle.

Frank–Wolfe (conditional gradient) is the algorithm you reach for when the feasible set $$\mathcal{C}$$ has a cheap **linear minimization oracle**

$$
s_k \in \arg\min_{s\in\mathcal{C}}\ \langle \nabla f(x_k), s\rangle
$$

and a *projection* onto $$\mathcal{C}$$ is expensive or destructive of sparsity. The 2010s revival (Jaggi; Lacoste-Julien) is now a 2020s toolkit: structured prediction, optimal transport, and constrained explanations of neural nets. This optional note is four case studies, not a second convergence proof.

## 1. Structured prediction: block-coordinate Frank–Wolfe

A structured-prediction ERM (CRF, structured SVM) has the form

$$
\min_{w}\ \frac{\lambda}{2}\|w\|_2^2 + \frac1n\sum_{i=1}^n \max_{y\in\mathcal{Y}_i}\bigl(\langle w, \phi(x_i,y)\rangle - \delta(y_i,y)\bigr).
$$

The dual is optimization over a product of probability simplices — a Cartesian product on which a **block-coordinate Frank–Wolfe (BCFW)** step is a *loss-augmented inference* call, i.e. the same oracle the structured model already implements. Lacoste-Julien, Jaggi, Schmidt, and Pletscher (ICML 2013) is the classical reference; it is still the reason FW appears in structured-prediction code in 2026.

The same block-coordinate idea moved to **optimal transport**. Fukunaga and Kasai, [arXiv:2205.13766](https://arxiv.org/abs/2205.13766) (2022; conference version ICASSP 2022), apply BCFW — including away-steps and pairwise steps — to a *semi-relaxed* OT problem whose tight marginal constraints would otherwise force a full LP. The linear oracle on each block is a closed-form argmin over a simplex; the output coupling is sparse. Their running application is **color transfer** between images: the transport plan is exactly the kind of sparse, simplex-constrained object FW is designed to keep.

## 2. Unbalanced and 1-D transport

Séjourné, Feydy, Vialard, Trouvé, and Peyré (AISTATS 2022, [PMLR v151](https://proceedings.mlr.press/v151/sejourne22a.html)) put Frank–Wolfe on the *dual* of 1-D unbalanced OT. The linearized subproblem is a *balanced* 1-D OT, which is solvable in linear time after a sort. That is the FW contract in one sentence: replace a hard nonlinear program by a linear oracle you already know how to solve. They also compute 1-D barycenters by the same linearization. When the goal is an *unregularized* UOT solution, FW can beat Sinkhorn; when you want a smooth, GPU-friendly coupling, Sinkhorn still wins. Students should be able to say *why*, not only *which*.

## 3. Constrained explanations of neural nets

Macdonald, Besançon, and Pokutta (ICML 2022, [PMLR v162](https://proceedings.mlr.press/v162/macdonald22a.html)) recast **rate-distortion explanations (RDE)** as a constrained problem and solve it with deterministic and stochastic Frank–Wolfe. Sparsity of a relevance map becomes an $$\ell_1$$-ball (or a simplex) constraint; a *feature-ordering* variant optimizes over the **Birkhoff polytope** (the convex hull of permutation matrices), whose linear oracle is an assignment problem. On image-classification benchmarks the multi-rate and ordering variants beat vanilla RDE. This is structured prediction in disguise: the “structure” is a polytope that encodes a human-readable explanation, and FW never materializes a projection onto that polytope.

## 4. A 2024 survey to keep on the desk

Bomze, Rinaldi, and Zeffiro, **“Frank–Wolfe and friends: a journey into projection-free first-order optimization methods”**, *Ann. Oper. Res.* 343:607–638, 2024, [doi:10.1007/s10479-024-06251-7](https://doi.org/10.1007/s10479-024-06251-7), It walks through traffic assignment, submodular optimization, matrix completion, adversarial attacks, SVM training, and maximal-clique search, and explains the 2020s variants (away-steps, pairwise, sliding, stochastic). Use it when you need a *menu*, not when you need a proof.

## When FW still beats projected gradient in 2026

Use Frank–Wolfe when (i) $$\mathcal{C}$$ is a polytope, spectrahedron, or flow polytope whose LMO is a sort, an assignment, or an eigenvalue, and (ii) you *want* the iterate to stay a sparse convex combination of atoms. Use a projection method when the projection is a cheap clip (box, simplex with Michelot) and you need a linear rate that vanilla FW will not give you without away-steps.

**Exercise.** Color-transfer toy: two 1-D histograms $$a,b\in\Delta^{k}$$ and a cost $$C_{ij}=(i-j)^2$$. Run (i) 40 FW steps on the transportation polytope (LMO = a transportation problem you may solve with `scipy.optimize.linprog` on a tiny $$k=12$$) and (ii) projected gradient on the same polytope. Compare the number of nonzeros in the plan and the OT cost. FW should be sparser; PGD should drop the cost faster in the first few steps if you project exactly.

## Sources

- M. Jaggi, ICML 2013 — FW duality gap and affine-invariant rates.
- S. Lacoste-Julien, M. Jaggi, M. Schmidt, P. Pletscher, ICML 2013 — BCFW for structured SVMs.
- T. Fukunaga and H. Kasai, [arXiv:2205.13766](https://arxiv.org/abs/2205.13766), 2022 / ICASSP 2022 — BCFW for semi-relaxed OT, color transfer.
- T. Séjourné et al., AISTATS 2022, [PMLR v151](https://proceedings.mlr.press/v151/sejourne22a.html) — FW for 1-D unbalanced OT.
- J. Macdonald et al., ICML 2022, [PMLR v162](https://proceedings.mlr.press/v162/macdonald22a.html) — FW for rate-distortion explanations.
- I. M. Bomze, F. Rinaldi, D. Zeffiro, *Ann. Oper. Res.*, 2024, [doi:10.1007/s10479-024-06251-7](https://doi.org/10.1007/s10479-024-06251-7) — “Frank–Wolfe and friends.”
