---
layout: post
title: "21-01 Last time - Dual method, Augmented Lagrangian method, ADMM, ADMM in scaled form"
chapter: '21'
order: 2
owner: Hooncheol Shin
categories:
- chapter21
lang: en
---

In the previous chapter (Chapter 20) we studied dual methods and ADMM. Before looking at applications of ADMM, let us summarize dual methods, the augmented Lagrangian method, ADMM, and ADMM in scaled form.

## Dual method
Consider the following problem.

>$$
>\begin{align}
>&\min_{x} &&f(x) \\\\
>&\text{ subject to } &&Ax = b
>\end{align}
>$$

Assume that $$f$$ is strictly convex and closed. The Lagrangian of this problem is
>$$
>\begin{align}
>L(x,u) = f(x)+u^{T}(Ax-b)
>\end{align}
>$$

The dual problem is
>$$
>\begin{equation}
>\max_u -f^{\ast}(-A^T u) - b^T u
>\end{equation}
>$$

where $$u$$ is the dual variable.

Dual gradient ascent for this problem repeats the following updates ($$k=1,2,3,...$$).
>$$
>\begin{align}
>x^{(k)}&=\underset{x}{\operatorname{argmin}} L(x,u^{(k-1)}) \\\\
>u^{(k)}&= u^{(k-1)} +t_{k}(Ax^{(k)}-b)
>\end{align}
>$$

Here $$t_{k}$$ is the step size at the $$k$$-th iteration.

In this dual method, as in the first update, the primal variable $$x$$ is set to the minimizer of the Lagrangian at the dual variable $$u^{(k-1)}$$ from the previous step, and the dual variable $$u$$ is updated by gradient ascent, where $$Ax-b$$ is the gradient direction.

The advantage of this method is that when $$f$$ is decomposable into $$B$$ parts, $$x$$ can also be split into $$B$$ blocks $$( x =(x_{1}, ...,x_{B})\in \mathbb{R}^{n}, \text{ where }x_{i}\in \mathbb{R}^{n_{i}})$$ and the matrix $$A$$ into $$B$$ sub-matrix blocks $$(A = [A_{1}, ..., A_{B}] \text{ where }A_{i} \in \mathbb{R}^{m \times n_{i}})$$, so the computation is easy to parallelize and scale. The drawback is that demanding conditions are needed to guarantee convergence: to guarantee primal feasibility, $$f$$ must be strongly convex. [[20-01-01]]({% multilang_post_url contents/chapter20/21-03-27-20_01_01_Convergence_Analysis %})

## Augmented Lagrangian method
The augmented Lagrangian method, also called the method of multipliers, adds an extra term to the primal problem. As the iterations proceed, the KKT conditions are gradually satisfied. Compared with the dual method, it relaxes the condition needed for convergence ($$f$$ strongly convex). In exchange, the problem can no longer be decomposed. The primal problem is defined as follows.

>$$
>\begin{align}
>&\min_{x} &&f(x)+\frac{\rho}{2}||Ax-b||_{2}^{2}&\\\\
>&\text{subject to} &&Ax=b
>\end{align}
>$$

where $$\rho>0$$. The Lagrangian of this problem is

>$$
>\begin{align}
>L_{\rho}(x,u)=f(x)+u^{T}(Ax-b)+\frac{\rho}{2}||Ax-b||_{2}^{2}.
>\end{align}
>$$

Dual gradient ascent repeats the following ($$k=1,2,3,...$$).
>$$
>\begin{align}
>x^{(k)}&=\underset{x}{\operatorname{argmin}} L_{\rho}(x,u^{(k-1)}) \\\\
>u^{(k)}&= u^{(k-1)} +\rho(Ax^{(k)}-b)
>\end{align}
>$$

As mentioned above, the advantage of this method is better convergence conditions than the dual method. The drawback is that the added quadratic term destroys decomposability.

## Alternating direction method of multipliers (ADMM)
ADMM combines the advantages of the dual method and the augmented Lagrangian method. Suppose the problem is of the following form.

>$$
>\begin{align}
>\min_{x} f(x)+g(z) \qquad \text{subject to  }Ax+Bz=c
>\end{align}
>$$

For this problem we can define the augmented Lagrangian with $$\rho>0$$.
>$$
>\begin{align}
>&L_{\rho} (x,z,u) = f(x)+g(z)+u^{T}(Ax+Bz-c)+\frac{\rho}{2}||Ax+Bz-c||_{2}^{2}\\\\
>\end{align}
>$$

We then update the variables by repeating the following.
>$$
>\begin{align}
>&\text{for k = 1,2,3,...}\\\\
>&x^{(k)}=\underset{x}{\operatorname{argmin}} L_{\rho}(x,z^{(k-1)},u^{(k-1)})\\\\
>&z^{(k)}=\underset{z}{\operatorname{argmin}} L_{\rho}(x^{(k)},z,u^{(k-1)})\\\\
>&u^{(k)}=u^{(k-1)}+\rho(Ax^{(k)}+Bz^{(k)}-c)
>\end{align}
>$$

In ADMM, the primal variables $$x, z$$ are not updated jointly but one after the other. When updating sequentially, the other variable takes its most recent value. That is, when updating $$z$$ at iteration $$k$$ we use $$x^{(k)}$$ rather than the value $$x^{(k-1)}$$ from the previous iteration, and when updating $$u$$ we immediately use the primal variables $$x^{(k)}, z^{(k)}$$ just computed in the current iteration.

## Convergence of ADMM
Without assuming that $$A$$ and $$B$$ in the constraint have full rank, and under only modest assumptions on $$f$$ and $$g$$, ADMM satisfies the following for every $$\rho > 0$$.

* Residual convergence: $$r^{(k)} = A x^{(k)} + B z^{(k)} - c \to 0$$ as $$k \to \infty$$, i.e. the primal iterates approach feasibility.
* Objective convergence: $$f(x^{(k)}) + g(z^{(k)}) \to f^{\star} + g^{\star}$$, where $$f^{\star} + g^{\star}$$ is the optimal primal objective value.
* Dual convergence: $$u^{(k)} \to u^{\star}$$, where $$u^{\star}$$ is a dual solution.

The convergence rate is not known in general and is still being studied. References on convergence are given in the [introduction to Chapter 21]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %}).

## ADMM in scaled form
ADMM can be written in scaled form by replacing the dual variable $$u$$ with the scaled variable $$w=u/\rho$$. The ADMM steps then become
>$$
>\begin{align}
&x^{(k)} = \underset{x}{\operatorname{argmin}} f(x) + \frac{\rho}{2} ||Ax + Bz^{(k-1)} - c + w^{(k-1)} ||_2^2 \\\\
&z^{(k)} = \underset{z}{\operatorname{argmin}} g(z) + \frac{\rho}{2} || Ax^{(k)} + Bz - c + w^{(k-1)} ||_2^2  \\\\
&w^{(k)} = w^{(k-1)} + Ax^{(k)} + Bz^{(k)} - c 
\end{align}
>$$

Here $$w^{(k)}$$ is the running sum of the residuals up to iteration $$k$$, which can also be written as
>$$
>\begin{align}
w^{(k)} = w^{(0)} + \sum_{i=1}^k (Ax^{(i)} + Bz^{(i)} - c) 
\end{align}
>$$
