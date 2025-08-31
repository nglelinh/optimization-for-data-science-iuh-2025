---
layout: post
title: 09-05-01 Accelerated proximal gradient method
chapter: "09"
order: 7
owner: "Kyeongmin Woo"
---

# Accelerated proximal gradient method

If proximal gradient descent is accelerated, it can achieve the optimal convergence rate of $$O(1/\sqrt{\epsilon})$$. Nesterov proposed four methods, three of which are acceleration methods:

- 1983: Original acceleration method for smooth functions
- 1988: Another acceleration method for smooth functions
- 2005: Technique for smoothing nonsmooth functions along with the original acceleration method
- 2007: Acceleration method for composite functions

Now, let's look at the method of Beck and Teboulle (2008), which extends Nesterov's (1983) method for composite functions.

## Accelerated proximal gradient method
As before, suppose $$g$$ is convex and differentiable, and $$h$$ is convex. The problem is defined as:
> 
\begin{align}
\min_x g(x) + h(x)
\end{align}

The **Accelerated proximal gradient method** considers the direction in which $$x$$ was moving so that the direction does not change abruptly when moving to the next position. In other words, it gives momentum to the direction of progress, creating inertia to continue moving in the same direction as before.

The initial value of the algorithm is set to $$x^{(0)} = x^{(-1)} \in \mathbb{R}^n$$. Then, after calculating the position $$v$$ considering momentum, the proximal gradient is performed.

> $$
\begin{align}
v & = x^{(k-1)} + \frac{k-2}{k + 1}  (x^{(k-1)} −x^{(k-2)}) \\
x^{(k)} & = \text{prox}_{t_k} (v − t_k \nabla g(v)), k = 1,2,3,...  \\
\end{align} $$

- In the first step $$k = 1$$, $$x^{(k-1)} −x^{(k-2)}$$ is zero, so it is the same as the proximal gradient update.
- In the next steps, $$v$$ has momentum in the previous direction $$x^{(k-1)} −x^{(k-2)}$$. As $$k$$ increases, the momentum weight increases and converges to 1.
- When $$h = 0$$, this is the same as the **accelerated gradient method**.

The figure below shows how the momentum weight changes as $$k$$ changes.

In this figure, the value is negative when k = 0, but since the momentum term is zero at that time, it does not cause any problems. As k increases, the weight approaches 1, so the value is updated further and helps to converge faster.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/momentum_weight.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Fig1] Momentum weights [3]</figcaption>
</p>
</figure>

## Lasso example
If we apply the accelerated proximal gradient to the Lasso example seen earlier, we get the results shown in the figure below. It can be seen that the accelerated proximal gradient has much faster performance compared to subgradient or proximal gradient methods.

There is a part in the middle of the graph that jumps, which is called “Nesterov ripples.” Therefore, the accelerated proximal gradient is not monotonic decreasing and is not a descent method.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/accelerated_proximal_gradient.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Fig2] Accelerated Proximal Gradient [3]</figcaption>
</p>
</figure>