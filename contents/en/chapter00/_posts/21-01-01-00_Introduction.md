---
layout: post
title: 00 Introduction
chapter: '00'
order: 1
owner: GitHub Copilot
lang: en
categories:
- chapter00
---

Imagine piloting an autonomous spacecraft through a gravitational valley with a fixed fuel tank: every thruster firing is a decision vector, fuel consumption is the objective, and orbital safety corridors are the constraints. Before you can design the autopilot—or prove that it will never get trapped in a false valley—you need a sharp mathematical language for *rates of change*, *multidimensional geometry*, *sets and limits*, and *uncertainty*. Chapter 00 builds that exact toolkit so that every theorem in convex optimization feels inevitable rather than mysterious.

## Background Knowledge Map: The Four Mathematical Pillars of Optimization

- **Multivariable Calculus (Local Geometry & Descent):** Gradients point uphill, Hessians measure curvature, and Taylor expansions turn nonlinear objectives into tractable local quadratics. Without calculus, first- and second-order optimality conditions cannot even be stated.
- **Linear Algebra (Structure & Conditioning):** Decision variables live in $$\mathbb{R}^n$$, linear constraints are matrix equations $$Ax = b$$, and eigenvalues of the Hessian govern how fast gradient methods converge. Poor conditioning stretches level sets into narrow canyons.
- **Set Theory & Real Analysis (Existence of Solutions):** Continuity and compactness (Weierstrass's theorem) tell us when a minimum actually exists instead of escaping to infinity or approaching an unattainable boundary.
- **Probability & Statistics (Data-Driven Objectives):** Empirical risk minimization, maximum likelihood estimation, and stochastic gradient methods all cast statistical inference directly as optimization problems over noisy data.

### Step-by-Step Worked Example (Read Slowly): Unifying Calculus and Linear Algebra on a 2D Quadratic

Consider minimizing the coupled quadratic objective:

$$f(x_1, x_2) = (x_1 - 2)^2 + 4(x_2 + 1)^2 + x_1 x_2$$

1. **Compute the gradient (first-order condition):** Differentiate with respect to each coordinate and set $$\nabla f(x_1, x_2) = \mathbf{0}$$:
   $$\frac{\partial f}{\partial x_1} = 2(x_1 - 2) + x_2 = 2x_1 + x_2 - 4 = 0$$
   $$\frac{\partial f}{\partial x_2} = 8(x_2 + 1) + x_1 = x_1 + 8x_2 + 8 = 0$$
2. **Solve the linear system:** From the second equation, $$x_1 = -8x_2 - 8$$. Substituting into the first gives:
   $$2(-8x_2 - 8) + x_2 - 4 = -15x_2 - 20 = 0 \implies x_2^* = -\frac{4}{3}, \quad x_1^* = -8\left(-\frac{4}{3}\right) - 8 = \frac{8}{3}.$$
3. **Verify optimality via the Hessian (linear algebra):**
   $$\nabla^2 f(x_1, x_2) = \begin{pmatrix} 2 & 1 \\ 1 & 8 \end{pmatrix}.$$
   Its trace is $$2 + 8 = 10 > 0$$ and its determinant is $$2(8) - 1^2 = 15 > 0$$, so both eigenvalues are strictly positive. Therefore $$\nabla^2 f \succ 0$$ everywhere, certifying that $$x^* = (8/3, -4/3)^T$$ is the unique global minimizer.

Optimization is at the heart of data science. Whether you're training a neural network, minimizing errors in regression models, or efficiently allocating resources in recommendation systems, you're essentially solving problems that involve finding the "best" solution from a vast set of possibilities. But to do this effectively, you need to speak the language of mathematics. We'll revisit key ideas from linear algebra, set theory, and calculus, ensuring you're equipped to handle gradients, matrices, constraints, and uncertainties that arise in optimization tasks.

A later optional lesson, [00-05 Applications and recent developments]({% multilang_post_url contents/chapter00/2026-09-16-00_05_Applications_Recent %}), maps those same tools onto autodiff, LoRA, and diffusion models (2022–2025).