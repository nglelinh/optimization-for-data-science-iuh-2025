---
layout: post
title: 06-03-03 Convergence analysis for backtracking
chapter: '06'
order: 10
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
lesson_type: required
---

Suppose $$f$$ is convex and differentiable with $$dom(f) = \mathbb{R}^n$$, and $$\nabla f$$ is Lipschitz continuous with constant $$L > 0$$:
>$$ \| \nabla f(x) - \nabla f(y) \|_2 \le L \| x - y \|_2 $$ for any $$x, y$$

Reference: [[Wikipedia: Lipschitz continuity](https://en.wikipedia.org/wiki/Lipschitz_continuity)]

## Convergence Theorem
**Gradient descent** with backtracking line search satisfies:
> $$ \begin{align}
f(x^{(k)}) - f^* \le \frac{\| x^{(0)} - x^* \|_2^2}{2 t_{min} k}, \quad t_{min} = \min \{ 1, \beta/L \}
\end{align} $$

The convergence rate for backtracking line search is similar to that for fixed step size, with the step size $$t$$ replaced by $$t_{min}$$. If $$\beta$$ is not too small, the performance is comparable to fixed step size ($$\beta/L$$ vs. $$1/L$$).