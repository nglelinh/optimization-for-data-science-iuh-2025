---
layout: post
title: 06-03-06 Can we do better?
chapter: '06'
order: 13
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

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