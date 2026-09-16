---
layout: post
title: 05-08 Applications and recent developments
chapter: '05'
order: 13
owner: Nguyen Le Linh
categories:
- chapter05
lang: en
lesson_type: optional
---

Chapter 05 classified convex programs by the *shape* of the objective and the cones in the constraints: LP, QP, QCQP, SOCP, SDP, and geometric programs. That taxonomy is also the API of a modeling language. This lesson looks at three places where those canonical forms are the 2022–2026 production objects — a modern interior-point solver shipped with CVXPY, portfolio QPs you can backtest, and SDP relaxations that certify neural nets — plus a reminder that Lasso and sparse recovery are still QPs (or QPs in extended form) you should model, not hand-code.

You already have a DCP/CVXPY lab in [05-07]({% multilang_post_url contents/chapter05/2026-09-15-05_07_Modeling_with_DCP_CVXPY %}). Treat this lesson as the *why these cones* companion.

## Clarabel: a 2024 interior-point engine for the whole taxonomy

Goulart and Chen (*Clarabel: An interior-point solver for conic programs with quadratic objectives*, [arXiv:2405.12762](https://arxiv.org/abs/2405.12762), 2024; docs [clarabel.org](https://clarabel.org/); [citing page](https://oxfordcontrol.github.io/ClarabelDocs/stable/citing/)) built a homogeneous-embedding interior-point method for convex programs with conic constraints and a quadratic objective. The solver speaks the cones this chapter named — nonnegative, second-order, semidefinite (with chordal decomposition), and selected nonsymmetric cones — and is distributed as a standard solver in CVXPY. Their numerical profile is especially strong on QPs relative to several open-source and commercial codes.

The pedagogical point is ruthless: once your DCP model is canonicalized, you are no longer “doing Lasso in Python.” You are handing a cone program to an IPM. Switching `solver=cp.CLARABEL` versus `cp.OSQP` versus `cp.SCS` is an experiment on *canonical form + algorithm*, not a rewrite of the science. OSQP (Stellato, Banjac, O’Donoghue, Bemporad, and Boyd, *Math. Prog. Comp.* 2020) remains the first-choice first-order QP solver for many control and portfolio QPs; Clarabel is the 2024 interior-point counterpart you should know by name.

## Portfolio construction as a QP you can ship

Markowitz mean–variance allocation is the QP

$$
\begin{align}
\min_x \quad & x^\top \Sigma x - \gamma \hat{r}^\top x \\
\text{s.t.} \quad & \mathbf{1}^\top x = 1, \quad x\in\mathcal{X},
\end{align}
$$

with $$\mathcal{X}$$ a polytope of long-only, leverage, or turnover limits. Boyd, Busseti, Diamond, Kahn, Koh, Nystrup, and Speth (*Multi-Period Trading via Convex Optimization*, [*Found. Trends Optim.* 2017](https://stanford.edu/~boyd/papers/cvx_portfolio.html)) put single- and multi-period versions of this QP — plus transaction and holding costs — in one framework. The companion library [cvxportfolio](https://www.cvxportfolio.com/) (actively maintained through the mid-2020s, currently documented at v1.5) is how you *run* that paper on recent market data: `SinglePeriodOptimization` / `MultiPeriodOptimization` policies inside a `StockMarketSimulator`.

The 2017 monograph is older than 2022; the reason it belongs here is that the *canonical form* has not been replaced, only the solver stack (OSQP / Clarabel) and the software API have. If you need a 2022–2023 scientific counterpart, Wasserstein DRO portfolios (Gao and Kleywegt, [*Math. Oper. Res.* 2023](https://doi.org/10.1287/moor.2022.1275); see Chapter 02) are QPs or SOCPs once the dual is written down.

## SDP relaxations for neural-network verification

Asking whether a ReLU network is locally robust — “no perturbation of radius $$\varepsilon$$ changes the predicted class” — is a nonconvex feasibility problem. Replacing products of activations by a positive-semidefinite moment matrix produces an SDP *relaxation* (the same relaxation idea as 04-08, now in the SDP cone of 05-05). Lan, Zheng, and Lomuscio (*Tight Neural Network Verification via Semidefinite Relaxations and Linear Reformulations*, [AAAI 2022](https://doi.org/10.1609/aaai.v36i7.20689)) combine a layerwise SDP with reformulation-linearization (RLT) cuts and report large gains in certified robustness on MNIST networks (for example, from 0% to 82% certified on a ~10k-node net in their tables). An earlier layer-SDP plus triangle cuts appears in Batten, Kouvaros, Lomuscio, and Zheng ([IJCAI 2021](https://doi.org/10.24963/ijcai.2021/301)).

You will not solve ImageNet-scale SDPs in this course. You *will* recognize the pattern: a combinatorial or bilinear constraint is replaced by $$X\succeq 0$$ plus linear equalities, and a solver for Chapter 05’s SDP class either certifies the property or returns a bound.

## Sparse recovery is still a canonical QP

Lasso

$$
\min_x \tfrac12\|Ax-b\|_2^2 + \lambda \|x\|_1
$$

is the sparse-recovery workhorse in imaging and high-dimensional statistics. In CVXPY it is a few atoms (see 05-07). The *science* after 2021 is often *unrolling* that QP’s proximal-gradient iteration into a network (Monga, Li, and Eldar, “Algorithm Unrolling,” [*IEEE Signal Processing Magazine*, 2021](https://doi.org/10.1109/MSP.2020.3016905)) so that step-sizes and dictionaries become trainable. The inner object remains the same QP. If you can write Lasso as a QP with slacks, you can read an unrolled-ISTA paper without new theory.

## Sources

1. P. J. Goulart and Y. Chen, “Clarabel: An interior-point solver for conic programs with quadratic objectives,” arXiv:2405.12762, 2024. [arXiv](https://arxiv.org/abs/2405.12762) · [clarabel.org](https://clarabel.org/)
2. S. Boyd, E. Busseti, S. Diamond, et al., “Multi-Period Trading via Convex Optimization,” *Found. Trends Optim.*, 2017. [page](https://stanford.edu/~boyd/papers/cvx_portfolio.html) · [cvxportfolio](https://www.cvxportfolio.com/)
3. J. Lan, Y. Zheng, and A. Lomuscio, “Tight Neural Network Verification via Semidefinite Relaxations and Linear Reformulations,” AAAI 2022. [DOI](https://doi.org/10.1609/aaai.v36i7.20689)
4. B. Batten, P. Kouvaros, A. Lomuscio, and Y. Zheng, “Efficient Neural Network Verification via Layer-based Semidefinite Relaxations and Linear Cuts,” IJCAI 2021. [DOI](https://doi.org/10.24963/ijcai.2021/301)
5. V. Monga, Y. Li, and Y. C. Eldar, “Algorithm Unrolling: Interpretable, Efficient Deep Learning for Signal and Image Processing,” *IEEE SPM* 38(2):18–44, 2021. [DOI](https://doi.org/10.1109/MSP.2020.3016905)
