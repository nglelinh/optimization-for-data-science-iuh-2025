---
layout: post
title: 02-02-01 Ví dụ về tập lồi
chapter: '02'
order: 7
owner: Wontak Ryu
categories:
- chapter02
lang: vi
---

Tập lồi bao gồm nhiều dạng khác nhau, từ những dạng tầm thường như điểm và đường thẳng đến siêu phẳng, nửa không gian, hình cầu, ellipsoid, đa diện và hình nón.


## Siêu phẳng

Siêu phẳng là một tập con $$(n-1)$$ chiều chia không gian $$n$$ chiều thành hai phần, được định nghĩa như sau. Ở đây, $$a$$ là vector pháp tuyến và $$b$$ là độ lệch từ gốc tọa độ. Siêu phẳng vừa là tập lồi vừa là tập affine.

> {$$x : a^T x = b$$} với $$ a \in \mathbb{R}^n, a \ne 0, b \in \mathbb{R}$$

Trong hình dưới đây, bất kỳ $$x$$ nào trên siêu phẳng đều thỏa mãn $$(x - x_0)$$ vuông góc với $$a$$. Do đó, $$a^T (x - x_0) = 0$$, vậy nếu $$a^T x = b$$, thì $$b = a^T x_0$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.05_Hyperplane.png" alt="[Hình1] Siêu phẳng [1]" width="70%">
  <figcaption style="text-align: center;">[Hình1] Siêu phẳng [1]</figcaption>
</p>
</figure>


## Nửa không gian

Nửa không gian là một phía của không gian được chia bởi siêu phẳng. Do đó, một siêu phẳng $$a^T x = b$$ định nghĩa hai nửa không gian. Nửa không gian là tập lồi nhưng không phải tập affine.

> {$$x : a^T x \le b$$} hoặc {$$x : a^T x \ge b$$}  với $$ a \in \mathbb{R}^n, a \ne 0, b \in \mathbb{R}$$

Đối với siêu phẳng $$a^T x = b$$, nửa không gian $$a^T x \ge b$$ nằm theo hướng của vector pháp tuyến $$a$$, trong khi $$a^T x \le b$$ nằm theo hướng của $$-a$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.06_Halfspace.png" alt="[Hình2] Nửa không gian [1]" width="70%">
  <figcaption style="text-align: center;">[Hình2] Nửa không gian [1]</figcaption>
</p>
</figure>


Lưu ý: Phần trong của $$\{x : a^T x \le b\}$$, tức là $$\{x : a^T x \lt b\}$$, được gọi là nửa không gian mở.


### Tính chất quan trọng: Nửa không gian là Lồi

Lấy hai điểm bất kỳ $x_1$ và $x_2$ trong nửa không gian:
- Cả hai đều thỏa mãn: $a^T x_1 \leq b$ và $a^T x_2 \leq b$

Với bất kỳ tổ hợp lồi nào: $x_\theta = \theta x_1 + (1 - \theta)x_2$ với $\theta \in [0, 1]$

Kiểm tra xem điểm này có nằm trong nửa không gian hay không:
$$a^T x_\theta = a^T(\theta x_1 + (1 - \theta)x_2) = \theta(a^T x_1) + (1 - \theta)(a^T x_2) \leq \theta b + (1 - \theta)b = b$$

Vì $x_\theta$ thỏa mãn bất đẳng thức, tất cả các điểm giữa $x_1$ và $x_2$ đều nằm trong nửa không gian → nửa không gian là lồi.


## Hình cầu Euclidean

Hình cầu Euclidean là một tập lồi khác, được định nghĩa như sau. ($$\| . \|_2$$ là chuẩn Euclidean, $$\|u\|_2 = (u^T u)^{1/2}$$.) $$x_c$$ là tâm và $$r$$ là bán kính. Do đó, $$B(x_c, r)$$ chứa tất cả các điểm trong bán kính $$r$$ từ tâm $$x_c$$.

> $$B(x_c, r) = \{ x \mid \|x - x_c \|_2 \le r \} = \{ x \mid (x - x_c)^T (x - x_c) \le r^2 \} \text{ với } r \ge 0$$

Hoặc, hình cầu Euclidean có thể được biểu diễn như:


> $$B(x_c, r) = \{ x_c + ru \mid \| u \|_2 \le 1 \} $$


## Ellipsoid

Ellipsoid là một tập lồi liên quan đến hình cầu Euclidean, được định nghĩa như:

> $$\mathcal{E} = \{x \mid (x - x_c)^T P^{-1} (x - x_c) \le 1 \} $$

Ở đây, $$P = P^T \succ 0$$ có nghĩa là $$P$$ đối xứng và xác định dương. Vector $$x_c$$ là tâm của ellipsoid, và ma trận $$P$$ xác định ellipsoid kéo dài bao xa theo mỗi hướng từ tâm. Các trục của ellipsoid là $$\sqrt{\lambda_i}$$, trong đó $$\lambda_i$$ là các giá trị riêng của $$P$$. Do đó, hình cầu là trường hợp đặc biệt của ellipsoid với $$P = r^2 I$$.

Hình dưới đây cho thấy một ellipsoid. Tâm $$x_c$$ là một điểm, và các trục chính và phụ được vẽ như các đoạn thẳng.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.07_Ellipsoid.png" alt="[Hình3] Ellipsoid [1]" width="70%">
  <figcaption style="text-align: center;">[Hình3] Ellipsoid [1]</figcaption>
</p>
</figure>


Ellipsoid cũng có thể được biểu diễn như:

> $$\mathcal{E} = \{ x_c + Au \mid \|u\|_2 \le 1 \} $$

Ở đây, $$A$$ là ma trận vuông không suy biến. Nếu $$A = P^{1/2}$$, biểu thức khớp với biểu thức trước đó, và $$A$$ đối xứng và xác định dương. Nếu $$A$$ đối xứng nửa xác định dương và suy biến, nó được gọi là ellipsoid suy biến, và chiều affine của nó bằng hạng của $$A$$. Ellipsoid suy biến vẫn là lồi.


## Hình cầu chuẩn

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


### Simplexes

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
