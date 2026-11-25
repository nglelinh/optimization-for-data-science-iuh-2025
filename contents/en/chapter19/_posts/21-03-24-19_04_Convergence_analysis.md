---
layout: post
title: 19-04 Convergence analysis
chapter: '19'
order: 8
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

At first glance, proving **quadratic local convergence** for a nonsmooth function $$f = g + h$$ seems impossible—after all, classical Newton's quadratic proof expands $$\nabla f(x^\star) = 0$$ in a Taylor series, and $$\nabla h(x^\star)$$ does not even exist! Lee, Sun, and Saunders (2014) cracked this cleanly with one masterstroke: rewrite the optimality condition as a fixed point of the **scaled proximal operator** $$x^\star = \operatorname{prox}_H(x^\star - H^{-1}\nabla g(x^\star))$$, and use its *non-expansiveness* to peel $$h$$ completely out of the error bound!

## Background Knowledge Map: Anatomy of the Lee–Sun–Saunders Convergence Proof

- **Regularity Assumptions:** $$g$$ is $$m$$-strongly convex ($$mI \preceq \nabla^2 g(x) \preceq LI$$) with $$M$$-Lipschitz Hessian $$\|\nabla^2 g(x) - \nabla^2 g(y)\| \le M\|x - y\|$$, and $$\operatorname{prox}_H$$ is solved accurately.
- **Global Convergence via Composite Backtracking:** Because $$v^{(k)}$$ satisfies $$\Delta_k \le -v_k^T H_k v_k \le -m\|v_k\|_2^2$$, backtracking always terminates with a uniformly bounded step size $$t_k \ge \min(1, \beta m / L)$$, forcing $$\|v_k\| \to 0$$ and therefore global convergence $$x^k \to x^\star$$ from any starting point.
- **Non-Expansiveness Eliminates $$h$$:** Comparing $$x^{k+1} = \operatorname{prox}_{H_k}(x^k - H_k^{-1}\nabla g(x^k))$$ against the fixed point $$x^\star = \operatorname{prox}_{H_k}(x^\star - H_k^{-1}\nabla g(x^\star))$$ lets firm non-expansiveness in $$\|\cdot\|_{H_k}$$ cancel $$h$$ completely, leaving only the smooth Taylor remainder $$\|\nabla g(x^\star) - \nabla g(x^k) - H_k(x^\star - x^k)\| \le \frac{M}{2}\|x^k - x^\star\|^2$$!
- **Exact Local Quadratic Rate:** Combining the non-expansiveness bound with $$mI \preceq H_k$$ yields $$\|x^{k+1} - x^\star\|_2 \le \frac{M}{2m}\sqrt{\frac{L}{m}}\|x^k - x^\star\|_2^2$$ (and $$\frac{M}{2m}\|x^k - x^\star\|_2^2$$ in 1D), matching unconstrained Newton's method despite the nonsmooth kink!

### Step-by-Step Worked Example (Read Slowly): Verifying Local Quadratic Contraction Numerically

Return to $$f(x) = e^x - 4x + |x|$$ (exact optimum $$x^\star = \ln 3 \approx 1.0986123$$), starting inside the local quadratic basin at $$x^0 = 1.0$$ (error $$e_0 = |x^0 - x^\star| \approx 0.0986123$$).

1. **Compute Iteration 1 with unit step $$t = 1$$:**
   - $$g'(1.0) = e - 4 \approx -1.2817182$$, $$H_0 = g''(1.0) = e \approx 2.7182818$$.
   - Solving $$-1.2817182 + e v_0 + 1 = 0 \implies v_0 = \frac{3 - e}{e} \approx +0.1036383$$.
   - $$x^1 = 1.0 + 0.1036383 = 1.1036383$$.
   - New error: $$e_1 = |x^1 - x^\star| \approx 0.0050260$$! (Error shrank by almost $$20\times$$ in one step!)
