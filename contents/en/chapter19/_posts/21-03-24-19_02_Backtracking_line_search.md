---
layout: post
title: 19-02 Backtracking line search
chapter: '19'
order: 6
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

In Lesson 19-01-02 we saw that a pure unit proximal Newton step on $$e^x - 4x + |x|$$ can actually *increase* the objective when started far from the solution. Fixing that with backtracking line search raises an immediate design question: should we recompute the expensive scaled prox $$\operatorname{prox}_H$$ at every trial step size $$t$$, or compute the direction $$v$$ *once* and search along the straight ray $$x + tv$$? Computing $$v$$ once and backtracking along the ray saves massive computation while still guaranteeing global convergence and eventual unit-step acceptance!

## Background Knowledge Map: Composite Backtracking Without Repeated Prox Solves

- **Composite Directional Derivative Proxy:** Because $$h$$ is nonsmooth, the classical Armijo slope $$\nabla f(x)^T v$$ does not exist. By convexity of $$h$$, $$\Delta = \nabla g(x)^T v + h(x + v) - h(x)$$ serves as a valid, strictly negative descent measure ($$\Delta \le -v^T H v < 0$$).
- **Modified Armijo Sufficient Decrease:** We accept $$t \in (0, 1]$$ as soon as $$f(x + tv) \le f(x) + \alpha t \nabla g(x)^T v + \alpha\big(h(x + tv) - h(x)\big)$$ (or equivalently using $$\alpha t \Delta$$, since $$h(x + tv) - h(x) \le t(h(x + v) - h(x))$$ by convexity!).
- **Single-Prox Efficiency Advantage:** Unlike proximal gradient backtracking (which re-evaluates $$\operatorname{prox}_{t h}$$ for every shrunk $$t$$), proximal Newton solves the expensive scaled prox *only once* per outer iteration to get $$v$$, then only evaluates scalar function values $$f(x + tv)$$ during backtracking.
- **Automatic Transition to Unit Steps:** Near $$x^\star$$, once $$\|x - x^\star\|$$ is small enough, the quadratic Taylor remainder becomes negligible compared to $$-\frac{1}{2} v^T H v$$, so $$t = 1$$ passes the Armijo check immediately for any $$\alpha \le 1/2$$.

### Step-by-Step Worked Example (Read Slowly): Executing Composite Backtracking on $$e^x - 4x + |x|$$

Resume directly from Lesson 19-01-02: $$f(x) = e^x - 4x + |x|$$ at $$x = 0$$ ($$f(0) = 1$$, $$g'(0) = -3$$), with the single precomputed proximal Newton direction $$v = +2$$. Choose backtracking parameters $$\alpha = 0.25$$ and $$\beta = 0.5$$.

1. **Trial 1 ($$t = 1$$):**
   - Candidate point: $$x + 1 \cdot v = 2$$.
   - Actual objective: $$f(2) = e^2 - 8 + 2 = e^2 - 6 \approx 1.3891$$.
   - Armijo threshold: $$f(0) + \alpha t g'(0) v + \alpha(h(2) - h(0)) = 1 + 0.25(1)(-3)(2) + 0.25(2 - 0) = 1 - 1.5 + 0.5 = 0.0$$.
   - Check: $$1.3891 > 0.0$$ $$\implies$$ **FAIL!** Shrink $$t \leftarrow \beta t = 0.5$$ (without re-solving any proximal subproblem!).
2. **Trial 2 ($$t = 0.5$$):**
   - Candidate point: $$x + 0.5 \cdot v = 1$$.
   - Actual objective: $$f(1) = e^1 - 4 + 1 = e - 3 \approx -0.2817$$.
   - Armijo threshold: $$f(0) + \alpha t g'(0) v + \alpha(h(1) - h(0)) = 1 + 0.25(0.5)(-3)(2) + 0.25(1 - 0) = 1 - 0.75 + 0.25 = 0.50$$.
   - Check: $$-0.2817 \le 0.50$$ $$\implies$$ **PASS!**
3. **Update and verify:**
   Accept $$x^1 = 1.0$$. Notice $$f$$ plunged from $$+1.0000$$ to $$-0.2817$$ (within $$0.014$$ of the global optimum $$f(\ln 3) \approx -0.2958$$!) using just *one* proximal Newton solve and *two* scalar evaluations of $$f$$.

**Proximal newton method** may not converge in cases with pure step size $$t_k=1, k=1,2,3, \cdots$$ like newton's method. Therefore, we need to optimize the step size through backtracking line search.

## Backtracking line search algorithm

1. Initialize parameters. ($$0 \lt \alpha \le 1/2, 0 \lt \beta \lt 1$$)
2. At each iteration, compute the Proximal newton direction as $$v = \text{prox}_{H} ( x - H^{-1} \nabla g (x) ) - x$$.
3. Initialize $$t=1$$.
4. If the condition $$f(x + tv) \gt f(x) + \alpha t \nabla g(x)^T v + \alpha (h(x + tv) - h(x))$$ is satisfied, reduce $$t=\beta t$$. Iterate step 4 while this condition is satisfied. ($$f = g + h$$)
5. Execute the Proximal newton update $$x^+ = x + tv$$.
6. If the termination condition is not satisfied, go to step 2.

Intuitively, we find a step size $$t$$ such that we move along direction $$v$$ to a position where the linear approximation of function $$f$$ at $$x$$ is reduced by a factor of $$\alpha$$. Since the $$h$$ part of $$f$$ is not differentiable, we use the discrete derivative $$h(x + tv) - h(x)$$.

## Efficiency of algorithm
There are many methods for performing backtracking line search, and here we have introduced one of them. 

In this method, when computing $$v$$, the prox operator is computed only once. In the case of proximal gradient descent, the prox operator had to be computed iteratively in the inner loop, which is a distinctly different characteristic. Therefore, this method can perform backtracking line search very efficiently when the computation of the prox operator is complex.

### [reference] Backtracking line search by method
* Gradient descent [06-02-02 Backtracking line search]({% multilang_post_url contents/chapter06/21-03-20-06_02_02_backtracking_line_search %})
* Proximal gradient descent [09-02 Convergence analysis]({% multilang_post_url contents/chapter09/20-01-08-09_02_convergence_analysis %})
* Newton's method [14-04 Backtracking line search]({% multilang_post_url contents/chapter14/2021-03-26-14_04_backtracking_line_search %})
