---
layout: post
title: "19-01-02 Proximal Newton method"
chapter: '19'
order: 4
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

In the previous section, we explained that the **proximal Newton method** uses the local Hessian $$\nabla^2 g(x)$$ in place of the spherical curvature $$\frac{1}{t} I$$ in the **proximal gradient descent** formula. The proximal Newton method is an old idea, studied in statistics under the name "local score".

Now let us see how the **proximal Newton method** can be formulated.

## Algorithm
The proximal Newton algorithm consists of finding the direction $$v$$ of the next step and then choosing the step size $$t_k$$.

* Step 1: Starting from the initial point $$x^{(0)}$$, repeat the following steps. ($$k=1,2,3,...$$)

* Step 2: Find the direction $$v$$ of the next step.

> \begin{align}
v^{(k)} & = \underset{v}{\text{argmin}} \ \nabla g(x^{(k-1)})^T v + \frac{1}{2} v^T H^{(k-1)} v + h(x^{(k-1)} + v)
\end{align}

Here $$H^{(k-1)} = \nabla^2 g(x^{(k-1)})$$ is the Hessian of $$g$$ at $$x^{(k-1)}$$.

* Step 3: Choose a step size to move along the direction $$v^{(k)}$$.

> \begin{align}
x^{(k)} & =x^{(k-1)} + t_k v^{(k)}
\end{align}

Here $$t_k$$ is the step size; with $$t_k=1$$ this is the pure proximal Newton method.

Unlike proximal gradient descent, the step size is chosen by backtracking line search.

#### Next position view
If we express the above in terms of the next position $$z$$ rather than the direction $$v$$, we get the following.

> $$
> \begin{align}
> z^{(k)} & = \underset{z}{\text{argmin}} \ \nabla g(x^{(k-1)})^T (z - x^{(k-1)}) + \frac{1}{2} (z - x^{(k-1)})^T H^{(k-1)} (z - x^{(k-1)}) + h(z) \\\\
> x^{(k)} & =x^{(k-1)} + t_k (z^{(k)} - x^{(k-1)} )
> \end{align}
> $$

Intuitively, in the first step we find the surrogate point $$z$$ that minimizes the quadratic model of the objective. We then move from $$x^{(k-1)}$$ in the direction of $$z$$, but we do not always move all the way to $$z$$.
