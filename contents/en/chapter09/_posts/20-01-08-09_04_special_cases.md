---
layout: post
title: '09-04 Special cases'
chapter: '09'
order: 5
owner: Kyeongmin Woo
categories:
- chapter09
lang: en
---

One of the deepest pleasures in convex optimization is watching seemingly unrelated algorithms snap together as special cases of a single template. Proximal gradient descent on $$f(x) = g(x) + h(x)$$ is not merely one more algorithm—it is a unifying umbrella that contains unconstrained gradient descent ($$h = 0$$), projected gradient descent ($$h = I_C$$), and Martinet–Rockafellar's proximal point / proximal minimization algorithm ($$g = 0$$) all at once. Seeing these connections lets you transfer convergence proofs and intuition effortlessly across all three regimes.

## Key ideas: The Unified Family of Generalized Gradient Methods

- **Pillar 1 — Smooth Limit ($$h(x) \equiv 0 \implies$$ Gradient Descent):** When $$h = 0$$, $$\operatorname{prox}_{t h}(y) = \arg\min_z \frac{1}{2t}\|z - y\|_2^2 = y$$ (the identity map), reducing proximal gradient directly to $$x^{(k)} = x^{(k-1)} - t_k \nabla g(x^{(k-1)})$$.
- **Pillar 2 — Indicator Limit ($$h(x) = I_C(x) \implies$$ Projected Gradient Descent):** Setting $$h(x) = 0$$ for $$x \in C$$ and $$+\infty$$ otherwise makes $$\operatorname{prox}_{t I_C}(y) = \arg\min_{z \in C} \|z - y\|_2^2 = P_C(y)$$, recovering projected gradient descent with an $$O(1/\varepsilon)$$ rate (beating projected *subgradient*'s $$O(1/\varepsilon^2)$$ whenever $$g$$ is smooth!).
- **Pillar 3 — Pure Proximal Limit ($$g(x) \equiv 0 \implies$$ Proximal Minimization / Point Algorithm):** When $$g = 0$$, the update $$x^{(k)} = \operatorname{prox}_{t_k h}(x^{(k-1)})$$ minimizes a strongly convex regularization of $$h$$ at every step. It converges for *any* step size $$t_k > 0$$ (even without smoothness of $$h$$!), though evaluating $$\operatorname{prox}_{t_k h}$$ can be as hard as minimizing $$h$$ itself.
- **Pillar 4 — When Prox Is Intractable:** If $$\operatorname{prox}_{t h}$$ has no closed form (e.g., total variation or overlapping group Lasso), one must either solve the prox subproblem approximately (requiring summable inner errors) or switch to operator splitting (ADMM, Douglas–Rachford, primal-dual methods).

### Worked example: One Formula, Three Classical Algorithms

Let $$C = [0, \infty)$$ (the nonnegative half-line), $$g(x) = \frac{1}{2}(x + 2)^2$$ (so $$\nabla g(x) = x + 2$$, $$L = 1$$), and start at $$x^{(0)} = 1$$ with step size $$t = 0.5$$.

1. **Case 1 — $$h(x) = 0$$ (Ordinary Gradient Descent):**
   $$x^{(1)} = \operatorname{prox}_{0.5 \cdot 0}(1 - 0.5(3)) = 1 - 1.5 = -0.5.$$
   The iterate freely enters the negative half-line heading toward $$x^\star = -2$$.
2. **Case 2 — $$h(x) = I_{[0, \infty)}(x)$$ (Projected Gradient Descent):**
   - Gradient proposal: $$y = 1 - 0.5(3) = -0.5$$.
   - Prox of indicator = Euclidean projection onto $$[0, \infty)$$:
     $$x^{(1)} = P_{[0, \infty)}(-0.5) = \max(-0.5,\; 0) = 0.$$
   It immediately hits the constrained optimum $$x^\star = 0$$!
3. **Case 3 — $$g(x) = 0$$, $$h(x) = \frac{1}{2}(x + 2)^2$$ (Proximal Minimization Algorithm):**
   $$x^{(1)} = \arg\min_z \left\{ \frac{1}{2(0.5)}(z - 1)^2 + \frac{1}{2}(z + 2)^2 \right\} = \arg\min_z \left\{ (z - 1)^2 + \frac{1}{2}(z + 2)^2 \right\}.$$
   Setting the derivative $$2(z - 1) + (z + 2) = 0 \implies 3z = 0 \implies x^{(1)} = 0$$. Notice that unlike explicit gradient descent, this *implicit* step stays stable for any $$t > 0$$—even $$t = 1000$$ moves smoothly to $$z = \frac{1 - 2t}{1 + t} \approx -2$$ without ever diverging!

# Special cases

Proximal gradient descent is also called composite gradient descent or generalized gradient descent.

Why is it called **"generalized”**? The reason is that Proximal gradient descent encompasses all of the following special cases:

- $$h = 0 \to$$ gradient descent
- $$h = I_C \to$$ projected gradient descent 
- $$g = 0 \to$$ proximal minimization algorithm

Therefore, all these algorithms have a convergence rate of $$O(1/\epsilon)$$.

## Projected gradient descent
When $$I_C(x)$$ is the indicator function of a closed convex set $$C \in \mathbb{R}^n$$, the problem of minimizing $$g(x)$$ over the set $$C$$ can be reformulated as follows. (Note: $$C$$ must be a closed set so that the projection is well-defined.)

> $$ \min_{x \in C} g(x) \iff \min_x g(x) + I_C(x)$$
>
> $$I_C(x) = 
>\begin{cases}
>0, & x \in C \\
>\infty, & x \notin C
>\end{cases}$$

At this time, the proximal mapping is defined as follows.

> $$
>\begin{align}
>\text{prox}_t(x)  
>&= \underset{z}{\text{argmin}} \frac{1}{2t} \lVert x−z \rVert_2^2 + I_C(z) \\
>& = \underset{z \in C}{\text{argmin}} \lVert x−z \rVert_2^2
>\end{align} $$

As a result, the proximal mapping $$\text{prox}_t(x) = P_C(x)$$ is the projection operator onto $$C$$.

The proximal gradient update step is: $$x^+ = P_C (x−t \nabla g(x) )$$. In other words, after performing the gradient descent update, you project onto $$C$$.

In the figure below, the pink rectangle is the feasible set $$C$$, and the current position is the upper of the two points below the rectangle. After taking a gradient descent step, you move outside $$C$$, so you project back onto $$C$$ to return inside the feasible set.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/projected_gradient_descent.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Fig1] Projected Gradient Descent [3]]</figcaption>
</p>
</figure>

