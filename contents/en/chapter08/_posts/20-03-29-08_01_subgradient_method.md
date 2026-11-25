---
layout: post
title: '08-01 Subgradient Method'
chapter: '08'
order: 2
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

When you first replace $$\nabla f(x^{(k-1)})$$ with a subgradient $$g^{(k-1)} \in \partial f(x^{(k-1)})$$, the update equation looks almost identical to ordinary gradient descent. Yet removing differentiability changes the algorithm's personality completely: you lose the guarantee of monotonic descent, you can no longer rely on Armijo backtracking line search, and you must rethink what "making progress" even means. This lesson introduces the canonical subgradient iteration and explains why optimization theorists deliberately drop the word "descent" from its name.

## Background Knowledge Map: Anatomy of the Subgradient Update

- **Pillar 1 — Generalized First-Order Oracle:** At each iterate $$x^{(k-1)}$$, the algorithm queries a single arbitrary vector $$g^{(k-1)} \in \partial f(x^{(k-1)})$$. Computing all of $$\partial f(x)$$ is unnecessary; any one supporting slope suffices to define the step.
- **Pillar 2 — Failure of Descent Directions:** For a smooth function, $$-\nabla f(x)$$ is always a descent direction whenever $$\nabla f(x) \neq 0$$. For a nonsmooth function, $$-g$$ can point strictly uphill along a ridge (forming an obtuse angle with the steepest descent direction), so $$f(x - tg) > f(x)$$ can happen for *every* $$t > 0$$.
- **Pillar 3 — Distance Contraction as a Lyapunov Function:** Instead of tracking $$f(x^{(k)})$$, the analysis monitors $$\|x^{(k)} - x^\star\|_2^2$$. Because $$g^{(k-1)\top}(x^{(k-1)} - x^\star) \ge f(x^{(k-1)}) - f^\star > 0$$, the negative subgradient always forms an acute angle with $$x^\star - x^{(k-1)}$$, guaranteeing distance reduction for sufficiently small $$t_k$$.
- **Pillar 4 — Keeping Track of $$x_{\text{best}}^{(k)}$$:** Since the last iterate $$x^{(k)}$$ may sit on an upward oscillation, any practical implementation stores $$x_{\text{best}}^{(k)} = \arg\min_{0 \le i \le k} f(x^{(i)})$$ at essentially zero extra memory cost.

### Step-by-Step Worked Example (Read Slowly): Why $$-g$$ Can Fail to Be a Descent Direction for Every $$t > 0$$

Consider $$f(x_1, x_2) = \max\{ x_1 + 2x_2,\; x_1 - 2x_2 \}$$, which simplifies to $$f(x_1, x_2) = x_1 + 2|x_2|$$.

1. **Evaluate at $$x^{(0)} = (0, 0)$$:** Here $$f(0, 0) = 0$$, and both linear pieces achieve the maximum simultaneously.
2. **Identify the subdifferential:** By the pointwise-maximum rule, $$\partial f(0, 0) = \operatorname{conv}\{(1, 2), (1, -2)\} = \{ (1, v) : v \in [-2, 2] \}$$.
3. **Pick the valid subgradient $$g = (1, 2) \in \partial f(0, 0)$$:** Move along $$-g$$ with *any* positive step size $$t > 0$$:
   $$x(t) = (0, 0) - t(1, 2) = (-t, -2t).$$
4. **Evaluate $$f(x(t))$$:**
   $$f(-t, -2t) = (-t) + 2|-2t| = -t + 4t = 3t > 0 = f(0, 0).$$
5. **Interpretation:** For *every* $$t > 0$$, no matter how infinitesimally small, moving along $$-g$$ strictly increases $$f$$! Yet if the minimizer over a bounded region lies in the half-space $$x_1 < 0, x_2 = 0$$, say $$x^\star = (-5, 0)$$, notice that $$(-g)^\top (x^\star - x^{(0)}) = (-1, -2)^\top (-5, 0) = +5 > 0$$, confirming that $$-g$$ still points toward $$x^\star$$ even while climbing uphill.

Assume the domain of the function is $${R}^n$$ and there is a convex function $$f$$ that may not be differentiable everywhere.

The subgradient method is defined by replacing the gradient in gradient descent with a subgradient. ($$\nabla f(x^{(k-1)}) \to g(x^{(k-1)})$$)

>$$ x^{(k)} = x^{(k-1)} - t_k \cdot g^{(k-1)}, \quad k = 1, 2, 3, . . . $$

Here, $$g^{(k-1)} \in \partial f(x^{(k-1)})$$, i.e., $$g^{(k-1)}$$ is a subgradient of $$f$$ at $$x^{(k-1)}$$.

## Subgradient method (not subgradient "descent")

Unlike gradient descent, the subgradient method does not always guarantee descent at each step (hence the name is not subgradient "descent"). Therefore, when using the subgradient method, it is important to track the best result at each iteration.

>$$f(x_{best}^{(k)}) = \min_{i=0,...k} f(x^{(i)})$$ 

$$f(x^{(k)}_{best})$$ denotes the minimum value of the function $$f$$ obtained over $$k$$ iterations of the subgradient method.
