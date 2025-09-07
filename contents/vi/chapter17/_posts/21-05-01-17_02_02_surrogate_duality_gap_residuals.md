---
layout: post
title: 17-02-02 Surrogate duality gap, residuals
chapter: '17'
order: 5
owner: Minjoo Lee
categories:
- chapter17
lang: en
---
To define the Primal-Dual algorithm, let's first define three types of residuals and the surrogate duality gap. Residuals and surrogate duality gap are the objectives to be minimized in the Primal-Dual algorithm.

## Residuals
The dual, central, and primal residuals at $$(x,u,v)$$ are defined as follows. 

> $$r_{dual} = \nabla f(x) +\nabla h(x)u + A^Tv\\$$
> $$r_{cent} =  Uh(x) + τ\mathbb{1} \\ $$ 
> $$r_{prim} = Ax−b$$

These correspond to each row of the function $$r(x,u,v)$$. The **Primal-dual interior point method** executes in the direction of satisfying 0 rather than continuously making these three residuals equal to 0. This means that it is not necessary to be feasible during the execution process.

The reason $$r_{dual}$$ is called the dual residual is that, as shown in the equation below, if $$r_{dual} = 0$$, it guarantees that $$u, v$$ are in the domain of $$g$$, which means dual feasible.

>$$\begin{align}
& r_{dual} = \nabla f(x) +\nabla h(x)u + A^Tv = 0 \\\\
& \iff \min_{x} L(x,u.v) = g(u,v) \\\\
\end{align}$$

Similarly, satisfying $$r_{prim}=0$$ means primal feasible, so $$r_{prim}$$ is called the primal residual.

## Surrogate duality gap
While the barrier method has a duality gap because it is feasible, the primal-dual interior-point method uses **surrogate duality gap** because it doesn't necessarily need to be feasible. **Surrogate duality gap** is defined by the following equation.

> $$−h(x)^Tu  \quad \text{for} \quad h(x) \le 0, u \ge 0$$ 

If $$r_{dual} = 0$$ and $$r_{prim} = 0$$, then the surrogate duality gap becomes the true duality gap. In other words, if primal and dual feasible, the surrogate duality gap becomes equal to the actual duality gap $$\frac{m}{t}$$.

**[Reference] Perturbed KKT conditions and parameter t** <br>

* In the perturbed KKT conditions, the parameter t is $$t = −\frac{m}{h(x)^Tu}$$. 
* For detailed information, see [15-03-01 Perturbed KKT conditions]({% multilang_post_url contents/chapter15/21-03-28-15_03_01_perturbed_kkt_conditions %}) and [15-03-02 Suboptimality gap]({% multilang_post_url contents/chapter15/21-03-28-15_03_02_suboptimality_gap %})

Furthermore, if $$u > 0,h(x) < 0$$ and the following condition is satisfied, then $$(x,u,v)$$ exists on the central path.

> $$r(x,u,v) = 0$$ for $$\tau = -\frac{h(x)^Tu}{m}$$

In other words, the residual is 0 at points existing on the central path.

