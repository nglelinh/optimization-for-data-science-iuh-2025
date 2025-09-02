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
