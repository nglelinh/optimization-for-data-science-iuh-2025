---
layout: post
title: 11-04 Strong duality
chapter: '11'
order: 5
owner: Wontak Ryu
categories:
- chapter11
lang: en
lesson_type: required
---

Weak duality ($$g^\star \le f^\star$$) is free, but **strong duality** ($$g^\star = f^\star$$)—the guarantee that solving the dual gives the *exact* primal optimal value—is the crown jewel that makes dual solvers and KKT conditions work. Does convexity alone guarantee strong duality? Surprisingly, *no*! There exist tiny, smooth convex problems with a nonzero duality gap when the feasible set lacks an interior. **Slater's condition** fixes this with one breathtakingly simple geometric check: if the problem is convex and there exists even *one* strictly feasible point $$x$$ with $$h_i(x) < 0$$ (and $$l_j(x) = 0$$), strong duality holds!

## Background Knowledge Map: When the Duality Gap Vanishes Completely

- **Pillar 1 — Convexity Is Necessary in General, Not Alone Sufficient:** Without a constraint qualification, the epigraph of the optimal-value function can have a vertical tangent at zero perturbation, preventing any finite Lagrange multiplier from supporting it and creating a nonzero gap even for convex problems.
- **Pillar 2 — Slater's Condition (Strict Feasibility):** For a convex problem, if there exists $$x \in \operatorname{relint}(\mathcal{D})$$ such that $$h_i(x) < 0$$ for all *non-affine* inequality constraints and $$l_j(x) = 0$$ (plus affine inequalities $$h_k(x) \le 0$$ need not be strict!), then $$g^\star = f^\star$$ and the dual optimum is attained whenever $$f^\star > -\infty$$.
- **Pillar 3 — Affine Refinement (Why LPs Need No Strict Interior):** Because linear inequalities need not be strictly satisfied in refined Slater's condition, every feasible linear program automatically satisfies strong duality without needing an interior point.
- **Pillar 4 — SVM Dual & the Kernel Trick:** In Support Vector Machines, the primal is a convex QP with purely affine constraints ($$y_i(x_i^\top \beta + \beta_0) \ge 1 - \xi_i, \xi_i \ge 0$$). Slater's condition holds trivially (just pick $$\beta = 0, \beta_0 = 0, \xi_i = 2$$!), guaranteeing strong duality and letting us replace inner products $$x_i^\top x_j$$ with nonlinear kernels $$K(x_i, x_j)$$ in the dual!

### Step-by-Step Worked Example (Read Slowly): Checking Slater's Condition on a Convex Problem (Pass vs. Fail)

1. **Example A — Slater's Condition Passes (Convex QCQP):**
   $$\min_{x \in \mathbb{R}^2}\; x_1 + x_2 \quad \text{s.t.} \quad x_1^2 + x_2^2 - 4 \le 0, \quad x_1 - x_2 = 0.$$
   - Check convexity: objective is linear (convex), $$h_1(x) = x_1^2 + x_2^2 - 4$$ is convex, $$l_1(x) = x_1 - x_2$$ is affine.
   - Test $$x = (0, 0)^\top$$: $$h_1(0, 0) = -4 < 0$$ (strictly negative!) and $$l_1(0, 0) = 0$$.
   - **Verdict:** Slater's condition holds $$\implies$$ strong duality $$g^\star = f^\star = -2\sqrt{2}$$ is guaranteed!
2. **Example B — Slater's Condition Fails (Boundary-Only Feasible Set):**
   $$\min_{x \in \mathbb{R}^2}\; e^{-x_1} \quad \text{s.t.} \quad x_1^2 / x_2 \le 0, \quad x_2 > 0.$$
   - Wait: $$h_1(x) = x_1^2 / x_2$$ is convex on $$x_2 > 0$$, and $$x_1^2 / x_2 \le 0$$ forces $$x_1 = 0$$—so **no** point can make $$h_1(x) < 0$$! Slater fails!
   - Primal value: since $$x_1 = 0$$ on the entire feasible set, $$f^\star = e^0 = 1$$.
   - Dual value: $$L(x, u) = e^{-x_1} + u x_1^2 / x_2$$. For any $$u \ge 0$$, send $$x_2 \to +\infty$$ with fixed $$x_1 > 0$$ to get $$\inf_{x_2 > 0} L(x, u) = e^{-x_1}$$, and then send $$x_1 \to +\infty$$ to get $$g(u) = 0$$ for all $$u \ge 0$$!
   - **Verdict:** $$g^\star = 0 < 1 = f^\star$$—a genuine nonzero duality gap in a **convex** problem because Slater's condition failed!

When a problem satisfies $$f^* = g^*$$, this is called **strong duality**. The **Slater condition** is a sufficient condition for strong duality.

## Slater condition: 
If the primal problem is convex and there exists at least one strictly feasible $$x \in \mathbb{R}^n$$, then strong duality holds.
>
$$
\begin{equation}
h_1(x)<0,\dots,h_m(x)<0, \text{ and } l_1(x) = 0,\dots,l_r(x) = 0,
\end{equation}
$$

Important refinement: Strict inequality need not be satisfied when the function is affine.
## Example: Support Vector Machine Dual 
Given $$y \in \{-1,1\}^n$$, $$X \in \mathbb{R}^{n \times p}$$ (where the columns of $$X$$ are $$x_1, ..., x_n$$), the SVM (Support Vector Machine) problem is defined as follows.

>
$$
\begin{alignat}{1}
\min_{\beta, \beta_0, \xi} & \quad \frac{1}{2}\parallel\beta\parallel_2^2 + C \sum_{i=1}^n \xi_i   \\\\
                                  s.t. & \quad \xi_i \geq 0, i=1,\dots,n   \\\\
                                       & \quad y_i(x_i^T \beta + \beta_0) \geq 1 - \xi_i, i=1,\dots,n
\end{alignat}
$$

Using dual variables $$v, w \geq 0$$, let us define the Lagrangian:
>
\begin{equation}
L(\beta,\beta_0,\xi,v,w) = \frac{1}{2} \parallel\beta\parallel_2^2 + C\sum_{i=1}^n \xi_i - \sum_{i=1}^n v_i \xi_i +  \sum_{i=1}^n w_i (1-\xi_i - y_i(x_i^T\beta + \beta_0))
\end{equation}


By minimizing with respect to $$\beta, \beta_0, \xi$$, we can obtain the following Lagrangian dual function:
>
$$
g(v,w) = 
\begin{cases}
-\frac{1}{2} w^T\tilde{X}\tilde{X}^T w +  1^Tw, &\text{if $w=C1-v, w^Ty=0$} \\\\
-\infty, &\text{otherwise}
\end{cases}
$$

Here $$\tilde{X}=\text{diag}(y) X$$. Therefore, the SVM dual problem (after eliminating the slack variable $$v$$) becomes the following. 
>
$$
\begin{alignat}{1}
\max_{w}  & \quad -\frac{1}{2} w^T\tilde{X}\tilde{X}^T w +  1^Tw \\\\
     s.t. &  \quad 0 \leq w \leq C1, w^Ty = 0
\end{alignat}
$$

Since the primal problem satisfies the Slater condition, strong duality holds. (That is, the objective is convex and the inequality constraints are affine in $$\beta, \beta_0, \xi$$.)

### Strong duality and Slater in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/strong-duality-slater_en.mp4"></video>
</div>

The dual function g(λ) below p*, the duality gap as a certificate, the (u, t) picture of supporting lines, and a convex problem without Slater whose gap is 1.
