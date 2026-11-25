---
layout: post
title: 17-02-01 Central path equations and Newton step
chapter: '17'
order: 4
owner: Minjoo Lee
categories:
- chapter17
lang: en
---

If you tried to apply Newton's method directly to the *unperturbed* KKT conditions, the complementarity equations $$u_i h_i(x) = 0$$ would form sharp L-shaped kinks at the boundary, trapping iterates on the wrong active face. By perturbing the right-hand side to $$u_i h_i(x) = -\tau$$, those kinks melt into smooth hyperbolas whose Jacobian is nonsingular everywhere in the strict interior. This lesson builds that exact residual map $$r_\tau(x, u, v)$$ and its block-structured Newton linear system.

## Key ideas: Linearizing the Perturbed KKT Map

- **Perturbed KKT Residual Map:** Stacking stationarity, perturbed complementarity, and equality feasibility into $$r_\tau(x, u, v) = [r_{\text{dual}}; r_{\text{cent}}; r_{\text{prim}}]$$ converts a constrained optimization problem into a smooth square system of $$n + m + p$$ nonlinear equations in $$n + m + p$$ unknowns.
- **Root-Finding Newton Linearization:** Expanding $$r_\tau(z + \Delta z) \approx r_\tau(z) + Dr_\tau(z)\,\Delta z = 0$$ yields the primal-dual search direction $$(\Delta x, \Delta u, \Delta v)$$ via a single linear solve $$Dr_\tau(z)\,\Delta z = -r_\tau(z)$$.
- **Block Structure of the KKT Jacobian:** The derivative $$Dr_\tau$$ combines the Lagrangian Hessian $$\nabla^2 f(x) + \sum_i u_i \nabla^2 h_i(x)$$, the constraint Jacobians $$\nabla h(x)$$ and $$A$$, and the diagonal scaling matrices $$U = \operatorname{diag}(u)$$ and $$H = \operatorname{diag}(h(x))$$.
- **Schur-Complement Reduction:** Because the complementarity block $$U \nabla h(x)\,\Delta x + H\,\Delta u = -r_{\text{cent}}$$ is diagonal in $$\Delta u$$, solvers eliminate $$\Delta u = -H^{-1}(r_{\text{cent}} + U \nabla h(x)\,\Delta x)$$ analytically, reducing the KKT system to a smaller symmetric system in $$(\Delta x, \Delta v)$$.

### Worked example: Solving the Primal-Dual Newton System by Hand

Consider the 1D quadratic problem $$\min_x \frac{1}{2} x^2 + x$$ subject to $$h(x) = -x \le 0$$ (exact optimum $$x^\star = 0, u^\star = 1$$).

1. **Write the residual map $$r_\tau(x, u)$$:**
   Here $$f'(x) = x + 1$$, $$f''(x) = 1$$, $$h(x) = -x$$, $$h'(x) = -1$$, and there are no equality constraints. Thus:
   $$r_\tau(x, u) = \begin{bmatrix} x + 1 - u \\ -u x + \tau \end{bmatrix}.$$
2. **Compute the Jacobian $$Dr_\tau(x, u)$$:**
   $$Dr_\tau(x, u) = \begin{bmatrix} f''(x) & h'(x) \\ u h'(x) & h(x) \end{bmatrix} = \begin{bmatrix} 1 & -1 \\ -u & -x \end{bmatrix}.$$
3. **Evaluate at $$(x, u) = (1, 1)$$ with target $$\tau = 0.2$$:**
   $$r_{0.2}(1, 1) = \begin{bmatrix} 1 + 1 - 1 \\ -(1)(1) + 0.2 \end{bmatrix} = \begin{bmatrix} 1 \\ -0.8 \end{bmatrix}, \qquad Dr_{0.2}(1, 1) = \begin{bmatrix} 1 & -1 \\ -1 & -1 \end{bmatrix}.$$
4. **Solve $$Dr_{0.2}(1, 1) \begin{bmatrix}\Delta x \\ \Delta u\end{bmatrix} = -r_{0.2}(1, 1)$$:**
   $$\begin{cases} \Delta x - \Delta u = -1 \\ -\Delta x - \Delta u = 0.8 \end{cases}$$
   Adding both equations gives $$-2\Delta u = -0.2 \implies \Delta u = 0.1$$. Substituting back gives $$\Delta x = -1 + 0.1 = -0.9$$.
