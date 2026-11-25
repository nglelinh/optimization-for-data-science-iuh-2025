---
layout: post
title: 22 Conditional Gradient (Frank-Wolfe) Method
chapter: '22'
order: 1
owner: YoungJae Choung
categories:
- chapter22
lang: en
---

Picture a 1956 operations research room long before GPUs or automatic differentiation: Marguerite Frank and Philip Wolfe are trying to minimize a smooth quadratic objective over a high-dimensional polytope where computing a Euclidean projection at every step is prohibitively expensive, yet solving a single linear program over that same polytope is routine. Their radical insight was to abandon projection altogether—instead of stepping outside the feasible set and pulling back, simply ask a linear oracle which extreme point points most sharply downhill, and slide a fraction of the way toward that corner. Nearly seventy years later, that exact projection-free idea powers sparse regression, low-rank matrix completion, and structured prediction at scales where Euclidean projection would collapse.

## Background Knowledge Map: Architecture of the Conditional Gradient Method

- **Linear Minimization Oracles (LMO) vs. Projection Oracles:** Projected gradient descent requires solving a quadratic subproblem at every iteration to snap back onto $$C$$. Frank–Wolfe replaces that quadratic projection with a linear minimization $$\arg\min_{s \in C} \langle \nabla f(x_k), s \rangle$$, which over $$\ell_1$$ balls, simplices, or nuclear-norm balls reduces to finding a single largest coordinate or leading singular vector.
- **Convex Combinations and Automatic Feasibility:** Because each iterate is updated as $$x_{k+1} = (1 - \gamma_k) x_k + \gamma_k s_k$$ with $$\gamma_k \in [0, 1]$$ and $$x_k, s_k \in C$$, convexity of $$C$$ guarantees $$x_{k+1} \in C$$ without ever leaving the constraint set.
- **Atomic Sparsity and Carathéodory Representation:** Every iteration adds at most one new extreme point (atom) $$s_k$$ to the active representation of $$x_k$$. Consequently, after $$k$$ steps, $$x_k$$ is guaranteed to be a convex combination of at most $$k+1$$ vertices—yielding naturally sparse vectors or low-rank matrices.
- **Duality Gap as a Free Stopping Certificate:** By convexity of $$f$$, the linearized gap $$g_k = \max_{s \in C} \langle \nabla f(x_k), x_k - s \rangle = \langle \nabla f(x_k), x_k - s_k \rangle$$ upper-bounds the true suboptimality $$f(x_k) - f(x^\star)$$, giving an exact, zero-cost convergence certificate at every iteration.

### Step-by-Step Worked Example (Read Slowly): One Projection-Free Step on the Probability Simplex

Consider minimizing $$f(x) = \frac{1}{2}\|x - c\|_2^2$$ with target $$c = (0.8, 0.5, 0.2)^\top$$ over the 3-dimensional probability simplex $$\Delta_3 = \{x \in \mathbb{R}^3 : x \ge 0,\ x_1 + x_2 + x_3 = 1\}$$, starting from the vertex $$x_0 = (0, 0, 1)^\top$$.

1. **Compute the gradient at $$x_0$$:**
   $$\nabla f(x_0) = x_0 - c = (0 - 0.8,\ 0 - 0.5,\ 1 - 0.2)^\top = (-0.8,\ -0.5,\ 0.8)^\top.$$
2. **Call the Linear Minimization Oracle (LMO):** Minimize $$\langle \nabla f(x_0), s \rangle$$ over $$s \in \Delta_3$$. The minimum over a simplex is achieved at the standard basis vector corresponding to the smallest gradient coordinate. Here the smallest entry is $$-0.8$$ at index 1, so $$s_0 = e_1 = (1, 0, 0)^\top$$.
3. **Compute the Frank–Wolfe duality gap:**
   $$g_0 = \langle \nabla f(x_0), x_0 - s_0 \rangle = (-0.8)(0 - 1) + (-0.5)(0 - 0) + (0.8)(1 - 0) = 0.8 + 0.8 = 1.6.$$
   This immediately certifies $$f(x_0) - f(x^\star) \le 1.6$$.
4. **Compute the exact line-search step size $$\gamma_0$$:** Along the segment $$x(\gamma) = x_0 + \gamma(s_0 - x_0)$$ with $$d_0 = s_0 - x_0 = (1, 0, -1)^\top$$, we minimize $$\frac{1}{2}\|x_0 + \gamma d_0 - c\|_2^2$$:
   $$\gamma_0 = \operatorname{clip}_{[0,1]}\!\left(\frac{-\langle \nabla f(x_0), d_0 \rangle}{\|d_0\|_2^2}\right) = \operatorname{clip}_{[0,1]}\!\left(\frac{1.6}{1^2 + 0^2 + (-1)^2}\right) = \frac{1.6}{2} = 0.8.$$
5. **Update and verify feasibility:**
   $$x_1 = (1 - 0.8)(0, 0, 1)^\top + 0.8(1, 0, 0)^\top = (0.8, 0, 0.2)^\top.$$
   Notice that $$x_1 \in \Delta_3$$ automatically (entries sum to $$1$$ and are nonnegative), its objective drops from $$f(x_0) = \frac{1}{2}(0.64 + 0.25 + 0.64) = 0.765$$ to $$f(x_1) = \frac{1}{2}(0^2 + (-0.5)^2 + 0^2) = 0.125$$, and it uses only 2 active vertices.

This chapter will examine the Frank-Wolfe algorithm proposed by Marguerite Frank and Philip Wolfe in 1956.

The Frank-Wolfe algorithm is an iterative first-order optimization algorithm for constrained convex optimization, also called the conditional gradient method, reduced gradient method, and convex combination algorithm.

This method was originally proposed by Marguerite Frank and Philip Wolfe in 1956. The Frank-Wolfe algorithm considers a linear approximation of the objective function at each iteration and moves toward the minimizer of this linear function.

[15] Wikipedia. [Frank–Wolfe algorithm](https://en.wikipedia.org/wiki/Frank%E2%80%93Wolfe_algorithm)

## 2026 applications (optional)

The linear-minimization oracle is why Frank–Wolfe survived into the 2020s: structured SVMs, semi-relaxed optimal transport (color transfer), 1-D unbalanced OT, and constrained explanations of neural nets (rate-distortion maps on an $$\ell_1$$ ball or the Birkhoff polytope). See the optional survey [22-05 Modern applications of Frank–Wolfe]({% multilang_post_url contents/chapter22/2026-09-16-22_05_modern_applications %}). Use it after 22-02 / 22-04, not instead of the convergence analysis.
