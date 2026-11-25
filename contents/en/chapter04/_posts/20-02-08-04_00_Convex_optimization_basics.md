---
layout: post
title: 04 Convex optimization basics
chapter: '04'
order: 1
owner: YoungJae Choung
categories:
- chapter04
lang: en
---

Imagine standing on a foggy mountain range where every valley might be a false bottom—that is general nonlinear optimization. Now imagine the fog lifts and reveals a single, giant smooth bowl: any step downhill eventually leads to the true lowest point on Earth. Chapter 04 formalizes the exact mathematical contract that turns messy engineering and machine-learning problems into that single-bowl world, and shows the legal algebraic moves that preserve it.

## Key ideas: Architecture of a Convex Program

1. **Standard-Form Modeling (Objective, Inequalities, and Affine Equalities)**: A convex program minimizes a convex objective $$f$$ over a domain $$D$$ subject to convex inequalities $$g_i(x) \le 0$$ and *affine* equalities $$h_j(x) = a_j^T x - b_j = 0$$. Requiring equalities to be affine ensures the feasible set stays convex—bending an equality constraint into a curve immediately destroys convexity of the slice.
2. **Global Optimality and Geometry of Solutions**: In a convex program, every local minimum is automatically a global minimum, and the set of all optimal solutions $$X_{\mathrm{opt}}$$ is itself a convex set. When the objective is strictly convex, the solution collapses to a unique point.
3. **First-Order Variational Optimality**: At a minimizer $$x^\star$$ on a convex feasible set $$C$$, moving toward any other feasible point $$y \in C$$ cannot decrease the objective to first order: $$\nabla f(x^\star)^T (y - x^\star) \ge 0$$. Geometrically, $$-\nabla f(x^\star)$$ lies in the normal cone $$N_C(x^\star)$$, a unifying condition that also powers modern differentiable optimization layers.
4. **Convexity-Preserving Reformulations**: Real-world models rarely arrive in textbook standard form. Partial minimization, monotone objective transformations, invertible changes of variables, equality elimination, slack variables, and convex relaxations let you reshape a problem into an equivalent—or tightly bounding—convex program without breaking its global-optimality guarantee.

### Worked example: Certifying and Solving a Constrained Convex Program

Consider minimizing the quadratic objective $$f(x_1, x_2) = (x_1 - 3)^2 + (x_2 - 1)^2$$ subject to the halfspace constraint $$g_1(x) = x_1 + x_2 - 2 \le 0$$.

1. **Check convexity of the formulation**: The Hessian of $$f$$ is $$\nabla^2 f(x) = 2I \succ 0$$, so $$f$$ is strictly convex. The inequality constraint $$g_1(x) = x_1 + x_2 - 2$$ is affine (hence convex), so the feasible set $$C = \{x \in \mathbb{R}^2 : x_1 + x_2 \le 2\}$$ is convex and the solution is guaranteed to be unique.
2. **Test the unconstrained minimizer**: Setting $$\nabla f(x) = (2(x_1 - 3), 2(x_2 - 1)) = (0, 0)$$ yields $$x_{\mathrm{unc}} = (3, 1)$$. Checking feasibility gives $$g_1(3, 1) = 3 + 1 - 2 = 2 > 0$$, so $$x_{\mathrm{unc}}$$ is infeasible and the optimum must lie on the boundary $$x_1 + x_2 = 2$$.
3. **Project onto the boundary**: Substitute $$x_2 = 2 - x_1$$ into $$f$$:
   $$f(x_1, 2 - x_1) = (x_1 - 3)^2 + (1 - x_1)^2 = (x_1^2 - 6x_1 + 9) + (x_1^2 - 2x_1 + 1) = 2x_1^2 - 8x_1 + 10.$$
   Setting the derivative $$4x_1 - 8 = 0$$ gives $$x_1^\star = 2$$, and hence $$x_2^\star = 2 - 2 = 0$$. The optimal value is $$f^\star = (2 - 3)^2 + (0 - 1)^2 = 1 + 1 = 2$$.
4. **Verify the first-order optimality condition**: At $$x^\star = (2, 0)$$, the gradient is $$\nabla f(x^\star) = (2(2-3), 2(0-1)) = (-2, -2)$$. For any feasible $$y = (y_1, y_2)$$ with $$y_1 + y_2 \le 2$$,
   $$\nabla f(x^\star)^T (y - x^\star) = -2(y_1 - 2) - 2(y_2 - 0) = 2\bigl(2 - (y_1 + y_2)\bigr) \ge 0.$$
   Thus $$x^\star = (2, 0)$$ is certified as the unique global minimizer.

## Convex Optimization Basics

This chapter introduces the main properties of convex problems and several techniques commonly used in solving them.

The optional [04-09 Applications and recent developments]({% multilang_post_url contents/chapter04/2026-09-16-04_09_Applications_Recent %}) shows how those optimality residuals become differentiable layers (cvxpylayers, Theseus) and convex decision surrogates.
