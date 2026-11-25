---
layout: post
title: 02-05 Separating and supporting hyperplanes
chapter: '02'
order: 13
owner: Wontak Ryu
categories:
- chapter02
lang: en
lesson_type: required
---

Here is one of the most powerful geometric miracles in mathematics: if two convex sets do not overlap, you can *always* slide a flat sheet of paper (a hyperplane) cleanly between them. That single fact—the Separating Hyperplane Theorem—is the geometric engine behind Support Vector Machines, Farkas' Lemma, and Strong Lagrange Duality. Its sibling, the Supporting Hyperplane Theorem, guarantees that every boundary point of a convex set admits a tangent flat that keeps the entire set on one side.

## Background Knowledge Map: Separation and Support Geometry

- **Separating Hyperplane Theorem:** For any two disjoint nonempty convex sets $$C, D$$, there exist $$a \neq 0$$ and $$b$$ such that $$a^T x \le b \;\forall x \in C$$ and $$a^T x \ge b \;\forall x \in D$$.
- **Strict Separation:** When $$C$$ and $$D$$ are closed and disjoint and at least one is compact (bounded), we get a strict margin: $$a^T x < b < a^T y$$—constructed directly from the minimum-distance segment between $$C$$ and $$D$$.
- **Supporting Hyperplane Theorem:** At every boundary point $$x_0 \in \partial C$$ of a convex set $$C$$, there exists $$a \neq 0$$ such that $$a^T x \le a^T x_0$$ for all $$x \in C$$ (the geometric origin of subgradients!).
- **Duality Link:** Proving a convex optimization problem has no feasible solution below value $$p^*$$ amounts to separating the epigraph from a target point—yielding the dual multipliers directly as the separating normal $$a$$.

### Step-by-Step Worked Example (Read Slowly): Constructing a Strict Separating & Supporting Hyperplane

Let $$C = \{x \in \mathbb{R}^2 : \|x\|_2 \le 1\}$$ (closed, compact unit disk) and $$x_0 = (3, 4)^T \notin C$$.

1. **Find the closest point $$p \in C$$ to $$x_0$$:** Since $$\|x_0\|_2 = \sqrt{3^2 + 4^2} = 5$$, the projection onto the unit disk is
   $$p = \frac{x_0}{\|x_0\|_2} = \begin{pmatrix} 3/5 \\ 4/5 \end{pmatrix}.$$
2. **Choose the unit separating normal $$u = \frac{x_0 - p}{\|x_0 - p\|_2} = (3/5, 4/5)^T$$:**
   - For every $$x \in C$$, Cauchy–Schwarz gives $$u^T x \le \|u\|_2 \|x\|_2 \le 1 \cdot 1 = 1$$ (with equality at $$x = p$$).
   - At $$x_0 = (3, 4)^T$$, $$u^T x_0 = \frac{3}{5}(3) + \frac{4}{5}(4) = \frac{25}{5} = 5$$.
3. **Read off both hyperplanes immediately:**
   - **Strict separating hyperplane** (midpoint $$b = \frac{1 + 5}{2} = 3$$): $$\frac{3}{5}x_1 + \frac{4}{5}x_2 = 3$$ strictly separates $$C$$ ($$u^T x \le 1 < 3$$) from $$x_0$$ ($$u^T x_0 = 5 > 3$$).
   - **Supporting hyperplane to $$C$$ at $$p$$:** $$\frac{3}{5}x_1 + \frac{4}{5}x_2 = 1$$ touches $$C$$ at $$p = (3/5, 4/5)^T$$ while keeping all of $$C$$ in the halfspace $$u^T x \le 1$$.

This section introduces two theorems that characterize convex sets: the **separating hyperplane theorem** and the **supporting hyperplane theorem**.

## Separating hyperplane theorem

Suppose there are several disjoint convex sets with no intersection. How can we separate them? The simplest way is to draw a line between the sets. This method is widely used in classification and is supported by the **separating hyperplane theorem**.

If there are two disjoint convex sets $$C$$ and $$D$$, then for $$x \in C$$, $$a^T x \le b$$ and for $$x \in D$$, $$a^T x \ge b$$ for some $$a \ne 0$$ and $$b$$. In other words, the affine function $$a^T x - b$$ is nonpositive on $$C$$ and nonnegative on $$D$$. The hyperplane $$\{ x \mid a^T x = b\}$$ is called a **separating hyperplane** for $$C$$ and $$D$$.

The figure below shows a separating hyperplane dividing two disjoint convex sets $$C$$ and $$D$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.05_01_Seperating_hyperplan_theorem.png" alt="[Fig1] Separating hyperplane theorem [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Separating hyperplane theorem [1]</figcaption>
</p>
</figure>

The converse of the separating hyperplane theorem does not hold. That is, the existence of a separating hyperplane does not guarantee that the sets are disjoint. For example, if $$C = D = \{0\} \subseteq \mathbb{R}$$, then $$x = 0$$ separates $$C$$ and $$D$$.

### Strict separation

If the separating hyperplane satisfies the stronger condition $$x \in C$$ implies $$a^T x < b$$ and $$x \in D$$ implies $$a^T x > b$$, this is called **strict separation**. Disjoint closed convex sets do not always require strict separation, but in many cases, this condition holds.

## Supporting hyperplanes theorem

The **supporting hyperplane theorem** states that for any nonempty convex set $$C$$ and any point $$x_0$$ on the boundary **bd** $$C$$, there exists a supporting hyperplane at $$x_0$$.

What is a supporting hyperplane? Suppose $$x_0$$ is a boundary point of $$C$$. If for all $$x \in C$$, $$a^T x \le a^T x_0$$ ($$a \ne 0$$), then the hyperplane $$\{x \mid a^T x = a^T x_0 \}$$ is a **supporting hyperplane** for $$C$$ at $$x_0$$.

[Note] The boundary is defined as $$x_0 \in$$ **bd** $$C = $$ **cl** $$C$$ $$\setminus$$ **int** $$C$$, i.e., the closure minus the interior.

Geometrically, the supporting hyperplane $$\{x \mid a^T x = a^T x_0\}$$ is tangent to $$C$$ at $$x_0$$ and the halfspace $$a^T x \le a^T x_0$$ contains $$C$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.05_02_Supporting_hyperplane_theorem.png" alt="[Fig 2] Supporting hyperplane [1]" width="70%">
  <figcaption style="text-align: center;">[Fig 2] Supporting hyperplane [1]</figcaption>
</p>
</figure>


