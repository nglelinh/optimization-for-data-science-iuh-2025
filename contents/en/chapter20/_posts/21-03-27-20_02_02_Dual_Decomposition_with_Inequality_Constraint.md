---
layout: post
title: "20-02-02 Dual Decomposition with Inequality Constraint"
chapter: '20'
order: 6
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

Real-world resource constraints are rarely exact equalities—bandwidth on a network link cannot *exceed* capacity $$b$$ ($$\sum_i A_i x_i \le b$$), and a shared warehouse budget cannot be overspent, though leaving unused capacity is perfectly legal! Switching from $$=$$ to $$\le$$ introduces one crucial economic rule: **prices cannot be negative** ($$u \ge 0$$). If a resource is under-utilized, its price drops to zero and stops there, turning dual decomposition into **projected dual ascent**.

## Background Knowledge Map: Inequality Pricing & Complementary Slackness

- **Nonnegative Dual Prices ($$u \ge 0$$):** For $$\sum_{i=1}^B A_i x_i \le b$$, dual feasibility requires $$u \ge 0$$, so every dual update projects onto the nonnegative orthant: $$u^{(k)} = \big(u^{(k-1)} + t_k(\sum_i A_i x_i^{(k)} - b)\big)_+$$.
- **Economic Meaning of Projection $$(\cdot)_+$$:** When total demand exceeds capacity ($$\sum_i A_i x_i > b$$), the price rises to ration the resource; when demand is below capacity ($$\sum_i A_i x_i < b$$), the price falls—clamping at $$0$$ if the resource is genuinely abundant!
- **Complementary Slackness at Equilibrium:** At convergence, either the resource is saturated ($$\sum_i A_i x_i^\star = b, u^\star \ge 0$$) or it has slack and becomes free ($$\sum_i A_i x_i^\star < b \implies u^\star = 0$$).
- **Network Utility Maximization (NUM):** This exact projected dual decomposition algorithm underlies TCP congestion control—routers update link congestion prices $$u_\ell = (u_\ell + t(\text{flow}_\ell - c_\ell))_+$$ while users independently adjust sending rates $$x_i$$!

### Step-by-Step Worked Example (Read Slowly): Congestion Pricing Across Two Links

Two users maximize utility (equivalently minimize cost) $$\min_{x \ge 0} \frac{1}{2}(x_1 - 5)^2 + \frac{1}{2}(x_2 - 3)^2$$ subject to a shared link capacity $$x_1 + x_2 \le 6$$ (and a second abundant link $$x_1 \le 10$$).

1. **Write the independent user responses for link prices $$u = (u_1, u_2)^T \ge 0$$:**
   - User 1: $$\min_{x_1 \ge 0} \frac{1}{2}(x_1 - 5)^2 + (u_1 + u_2)x_1 \implies x_1(u) = (5 - u_1 - u_2)_+$$.
   - User 2: $$\min_{x_2 \ge 0} \frac{1}{2}(x_2 - 3)^2 + u_1 x_2 \implies x_2(u) = (3 - u_1)_+$$.
2. **Iteration 1 starting from $$u^0 = (0, 0.5)^T$$ with step size $$t = 0.5$$:**
   - User rates: $$x_1^1 = 5 - 0.5 = 4.5$$, $$x_2^1 = 3 - 0 = 3.0$$.
   - Link 1 residual (congested!): $$4.5 + 3.0 - 6 = +1.5 \implies u_1^1 = (0 + 0.5(1.5))_+ = 0.75$$.
   - Link 2 residual (abundant!): $$4.5 - 10 = -5.5 \implies u_2^1 = (0.5 + 0.5(-5.5))_+ = (-2.25)_+ = 0$$!
3. **Iteration 2 at $$u^1 = (0.75, 0)^T$$:**
   - User rates: $$x_1^2 = 4.25, \; x_2^2 = 2.25$$ (total $$6.5$$, excess $$+0.5$$).
   - Prices: $$u_1^2 = 0.75 + 0.5(0.5) = 1.0$$, $$u_2^2 = 0$$.
4. **Verify exact equilibrium at $$u^\star = (1, 0)^T$$:**
   $$x_1^\star = 4, \; x_2^\star = 2$$, Link 1 is saturated ($$4 + 2 = 6, u_1^\star = 1 > 0$$) and Link 2 is free ($$4 < 10, u_2^\star = 0$$)—exact complementary slackness!

Consider the following problem. The difference from the previous one is that the constraint is an inequality.
> $$
> \begin{equation}
> \min_x \sum_{i=1}^B f_i(x_i) \quad \text{subject to} \quad \sum_{i=1}^B A_i x_i \leq b
> \end{equation}
> $$

## Dual decomposition (projected subgradient method) 
For this problem the dual variable must always be nonnegative, i.e. $$u \geq 0$$. Therefore, when computing the next value of $$u$$, we project it onto the nonnegative orthant.

> $$
> \begin{alignat}{1}
> x_i^{(k)} & \in \arg \min_{x_i} f_i(x_i) + (u^{(k-1)})^T A_i x_i, \quad i=1,\dots,B  \\
> u^{(k)}   & = \left( u^{(k-1)} + t_k \left(\sum_{i=1}^B A_i x_i^{(k)} - b \right) \right)_+
> \end{alignat}
> $$

Here $$u_{+}$$ denotes the nonnegative part of $$u$$, i.e. $$(u_+)_i = \max \left\{0,u_i \right\}, i=1,\dots,m$$.
These steps are repeated for $$k=1,2,3,\dots$$

#### Price coordination interpretation
In general, dual decomposition problems can be interpreted from the viewpoint of price coordination as follows. (Vandenberghe)
> * There are $$B$$ independent units, and each unit decides its own decision variable $$x_i$$.
> * Each constraint represents a limit on a resource shared by the $$B$$ units, and the dual variable $$u_j$$ is the price of resource $$j$$.
> * The dual variables are updated as
 \begin{equation}
 u_j^{+} = (u_j - t s_j)_{+}, \quad  j=1,\dots,m
 \end{equation}
>
> $$\quad$$ where $$s=b-\sum_{i=1}^B A_ix_i$$ is the slack: \\
> $$\qquad$$ - if $$s_j < 0$$, resource $$j$$ is over-utilized, so the price $$u_j$$ is increased; \\
> $$\qquad$$ - if $$s_j > 0$$, resource $$j$$ is under-utilized, so the price $$u_j$$ is decreased; \\
> $$\qquad$$ - the price is never allowed to become negative.
