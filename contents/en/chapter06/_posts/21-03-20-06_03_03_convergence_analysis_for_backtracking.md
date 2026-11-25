---
layout: post
title: 06-03-03 Convergence analysis for backtracking
chapter: '06'
order: 12
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
lesson_type: required
---

You might worry that replacing a known fixed step size $$t = 1/L$$ with Armijo backtracking could wreck the $$O(1/k)$$ convergence theorem—after all, backtracking doesn't even know $$L$$! Remarkably, the convergence rate stays **exactly $$O(1/k)$$**, paying at most a tiny constant factor $$1/\beta$$ because backtracking is mathematically guaranteed never to shrink the step size below $$\min(1, \beta/L)$$.

## Background Knowledge Map: Why Backtracking Preserves the $$O(1/k)$$ Rate

1. **Lower Bound on Accepted Step Size $$t_k$$**: For an $$L$$-smooth function and $$\alpha \le \frac{1}{2}$$, any $$t \le 1/L$$ satisfies $$f(x - t\nabla f) \le f(x) - \frac{t}{2}\|\nabla f\|_2^2 \le f(x) - \alpha t\|\nabla f\|_2^2$$. Therefore, either the initial step $$t_0 = 1$$ is accepted immediately, or the last rejected step had $$t_{\mathrm{rej}} > 1/L$$, forcing the accepted step to satisfy $$t_k = \beta t_{\mathrm{rej}} > \beta / L$$.
2. **Unified Effective Step Size $$t_{\min}$$**: Defining $$t_{\min} = \min(1, \beta/L)$$, every single iteration satisfies $$f(x^{(i+1)}) \le f(x^{(i)}) - \frac{t_{\min}}{2}\|\nabla f(x^{(i)})\|_2^2$$ (for $$\alpha = 1/2$$, or with $$\alpha$$ in place of $$1/2$$ in general).
3. **Identical Telescoping Proof**: Plugging $$t_{\min}$$ into the exact same telescoping sum as fixed-step gradient descent yields
   $$f(x^{(k)}) - f^\star \le \frac{\|x^{(0)} - x^\star\|_2^2}{2 t_{\min} k} = \frac{\|x^{(0)} - x^\star\|_2^2}{2 \min(1, \beta/L)\, k}.$$
4. **Often Faster Than Theory Predicts**: Because backtracking adapts to *local* curvature rather than the global worst-case $$L$$, it routinely takes steps much larger than $$1/L$$ across flat regions, outperforming fixed-step GD in practice.

### Step-by-Step Worked Example (Read Slowly): Computing $$t_{\min}$$ and Backtracking Overhead

Suppose $$f$$ is convex with global Lipschitz constant $$L = 10$$ (unknown to the algorithm), and we run Armijo backtracking with $$t_0 = 1$$, $$\alpha = 0.5$$, and $$\beta = 0.5$$.

1. **Compute the theoretical floor $$t_{\min}$$**:
   $$t_{\min} = \min\!\left(1, \frac{\beta}{L}\right) = \min\!\left(1, \frac{0.5}{10}\right) = 0.05.$$
2. **Verify the sequence of candidate steps $$t = \beta^m$$**:
   $$t \in \{1,\; 0.5,\; 0.25,\; 0.125,\; 0.0625,\; \dots\}.$$
   Notice that $$t = 0.125 > 1/L = 0.1$$ might fail in the steepest region, but the very next shrink gives $$t = 0.0625 \le 0.1 = 1/L$$, which is **guaranteed** to pass Armijo!
3. **Count the worst-case evaluations per iteration**: Reaching $$0.0625 = 2^{-4}$$ takes at most $$4$$ shrinks ($$5$$ function evaluations total), regardless of dimension $$n$$.
4. **Compare the convergence constant against oracle fixed step $$t = 1/L = 0.1$$**:
   - Fixed $$t = 1/L$$: bound is $$\frac{\|x^{(0)} - x^\star\|^2}{0.2 k}$$.
   - Backtracking ($$t_{\min} = 0.05$$): bound is $$\frac{\|x^{(0)} - x^\star\|^2}{0.1 k}$$ — at most a $$2\times$$ constant factor without ever needing to know $$L = 10$$!

Suppose $$f$$ is convex and differentiable with $$dom(f) = \mathbb{R}^n$$, and $$\nabla f$$ is Lipschitz continuous with constant $$L > 0$$:
>$$ \| \nabla f(x) - \nabla f(y) \|_2 \le L \| x - y \|_2 $$ for any $$x, y$$

Reference: [[Wikipedia: Lipschitz continuity](https://en.wikipedia.org/wiki/Lipschitz_continuity)]

## Convergence Theorem
**Gradient descent** with backtracking line search satisfies:
> $$ \begin{align}
f(x^{(k)}) - f^* \le \frac{\| x^{(0)} - x^* \|_2^2}{2 t_{min} k}, \quad t_{min} = \min \{ 1, \beta/L \}
\end{align} $$

The convergence rate for backtracking line search is similar to that for fixed step size, with the step size $$t$$ replaced by $$t_{min}$$. If $$\beta$$ is not too small, the performance is comparable to fixed step size ($$\beta/L$$ vs. $$1/L$$).