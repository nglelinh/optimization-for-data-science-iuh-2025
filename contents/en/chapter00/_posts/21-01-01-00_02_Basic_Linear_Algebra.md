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
