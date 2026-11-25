---
layout: post
title: 06-03 Convergence analysis
chapter: '06'
order: 9
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

Watching a loss curve drop on one dataset is encouraging, but engineering critical systems demands *guarantees*: how many iterations does gradient descent take to reach accuracy $$\varepsilon$$, and how does that number depend on the problem's geometry? Section 06-03 builds the classical convergence theory of gradient descent—from the quadratic upper bound of $$L$$-smoothness to $$O(1/k)$$ sublinear rates and exponential linear rates under strong convexity.

## Background Knowledge Map: Roadmap of Gradient Descent Convergence Theory

1. **The Smoothness Pillar ($$L$$-Lipschitz Gradient)**: Assuming $$\|\nabla f(x) - \nabla f(y)\|_2 \le L\|x - y\|_2$$ yields the **Descent Lemma**: $$f(y) \le f(x) + \nabla f(x)^T(y-x) + \frac{L}{2}\|y-x\|_2^2$$. Every convergence proof in this section starts from this single quadratic upper bound.
2. **Sublinear $$O(1/k)$$ Rate for Smooth Convex Functions**: With fixed step $$t \le 1/L$$ (or backtracking with $$t_{\min} = \min(1, \beta/L)$$), gradient descent guarantees $$f(x^{(k)}) - f^\star \le \frac{\|x^{(0)} - x^\star\|_2^2}{2 t k}$$, meaning $$O(1/\varepsilon)$$ iterations to reach $$\varepsilon$$-suboptimality.
3. **Linear (Exponential) Rate under $$m$$-Strong Convexity**: Adding a quadratic *lower* bound $$f(y) \ge f(x) + \nabla f(x)^T(y-x) + \frac{m}{2}\|y-x\|_2^2$$ upgrades the rate to $$f(x^{(k)}) - f^\star \le \left(1 - \frac{m}{L}\right)^k (f(x^{(0)}) - f^\star)$$, requiring only $$O\bigl(\kappa \log(1/\varepsilon)\bigr)$$ iterations!
4. **Lower Bounds and Acceleration**: Nesterov proved that *no* first-order method can beat $$\Omega(1/k^2)$$ on smooth convex functions (or $$\Omega(\sqrt{\kappa}\log(1/\varepsilon))$$ under strong convexity)—motivating Nesterov Accelerated Gradient and momentum methods.

### Step-by-Step Worked Example (Read Slowly): Comparing Iteration Budgets at $$\varepsilon = 10^{-4}$$

Suppose a problem has smoothness constant $$L = 10$$, initial distance $$\|x^{(0)} - x^\star\|_2 = 1$$, and initial suboptimality $$f(x^{(0)}) - f^\star = 5$$. Using fixed step size $$t = 1/L = 0.1$$, compare the theoretical iteration count to guarantee $$f(x^{(k)}) - f^\star \le 10^{-4}$$:

1. **Case A — Smooth Convex Only ($$m = 0$$)**:
   $$\frac{\|x^{(0)} - x^\star\|_2^2}{2 t k} = \frac{1}{0.2 k} = \frac{5}{k} \le 10^{-4} \implies k \ge 50{,}000 \text{ iterations}.$$
2. **Case B — Smooth + Strongly Convex with $$m = 1$$ ($$\kappa = L/m = 10$$)**:
   $$\left(1 - \frac{1}{10}\right)^k \cdot 5 = 0.9^k \cdot 5 \le 10^{-4} \implies 0.9^k \le 2 \times 10^{-5}.$$
   Taking natural logs:
   $$k \ge \frac{\ln(2 \times 10^{-5})}{\ln(0.9)} = \frac{-10.8198}{-0.10536} \approx 102.7 \implies k = 103 \text{ iterations}!$$
3. **Takeaway**: Strong convexity (for example, adding even a modest L2 regularizer) slashes the guaranteed iteration budget from **50,000** down to **103**—nearly a **500×** speedup!

In this section, we analyze the convergence of Gradient Descent. We will examine the error bounds for convergence in the case of a fixed step size and in the case of backtracking. In addition, we will analyze the error bounds when the strong convexity condition is satisfied."