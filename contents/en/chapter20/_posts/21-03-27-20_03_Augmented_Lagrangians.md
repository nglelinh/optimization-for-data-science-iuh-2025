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

Plain dual ascent has an Achilles' heel: if $$f(x)$$ is not strictly convex (say, a linear program or an $$\ell_1$$ regularizer), the Lagrangian minimizer $$x(u)$$ can jump wildly or even blow up to $$-\infty$$! In 1969, Magnus Hestenes and Michael Powell discovered an astonishingly simple cure—the **Augmented Lagrangian Method (Method of Multipliers)**. Adding the quadratic penalty $$\frac{\rho}{2}\|Ax - b\|_2^2$$ does not change the optimal solution by a single digit (since $$Ax - b = 0$$ at every feasible point!), yet it acts like a mathematical shock absorber: smoothing the dual, restoring convergence without strong convexity, and automatically locking the dual step size to $$t_k = \rho$$!

## Key ideas: Why the Quadratic Augmentation Changes Everything

- **Feasibility-Preserving Penalty:** Because $$\frac{\rho}{2}\|Ax - b\|_2^2 = 0$$ whenever $$Ax = b$$, minimizing $$f(x) + \frac{\rho}{2}\|Ax - b\|_2^2$$ subject to $$Ax = b$$ has the *exact* same optimal set and optimal value as the original problem—unlike pure quadratic penalty methods, which require $$\rho \to \infty$$!
- **Why the Step Size Is Exactly $$\rho$$:** Stationarity of the $$x$$-update gives $$0 \in \partial f(x^{(k)}) + A^T\big(u^{(k-1)} + \rho(Ax^{(k)} - b)\big)$$. Setting $$u^{(k)} = u^{(k-1)} + \rho(Ax^{(k)} - b)$$ makes $$(x^{(k)}, u^{(k)})$$ satisfy dual stationarity $$0 \in \partial f(x^{(k)}) + A^T u^{(k)}$$ *identically at every single iteration*!
- **Smoothing via Moreau Envelope:** The augmented dual function is literally the Moreau–Yosida regularization of the original dual $$g(u)$$, which is *always* continuously differentiable with $$(1/\rho)$$-Lipschitz gradient—even if $$f$$ is linear or nonsmooth!
- **The One Trade-Off (Loss of Separability):** Expanding $$\frac{\rho}{2}\|\sum_i A_i x_i - b\|_2^2$$ introduces cross-terms $$x_i^T A_i^T A_j x_j$$ that re-couple the blocks—setting the stage directly for ADMM in Section 20-04!

### Worked example: Rescuing a Linear Problem Where Dual Ascent Fails

Consider the 1D linear program $$\min_{x \in \mathbb{R}} 2x$$ subject to $$x = 3$$ (trivial optimum $$x^\star = 3, u^\star = -2$$). Notice $$f(x) = 2x$$ is **not** strictly convex!

1. **Watch plain dual ascent fail immediately:**
   The ordinary Lagrangian is $$L(x, u) = (2 + u)x - 3u$$. For *any* $$u \neq -2$$, $$\inf_x L(x, u) = -\infty$$! Plain dual ascent cannot even take step 1 unless you already guessed $$u^0 = -2$$!
2. **Now apply the Augmented Lagrangian Method with $$\rho = 1$$ from $$u^0 = 0$$:**
   $$L_1(x, u) = 2x + u(x - 3) + \frac{1}{2}(x - 3)^2.$$
   - **$$x$$-update:** Differentiate with respect to $$x$: $$2 + u^0 + (x^1 - 3) = 0 \implies x^1 = 3 - 2 - 0 = 1$$ (well-defined and finite!).
   - **$$u$$-update:** $$u^1 = u^0 + \rho(x^1 - 3) = 0 + 1(1 - 3) = -2 = u^\star$$!
3. **Check Iteration 2 at $$u^1 = -2$$:**
   - **$$x$$-update:** $$2 + (-2) + (x^2 - 3) = 0 \implies x^2 = 3 = x^\star$$!
   - **$$u$$-update:** $$u^2 = -2 + 1(3 - 3) = -2$$.
   Where plain dual ascent blew up to $$-\infty$$, the Augmented Lagrangian Method hit the *exact* primal-dual optimum in **two iterations** with finite $$\rho = 1$$!

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
