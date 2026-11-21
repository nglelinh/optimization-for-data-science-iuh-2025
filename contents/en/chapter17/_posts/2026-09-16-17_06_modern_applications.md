---
layout: post
title: 17-06 Modern applications of primal-dual interior-point methods (2022–2026)
chapter: '17'
order: 10
owner: Nguyen Le Linh
categories:
- chapter17
lang: en
lesson_type: optional
---

A primal-dual interior-point method takes *one* Newton step on the perturbed KKT map

$$
r_t(x,u,v) = 0
$$

instead of driving a barrier problem to high accuracy at every $$t$$. The objects you computed in this chapter — the surrogate duality gap $$-h(x)^\top u$$, the primal and dual residuals, the linearised complementarity block $$U\nabla h(x)\,\Delta x + H(x)\,\Delta u = -Uh(x) - (1/t)\mathbf{1}$$ — are exactly the residuals modern cone solvers print. The 2022–2026 story is that those solvers became the default Python backend, then moved onto GPUs, and then ran into the limits of SDP relaxations for neural-network verification.

## Clarabel: PD-IPM as a library, not a homework exercise

Clarabel (Goulart & Chen, 2024) implements a homogeneous primal-dual interior-point iteration for quadratic objectives over a product of symmetric and nonsymmetric cones. Relative to a textbook PD-IPM it adds: a homogeneous embedding (so infeasible and unbounded instances have well-posed central paths), Mehrotra-style correctors, and a sparse LDL factorisation of the KKT Newton system. The authors report that the solver is faster and more robust than several commercial and open-source competitors on standard benchmarks, *especially* on QPs — the case this chapter's Newton system was built for.

CVXPY 1.5 made Clarabel the default engine for the problem classes that previously fell through to ECOS. A student who writes `prob.solve()` on an SOCP is therefore running Chapter 17, not a simplex tableau. The dual variables returned by CVXPY are the $$u,v$$ of this chapter; the complementarity residual is the surrogate gap. That single fact is worth more than a new derivation: *you already have a PD-IPM on your laptop*.

## CuClarabel: the same Newton system on a GPU

Chen, Tse, Nobel, Goulart, and Boyd (2024) port the iteration to NVIDIA GPUs as **CuClarabel**. The algorithm is still a primal-dual interior-point method: a setup phase equilibrates data, a solve phase builds and factors the Newton system, and cones are processed with a mixed parallel strategy (linear constraints first, then other cones in parallel). The linear algebra is delegated to NVIDIA cuDSS, with an optional mixed-precision factorisation. Supported cones include the zero and nonnegative cones, second-order, exponential and power cones, and same-dimension PSD cones. The paper shows GPU IPM beating CPU IPM across a range of conic programs; the public examples include a portfolio QP — the same SOCP you can write in JuMP or CVXPY.

This is the complexity discussion of Chapter 17 made concrete. The bottleneck of PD-IPM was never the three-line update; it was the KKT factorisation. Once that factorisation is a GPU sparse direct solve, interior-point methods become plausible for the cone sizes that data-science pipelines actually emit (thousands to tens of thousands of variables), while first-order splitting remains the tool for millions of variables with modest accuracy.

## SDP relaxations for neural-network verification

Semidefinite relaxations of ReLU networks produce an SDP whose optimal value certifies robustness (Raghunathan, Steinhardt, Liang, and the line of SDP-NN verifiers). Those SDPs are solved by primal-dual interior-point methods when a *certificate* is required: first-order methods may look converged without a duality-gap proof. A 2025 analysis, “Interior-Point Vanishing Problem in Semidefinite Relaxations for Neural Network Verification” ([arXiv:2506.10269](https://arxiv.org/abs/2506.10269)), shows what happens when the relaxation is *not* strictly feasible: the central path has no interior, strong duality can fail, and a PD-IPM that monitors the gap $$X\cdot S$$ may never declare optimality. The authors use high-precision IPMs (SDPA-GMP) to diagnose the pathology and propose regularised / face-reduced SDPs.

This is Chapter 17's SDP section meeting a modern ML task. The central-path equation $$XS = \tau I$$ assumes $$X,S\succ 0$$. If the spectrahedron has empty relative interior, the hypothesis is false and the algorithm you implemented in 17-02 is not merely slow — it is *ill-posed*. The lesson is the one Boyd–Vandenberghe already taught: check Slater, then trust the gap.

## What to run in this course

For a one-hour lab, take a small long-only portfolio or a hard-margin SVM, solve it with `cp.CLARABEL`, and print the primal residual, dual residual, and gap. Then change the cone (box vs second-order) and watch the Newton iteration count. That is a primal-dual interior-point method applied to a data-science model, with no new theory beyond this chapter.

## Sources

- P. J. Goulart, Y. Chen, “Clarabel: An interior-point solver for conic programs with quadratic objectives,” 2024. [arXiv:2405.12762](https://arxiv.org/abs/2405.12762)
- Y. Chen, D. Tse, P. Nobel, P. Goulart, S. Boyd, “CuClarabel: GPU Acceleration for a Conic Optimization Solver,” 2024. [arXiv:2412.19027](https://arxiv.org/abs/2412.19027)
- CVXPY 1.5: Clarabel as default IPM backend.
- “Interior-Point Vanishing Problem in Semidefinite Relaxations for Neural Network Verification,” 2025. [arXiv:2506.10269](https://arxiv.org/abs/2506.10269)
