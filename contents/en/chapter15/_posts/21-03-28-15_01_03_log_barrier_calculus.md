---
layout: post
title: 15-01-03 Log barrier calculus
chapter: "15"
order: 5
owner: "Minjoo Lee"
categories:
- chapter15
lang: en
---

To run Newton's method on $$tf(x) + \phi(x)$$, you need exact, bug-free formulas for $$\nabla \phi(x)$$ and $$\nabla^2 \phi(x)$$. Look closely at the Hessian of the log barrier: it automatically splits into a sum of positive-semidefinite rank-1 outer products $$\frac{1}{h_i(x)^2}\nabla h_i(x)\nabla h_i(x)^T$$ plus positively weighted Hessians $$-\frac{1}{h_i(x)}\nabla^2 h_i(x)$$ (since $$h_i(x) < 0$$). That structure explains *at a glance* why $$\phi$$ is always convex and why its curvature explodes right as you approach any constraint wall!

## Background Knowledge Map: Derivatives of the Logarithmic Barrier

- **Pillar 1 — Barrier Gradient (Repulsive Force):** $$\nabla \phi(x) = \sum_{i=1}^m \frac{1}{-h_i(x)}\nabla h_i(x)$$. Because $$-h_i(x) > 0$$ is the slack to wall $$i$$, approaching wall $$i$$ ($$-h_i(x) \to 0^+$$) creates an enormous gradient pushing $$x$$ inward along $$-\nabla h_i(x)$$.
- **Pillar 2 — Barrier Hessian (Two PSD Terms):** $$\nabla^2 \phi(x) = \sum_{i=1}^m \frac{1}{h_i(x)^2}\nabla h_i(x)\nabla h_i(x)^T + \sum_{i=1}^m \frac{1}{-h_i(x)}\nabla^2 h_i(x)$$. Every term is $$\succeq 0$$ for convex $$h_i$$.
- **Pillar 3 — Polyhedral Simplification (Linear Inequalities):** When $$h_i(x) = a_i^T x - b_i$$, $$\nabla^2 h_i = 0$$ vanishes, leaving the clean weighted Gram matrix $$\nabla^2 \phi(x) = A^T D^2 A$$ where $$D_{ii} = \frac{1}{b_i - a_i^T x}$$.
- **Pillar 4 — Nonnegative Orthant Special Case:** For $$x > 0$$ ($$h_i(x) = -x_i$$), $$\nabla \phi(x) = -X^{-1}\mathbf{1}$$ and $$\nabla^2 \phi(x) = X^{-2}$$ (purely diagonal!), which makes linear-programming Newton systems remarkably fast to factor.

### Step-by-Step Worked Example (Read Slowly): Computing $$\nabla \phi(x)$$ and $$\nabla^2 \phi(x)$$ for a 2D Triangle

Consider the triangular feasible set $$x_1 \ge 0$$, $$x_2 \ge 0$$, and $$x_1 + x_2 \le 3$$, so $$h_1(x) = -x_1$$, $$h_2(x) = -x_2$$, $$h_3(x) = x_1 + x_2 - 3$$. Evaluate $$\nabla \phi$$ and $$\nabla^2 \phi$$ at the interior point $$x = (1, 1)^T$$.

1. **Compute slacks $$-h_i(x)$$ and gradients $$\nabla h_i(x)$$:**
   - $$-h_1(1,1) = 1$$, $$\quad \nabla h_1 = (-1, 0)^T$$.
   - $$-h_2(1,1) = 1$$, $$\quad \nabla h_2 = (0, -1)^T$$.
   - $$-h_3(1,1) = 3 - (1+1) = 1$$, $$\quad \nabla h_3 = (1, 1)^T$$.
2. **Compute the barrier gradient $$\nabla \phi(1,1) = \sum_{i=1}^3 \frac{1}{-h_i(x)}\nabla h_i(x)$$:**
   $$\nabla \phi(1,1) = \frac{1}{1}\begin{bmatrix} -1 \\ 0 \end{bmatrix} + \frac{1}{1}\begin{bmatrix} 0 \\ -1 \end{bmatrix} + \frac{1}{1}\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}!$$
   Because $$\nabla \phi(1,1) = 0$$, $$x = (1,1)^T$$ is the exact **analytic center** of this triangle!
3. **Compute the barrier Hessian $$\nabla^2 \phi(1,1) = \sum_{i=1}^3 \frac{1}{h_i(x)^2}\nabla h_i \nabla h_i^T$$:**
   $$\nabla^2 \phi(1,1) = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} + \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} + \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} \succ 0.$$
   Notice $$\det = 4 - 1 = 3 > 0$$ and eigenvalues are $$1, 3 > 0$$, confirming strict convexity.

The gradient and Hessian of the log barrier function are as follows.
>
\begin{align}
\phi(x) = - \sum_{i=1}^{m} \log(-h_i(x))
\end{align}

Gradient:
>
\begin{align}
\nabla \phi(x) = - \sum_{i=1}^{m} \frac{1}{h_i(x)} \nabla h_i(x)
\end{align}

Hessian:

>
\begin{align}
\nabla^2 \phi(x) = \sum_{i=1}^{m} \frac{1}{h_i(x)^2} \nabla h_i(x) \nabla h_i(x)^T -  \sum_{i=1}^{m} \frac{1}{h_i(x)} \nabla^2 h_i(x)
\end{align}

## Example: $$\phi(x) = -\sum_{i=1}^{n} \log(x_i)$$
If we compute the gradient and Hessian for the barrier function $$\phi(x) = -\sum_{i=1}^{n} \log(-x_i)$$, we get the following results.
>
\begin{align}
\phi(x) = -\sum_{i=1}^{n} \log(x_i)
\end{align}
Therefore, $$h_i(x) =  -x_i$$ and $$x_i \ge 0$$.

Gradient:
>
$$
\nabla \phi(x) = - 
\begin{bmatrix}
1/x_1 \\\
\vdots \\\
1/x_n \\\
\end{bmatrix}
 = -X^{-1} \mathbb{1}, \qquad X = \text{diag}(x)$$
 
Hessian :
>
$$
\nabla^2 \phi(x) = 
\begin{bmatrix}
1/x_1^2 & \cdots & \\\
\vdots & \ddots & \vdots  \\\
& \cdots & 1/x_n^2 \\\
\end{bmatrix}
 = X^{-2}$$