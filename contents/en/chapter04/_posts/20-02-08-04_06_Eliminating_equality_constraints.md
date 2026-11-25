---
layout: post
title: 04-06 Eliminating equality constraints
chapter: '04'
order: 7
owner: YoungJae Choung
categories:
- chapter04
lang: en
---

If a robot arm is bolted to a flat rail, you do not need three spatial coordinates to describe its position—one coordinate along the rail tells the whole story. Eliminating affine equality constraints $$Ax = b$$ works on the exact same principle: every feasible vector $$x$$ splits into a single particular anchor $$x_0$$ plus a free movement $$My$$ inside the null space of $$A$$, turning a constrained problem into a lower-dimensional problem with no equality constraints at all.

## Background Knowledge Map: Null-Space Parameterization of Affine Constraints

1. **Affine Subspace Decomposition**: Whenever $$Ax = b$$ is consistent, pick any particular solution $$x_0$$ with $$Ax_0 = b$$ and a matrix $$M \in \mathbb{R}^{n \times (n-r)}$$ whose columns form a basis for $$\operatorname{null}(A)$$ (where $$r = \operatorname{rank}(A)$$). Then $$\{x : Ax = b\} = \{My + x_0 : y \in \mathbb{R}^{n-r}\}$$, giving an exact, redundancy-free parameterization.
2. **Convexity Is Automatically Preserved**: Substituting $$x = My + x_0$$ composes the convex objective $$f$$ and convex inequalities $$g_i$$ with an affine map. Because pre-composition with an affine function always preserves convexity, the reduced problem in $$y$$ is guaranteed to remain convex.
3. **Dimension Reduction vs. Sparsity Loss**: Eliminating $$r$$ independent equalities shrinks the variable count from $$n$$ to $$n - r$$, which is great for small dense problems or analytical derivations. However, for large sparse systems (e.g., network flows or PDE meshes), computing a null-space basis $$M$$ via QR/SVD can be expensive and turn a sparse problem into a dense one—which is why large-scale solvers often keep $$Ax = b$$ explicitly via KKT systems.
4. **Choice of Basis $$M$$ Matters Numerically**: Using an *orthonormal* basis $$M$$ (so $$M^T M = I$$, obtained from QR factorization of $$A^T$$) preserves Euclidean norms and avoids inflating the condition number of the Hessian $$M^T \nabla^2 f(x) M$$.

### Step-by-Step Worked Example (Read Slowly): Reducing a 3D Constrained Quadratic to a 1D Unconstrained Problem

Minimize $$f(x_1, x_2, x_3) = x_1^2 + 2x_2^2 + x_3^2$$ subject to the two linear equalities:
$$x_1 + x_2 + x_3 = 6, \qquad x_1 - x_3 = 0.$$

1. **Write the system as $$Ax = b$$**:
   $$A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 0 & -1 \end{bmatrix}, \qquad b = \begin{bmatrix} 6 \\ 0 \end{bmatrix}.$$
   Since $$\operatorname{rank}(A) = 2$$ and $$n = 3$$, the null space has dimension $$3 - 2 = 1$$.
2. **Find a particular solution $$x_0$$ and a null-space basis $$M$$**:
   - Setting $$x_3 = 0$$ gives $$x_1 = 0$$ and $$x_2 = 6$$, so $$x_0 = (0, 6, 0)^T$$ satisfies $$Ax_0 = (6, 0)^T = b$$.
   - For $$Av = 0$$: $$v_1 - v_3 = 0 \implies v_1 = v_3$$, and $$v_1 + v_2 + v_3 = 0 \implies v_2 = -2v_3$$. Choosing $$v_3 = 1$$ gives the basis column $$M = (1, -2, 1)^T$$.
   - Check $$AM = (1 - 2 + 1,\; 1 - 1)^T = (0, 0)^T$$.
3. **Substitute $$x = My + x_0 = (y,\; 6 - 2y,\; y)^T$$ into the objective**:
   $$\tilde{f}(y) = y^2 + 2(6 - 2y)^2 + y^2 = 2y^2 + 2(36 - 24y + 4y^2) = 10y^2 - 48y + 72.$$
4. **Solve the unconstrained 1D problem and lift back to $$x$$**:
   Setting $$\tilde{f}'(y) = 20y - 48 = 0$$ gives $$y^\star = \frac{48}{20} = 2.4$$.
   Substituting back:
   $$x^\star = M(2.4) + x_0 = \begin{bmatrix} 2.4 \\ 6 - 4.8 \\ 2.4 \end{bmatrix} = \begin{bmatrix} 2.4 \\ 1.2 \\ 2.4 \end{bmatrix}.$$
   Verify constraints: $$2.4 + 1.2 + 2.4 = 6$$ and $$2.4 - 2.4 = 0$$. Optimal value: $$f(x^\star) = 2.4^2 + 2(1.2)^2 + 2.4^2 = 5.76 + 2.88 + 5.76 = 14.4$$.

This section explains techniques for eliminating equality constraints in convex optimization problems to simplify the feasible set or problem structure.

>$$
\begin{aligned}
&\min_{x} &&f(x)\\
&\text{subject to } &&g_{i}(x) \leq 0, i = 1, .., m\\
&&&{Ax = b}.\\
\end{aligned}
$$

For an arbitrary solution $$x_{0}$$ satisfying $$Ax_{0} = b$$ and $$\text{col}(M) = \text{null}(A)$$, any $$x$$ that satisfies the equality constraint can be expressed as follows:
>$$x = My + x_{0}$$

That is, $$Ax = A(My + x_{0}) = AMy + Ax_{0} = 0 + b = b$$. Therefore, by substituting $$My+x_{0}$$ for $$x$$ in the given problem, we can eliminate the equality constraint.

Thus, the following problem is equivalent to the original problem:

>$$
\begin{aligned}
&\min_y &&f(My+x_0)\\
&\text{subject to} &&g_{i}(My+x_{0}) \leq 0, i = 1, .., m.\\
\end{aligned}
$$

However, caution is advised when using this method for the following reasons:
1. The computation of $$M$$ is generally very expensive.
2. If $$x$$ is sparser than $$y$$, the cost of computation using $$y$$ may be higher.
