---
layout: post
title: 00-02 Basic Linear Algebra
chapter: '00'
order: 7
owner: GitHub Copilot
lang: en
categories:
- chapter00
lesson_type: required
---

Open the hood of almost any convex optimization solver—whether it is fitting a ridge regression, solving a portfolio linear program, or taking a Newton step in an interior-point method—and you will find the same workhorse engine: solving linear systems $$Ax = b$$ and analyzing symmetric matrices. Fluency in linear algebra turns multi-page coordinate sums into clean, geometric matrix equations whose behavior you can read at a glance.

## Background Knowledge Map: Linear Algebra as Optimization Infrastructure

- **Vector Spaces, Norms & Inner Products:** Equip $$\mathbb{R}^n$$ with length, angles, and projections so we can measure residuals $$\|Ax - b\|_2$$ and enforce orthogonality conditions.
- **Matrices as Linear Maps & Constraints:** Encode affine feasible sets $$\{x : Ax = b\}$$, feature designs, and Jacobians; rank and nullspace reveal whether solutions are unique or have free degrees of freedom.
- **Eigenvalues & Positive Definiteness:** Diagonalize symmetric quadratic forms $$x^T Q x$$ into independent principal axes, certifying convexity ($$Q \succeq 0$$) and quantifying ill-conditioning ($$\kappa = \lambda_{\max}/\lambda_{\min}$$).
- **Normal Equations & Projections:** Bridge geometry and algebra by showing that least-squares optimality means the residual $$b - Ax^*$$ is orthogonal to the column space of $$A$$.

### Step-by-Step Worked Example (Read Slowly): Solving Least Squares via Normal Equations

Fit a line $$y \approx x_1 + x_2 t$$ to three data points $$(t, y) \in \{(0, 1), (1, 2), (2, 4)\}$$ by minimizing $$\|Ax - b\|_2^2$$ where

$$A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \end{pmatrix}, \qquad b = \begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}.$$

1. **Form the normal equations $$A^T A x = A^T b$$:**
   $$A^T A = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} 3 & 3 \\ 3 & 5 \end{pmatrix}, \qquad A^T b = \begin{pmatrix} 1 + 2 + 4 \\ 0 + 2 + 8 \end{pmatrix} = \begin{pmatrix} 7 \\ 10 \end{pmatrix}.$$
2. **Invert the $$2 \times 2$$ Gram matrix:** Since $$\det(A^T A) = 3(5) - 3^2 = 6 > 0$$, $$A^T A$$ is strictly positive definite and invertible:
   $$x^* = (A^T A)^{-1} A^T b = \frac{1}{6}\begin{pmatrix} 5 & -3 \\ -3 & 3 \end{pmatrix}\begin{pmatrix} 7 \\ 10 \end{pmatrix} = \frac{1}{6}\begin{pmatrix} 5 \\ 9 \end{pmatrix} = \begin{pmatrix} 5/6 \\ 3/2 \end{pmatrix}.$$
3. **Verify orthogonality of the residual:** $$r = b - Ax^* = (1 - 5/6,\; 2 - 14/6,\; 4 - 23/6)^T = (1/6,\; -1/3,\; 1/6)^T$$. Checking $$A^T r = (1/6 - 2/6 + 1/6,\; 0 - 1/3 + 2/6)^T = (0, 0)^T$$ confirms optimality.

Almost every optimization iterate is a vector, every linear constraint is a matrix–vector product, and every local curvature story is an eigenvalue of a Hessian or Gram matrix. This page orients the three linear-algebra lessons that follow.

## Objects you will reuse all semester

- **Vectors and inner products.** The Euclidean geometry $$\langle g, d\rangle = g^\top d$$ decides whether $$d$$ is a descent direction ($$g^\top d < 0$$). Other geometries (Mahalanobis, mirror maps) appear later as preconditioning and dual norms (Chapter 13).
- **Matrices as linear maps.** An equality $$Ax = b$$ cuts an affine subspace; the nullspace of $$A$$ is the set of feasible steps. Least squares (Chapter 05) solves $$A^\top A \hat{x} = A^\top y$$ when $$A$$ has full column rank.
- **Eigenvalues and quadratic forms.** If $$Q\succeq 0$$ then $$x\mapsto x^\top Q x$$ is convex; the condition number $$\kappa = \lambda_{\max}(Q)/\lambda_{\min}(Q)$$ of a strongly convex quadratic is exactly the number that slows vanilla gradient descent and motivates acceleration (Chapters 06, 09, 26).

A symmetric matrix $$Q$$ admits an orthonormal diagonalization $$Q = U\Lambda U^\top$$. The Rayleigh quotient

$$
\lambda_{\min}(Q) = \min_{\|x\|_2=1} x^\top Q x, \qquad \lambda_{\max}(Q) = \max_{\|x\|_2=1} x^\top Q x
$$

is the cleanest way to *see* strong convexity and smoothness constants.

## Lessons in this block

1. Vectors and vector spaces
2. Matrices and linear transformations
3. Eigenvalues and eigenvectors

Checkpoint: explain in one sentence why $$\nabla^2 f(x)\succeq 0$$ everywhere implies that a twice-differentiable $$f$$ is convex. (Chapter 03 will prove it; linear algebra is what makes the statement meaningful.)
