---
layout: post
title: "19-06 Proximal quasi-Newton methods"
chapter: '19'
order: 10
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

What happens when $$g(x)$$ has $$p = 50{,}000$$ variables, so computing and storing $$\nabla^2 g(x)$$ is out of the question, yet proximal gradient descent is still crawling? You marry Chapter 18 (Quasi-Newton) with Chapter 19 (Proximal Newton) to obtain **Proximal Quasi-Newton methods**: replace the exact Hessian $$\nabla^2 g(x)$$ inside the scaled proximal map by a BFGS, L-BFGS, or block-diagonal curvature matrix $$B_k$$!

## Key ideas: Replacing Exact Hessians in Composite Optimization

- **Proximal BFGS & L-BFGS (Lee, Sun, Saunders 2014):** Maintains a positive-definite secant matrix $$B_k$$ using only gradients of $$g$$, solving $$\min_v \nabla g(x^k)^T v + \frac{1}{2} v^T B_k v + h(x^k + v)$$. When $$B_k$$ satisfies the Dennis–Moré condition, it achieves **local superlinear convergence** without ever computing a second derivative!
- **Blockwise / Diagonal Hessian Approximations (Tseng & Yun 2009):** When $$h(x) = \sum_b h_b(x_b)$$ is block-separable, choosing $$B_k$$ to be block-diagonal decouples the scaled proximal subproblem into tiny independent blocks—combining fast per-iteration cost with linear convergence.
- **Handling Singular or Indefinite Hessians:** On high-dimensional problems with $$p > n$$, the true Hessian $$\nabla^2 g(x)$$ is rank-deficient (singular), causing exact proximal Newton subproblems to become unbounded unless regularized; BFGS automatically stays strictly positive definite ($$B_k \succ 0$$) whenever $$y_k^T s_k > 0$$.
- **Fast Subproblem Solves with L-BFGS Compact Form:** Because an L-BFGS matrix $$B_k = \gamma_k I - U_k M_k U_k^T$$ is a diagonal matrix plus a rank-$$2m$$ update, its scaled proximal subproblem can be solved efficiently in the dual space of dimension $$2m \ll p$$!

### Worked example: One Proximal-BFGS Step Without Second Derivatives

Minimize $$f(x) = g(x) + |x_1| + |x_2|$$ where we only observe gradients of $$g$$. Suppose from step 0 we recorded $$s_0 = (1, 0)^T$$ and $$y_0 = \nabla g(x^1) - \nabla g(x^0) = (4, 0)^T$$ starting from $$B_0 = I_2$$, and at $$x^1 = (1, 1)^T$$ the gradient is $$\nabla g(x^1) = (3, 2)^T$$.

1. **Update the Hessian approximation $$B_1$$ via BFGS (no second derivatives!):**
   With $$s_0^T B_0 s_0 = 1$$ and $$y_0^T s_0 = 4 > 0$$:
   $$B_1 = I_2 - \frac{s_0 s_0^T}{1} + \frac{y_0 y_0^T}{4} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} - \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} + \frac{1}{4}\begin{bmatrix} 16 & 0 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 4 & 0 \\ 0 & 1 \end{bmatrix}.$$
2. **Form the Proximal-BFGS subproblem at $$x^1 = (1, 1)^T$$:**
   $$v^{(1)} = \arg\min_{v_1, v_2} \; \left(3v_1 + 2v_1^2 + |1 + v_1|\right) + \left(2v_2 + \tfrac{1}{2}v_2^2 + |1 + v_2|\right).$$
3. **Solve using the scaled prox formula $$z = \operatorname{prox}_{B_1}(x^1 - B_1^{-1}\nabla g(x^1))$$:**
   - Unconstrained quasi-Newton target: $$x^1 - B_1^{-1}\nabla g(x^1) = \begin{bmatrix} 1 \\ 1 \end{bmatrix} - \begin{bmatrix} 3/4 \\ 2 \end{bmatrix} = \begin{bmatrix} 0.25 \\ -1.0 \end{bmatrix}$$.
   - Apply coordinate-wise soft-thresholding with thresholds $$1/B_{1,11} = 0.25$$ and $$1/B_{1,22} = 1.0$$:
     $$z_1 = S_{0.25}(0.25) = 0, \qquad z_2 = S_{1.0}(-1.0) = 0!$$
4. **Result:**
   The BFGS curvature estimate $$B_{1,11} = 4$$ prevented overshooting coordinate 1 and landed cleanly at $$x^2 = (0, 0)^T$$—identifying the exact sparse support $$\emptyset$$ in a single proximal quasi-Newton step!

As problems grow larger, computing the Hessian becomes very expensive. **Proximal quasi-Newton methods** avoid computing the Hessian $$H^{(k-1)} = \nabla^2 g(x^{(k-1)})$$ at each step, while still achieving a superlinear or linear convergence rate.

## Proximal quasi-Newton method
* Lee (2014) proposed updating the Hessian approximation in the BFGS style. This method works very well and has a local superlinear convergence rate.
* Tseng and Yun (2009) proposed approximating the Hessian blockwise. This works only when $$f = g + h$$ can be split into parts in which $$h$$ depends on only some of the optimization variables. Computing the Hessian blockwise is much faster. This method has a linear convergence rate.

Quasi-Newton methods are useful not only when the Hessian is hard to compute, but also in ill-conditioned problems where the Hessian is singular or nearly singular.

#### References
* J. Lee and Y. Sun and M. Saunders (2014), "Proximal Newton-type methods for minimizing composite functions"
* P. Tseng and S. Yun (2009), "A coordinate gradient descent method for nonsmooth separable minimization"
