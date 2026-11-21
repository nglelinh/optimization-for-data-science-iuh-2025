---
layout: post
title: "19-07 Projected Newton method"
chapter: '19'
order: 11
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

## What's wrong with projected Newton?
When $$h$$ is the indicator function $$h = I_C(x)$$ of a convex set $$C$$, the problem becomes

>$$ \min_{x} \ g(x) \quad  \text{subject to}  \quad  x \in C$$

Hence, when $$h(x) = I_C(x)$$, proximal gradient descent becomes **projected gradient descent**. That is, projected gradient descent is a special case of proximal gradient descent.

What about proximal Newton when $$h(x) = I_C(x)$$? In this case the update is

> $$
> \begin{align}
> z^{+} & =\underset{z \in C}{\text{argmin}} \ \frac{1}{2} \parallel x - H^{-1} \nabla g(x) - z \parallel_H^2  \\\\
> &= \underset{z \in C}{\text{argmin}} \ \nabla g(x)^T (z - x) + \frac{1}{2} (z - x)^T H (z - x)  \\\\
> \end{align}
> $$

If $$H = I$$, this is the projection of $$x - \nabla g(x)$$ onto the set $$C$$, but for a general $$H \neq I$$ it is not a projection. (If $$H = I$$ the $$H$$-norm is the $$l_2$$-norm; a projection would require the plain $$l_2$$-norm rather than the $$H$$-norm.)
Therefore, the projected Newton method is not a special case of the proximal Newton method.

## Projected Newton for box constraints
In the special case of box constraints, projected Newton can be applied (Bertsekas, 1982; Kim et al., 2010; Schmidt et al., 2011).

Consider the problem

>$$ \min_{x} \ g(x) \quad  \text{subject to}  \quad  l \le x \le u $$

Given a starting point $$x^{(0)}$$ and a small constant $$\epsilon \gt 0$$, the projected Newton method repeats the following steps ($$k = 1, 2, 3, ...$$).

* Step 1: Define the binding set.

> \begin{align}
B_{k-1} & = \\{ i : x_i^{(k-1)} \le l_i + \epsilon \quad \text{and} \quad  \nabla_i g(x^{(k-1)}) \gt 0 \\} \quad  \cup \quad 
\\{ i : x_i^{(k-1)} \ge u_i - \epsilon  \quad \text{and} \quad  \nabla_i g(x^{(k-1)}) \lt 0 \\} 
\end{align}

In the optimization step, these variables are pushed to the boundary of the box. The more of them we push, the smaller the objective becomes.

* Step 2: Define the free set $$F_{k-1} = \left\{1,....,n \right\} \backslash B_{k-1}$$.
* Step 3: Compute the inverse of the principal submatrix of the Hessian over the free variables.

>$$ S^{(k-1)} = [(\nabla^2 g(x^{(k-1)}))_{F_{k-1}}]^{-1}$$

* Step 4: Take a Newton step over the free variables and project.

> $$
> \begin{align}
> x^{(k)} = P_{[l, u]} \left( x^{(k-1)} - t_k \begin{bmatrix} S^{(k-1)} & 0 \\
> 0 & I \end{bmatrix} 
> \begin{bmatrix} \nabla_{F_{k-1}} g(x^{(k-1)}) \\ \nabla_{B_{k-1}} g(x^{(k-1)}) \end{bmatrix}
> \right)
> \end{align}
> $$

Here $$P_{[l,u]}$$ is the projection onto $$[l, u] = [l_1, u_1] \times \cdots \times [l_n, u_n]$$.

In the matrix expression, a Newton step is taken for the free variables, while for the binding variables a plain gradient step is taken. Also, the projection is a simple operation: for each coordinate outside the box, we simply set it to the appropriate $$l_i$$ or $$u_i$$.

This method is appropriate when the problem is very large (e.g., high-dimensional) and most variables are near the boundary, so that the free set is very small.

What kinds of problems have box constraints? Quite a lot of them do, for example:

*  Nonnegative least squares
*  Support vector machine dual
*  Graphical lasso dual
*  Fused lasso (total variation denoising) dual

## Convergence properties
* Bertsekas (1982) showed that, under suitable assumptions, projected Newton identifies the correct binding constraints after a finite number of iterations. From then on it coincides with Newton's method on the free variables.
*  Bertsekas (1982) also proved superlinear convergence.
*  Kim et al. (2010) and Schmidt et al. (2011) proposed projected quasi-Newton methods using BFGS-style updates.