## Proximal minimization algorithm

Consider the problem of minimizing a convex function $$h$$ as follows. Here, $$h$$ does not need to be differentiable and $$g(x) = 0$$.
>
\begin{align}
\min_x h(x)
\end{align}

The proximal mapping is defined as:
> $$
\begin{align}
x^{(k)} &= \text{prox}_{t_k} \big(x^{(k-1)} - t_k \nabla g ( x^{(k-1)} ) \big) , \qquad k = 1, 2, 3, ... \\
&= \text{prox}_{t_k} \big(x^{(k-1)} \big) ,  \qquad \qquad \qquad \qquad \; k = 1, 2, 3, ... \\
\end{align} $$

Therefore, the proximal gradient update step is:
> $$x^+ = \underset{z}{\text{argmin}} \frac{1}{2t} \lVert x−z \rVert_2^2 + h(z)$$

This proximal gradient method, defined only by $$h$$ with $$g = 0$$, is called the **proximal minimization algorithm (PMA)**. This method is faster than subgradient methods, but if the proximal mapping does not have a closed form, it cannot be implemented.

## What happens if we can't evaluate prox?
Theoretically, when applying proximal gradient to $$f = g + h$$, it is assumed that the prox function can be computed exactly. That is, it is assumed that the minimum can be found exactly via the proximal mapping.
>  $$\text{prox}_t(x )= \underset{z}{\text{argmin}} \frac{1}{2t} \lVert x−z \rVert_2^2 + h(z)$$

In general, it is not clear what happens if the minimum is only approximated.
However, if the error in approximating the prox operator can be precisely controlled, it has been shown that the original convergence rate can be maintained. (Schmidt et al. (2011), Convergence rates of inexact proximal-gradient methods for convex optimization)

In practice, if prox can be computed approximately, it will be performed with high accuracy.
