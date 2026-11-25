---
layout: post
title: 17-02 Primal-dual interior-point method
chapter: '17'
order: 3
owner: Minjoo Lee
categories:
- chapter17
lang: en
---

At first glance, switching from the barrier method to a primal-dual interior-point method looks like a minor engineering tweak—dropping the inner loop and taking one Newton step per $$\tau$$ update. In practice, that single architectural shift transforms interior-point optimization from a textbook curiosity into the fastest general-purpose convex solver engine ever built. Understanding *why* one coupled primal-dual step outperforms an entire inner barrier loop is the conceptual heart of Chapter 17.

## Background Knowledge Map: Barrier Method vs. Primal-Dual Philosophy

- **Single-Loop Coupled Newton Dynamics:** The barrier method isolates primal updates inside an inner loop while holding $$t$$ fixed; PD-IPM updates $$(x, u, v)$$ simultaneously in one linearized KKT solve and decreases $$\tau$$ at every iteration.
- **Infeasible-Start Flexibility:** Barrier methods demand a strictly feasible starting point satisfying $$Ax^0 = b$$ and $$h(x^0) < 0$$ (often requiring a full Phase I solve). PD-IPMs only require strict interiority of the inequalities and multipliers ($$h(x^0) < 0, u^0 > 0$$), driving $$Ax^k - b \to 0$$ automatically along the way.
- **Direct Control of Complementarity:** Because $$u$$ is an independent variable rather than a post-hoc formula $$-1/(t h(x))$$, the linearized complementarity equation $$U \nabla h(x)\,\Delta x + H(x)\,\Delta u = -Uh(x) - \tau \mathbf{1}$$ directly balances primal slackness against dual magnitude.
- **Superlinear Local Acceleration:** Near the solution, the coupled KKT Jacobian approaches the exact Newton system for the active constraints, allowing PD-IPMs to transition from linear global progress to superlinear (and in LP, quadratic) local convergence.

### Step-by-Step Worked Example (Read Slowly): Handling an Infeasible Start

Suppose we want to solve the LP $$\min 2x_1 + 3x_2$$ subject to $$x_1 + x_2 = 4$$ and $$x_1, x_2 \ge 0$$ (exact optimum $$x^\star = (4, 0), v^\star = -2, u^\star = (0, 1)$$).

1. **Pick a simple interior starting point that violates the equality constraint:**
   Set $$x^0 = (2, 1)$$, $$u^0 = (1, 1)$$, $$v^0 = 0$$. Notice $$x^0 > 0$$ and $$u^0 > 0$$, so the strict positivity requirement holds, even though $$x_1^0 + x_2^0 = 3 \neq 4$$ (primal residual $$r_{\text{prim}}^0 = -1$$). A standard barrier method cannot even start here without a Phase I problem.
2. **Check the dual residual:**
   With $$c = (2, 3)^T$$, $$A = [1, 1]$$, and $$h(x) = -x$$:
   $$r_{\text{dual}}^0 = c - u^0 + A^T v^0 = \begin{bmatrix} 2 \\ 3 \end{bmatrix} - \begin{bmatrix} 1 \\ 1 \end{bmatrix} + \begin{bmatrix} 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}.$$
3. **See how one Newton step eliminates infeasibility:**
   In the primal-dual Newton system, the equality row enforces $$A \Delta x = -r_{\text{prim}}^0 = 1$$ (i.e., $$\Delta x_1 + \Delta x_2 = 1$$), and the stationarity row enforces $$-\Delta u + A^T \Delta v = -r_{\text{dual}}^0$$.
4. **Observe the exact contraction law for linear residuals:**
   For *any* step length $$\theta \in (0, 1]$$ chosen by backtracking, the updated residuals satisfy:
   $$r_{\text{prim}}(z^0 + \theta \Delta z) = (1 - \theta) r_{\text{prim}}^0, \qquad r_{\text{dual}}(z^0 + \theta \Delta z) = (1 - \theta) r_{\text{dual}}^0.$$
   If $$\theta = 0.8$$ is feasible, both primal and dual infeasibility shrink by $$80\%$$ in a single iteration—and as soon as a full step $$\theta = 1$$ is accepted, both linear residuals vanish identically to $$0$$ for all remaining iterations!

Like the barrier method, the **primal-dual interior-point method** also aims to (approximately) compute points on the central path. However, the two methods have several differences.

## Differences between Primal-dual interior-point method and barrier method
* Generally performs **one Newton step** per iteration. (That is, there is no additional loop for the centering step.)
* **Does not necessarily need to be feasible**. (Pushes toward feasible regions through backtracking line search.)
* Generally **more effective**. Particularly shows superior performance compared to linear convergence under appropriate conditions.
* Somewhat less intuitive compared to the barrier method.
