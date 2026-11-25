---
layout: post
title: '07-03-05 Example: Distance to a Convex Set'
chapter: '07'
order: 11
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
---

Suppose a drone flies outside a convex safe-flight corridor $$C$$ and needs to know the fastest direction back to safety. Its distance to the corridor is $$\operatorname{dist}(x, C) = \min_{y \in C} \|x - y\|_2 = \|x - P_C(x)\|_2$$. Remarkably, this distance function is convex, smooth everywhere *outside* $$C$$ with a unit-length gradient pointing straight away from its projection $$P_C(x)$$, and nonsmooth right on the boundary of $$C$$!

## Background Knowledge Map: Convexity and Subgradients of the Distance Function

1. **Convexity via Partial Minimization**: Because $$h(x, y) = \|x - y\|_2$$ is jointly convex in $$(x, y)$$ and $$C$$ is a closed convex set, the partial minimum $$\operatorname{dist}(x, C) = \min_{y \in C}\|x - y\|_2$$ is guaranteed to be convex in $$x$$. Moreover, the closest point $$P_C(x) = \arg\min_{y \in C}\|x - y\|_2$$ is always **unique** (strict convexity of $$\|\cdot\|_2^2$$).
2. **Projection Optimality (Obtuse-Angle Theorem)**: By Chapter 04's first-order optimality applied to $$\frac{1}{2}\|x - y\|_2^2$$ over $$y \in C$$, $$u = P_C(x)$$ if and only if
   $$(x - u)^T (y - u) \le 0 \quad \text{for all } y \in C$$
   (equivalently, $$x - P_C(x) \in N_C(P_C(x))$$).
3. **Exact Subgradient Outside $$C$$**: For any $$x \notin C$$, $$\operatorname{dist}(x, C)$$ is actually **differentiable** with unit-norm gradient:
   $$\nabla \operatorname{dist}(x, C) = \frac{x - P_C(x)}{\|x - P_C(x)\|_2}.$$
   Moving opposite this gradient walks in a straight line directly toward the closest safe point $$P_C(x)$$!
4. **Subdifferential Inside and on the Boundary of $$C$$**: For $$x \in C$$, $$\operatorname{dist}(x, C) = 0$$ is minimized, so $$0 \in \partial \operatorname{dist}(x, C)$$. Specifically, $$\partial \operatorname{dist}(x, C) = N_C(x) \cap B_2(0, 1)$$ (outward normal vectors of length at most 1).

### Step-by-Step Worked Example (Read Slowly): Computing Projection and Subgradient for a Disk

Let $$C = \{y \in \mathbb{R}^2 : \|y\|_2 \le 2\}$$ be the closed disk of radius $$2$$ centered at the origin, and evaluate $$\operatorname{dist}(x, C)$$ and its subgradient at $$x = (3, 4)$$.

1. **Find the Euclidean projection $$P_C(x)$$**:
   - Since $$\|x\|_2 = \sqrt{3^2 + 4^2} = 5 > 2$$, $$x$$ lies outside $$C$$.
   - Scaling $$x$$ radially down to radius $$2$$ gives
     $$P_C(x) = \frac{2}{5}(3, 4) = (1.2,\; 1.6).$$
2. **Compute the distance and gradient vector $$g$$**:
   - Displacement: $$x - P_C(x) = (3 - 1.2,\; 4 - 1.6) = (1.8,\; 2.4)$$.
   - Distance: $$\operatorname{dist}(x, C) = \sqrt{1.8^2 + 2.4^2} = \sqrt{3.24 + 5.76} = \sqrt{9} = 3$$ (which also equals $$5 - 2 = 3$$!).
   - Gradient:
     $$g = \frac{x - P_C(x)}{\|x - P_C(x)\|_2} = \frac{(1.8, 2.4)}{3} = (0.6,\; 0.8).$$
3. **Verify the subgradient inequality at a test point $$z = (0, 2) \in C$$**:
   - Left-hand side: $$\operatorname{dist}(z, C) = 0$$.
   - Right-hand side: $$\operatorname{dist}(x, C) + g^T(z - x) = 3 + (0.6, 0.8)\cdot(-3, -2) = 3 + (-1.8 - 1.6) = -0.4$$.
   - Indeed $$0 \ge -0.4$$! And checking the obtuse-angle property: $$(x - P_C(x))^T(z - P_C(x)) = (1.8, 2.4)\cdot(-1.2, 0.4) = -2.16 + 0.96 = -1.2 \le 0$$.

The distance function to a closed convex set $$C$$ is defined as:
>
\begin{alignat}{1}
dist(x,C) & = \min_{y \in C} \| y-x \|_2 \\
      & = \| x-P_C(x) \|_2 \\
      & \geq 0 
\end{alignat}

Here, $$P_C(x)$$ is the projection of the point $$x$$ onto the set $$C$$, i.e., the closest point in $$C$$ to $$x$$. The subgradient of the distance function is:
>
\begin{equation}
\partial dist(x,C) = \{\frac{x-P_C(x)}{ \| x-P_C(x) \|_2}\}
\end{equation}

### Proof

If $$u=P_C(x)$$, then by the first-order optimality condition,
>
\begin{equation}
(x-u)^T(y-u) \leq 0 \ \text{ for all } y \in C
\end{equation}

Thus,
>
\begin{equation}
C \subseteq H = \{y:(x-u)^T(y-u) \leq 0 \}
\end{equation}

(i) For $$y \in H$$,
>
\begin{equation}
(x-u)^T(y-u) \leq 0
\end{equation}

On the other hand, since $$dist(y,C)\geq 0$$,
>
\begin{equation}
dist(y,C) \geq \frac{(x-u)^T(y-u)}{ \| x-u \|_2} \text{ for all } y \in H
\end{equation}

(ii) For $$y \notin H$$,
>
\begin{equation}
(x-u)^T(y-u) = \| x-u \|_2 \| y-u \|_2 \cos\theta,
\end{equation}

where $$\theta$$ is the angle between $$x-u$$ and $$y-u$$. Then,
>
$$
\eqalign{
dist(y,C) &\geq dist(y,H) \\

&= \| y-u \|_2 \cos \theta \\
&= \frac{(x-u)^T(y-u)}{ \| x-u \|_2} \text{ for all }y \notin H
}
$$

Therefore, from (i) and (ii), for all $$y$$,
>
$$
\eqalign{
dist(y,C) &\geq \frac{(x-u)^T(y-u)}{ \| x-u \|_2} \\
&= \frac{(x-u)^T(y-x+x-u)}{ \| x-u \|_2}\\
& = \| x-u \|_2 + \left(\frac{x-u}{ \| x-u \|_2}\right)^T(y-x)
}
$$

In conclusion, $$dist(x,C)$$ has the following subgradient at $$x$$:
>
$$g=\frac{x-u}{ \| x-u \|_2}=\frac{x-P_C(x)}{ \| x-P_C(x) \|_2} $$

Moreover, the subdifferential $$\partial dist(x,C)$$ contains only one element, so $$dist(x,C)$$ is differentiable and its derivative coincides with the subgradient.
