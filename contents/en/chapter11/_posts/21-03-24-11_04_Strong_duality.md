---
layout: post
title: 11-4 Strong duality
chapter: '11'
order: 5
owner: Wontak Ryu
categories:
- chapter11
lang: en
lesson_type: required
---

When a problem satisfies $$f^* = g^*$$, this is called **strong duality**. The **Slater condition** is a sufficient condition for strong duality.

## Slater condition: 
If the primal problem is convex and there exists at least one strictly feasible $$x \in \mathbb{R}^n$$, then strong duality holds.
>
$$
\begin{equation}
h_1(x)<0,\dots,h_m(x)<0, \text{ and } l_1(x) = 0,\dots,l_r(x) = 0,
\end{equation}
$$

Important refinement: Strict inequality need not be satisfied when the function is affine.
## Example: Support Vector Machine Dual 
Given $$y \in \{-1,1\}^n$$, $$X \in \mathbb{R}^{n \times p}$$ (where the columns of $$X$$ are $$x_1, ..., x_n$$), the SVM (Support Vector Machine) problem is defined as follows.

>
$$
\begin{alignat}{1}
\min_{\beta, \beta_0, \xi} & \quad \frac{1}{2}\parallel\beta\parallel_2^2 + C \sum_{i=1}^n \xi_i   \\\\
                                  s.t. & \quad \xi_i \geq 0, i=1,\dots,n   \\\\
                                       & \quad y_i(x_i^T \beta + \beta_o) \geq 1 - \xi_i, i=1,\dots,n
\end{alignat}
$$

Using dual variables $$v, w \geq 0$$, let us define the Lagrangian:
>
\begin{equation}
L(\beta,\beta_0,\xi,v,w) = \frac{1}{2} \parallel\beta\parallel\_2^2 + C\sum_{i=1}^n \xi_i - \sum_{i=1}^n v_i \xi_i +  \sum_{i=1}^n w_i (1-\xi_i - y_i(x_i^T\beta + \beta_o))
\end{equation}


By minimizing with respect to $$\beta, \beta_0, \xi$$, we can obtain the following Lagrangian dual function:
>
$$
g(v,w) = 
\begin{cases}
-\frac{1}{2} w^T\tilde{X}\tilde{X}^T w +  1^Tw, &\text{if $w=C1-v, w^Ty=0$} \\\\
-\infty, &\text{otherwise}
\end{cases}
$$

Here $$\tilde{X}=\text{diag}(y) X$$. Therefore, the SVM dual problem (after eliminating the slack variable $$v$$) becomes the following. 
>
$$
\begin{alignat}{1}
\max_{w}  & \quad -\frac{1}{2} w^T\tilde{X}\tilde{X}^T w +  1^Tw \\\\
     s.t. &  \quad 0 \leq w \leq C1, w^Ty = 0
\end{alignat}
$$

Since the primal problem satisfies the Slater condition, strong duality holds. (That is, the objective is convex and the inequality constraints are affine in $$\beta, \beta_0, \xi$$.)



