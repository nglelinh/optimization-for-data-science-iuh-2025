---
layout: post
title: 05-06 Conic Programming (CP)
chapter: '05'
order: 12
owner: Hooncheol Shin
categories:
- chapter05
lang: en
---

After seeing LPs, SOCPs, and SDPs, you might notice a striking pattern: every single one minimizes a *linear* objective $$c^T x$$ subject to affine equalities $$Ax = b$$ and a membership constraint saying that an affine expression must stay inside a convex cone $$K$$. Conic Programming (CP) is the grand unified abstraction that captures all of them—plus exponential and power cones—under one mathematical roof and one solver API.

## Key ideas: The Unified Conic Framework

1. **Proper Cones and Generalized Inequalities**: A cone $$K \subseteq \mathbb{R}^m$$ is *proper* if it is convex, closed, solid (non-empty interior), and pointed ($$K \cap (-K) = \{0\}$$). Any proper cone induces a partial order $$u \preceq_K v \iff v - u \in K$$, generalizing scalar $$\le$$ to vectors and matrices.
2. **All Canonical Classes as Choices of $$K$$**:
   - **LP**: $$K = \mathbb{R}^m_+$$ (nonnegative orthant).
   - **SOCP**: $$K = \mathcal{Q}_{n_1} \times \cdots \times \mathcal{Q}_{n_r}$$ (Cartesian product of second-order cones).
   - **SDP**: $$K = \mathbb{S}^k_+$$ (positive semidefinite cone).
   - **Exponential / Power Cones**: Handle logarithms, entropy, relative entropy, and $$p$$-norms cleanly inside modern conic solvers (like Clarabel and MOSEK).
3. **Why Solvers Love Conic Form**: Moving all nonlinearity out of the objective and constraints and into a small library of standard cones $$K$$ means a solver only needs to know the barrier function and dual cone $$K^\star = \{y : y^T x \ge 0 \;\forall x \in K\}$$ for those few cones.
4. **Self-Dual Cones**: The three classical cones—$$\mathbb{R}^m_+$$, $$\mathcal{Q}_n$$, and $$\mathbb{S}^k_+$$—are *self-dual* ($$K^\star = K$$), which gives primal–dual interior-point methods extraordinary symmetry and numerical precision.

### Worked example: Unifying an LP and an SOCP Inside One Product Cone

Consider minimizing $$x_1 + x_2$$ subject to $$x_1 \ge 1$$ and $$\sqrt{x_1^2 + x_2^2} \le 2$$. Let us express this single problem as a standard Conic Program $$\min c^T x \text{ s.t. } Fx + g \preceq_K 0$$.

1. **Identify the required product cone $$K$$**:
   - Constraint 1 ($$x_1 \ge 1 \iff 1 - x_1 \le 0$$) lives in the 1D nonnegative orthant $$K_1 = \mathbb{R}_+$$.
   - Constraint 2 ($$\|x\|_2 \le 2 \iff (x_1, x_2, 2) \in \mathcal{Q}_3$$) lives in the 3D second-order cone $$K_2 = \mathcal{Q}_3$$.
   - Combine them into the product cone $$K = \mathbb{R}_+ \times \mathcal{Q}_3 \subseteq \mathbb{R}^4$$.
2. **Write $$s = -(Fx + g) \in K$$ explicitly**:
   $$s = \begin{bmatrix} x_1 - 1 \\ x_1 \\ x_2 \\ 2 \end{bmatrix} = \underbrace{\begin{bmatrix} 1 & 0 \\ 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}}_{-F} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \underbrace{\begin{bmatrix} -1 \\ 0 \\ 0 \\ 2 \end{bmatrix}}_{-g} \in \mathbb{R}_+ \times \mathcal{Q}_3.$$
3. **Solve the conic program geometrically**: We want the smallest $$x_1 + x_2$$ inside the disk $$x_1^2 + x_2^2 \le 4$$ with $$x_1 \ge 1$$.
   - To minimize $$x_1 + x_2$$, push $$x_1$$ as small as allowed ($$x_1^\star = 1$$) and $$x_2$$ as negative as the disk permits: $$x_2^\star = -\sqrt{4 - 1^2} = -\sqrt{3}$$.
   - Check gradient/feasibility on the boundary: at $$x = (1, -\sqrt{3})$$, $$s = (0, 1, -\sqrt{3}, 2)^T$$ has $$s_1 = 0 \in \mathbb{R}_+$$ and $$\sqrt{1^2 + (-\sqrt{3})^2} = 2 \le 2$$, so $$s \in K$$ and $$f^\star = 1 - \sqrt{3} \approx -0.732$$.

If the inequality constraint in a general LP is replaced by a generalized inequality constraint, the problem is called a *Conic Program* (CP).

### Conic Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{Fx + g \preceq_K 0} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&c, x \in \mathbb{R}^{n}, A \in \mathbb{R}^{p \times n}, \text{and } b \in \mathbb{R}^{p}.
>\end{align}$$

* $$F: \mathbb{R}^n \rightarrow Y$$ is a linear map, $$g \in Y$$, for Euclidean space $$Y$$.
* LP is the special case when $$K = \mathbb{R}_{+}^n$$, i.e., LP $$\subseteq$$ CP.
* SDP is the special case when $$K = \mathbb{S}_{+}^n$$, i.e., SDP $$\subseteq$$ CP.