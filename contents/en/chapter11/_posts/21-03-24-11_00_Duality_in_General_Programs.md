---
layout: post
title: 11 Duality in General Programs
chapter: '11'
order: 1
owner: Wontak Ryu
categories:
- chapter11
lang: en
lesson_type: required
---

### Review: duality in linear program

Given $$c \in \mathbb{R}^n$$, $$A \in \mathbb{R}^{m \times n}$$, $$b \in \mathbb{R}^m$$, $$G \in \mathbb{R}^{r \times n}$$, $$h \in \mathbb{R}^r$$, 

#### Primal LP: 
>
$$
\begin{alignat}{1}
\min_{x} & \quad c^T x   \\\\ 
  s.t.   & \quad Ax = b  \\\\
         & \quad Gx \leq h 
\end{alignat}
$$


#### Dual LP: 
>
$$
\begin{alignat}{1}
\max_{u,b} & \quad -b^T u - h^T v   \\\\
         s.t. & \quad - A^T u - G^T v = c  \\\\
             & \quad v \geq 0 
\end{alignat}
$$

### Explanation 1: 

For all $$u$$ and $$v \geq 0$$, and for any primal feasible $$x$$, the following holds. 
>
$$
\begin{equation}
u^T (Ax-b) + v^T(Gx-h) \leq 0
\end{equation}
$$

That is,

>
$$
\begin{equation}
(-A^Tu - G^Tv)^T x \geq -b^Tu - h^T v
\end{equation}
$$

By this relationship, if $$c=-A^Tu - G^Tv$$, we obtain a lower bound on the primal optimum. 


### Explanation 2: 

For all $$u$$ and $$v \geq 0$$, and for any primal feasible $$x$$,

>
$$
\begin{equation}
c^T x \geq c^T x + u^T (Ax-b) + v^T (Gx -h) := L(x,u,v)
\end{equation}
$$

Thus, if $$C$$ is the primal feasible set and $$f^*$$ is the primal optimum, then 

>
$$
\begin{equation}
f^* \geq \min_{x \in C} L(x,u,v) \geq \min_x L(x,u,v) := g(u,v)
\end{equation}
$$

In other words, $$g(u,v)$$ is a lower bound on $$f^*$$. 

>
$$
g(u,v) =
\begin{cases}
-b^T u - h^T v & \text{if $c=-A^Tu - G^T v$} \\\\
-\infty            & \text{otherwise} 
\end{cases}
$$

The second explanation yields the same dual as the first, but it is completely general and applies to arbitrary optimization problems (including nonconvex ones).