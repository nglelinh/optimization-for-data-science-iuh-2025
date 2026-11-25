---
layout: post
title: "08-01-07 Example: Intersection of sets"
chapter: '08'
order: 9
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

From reconstructing CT scans that must simultaneously match X-ray measurements and physical density bounds, to finding a portfolio that satisfies both risk caps and regulatory sector limits, engineers constantly face the **convex feasibility problem**: find a single point $$x$$ lying inside the intersection $$C_1 \cap C_2 \cap \dots \cap C_m$$ of several closed convex sets. Remarkably, by rewriting feasibility as minimizing the maximum Euclidean distance to all sets—an objective whose optimal value is known to be $$f^\star = 0$$—Polyak's subgradient method morphs automatically into the classic **alternating projections** algorithm!

## Background Knowledge Map: Convex Feasibility as Nonsmooth Optimization

- **Pillar 1 — Distance-to-Set Function:** For a nonempty closed convex set $$C_i$$, $$d_{C_i}(x) = \min_{y \in C_i} \|x - y\|_2$$ is convex and $$1$$-Lipschitz. Outside $$C_i$$, it is differentiable with unit-length gradient $$\nabla d_{C_i}(x) = \frac{x - P_{C_i}(x)}{\|x - P_{C_i}(x)\|_2}$$, pointing directly away from the unique Euclidean projection $$P_{C_i}(x)$$.
- **Pillar 2 — Pointwise Maximum Formulation:** Defining $$f(x) = \max_{1 \le i \le m} d_{C_i}(x)$$ converts feasibility into $$\min_x f(x)$$. Whenever the intersection is nonempty, $$f^\star = 0$$ is known exactly, unlocking Polyak's step size with zero tuning.
- **Pillar 3 — Active-Set Subgradient Selection:** By Danskin's / pointwise-maximum subdifferential rule, choosing the farthest set $$j \in \arg\max_i d_{C_i}(x^{(k)})$$ yields a valid unit-norm subgradient $$g^{(k)} = \frac{x^{(k)} - P_{C_j}(x^{(k)})}{\|x^{(k)} - P_{C_j}(x^{(k)})\|_2}$$ with $$\|g^{(k)}\|_2 = 1$$.
- **Pillar 4 — Equivalence to Farthest-Set Projection:** Plugging $$f(x^{(k)}) = d_{C_j}(x^{(k)})$$, $$f^\star = 0$$, and $$\|g^{(k)}\|_2 = 1$$ into Polyak's update gives $$x^{(k+1)} = x^{(k)} - d_{C_j}(x^{(k)}) \frac{x^{(k)} - P_{C_j}(x^{(k)})}{d_{C_j}(x^{(k)})} = P_{C_j}(x^{(k)})$$: every Polyak subgradient step is literally an exact Euclidean projection onto the most violated constraint set.

### Step-by-Step Worked Example (Read Slowly): Finding a Point in the Intersection of a Half-Space and a Disk

Let $$C_1 = \{ (x_1, x_2) \in \mathbb{R}^2 : x_1^2 + x_2^2 \le 1 \}$$ (the unit disk) and $$C_2 = \{ (x_1, x_2) \in \mathbb{R}^2 : x_1 \ge 0.5 \}$$ (a right half-space). Start at $$x^{(0)} = (-3, 0)$$.

1. **Iteration 1 at $$x^{(0)} = (-3, 0)$$:**
   - Distance to $$C_1$$: $$P_{C_1}(-3, 0) = (-1, 0)$$, so $$d_{C_1}(x^{(0)}) = \|(-3, 0) - (-1, 0)\|_2 = 2.0$$.
   - Distance to $$C_2$$: $$P_{C_2}(-3, 0) = (0.5, 0)$$, so $$d_{C_2}(x^{(0)}) = \|(-3, 0) - (0.5, 0)\|_2 = 3.5$$.
   - Farthest set is $$C_2$$ ($$f(x^{(0)}) = 3.5$$). The unit subgradient is $$g^{(0)} = \frac{(-3, 0) - (0.5, 0)}{3.5} = (-1, 0)$$.
   - Polyak step size: $$t_1 = \frac{f(x^{(0)}) - 0}{\|g^{(0)}\|_2^2} = \frac{3.5}{1^2} = 3.5$$.
   - Update: $$x^{(1)} = (-3, 0) - 3.5(-1, 0) = (0.5, 0) = P_{C_2}(x^{(0)})$$.
2. **Verify feasibility at $$x^{(1)} = (0.5, 0)$$:**
   - Check $$C_1$$: $$0.5^2 + 0^2 = 0.25 \le 1$$ (inside $$C_1$$, $$d_{C_1} = 0$$).
   - Check $$C_2$$: $$0.5 \ge 0.5$$ (inside $$C_2$$, $$d_{C_2} = 0$$).
   - Thus $$f(x^{(1)}) = 0 = f^\star$$ and $$x^{(1)} \in C_1 \cap C_2$$ in one step! When the sets meet at an angle (e.g., two slanted half-spaces), the exact same rule zig-zags cleanly into $$C_1 \cap C_2$$ while shrinking $$\|x^{(k)} - x^\star\|_2$$ monotonically at every projection.

