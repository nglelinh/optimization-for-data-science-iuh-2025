---
layout: post
title: 11-3 Lagrange dual problem
chapter: '11'
order: 4
owner: Wontak Ryu
categories:
- chapter11
lang: en
lesson_type: required
---

Consider the following optimization problem:
>
$$
\begin{alignat}{1}
\min_x & \quad f(x)  \\
s.t.   & \quad h_i(x) \leq 0, i=1,\dots,m  \\
       & \quad l_j(x) = 0, j=1,\dots,r
\end{alignat}
$$

The dual function $$g(u,v)$$ satisfies $$f^* \geq g(u,v)$$ for all $$u\geq 0$$ and $$v$$. Therefore, we can obtain the best lower bound by maximizing $$g(u,v)$$ over all feasible $$u$$ and $$v$$. This is called the Lagrange dual problem. 
>
$$
\begin{alignat}{1}
\max_{u,v} & \quad g(u,v)   \\
           s.t. & \quad u \geq 0
\end{alignat}
$$

Here, if we denote the dual optimal value as $$g^*$$, then $$f^* \geq g^*$$. This is called weak duality. This property always holds even when the primal problem is not convex. Moreover, the dual problem is always a convex optimization problem, even when the primal problem is not convex.

By definition, $$g$$ is concave with respect to $$(u,v)$$, and $$u \geq 0$$ is a convex constraint. Therefore, the dual problem corresponds to a concave maximization problem. 
>
\begin{alignat}{1}
 g(u,v) & = \min_x \{ f(x) + \sum_{i=1}^m u_i h_i(x) + \sum_{j=1}^r v_j l_j(x) \}  \\ 
        & = - \underbrace{\max_x \{ -f(x) - \sum_{i=1}^m u_i h_i(x) - \sum_{j=1}^r v_j l_j(x) \}}_{\text{pointwise maximum of convex functions in $(u,v)$}}
\end{alignat}




## Example: nonconvex quartic minimization
Let us minimize the function $$f(x)=x^4 - 50 x^2 + 100 x$$ subject to $$x \geq -4.5$$.


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter11/dual-gen_13.png" width="70%">
  <figcaption style="text-align: center;">[Fig 4] Example of nonconvex quadratic minimization</figcaption>
</p>
</figure>

In this case, the dual function $$g$$ is as follows: 
>
$$
\begin{equation}
 g(u) = \min_{i=1,2,3} \{F_i^4(u) - 50 F_i^2(u) + 100 F_i(u) \}
\end{equation}
$$

where, for $$i=1,2,3$$, 
>
$$
\begin{alignat}{1}
F_i(u) = & \frac{- a_i}{12\cdot 2^{1/3}} \left( 432(100-u)-(432^2(100-u)^2 - 4\cdot 1200^3)^{1/2} \right )^{1/3} \\ 
           & - 100 \cdot 2^{1/3} \frac{1}{\left( 432(100-u)-(432^2(100-u)^2 - 4\cdot 1200^3)^{1/2} \right )^{1/3}}
\end{alignat}
$$

and $$a_1=1, a_2 = (-1+i\sqrt{3})/2, a_3 = (-1-i \sqrt{3})/2$$.
While it is difficult to determine whether $$g$$ is concave just by looking at the function, we can know that $$g$$ is concave under the convexity property of duality.
