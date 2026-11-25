---
layout: post
title: '09-05-01 Accelerated proximal gradient method'
chapter: '09'
order: 7
owner: Kyeongmin Woo
categories:
- chapter09
lang: en
---

Extending Nesterov's smooth acceleration to composite nonsmooth problems $$f(x) = g(x) + h(x)$$ was one of the landmark breakthroughs of 2000s optimization—independently refined by Nesterov (2007) and popularized by Beck and Teboulle (2009) as **FISTA**. With only two lines of extra arithmetic—an extrapolated point $$v$$ and a scalar momentum sequence—you keep the exact same per-iteration cost as proximal gradient descent while upgrading the convergence rate from $$O(1/\varepsilon)$$ to the optimal $$O(1/\sqrt{\varepsilon})$$.

## Key ideas: Mechanics of Accelerated Proximal Gradient

- **Pillar 1 — Two-Sequence State ($$x^{(k)}$$ and $$v^{(k)}$$):** The algorithm maintains the main proximal iterates $$x^{(k)}$$ and an auxiliary extrapolated sequence $$v^{(k)} = x^{(k-1)} + \frac{k-2}{k+1}(x^{(k-1)} - x^{(k-2)})$$. Notice that $$v^{(k)}$$ may leave the sparse support or feasible set; the subsequent proximal map $$\operatorname{prox}_{t_k h}$$ immediately snaps $$x^{(k)}$$ back.
- **Pillar 2 — Same Oracle Cost as Plain Proximal Gradient:** Each iteration still performs exactly one smooth gradient evaluation $$\nabla g(v^{(k)})$$ and one proximal evaluation $$\operatorname{prox}_{t_k h}$$. There are no Hessians, no inner loops, and only one extra vector stored in memory.
- **Pillar 3 — Nesterov's Historical Arc (1983–2007):** Nesterov first accelerated smooth unconstrained problems (1983), then refined estimate sequences (1988), bridged to nonsmooth problems via smoothing (2005), and finally unified composite optimization $$g + h$$ (2007)—achieving $$O(1/\sqrt{\varepsilon})$$ whenever $$h$$ is prox-friendly.
- **Pillar 4 — Backtracking Compatibility:** Just like plain proximal gradient, accelerated proximal gradient supports backtracking line search on $$g$$ at the extrapolated point $$v^{(k)}$$ whenever $$L$$ is unknown, preserving the $$O(1/k^2)$$ rate.

### Worked example: Two Steps of Accelerated Proximal Gradient on a 1D Lasso

Minimize $$f(x) = \frac{1}{2}(x - 5)^2 + |x|$$ (so $$\nabla g(x) = x - 5$$, $$L = 1$$, exact optimum $$x^\star = S_1(5) = 4$$) using conservative step size $$t = 0.5$$, starting from $$x^{(0)} = x^{(-1)} = 0$$, with momentum $$\beta_k = \frac{k-1}{k+2}$$ for $$k = 1, 2$$.

1. **Iteration $$k = 1$$ ($$\beta_1 = 0$$):**
   - Extrapolate: $$v^{(1)} = x^{(0)} + 0 = 0$$.
   - Smooth step: $$u^{(1)} = 0 - 0.5(0 - 5) = 2.5$$.
   - Soft-threshold with $$\lambda t = 1 \cdot 0.5 = 0.5$$:
     $$x^{(1)} = S_{0.5}(2.5) = 2.0.$$
2. **Iteration $$k = 2$$ ($$\beta_2 = 1/4 = 0.25$$):**
   - Extrapolate: $$v^{(2)} = x^{(1)} + 0.25(x^{(1)} - x^{(0)}) = 2.0 + 0.25(2.0 - 0) = 2.5$$.
   - Smooth step at $$v^{(2)}$$: $$u^{(2)} = 2.5 - 0.5(2.5 - 5) = 2.5 + 1.25 = 3.75$$.
   - Soft-threshold with $$\lambda t = 0.5$$:
     $$x^{(2)} = S_{0.5}(3.75) = 3.25.$$
3. **Compare with plain ISTA ($$\beta_k \equiv 0$$) at $$k = 2$$:**
   - Plain ISTA gives $$u^{(2)}_{\text{ISTA}} = 2.0 - 0.5(2.0 - 5) = 3.5 \implies x^{(2)}_{\text{ISTA}} = S_{0.5}(3.5) = 3.0$$.
   - Accelerated proximal gradient is already at $$3.25$$ (distance $$0.75$$ from $$x^\star = 4$$) vs. $$3.0$$ (distance $$1.0$$) after just two steps!

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