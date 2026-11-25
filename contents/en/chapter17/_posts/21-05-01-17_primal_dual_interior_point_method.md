---
layout: post
title: 17 Primal-Dual Interior-Point Methods
chapter: '17'
order: 1
owner: Minjoo Lee
categories:
- chapter17
lang: en
---

Imagine piloting a glider down a deep, steep-walled canyon toward a tiny landing strip wedged in the corner where two sheer cliffs meet. The classical log-barrier method from Chapter 15 flies cautiously: it freezes an altitude parameter, takes a full sequence of Newton corrections until it sits dead-center in the canyon, then drops the altitude slightly and repeats the entire centering ritual. **Primal-dual interior-point methods (PD-IPMs)** throw away that inner loop. Instead of solving a sequence of subproblems to high precision, they treat the primal variables, dual multipliers, and complementarity conditions as one coupled nonlinear system—taking a *single* damped Newton step per iteration that simultaneously drives feasibility and optimality to zero.

## Key ideas: The Architecture of Primal-Dual Interior-Point Methods

- **Perturbed KKT Systems & the Central Path:** Rather than minimizing an unconstrained barrier objective directly, PD-IPMs formulate optimality as root-finding on the perturbed KKT map $$r_\tau(x, u, v) = 0$$, where complementary slackness $$u_i h_i(x) = 0$$ is relaxed to $$u_i h_i(x) = -\tau$$ for $$\tau > 0$$. Driving $$\tau \to 0$$ traces a smooth analytic curve—the *central path*—leading directly into the optimal primal-dual face.
- **Simultaneous Newton Linearization:** Applying Newton's root-finding method directly to $$r_\tau(x, u, v) = 0$$ produces a single coupled linear system for $$(\Delta x, \Delta u, \Delta v)$$. Because primal and dual variables inform each other inside the same Jacobian, one step can make dramatic progress without ever converging an inner centering loop.
- **Infeasible-Start Trajectory & Surrogate Duality Gap:** Unlike the barrier method, PD-IPMs do not require $$Ax^k = b$$ or dual feasibility at intermediate iterates—only strict positivity of slacks and multipliers ($$-h(x^k) > 0, u^k > 0$$). Progress is tracked jointly via the primal/dual residual norms and the *surrogate duality gap* $$\eta = -h(x)^T u$$.
- **Conic Generality (LP, QP, SOCP, SDP):** The primal-dual framework lifts effortlessly from nonnegative orthants (Linear Programming) to symmetric positive semidefinite cones (Semidefinite Programming), powering modern solvers such as Clarabel, MOSEK, and SDPT3 with polynomial-time worst-case complexity and superlinear local convergence.

### Worked example: One Primal-Dual Step vs. Barrier Centering

Consider the minimal 1D constrained problem $$\min_{x \in \mathbb{R}} x$$ subject to $$h(x) = -x \le 0$$ (exact optimum $$x^\star = 0, u^\star = 1$$).

1. **Write the perturbed KKT residual:**
   With $$f'(x) = 1$$ and $$h'(x) = -1$$, the perturbed KKT conditions for target $$\tau > 0$$ are:
   $$r_\tau(x, u) = \begin{bmatrix} 1 - u \\ -u x + \tau \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}, \quad x > 0, \; u > 0.$$
2. **Start from a dual-infeasible interior point:**
   Take $$(x^0, u^0) = (2, 0.5)$$. Note that $$r_{\text{dual}}^0 = 1 - 0.5 = 0.5 \neq 0$$, and the surrogate duality gap is $$\eta_0 = -h(x^0) u^0 = (2)(0.5) = 1.0$$. With centering parameter $$\sigma = 0.5$$, set $$\tau = \sigma \eta_0 / m = 0.5(1.0)/1 = 0.5$$.
3. **Form and solve the single primal-dual Newton system:**
   The Jacobian of $$r_\tau$$ is $$J(x, u) = \begin{bmatrix} 0 & -1 \\ -u & -x \end{bmatrix} = \begin{bmatrix} 0 & -1 \\ -0.5 & -2 \end{bmatrix}$$, and $$r_\tau(2, 0.5) = \begin{bmatrix} 0.5 \\ -0.5 \end{bmatrix}$$. Solving $$J \Delta z = -r_\tau$$:
   $$-\Delta u = -0.5 \implies \Delta u = 0.5,$$
   $$-0.5\,\Delta x - 2(0.5) = 0.5 \implies -0.5\,\Delta x = 1.5 \implies \Delta x = -3.$$
4. **Apply fraction-to-the-boundary damping:**
   A full step $$\theta = 1$$ would give $$x^0 + \Delta x = 2 - 3 = -1 < 0$$, violating $$x > 0$$. The maximum boundary step is $$\theta_{\max} = \frac{2}{3}$$. Choosing $$\theta = 0.5 < \theta_{\max}$$ yields:
   $$x^1 = 2 + 0.5(-3) = 0.5 > 0, \qquad u^1 = 0.5 + 0.5(0.5) = 0.75 > 0.$$
5. **Verify simultaneous progress:**
   In just *one* linear solve, the dual residual dropped in half ($$0.5 \to 0.25$$) and the surrogate gap fell by $$62.5\%$$ ($$1.0 \to 0.5 \times 0.75 = 0.375$$), with no inner centering loop required.

In this chapter, we will examine the **Primal-Dual Interior-Point Method**, which improves performance by reducing the centering step of the Barrier method we learned earlier to a single step.

The **Primal-Dual Interior-Point Method** relaxes the constraint that the centering step must be feasible and uses the root finding version of Newton's Method to approximate nonlinear equations with linear equations to find solutions, making it faster and more accurate than the Barrier method.

## References and further readings
* S. Boyd and L. Vandenberghe (2004), “Convex optimization,” Chapter 11
* S. Wright (1997), “Primal-dual interior-point methods,” Chapters 5 and 6
* J. Renegar (2001), “A mathematical view of interior-point methods”
* Y. Nesterov and M. Todd (1998), “Primal-dual interior-point methods for self-scaled cones.” SIAM J. Optim.