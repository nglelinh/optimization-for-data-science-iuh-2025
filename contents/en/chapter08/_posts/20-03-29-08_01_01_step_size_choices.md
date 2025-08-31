---
layout: post
title: 08-01-01 Step size choices
chapter: "08"
order: 3
owner: "Kyeongmin Woo"
---

There are various ways to choose the **step size** in the subgradient method.

Let’s take a closer look at the following two approaches:

- **Fixed step sizes**: $$t_k = t$$, where $$k = 1, 2, 3, ...$$
- **Diminishing step sizes**: $$t_k$$ that satisfy the following conditions:

>\begin{align}
> \sum_{k=1}^{\infty} t_k = \infty, \quad \sum_{k=1}^{\infty} t_k^{2} < \infty
>\end{align}

#### Example of Diminishing step sizes

> $$\begin{align}
& t_k = \frac{1}{k}, k = 1,2,3,... \\
& \sum_{k=1}^{\infty}t_k = \infty \quad \text{(Harmonic  series)} \\
& \sum_{k=1 }^{\infty}t^2_k \approx 1.644934 < \infty \quad \text{(Basel problem)} \\
\end{align} $$

A key feature of the step size in the subgradient method is that it must be set in advance, unlike in gradient descent. In other words, unlike the backtracking line search in gradient descent, the step size in the subgradient method does not adapt to the curvature of the function.
