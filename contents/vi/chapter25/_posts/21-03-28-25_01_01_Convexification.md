---
layout: post
title: 25-01-01 Convexification
chapter: '25'
order: 3
owner: YoungJae Choung
categories:
- chapter25
lang: vi
---

Transforming an integer program into an equivalent convex problem is called convexification. When convexification is performed, the feasible set becomes a polyhedron, making it easy to find valid cutting planes for the cutting plane algorithm.

## Convexification
To convexify an integer program, the objective function must be linear. In this case, the constraints of the integer program consist of a convex set $$C$$ and an integer set $${x_j}$$.

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\
> \text{subject to } & \quad  x \in C \\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\
> \end{align}
> $$

In this case, the feasible set can be redefined as the convex hull $$S := \text{conv} \left \{ x \in C : x_j \in \mathbb{Z}, j \in J \right \}$$. Using the feasible set defined by this convex hull $$S$$, we can define a convex problem equivalent to the original problem as follows. This process is called convexification. 

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\
> \text{subject to } & \quad  x \in S \\
> \end{align}
> $$

In the figure below, the blue region is $$C$$, the red points are $${x_j}$$, and the convex hull $$S$$ formed by these two sets is the red region.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_cutting_plane_concept.png" alt="[Fig1] Cutting Plane">
  <figcaption style="text-align: center;">[Fig1] Cutting Plane</figcaption>
</p>
</figure>
출처: https://commons.wikimedia.org/wiki/File:Cutting_plane_algorithm2.png <br><br>

The reason these two formulations are equivalent is because the objective function is linear. 

## Special case: integer linear programs
Let's apply the above convexification process to the following integer linear program.

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\
> \text{subject to } & \quad  Ax \le b \\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\
> \end{align}
> $$

The convex hull $$S$$ of the integer linear program is defined as follows:

> **Theorem**: If $$A, b$$ are rational numbers, then the following set is a polygon.
$$S := \text{conv} \left \{ x : Ax \le b,  x_j \in \mathbb{Z}, j \in J \right \}$$

So is an integer linear program a linear program? Of course it is. However, in this case, the polyhedron $$S$$ can become a very complex polygon with an exponentially large number of inequalities. Therefore, generally, we need to solve the problem using different methods than those used to solve linear programs.