5. **Check the updated point $$(x^+, u^+) = (1 - 0.9, \; 1 + 0.1) = (0.1, \; 1.1)$$:**
   Both coordinates remain strictly positive ($$x^+ = 0.1 > 0, u^+ = 1.1 > 0$$)! Moreover:
   - Dual residual: $$x^+ + 1 - u^+ = 0.1 + 1 - 1.1 = 0$$ (exact stationarity achieved in one step!).
   - Complementarity product: $$u^+ x^+ = (1.1)(0.1) = 0.11$$ (reduced from $$1.0$$ down near $$\tau = 0.2$$, with the discrepancy $$0.11 - 0.2 = -0.09 = \Delta x \Delta u$$ coming purely from the second-order bilinear term!).

The **Primal-dual interior-point method** is a method that finds solutions by finding the central path, similar to the barrier method. To do this, it defines perturbed KKT conditions as residual functions and finds solutions that make them zero. This section aims to explain this approach.

## Central path equations
By moving the right-hand side to the left-hand side in the central path equations explained in the previous [17-01 Optimality conditions]({% multilang_post_url contents/chapter17/21-05-01-17_01_barrier_method_duality_optimality_revisited %}), we can organize them as follows. (The optimality conditions of central path equations are also called perturbed KKT conditions.)
> $$
> \begin{array}{rcl}
> ∇f(x) +∇h(x)u + A^Tv & = & 0 \\\
>  Uh(x) + \tau\mathbb{1}  & = & 0 \\\
> Ax−b & = & 0 \\\
> u,−h(x)  & > & 0
> \end{array}
> $$

Note that the complementary slackness and inequality constraints in the KKT conditions for the original problem differ from those in the perturbed KKT conditions. For the original problem, $$Uh(x) = 0$$ and $$u,−h(x)  \ge 0$$, but in the perturbed KKT conditions, $$Uh(x) = - \tau\mathbb{1}$$ and $$u,−h(x)  \gt 0$$.

These organized nonlinear equations, the perturbed KKT conditions, can be solved by approximating them as linear equations using the root finding version of Newton's method.

## Newton step
Now let's learn about the method of finding solutions by linearly approximating the perturbed KKT conditions. The perturbed KKT conditions equation can be defined as the following residual function $$r(x, u, v) = 0$$. (The reason for naming it residual is that these values must be 0 to be optimal.)

> $$r(x,u,v) :=
> \begin{bmatrix}
> ∇f(x) +∇h(x)u + A^Tv \\\
> Uh(x) + τ\mathbb{1} \\\
> Ax−b
> \end{bmatrix}, H(x) = \text{Diag}(h(x))$$

To find the roots of the function, approximating $$r(x, u, v)$$ with a first-order Taylor expansion gives us the following. (This process approximates non-linear equations to linear equations. For detailed information, see [14-02-01 Root finding]({% multilang_post_url contents/chapter14/2021-03-26-14_01_newton_method %}))
>$$\begin{align}
0 & = r(x + \Delta x, u + \Delta u, r + \Delta v)  \\\\
  & \approx r(x, u, v) + \nabla r(x, u, v) 
\begin{pmatrix}
\Delta x \\\\
\Delta u \\\\
\Delta v \\\\
\end{pmatrix} \\\\
\end{align}$$

Accordingly, the function $$r(x, u, v)$$ can be organized as follows.

>$$\begin{align}
\nabla r(x, u, v) 
\begin{pmatrix}
\Delta x \\\\
\Delta u \\\\
\Delta v \\\\
\end{pmatrix} = -r(x, u, v) \\\\
\end{align}$$

By differentiating $$r(x, u, v)$$ with respect to $$x, u, v$$ to obtain the Jacobian matrix $$\nabla r(x, u, v)$$ and substituting the above equation, we get the following.
> $$\begin{bmatrix}
> \nabla^2f(x) + \sum_i u_i \nabla^2h_i(x) & \nabla h(x) & A^T \\\
>  U \nabla  h(x)^T & H(x) & 0 \\\
> A & 0 & 0
> \end{bmatrix}
> \begin{bmatrix}
> \Delta x \\\
> \Delta u \\\
> \Delta v
> \end{bmatrix} = −r(x,u,v)$$
> where
> $$r(x,u,v) :=
> \begin{bmatrix}
> \nabla f(x) +\nabla h(x)u + A^Tv \\\
> Uh(x) + τ\mathbb{1} \\\
> Ax−b
> \end{bmatrix}, H(x) = \text{Diag}(h(x))$$

The solution $$(\Delta x, \Delta u, \Delta v)$$ to this equation is the update direction for the primal and dual variables. The reason why the method introduced in this chapter is called the **Primal-Dual** interior point method is that it simultaneously updates primal and dual variables using residual functions.