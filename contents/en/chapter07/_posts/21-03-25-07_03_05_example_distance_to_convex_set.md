---
layout: post
title: '07-03-05 Example: Distance to a Convex Set'
chapter: '07'
order: 11
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
---


The distance function to a closed convex set $$C$$ is defined as:
>
\begin{alignat}{1}
dist(x,C) & = \min_{y \in C} \| y-x \|_2 \\
      & = \| x-P_C(x) \|_2 \\
      & \geq 0 
\end{alignat}

Here, $$P_C(x)$$ is the projection of the point $$x$$ onto the set $$C$$, i.e., the closest point in $$C$$ to $$x$$. The subgradient of the distance function is:
>
\begin{equation}
\partial dist(x,C) = \{\frac{x-P_C(x)}{ \| x-P_C(x) \|_2}\}
\end{equation}

#### Proof

If $$u=P_C(x)$$, then by the first-order optimality condition,
>
\begin{equation}
(x-u)^T(y-u) \leq 0 \ \text{ for all } y \in C
\end{equation}

Thus,
>
\begin{equation}
C \subseteq H = \{y:(x-u)^T(y-u) \leq 0 \}
\end{equation}

(i) For $$y \in H$$,
>
\begin{equation}
(x-u)^T(y-u) \leq 0
\end{equation}

On the other hand, since $$dist(y,C)\geq 0$$,
>
\begin{equation}
dist(y,C) \geq \frac{(x-u)^T(y-u)}{ \| x-u \|_2} \text{ for all } y \in H
\end{equation}

(ii) For $$y \notin H$$,
>
\begin{equation}
(x-u)^T(y-u) = \| x-u \|_2 \| y-u \|_2 \cos\theta,
\end{equation}

where $$\theta$$ is the angle between $$x-u$$ and $$y-u$$. Then,
>
$$
\eqalign{
dist(y,C) &\geq dist(y,H) \\

&= \| y-u \|_2 \cos \theta \\
&= \frac{(x-u)^T(y-u)}{ \| x-u \|_2} \text{ for all }y \notin H
}
$$

Therefore, from (i) and (ii), for all $$y$$,
>
$$
\eqalign{
dist(y,C) &\geq \frac{(x-u)^T(y-u)}{ \| x-u \|_2} \\
&= \frac{(x-u)^T(y-x+x-u)}{ \| x-u \|_2}\\
& = \| x-u \|_2 + \left(\frac{x-u}{ \| x-u \|_2}\right)^T(y-x)
}
$$

In conclusion, $$dist(x,C)$$ has the following subgradient at $$x$$:
>
$$g=\frac{x-u}{ \| x-u \|_2}=\frac{x-P_C(x)}{ \| x-P_C(x) \|_2} $$

Moreover, the subdifferential $$\partial dist(x,C)$$ contains only one element, so $$dist(x,C)$$ is differentiable and its derivative coincides with the subgradient.
