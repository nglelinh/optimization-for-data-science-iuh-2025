---
layout: post
title: 15-09 Modern applications of the barrier method (2022–2026)
chapter: '15'
order: 15
owner: Nguyen Le Linh
categories:
- chapter15
lang: en
lesson_type: optional
---

The log barrier

$$
\phi(x) = -\sum_{i=1}^{m}\log\bigl(-h_i(x)\bigr)
$$

turns an inequality-constrained problem into a *smooth* family of unconstrained (or equality-constrained) Newton problems indexed by a tightness parameter $$t$$. That is still how industrial convex solvers think, even when the user never types `log`. This lesson follows the barrier from the central path you derived in this chapter into four places students actually meet in 2022–2026: the default CVXPY engine, GPU-era cone solvers, safe reinforcement learning, and differentiable control layers.

## Clarabel: a barrier-style IPM as CVXPY's default engine

Goulart and Chen (2024) describe **Clarabel**, an open-source interior-point solver for convex conic programs with quadratic objectives. The algorithm is a homogeneous embedding specialised to an interior-point iteration: a log-style barrier (or a self-concordant analogue on each atomic cone) keeps iterates in the interior of the nonnegative orthant, the second-order cone, the exponential and power cones, and the PSD cone, while a Newton system on the KKT residual drives primal feasibility, dual feasibility, and complementarity. Chordal decomposition is available for large SDPs.

The software fact that changes homework is this: as of CVXPY 1.5, Clarabel *replaces ECOS as the default* for the problem classes where ECOS used to be called automatically (CVXPY 1.5 release notes; Goulart & Chen, §implementation). Quadratic programs still often go to OSQP (an ADMM solver, Chapter 21), but LPs, SOCPs, and many exponential-cone models now silently run a barrier / interior-point method. The modelling habit from [05-07]({% multilang_post_url contents/chapter05/2026-09-15-05_07_Modeling_with_DCP_CVXPY %}) therefore has a Chapter 15 engine under the hood:

```python
import cvxpy as cp
x = cp.Variable(n)
prob = cp.Problem(cp.Minimize(cp.sum_squares(A @ x - b)), [x >= 0, cp.norm(x, 2) <= 1])
prob.solve(solver=cp.CLARABEL)
```

Ask `prob.solver_stats` after a default solve: if you did not name OSQP, you are watching a central-path method. That is the cleanest modern answer to “where is the barrier method used in data science?” — *inside the modelling layer you already teach*.

## Portfolio, MPC, and other cone QPs

The same solver stack is the production path for mean–variance and risk-constrained portfolios, model-predictive control (MPC) QPs, and small robust-optimisation cones. Clarabel's own numerical section and the later GPU port (Chapter 17) use portfolio and control QPs as running examples precisely because they are *self-concordant enough* for Newton and *structured enough* for a sparse KKT factorisation. A data-science student who writes a long-only portfolio with a tracking-error SOCP is not “doing finance instead of ML”; they are generating the central path of Chapter 15 on a problem whose Hessian is a covariance plus a barrier term on the simplex (or on a second-order cone).

The modelling moral is the same as Boyd & Vandenberghe, Chapter 11: *do not hand-code a projected gradient on a cone if a barrier IPM is one `solve()` away.* First-order splitting (OSQP, SCS) wins when you need warm starts at 100 Hz; the barrier wins when you need a high-accuracy certificate and the dimension still fits a sparse Newton system.

## Log barriers in constrained and safe RL

Liu, Ding, and Liu (*IPO: Interior-Point Policy Optimization under Constraints*, AAAI 2020) put a logarithmic barrier on the cost constraint of a constrained MDP and then run a PPO-style first-order method on the resulting smooth objective. The barrier is not solved by Newton in that paper — the policy is a neural net — but the *reduction* is exactly Chapter 15: inequalities become a penalty whose gradient blows up at the boundary, so iterates stay strictly feasible if they start feasible. OmniSafe (Ji, Zhou, Zhang, Dai, Pan, Sun, Huang, Geng, Liu, Yang; JMLR 2024) and Safety Gymnasium (Ji et al., NeurIPS 2023 Datasets) ship IPO next to PPO-Lagrangian, which is why a 2024–2026 student meets log barriers in a *policy-optimisation* README rather than only in a convex-analysis chapter.

The comparison is pedagogically sharp. IPO is a barrier method with a *stochastic, first-order* inner solver; Clarabel is a barrier method with a *deterministic, Newton* inner solver. Same outer idea, opposite computational regime. When the constraint is a convex cone on a few hundred variables, Newton on the barrier is optimal; when the “variable” is a deep policy, you keep the barrier and throw away the Hessian.

## Differentiable layers that still call a barrier solver

Agrawal, Amos, Barratt, Boyd, Diamond, and Kolter (NeurIPS 2019) introduced **cvxpylayers**: a CVXPY problem becomes a PyTorch / JAX layer whose backward pass differentiates the solution map. The forward solve is still an IPM or a first-order cone solver; the backward pass applies implicit differentiation to the KKT system — the same Jacobian that Newton's method factors in this chapter. Through 2022–2026 the pattern is standard in differentiable MPC, structured prediction, and “optimization-as-a-layer” architectures: you do *not* unroll gradient descent through 50 projected steps if a barrier solver returns a solution and a factorisation you can reuse for the adjoint.

That is the deepest Chapter 15 transfer: the Newton system of the central path is not only an algorithm for $$x^\star(t)$$, it is the linear map that lets learning systems treat `solve()` as a differentiable primitive.

## Sources

- P. J. Goulart, Y. Chen, “Clarabel: An interior-point solver for conic programs with quadratic objectives,” 2024. [arXiv:2405.12762](https://arxiv.org/abs/2405.12762)
- CVXPY 1.5 release notes: Clarabel replaces ECOS as the default for former ECOS problem classes.
- Y. Liu, J. Ding, X. Liu, “IPO: Interior-Point Policy Optimization under Constraints,” AAAI 2020.
- J. Ji et al., “OmniSafe: An Infrastructure for Accelerating Safe Reinforcement Learning Research,” JMLR 25(285), 2024; “Safety Gymnasium,” NeurIPS 2023 Datasets.
- A. Agrawal, B. Amos, S. Barratt, S. Boyd, S. Diamond, J. Z. Kolter, “Differentiable Convex Optimization Layers,” NeurIPS 2019 (cvxpylayers; still the 2022–2026 interface).
