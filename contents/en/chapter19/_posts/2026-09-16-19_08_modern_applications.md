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
