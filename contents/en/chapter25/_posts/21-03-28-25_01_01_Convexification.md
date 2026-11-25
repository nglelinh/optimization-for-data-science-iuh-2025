---
layout: post
title: 25-01-01 Convexification
chapter: '25'
order: '3'
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

At its deepest geometric level, every integer linear program is secretly just a linear program in disguise! By Meyer’s theorem, the convex hull of the integer points inside any rational polyhedron $$P = \{x : Ax \le b\}$$ is itself a polyhedron $$\operatorname{conv}(P \cap \mathbb{Z}^n)$$ whose vertices are all integer vectors. If you could hand an LP solver the linear inequalities describing $$\operatorname{conv}(P \cap \mathbb{Z}^n)$$, simplex would return the exact integer optimum on the very first run. Convexification is the formal theory of how close we can get to that ideal polyhedron.

## Background Knowledge Map: Convex Hulls and Polyhedral Theory for ILPs

- **Equivalence Over the Convex Hull:** Because a linear objective $$c^\top x$$ achieves its minimum over a compact set $$S$$ at an extreme point of $$\operatorname{conv}(S)$$, minimizing $$c^\top x$$ over $$S = P \cap \mathbb{Z}^n$$ yields the exact same optimal value and extreme-point optima as minimizing $$c^\top x$$ over $$\operatorname{conv}(S)$$.
- **Meyer’s Theorem (Rational Polyhedra):** Whenever $$A$$ and $$b$$ have rational entries, $$\operatorname{conv}(\{x \in \mathbb{Z}^n : Ax \le b\})$$ is a polyhedron—meaning it can be represented by a *finite* system of linear inequalities $$\tilde{A}x \le \tilde{b}$$.
- **Why We Cannot Write Down $$\operatorname{conv}(S)$$ Explicitly:** Although finite, the number of facet-defining inequalities of $$\operatorname{conv}(S)$$ is typically exponential in $$n$$ (for example, in the Traveling Salesman Problem).
- **Local Convexification via Cutting Planes:** We never need the entire convex hull—only the few facets active near the optimal face! Cutting planes build this local polyhedral description on demand.

### Step-by-Step Worked Example (Read Slowly): Explicitly Computing $$\operatorname{conv}(P \cap \mathbb{Z}^2)$$

Let $$P = \{(x_1, x_2) \in \mathbb{R}_{\ge 0}^2 : x_1 + 2 x_2 \le 3,\ 2 x_1 + x_2 \le 3.5\}$$. Let us find $$P \cap \mathbb{Z}^2$$ and its exact convexification $$\operatorname{conv}(P \cap \mathbb{Z}^2)$$.

1. **List all integer points in $$P$$:**
   - For $$x_2 = 0$$: $$x_1 \le 3$$ and $$2x_1 \le 3.5 \implies x_1 \in \{0, 1\}$$. Points: $$(0, 0), (1, 0)$$.
   - For $$x_2 = 1$$: $$x_1 \le 1$$ and $$2x_1 \le 2.5 \implies x_1 \in \{0, 1\}$$. Points: $$(0, 1), (1, 1)$$.
   - For $$x_2 = 2$$: $$x_1 + 4 \le 3$$ has no nonnegative solution.
   Thus $$S = P \cap \mathbb{Z}^2 = \{(0, 0), (1, 0), (0, 1), (1, 1)\}$$.
2. **Identify the convex hull $$\operatorname{conv}(S)$$:** The convex hull of those 4 lattice points is simply the unit square:
   $$\operatorname{conv}(S) = \{(x_1, x_2) : 0 \le x_1 \le 1,\ 0 \le x_2 \le 1\}.$$
3. **Compare LP vertices before and after convexification:**
   - Original $$P$$ had fractional vertices $$(1.75, 0)$$, $$(0, 1.5)$$, and $$(4/3, 5/6)$$.
   - Convexified $$\operatorname{conv}(S)$$ has only integer vertices $$(0,0), (1,0), (0,1), (1,1)$$.
   Any linear objective $$c_1 x_1 + c_2 x_2$$ minimized over $$\operatorname{conv}(S)$$ is now guaranteed to hit an integer optimum immediately via ordinary LP!

Transforming an integer program into an equivalent convex problem is called convexification. When convexification is performed, the feasible set becomes a polyhedron, making it easy to find valid cutting planes for the cutting plane algorithm.

## Convexification

To convexify an integer program, the objective function must be linear. In this case, the constraints of the integer program consist of a convex set $$C$$ and an integer set $$\{x_j\}$$.

>$$
>\begin{align}
>\min_{x} & \quad c^{T}x \\
>\text{subject to } & \quad x \in C \\
>& \quad x_j \in \mathbb{Z}, \quad j \in J \\
>\end{align}
>$$

In this case, the feasible set can be redefined as the convex hull $$S := \text{conv} \left \{ x \in C : x_j \in \mathbb{Z}, j \in J \right \}$$. Using the feasible set defined by this convex hull $$S$$, we can define a convex problem equivalent to the original problem as follows. This process is called convexification.

>$$
>\begin{align}
>\min_{x} & \quad c^{T}x \\
>\text{subject to } & \quad x \in S \\
>\end{align}
>$$

In the figure below, the blue region is $$C$$, the red points are $$\{x_j\}$$, and the convex hull $$S$$ formed by these two sets is the red region.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_cutting_plane_concept.png" alt="[Fig1] Cutting Plane">
  <figcaption style="text-align: center;">[Fig1] Cutting Plane</figcaption>
</p>
</figure>

Source: https://commons.wikimedia.org/wiki/File:Cutting_plane_algorithm2.png

<br><br>

The reason these two formulations are equivalent is because the objective function is linear.

## Special case: integer linear programs

Let's apply the above convexification process to the following integer linear program.

>$$
>\begin{align}
>\min_{x} & \quad c^{T}x \\
>\text{subject to } & \quad Ax \le b \\
>& \quad x_j \in \mathbb{Z}, \quad j \in J \\
>\end{align}
>$$

The convex hull $$S$$ of the integer linear program is defined as follows:

>**Theorem**: If $$A, b$$ are rational numbers, then the following set is a polyhedron.
>
>$$S := \text{conv} \left \{ x : Ax \le b, x_j \in \mathbb{Z}, j \in J \right \}$$

So is an integer linear program a linear program? Of course it is. However, in this case, the polyhedron $$S$$ can become a very complex polyhedron with an exponentially large number of inequalities. Therefore, generally, we need to solve the problem using different methods than those used to solve linear programs.