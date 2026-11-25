---
layout: post
title: 02-04 Generalized inequalities
chapter: '02'
order: 12
owner: Wontak Ryu
categories:
- chapter02
lang: en
---

When buying a laptop, you want both *lower price* and *longer battery life*. Between Laptop A ($\$1000$, 12h) and Laptop B ($\$1200$, 16h), neither is strictly better in both dimensions—vector comparisons are only *partial* orders! Proper cones formalize vector inequalities $$x \preceq_K y$$ cleanly, explaining the crucial difference between a single utopian **minimum** element and the trade-off frontier of **minimal (Pareto-optimal)** elements.

## Key ideas: Ordering Vectors and Matrices with Cones

- **Proper Cone ($$K$$):** A cone that is convex, closed, solid (nonempty interior), and pointed (contains no full line: $$K \cap (-K) = \{0\}$$)—needed so $$\preceq_K$$ behaves like a genuine partial order.
- **Generalized Inequality ($$x \preceq_K y \iff y - x \in K$$):** Unifies componentwise vector inequalities ($$K = \mathbb{R}_+^n$$) and Loewner matrix inequalities ($$K = \mathbb{S}_+^n$$, where $$X \preceq Y \iff Y - X \succeq 0$$).
- **Strict Inequality ($$x \prec_K y \iff y - x \in \text{int}(K)$$):** Requires $$K$$ to be solid; for matrices, $$X \prec Y$$ means $$Y - X$$ is strictly positive definite.
- **Minimum vs. Minimal Elements:** A *minimum* beats every other point in $$S$$ ($$S \subseteq x + K$$); a *minimal* (Pareto-optimal) point is merely undefeated by any other point in $$S$$ ($$(x - K) \cap S = \{x\}$$).

### Worked example: Minimum vs. Minimal Elements Under $$\mathbb{R}_+^2$$

Consider four cost vectors (e.g., latency and energy) in $$\mathbb{R}^2$$ ordered by $$K = \mathbb{R}_+^2$$:
$$S = \{(1, 4),\; (2, 2),\; (3, 1),\; (3, 3)\}.$$

1. **Test for dominated points:** Compare $$(2, 2)$$ and $$(3, 3)$$:
   $$(3, 3) - (2, 2) = (1, 1) \in \mathbb{R}_+^2 \implies (2, 2) \preceq_{\mathbb{R}_+^2} (3, 3).$$
   Therefore $$(3, 3)$$ is strictly dominated and is **not minimal**.
2. **Check the remaining three points pairwise:**
   - $$(1, 4) - (2, 2) = (-1, 2) \notin \mathbb{R}_+^2 \cup (-\mathbb{R}_+^2)$$ (incomparable).
   - $$(2, 2) - (3, 1) = (-1, 1) \notin \mathbb{R}_+^2 \cup (-\mathbb{R}_+^2)$$ (incomparable).
   - $$(1, 4) - (3, 1) = (-2, 3) \notin \mathbb{R}_+^2 \cup (-\mathbb{R}_+^2)$$ (incomparable).
3. **Conclude:** The set $$S$$ has **three minimal (Pareto-optimal) elements**—$$(1, 4)$$, $$(2, 2)$$, and $$(3, 1)$$—and **no minimum element**, because no single point dominates all others simultaneously.

In one-dimensional real space $$\mathbb{R}$$, given two numbers 1 and 2, we can say 2 is greater than 1. But in $$n$$-dimensional real space $$\mathbb{R}^n$$, given two points $$x_1$$ and $$x_2$$, can we say which is greater? This is not straightforward.

This section introduces **generalized inequalities** for comparing order between two points in $$\mathbb{R}^n$$, and also discusses the concepts of minimum and minimal elements of a set.

## Proper cone

A convex cone $$K \subseteq \mathbb{R}^n$$ is called a **proper cone** if it satisfies:

* K is closed (includes its boundary).
* K is solid (its interior is nonempty).
* K is pointed (does not contain any line) (i.e., $$x \in K, -x \in K \implies x = 0$$).

If a pointed & closed convex cone is defined in a subspace of dimension $$n-1$$ or less, its interior is empty, since it cannot contain an open ball in $$n$$ dimensions. Thus, it is not solid and cannot be a proper cone. For example, a 2D pie-shaped pointed & closed convex cone in $$\mathbb{R}^3$$ is not a proper cone.

