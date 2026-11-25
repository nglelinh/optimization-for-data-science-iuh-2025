---
layout: post
title: 04-09 Applications and recent developments
chapter: '04'
order: 10
owner: Nguyen Le Linh
categories:
- chapter04
lang: en
lesson_type: optional
---

For decades, convex optimization lived at the *end* of a machine-learning pipeline: first you trained a neural network to predict prices or demands, and only afterward did you hand those predictions to a solver to make a decision. Over the last few years, that wall collapsed—by differentiating directly *through* the first-order optimality conditions of Chapter 04, an entire convex solver now sits inside PyTorch or JAX as a trainable layer.

## Background Knowledge Map: From Optimality Conditions to Differentiable Layers

1. **Implicit Function Theorem on KKT/Variational Residuals**: At a solution $$x^\star(\theta)$$ of a parameterized convex program, the optimality condition can be written as a root-finding equation $$F(x^\star(\theta), \theta) = 0$$. Differentiating implicitly yields $$\frac{\partial x^\star}{\partial \theta} = -\bigl(D_x F\bigr)^{-1} D_\theta F$$, letting backpropagation flow through `argmin` without unrolling hundreds of solver iterations.
2. **Canonicalization and `cvxpylayers`**: Just as Chapter 04 transforms arbitrary convex programs into standard forms, `cvxpylayers` compiles a Disciplined Parametrized Program (DPP) into a cone program, solves it forward, and differentiates the homogeneous self-dual embedding residual in the backward pass.
3. **Nonlinear Least Squares in Robotics (`Theseus`)**: Vision, SLAM, and motion planning rely on Gauss–Newton and Levenberg–Marquardt updates. Embedding these structured solvers as differentiable layers lets perception networks learn features directly optimized for downstream geometric pose accuracy.
4. **Decision-Focused Learning (Predict-Then-Optimize)**: Minimizing prediction MSE does not necessarily minimize downstream decision cost when predictions enter a constrained LP or QP. Differentiating through convex surrogates (such as SPO+ or quadratic-regularized LPs) aligns the predictor's gradients with actual operational regret.

### Step-by-Step Worked Example (Read Slowly): Differentiating Through an Argmin Layer by Hand

Consider a 1D parameterized convex optimization layer:
$$x^\star(\theta) = \arg\min_{x \ge 0} \; \frac{1}{2}(x - \theta)^2 + \frac{1}{2}x^2,$$
where $$\theta \in \mathbb{R}$$ is the output of an upstream neural network layer.

1. **Write the first-order optimality condition**: The objective is $$f(x; \theta) = x^2 - \theta x + \frac{1}{2}\theta^2$$ with derivative $$\nabla_x f(x; \theta) = 2x - \theta$$. On $$C = [0, \infty)$$, optimality requires $$x^\star \ge 0$$, $$2x^\star - \theta \ge 0$$, and $$x^\star(2x^\star - \theta) = 0$$.
2. **Solve for $$x^\star(\theta)$$ in closed form**:
   - If $$\theta > 0$$, the constraint $$x \ge 0$$ is inactive, so $$2x^\star - \theta = 0 \implies x^\star(\theta) = \frac{\theta}{2}$$.
   - If $$\theta \le 0$$, the constraint binds and $$x^\star(\theta) = 0$$.
   Thus $$x^\star(\theta) = \max\!\left(0, \frac{\theta}{2}\right)$$—a scaled ReLU emerging naturally from constrained convex optimization!
3. **Compute the implicit derivative $$\frac{dx^\star}{d\theta}$$**:
   - On the active interior ($$\theta > 0$$), the residual is $$F(x, \theta) = 2x - \theta = 0$$. Implicit differentiation gives
     $$\frac{\partial F}{\partial x} \frac{dx^\star}{d\theta} + \frac{\partial F}{\partial \theta} = 0 \implies 2\frac{dx^\star}{d\theta} - 1 = 0 \implies \frac{dx^\star}{d\theta} = \frac{1}{2}.$$
   - On the boundary region ($$\theta < 0$$), the solution is pinned at $$x^\star(\theta) = 0$$, so $$\frac{dx^\star}{d\theta} = 0$$.
4. **Backpropagate a downstream loss**: Suppose the downstream task loss is $$L(x^\star) = (x^\star - 3)^2$$ and the current prediction is $$\theta = 4$$. Forward pass: $$x^\star(4) = 2$$, loss $$L = (2 - 3)^2 = 1$$. Backward pass: $$\frac{dL}{d\theta} = \frac{dL}{dx^\star}\frac{dx^\star}{d\theta} = 2(2 - 3)\cdot \frac{1}{2} = -1$$, telling the upstream network to increase $$\theta$$.

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
