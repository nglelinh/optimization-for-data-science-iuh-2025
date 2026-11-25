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

One of the deepest dualities in convex analysis links two seemingly unrelated geometric properties: **curvature** (strong convexity) in the primal space and **smoothness** (Lipschitz gradients) in the dual space! The sharper the bowl of $$f$$ (parameter $$d$$), the gentler and smoother the landscape of its conjugate $$f^\ast$$ (Lipschitz constant $$1/d$$). That single equivalence tells you immediately what step size $$t$$ guarantees monotonic ascent for dual gradient descent—and explains why losing strong convexity makes dual ascent oscillate.

## Background Knowledge Map: The Strong Convexity $$\Longleftrightarrow$$ Smoothness Duality

- **Fenchel Conjugate Duality Theorem:** A closed convex function $$f$$ is $$d$$-strongly convex *if and only if* its conjugate $$f^\ast$$ has a $$(1/d)$$-Lipschitz continuous gradient: $$\|\nabla f^\ast(u) - \nabla f^\ast(v)\|_2 \le \frac{1}{d}\|u - v\|_2$$.
- **Dual Smoothness Constant Under Linear Maps:** For $$g(u) = -f^\ast(-A^T u) - b^T u$$, applying the chain rule gives $$\|\nabla g(u) - \nabla g(v)\|_2 \le \frac{\|A\|_2^2}{d}\|u - v\|_2$$, so the dual objective is $$L_g$$-smooth with $$L_g = \sigma_{\max}^2(A)/d$$.
- **Exact Safe Step Size for Dual Ascent:** Standard smooth gradient ascent theory immediately gives the constant step-size rule $$t \le \frac{1}{L_g} = \frac{d}{\|A\|_2^2}$$, guaranteeing $$O(1/k)$$ dual suboptimality (and linear convergence if $$f$$ is also smooth!).
- **What Breaks When $$d = 0$$:** If $$f$$ is not strongly convex ($$d = 0$$), $$L_g = \infty$$—the dual has sharp ridges where constant-step dual ascent can bounce forever, directly motivating the Augmented Lagrangian in Section 20-03.

### Step-by-Step Worked Example (Read Slowly): Computing the Exact Dual Step Size Bound

Consider $$\min_x f(x) = \frac{1}{2}(4x_1^2 + 2x_2^2)$$ subject to $$2x_1 + x_2 = 5$$.

1. **Find the primal strong convexity constant $$d$$:**
   $$\nabla^2 f(x) = \begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix} \implies d = \lambda_{\min}(\nabla^2 f) = 2.$$
2. **Compute the operator norm squared $$\|A\|_2^2$$:**
   Here $$A = [2, 1]$$, so $$\|A\|_2^2 = 2^2 + 1^2 = 5$$.
3. **Predict the dual smoothness constant $$L_g$$ from the theorem:**
   $$L_g \le \frac{\|A\|_2^2}{d} = \frac{5}{2} = 2.5 \implies \text{guaranteed safe step size } t \le \frac{1}{L_g} = 0.4.$$
4. **Verify directly by computing the exact dual Hessian!**
   Minimizing $$L(x, u) = 2x_1^2 + x_2^2 + u(2x_1 + x_2 - 5)$$ gives $$x_1(u) = -\frac{u}{2}$$ and $$x_2(u) = -\frac{u}{2}$$.
   Substituting back gives $$g(u) = -\frac{3}{4}u^2 - 5u$$, whose exact gradient is $$g'(u) = -\frac{3}{2}u - 5$$—Lipschitz with exact constant $$L_{\text{exact}} = 1.5 \le 2.5 = \frac{\|A\|_2^2}{d}$$!
   Check step size $$t = 0.4$$: $$u^{k+1} = u^k + 0.4(-1.5 u^k - 5) = 0.4 u^k - 2$$, which contracts the dual error by $$60\%$$ at *every* iteration!

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