Suppose we want to find a point in the intersection of several closed convex sets.

First, let $$f_i(x)$$ be the distance from a point $$x$$ to the set $$C_i$$, and let $$f(x)$$ be the maximum of the distances from $$x$$ to all the sets $$C_i, i=1,...,m$$:
>
$$ \begin{align}
f_i(x) & = \mathbb{dist}(x, C_i), \quad i=1,...,m \\
f(x) & = \max_{i=1,...,m}\text{ }f_i(x)
\end{align} $$

Using these two functions, the problem of finding a point in the intersection of the convex sets can be formulated as the following minimization problem:

>
$$ \begin{align}
\min_{x}\text{ }f(x)
\end{align} $$

Finding a point in the intersection of the convex sets is equivalent to finding the point $$x$$ that minimizes the maximum distance $$f(x)$$ to the sets $$C_i$$. In this case, the objective function $$f(x)$$ is convex. If the sets have a common point, then $$f^* = 0$$ and the optimal point is $$x^* \in C_1 \cap C_2 \cap ... \cap C_m$$.

## Gradient of distance function

In [the previous section]({% multilang_post_url contents/chapter07/21-03-25-07_03_05_example_distance_to_convex_set %}), we defined the distance to a convex set as $$dist(x, C_i) = \min_{y \in C} \lVert y-x \rVert _2$$, and saw that its gradient is:

>
$$ \begin{align}
\partial dist(x,C) = \frac{x-P_C(x)}{ \Vert x-P_C(x) \Vert_2}
\end{align} $$

Here, $$P_C(x)$$ is the projection of the point $$x$$ onto the set $$C$$.

## Subdifferential of finite pointwise maximum

The subdifferential of the finite pointwise maximum function $$f(x)=\max_{i=1,...,m}\text{ }f_i(x)$$ is given by

>
$$ \begin{align}
\partial f(x) = \text{conv}\left(\bigcup_{i:f_i(x)=f(x)} \partial f_i(x)\right)
\end{align} $$

That is, the subdifferential of $$f$$ at $$x$$ is the convex hull of the union of the subdifferentials $$\partial f_i(x)$$ of all the functions $$f_i$$ that attain the maximum at $$x$$.

In particular, if $$f_i(x) = f(x)$$ and $$g_i \in \partial f_i(x)$$, then $$g_i \in \partial f(x)$$.

## Deriving subgradient updating steps

As we saw in [the previous section]({% multilang_post_url contents/chapter07/21-03-25-07_03_05_example_distance_to_convex_set %}), $$dist(x, C_i)$$ has the following subgradient:

>$$\text{Recall:}$$
$$ \begin{align}
g_i = \nabla f_i(x) = \frac{x-P_{C_i}(x)}{ \Vert x-P_{C_i}(x) \Vert_2}
\end{align} $$

If the convex sets have a common point, we know right away that $$f^*=0$$, so we can use Polyak step sizes. Since $$x-P_{C_i}(x)$$ is normalized in the subgradient above, $$ \Vert g \Vert_2^{2}=1$$. Substituting these known values into the Polyak step size $$t_k = \frac{f(x^{(k-1)})-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}}$$, we obtain the following subgradient method update (here $$i$$ is an index of a set farthest from $$x^{(k-1)}$$, i.e. $$f_i(x^{(k-1)}) = f(x^{(k-1)})$$):

>
$$ \begin{align}
x^{(k)} & = x^{(k-1)} - t_{k}\cdot g^{(k-1)} \\
& = x^{(k-1)} - \frac{f(x^{(k-1)})-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}} \frac{x^{(k-1)}-P_{C_i}(x^{(k-1)})}{ \Vert x^{(k-1)}-P_{C_i}(x^{(k-1)}) \Vert_2}  \\
& = x^{(k-1)} - f(x^{(k-1)}) \frac{x^{(k-1)}-P_{C_i}(x^{(k-1)})}{ \Vert x^{(k-1)}-P_{C_i}(x^{(k-1)}) \Vert_2}
\end{align} $$

Here the Polyak step size is $$f(x^{(k-1)}) = dist(x^{(k-1)}, C_i) =  \Vert x^{(k-1)}-P_{C_i}(x^{(k-1)}) \Vert_2$$, so the subgradient method simplifies to:

>
$$ \begin{align}
x^{(k)} = P_{C_i}(x^{(k-1)})
\end{align} $$

In pictures, at each step the iterate is projected onto the set that is farthest from it, and this is repeated.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter08/08_01_projection.png" alt="projection" width="60%" height="60%">
</p>
  <figcaption style="text-align: center;">[Fig 2] Alternating Projection Algorithm [10]</figcaption>
</figure>
