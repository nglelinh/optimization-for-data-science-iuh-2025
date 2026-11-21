---
layout: post
title: "20-01 Dual (sub)gradient methods"
chapter: '20'
order: 2
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

Even when the dual (conjugate) cannot be found in closed form, we can still use a dual-based subgradient or gradient method.

For example, consider the following problem.
>\begin{equation}
\min_x f(x) \text{ subject to } Ax = b
\end{equation}

The dual of this problem is as follows, where $$f^{\ast}$$ is the conjugate of $$f$$.
>\begin{equation}
\max_u -f^{\ast}(-A^T u) - b^T u
\end{equation}

Define $$g(u) = -f^{\ast}(-A^Tu)-b^Tu$$. Then a subgradient of $$g(u)$$ is
>\begin{equation}
\partial g(u) = A \partial f^{\ast}(-A^Tu) - b
\end{equation}

Writing the element of $$\partial f^{\ast}(-A^Tu)$$ as $$x$$, this can be expressed as

>\begin{equation}
\partial g(u) = Ax-b \quad \text{where} \quad x \in \arg\min_z f(z) + u^T A z
\end{equation}

## Dual subgradient method
The **dual subgradient method** maximizes the dual objective. Starting from $$u^{(0)}$$, it repeats the following steps for $$k=1,2,3,\dots$$
> $$
> \begin{alignat}{1}
> x^{(k)} & \in \arg \min_x f(x) + ({u^{(k-1)}})^T A x  \\
> u^{(k)} & = u^{(k-1)} + t_k (A x^{(k)} - b) 
> \end{alignat}
> $$

Here the step sizes $$t_k$$ ($$k=1,2,3,\dots$$) are chosen in the standard way.

#### The strictly convex case
If $$f$$ is strictly convex, then $$f^{\ast}$$ is differentiable.

The algorithm then becomes **dual gradient ascent**, which repeats the following steps for $$k=1,2,3,\dots$$
> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg \min_x f(x) + ({u^{(k-1)}})^T A x  \\
> u^{(k)} & = u^{(k-1)} + t_k (A x^{(k)}-b) 
> \end{alignat}
> $$

The difference from the previous version is that $$x^{(k)}$$ is unique. (Note that the relation with $$\text{argmin}$$ is now "$$=$$" instead of "$$\in$$".)

Again the step sizes $$t_k$$ ($$k=1,2,3,\dots$$) are chosen in the standard way, and when computing the $$\text{argmin}$$ we can apply proximal gradient or acceleration as usual.
