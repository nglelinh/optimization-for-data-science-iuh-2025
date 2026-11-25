---
layout: post
title: 05-03 Quadratically Constrained Quadratic Programming (QCQP)
chapter: '05'
order: 9
owner: Hooncheol Shin
categories:
- chapter05
lang: en
---

Sometimes a quadratic objective is not enough—the *constraints* themselves are curved. When a robot must stay inside a circular safety zone, an antenna array must obey a total power budget $$\|w\|_2^2 \le P_{\max}$$, or a portfolio must cap its variance $$x^T \Sigma x \le \sigma_{\max}^2$$, the feasible region becomes an intersection of ellipsoids rather than flat walls. That is the domain of Quadratically Constrained Quadratic Programming (QCQP).

## Background Knowledge Map: Geometry and Reformulations of QCQPs

1. **Convexity Condition on Every Matrix $$P_i$$**: A QCQP minimizes $$\frac{1}{2}x^T P_0 x + q_0^T x + r_0$$ subject to $$\frac{1}{2}x^T P_i x + q_i^T x + r_i \le 0$$ ($$i = 1, \dots, m$$) and $$Ax = b$$. The problem is convex if and only if **every** symmetric matrix $$P_0, P_1, \dots, P_m \in \mathbb{S}_+^n$$ is positive semidefinite.
2. **Geometric Picture — Intersection of Ellipsoids**: Each inequality $$\frac{1}{2}x^T P_i x + q_i^T x + r_i \le 0$$ defines an ellipsoid (when $$P_i \succ 0$$) or an elliptic cylinder (when $$P_i \succeq 0$$ is singular). Notice that setting $$P_1 = \dots = P_m = 0$$ recovers a QP, and further setting $$P_0 = 0$$ recovers an LP.
3. **Every Convex QCQP Rewrites as an SOCP**: Factoring $$P_i = L_i L_i^T$$ lets you complete the square and turn any convex quadratic inequality into a Euclidean norm constraint $$\|A_i x + b_i\|_2 \le c_i^T x + d_i$$, allowing modern conic solvers (like Clarabel or ECOS) to solve QCQPs natively.
4. **Warning on Nonconvex QCQPs**: If even a single $$P_i$$ has a negative eigenvalue (or if a quadratic constraint is written as an *equality* $$x^T P_i x = 1$$), the problem becomes nonconvex and generally NP-hard—requiring SDP relaxation (Shor relaxation) to obtain tight lower bounds.

### Step-by-Step Worked Example (Read Slowly): Solving a Disk-Constrained Quadratic Program

Minimize $$f_0(x_1, x_2) = (x_1 - 3)^2 + (x_2 - 4)^2$$ subject to the quadratic ball constraint $$x_1^2 + x_2^2 \le 4$$.

1. **Verify standard convex QCQP form**:
   - Objective: $$f_0(x) = \frac{1}{2}x^T (2I) x + (-6, -8)x + 25$$, so $$P_0 = 2I \succ 0$$.
   - Constraint: $$\frac{1}{2}x^T (2I) x - 4 \le 0$$, so $$P_1 = 2I \succ 0$$. Both matrices are positive definite, guaranteeing a unique global minimizer.
2. **Check the unconstrained minimizer**: $$x_{\mathrm{unc}} = (3, 4)$$ has $$\|x_{\mathrm{unc}}\|_2^2 = 3^2 + 4^2 = 25 > 4$$, so it lies outside the disk of radius $$2$$. Thus the quadratic constraint must be active: $$\|x^\star\|_2 = 2$$.
3. **Apply the KKT stationarity condition**: With multiplier $$\lambda \ge 0$$ for $$g_1(x) = x_1^2 + x_2^2 - 4 \le 0$$,
   $$\nabla f_0(x) + \lambda \nabla g_1(x) = 0 \implies 2(x - x_{\mathrm{unc}}) + 2\lambda x = 0 \implies (1 + \lambda) x = (3, 4).$$
4. **Solve for $$\lambda^\star$$ and $$x^\star$$**: Taking norms of $$(1 + \lambda)x^\star = (3, 4)$$ gives
   $$(1 + \lambda)\|x^\star\|_2 = \|(3, 4)\|_2 = 5 \implies (1 + \lambda)(2) = 5 \implies 1 + \lambda^\star = 2.5 \implies \lambda^\star = 1.5 > 0.$$
   Hence $$x^\star = \frac{1}{2.5}(3, 4) = (1.2, 1.6)$$. Check feasibility: $$1.2^2 + 1.6^2 = 1.44 + 2.56 = 4$$. Optimal value: $$(1.2 - 3)^2 + (1.6 - 4)^2 = (-1.8)^2 + (-2.4)^2 = 3.24 + 5.76 = 9 = (5 - 2)^2$$.

If the inequality constraint functions in a quadratic program are replaced with convex quadratic functions, the problem is called a *Quadratically Constrained Quadratic Program* (QCQP).

### Quadratically Constrained Quadratic Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P_0 x + q_0^T x + r_0} \\\\
>    &\text{subject to } &&{(1/2)x^T P_i x + q_i^T x + r_i \leq 0}, i = 1, \dotsc, m\\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P_i \in \mathbb{S}_{+}^n \text{ for } i = 0, \dotsc, m, \text{ and } A \in \mathbb{R}^{p \times n}.
>\end{align} $$

## QP and equivalent QCQP
If $$P_i = 0$$ for all $$i = 1, \dotsc, m$$ in the QCQP constraints, the problem reduces to a QP. Thus, QP is a special case of QCQP, and $$QP \subseteq QCQP$$.

### Recall: Quadratic Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{subject to } &&{Gx \preceq h} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P \in \mathbb{S}_{+}^n, G \in \mathbb{R}^{m \times n}, \text{ and } A \in \mathbb{R}^{p \times n}.
>\end{align} $$