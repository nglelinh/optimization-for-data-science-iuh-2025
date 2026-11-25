---
layout: post
title: '09-02 Convergence analysis'
chapter: '09'
order: 3
owner: Kyeongmin Woo
categories:
- chapter09
lang: en
---

How can an algorithm that minimizes a *nondifferentiable* objective $$f = g + h$$ achieve the exact same $$O(1/\varepsilon)$$ convergence rate as smooth gradient descent? The secret lies in a remarkable algebraic disguise: by defining the **generalized gradient** $$G_t(x) = \frac{1}{t}(x - \operatorname{prox}_{t h}(x - t\nabla g(x)))$$, every proximal gradient step looks formally identical to smooth gradient descent—and obeys the same sufficient-decrease inequality whenever $$t \le 1/L$$ or Armijo-style backtracking holds!

## Key ideas: Proving the $$O(1/\varepsilon)$$ Proximal Rate

- **Pillar 1 — $$L$$-Smoothness of $$g$$ (Quadratic Upper Bound):** Assuming $$\nabla g$$ is $$L$$-Lipschitz guarantees $$g(y) \le g(x) + \nabla g(x)^\top(y - x) + \frac{L}{2}\|y - x\|_2^2$$. Whenever $$t \le 1/L$$, the proximal subproblem majorizes $$f$$ globally, ensuring monotonic descent $$f(x^{(k)}) \le f(x^{(k-1)})$$.
- **Pillar 2 — The Generalized Gradient $$G_t(x)$$:** Rewriting $$x^+ = x - t G_t(x)$$ implies $$G_t(x) - \nabla g(x) \in \partial h(x^+)$$ by first-order optimality of $$\operatorname{prox}_{t h}$$. Consequently, $$G_t(x) = 0 \iff 0 \in \nabla g(x) + \partial h(x) = \partial f(x)$$.
- **Pillar 3 — Key Descent Inequality:** For $$t \le 1/L$$ and any $$z$$, $$f(x^+) \le f(z) + G_t(x)^\top(x - z) - \frac{t}{2}\|G_t(x)\|_2^2$$. Setting $$z = x$$ shows guaranteed descent of $$\frac{t}{2}\|G_t(x)\|_2^2$$; setting $$z = x^\star$$ telescopes $$\|x^{(k)} - x^\star\|_2^2$$ cleanly to yield $$f(x^{(k)}) - f^\star \le \frac{\|x^{(0)} - x^\star\|_2^2}{2 k t}$$.
- **Pillar 4 — Backtracking Line Search Without Knowing $$L$$:** When $$L$$ is unknown or expensive to compute (e.g., top singular value of a massive matrix), shrinking $$t \leftarrow \beta t$$ until $$g(x - t G_t(x)) \le g(x) - t\nabla g(x)^\top G_t(x) + \frac{t}{2}\|G_t(x)\|_2^2$$ preserves the exact $$O(1/k)$$ rate with effective step size $$\ge \min\{t_0, \beta/L\}$$.

### Worked example: Verifying the Generalized Gradient & Descent Bound

Take $$g(x) = 2x^2$$ (so $$\nabla g(x) = 4x$$, Lipschitz constant $$L = 4$$) and $$h(x) = |x|$$ on $$\mathbb{R}$$ (minimizer $$x^\star = 0, f^\star = 0$$). Start at $$x^{(0)} = 1$$ with step size $$t = 1/L = 0.25$$.

1. **Compute the proximal gradient step:**
   - Smooth step: $$u = x^{(0)} - t\nabla g(x^{(0)}) = 1 - 0.25(4) = 0$$.
   - Prox step (threshold $$t \cdot 1 = 0.25$$): $$x^{(1)} = S_{0.25}(0) = 0$$.
2. **Compute the generalized gradient $$G_t(x^{(0)})$$:**
   $$G_t(1) = \frac{x^{(0)} - x^{(1)}}{t} = \frac{1 - 0}{0.25} = 4.$$
3. **Check the sufficient-decrease inequality $$f(x^{(1)}) \le f(x^{(0)}) - \frac{t}{2}\|G_t(x^{(0)})\|_2^2$$:**
   - Left-hand side: $$f(x^{(1)}) = f(0) = 0$$.
   - Right-hand side: $$f(1) - \frac{0.25}{2}(4^2) = (2(1)^2 + |1|) - 0.125(16) = 3 - 2 = 1$$.
   - Indeed $$0 \le 1$$!
