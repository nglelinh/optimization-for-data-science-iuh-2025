---
layout: post
title: 02-02-02 Convex Cone examples
chapter: '02'
order: 8
owner: Wontak Ryu
categories:
- chapter02
lang: en
---

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

**Positive semidefinite** $$\mathbb{S}^n_+$$의 정의는 다음과 같다. 이때 $$\mathbb{S}^n$$는  $$n × n$$ symmetric matrix이다.
>$$\mathbb{S}^n_+ =$$ { $$ X \in \mathbb{S}^n : X \succeq 0 $$} 

$$\mathbb{S}^n_+$$는  $$\theta_1, \theta_2 \ge 0$$, $$A, B \in  \mathbb{S}^n_+$$이면 $$\theta_1 A + \theta_2 B \in  \mathbb{S}^n_+$$를 만족하기 때문에 convex cone이며 **positive semidefinite cone**이라고 부른다.

다음 그림은 $$S^2_+$$에서의 positive semidefinite cone의 boundary를 $$ (x, y, z) \in R^3$$ 상에서 그린 그림이다. 행렬 $$X$$는 positive semidefinite이기 때문에 determinant가 0이상 이어야 한다.

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


