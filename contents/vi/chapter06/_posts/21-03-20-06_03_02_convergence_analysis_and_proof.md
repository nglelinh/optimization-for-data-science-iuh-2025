---
layout: post
title: 06-03-02 Convergence analysis & Proof
chapter: '06'
order: 9
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
**Gradient descent** with fixed step size $$t \le 1/L$$ satisfies:
>$$
\begin{align}
f(x^{(k)}) - f^* \le  \frac{ \| x^{(0)} - x^* \|^2_2 }{2tk}
\end{align}
$$

With fixed step size, the convergence rate is $$O(1/k)$$. To achieve $$f(x^{(k)}) - f^* \le \epsilon$$, $$O(1/\epsilon)$$ iterations are needed.

## Proof
If $$\nabla f$$ is Lipschitz continuous and $$f$$ is convex, then $$f$$ has a quadratic upper bound (see [06-03-02]({% multilang_post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %})).

> $$
\begin{align}
f(y) \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \| y - x \|^2_2 \quad \forall x, y
\end{align}
$$

For gradient descent $$x^+ = x - t \nabla f(x)$$, substitute $$y = x^+$$:

>$$
\begin{align}
f(x^+) & \le f(x) - t ( 1 - \frac{Lt}{2} )\| \nabla f(x) \|^2_2 \\\
& \le f(x) -  \frac{t}{2} \| \nabla f(x) \|^2_2 \quad \text{if } t \le 1/L
\end{align}
$$

Thus, $$f(x^+) < f(x)$$ and gradient descent converges.