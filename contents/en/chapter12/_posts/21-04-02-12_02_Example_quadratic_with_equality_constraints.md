---
layout: post
title: 12-02 Example quadratic with equality constraints
chapter: '12'
order: 3
owner: Wontak Ryu
categories:
- chapter12
lang: en
lesson_type: required
---

Equality-constrained quadratic programs—minimizing $$\frac{1}{2}x^\top P x + q^\top x + r$$ subject to $$Ax = b$$—are the workhorse subproblems inside Newton's method, interior-point solvers, portfolio optimization (Markowitz mean-variance), and Model Predictive Control. Because there are no inequality constraints at all, complementary slackness and dual sign restrictions vanish completely, and the KKT conditions collapse into a single linear block system called the **KKT matrix equation**!

## Key ideas: Equality-Constrained QPs & the KKT Linear System

- **Pillar 1 — Exact Equivalence to a Linear System:** For $$P \succeq 0$$, the problem is convex with affine constraints (Slater holds trivially whenever $$Ax = b$$ is feasible). Thus $$x^\star$$ is optimal *if and only if* there exists $$v^\star \in \mathbb{R}^p$$ satisfying $$P x^\star + A^\top v^\star = -q$$ (stationarity) and $$A x^\star = b$$ (primal feasibility).
- **Pillar 2 — Saddle-Point Block Matrix Structure:** Writing both equations together gives the symmetric $$(n+p) \times (n+p)$$ KKT matrix $$\begin{pmatrix} P & A^\top \\ A & 0 \end{pmatrix} \begin{pmatrix} x^\star \\ v^\star \end{pmatrix} = \begin{pmatrix} -q \\ b \end{pmatrix}$$. Even when $$P \succ 0$$, this matrix is *indefinite* (having positive and negative eigenvalues), reflecting the primal-min / dual-max saddle structure.
- **Pillar 3 — Nonsingularity & Uniqueness:** When $$P \succ 0$$ and $$A$$ has full row rank $$p$$, the KKT matrix is nonsingular and we can eliminate $$x^\star = -P^{-1}(q + A^\top v^\star)$$ via the Schur complement $$A P^{-1} A^\top v^\star = -(b + A P^{-1} q)$$.
- **Pillar 4 — Null-Space Interpretation When $$P$$ Is Singular:** Even if $$P \succeq 0$$ is singular, the KKT matrix remains nonsingular whenever $$P$$ is strictly positive definite on $$\ker(A)$$ (i.e., $$z^\top P z > 0$$ for all nonzero $$z$$ with $$Az = 0$$).

### Worked example: Solving a $$2 \times 2$$ Equality-Constrained QP via the KKT Matrix

Minimize $$\frac{1}{2}(2x_1^2 + 4x_2^2) - 2x_1$$ subject to $$x_1 + x_2 = 3$$.
Here $$P = \begin{pmatrix}2 & 0 \\ 0 & 4\end{pmatrix}$$, $$q = \begin{pmatrix}-2 \\ 0\end{pmatrix}$$, $$A = \begin{pmatrix}1 & 1\end{pmatrix}$$, $$b = (3)$$.

1. **Assemble the $$3 \times 3$$ KKT linear system:**
   $$\begin{pmatrix} 2 & 0 & 1 \\ 0 & 4 & 1 \\ 1 & 1 & 0 \end{pmatrix} \begin{pmatrix} x_1^\star \\ x_2^\star \\ v^\star \end{pmatrix} = \begin{pmatrix} 2 \\ 0 \\ 3 \end{pmatrix}.$$
2. **Express $$x_1^\star, x_2^\star$$ in terms of the multiplier $$v^\star$$ from the first two rows:**
   - Row 1: $$2x_1^\star + v^\star = 2 \implies x_1^\star = 1 - \frac{v^\star}{2}$$.
   - Row 2: $$4x_2^\star + v^\star = 0 \implies x_2^\star = -\frac{v^\star}{4}$$.
3. **Substitute into Row 3 (primal feasibility $$x_1^\star + x_2^\star = 3$$):**
   $$\left(1 - \frac{v^\star}{2}\right) + \left(-\frac{v^\star}{4}\right) = 3 \implies 1 - \frac{3}{4} v^\star = 3 \implies -\frac{3}{4} v^\star = 2 \implies v^\star = -\frac{8}{3}.$$
4. **Back-substitute to recover the exact optimal primal solution:**
   - $$x_1^\star = 1 - \frac{-8/3}{2} = 1 + \frac{4}{3} = \frac{7}{3}$$.
   - $$x_2^\star = -\frac{-8/3}{4} = \frac{2}{3}$$.
   - Check feasibility: $$\frac{7}{3} + \frac{2}{3} = \frac{9}{3} = 3$$! Check stationarity: $$\nabla f(x^\star) = (2(7/3) - 2,\; 4(2/3))^\top = (8/3,\; 8/3)^\top = -v^\star (1, 1)^\top$$—perfectly orthogonal to the constraint line $$x_1 + x_2 = 3$$!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

A [quadratic program]() with only equality constraints is as follows.
>$$
>\begin{align}
>    &\min_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{subject to} &&{Ax = b},\\\\
>&\text{where } &&P \in \mathbb{S}_{+}^n \text{ and } A \in \mathbb{R}^{\text{p x n}}.
>\end{align}
>$$

This problem is convex and has no inequality constraints, so it satisfies Slater's condition (Strong duality). If the primal & dual solutions are $$x^\star, \nu^\star$$, then by KKT conditions they satisfy the following conditions [1].

* Stationarity: $$Px^\star + q + A^T\nu^\star = 0$$
* Complementary Slackness: Since there are no inequality constraints, this does not need to be considered.
* Primal & dual feasibility: $$Ax^\star = b$$

These conditions can be concisely expressed using a block matrix, which is called the KKT matrix [3].
> $$
> \begin{bmatrix}
>     P       & A^T  \\\\
>     A       & 0  \\\\
> \end{bmatrix}
> \begin{bmatrix}
>     x^\star  \\\\
>     \nu^\star  \\\\
> \end{bmatrix}
> =
> \begin{bmatrix}
>     -q  \\\\
>     b  \\\\
> \end{bmatrix}
> $$

Solving this matrix equation gives the primal & dual solutions for the given problem.

An interesting fact is that this problem can also be seen as computing the Newton step for an equality constrained problem [3]. For the problem $$min_x f(x) \text{ subject to } Ax = b$$, if we set P, q, r as follows, then the objective function of the quadratic program becomes identical to the second-order Taylor expansion of $$f(x)$$.<br/>
> $$P = \nabla^2 f(x^{(k-1)})$$, $$q = \nabla f(x^{(k-1)})$$, $$r = f(x^{(k-1)})$$