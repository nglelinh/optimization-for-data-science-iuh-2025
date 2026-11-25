---
layout: post
title: 16-02 Optimality conditions
chapter: '16'
order: 3
owner: Minjoo Lee
categories:
- chapter16
lang: en
---

When you check whether a candidate point $$(x, u, v)$$ is optimal for a convex program, the KKT conditions give you a four-part checklist: primal feasibility, dual feasibility, complementary slackness, and stationarity. When you compare that checklist side-by-side against the optimality conditions of the **barrier problem**, you discover something remarkable: three of the four equations are *identical*, and the fourth merely shifts $$u_i h_i(x) = 0$$ to $$u_i h_i(x) = -1/t$$.

## Key ideas: Exact KKT vs. Central-Path Optimality

- **Pillar 1 — Sufficiency of KKT for Convex Problems:** When $$f, h_1, \dots, h_m$$ are convex and differentiable and $$l_1, \dots, l_r$$ are affine, any $$(x^\star, u^\star, v^\star)$$ satisfying KKT is guaranteed globally primal and dual optimal with zero duality gap.
- **Pillar 2 — Necessity via Slater's Condition:** Under strict feasibility (Slater's condition), strong duality holds and KKT conditions become both *necessary and sufficient*.
- **Pillar 3 — Barrier KKT as a Homotopy Deformation:** Introducing $$u_i(t) = -\frac{1}{t h_i(x^*(t))} > 0$$ rewrites barrier optimality as exact stationarity, exact primal/dual feasibility, and perturbed complementarity $$u_i h_i = -1/t$$.
- **Pillar 4 — Measuring Distance to KKT (Residuals):** Primal-dual solvers track three residuals—primal residual $$r_{\text{pri}} = Ax - b$$, dual residual $$r_{\text{dual}} = \nabla f + \sum u_i \nabla h_i + A^T v$$, and complementarity residual $$r_{\text{cent}} = -u \odot h - \frac{1}{t}\mathbf{1}$$—driving all three to zero simultaneously.

### Worked example: Comparing Exact KKT and Barrier KKT Residuals

Consider $$\min_{x \in \mathbb{R}} (x - 4)^2$$ subject to $$h_1(x) = x - 2 \le 0$$ (i.e., $$x \le 2$$).

1. **Solve the exact KKT conditions:**
   - Stationarity: $$2(x^\star - 4) + u_1^\star (1) = 0 \implies u_1^\star = 2(4 - x^\star)$$.
   - Try inactive ($$u_1^\star = 0$$): gives $$x = 4$$, violating $$x \le 2$$.
   - Try active ($$x^\star = 2$$): gives $$u_1^\star = 2(4 - 2) = 4 \ge 0$$, and $$u_1^\star h_1(x^\star) = 4(0) = 0$$. **Exact KKT optimum:** $$(x^\star, u_1^\star) = (2, 4)$$.
2. **Now test a central-path point at $$t = 10$$:**
   - Perturbed KKT equations: $$2(x - 4) + u_1 = 0$$ and $$u_1(x - 2) = -\frac{1}{10} = -0.1$$ with $$x < 2, u_1 > 0$$.
   - Substitute $$u_1 = 8 - 2x$$: $$(8 - 2x)(x - 2) = -0.1 \implies 2x^2 - 12x + 15.9 = 0$$.
   - Root with $$x < 2$$: $$x^*(10) = \frac{12 - \sqrt{144 - 127.2}}{4} = \frac{12 - \sqrt{16.8}}{4} \approx 1.9753$$.
   - Dual variable: $$u_1(10) = 8 - 2(1.9753) = 4.0494$$.
3. **Check all residuals:** $$r_{\text{dual}} = 2(1.9753 - 4) + 4.0494 = 0$$, $$r_{\text{cent}} = -u_1 h_1 - 0.1 = -(4.0494)(-0.0247) - 0.1 = 0$$, and $$(1.9753, 4.0494)$$ is already within $$0.05$$ of the exact KKT pair $$(2, 4)$$!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

In this section, we will examine the KKT optimality conditions for primal problems and barrier problems respectively, and then compare their differences.
<br/>

## KKT optimality conditions

Let's review the KKT conditions that we covered in Chapter 12. KKT conditions are used as conditions for determining optimality.

### Primal problem
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad f(x) \\\\
>    \text{subject to} &\quad h_i(x) \leq 0, i = 1, \ldots, m \\\\
>    &\quad l_j(x) = 0, j = 1, \ldots, r
>\end{align}
>$$

When the given primal problem is convex, KKT conditions become sufficient conditions for primal & dual optimality. That is, when $$f, h_1, \dots, h_m$$ are convex and $$l_1, \dots, l_r$$ are affine, if $$x^\star, u^\star, v^\star$$ satisfy the following KKT conditions, then $$x^\star$$ and $$(u^\star, v^\star)$$ are primal & dual optimal with zero duality gap. (We assume that $$f, h_1, \dots, h_m, l_1, \dots, l_r$$ are differentiable.) <br>

