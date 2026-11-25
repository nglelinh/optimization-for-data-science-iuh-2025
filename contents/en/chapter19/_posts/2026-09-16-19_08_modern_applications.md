---
layout: post
title: 19-08 Modern applications of proximal Newton methods (2022–2026)
chapter: '19'
order: 12
owner: Nguyen Le Linh
categories:
- chapter19
lang: en
lesson_type: optional
---

Between 2022 and 2026, proximal Newton methods quietly crossed a major scalability frontier. In high-dimensional genomics, where precision matrices have $$p \approx 20{,}000$$ genes (over 200 million matrix entries), classical Graphical Lasso and even QUIC hit a memory and speed wall. New solvers like **MARS** (adaptive KKT sieving + semismooth Newton augmented Lagrangian) and `scikit-learn`'s `newton-cholesky` GLM path show that the core insight of Chapter 19—couple second-order curvature with exact nonsmooth structure, and shrink the working set via KKT certificates—scales to modern data science.

## Key ideas: Modern Second-Order Composite Solvers (2022–2026)

- **Adaptive KKT Sieving (MARS, JMLR 2023):** Before forming a huge Hessian, check the KKT optimality condition $$|\nabla_j g(x)| < \lambda$$ to certify coordinates that must be zero, solving the semismooth Newton system only on the tiny surviving active set.
- **Semismooth Newton Augmented Lagrangian (SSNAL):** Applies generalized Newton steps to the continuously differentiable (but piecewise-smooth) augmented Lagrangian dual, achieving superlinear convergence on massive $$\ell_1$$-penalized D-trace and Lasso paths.
- **Production GLM Solvers (`newton-cholesky` in `scikit-learn`):** When $$h(\beta) = \frac{\alpha}{2}\|\beta\|_2^2$$ is quadratic ridge, proximal Newton reduces to a single Cholesky solve of $$(X^T W X + \alpha I) v = -\nabla f$$, outperforming L-BFGS whenever $$n \gg p$$.
- **Support Identification & Local Quadratic Polishing:** Across all modern applications, the winning pattern is identical: identify the sparse support cheaply, then let second-order curvature polish the free variables to $$10^{-10}$$ accuracy in 3–5 steps.

### Worked example: KKT Active-Set Sieving on a 3-Feature Lasso

Consider $$\min_{x \in \mathbb{R}^3} \frac{1}{2}\|Ax - b\|_2^2 + \lambda\|x\|_1$$ with $$\lambda = 2$$, where at the current iterate $$x^k = (1, 0, 0)^T$$ the smooth gradient is $$\nabla g(x^k) = (-2.0, \; 0.3, \; -0.5)^T$$ and the Hessian is $$H = A^T A = \begin{bmatrix} 4 & 1 & 0 \\ 1 & 5 & 2 \\ 0 & 2 & 6 \end{bmatrix}$$.

1. **Test the KKT zero-optimality condition $$|\nabla_j g(x^k)| < \lambda$$ on zero coordinates:**
   - Coordinate 1 is nonzero ($$x_1^k = 1$$) $$\implies$$ stays in the **active set** $$\mathcal{A}$$.
   - Coordinate 2 has $$x_2^k = 0$$ and $$|\nabla_2 g(x^k)| = 0.3 < 2 = \lambda$$ $$\implies$$ **sieved out** (fixed at $$v_2 = 0$$).
   - Coordinate 3 has $$x_3^k = 0$$ and $$|\nabla_3 g(x^k)| = 0.5 < 2 = \lambda$$ $$\implies$$ **sieved out** (fixed at $$v_3 = 0$$).
2. **Solve the reduced Newton system on $$\mathcal{A} = \{1\}$$ only:**
   Instead of factoring the $$3 \times 3$$ matrix $$H$$ (or a $$20{,}000 \times 20{,}000$$ matrix in genomics!), we only solve the $$1 \times 1$$ subproblem:
   $$\min_{v_1} \; -2.0 v_1 + \frac{1}{2}(4)v_1^2 + 2|1 + v_1| \implies -2 + 4v_1 + 2 = 0 \implies v_1 = 0.$$
3. **Global KKT certification:**
   At $$x^k = (1, 0, 0)^T$$, $$\nabla_1 g + 2\operatorname{sign}(1) = -2 + 2 = 0$$ and $$|\nabla_2 g|, |\nabla_3 g| < 2$$—so KKT sieving just certified global optimality using a $$1 \times 1$$ solve instead of a $$3 \times 3$$ solve!

Proximal Newton applies a quadratic model to the *smooth* piece $$g$$ and leaves the *nonsmooth* piece $$h$$ inside the subproblem

$$
v^{+} = \arg\min_v\ \nabla g(x)^\top v + \tfrac12 v^\top H v + h(x+v),\qquad H\approx\nabla^2 g(x).
$$

When $$h=\lambda\|\cdot\|_1$$ that inner problem is a Lasso; when $$h$$ is an indicator it is a constrained quadratic. The 2014 theory (Lee, Sun, Saunders) and the classical implementations (glmnet, QUIC) are still the right mental model. What changed in 2022–2026 is scale: second-order composite solvers now finish precision-matrix paths that first-order glasso cannot, and production GLM libraries grew an explicit Newton–Cholesky path that is proximal Newton with $$h=\frac{\alpha}{2}\|\cdot\|_2^2$$.

