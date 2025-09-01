---
layout: post
title: 11-2 Lagrange dual function
chapter: '11'
order: 3
owner: Wontak Ryu
categories:
- chapter11
lang: en
---

Let $$C$$ be the primal feasible set and $$f^*$$ the primal optimal value. Minimizing $$L(x,u,v)$$ over all $$x$$ yields the following lower bound.

>
$$
\begin{equation}
f^* \geq \min_{x \in C} L(x,u,v) \geq \min_x L(x,u,v) := g(u,v)
\end{equation}
$$

Here, $$g(u,v)$$ is called the Lagrange dual function and provides a lower bound on $$f^*$$ for any dual feasible $$u\geq 0$$, $$v$$.

For example, in the figure below

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter11/dual-gen_7.png" width="70%">
  <figcaption style="text-align: center;">[Fig 2] Example of Lagrangian dual function[1]</figcaption>
</p>
</figure>


* The dashed horizontal line indicates the function $$f^*$$.
* The dual variable is $$\lambda$$.
* The solid line indicates $$g(\lambda)$$.



## Example: Quadratic Program
####  1) Positive Definite ($$Q \succ 0$$)

Consider the following quadratic problem (here $$Q \succ 0$$)
>
$$
\begin{alignat}{1}
\min_x  & \quad \frac{1}{2}x^T Q x + c^T x \\\\
       s.t. & \quad Ax = b, \\\\
            & \quad x \geq 0
\end{alignat}
$$

Then,

##### Lagrangian:
>
$$
\begin{equation}
L(x,u,v) = \frac{1}{2}x^T Q x + c^T x - u^Tx + v^T (Ax-b)
\end{equation}
$$

##### Lagrangian dual function:

From the expression above, to minimize the Lagrangian function, differentiate with respect to $$x$$ and find $$x^*$$ such that the derivative is zero.
\begin{equation}
Qx - (c-u+A^T v) = 0,
\end{equation}
즉,
\begin{equation}
Qx = (c-u+A^T v)
\end{equation}
이 때, $$Q$$는 positive definite하므로 역행렬이 존재하므로, $$x^*$$를 찾으면, $$x^* = Q^{-1}(c - u + A^Tv)$$ 임을 알 수 있다. 따라서, $$x^*$$를 Lagrangian 함수에 대입을 하면, 아래를 얻을 수 있다.

$$
\begin{alignat}{1}
& (c - u + A^T v)^T (Q^{-1})^T Q Q^{-1}(c - u + A^T v) - (c - u + A^T v)^T Q^{-1} (c - u + A^T v) - b^T v \\\
= & (c - u + A^T v)^T Q^{-1}(c - u + A^T v) - (c - u + A^T v)^T Q^{-1} (c - u + A^T v) - b^T v \\\
= & -\frac{1}{2} (c-u+A^Tv)^T Q^{-1} (c-u+A^T v) - b^T v
\end{alignat}
$$

따라서,
>
$$
\begin{equation}
g(u,v) = \min_x L(x,u,v) = -\frac{1}{2} (c-u+A^Tv)^T Q^{-1} (c-u+A^T v) - b^T v
\end{equation}
$$

For all $$u \geq 0$$ and $$v$$, this corresponds to a lower bound on the primal optimum $$f^*$$.

#### 2) Positive Semidefinite ($$Q \succeq 0$$)
위와 같은문제이나, 이번에는 $$Q \succeq 0$$ 이면,

##### Lagrangian:
>
$$
\begin{equation}
L(x,u,v) = \frac{1}{2}x^T Q x + c^T x - u^Tx + v^T (Ax-b)
\end{equation}
$$

##### Lagrangian dual function:
$$Q$$가 positive definite 할 때 처럼, 아래 식을 만족하는 $$x^*$$를 찾아야 한다.

$$
\begin{equation}
Qx = (c-u+A^T v)
\end{equation}
$$
이 때, $$Q$$는 positive semi-definite이므로 역행렬이 존재하지 않을 수 있다. 따라서, 다음의 두가지 경우를 고려해야 한다.

(1) $$c-u+A^T v \in col(Q)$$. In this case, there exists $$x^*$$ satisfying $$Qx = (c-u+A^T v)$$, which can be found using the generalized inverse $$Q^+$$ (the Moore-Penrose pseudo-inverse, $$Q^+ = (Q^TQ)^{-1}Q^T$$).
(2) $$c-u+A^T v \notin col(Q)$$. In this case, there is no $$x^*$$ satisfying $$Qx = (c-u+A^T v)$$, meaning there is no $$x^*$$ that minimizes $$L(x,u,v)$$, and the minimum of $$L(x,u,v)$$ is $$-\infty$$.

From these two cases, the Lagrangian dual function can be summarized as follows.
>
$$
g(u,v) =
\begin{cases}
-\frac{1}{2} (c-u+A^T v)^T Q^{+} (c - u + A^T v) - b^T v  & \text{if $c-u+A^T v \perp \text{null}(Q)$} \\\\
-\infty  & \text{otherwise}
\end{cases}
$$

For all $$u\geq 0$$, $$v$$ with $$c-u+A^Tv \perp \text{null}(Q)$$, $$g(u,v)$$ is a nontrivial lower bound on $$f^*$$.

## Example: Quadratic Program in 2D

For example, in the following figure, $$f(x_1,x_2)$$ is a quadratic function over variables greater than 0 ($$x\ge0$$), and the dual function $$g(u_1,u_2)$$ is a quadratic function over variables greater than 0 ($$u\ge0$$).

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter11/dual-gen_10.png" width="70%">
  <figcaption style="text-align: center;">[Fig 3] Example of quadratic program in 2D</figcaption>
</p>
</figure>

* The blue point is the optimal dual value, and the red point is the optimal primal value.
* For all $$u>0$$, the dual function $$g(u)$$ provides a lower bound on $$f^*$$.
* The maximum of the dual function $$g(u)$$ matches exactly the value $$f^*$$.