* reference: [12-01 KKT conditions]({% multilang_post_url contents/chapter12/21-04-02-12_00_KKT_conditions %})

### KKT conditions for the given primal problem
>$$
>\begin{align}
>l_i &= 0, \quad i=1, \dots, r\\\\
>u_i^\star, -h_i(x^\star) &\ge 0, \quad i=1, \dots, m\\\\
>u_i^\star h_i(x^\star) &= 0, \quad i=1, \dots, m\\\\
>\nabla f(x^\star) + \sum_{i=1}^m \nabla h_i(x^\star) u^\star_i + \sum_{i=1}^r \nabla l_i(x^\star) v_i^\star &= 0.\\\\
>\end{align}
>$$

## Central path equations

Let's also examine the conditions for determining the optimality of barrier problems.

### Barrier problem

>$$
\begin{align}
    \mathop{\text{minimize}}_x &\quad f(x) + \tau \phi(x) \\\\
    &\quad l_j(x) = 0, j = 1, \ldots, r  \\\\
\end{align}$$
>
>$$ \text{where } \phi(x) = - \sum_{i=1}^m \log \big( -h_i(x) \big).$$


By organizing the KKT conditions for barrier problems, we can derive the following optimality conditions. Note the differences in the inequality constraint and complementary slackness conditions compared to the KKT optimality conditions for primal problems examined earlier. (Reference: [15-03-01 Perturbed KKT conditions]({% multilang_post_url contents/chapter15/21-03-28-15_03_01_perturbed_kkt_conditions %}))

### Optimality conditions for barrier problem (and its dual)

>$$
\begin{align}
l_i &= 0, \quad i=1, \dots, r\\\\
u_i(t), -h_i(x^\star(t)) &\gt 0, \quad i=1, \dots, m\\\\
u_i(t) h_i(x^\star(t)) &= -\tau, \quad i=1, \dots, m\\\\
\nabla f(x^\star(t)) + \sum_{i=1}^m \nabla h_i(x^\star(t)) u_i(t) + \sum_{i=1}^r \nabla l_i(x^\star(t)) \hat{v}_i^\star &= 0,\\\\
\end{align} \\\\
$$
>
>$$\text{where } \tau = \frac{1}{t}, u_i(t) = - \frac{1}{t h_i(x^\star(t))}, \quad \hat{v} = \frac{1}{t}v.$$

## Special case: linear programming

### Recall: Primal problem of LP in standard form
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad c^Tx \\\\
>    \text{subject to} &\quad Ax = b \\\\
>    &\quad x \ge 0
>\end{align}
>$$

### Recall: Dual problem of LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty \\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>    &\quad s \ge 0
>\end{align}
>$$

Linear programming has the nice property of always satisfying strong duality due to the refined Slater's condition, since the inequality constraints are affine. The optimality conditions for LP are as follows:

>$$
>\begin{align}
>A^T y^\star + s^\star &= c\\\\
>Ax^\star &= b\\\\
>X S \mathbb{1} &= 0\\\\
>x^\star, s^\star &\ge 0,\\\\
>\end{align}$$
> 
>$$text{where }X = Diag(x^\star), S = Diag(s^\star)$$

Note that $$X S \mathbb{1} = 0$$ is equivalent to $$Xs^\star=(x_1^\star s_1^\star, \dots, x_n^\star s_n^\star)=0$$. We use $$X, S$$ notation for convenience in algorithms that will be introduced later.

### Algorithms for linear programming

We introduce two representative methods for solving LP using optimality conditions.

1. Simplex: A method that maintains conditions 1, 2, and 3 while gradually satisfying condition 4.
2. Interior-point methods: A method that maintains condition 4 while gradually satisfying conditions 1, 2, and 3. This will be covered in the next chapter.

## Central path for linear programming

### Recall: Barrier problem for LP
>$$\begin{align}
    \mathop{\text{minimize}}_x &\quad c^Tx - \tau \sum_{i=1}^n \log(x_i)\\\\
    \text{subject to} &\quad Ax = b, \\\\
    \text{where}  &\quad \tau > 0
\end{align}$$


### Recall: Dual problem of Barrier problem for LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty + \tau \sum_{i=1}^n log(s_i)\\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>\end{align}
>$$

The optimality conditions for the barrier problem of LP are as follows:

>$$
\begin{align}
A^T y^\star + s^\star &= c\\\\
Ax^\star &= b\\\\
X S \mathbb{1} &= \tau \mathbb{1}\\\\
x^\star, s^\star &\gt 0,\\\\
\text{where} &\quad X = Diag(x^\star), S = Diag(s^\star)
\end{align}$$

Conditions 3 and 4 show differences from the KKT conditions of the primal LP.

### KKT: normals and Lagrange multipliers (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/kkt-normals_en.mp4"></video>
</div>

At the optimum, $$-\nabla f(x^*)$$ is a nonnegative combination of the normals of the active constraints, and inactive constraints get multiplier $$0$$.

### Try it yourself: KKT multipliers

<div class="opx-explainer" data-opx="kkt" data-lang="en"></div>