2. **Compute Iteration 2 with unit step $$t = 1$$:**
   - $$g'(1.1036383) = e^{1.1036383} - 4 \approx 3.015116 - 4 = -0.984884$$, $$H_1 = 3.015116$$.
   - $$v_1 = \frac{3 - 3.015116}{3.015116} \approx -0.0050134 \implies x^2 = 1.0986249$$.
   - New error: $$e_2 = |x^2 - x^\star| \approx 0.0000126$$! (Error shrank by $$400\times$$—doubling the number of accurate decimal digits!)
3. **Check against the theoretical bound $$e_{k+1} \le \frac{M}{2m} e_k^2$$:**
   On $$[1.0, 1.11]$$, $$m = e^{1.0} \approx 2.718$$ and $$M = \sup g'''(x) = e^{1.11} \approx 3.034$$, so $$\frac{M}{2m} \approx 0.558$$.
   - Predicted bound for $$e_1$$: $$0.558 \times (0.0986123)^2 \approx 0.00543 \ge 0.00503 = e_1$$ $$\checkmark$$.
   - Predicted bound for $$e_2$$: $$0.558 \times (0.005026)^2 \approx 0.0000141 \ge 0.0000126 = e_2$$ $$\checkmark$$.

To analyze the convergence of the Proximal Newton method, we will follow the proof from Lee (2014) [1].

[1] J. Lee and Y. Sun and M. Saunders (2014), Proximal Newton-type methods for minimizing

To prove convergence, we make the following assumptions:

* $$f = g + h$$, $$g$$ and $$h$$ are convex and $$g$$ is twice differentiable (smooth)
* $$mI \preceq \nabla^2 g(x) \preceq LI$$.
* $$\nabla^2 g(x)$$ is Lipschitz with constant $$M$$
* $$\text{prox}_H(\cdot)$$ can be computed exactly

The above three assumptions imply that the function is strictly convex, and assuming that $$\text{prox}_H(\cdot)$$ can be computed exactly is because this is not easy to achieve in practice.
 
## Convergence Theorem

> **Proximal Newton method** converges globally using backtracking line search.
> \begin{align}
\parallel x^{(k)} - x^{\star} \parallel_2 \le \frac{M}{2m} \parallel x^{(k-1)} - x^{\star} \parallel_2^2
\end{align}

This is called **local quadratic convergence**. After $$k \ge k_0$$, to satisfy $$f(x^{(k)}) - f^{\star} \le \epsilon$$, $$O(\log \log (1/\epsilon))$$ iterations are needed. However, each iteration uses a scaled prox.

## Proof sketch
To show **global convergence**, we can show that at any step, the backtracking exit condition for step size $$t$$ is satisfied as follows.

> \begin{align}
t \le \min \left\\{ 1, \frac{2m}{L} (1-\alpha) \right\\} \\\\
\end{align}

With this equation, we can show that when the global minimum is reached, the update direction converges to 0.

To show **local quadratic convergence**, after sufficiently many iterations, the pure Newton step $$t=1$$ satisfies the backtracking exit conditions, and the following equation holds.

> $$
> \begin{align}
> \parallel x^{+} - x^{\star} \parallel_2 & \le \frac{1}{\sqrt(m)} \parallel x^{+} - x^{\star} \parallel_H \\\\
> & =  \frac{1}{\sqrt(m)} \parallel \text{prox}_H(x - H^{-1} \nabla g(x) )  - \text{prox}_H(x^{\star} - H^{-1} \nabla g(x^{\star}) )  \parallel_H \\\\
> & \le \frac{M}{2m} \parallel x - x^{\star} \parallel_2^2 \\\\
> \end{align}
> $$

Summarizing this, we get the following:

> \begin{align}
\parallel x^{+} - x^{\star} \parallel_2 \ \le \ \frac{1}{\sqrt(m)} \parallel x^{+} - x^{\star} \parallel_H \  \le \ \frac{M}{2m} \parallel x - x^{\star} \parallel_2^2
\end{align}

* The first inequality holds due to the lowest eigenvalue bound, and the equality holds by the fact that $$\text{prox}_H(\cdot)$$ becomes the identity at the definition of $$x^+$$ and global minimum $$x^{\star}$$.

* The second inequality holds due to the nonexpansiveness of the proximal operator, the Lipschitz assumption, and the largest eigenvalue bound.
