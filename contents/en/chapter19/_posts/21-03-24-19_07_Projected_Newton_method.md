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

Here is a trap that catches almost every graduate student the first time they try to add box constraints $$x \ge 0$$ to Newton's method: *"For gradient descent, we just project $$x - t\nabla g(x)$$ onto $$C$$. So for Newton's method, can't we just project $$x - H^{-1}\nabla g(x)$$ onto $$C$$?"* **NO!** Because the Newton direction is only guaranteed to descend in the *$$H$$-metric*, applying a *Euclidean* projection $$\Pi_C$$ can twist the direction past $$90^\circ$$ from $$-\nabla g(x)$$ and turn it into an **ascent direction**! Dimitri Bertsekas's **Projected Newton method** fixes this brilliantly by decoupling the *binding* (active) coordinates from the *free* coordinates.

## Background Knowledge Map: Why Naive Projection Fails and How Bertsekas Fixes It

- **Metric Mismatch of Naive Projected Newton:** Proximal Newton for $$h = I_C$$ solves $$\min_{z \in C} \|x - H^{-1}\nabla g(x) - z\|_H^2$$ (an oblique $$H$$-projection, which is a full QP). Replacing $$\|\cdot\|_H$$ with Euclidean $$\|\cdot\|_2$$ breaks the optimality geometry and can increase $$g(x)$$.
- **Binding vs. Free Variables ($$x \ge 0$$):** For nonnegativity constraints, a coordinate $$i$$ is in the **binding set** $$\mathcal{B}(x)$$ if $$x_i = 0$$ (or $$\le \epsilon$$) *and* $$\nabla_i g(x) > 0$$ (meaning the negative gradient pushes it straight into the wall). All other coordinates are **free** ($$\mathcal{F}(x)$$).
- **Block-Diagonal Hessian Scaling (Bertsekas 1982):** By zeroing out the off-diagonal couplings between $$\mathcal{B}(x)$$ and $$\mathcal{F}(x)$$ in the Hessian inverse (keeping a positive diagonal on $$\mathcal{B}$$ and the exact inverse $$H_{\mathcal{F}\mathcal{F}}^{-1}$$ on $$\mathcal{F}$$), Euclidean projection $$\Pi_C(x - t D \nabla g(x))$$ is *mathematically guaranteed* to be a descent direction!
- **Superlinear Speed on Box Constraints:** Once the active face $$\mathcal{B}(x^\star)$$ is identified, Bertsekas's projected Newton takes exact full Newton steps on the free subspace $$\mathcal{F}(x^\star)$$ while clamping $$\mathcal{B}(x^\star)$$ at zero—giving quadratic local convergence with trivial $$O(n)$$ Euclidean projection!

### Step-by-Step Worked Example (Read Slowly): Catching Naive Projected Newton Going Uphill!

Minimize $$g(x) = \frac{1}{2} x^T H x + c^T x$$ over the nonnegative orthant $$C = \{x \in \mathbb{R}^2 : x_1 \ge 0, x_2 \ge 0\}$$, where:
$$H = \begin{bmatrix} 1 & 2 \\ 2 & 5 \end{bmatrix} \succ 0, \qquad c = \begin{bmatrix} 1 \\ 1 \end{bmatrix}.$$
Notice at $$x = (0, 0)^T$$, $$\nabla g(0) = (1, 1)^T > 0$$, so $$x = (0, 0)^T$$ is **already the unique global minimizer** ($$g(0) = 0$$, and $$g(x) > 0$$ for all $$x \ge 0, x \neq 0$$)!

1. **Compute the unconstrained Newton step from $$x = (0, 0)^T$$:**
   Since $$\det(H) = 5 - 4 = 1$$, $$H^{-1} = \begin{bmatrix} 5 & -2 \\ -2 & 1 \end{bmatrix}$$. Thus:
   $$p_N = -H^{-1}\nabla g(0) = -\begin{bmatrix} 5 & -2 \\ -2 & 1 \end{bmatrix}\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} -3 \\ +1 \end{bmatrix}.$$
2. **Apply naive Euclidean projection $$\Pi_C(x + t p_N)$$ for any $$t > 0$$:**
   $$z_{\text{naive}}(t) = \Pi_{\mathbb{R}_+^2}\!\begin{bmatrix} -3t \\ t \end{bmatrix} = \begin{bmatrix} 0 \\ t \end{bmatrix}.$$
   Evaluate the objective at $$z_{\text{naive}}(t)$$:
   $$g(0, t) = \frac{5}{2} t^2 + t > 0 = g(0, 0) \quad \text{for ALL } t > 0!$$
   Naive projected Newton walks strictly **uphill** from the exact optimum for *every* positive step size!
3. **Apply Bertsekas's Projected Newton fix:**
   At $$x = (0, 0)^T$$, both $$x_1 = 0, \nabla_1 g = 1 > 0$$ and $$x_2 = 0, \nabla_2 g = 1 > 0$$ belong to the binding set $$\mathcal{B} = \{1, 2\}$$. Bertsekas replaces $$H$$ on $$\mathcal{B}$$ by its positive diagonal $$D_{\mathcal{B}} = \operatorname{diag}(1, 5)$$, giving direction $$-D_{\mathcal{B}}^{-1}\nabla g(0) = (-1, -0.2)^T$$. Projecting onto $$\mathbb{R}_+^2$$ yields $$(0, 0)^T$$—staying locked at the true optimum immediately!

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
