---
layout: post
title: 22-07 Modern applications of Frank–Wolfe
chapter: '22'
order: 8
owner: Nguyen Le Linh
categories:
- chapter22
lang: en
lesson_type: optional
---

As optimization scales to high-dimensional structured domains—from sequence tagging and unbalanced optimal transport to sparse neural explanations—the bottleneck is rarely computing a gradient; it is enforcing the structural constraint. Projection-free Frank–Wolfe methods turn what would be an intractable quadratic projection into a fast linear oracle, bridging classical 1956 convex optimization with 2024–2026 machine learning pipelines.

## Key ideas: Selecting Frank–Wolfe in Modern Applied Workflows

- **Oracle Complexity Asymmetry:** Frank–Wolfe beats projected gradient descent precisely when the Linear Minimization Oracle is asymptotically cheaper than Euclidean projection (e.g., $$O(d)$$ vs. $$O(d \log d)$$ on structured polytopes, or top-1 SVD vs. full SVD on trace-norm balls).
- **Block-Coordinate Scalability:** Decomposing product constraints $$\mathcal{C} = \mathcal{C}_1 \times \dots \times \mathcal{C}_n$$ via Block-Coordinate FW allows stochastic per-example updates while preserving global primal-dual gap certificates.
- **Unbalanced & 1D Optimal Transport:** In transport problems with relaxed marginal penalties, linear subproblems decompose cleanly over rows/columns or 1D orderings, making conditional gradients competitive with Sinkhorn iterations when exact sparse couplings are preferred over entropic blur.
- **Sparsity-Accuracy Trade-off via Iteration Budget:** Because each FW step adds at most one atom, stopping early at $$k$$ iterations acts simultaneously as computational budgeting and explicit structural regularization (e.g., rank-$$k$$ matrices or $$k$$-sparse explanations).

### Worked example: Comparing LMO vs. Projection Cost on a $$2 \times 2$$ Trace-Norm Step

Suppose we minimize a matrix loss with current iterate $$X_0 = 0 \in \mathbb{R}^{2 \times 2}$$ over the trace-norm ball $$\|X\|_{\text{tr}} \le 3$$, and the gradient is $$G = \begin{pmatrix} -4 & 0 \\ 0 & -2 \end{pmatrix}$$.

1. **Frank–Wolfe LMO (rank-1 only):** We only need the largest singular value $$\sigma_1 = 4$$ with $$u_1 = (1, 0)^\top$$, $$v_1 = (-1, 0)^\top$$.
   $$S_0 = -3 u_1 v_1^\top = \begin{pmatrix} 3 & 0 \\ 0 & 0 \end{pmatrix}.$$
   With step size $$\gamma = \frac{1}{2}$$, $$X_1^{\text{FW}} = \begin{pmatrix} 1.5 & 0 \\ 0 & 0 \end{pmatrix}$$—strictly **rank 1**.
2. **Projected Gradient Step (full SVD + simplex projection):** With step size $$\eta = 1$$, the unprojected step is $$Y = X_0 - G = \begin{pmatrix} 4 & 0 \\ 0 & 2 \end{pmatrix}$$, whose singular values $$(4, 2)$$ sum to $$6 > 3$$. Projecting $$(4, 2)$$ onto the $$\ell_1$$ ball of radius $$3$$ requires soft-thresholding by $$\tau = 1.5$$, giving singular values $$(2.5, 0.5)$$ and $$X_1^{\text{PGD}} = \begin{pmatrix} 2.5 & 0 \\ 0 & 0.5 \end{pmatrix}$$—**rank 2**.
3. **Key Takeaway:** Even on a $$2 \times 2$$ toy problem, PGD requires *all* singular values and immediately inflates rank, whereas FW needs only the top singular pair and preserves low-rank structure automatically.

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
