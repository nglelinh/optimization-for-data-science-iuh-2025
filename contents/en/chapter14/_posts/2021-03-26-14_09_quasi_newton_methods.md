---
layout: post
title: 14-09 Quasi-Newton methods
chapter: '14'
order: 17
owner: Minjoo Lee
categories:
- chapter14
lang: en
---

Computing and factoring a $$10{,}000 \times 10{,}000$$ Hessian at every iteration is out of the question—yet throwing away all curvature information and falling back to plain gradient descent feels wasteful. **Quasi-Newton methods** (like BFGS and L-BFGS) strike an ingenious compromise: they never compute a single second derivative, instead learning an approximate inverse Hessian $$B_k \approx (\nabla^2 f(x^{(k)}))^{-1}$$ on the fly from the gradient differences you *already* computed!

## Background Knowledge Map: Learning Curvature Without Hessians

- **Pillar 1 — The Secant Equation:** Define step $$s_k = x^{(k+1)} - x^{(k)}$$ and gradient change $$y_k = \nabla f(x^{(k+1)}) - \nabla f(x^{(k)})$$. Any sensible Hessian approximation $$H_{k+1}$$ must satisfy $$H_{k+1} s_k = y_k$$ along the most recent step.
- **Pillar 2 — Low-Rank Updates Avoid $$O(n^3)$$ Factorizations:** BFGS updates $$H_k^{-1}$$ directly via a symmetric rank-2 update in $$O(n^2)$$ flops (and L-BFGS in $$O(mn)$$ flops using only the last $$m$$ pairs $$(s_i, y_i)$$).
- **Pillar 3 — Curvature Condition Preserves Positive Definiteness:** Whenever $$s_k^T y_k > 0$$ (guaranteed by Wolfe line search on convex functions), BFGS preserves $$H_{k+1} \succ 0$$, guaranteeing every quasi-Newton step is a descent direction.
- **Pillar 4 — Superlinear Convergence Sweet Spot:** While slower than Newton's quadratic rate per iteration, superlinear convergence at $$O(n^2)$$ (or $$O(n)$$) per step makes L-BFGS the default workhorse for medium-to-large smooth optimization.

### Step-by-Step Worked Example (Read Slowly): One Secant / BFGS Curvature Update in 1D & 2D

Suppose we minimize a smooth function in 1D where we only observe gradients (no second derivatives): at $$x^{(0)} = 0$$, $$f'(0) = -4$$; we take an initial step to $$x^{(1)} = 1$$ and observe $$f'(1) = -1$$.

1. **Compute the secant pair $$(s_0, y_0)$$:**
   - Step: $$s_0 = x^{(1)} - x^{(0)} = 1 - 0 = 1$$.
   - Gradient difference: $$y_0 = f'(1) - f'(0) = -1 - (-4) = 3$$.
   - Check curvature condition: $$s_0 y_0 = 1 \times 3 = 3 > 0$$ (positive curvature!).
2. **Form the secant Hessian approximation $$H_1$$:**
   $$H_1 s_0 = y_0 \implies H_1 = \frac{y_0}{s_0} = \frac{3}{1} = 3 \qquad \left(H_1^{-1} = \frac{1}{3}\right).$$
3. **Take the quasi-Newton step from $$x^{(1)} = 1$$:**
   $$x^{(2)} = x^{(1)} - H_1^{-1} f'(1) = 1 - \frac{1}{3}(-1) = \frac{4}{3} \approx 1.333.$$
   Notice that if $$f(x) = \frac{3}{2}x^2 - 4x$$ (true minimizer $$x^\star = \frac{4}{3}$$), the secant approximation recovered the *exact* Hessian $$3$$ from just two gradient evaluations and landed straight on $$x^\star$$!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
    });
</script>

If the computation of the Hessian is too expensive or the Hessian is singular, we use quasi-Newton methods to approximate the Hessian matrix, i.e., $$\nabla^{2}f(x)$$ is replaced by $$H>0$$, and we use $$H$$ for the update:

>\begin{align}
>x^{+} = x - tH^{-1}\nabla f(x)
>\end{align}

Some features of quasi-Newton methods are as follows. For more details, see [Chapter 18]({% multilang_post_url contents/chapter18/21-03-23-18_00_Quasi_Newton_methods %}).

* The approximate Hessian $$H$$ is updated at each step. The goal is to use a relatively cheap computation for $$H^{-1}$$.
* The convergence rate is superlinear, but not as fast as Newton's method. Typically, $$n$$ steps of quasi-Newton are equivalent to one step of Newton in terms of progress.
* Many quasi-Newton methods update $$H$$ at each iteration using propagation techniques.
