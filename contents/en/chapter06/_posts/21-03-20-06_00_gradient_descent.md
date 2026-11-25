---
layout: post
title: 06 Gradient Descent
chapter: '06'
order: 1
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

Imagine you are blindfolded on a vast mountain slope and want to reach the lowest valley floor. You cannot see the whole map, so you feel the slope under your boots, take a careful step downhill, and repeat. That humble idea—invented by Augustin-Louis Cauchy in 1847 to compute planetary orbits—is **Gradient Descent**, the engine driving modern machine learning, deep learning, and large-scale convex optimization.

## Background Knowledge Map: The Anatomy of Gradient Descent

1. **First-Order Oracle Model**: Gradient descent needs only function values $$f(x)$$ and gradients $$\nabla f(x)$$, avoiding the $$O(n^3)$$ cost of inverting an $$n \times n$$ Hessian matrix. That makes it feasible even when $$n$$ reaches billions of parameters.
2. **Step-Size Selection (The Throttle of Convergence)**: Moving in the steepest-descent direction $$-\nabla f(x_k)$$ is only half the algorithm—choosing how far to step ($$t_k$$) determines whether you crawl, converge cleanly, or explode to infinity. Fixed step sizes, backtracking line search, and exact line search balance per-step cost against reliability.
3. **Smoothness vs. Strong Convexity (Convergence Rates)**: When $$\nabla f$$ is $$L$$-Lipschitz continuous, gradient descent reduces error at rate $$O(1/k)$$ on general convex functions. Add $$m$$-strong convexity and the rate jumps to *linear* (exponential) convergence $$O\bigl((1 - m/L)^k\bigr)$$, governed by the condition number $$\kappa = L/m$$.
4. **Modern Extensions**: From functional gradient descent (Gradient Boosting) to mini-batch Stochastic Gradient Descent (SGD), Heavy-Ball/Nesterov Momentum, and L1/L2 regularized objectives, virtually every workhorse optimizer in data science is a direct descendant of this chapter's core update $$x_{k+1} = x_k - t_k \nabla f(x_k)$$.

### Step-by-Step Worked Example (Read Slowly): Three Iterations of Gradient Descent on a 2D Bowl

Minimize $$f(x_1, x_2) = x_1^2 + 4x_2^2$$ starting from $$x^{(0)} = (4, 1)$$ with fixed step size $$t = 0.2$$.

1. **Compute the gradient and smoothness constant**:
   $$\nabla f(x_1, x_2) = (2x_1,\; 8x_2), \qquad \nabla^2 f = \operatorname{diag}(2, 8) \implies L = 8.$$
   The stability threshold is $$t < 2/L = 0.25$$, and our choice $$t = 0.2$$ satisfies it.
2. **Iteration 1**:
   - Gradient at $$x^{(0)} = (4, 1)$$: $$\nabla f(x^{(0)}) = (8, 8)$$, $$f(x^{(0)}) = 16 + 4 = 20$$.
   - Update: $$x^{(1)} = (4, 1) - 0.2(8, 8) = (2.4,\; -0.6)$$, with $$f(x^{(1)}) = 5.76 + 1.44 = 7.20$$.
3. **Iteration 2**:
   - Gradient at $$x^{(1)} = (2.4, -0.6)$$: $$\nabla f(x^{(1)}) = (4.8,\; -4.8)$$.
   - Update: $$x^{(2)} = (2.4, -0.6) - 0.2(4.8, -4.8) = (1.44,\; 0.36)$$, with $$f(x^{(2)}) = 2.0736 + 0.5184 = 2.592$$.
4. **Observe the exact contraction factor**: Along $$x_1$$, each step multiplies by $$1 - 2(0.2) = 0.6$$; along $$x_2$$, each step multiplies by $$1 - 8(0.2) = -0.6$$ (oscillating across the steeper valley!). Thus $$f(x^{(k)}) = 0.36^k \cdot 20$$ shrinks geometrically toward $$f^\star = 0$$.

In this chapter, we explore **Gradient Descent**, one of the most fundamental and important methods in optimization. 

In optimization algorithms, choosing the search direction and step size is crucial for convergence speed and success. Gradient descent moves in the direction of the negative gradient. The step size can be fixed or adaptively chosen, and we will discuss both approaches in this chapter.

For gradient descent to converge, certain preconditions must be met. If these conditions are satisfied, we can analyze how quickly gradient descent converges. If strong convexity holds, convergence is even faster, and we will examine the convergence rate in such cases.

We will also look at applications of gradient descent, including gradient boosting and stochastic gradient descent.

A later optional lesson, [06-08 Applications and recent developments]({% multilang_post_url contents/chapter06/2026-09-16-06_08_Applications_Recent %}), contrasts the Lipschitz theory with the edge of stability, Lion, and schedule-free averaging (2021–2024). The linear rate of 06-03-04 can be reused on some *nonconvex* ERMs under the Polyak–Łojasiewicz condition; that bridge is the optional note [28-05]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}).