4. **Check the $$O(1/k)$$ theorem bound at $$k = 1$$:**
   $$\frac{\|x^{(0)} - x^\star\|_2^2}{2kt} = \frac{(1 - 0)^2}{2 \cdot 1 \cdot 0.25} = \frac{1}{0.5} = 2 \ge 0 = f(x^{(1)}) - f^\star.$$
   Notice also what happens if we *violate* $$t \le 1/L$$ by choosing $$t = 1 > 0.25$$: the backtracking test $$g(x^+) \le g(x) - t\nabla g(x)^\top G_t(x) + \frac{t}{2}\|G_t(x)\|_2^2$$ immediately triggers and shrinks $$t$$ back into the safe regime.

# Convergence analysis
In this section, we analyze the convergence of proximal gradient descent. 

## Convergence Analysis
For the objective function $$f(x) = g(x) + h(x)$$, we assume the following:

* $$g$$ is convex, differentiable, and **dom**$$(g) = \mathbb{R}^n$$, and $$\nabla g$$ is Lipschitz continuous ($$L > 0$$).
* $$h$$ is convex, and $$\text{prox}_{t}(x) = \underset{z} {\text{argmin}} \{ \parallel x - z \parallel_2^2/ (2t) + h(z) \}$$ needs to be computed.

### Convergence Theorem
> **Proximal gradient descent** satisfies the following equation for a fixed step size $$t \le 1/L$$: 
>\begin{align}
f(x^{(k)}) - f^{\*} \le  \frac{ \lVert x^{(0)} - x^{\*} \rVert^2_2 }{2tk}
\end{align}

Proximal gradient descent has a convergence rate of $$O(1/k)$$ or $$O(1/\epsilon)$$, which is the same performance as gradient descent. However, this performance is based on the number of iterations, not the number of operations. (The number of operations can vary depending on the function $$h$$.)

## Backtracking line search
The backtracking line search method of proximal gradient descent is similar to gradient descent but operates only on the smooth part $$g$$, not the function $$f$$. 

First, set the parameter to $$0 < \beta < 1$$ and start with $$t=1$$. In each iteration, reduce $$t$$ to $$t = \beta t$$ while satisfying the following condition, and update proximal gradient descent if the condition is not met.
> \begin{align}
g(x - tG_t(x)) > g(x) - t \nabla g(x)^T G_t(x) + \frac{t}{2} \parallel G_t(x) \parallel_2 ^2
\end{align}

This backtracking condition means that the value of the function $$g$$ at the next step location $$x - tG_t(x)$$ is greater than the value of the Taylor second-order approximation of the function $$g$$.

If $$G_t(x) = \nabla g(x)$$ in this equation, we can see that $$g(x - t \nabla g(x)) > g(x) - \alpha t \lVert \nabla g(x) \rVert_2^2 $$, which becomes identical to the backtracking condition of gradient descent. 

**Note:** For more details on the backtracking of gradient descent, refer to [06-02-02 backtracking line search]({% multilang_post_url contents/chapter06/21-03-20-06_02_02_backtracking_line_search %}).

### Backtracking line search algorithm
If we summarize this in an algorithm, it is as follows. (However, $$\nabla x = - t G_t(x)$$)

1. Initialize the parameters. ($$0 \lt \beta \lt 1$$, $$0 \lt \alpha \le 1/2$$)
2. In each iteration, initialize $$t = t_{\text{init}}$$. ($$t_{\text{init}} = 1$$)
3. If the condition $$g(x - tG_t(x)) \gt g(x) - t \nabla g(x)^T G_t(x) + \frac{t}{2} \parallel G_t(x) \parallel_2 ^2 $$ is satisfied, reduce $$t = \beta t$$. Repeat step 3 while this condition is met.
4. Perform the gradient descent update $$ x^+ = x - t G_t(x) = \text{prox}_t(x - t \nabla g(x))$$.
5. If the termination condition is not met, go back to step 2.

When backtracking in proximal gradient descent, since $$G_t(x)$$ is computed repeatedly, the proximal mapping included in $$G_t(x)$$ is also computed repeatedly. Since the proximal mapping is very costly to compute, the overall computational cost of backtracking can be high.

### Convergence Theorem
Under the same assumptions as above, the backtracking line search method also satisfies the same performance.

>**Proximal gradient descent** satisfies the following equation for backtracking line search. The step size is $$t_{\text{min}} = \text{min} \{1,\beta /L \}$$.

> $$
f(x^{(k)})−f^{\star} ≤ \frac{\lVert x^{(0)} − x^{\star} \rVert_{2}^{2}}{2 t_{min}k}, \space t_{\text{min}} = \text{min} \{ 1, \beta / L \} \\
$$
