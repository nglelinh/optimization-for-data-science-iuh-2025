---
layout: post
title: 04-09 Applications and recent developments
chapter: '04'
order: 12
owner: Nguyen Le Linh
categories:
- chapter04
lang: en
lesson_type: optional
---

Chapter 04 is the contract of a convex program: variables, objective, constraints, optimality, and the legal rewrites (partial minimization, change of variables, eliminating equalities, slacks, relaxations). The same contract is now a *layer* inside a neural net and a *loss* for a predictor that will be consumed by a solver. This lesson looks at three 2019–2023 developments that only make sense after you can write “$$0\in\partial f(x^\star)+N_{\mathcal{C}}(x^\star)$$” without flinching.

## Differentiable convex layers and implicit optimality

Agrawal, Amos, Barratt, Boyd, Diamond, and Kolter (*Differentiable Convex Optimization Layers*, [NeurIPS 2019](https://web.stanford.edu/~boyd/papers/diff_cvxpy.html); library [cvxpylayers](https://cvxpylayers.org/)) embed a disciplined convex program in a PyTorch or TensorFlow graph. The forward pass *solves* the program; the backward pass differentiates the solution map by implicit differentiation through the residual of the solver (an affine-solver-affine factorization they call DPP). The 2019 date is slightly before the requested window; the library is the 2022–2026 default when a paper says “we put a QP in the net.”

The optimality language is exactly this chapter’s. If $$x^\star(\theta)$$ solves a parametrized convex problem, the KKT residual $$F(x,\lambda;\theta)=0$$ is an implicit equation. You do not need to unroll projected gradient; you linearize $$F$$, as Blondel et al. later automated in JAXopt ([NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html)). Chapter 04’s first-order condition is the *specification* of $$F$$.

## Theseus: nonlinear least squares as a differentiable layer

Not every inner problem is convex. Robotics and 3D vision repeatedly solve nonlinear least squares

$$
\min_x \tfrac12 \sum_i \bigl\| r_i(x;\theta)\bigr\|_2^2
$$

with Gauss–Newton or Levenberg–Marquardt. Pineda, Fan, Monge, Venkataraman, Sodhi, Chen, Ortiz, DeTone, Wang, Anderson, Dong, Amos, and Mukadam (*Theseus: A Library for Differentiable Nonlinear Optimization*, [NeurIPS 2022](https://arxiv.org/abs/2207.09442); [facebookresearch/theseus](https://github.com/facebookresearch/theseus)) ship a PyTorch library that treats that inner solve as a layer: sparse solvers, Lie groups, batching, GPU, and gradients by implicit differentiation or by differentiating the unrolled steps.

Why it belongs in *this* chapter rather than only in a robotics elective: the authors still start from an optimality residual (a stationarity condition for the least-squares objective) and then choose a *legal rewrite* — implicit differentiation versus unrolling — exactly the “transformations and change of variables” habit of 04-05. When the inner problem *is* convex, prefer cvxpylayers; when it is a structured nonlinear LS, Theseus is the 2022 reference implementation.

## Amortized optimization and convex surrogates for decisions

Two complementary ideas recycle Chapter 04’s vocabulary.

Amos (*Tutorial on Amortized Optimization*, [*Foundations and Trends in Machine Learning* 16:592–732, 2023](https://doi.org/10.1561/2200000102); [arXiv:2202.00665](https://arxiv.org/abs/2202.00665)) surveys *learning to optimize*: a network predicts $$x\approx x^\star(\theta)$$ for a family of problems that share structure (variational inference, sparse coding, meta-learning, optimal transport, deep equilibrium nets). Amortization does not replace optimality conditions; it *approximates the solution map*. You still need the inner problem to be well-posed, and you still debug by looking at residuals.

Elmachtoub and Grigas ([*Management Science* 2022](https://doi.org/10.1287/mnsc.2020.3922)) start from a true decision loss that is discontinuous in the predicted cost, then *relax* it to a convex surrogate SPO+ derived from duality — a textbook use of 04-08 (relaxation) plus the optimality conditions of a linear program. The feasible set stays the original polyhedron; only the training objective is replaced by something convex in the predictor’s parameters.

## A pattern to reuse on homework

Write the inner problem in standard form, name the rewrite, and name the outer gradient:

$$
\begin{align}
\text{inner:}&\quad x^\star(\theta)\in\arg\min_{x\in\mathcal{C}(\theta)} f(x;\theta),\\
\text{rewrite:}&\quad F(x^\star,\nu^\star;\theta)=0 \quad\text{(KKT / stationarity)},\\
\text{outer:}&\quad \nabla_\theta \ell\bigl(x^\star(\theta)\bigr) \quad\text{via } \nabla_x F,\;\nabla_\theta F.
\end{align}
$$

If you cannot write $$F$$, you are not ready to differentiate through the solver. If you can write $$F$$ but $$\mathcal{C}$$ is nonconvex, you are in Theseus / nonlinear LS territory, and global optimality is gone — which is precisely why Chapter 04 spent so many pages on convex solution sets.

## Sources

1. A. Agrawal, B. Amos, S. Barratt, S. Boyd, S. Diamond, and J. Z. Kolter, “Differentiable Convex Optimization Layers,” NeurIPS 2019. [page](https://web.stanford.edu/~boyd/papers/diff_cvxpy.html) · [cvxpylayers](https://cvxpylayers.org/)
2. M. Blondel et al., “Efficient and Modular Implicit Differentiation,” NeurIPS 2022. [abstract](https://proceedings.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html)
3. L. Pineda et al., “Theseus: A Library for Differentiable Nonlinear Optimization,” NeurIPS 2022. [arXiv:2207.09442](https://arxiv.org/abs/2207.09442) · [code](https://github.com/facebookresearch/theseus)
4. B. Amos, “Tutorial on Amortized Optimization,” *Found. Trends Mach. Learn.* 16:592–732, 2023. [DOI](https://doi.org/10.1561/2200000102) · [arXiv:2202.00665](https://arxiv.org/abs/2202.00665)
5. A. N. Elmachtoub and P. Grigas, “Smart ‘Predict, then Optimize’,” *Management Science* 2022. [DOI](https://doi.org/10.1287/mnsc.2020.3922)
