---
layout: post
title: 02-02-01 Convex set examples
chapter: '02'
order: 7
owner: Wontak Ryu
categories:
- chapter02
lang: en
---

Convex sets include a variety of forms, from trivial ones like points and lines to hyperplanes, halfspaces, balls, ellipsoids, polyhedra, and cones.


## Hyperplanes

A hyperplane is an $$(n-1)$$-dimensional subset that divides an $$n$$-dimensional space in half, defined as follows. Here, $$a$$ is the normal vector and $$b$$ is the offset from the origin. A hyperplane is both a convex set and an affine set.

> {$$x : a^T x = b$$} with $$ a \in \mathbb{R}^n, a \ne 0, b \in \mathbb{R}$$

In the figure below, any $$x$$ on the hyperplane satisfies that $$(x - x_0)$$ is orthogonal to $$a$$. Thus, $$a^T (x - x_0) = 0$$, so if $$a^T x = b$$, then $$b = a^T x_0$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.05_Hyperplane.png" alt="[Fig1] Hyperplane [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Hyperplane [1]</figcaption>
</p>
</figure>


## Halfspaces

A halfspace is one side of a space divided by a hyperplane. Thus, a single hyperplane $$a^T x = b$$ defines two halfspaces. A halfspace is a convex set but not an affine set.

> {$$x : a^T x \le b$$} or {$$x : a^T x \ge b$$}  with $$ a \in \mathbb{R}^n, a \ne 0, b \in \mathbb{R}$$

For the hyperplane $$a^T x = b$$, the halfspace $$a^T x \ge b$$ is in the direction of the normal vector $$a$$, while $$a^T x \le b$$ is in the direction of $$-a$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.06_Halfspace.png" alt="[Fig2] Halfspace [1]" width="70%">
  <figcaption style="text-align: center;">[Fig2] Halfspace [1]</figcaption>
</p>
</figure>


Note: The interior of $$\{x : a^T x \le b\}$$, that is $$\{x : a^T x \lt b\}$$, is called an open halfspace.


## Euclidean balls

A Euclidean ball is another convex set, defined as follows. ($$\| . \|_2$$ is the Euclidean norm, $$\|u\|_2 = (u^T u)^{1/2}$$.) $$x_c$$ is the center and $$r$$ is the radius. Thus, $$B(x_c, r)$$ contains all points within radius $$r$$ from center $$x_c$$.

> $$B(x_c, r) = \{ x \mid \|x - x_c \|_2 \le r \} = \{ x \mid (x - x_c)^T (x - x_c) \le r^2 \} \text{ with } r \ge 0$$

Alternatively, the Euclidean ball can be expressed as:


> $$B(x_c, r) = \{ x_c + ru \mid \| u \|_2 \le 1 \} $$


## Ellipsoids

An ellipsoid is a convex set related to the Euclidean ball, defined as:

> $$\mathcal{E} = \{x \mid (x - x_c)^T P^{-1} (x - x_c) \le 1 \} $$

Here, $$P = P^T \succ 0$$ means $$P$$ is symmetric and positive definite. The vector $$x_c$$ is the center of the ellipsoid, and the matrix $$P$$ determines how far the ellipsoid extends in each direction from the center. The axes of the ellipsoid are $$\sqrt{\lambda_i}$$, where $$\lambda_i$$ are the eigenvalues of $$P$$. Thus, a ball is a special case of an ellipsoid with $$P = r^2 I$$.

The figure below shows an ellipsoid. The center $$x_c$$ is a point, and the major and minor axes are drawn as line segments.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.07_Ellipsoid.png" alt="[Fig3] Ellipsoid [1]" width="70%">
  <figcaption style="text-align: center;">[Fig3] Ellipsoid [1]</figcaption>
</p>
</figure>


The ellipsoid can also be expressed as:

> $$\mathcal{E} = \{ x_c + Au \mid \|u\|_2 \le 1 \} $$

Here, $$A$$ is a square nonsingular matrix. If $$A = P^{1/2}$$, the expression matches the previous one, and $$A$$ is symmetric and positive definite. If $$A$$ is symmetric positive semidefinite and singular, it is called a degenerate ellipsoid, and its affine dimension equals the rank of $$A$$. A degenerate ellipsoid is still convex.


## Norm balls

A norm ball is the set of points within radius $$r$$ from center $$x_c$$, defined using an arbitrary norm. While a Euclidean ball uses the Euclidean norm, a norm ball can use any norm. If $$\|.\|$$ is any norm on $$\mathbb{R}^n$$, the norm ball is defined as:

> $$ \{ x \mid \|x - x_c \| \le r  \} $$

When the p-norm is defined as:

> $$ \| x  \|_{p} = \left( \sum_{i=0}^n |x_i|^{p} \right)^{1/p} \text{ for  } p \ge 1$$

The shape of the norm ball depends on the value of $$p$$. The figure below shows the shape of the norm ball in 3D for different values of $$p$$. The norm ball is convex if $$p \ge 1$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.07_2_norm_ball.png" alt="[Fig4] Norm ball [1]" width="70%">
  <figcaption style="text-align: center;">[Fig4] Norm ball [1]</figcaption>
</p>
</figure>


The next figure shows the shape of the norm ball in 2D for different values of $$p$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.07_3_norm_ball2.png" alt="[Fig4] Norm ball [2]" width="70%">
  <figcaption style="text-align: center;">[Fig4] Norm ball [2]</figcaption>
</p>
</figure>



## Polyhedra

A polyhedron is defined as the intersection of linear inequalities and equalities. Affine sets (subspaces, hyperplanes, lines), rays, line segments, and halfspaces are all polyhedra. Polyhedra are convex sets, and a bounded polyhedron is called a polytope.

> $$\mathcal{P} = \{ x \mid a^T_i x \le b_i, i = 1, ..., m, c_j^Tx  = d_j, j = 1, ..., p\}$$

A single equality $$c_j^Tx  = d_j$$ can be represented by two inequalities $$c^T_jx \le d_j$$ and $$c^T_jx \ge d_j$$. Thus, polyhedra can be defined using only inequalities.

The figure below shows a pentagonal polyhedron formed by the intersection of five halfspaces, with outward normal vectors $$a_1, ..., a_5$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.09_Polyhedra.png" alt="[Fig5] Polyhedra [1]" width="70%">
  <figcaption style="text-align: center;">[Fig5] Polyhedra [1]</figcaption>
</p>
</figure>


In matrix form, a polyhedron can be defined as:

> $$\mathcal{P} =  \{ x \mid A^Tx \preceq b, C^Tx  = d \}$$
where
$$
A = 
\begin{bmatrix}
a^T_1 \\
\vdots \\
a^T_m
\end{bmatrix}, 
$$
$$
C = 
\begin{bmatrix}
c^T_1 \\
\vdots \\
c^T_p
\end{bmatrix}
$$


#### Simplexes

A simplex is the simplest polygon that can be formed in $$n$$-dimensional space, constructed from $$n+1$$ points.

If there are $$k + 1$$ points $$v_0, ..., v_k \in \mathbb{R}^n$$ that are affinely independent, the simplex is defined as the convex hull of these $$k+1$$ points. Affinely independent means $$v_1 − v_0, ..., v_k − v_0$$ are linearly independent.

> $$C = \mathbb{conv} \{v_0, ... , v_k\} = \{ \theta_0 v_0 + \cdots + \theta_k v_k  \mid \theta \succeq 0, 1^T \theta = 1 \}$$

The figure below shows simplexes from 0 to 3 dimensions: a point in 0D, a line segment in 1D, a triangle in 2D, and a tetrahedron in 3D.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.02_10_Simplex.png" alt="[Fig6] Simplex [source - wikipedia]" width="70%">
  <figcaption style="text-align: center;">[Fig6] Simplex [source - wikipedia]</figcaption>
</p>
</figure>


A common example of a simplex is the probability simplex:

> $$C = \mathbb{conv} \{e_1, ..., e_n \} = \{ \theta \mid \theta \succeq 0, 1^T \theta = 1\}$$
