---
layout: post
title: 02-05 Separating and supporting hyperplanes
chapter: '02'
order: 11
owner: Wontak Ryu
categories:
- chapter02
lang: en
---

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

#### Strict separation

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


