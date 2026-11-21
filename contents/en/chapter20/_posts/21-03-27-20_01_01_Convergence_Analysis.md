---
layout: post
title: "20-01-01 Convergence Analysis"
chapter: '20'
order: 3
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

## Lipschitz gradients and strong convexity
Suppose $$f$$ is a closed convex function. Then the following equivalence holds.
>\begin{equation}
\text{$$f$$ is strongly convex with parameter $$d$$ $$\Longleftrightarrow \nabla f^{\ast}$$ is Lipschitz with parameter $$1/d$$.} 
\end{equation}

### Proof ###
We prove the direction "$$\Rightarrow$$". If $$g$$ is strongly convex with parameter $$d$$ and minimized at $$x$$, then
>\begin{equation}
g(y) \geq g(x) + \frac{d}{2}\lVert y-x \rVert_2^2, \text{ for all } y
\end{equation}

Let $$x_u = \nabla f^{\ast}(u)$$ be the minimizer of $$g(x) = f(x) − u^T x$$, and let $$x_v = \nabla f^{\ast}(v)$$ be the minimizer of $$g(x) = f(x) − v^T x$$.

Then the inequality above gives the following two inequalities.
> $$
> \begin{alignat}{1}
> f(x_v) - u^Tx_v \geq f(x_u) - u^T x_u + \frac{d}{2} \lVert x_u - x_v \rVert_2^2 \\
> f(x_u) - v^Tx_u \geq f(x_v) - v^T x_v + \frac{d}{2} \lVert x_u - x_v \rVert_2^2 
> \end{alignat}
> $$

Adding the two inequalities gives
>\begin{equation}
f(x_v) - u^Tx_v + f(x_u) - v^Tx_u \geq f(x_u) - u^T x_u +  f(x_v) - v^T x_v + d \lVert x_u - x_v \rVert_2^2.  
\end{equation}

Rearranging and applying the Cauchy–Schwarz inequality, we get
> $$
> \begin{align}
> d \lVert x_u - x_v \rVert_2^2 & \leq - u^Tx_v - v^Tx_u + u^T x_u + v^T x_v \\\\
> & = (u-v)^T(x_u - x_v) \\\\
> & \leq \lVert u-v \rVert_2 \lVert x_u - x_v \rVert_2
> \end{align}
> $$

Therefore

> $$\lVert x_u - x_v \rVert_2 \leq \frac{1}{d} \lVert u-v \rVert_2$$

which shows that $$\nabla f^{\ast}$$ is Lipschitz with parameter $$1/d$$.

## Convergence guarantees
Combining this result with the analysis of gradient descent, we obtain the following convergence guarantees for the dual objective.

* If $$f$$ is strongly convex with parameter $$d$$, then dual gradient ascent with step sizes $$t_k=d$$ ($$k=1,2,3, \dots$$) converges at the rate $$O(1/\epsilon)$$.
* If $$f$$ is strongly convex with parameter $$d$$ and $$\nabla f$$ is Lipschitz with parameter $$L$$, then dual gradient ascent with step sizes $$t_k=2/(1/d + 1/L)$$ ($$k=1,2,3, \dots$$) converges at the rate $$O(\log(1/\epsilon))$$ (linear convergence).

(These step sizes assume $$\lVert A \rVert_2 \le 1$$; in general the dual gradient is Lipschitz with constant $$\lVert A \rVert_2^2 / d$$, so the step sizes should be scaled by $$1/\lVert A \rVert_2^2$$.)
