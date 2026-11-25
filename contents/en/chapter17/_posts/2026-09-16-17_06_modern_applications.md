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

A decade ago, primal-dual interior-point methods were often taught as an elegant but somewhat heavy 1990s technology—too expensive for machine learning and too brittle for raw industrial pipelines. Between 2022 and 2026, that narrative flipped completely. Homogeneous conic solvers like Clarabel became the default backend inside CVXPY, GPU sparse direct factorizations brought PD-IPMs onto NVIDIA hardware (CuClarabel), and SDP relaxations for neural-network robustness pushed interior-point theory to its sharpest geometric edge: what happens when Slater's condition fails and the interior itself vanishes.

## Background Knowledge Map: Modern Conic PD-IPMs in Practice

- **Homogeneous Self-Dual Embedding:** Classical PD-IPMs diverge unpredictably on infeasible or unbounded problems. Modern solvers (Clarabel, MOSEK) embed the problem in a homogeneous self-dual cone with scaling variables $$(\tau, \kappa)$$, guaranteeing a well-defined central path that returns either an optimal solution or an Farkas infeasibility certificate.
- **Symmetric & Nonsymmetric Cones:** Beyond LP/QP/SOCP/SDP, modern libraries handle exponential cones (logistic regression, entropy) and power cones inside the same unified KKT Newton factorization.
- **GPU Sparse Direct KKT Factorizations:** Because PD-IPM's runtime is dominated by sparse $$LDL^T$$ factorization of the KKT matrix, GPU solvers like CuClarabel (using cuDSS) accelerate medium-to-large conic QPs by an order of magnitude while retaining $$10^{-8}$$ duality-gap certificates.
- **Facial Reduction & Interior-Point Vanishing:** In SDP relaxations of ReLU neural networks, algebraic couplings often force every feasible matrix $$X \succeq 0$$ onto a low-rank boundary face (no $$X \succ 0$$ exists), causing standard IPMs to stall unless facial reduction or regularization restores strict feasibility.

### Step-by-Step Worked Example (Read Slowly): Diagnosing an Interior-Point Vanishing SDP

Consider a tiny $$2 \times 2$$ SDP mimicking a degenerate ReLU-network verification constraint:
$$\min_{X \succeq 0} \; X_{22} \quad \text{subject to} \quad X_{11} = 0, \quad X_{11} + 2X_{12} + X_{22} = 1.$$

1. **Test Slater's strict feasibility condition:**
   Any feasible $$X = \begin{bmatrix} X_{11} & X_{12} \\ X_{12} & X_{22} \end{bmatrix} \succeq 0$$ has $$X_{11} = 0$$. For $$X$$ to be positive semidefinite, its determinant must satisfy:
   $$X_{11} X_{22} - X_{12}^2 = -X_{12}^2 \ge 0 \implies X_{12} = 0.$$
   Therefore, **no strictly positive definite matrix $$X \succ 0$$ is feasible**—the relative interior of the feasible set is empty!
2. **See what happens to a naive PD-IPM central path:**
   A primal-dual solver attempts to maintain $$X \succ 0$$ and $$S \succ 0$$ with $$XS = \mu I$$. As $$X_{11} \to 0^+$$ to satisfy the first constraint, $$S_{11} = \mu / X_{11} \to +\infty$$, blowing up the dual multiplier and destabilizing the KKT factorization before the duality gap can certify optimality.
3. **Apply facial reduction to restore strict feasibility:**
   Since $$X_{11} = 0$$ and $$X \succeq 0$$ force the first row and column of $$X$$ to vanish, every feasible matrix lies on the $$1 \times 1$$ face $$X = \begin{bmatrix} 0 & 0 \\ 0 & z \end{bmatrix}$$ with $$z \ge 0$$. Substituting into the second constraint yields $$z = 1 > 0$$, a strictly feasible $$1 \times 1$$ SDP with immediate certificate $$f^\star = 1$$!

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
