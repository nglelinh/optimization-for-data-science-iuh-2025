---
layout: post
title: 19 Proximal Newton Method
chapter: '19'
order: 1
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

Classical Newton's method is the Ferrari of smooth optimization—quadratic convergence, effortless immunity to ill-conditioning—until a single sharp corner like $$\lambda \|x\|_1$$ or a box constraint $$x \in C$$ enters the objective. Suddenly $$\nabla^2 f(x)$$ does not even exist at the solution! **Proximal Newton methods** rescue second-order speed for composite nonsmooth problems $$\min_x g(x) + h(x)$$ by applying a full Hessian quadratic model *only* to the smooth loss $$g$$ while keeping the nonsmooth regularizer $$h$$ intact inside the subproblem. That simple split powers modern workhorses from `glmnet` to graphical Lasso (`QUIC`).

## Background Knowledge Map: Extending Second-Order Methods to Composite Objectives

- **Composite Splitting ($$f = g + h$$):** Separating a twice-differentiable data-fidelity term $$g$$ from a simple convex nonsmooth term $$h$$ (such as $$\ell_1$$ sparsity or a set indicator $$I_C$$) lets us exploit second-order curvature where it exists without smoothing away the exact corners where sparsity lives.
- **Scaled Proximal Operators ($$\operatorname{prox}_H$$):** Replacing the Euclidean metric $$\frac{1}{2t}\|x - z\|_2^2$$ of proximal gradient descent with the Hessian metric $$\frac{1}{2}\|x - z\|_H^2$$ generalizes the proximal map while preserving uniqueness and firm non-expansiveness in the $$H$$-norm.
- **Outer Superlinear/Quadratic Speed vs. Inner Subproblem Cost:** Proximal Newton slashes outer gradient/Hessian evaluations from $$O(1/\epsilon)$$ to $$O(\log\log(1/\epsilon))$$, at the price of solving a composite quadratic subproblem (typically via fast coordinate descent or active-set methods) at each outer step.
- **Quasi-Newton & Projected Variants:** When forming $$\nabla^2 g(x)$$ is too costly, BFGS-style approximations yield *proximal quasi-Newton* methods; when $$h = I_C$$ is a box indicator, Bertsekas's *projected Newton* method avoids the ascent trap of naive Euclidean projection.

### Step-by-Step Worked Example (Read Slowly): Proximal Gradient vs. Proximal Newton in 2D

Minimize the composite objective $$f(x) = g(x) + h(x)$$ with $$g(x) = \frac{1}{2}(x_1^2 + 10 x_2^2)$$ and $$h(x) = |x_1| + |x_2|$$ (exact optimum $$x^\star = (0, 0)^T$$), starting from $$x^0 = (5, 5)^T$$.

1. **One Proximal Gradient (ISTA) step:**
   Here $$\nabla g(x) = (x_1, 10 x_2)^T$$ has Lipschitz constant $$L = 10$$, so we must take step size $$t = \frac{1}{L} = 0.1$$:
   $$x^0 - t\nabla g(x^0) = \begin{bmatrix} 5 \\ 5 \end{bmatrix} - 0.1\begin{bmatrix} 5 \\ 50 \end{bmatrix} = \begin{bmatrix} 4.5 \\ 0 \end{bmatrix}.$$
   Applying soft-thresholding $$S_{0.1}(\cdot)$$ coordinate-wise yields $$x^1_{\text{PG}} = (4.4, 0)^T$$. Because the steep $$x_2$$ curvature forced $$t = 0.1$$, coordinate $$x_1$$ barely budged ($$5 \to 4.4$$)!
2. **One Proximal Newton step:**
   The exact Hessian is $$H = \nabla^2 g(x^0) = \operatorname{diag}(1, 10)$$. The proximal Newton subproblem minimizes:
   $$\min_{v_1, v_2} \; \left(5v_1 + \tfrac{1}{2}v_1^2 + |5 + v_1|\right) + \left(50v_2 + 5v_2^2 + |5 + v_2|\right).$$
   Substituting $$z = x^0 + v$$, this decouples into $$\min_{z_1} \frac{1}{2}z_1^2 + |z_1| \implies z_1 = 0$$ and $$\min_{z_2} 5z_2^2 + |z_2| \implies z_2 = 0$$!
   Thus $$v = (-5, -5)^T$$ and $$x^1_{\text{PN}} = (0, 0)^T = x^\star$$ in **one single step**—completely eliminating the $$10\times$$ ill-conditioning!

In this chapter, we will examine **Proximal Newton Method**, **Proximal quasi-Newton method**, and **Projected Newton method**.

### Reference Papers

Proximal Newton method:

* J. Friedman and T. Hastie and R. Tibshirani (2009), "Regularization paths for generalized linear models via coordinate descent"
* C.J. Hsiesh and M.A. Sustik and I. Dhillon and P. Ravikumar (2011), "Sparse inverse covariance matrix estimation using quadratic approximation"
* M. Patriksson (1998), "Cost approximation: a unified framework of descent algorithms for nonlinear programs"
* J. Lee and Y. Sun and M. Saunders (2014), "Proximal Newton-type methods for minimizing composite functions"
* P. Tseng and S. Yun (2009), "A coordinate gradient descent method for nonsmooth separable minimization"

Projected Newton method:

* A. Barbero and S. Sra (2011), "Fast Newton-type methods for total variation regularization"
* D. Bertsekas (1982), "Projected Newton methods for optimization problems with simple constraints"
* D. Kim and S. Sra. and I. Dhillon (2010), "Tackling box-constrained optimization via a new projected
quasi-Newton approach"
*  M. Schmidt and D. Kim and S. Sra (2011), "Projected Newton-type methods in machine learning"
