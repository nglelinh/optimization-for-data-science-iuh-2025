---
layout: post
title: 17-02-03 Primal-Dual Algorithm
chapter: '17'
order: 6
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---
To define the Primal-Dual algorithm, let's first define $$\tau(x,u)$$ as follows
> $$\tau(x,u) := -\frac{h(x)^Tu}{m} \quad \text{with} \quad h (x) \le 0, u \ge 0$$

For reference, $$t$$ and $$\mu$$ in the Barrier method are redefined and denoted as $$\tau$$ and $$\sigma$$ in the Primal-Dual algorithm.
> $$\tau = \frac{1}{t}, \quad \sigma = \frac{1}{\mu}$$

## Primal-Dual Algorithm 
The Primal-Dual algorithm is as follows.
> 1. Choose $$\sigma$$ ($$\sigma ∈ (0,1)$$)<br>
> 2. Choose $$(x^0,u^0,v^0)$$ $$(h(x^0) < 0$$. $$u^0 > 0$$)<br>
> 3. Repeat the following steps ($$k = 0,1,... $$)<br>
> $$\quad$$ * Calculate Newton step :<br>
> $$\qquad \quad (x,u,v) = (x^k,u^k,v^k)$$ <br>
> $$\qquad \quad \tau := \sigma \tau(x^k,u^k)$$ 계산<br>
> $$\qquad \quad \tau$$에 대해 $$(\Delta x,\Delta u,\Delta v)$$ 계산<br>
> $$\quad$$ * Select step length $$θ_k$$ with Backtracking<br>
> $$\quad$$ * Primal-Dual update :<br>
> $$\qquad \quad (x^{k+1},u^{k+1},v^{k+1}) := (x^k,u^k,v^k) + \theta_k(\Delta x,\Delta u,\Delta v)$$<br>
> 4. Termination condition : Stop if the conditions $$-h(x^{k+1})^Tu \le \epsilon$$ and $$(\parallel r_{prim} \parallel^2_2 + \parallel r_{dual} \parallel^2_2)^{1/2} \le \epsilon $$ are satisfied <br>

The algorithm calculates $$(\Delta x,\Delta u,\Delta v)$$ by executing Newton step at each stage and obtains $$(x^{k+1},u^{k+1},v^{k+1})$$ by performing Primal-Dual updates. However, $$\theta_k$$ is selected through Backtracking line search so that the Primal-Dual variables become feasible. The algorithm terminates when the surrogate duality gap and primal and dual residuals become smaller than $$\epsilon$$.


## Backtracking line search
Since the Primal-Dual algorithm executes Newton step only once, it can be viewed as finding the direction of the solution rather than finding the exact solution. Therefore, an appropriate step length must be found so that moving in that direction can enter the feasible set.

That is, at each step of the algorithm, $$θ$$ is obtained to update the primal-dual variables.

> $$x^+ = x + θ\Delta x, \quad  u^+ = u + θ\Delta u, \quad v^+ = v + θ\Delta v$$

This process has two main objectives.

* Maintaining the condition $$h(x) < 0, u > 0$$
* Decreasing $$\parallel r(x,u,v) \parallel$$

For this purpose, **multi-stage backtracking line search** is used.

### Stage 1: dual feasibility $$u \gt 0$$
Initially, we start with the largest step $$\theta_{max} \leq 1$$ that satisfies $$u + \theta \Delta u \geq 0$$. 

> $$\theta_{\max} = \min \Biggl\{1,\  \min \Bigl\{ −\frac{u_i}{\Delta u_i} : ∆u_i < 0 \Bigr\} \Biggr\}$$

The above equation is derived as follows.

> $$\begin{align}
&u + \theta \Delta u && \ge 0  \\\\
\Leftrightarrow \quad &u && \ge -\theta \Delta u \\\\
\Leftrightarrow \quad &- u/\Delta u && \ge \theta \quad  \text{ such that }-\Delta u \gt 0  \\\\
\end{align}$$

This is the process of making $$u$$ feasible.

### Stage 2: primal feasibility $$h(x) \lt 0$$
Next, with parameters $$\alpha, \beta \in (0,1)$$ and $$\theta$$ set to $$0.99\theta_{max}$$, the following update is performed.

* Update $$\theta = \beta\theta$$ until $$h_i(x^+) < 0, i = 1,...m$$ is satisfied <br>

This is the process of making $$x$$ feasible.

### Stage 3 : reduce $$\parallel r(x,u,v) \parallel$$
* Update $$\theta = \beta \theta$$ until $$\| r(x^+,u^+,v^+) \| \leq (1−\alpha \theta) \| r(x,u,v) \|$$ is satisfied 

The update equation in Stage 3 is the same as the existing backtracking line search algorithm.

The right-hand side of the above equation can be derived as follows. First, we obtain the following result from Newton's method.
> $$\begin{align}
\Delta w = (\Delta x, \Delta u, \Delta v) &\approx -r^{'}(w)^{-1} r(w) \\\\
\Leftrightarrow r(w)  &\approx  -r^{'}(w) \Delta w \\\\
\end{align}$$

Since $$r^{'}(w) \Delta w \approx -r(w)$$ in the above equation, we substitute this into the first-order Taylor approximation below.
> $$\begin{align}
r(w + \theta \Delta w) & \approx r(w) +  r^{'}(w) (\theta \Delta w) \\\\
&\approx (1-\theta) r(w) \\\\
\end{align}$$

As a result, we get $$r(w + \alpha \theta \Delta w) \approx (1-\alpha  \theta) r(w)$$.
