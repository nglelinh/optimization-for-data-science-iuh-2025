---
layout: post
title: '08-01-01 Step size choices'
chapter: '08'
order: 3
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

Imagine trying to park a car at the exact bottom of a V-shaped ramp where the accelerator only has two settings: full forward or full reverse. If your stride length stays fixed forever, you will hop back and forth across the bottom indefinitely without ever landing on it; if you shrink your stride too fast, you will stall halfway down the ramp and never reach the bottom. Choosing step sizes $$t_k$$ in the subgradient method is the exact mathematical balancing act between reaching the optimum from any distance and damping out the oscillations once you arrive.

## Key ideas: Step-Size Schedules in Nonsmooth Optimization

- **Pillar 1 — Non-Vanishing Subgradients Near $$x^\star$$:** Unlike smooth gradients that shrink continuously to $$0$$ as $$x \to x^\star$$, subgradients of nonsmooth functions like $$|x|$$ maintain norm $$1$$ arbitrarily close to the minimizer. Fixed step sizes therefore create a permanent residual error neighborhood around $$f^\star$$.
- **Pillar 2 — The Infinite-Travel Condition ($$\sum_{k=1}^\infty t_k = \infty$$):** Because the starting point $$x^{(0)}$$ may lie arbitrarily far from $$x^\star$$, the total accumulated step length must diverge so the algorithm can traverse any finite initial distance $$R = \|x^{(0)} - x^\star\|_2$$.
- **Pillar 3 — The Square-Summable Noise Condition ($$\sum_{k=1}^\infty t_k^2 < \infty$$):** The overshoot error accumulated from non-vanishing subgradient norms scales with $$\sum_{k=1}^K t_k^2 G^2$$. Requiring this series to converge guarantees that the error ratio $$\frac{\sum t_k^2}{\sum t_k} \to 0$$, ensuring exact convergence $$f_{\text{best}}^{(k)} \to f^\star$$.
- **Pillar 4 — Constant Step Length vs. Constant Step Size:** Scaling the step by the subgradient norm ($$t_k = \gamma / \|g^{(k-1)}\|_2$$) keeps the Euclidean displacement $$\|x^{(k)} - x^{(k-1)}\|_2 = \gamma$$ uniform across steep and flat regions, preventing wild jumps when $$\|g\|$$ is large.

### Worked example: Fixed vs. Diminishing Step Sizes on $$f(x) = |x|$$

Let $$f(x) = |x|$$ ($$x^\star = 0, f^\star = 0$$), starting at $$x^{(0)} = 0.7$$, using subgradient $$g(x) = \operatorname{sign}(x)$$ (with $$g(0) = 0$$).

1. **Fixed step size $$t_k = 0.5$$:**
   - $$k=1$$: $$x^{(1)} = 0.7 - 0.5(1) = 0.2$$ ($$f = 0.2$$).
   - $$k=2$$: $$x^{(2)} = 0.2 - 0.5(1) = -0.3$$ ($$f = 0.3$$).
   - $$k=3$$: $$x^{(3)} = -0.3 - 0.5(-1) = 0.2$$ ($$f = 0.2$$).
   - The iterates enter a permanent 2-cycle $$0.2 \leftrightarrow -0.3$$; $$f_{\text{best}}^{(k)}$$ stalls at $$0.2 \le \frac{G^2 t}{2} = \frac{1^2 \cdot 0.5}{2} = 0.25$$ and never reaches $$0$$.
2. **Diminishing step size $$t_k = 1/k$$ (satisfies $$\sum 1/k = \infty$$ and $$\sum 1/k^2 = \pi^2/6 < \infty$$):**
   - $$k=1$$ ($$t_1 = 1$$): $$x^{(1)} = 0.7 - 1(1) = -0.3$$ ($$f = 0.3$$).
   - $$k=2$$ ($$t_2 = 0.5$$): $$x^{(2)} = -0.3 - 0.5(-1) = 0.2$$ ($$f = 0.2$$).
   - $$k=3$$ ($$t_3 = 1/3$$): $$x^{(3)} = 0.2 - \frac{1}{3}(1) = -\frac{2}{15} \approx -0.133$$ ($$f \approx 0.133$$).
   - $$k=4$$ ($$t_4 = 0.25$$): $$x^{(4)} = -\frac{2}{15} + \frac{1}{4} = \frac{7}{60} \approx 0.117$$ ($$f \approx 0.117$$).
3. **Compare with a too-fast schedule $$t_k = 2^{-k}$$ ($$\sum 2^{-k} = 1 < \infty$$):** Starting from $$x^{(0)} = 2.0$$, the maximum possible total movement is $$\sum_{k=1}^\infty 2^{-k} = 1$$, so $$x^{(k)} > 1$$ forever and the method stalls at $$f(x) \ge 1$$—illustrating why $$\sum t_k = \infty$$ is indispensable.

There are various ways to choose the **step size** in the subgradient method.

Let’s take a closer look at the following two approaches:

- **Fixed step sizes**: $$t_k = t$$, where $$k = 1, 2, 3, ...$$
- **Diminishing step sizes**: $$t_k$$ that satisfy the following conditions:

>\begin{align}
> \sum_{k=1}^{\infty} t_k = \infty, \quad \sum_{k=1}^{\infty} t_k^{2} < \infty
>\end{align}

### Example of Diminishing step sizes

> $$\begin{align}
& t_k = \frac{1}{k}, k = 1,2,3,... \\
& \sum_{k=1}^{\infty}t_k = \infty \quad \text{(Harmonic  series)} \\
& \sum_{k=1 }^{\infty}t^2_k \approx 1.644934 < \infty \quad \text{(Basel problem)} \\
\end{align} $$

A key feature of the step size in the subgradient method is that it must be set in advance, unlike in gradient descent. In other words, unlike the backtracking line search in gradient descent, the step size in the subgradient method does not adapt to the curvature of the function.
