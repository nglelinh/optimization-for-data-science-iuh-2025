---
layout: post
title: "19-01-03 Scaled proximal map"
chapter: '19'
order: 5
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

At first sight, the proximal Newton subproblem looks much messier than proximal gradient descent—a full quadratic form $$\frac{1}{2} v^T H v$$ entangled with a nonsmooth function $$h(x + v)$$. Yet if you simply change your ruler from the Euclidean norm $$\|z\|_2$$ to the **$$H$$-norm** $$\|z\|_H = \sqrt{z^T H z}$$, the entire proximal Newton update collapses back into the familiar one-line formula $$x^+ = \operatorname{prox}_H(x - H^{-1}\nabla g(x))$$. Even better, every geometric superpower of the ordinary prox—uniqueness and firm non-expansiveness—survives intact in the $$H$$-norm!

## Key ideas: Geometry of the $$H$$-Scaled Proximal Map

- **Change of Inner Product ($$H$$-Norm):** For any $$H \succ 0$$, $$\langle a, b \rangle_H = a^T H b$$ defines a valid inner product on $$\mathbb{R}^n$$ whose unit balls are ellipsoids aligned with the local curvature of $$g$$.
- **Definition & Uniqueness:** $$\operatorname{prox}_H(x) = \arg\min_z \frac{1}{2}\|x - z\|_H^2 + h(z)$$. Because $$H \succ 0$$ makes the quadratic term strictly convex and $$h$$ is convex, the minimizer exists and is strictly unique.
- **Firm Non-Expansiveness in $$\|\cdot\|_H$$:** Using subgradient monotonicity of $$h$$, one proves $$\|\operatorname{prox}_H(x) - \operatorname{prox}_H(y)\|_H^2 \le \langle x - y, \; \operatorname{prox}_H(x) - \operatorname{prox}_H(y) \rangle_H$$, which by Cauchy–Schwarz implies $$\|\operatorname{prox}_H(x) - \operatorname{prox}_H(y)\|_H \le \|x - y\|_H$$.
- **Why Scaled Prox Usually Lacks a Closed Form:** When $$H$$ is diagonal and $$h$$ is separable (like $$\|z\|_1$$), $$\operatorname{prox}_H$$ reduces to coordinate-wise soft-thresholding with per-coordinate thresholds $$1/H_{ii}$$. When $$H$$ has off-diagonal couplings, coordinates interact and an inner solver (such as coordinate descent) is required.

### Worked example: Computing $$\operatorname{prox}_H$$ and Verifying $$H$$-Non-Expansiveness

Let $$h(z) = |z_1| + |z_2|$$ and $$H = \begin{bmatrix} 1 & 0 \\ 0 & 4 \end{bmatrix} \succ 0$$. Evaluate $$\operatorname{prox}_H$$ at $$x = (2, 1)^T$$ and $$y = (0, 0)^T$$.

1. **Write out the scaled proximal subproblem at $$x = (2, 1)^T$$:**
   $$\operatorname{prox}_H(x) = \arg\min_{z_1, z_2} \left[\frac{1}{2}(1)(z_1 - 2)^2 + |z_1|\right] + \left[\frac{1}{2}(4)(z_2 - 1)^2 + |z_2|\right].$$
2. **Solve each coordinate exactly:**
   - Coordinate 1: $$z_1 - 2 + \operatorname{sign}(z_1) = 0 \implies z_1^\star = S_{1/1}(2) = 1$$.
   - Coordinate 2: $$4(z_2 - 1) + \operatorname{sign}(z_2) = 0 \implies z_2^\star = S_{1/4}(1) = 1 - 0.25 = 0.75$$.
   Thus $$\operatorname{prox}_H(x) = (1, \; 0.75)^T$$. (By symmetry, $$\operatorname{prox}_H(0, 0) = (0, 0)^T$$.)
