---
layout: post
title: 02-02-02 Convex Cone examples
chapter: '02'
order: 10
owner: Wontak Ryu
categories:
- chapter02
lang: en
---

When an engineer constrains a robust antenna beamformer or a statistician estimates a valid covariance matrix, scalar inequalities like $$x \ge 0$$ are no longer enough. Convex cones generalize nonnegativity to vectors and matrices: the second-order (norm) cone constrains Euclidean magnitudes, the normal cone captures all outward-pointing optimality directions at a boundary point, and the positive semidefinite cone $$\mathbb{S}_+^n$$ constrains symmetric matrices to have nonnegative eigenvalues.

## Key ideas: The Big Three Convex Cones

- **Norm Cone (Second-Order / Lorentz Cone):** $$C = \{(x, t) \in \mathbb{R}^{n+1} : \|x\| \le t\}$$ turns norm constraints into conic form, powering SOCP formulations for robust regression and portfolio risk.
- **Normal Cone ($$N_C(x)$$):** Collects all vectors $$g$$ making an obtuse angle with feasible directions at $$x \in C$$ ($$g^T(y - x) \le 0$$ for all $$y \in C$$); optimality of a smooth convex problem is simply $$-\nabla f(x^*) \in N_C(x^*)$$.
- **Positive Semidefinite Cone ($$\mathbb{S}_+^n$$):** $$\{X \in \mathbb{S}^n : z^T X z \ge 0 \;\forall z \in \mathbb{R}^n\}$$ is an intersection of infinitely many linear halfspaces in $$X$$, proving immediately that $$\mathbb{S}_+^n$$ is a closed convex cone.
- **Conic Hierarchy:** $$\text{LP } (\mathbb{R}_+^n) \subset \text{SOCP } (\text{Lorentz cone}) \subset \text{SDP } (\mathbb{S}_+^n)$$—each cone unlocks richer modeling power while staying polynomial-time solvable.

### Worked example: Membership and Convexity in the PSD Cone $$\mathbb{S}_+^2$$

Test two symmetric $$2 \times 2$$ matrices:
$$A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}.$$

1. **Check $$A \in \mathbb{S}_+^2$$:** Trace $$= 2 + 2 = 4 > 0$$ and determinant $$= 2(2) - 1^2 = 3 > 0$$ (eigenvalues $$\lambda_1 = 3, \lambda_2 = 1$$). Since both eigenvalues are $$\ge 0$$, $$A \in \mathbb{S}_+^2$$.
2. **Check $$B \in \mathbb{S}_+^2$$:** Determinant $$= 1(1) - 2^2 = -3 < 0$$ (eigenvalues $$3$$ and $$-1$$). Picking $$z = (1, -1)^T$$ gives $$z^T B z = 1 - 4 + 1 = -2 < 0$$, so $$B \notin \mathbb{S}_+^2$$.
3. **Verify convex combination closure inside $$\mathbb{S}_+^2$$:** Combine $$A \in \mathbb{S}_+^2$$ with $$C = \begin{pmatrix} 4 & 0 \\ 0 & 0 \end{pmatrix} \in \mathbb{S}_+^2$$ at $$\theta = 0.5$$:
   $$M = 0.5 A + 0.5 C = \begin{pmatrix} 3 & 0.5 \\ 0.5 & 1 \end{pmatrix}.$$
   Its trace is $$4 > 0$$ and determinant is $$3(1) - 0.25 = 2.75 > 0$$, confirming $$M \in \mathbb{S}_+^2$$.

Examples of convex cones include the norm cone, normal cone, and positive semidefinite cone.

## Norm cone

A **norm cone** is a cone defined by all points $$(x, t)$$ such that $$\| x \| \le t$$ in $$\mathbb{R}^{n+1}$$, where the norm can be arbitrary.

> $$C = \{(x, t) : \| x \| \le t\} \subseteq \mathbb{R}^{n+1}$$, for a norm $$\|·\|$$

The figure below shows the norm cone for the $$l_2$$ norm $$\|·\|_2$$, also called the second-order cone or ice cream cone.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.08_Norm_Cone.png" alt="[Fig1] Norm Cone [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Norm Cone [1]</figcaption>
</p>
</figure>

## Normal Cone

For a set $$C$$ and a point $$x \in C$$, the **normal cone** is defined as:

> $$N_C(x) = \{ g: g^T (y - x) \le 0, \text{ for all } y \in C \}$$

The normal cone consists of all vectors $$g$$ such that the inner product with $$y-x$$ is always less than or equal to zero for all $$y \in C$$. This means the angle between $$g$$ and $$y-x$$ is between 90 and 270 degrees (i.e., $$\cos\theta < 0$$).

* If $$x$$ is on the boundary, the only $$g$$ is the normal of the supporting hyperplane.
* If $$x$$ is a vertex, there are multiple supporting hyperplanes, so $$g$$ forms a pie shape.
* If $$x$$ is in the interior, the only $$g$$ is the zero vector.

The figure below shows the normal vector.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.04_2_Normal_Cone.png" alt="[Fig2] Normal Cone [3]" width="70%">
  <figcaption style="text-align: center;">[Fig2] Normal Cone [3]</figcaption>
</p>
</figure>


## Positive semidefinite cone

The **positive semidefinite cone** $$\mathbb{S}^n_+$$ is defined as follows, where $$\mathbb{S}^n$$ represents $$n \times n$$ symmetric matrices:

> $$\mathbb{S}^n_+ = \{ X \in \mathbb{S}^n : X \succeq 0 \}$$

$$\mathbb{S}^n_+$$ is a convex cone because for $$\theta_1, \theta_2 \ge 0$$ and $$A, B \in \mathbb{S}^n_+$$, we have $$\theta_1 A + \theta_2 B \in \mathbb{S}^n_+$$. This is called the **positive semidefinite cone**.

The following figure shows the boundary of the positive semidefinite cone in $$\mathbb{S}^2_+$$ plotted in $$(x, y, z) \in \mathbb{R}^3$$. Since matrix $$X$$ is positive semidefinite, its determinant must be non-negative.

$$
X = 
\begin{bmatrix}
x, y \\\
y, z
\end{bmatrix}
\in \mathbb{S}^2_+ \iff x \ge 0, z \ge 0, xz \ge y^2$$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.10_Positive_Semidefinite_Cone.png" alt="[Fig3] Positive semidefinite cone [1]" width="70%">
  <figcaption style="text-align: center;">[Fig3] Positive semidefinite cone [1]</figcaption>
</p>
</figure>


