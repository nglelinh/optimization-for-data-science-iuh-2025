---
layout: post
title: '09-05-02 Convergence analysis'
chapter: '09'
order: 8
owner: Kyeongmin Woo
categories:
- chapter09
lang: en
---

Proving $$O(1/k)$$ convergence for plain proximal gradient was straightforward because $$f(x^{(k)})$$ decreases monotonically at every step. Proving $$O(1/k^2)$$ convergence for accelerated proximal gradient is famously subtler—precisely because $$f(x^{(k)})$$ is *not* monotonic! Instead of proving $$f(x^{(k)}) \le f(x^{(k-1)})$$, the proof constructs a clever **Lyapunov potential function** combining the scaled objective gap $$(k+1)^2 (f(x^{(k)}) - f^\star)$$ with a kinetic-energy term, and shows that *this combined energy* never increases.

## Key ideas: Understanding the $$O(1/k^2)$$ Convergence Theorem

- **Pillar 1 — The $$O(1/(k+1)^2)$$ Upper Bound:** Under $$L$$-smoothness of $$g$$ and convexity of $$h$$, accelerated proximal gradient with fixed step $$t \le 1/L$$ satisfies $$f(x^{(k)}) - f^\star \le \frac{2L \|x^{(0)} - x^\star\|_2^2}{(k+1)^2}$$. Notice the quadratic denominator $$(k+1)^2$$, which cuts iteration complexity from $$O(1/\varepsilon)$$ down to $$O(1/\sqrt{\varepsilon})$$.
- **Pillar 2 — Energy Conservation Instead of Monotonic Descent:** Because momentum injects kinetic energy, $$f(x^{(k)})$$ can temporarily rise while kinetic energy drops, yet the total potential $$\mathcal{E}_k = t_k^2(f(x^{(k)}) - f^\star) + \frac{1}{2t}\|z^{(k)} - x^\star\|_2^2$$ decreases monotonically ($$\mathcal{E}_k \le \mathcal{E}_{k-1}$$), immediately yielding $$f(x^{(k)}) - f^\star \le \mathcal{E}_0 / t_k^2 = O(1/k^2)$$.
- **Pillar 3 — Backtracking Line Search Constant:** When $$L$$ is unknown and backtracking shrinks $$t$$ by factor $$\beta \in (0, 1)$$, the exact same $$O(1/k^2)$$ bound holds with $$L$$ replaced by $$L/\beta$$ (provided step sizes are non-increasing, $$t_k \le t_{k-1}$$).
- **Pillar 4 — Optimality via Nesterov's Lower Bound:** For high-dimensional smooth convex problems ($$n \ge 2k+1$$), no first-order method whose iterates lie in the span of past gradients can beat $$\Omega(L \|x^{(0)} - x^\star\|_2^2 / k^2)$$, certifying that accelerated proximal gradient is worst-case optimal.

### Worked example: Comparing Guaranteed Iteration Budgets for $$O(1/k)$$ vs. $$O(1/k^2)$$

Suppose a composite problem has $$L = 10$$, initial squared distance $$\|x^{(0)} - x^\star\|_2^2 = 4$$, step size $$t = 1/L = 0.1$$, and target suboptimality $$\varepsilon = 10^{-3}$$.

1. **Plain Proximal Gradient bound:** $$f(x^{(k)}) - f^\star \le \frac{L \|x^{(0)} - x^\star\|_2^2}{2k} = \frac{10 \cdot 4}{2k} = \frac{20}{k}$$.
   - Set $$\frac{20}{k} \le 10^{-3} \implies k \ge 20{,}000$$ iterations.
2. **Accelerated Proximal Gradient bound:** $$f(x^{(k)}) - f^\star \le \frac{2L \|x^{(0)} - x^\star\|_2^2}{(k+1)^2} = \frac{2 \cdot 10 \cdot 4}{(k+1)^2} = \frac{80}{(k+1)^2}$$.
   - Set $$\frac{80}{(k+1)^2} \le 10^{-3} \implies (k+1)^2 \ge 80{,}000 \implies k + 1 \ge \sqrt{80{,}000} \approx 282.84 \implies k = 282$$ iterations!
3. **Speedup ratio:** Even though the numerator constant is $$4\times$$ larger ($$80$$ vs. $$20$$), the quadratic denominator reduces the guaranteed iteration count from **20,000** down to **282**—more than a **$$70\times$$ speedup**—and at $$\varepsilon = 10^{-5}$$ the speedup jumps to over **$$700\times$$**!

# Convergence analysis

In this section, we analyze the convergence of the accelerated proximal gradient method.

## Convergence Theorem
Suppose $$g$$ is convex and differentiable, $$h$$ is convex, and $$\nabla g$$ is Lipschitz continuous with constant $$L > 0$$. Then, the accelerated proximal gradient method with fixed step size $$t \le 1/L$$ satisfies the following:

> $$f(x^{(k)}) - f^* \le \frac{2L \lVert x^{(0)} - x^* \rVert^2_2}{(k+1)^2}$$

This means the convergence rate is $$O(1/k^2)$$, which is faster than the standard proximal gradient method.

## Backtracking line search
The backtracking line search for the accelerated proximal gradient method is similar to that for the standard proximal gradient method, but the step size is chosen adaptively.

For more details, refer to Beck and Teboulle (2009), "A Fast Iterative Shrinkage-Thresholding Algorithm for Linear Inverse Problems" (FISTA).
