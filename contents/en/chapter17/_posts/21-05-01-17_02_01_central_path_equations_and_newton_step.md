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