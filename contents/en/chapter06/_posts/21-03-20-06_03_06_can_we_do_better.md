---
layout: post
title: 06-03-06 Can we do better?
chapter: '06'
order: 15
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

Gradient descent achieves $$O(1/k)$$ on smooth convex functions. Is that a fundamental speed limit of nature, or are we leaving performance on the table? In 1983, Arkadi Nemirovski and Yurii Nesterov answered both halves of that question: *no* first-order method can beat $$\Omega(1/k^2)$$—and Nesterov constructed an accelerated algorithm that actually hits that optimal $$O(1/k^2)$$ limit!

## Background Knowledge Map: Information-Based Complexity and Optimal First-Order Rates

1. **What Defines a First-Order Method?**: Every iterate $$x^{(k)}$$ lies in the linear span of the starting point and all past gradients:
   $$x^{(k)} \in x^{(0)} + \operatorname{span}\{\nabla f(x^{(0)}), \nabla f(x^{(1)}), \dots, \nabla f(x^{(k-1)})\}.$$
   Gradient descent uses only the *latest* gradient; accelerated methods combine past iterates (momentum) to exploit the full Krylov subspace.
2. **Nesterov's Worst-Case Lower Bound**: There exists an $$L$$-smooth convex quadratic (a tridiagonal chain where each gradient evaluation unlocks only one new coordinate per iteration!) such that **every** first-order method satisfies
   $$f(x^{(k)}) - f^\star \ge \frac{3L\|x^{(0)} - x^\star\|_2^2}{32(k + 1)^2} = \Omega\!\left(\frac{1}{k^2}\right).$$
3. **The Gap Between GD and Optimal First-Order Methods**:
   - *Smooth convex*: GD gets $$O(1/\varepsilon)$$ iterations; Nesterov Accelerated Gradient (NAG) achieves the optimal $$O(1/\sqrt{\varepsilon})$$.
   - *Smooth $$m$$-strongly convex*: GD gets $$O(\kappa \log(1/\varepsilon))$$; NAG achieves the optimal $$O(\sqrt{\kappa}\log(1/\varepsilon))$$.
4. **Why Momentum Breaks Monotonicity to Go Faster**: Unlike vanilla GD, accelerated methods can briefly *increase* $$f(x^{(k)})$$ (non-monotone oscillations), trading strict per-step descent for dramatically faster global convergence.

### Step-by-Step Worked Example (Read Slowly): Comparing GD vs. Nesterov Iteration Complexity

Suppose you need to solve a large smooth convex problem to suboptimality $$\varepsilon = 10^{-6}$$ (with $$L\|x^{(0)} - x^\star\|_2^2 = 1$$), and also consider a strongly convex version with condition number $$\kappa = 10{,}000$$.

1. **Smooth convex regime ($$\varepsilon = 10^{-6}$$)**:
   - **Vanilla Gradient Descent ($$O(1/\varepsilon)$$)**: requires roughly $$\frac{1}{2\varepsilon} = 500{,}000$$ iterations.
   - **Nesterov Accelerated Gradient ($$O(1/\sqrt{\varepsilon})$$)**: requires roughly $$\sqrt{\frac{2}{\varepsilon}} \approx 1{,}414$$ iterations — more than **350× faster**!
2. **Strongly convex regime ($$\kappa = 10{,}000$$, $$\varepsilon = 10^{-6}$$, $$\ln(1/\varepsilon) \approx 13.8$$)**:
   - **Vanilla Gradient Descent ($$\kappa \ln(1/\varepsilon)$$)**: $$\approx 10{,}000 \times 13.8 = 138{,}000$$ iterations.
   - **Nesterov Accelerated Gradient ($$\sqrt{\kappa}\ln(1/\varepsilon)$$)**: $$\approx 100 \times 13.8 = 1{,}380$$ iterations — a **100× speedup** purely from using past gradient history!

Gradient descent has a convergence rate of $$O(1/\epsilon)$$ for problems represented by functions that have Lipschitz gradients and are convex and differentiable. Are there first-order methods that are faster than gradient descent?

### First-order method
A first-order method can express changes at the $$x^{(k)}$$-th iteration as follows. Therefore, the change at the $$x^{(k)}$$-th iteration is expressed as the span of gradients from the initial position $$x^{(0)}$$ to $$x^{(k−1)}$$.

> $$x^{(0)} + $$ **span**$$\{∇f(x^{(0)}),∇f(x^{(1)}),...,∇f(x^{(k−1)})\}$$

###  Theorem (Nesterov)
Nesterov's theorem provides a lower bound for the convergence of first-order methods.

> **Nesterov Theorem** For any $$k ≤ (n−1)/2$$ and starting point $$x^{(0)}$$, there exists a function $$f$$ such that any first-order method satisfies the following condition (where $$n$$ denotes the dimension):<br>
\begin{align}
f(x^{(k)})−f^{\star} ≥ \frac{3L \lVert x^{(0)} −x^{\star} \rVert_2^2}{32(k + 1)^2 }\\\
\end{align}

Since Nesterov's theorem has $$k^2$$ in the denominator of the lower bound, the convergence rate becomes $$O(1/k^2)$$. Furthermore, the number of iterations becomes $$O(1/\sqrt{\epsilon})$$. We will examine this content in detail later.