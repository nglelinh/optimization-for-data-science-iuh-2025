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

When a barrier solver runs, measuring how close you are to optimality is easy: every iterate is feasible, so $$f(x) - g(u, v) = m/t$$ is a genuine, certified upper bound on suboptimality. Once a primal-dual solver allows *infeasible* iterates, $$g(u, v)$$ may not even be finite—so how do we know whether a step actually improved things, or when it is safe to stop? The answer lies in splitting the KKT error into three distinct residuals and replacing the true duality gap with a **surrogate duality gap**.

## Background Knowledge Map: Measuring Progress Without Feasibility

- **Primal Residual ($$r_{\text{prim}} = Ax - b$$):** Quantifies violation of linear equality constraints. Driving $$\|r_{\text{prim}}\|_2 \to 0$$ pulls iterates onto the affine feasible subspace.
- **Dual Residual ($$r_{\text{dual}} = \nabla f(x) + \nabla h(x) u + A^T v$$):** Measures violation of Lagrangian stationarity. Only when $$r_{\text{dual}} = 0$$ does $$x$$ minimize $$L(\cdot, u, v)$$, certifying that $$(u, v)$$ lies in the domain of the dual function $$g$$.
- **Centrality Residual ($$r_{\text{cent}} = U h(x) + \tau \mathbf{1}$$):** Tracks how far each inequality's complementarity product $$-u_i h_i(x)$$ deviates from the uniform central-path target $$\tau$$, preventing any single constraint from slamming into the boundary prematurely.
- **Surrogate Duality Gap ($$\eta = -h(x)^T u$$):** Defined whenever $$h(x) \le 0$$ and $$u \ge 0$$, $$\eta \ge 0$$ equals the true duality gap *if and only if* $$r_{\text{prim}} = 0$$ and $$r_{\text{dual}} = 0$$. In the algorithm, $$\eta / m$$ dynamically sets the next target $$\tau = \sigma \eta / m$$.

### Step-by-Step Worked Example (Read Slowly): Auditing Residuals and Surrogate Gap at an Infeasible Point

Consider the convex QP $$\min \frac{1}{2}(x_1^2 + x_2^2)$$ subject to $$x_1 + x_2 = 2$$ and $$h_1(x) = -x_1 \le 0, \; h_2(x) = -x_2 \le 0$$ ($$m = 2$$). Evaluate the residuals at the infeasible interior iterate $$x = (0.5, 1.0)^T$$, $$u = (0.4, 0.6)^T$$, $$v = -1.0$$ with $$\tau = 0.5$$.

1. **Primal residual:**
   $$r_{\text{prim}} = Ax - b = (0.5 + 1.0) - 2 = -0.5 \implies \|r_{\text{prim}}\|_2 = 0.5.$$
2. **Dual residual:**
   Since $$\nabla f(x) = (x_1, x_2)^T$$, $$\nabla h(x) = -I$$, and $$A^T = (1, 1)^T$$:
   $$r_{\text{dual}} = \begin{bmatrix} 0.5 \\ 1.0 \end{bmatrix} - \begin{bmatrix} 0.4 \\ 0.6 \end{bmatrix} + (-1.0)\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} -0.9 \\ -0.6 \end{bmatrix}, \quad \|r_{\text{dual}}\|_2 = \sqrt{0.81 + 0.36} = \sqrt{1.17} \approx 1.0817.$$
3. **Surrogate duality gap:**
   $$\eta = -h(x)^T u = x_1 u_1 + x_2 u_2 = (0.5)(0.4) + (1.0)(0.6) = 0.2 + 0.6 = 0.8.$$
   Notice why $$\eta = 0.8$$ is only a *surrogate*: at $$x = (0.5, 1.0)$$, $$f(x) = 0.625$$ is actually *below* the true optimal value $$f^\star = 1.0$$ (at $$x^\star = (1, 1)$$) because $$x$$ is primal infeasible!
4. **Centrality residual:**
   $$r_{\text{cent}} = U h(x) + \tau \mathbf{1} = \begin{bmatrix} -0.2 + 0.5 \\ -0.6 + 0.5 \end{bmatrix} = \begin{bmatrix} 0.3 \\ -0.1 \end{bmatrix}.$$
5. **Diagnostic takeaway:**
   Although the average complementarity $$\eta/m = 0.4$$ is modest, the combined feasibility residual $$\sqrt{\|r_{\text{prim}}\|_2^2 + \|r_{\text{dual}}\|_2^2} = \sqrt{0.25 + 1.17} = \sqrt{1.42} \approx 1.1916$$ is still large, so a solver cannot terminate until *both* $$\eta \le \epsilon$$ and $$\sqrt{\|r_{\text{prim}}\|_2^2 + \|r_{\text{dual}}\|_2^2} \le \epsilon$$ hold.

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

