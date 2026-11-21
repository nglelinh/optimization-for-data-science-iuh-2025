---
layout: post
title: "17-02-03 Primal-Dual Algorithm"
chapter: '17'
order: 6
owner: Minjoo Lee
categories:
- chapter17
lang: en
---

To define the primal-dual algorithm, we first define $$\tau(x,u)$$ as follows.
> $$\tau(x,u) := -\frac{h(x)^Tu}{m} \quad \text{with} \quad h (x) \le 0, u \ge 0$$

Note that the $$t$$ and $$\mu$$ of the barrier method are rewritten as $$\tau$$ and $$\sigma$$ in the primal-dual algorithm.
> $$\tau = \frac{1}{t}, \quad \sigma = \frac{1}{\mu}$$

## Primal-Dual Algorithm 
The primal-dual algorithm is as follows.
> 1. Choose $$\sigma \in (0,1)$$.<br>
> 2. Choose $$(x^0,u^0,v^0)$$ with $$h(x^0) < 0$$ and $$u^0 > 0$$.<br>
> 3. Repeat the following steps ($$k = 0,1,... $$):<br>
> $$\quad$$ * Compute the Newton step:<br>
> $$\qquad \quad (x,u,v) = (x^k,u^k,v^k)$$ <br>
> $$\qquad \quad$$ compute $$\tau := \sigma \tau(x^k,u^k)$$<br>
> $$\qquad \quad$$ compute $$(\Delta x,\Delta u,\Delta v)$$ for this $$\tau$$<br>
> $$\quad$$ * Choose the step length $$\theta_k$$ by backtracking.<br>
> $$\quad$$ * Primal-dual update:<br>
> $$\qquad \quad (x^{k+1},u^{k+1},v^{k+1}) := (x^k,u^k,v^k) + \theta_k(\Delta x,\Delta u,\Delta v)$$<br>
> 4. Stop when $$-h(x^{k+1})^Tu \le \epsilon$$ and $$(\parallel r_{prim} \parallel^2_2 + \parallel r_{dual} \parallel^2_2)^{1/2} \le \epsilon $$.<br>

At each step the algorithm takes a Newton step to compute $$(\Delta x,\Delta u,\Delta v)$$ and then performs the primal-dual update to obtain $$(x^{k+1},u^{k+1},v^{k+1})$$. The step length $$\theta_k$$ is chosen by backtracking line search so that the primal-dual variables stay feasible. The algorithm stops when the surrogate duality gap and the primal and dual residuals are smaller than $$\epsilon$$.


## Backtracking line search
Since the primal-dual algorithm takes only one Newton step per iteration, the step should be regarded as giving a direction toward the solution rather than an exact solution. We therefore need to choose a suitable step length so that, while moving in that direction, the iterate stays inside the feasible set.

That is, at each step of the algorithm we find $$\theta$$ and update the primal-dual variables.

> $$x^+ = x + \theta \Delta x, \quad  u^+ = u + \theta \Delta u, \quad v^+ = v + \theta \Delta v$$

This process has two main goals.

* Maintain $$h(x) < 0, u > 0$$.
* Decrease $$\parallel r(x,u,v) \parallel$$.

For this we use a **multi-stage backtracking line search**.

#### Stage 1: dual feasibility $$u \gt 0$$
We start with the largest step $$\theta_{max} \le 1$$ satisfying $$u + \theta \Delta u \ge 0$$.

> $$\theta_{\max} = \min \Biggl\{1,\  \min \Bigl\{ -\frac{u_i}{\Delta u_i} : \Delta u_i < 0 \Bigr\} \Biggr\}$$

This is derived as follows.

> $$\begin{align}
&u + \theta \Delta u && \ge 0  \\\\
\Leftrightarrow \quad &u && \ge -\theta \Delta u \\\\
\Leftrightarrow \quad &- u/\Delta u && \ge \theta \quad  \text{ for the components with }\Delta u \lt 0  \\\\
\end{align}$$

This step makes $$u$$ feasible.

#### Stage 2: primal feasibility $$h(x) \lt 0$$
Next, choose parameters $$\alpha, \beta \in (0,1)$$, set $$\theta = 0.99\theta_{max}$$, and then do the following.

* Update $$\theta = \beta\theta$$ until $$h_i(x^+) < 0, i = 1,...,m$$.

This step makes $$x$$ feasible.

#### Stage 3: reduce $$\parallel r(x,u,v) \parallel$$
* Update $$\theta = \beta \theta$$ until $$\| r(x^+,u^+,v^+) \| \le (1-\alpha \theta) \| r(x,u,v) \|$$.

The update in Stage 3 is the same as in the standard backtracking line search algorithm.

The right-hand side of the condition can be derived as follows. First, from Newton's method we have
> $$\begin{align}
\Delta w = (\Delta x, \Delta u, \Delta v) &\approx -r^{\prime}(w)^{-1} r(w) \\\\
\Leftrightarrow r(w)  &\approx  -r^{\prime}(w) \Delta w \\\\
\end{align}$$

Since $$r^{\prime}(w) \Delta w \approx -r(w)$$, substituting this into the first-order Taylor approximation gives
> $$\begin{align}
r(w + \theta \Delta w) & \approx r(w) +  r^{\prime}(w) (\theta \Delta w) \\\\
&\approx (1-\theta) r(w) \\\\
\end{align}$$

Consequently, $$r(w + \alpha \theta \Delta w) \approx (1-\alpha  \theta) r(w)$$.