3. **Verify non-expansiveness in the $$H$$-norm:**
   - Input $$H$$-distance squared:
     $$\|x - y\|_H^2 = (2)^2(1) + (1)^2(4) = 4 + 4 = 8 \implies \|x - y\|_H = \sqrt{8} \approx 2.8284.$$
   - Output $$H$$-distance squared:
     $$\|\operatorname{prox}_H(x) - \operatorname{prox}_H(y)\|_H^2 = (1)^2(1) + (0.75)^2(4) = 1 + 2.25 = 3.25 \implies \|\operatorname{prox}_H(x) - \operatorname{prox}_H(y)\|_H \approx 1.8028.$$
   Clearly $$1.8028 \le 2.8284$$—and notice it even satisfies *firm* non-expansiveness: $$\langle x - y, \operatorname{prox}_H(x) - \operatorname{prox}_H(y) \rangle_H = (2)(1)(1) + (1)(0.75)(4) = 5 \ge 3.25$$ $$\checkmark$$!

The **proximal Newton method** can be rewritten in the same form as **proximal gradient descent**.

## Scaled proximal map
If $$H \succ 0$$, the **scaled proximal map** is defined as follows.

> \begin{align}
\text{prox}_{H}(x) = \underset{z}{\text{argmin}}  \frac{1}{2} \parallel x - z \parallel_H^2 + h(z)
\end{align}

Here $$\parallel x\parallel_H^2 = x^THx$$ is the squared $$H\text{-norm}$$. When $$H = \frac{1}{t} I$$, this becomes the usual **unscaled proximal map**.

In general, the **scaled proximal map** has the same nice properties as the ordinary prox.

* **uniqueness**: the solution is unique (this holds because $$H \succ 0$$ makes the problem strictly convex).
* **non-expansiveness**: the map does not expand distances (this holds because the scaled proximal map generalizes the projection operator, which is non-expansive).

#### [Note] Non-expansiveness of the projection operator
For two points $$x$$, $$y$$ and the projection operator $$P_C$$ onto a convex set $$C$$, non-expansiveness means $$\parallel P_C(x) - P_C(y) \parallel_2 \le \parallel x - y \parallel_2$$. In other words, $$P_C$$ is 1-Lipschitz, which holds whenever $$C$$ is convex.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.01_03_projection_operator.png" alt="[Fig 1] Projection onto a convex set C [3]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Projection onto a convex set C [3]</figcaption>
</p>
</figure>

## Proximal Newton update
Using the **scaled proximal map**, the proximal Newton update can be rewritten as follows.

> $$
> \begin{align}
> z^{+} & = \underset{z}{\text{argmin}} \ \nabla g(x)^T (z - x) + \frac{1}{2} (z - x)^T H (z - x) + h(z) \\\\
> & =\underset{z}{\text{argmin}} \ \frac{1}{2} \parallel x - H^{-1} \nabla g(x) - z \parallel_H^2 + h(z)
> \end{align}
> $$

Equivalently:

> $$
> \begin{align}
> z^{(k)} & = \text{prox}_{H^{(k-1)}} ( x^{(k-1)} - (H^{(k-1)})^{-1} \nabla g (x^{(k-1)}) ) \\\\
> x^{(k)} & =x^{(k-1)} + t_k (z^{(k)} - x^{(k-1)} )
> \end{align}
> $$

Intuitively, we take a Newton step on $$g$$, apply the scaled prox operator with respect to $$H^{(k-1)}$$, and move in that direction.

From this we see the following.

* When $$h(z) = 0$$, the proximal operator is the identity, and we recover the ordinary Newton update.
* If we replace $$H^{(k-1)}$$ by $$\frac{1}{r_k} I$$ and set $$t_k = 1$$, we obtain the proximal gradient update with step size $$r_k$$.
* The difficulty of the prox depends not only on $$h$$ but also on the structure of the Hessian of $$g$$. For example, if $$H$$ is diagonal or banded, the problem is much easier than when $$H$$ is dense.

Thus, the proximal Newton method generalizes both proximal gradient descent and Newton's method.