## Graphical models: from QUIC to MARS

QUIC (Hsieh, Sustik, Dhillon, Ravikumar, JMLR 2014) is the example already in 19-05: a Newton quadratic on $$-\log\det\Theta+\langle S,\Theta\rangle$$ with an $$\ell_1$$ penalty, inner coordinate descent, and superlinear convergence. It remains a standard reference. **MARS** (Li, Jiang, Sun, JMLR 2023) is the 2020s sequel that students should cite for *high-dimensional* precision matrices. The estimator is an $$\ell_1$$-penalised D-trace loss rather than glasso; the algorithm is adaptive sieving (drop coordinates certified zero by KKT) plus a **semismooth Newton augmented Lagrangian** (SSNAL) solve on each reduced dual. The authors report paths on problems with $$p\approx 2\times 10^4$$ (breast-cancer gene-expression, hundreds of millions of dual variables before sieving) where glasso and QUIC stall.

Two Chapter 19 morals travel intact. First, the expensive object is still a *scaled proximal map* (here a dual Newton system), not a full dense Hessian of all $$p^2$$ entries. Second, active-set / sieving is how proximal Newton stays cheaper than proximal gradient: once the support is identified, quadratic convergence on the free set looks like the local analysis of 19-04. Genomics and Gaussian Markov random fields are the application, not a metaphor — the package is [QianLI-QL/MARS](https://github.com/QianLI-QL/MARS).

## GLMs in scikit-learn: Newton when $$h$$ is quadratic, L-BFGS when it is not

`PoissonRegressor(..., solver="newton-cholesky")` (scikit-learn 1.2, 2022) and the later logistic extension form $$H=\nabla^2 g+\alpha I$$ and Cholesky-solve the Newton step. The $$\alpha\|w\|_2^2$$ term is Tikhonov / ridge: the composite view is $$g=$$ negative log-likelihood, $$h=\frac{\alpha}{2}\|w\|_2^2$$, and the proximal map of a strongly convex quadratic is itself a linear solve — so proximal Newton *collapses* to damped Newton. That is the “when would we use proximal Newton?” table of 19-03 in library form: if $$h$$ is cheap (ridge, box, $$\ell_1$$ with coordinate descent), a Hessian of $$g$$ is worth forming whenever $$d$$ is small.

Keep L-BFGS (`solver="lbfgs"`) for the wide, bound-constrained case (Chapter 18) and SAGA for the huge, sparse, $$\ell_1$$ case (Chapter 26). Proximal Newton is the *middle* of that menu: moderate $$d$$, expensive $$g$$, structured $$h$$.

## glmnet and LIBLINEAR, still the sparse-GLM workhorses

Friedman, Hastie, Tibshirani's **glmnet** (the 19-05 citation) remains the path algorithm in R and in Python wrappers through 2026: cyclic coordinate descent on the inner quadratic, which *is* a proximal-Newton / IRLS outer loop. LIBLINEAR's trust-region Newton for $$\ell_2$$-regularised logistic / SVM, and NewGLMNET for $$\ell_1$$, are the same idea with a different inner solver. They are not new papers, but they are the codes that still train sparse logistic models on click-through and medical tabular data while deep-learning papers discuss Sophia. A course that teaches proximal Newton and then never names `glmnet::glmnet` has skipped the application.

The 2022–2026 increment is integration: scikit-learn's GLM rewrite, biglasso-style out-of-core paths, and SSNAL-based composite solvers (the Sun–Toh line) made the *same* outer iteration reliable at sizes glmnet's dense-enough-to-fit-in-RAM assumption does not cover.

## How to tell a proximal-Newton paper from a first-order one

Look at the inner problem. If each iteration solves a *quadratic plus $$h$$* (Lasso, box QP, dual Newton on a cone) to moderate accuracy and then takes a line search on the composite objective, it is Chapter 19. If each iteration is a gradient step plus a closed-form shrink, it is Chapter 09. MARS, QUIC, glmnet, and Newton–Cholesky sit on the first side; ISTA, FISTA, and SAGA sit on the second. Hybrid papers (inexact inner solves, quasi-Newton $$H_k$$) are 19-06, and they are how you scale when $$\nabla^2 g$$ itself is only available as a Hessian–vector product.

## Sources

- Q. Li, B. Jiang, D. Sun, “MARS: A Second-Order Reduction Algorithm for High-Dimensional Sparse Precision Matrices Estimation,” JMLR 24, 2023. [paper](https://jmlr.org/papers/v24/21-0699.html)
- C.-J. Hsieh, M. A. Sustik, I. S. Dhillon, P. Ravikumar, “QUIC: Quadratic Approximation for Sparse Inverse Covariance Estimation,” JMLR 15, 2014.
- J. Lee, Y. Sun, M. A. Saunders, “Proximal Newton-type methods for minimizing composite functions,” SIAM J. Optim. 24(3), 2014.
- J. Friedman, T. Hastie, R. Tibshirani, “Regularization paths for generalized linear models via coordinate descent,” J. Stat. Softw. 33(1), 2010 (glmnet; still the production path).
- scikit-learn 1.2+ `newton-cholesky` GLM solver.