See *[Wikipedia: Interior (topology)](https://en.wikipedia.org/wiki/Interior_(topology))* for the definition of interior.

## Generalized inequality

Using a proper cone, we can define a partial ordering in $$\mathbb{R}^n$$ called a **generalized inequality**. It has properties similar to the standard ordering in $$\mathbb{R}$$:

> $$x \preceq_{K} y \iff y − x \in K$$

Similarly, strict partial ordering is defined as:

> $$x \prec_{K} y \iff y − x \in $$ **int** $$K$$

If $$K = \mathbb{R}_{+}$$, then $$\preceq_{K}$$ is the usual $$\le$$ in $$\mathbb{R}$$.

### Properties of generalized inequalities

Generalized inequality $$\preceq_{K}$$ satisfies:

* **Preserved under addition**: if $$x \preceq_{K} y$$ and $$u \preceq_{K} v$$, then $$ x+u \preceq_{K} y +v$$.
* **Transitive**: if $$x \preceq_{K} y$$ and $$y \preceq_{K} z$$ then $$x \preceq_{K}  z$$.
* **Preserved under nonnegative scaling**: if $$x \preceq_{K} y$$ and $$α \ge 0$$ then $$αx \preceq_{K} αy$$.
* **Reflexive**: $$x \preceq_{K} x$$.
* **Antisymmetric**: if $$x \preceq_{K} y$$ and $$y \preceq_{K} x$$, then $$x = y$$.
* **Preserved under limits**: if $$x_i \preceq_{K}  y_i$$ for $$i = 1, 2, ..., x_i \to x$$ and $$y_i \to y$$ as $$i \to ∞$$, then $$x \preceq_{K} y$$.

Strict generalized inequalities have corresponding properties.

## Minimum and minimal elements

The most significant difference between ordering in $$\mathbb{R}$$ and generalized ordering in $$\mathbb{R}^n$$ is **linear ordering**. In $$\mathbb{R}$$, we can compare any two points with $$x \lt y$$ or $$x \gt y$$, but generalized inequality cannot always do this. Therefore, defining the concepts of maximum and minimum in the context of generalized inequality is expected to be much more complex.

### Minimum elements

If $$x \in S$$ satisfies $$x \preceq_{K} y$$ for all $$y \in S$$, then $$x$$ is a **minimum** element of set $$S$$. Similarly, **maximum** can be defined in the same manner. If a minimum exists in a set, it is unique. That is, there exists only one minimum.

If a point $$x \in S$$ is the minimum of $$S$$, then $$S \subseteq x + K$$. Here, $$x + K$$ means that (according to $$\preceq_{K}$$) all points are comparable with $$x$$ and are greater than or equal to $$x$$.

### Minimal elements

A similar concept is **minimal**. If $$x \in S$$ and for all $$y \in S$$, the condition $$y \preceq_{K} x$$ holds only when $$y=x$$, then $$x$$ is a **minimal** element of set $$S$$. Similarly, **maximal** can be defined in the same manner. A set can have multiple minimal elements.

If a point $$x \in S$$ is minimal in $$S$$, then $$(x - K) \cap S = \{x\}$$. Here, $$x - K$$ means that (according to $$\preceq_{K}$$) all points are comparable with $$x$$ and are less than or equal to $$x$$.

In the case of $$K = \mathbb{R}_{+}$$, minimal and minimum are the same and correspond to the general definition of minimum.

### Minimum and minimal in $$\mathbb{R}^2_{+}$$ cone

Consider the $$\mathbb{R}^2_{+}$$ cone $$K$$. The inequality $$x \preceq_{K} y$$ means that $$y$$ is to the upper right of $$x$$. When $$x \in S$$, saying that $$x$$ is the minimum means that all points in $$S$$ are to the upper right of $$x$$. Saying that $$x$$ is minimal means that there are no points in $$S$$ to the lower left of $$x$$.

In the figure below, $$S_1$$ has a minimum $$x_1$$. The set $$x + K$$ is shown in light gray, and since $$S_1 \subseteq x + K$$, $$x_1$$ is the minimum. $$S_2$$ has a minimal element $$x_2$$. The set $$x - K$$ is shown in light gray, and since $$(x - K) \cap S = \{x\}$$, $$x_2$$ is minimal.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_01_Minimum_and_minimal.png" alt="[Fig1] Minimum and minimal elements [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Minimum and minimal elements [1]</figcaption>
</p>
</figure>


