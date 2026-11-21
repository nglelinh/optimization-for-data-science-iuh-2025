---
layout: post
title: "20-03 Augmented Lagrangians"
chapter: '20'
order: 7
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

A drawback of dual ascent is that it needs strong conditions to guarantee convergence. (To guarantee convergence, $$f$$ had to be strongly convex.) This drawback can be remedied by the **augmented Lagrangian method** (also called the **method of multipliers**).

We transform the primal problem as follows.
>\begin{equation}
\min_x f(x) + \frac{\rho}{2} \lVert Ax - b \rVert _2^2 \quad \text{ subject to } \quad Ax = b
\end{equation}

Here $$\rho > 0$$. If $$A$$ has full column rank, the objective is strongly convex. The new problem is exactly equivalent to the original one (the augmented term $$Ax - b$$ is zero at every feasible point).

## Augmented Lagrangian Method
**Dual gradient ascent** on this problem repeats the following for $$k=1,2,3,\dots$$
> $$
> \begin{alignat}{1}
> x^{(k)} & \in \arg\min_x f(x) + (u^{(k-1)})^T A x + \frac{\rho}{2} \lVert Ax - b \rVert_2^2  \\
> u^{(k)} & = u^{(k-1)} + \rho (A x^{(k)} - b)
> \end{alignat}
> $$

In this dual algorithm, $$\rho$$ plays the role of the step size, i.e. $$t_k=\rho$$. To see why, consider the following.

#### Why $$\rho$$ is a suitable step size

Since $$x^{(k)}$$ minimizes $$f(x) + (u^{(k-1)})^T Ax + \frac{\rho}{2} \lVert Ax - b\rVert _2^2$$,
the stationarity condition says that the subgradient of the objective at $$x^{(k)}$$ must contain $$0$$:

> $$
> \begin{alignat}{1}
> 0 & \in \partial f(x^{(k)}) + A^T \left( u^{(k-1)} + \rho (A x^{(k)} -b) \right)  \\
>   & = \partial f(x^{(k)}) + A^T u^{(k)}
> \end{alignat}
> $$

So with the update $$u^{(k)} = u^{(k-1)} + \rho (A x^{(k)} - b)$$, $$x^{(k)}$$ minimizes the Lagrangian $$f(x) + (u^{(k)})^T A x$$ exactly as the dual stationarity condition requires. Under suitable conditions, $$Ax^{(k)}-b$$ approaches $$0$$, so the iterates become feasible, the KKT conditions are eventually satisfied, and $$x^{(k)}$$ and $$u^{(k)}$$ approach optimality.

The advantage of the **augmented Lagrangian method** is its much better convergence; its drawback is that it loses the decomposability of the problem.
