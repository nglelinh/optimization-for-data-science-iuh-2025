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

You now have all the pieces of the engine—perturbed KKT residuals, the coupled Newton direction, and the surrogate duality gap—so it is time to assemble the complete **Primal-Dual Interior-Point Algorithm**. The subtle part is not computing $$(\Delta x, \Delta u, \Delta v)$$, but choosing the step length $$\theta_k$$: step too aggressively and a multiplier or slack crosses zero, shattering the interior invariant; step too timidly and convergence stalls. Backtracking on the residual norm $$\|r_\tau\|_2$$ with a fraction-to-the-boundary cap threads that needle cleanly.

## Background Knowledge Map: Orchestrating the Primal-Dual Loop

- **Adaptive Target Reduction ($$\tau = \sigma \eta / m$$):** Rather than guessing a fixed schedule for $$\tau$$, the algorithm measures the current average complementarity $$\eta / m$$ and aims for a fraction $$\sigma \in (0, 1)$$ of it (typically $$\sigma \in [0.1, 0.5]$$), balancing aggressive gap reduction against staying near the central path.
- **Fraction-to-the-Boundary Step Cap ($$\theta_{\max}$$):** Before backtracking begins, we compute the largest step $$\theta_{\max} = \min\!\big(1, \; \min_{\Delta u_i < 0}(-u_i/\Delta u_i)\big)$$ that keeps $$u + \theta \Delta u > 0$$, and shrink by $$0.99$$ so iterates never touch the boundary $$u_i = 0$$.
- **Residual-Norm Backtracking Line Search:** Because the objective $$f(x)$$ can actually *increase* while an infeasible iterate moves toward feasibility, line search cannot monitor $$f(x)$$. Instead, it enforces strict interiority $$h(x^+) < 0$$ and sufficient decrease of the total residual norm: $$\|r_\tau(z + \theta \Delta z)\|_2 \le (1 - \alpha \theta)\|r_\tau(z)\|_2$$.
- **Dual-Criterion Termination:** The loop halts only when *both* the surrogate gap $$\eta \le \epsilon_{\text{feas}}$$ and the combined primal-dual feasibility residual $$\sqrt{\|r_{\text{prim}}\|_2^2 + \|r_{\text{dual}}\|_2^2} \le \epsilon$$ meet tolerance.

### Step-by-Step Worked Example (Read Slowly): One Full Iteration with Backtracking

Consider $$\min x_1 + 2x_2$$ subject to $$x_1 + x_2 = 2$$ and $$x_1, x_2 \ge 0$$ (exact optimum $$x^\star = (2, 0), u^\star = (0, 1), v^\star = -1$$). Start at $$x^0 = (1, 1)^T, u^0 = (1, 1)^T, v^0 = -1$$ with $$\sigma = 0.5$$ and backtracking parameter $$\alpha = 0.1$$.

1. **Compute the surrogate gap and target $$\tau$$:**
   $$\eta_0 = x_1^0 u_1^0 + x_2^0 u_2^0 = 1 + 1 = 2 \implies \tau_0 = \frac{2}{2} = 1, \quad \tau = \sigma \tau_0 = 0.5.$$
2. **Evaluate the residuals at $$z^0$$:**
   - $$r_{\text{prim}}^0 = 1 + 1 - 2 = 0$$.
   - $$r_{\text{dual}}^0 = \begin{bmatrix}1\\2\end{bmatrix} - \begin{bmatrix}1\\1\end{bmatrix} + (-1)\begin{bmatrix}1\\1\end{bmatrix} = \begin{bmatrix}-1\\0\end{bmatrix}$$.
   - $$r_{\text{cent}}^0 = \begin{bmatrix}-1 + 0.5 \\ -1 + 0.5\end{bmatrix} = \begin{bmatrix}-0.5 \\ -0.5\end{bmatrix}$$.
   - Residual norm: $$\|r_\tau(z^0)\|_2 = \sqrt{1^2 + 0^2 + (-0.5)^2 + (-0.5)^2 + 0^2} = \sqrt{1.5} \approx 1.2247$$.
3. **Solve the Newton system for $$(\Delta x, \Delta u, \Delta v)$$:**
   From $$r_{\text{prim}}$$: $$\Delta x_1 + \Delta x_2 = 0 \implies \Delta x_2 = -\Delta x_1$$.
   From $$r_{\text{dual}}$$: $$-\Delta u_1 + \Delta v = 1$$ and $$-\Delta u_2 + \Delta v = 0 \implies \Delta u_1 = \Delta v - 1, \; \Delta u_2 = \Delta v$$.
   From $$r_{\text{cent}}$$: $$-\Delta x_1 - \Delta u_1 = 0.5$$ and $$-\Delta x_2 - \Delta u_2 = 0.5$$. Adding these two equations eliminates $$\Delta x_1 + \Delta x_2 = 0$$, giving:
   $$-(\Delta u_1 + \Delta u_2) = 1 \implies -(2\Delta v - 1) = 1 \implies \Delta v = 0.$$
   Hence $$\Delta u = (-1, 0)^T$$ and $$\Delta x = (0.5, -0.5)^T$$.
4. **Compute the boundary step cap $$\theta_{\max}$$:**
   Since $$\Delta u_1 = -1 < 0$$, $$u_1 + \theta \Delta u_1 > 0 \implies \theta < 1$$. Since $$\Delta x_2 = -0.5 < 0$$, $$x_2 + \theta \Delta x_2 > 0 \implies \theta < 2$$. Taking $$0.99 \theta_{\max}$$ gives $$\theta = 0.99$$ (for clean hand arithmetic, test $$\theta = 0.8$$).
5. **Verify the backtracking decrease condition at $$\theta = 0.8$$:**
   $$x^1 = (1.4, 0.6)^T, \quad u^1 = (0.2, 1.0)^T, \quad v^1 = -1.$$
   - $$r_{\text{prim}}^1 = 0$$, $$r_{\text{dual}}^1 = (1 - 0.8) r_{\text{dual}}^0 = (-0.2, 0)^T$$.
   - $$r_{\text{cent}}^1 = \begin{bmatrix}-(1.4)(0.2) + 0.5 \\ -(0.6)(1.0) + 0.5\end{bmatrix} = \begin{bmatrix}0.22 \\ -0.10\end{bmatrix}$$.
   - $$\|r_\tau(z^1)\|_2 = \sqrt{0.04 + 0.0484 + 0.01} = \sqrt{0.0984} \approx 0.3137 \le (1 - 0.1 \times 0.8)(1.2247) = 1.1268$$.
   The step is accepted immediately! Surrogate gap plunged from $$2.0$$ to $$1.4(0.2) + 0.6(1.0) = 0.88$$.

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
