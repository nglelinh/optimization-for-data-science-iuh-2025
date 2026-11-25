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

In statistics, minimizing a locally quadratic approximation to a log-likelihood plus a penalty has been used for decades under names like *local scoring* and *iteratively reweighted least squares (IRLS)*. In convex optimization, Lee, Sun, and Saunders unified these ideas into the **Proximal Newton Method**: at every iterate $$x^{(k-1)}$$, form the exact second-order Taylor model of $$g$$, add $$h(x^{(k-1)} + v)$$, solve for the descent direction $$v^{(k)}$$, and damp with a line-search step $$t_k$$.

## Background Knowledge Map: Anatomy of the Proximal Newton Iteration

- **Composite Quadratic Subproblem:** The search direction $$v^{(k)} = \arg\min_v \nabla g(x^{(k-1)})^T v + \frac{1}{2} v^T H^{(k-1)} v + h(x^{(k-1)} + v)$$ minimizes the true second-order model of $$g$$ coupled with the exact nonsmooth penalty $$h$$.
- **Guaranteed Descent Direction:** Whenever $$H^{(k-1)} \succ 0$$ and $$v^{(k)} \neq 0$$, optimality of the subproblem proves $$\nabla g(x)^T v + h(x + v) - h(x) \le -v^T H v < 0$$, guaranteeing that $$v^{(k)}$$ is a strict descent direction for $$f = g + h$$!
- **Fixed-Point Optimality Characterization:** $$v^{(k)} = 0$$ if and only if $$0 \in \nabla g(x^{(k-1)}) + \partial h(x^{(k-1)})$$, meaning $$x^{(k-1)}$$ is already a global minimizer of $$f$$.
- **Why Damping ($$t_k \in (0, 1]$$) Is Essential:** Just like classical Newton's method on $$e^x - 4x$$, taking a full unit step $$t_k = 1$$ far from the solution can overshoot and increase $$f$$; pairing $$v^{(k)}$$ with backtracking guarantees global convergence while still accepting $$t_k = 1$$ near $$x^\star$$.

### Step-by-Step Worked Example (Read Slowly): One Proximal Newton Direction on a Non-Quadratic Objective

Consider the 1D non-quadratic composite objective $$f(x) = \underbrace{e^x - 4x}_{g(x)} + \underbrace{|x|}_{h(x)}$$ starting at $$x^0 = 0$$ (where $$f(0) = 1$$). Note the exact optimum satisfies $$e^{x^\star} - 4 + 1 = 0 \implies x^\star = \ln 3 \approx 1.0986$$ with $$f(x^\star) = 3 - 3\ln 3 \approx -0.2958$$.

1. **Compute local gradient and Hessian of $$g$$ at $$x^0 = 0$$:**
   $$g'(0) = e^0 - 4 = -3, \qquad H^{(0)} = g''(0) = e^0 = 1.$$
2. **Form and solve the proximal Newton subproblem:**
   $$v^{(1)} = \arg\min_v \; -3v + \frac{1}{2}(1)v^2 + |0 + v|.$$
   Test $$v > 0$$: derivative is $$-3 + v + 1 = 0 \implies v^{(1)} = 2$$ (valid since $$2 > 0$$).
3. **Verify the descent-direction inequality:**
   $$\nabla g(0)^T v^{(1)} + h(0 + v^{(1)}) - h(0) = (-3)(2) + 2 - 0 = -4 = -(v^{(1)})^T H^{(0)} v^{(1)} < 0 \quad \checkmark$$
4. **Check why a full unit step $$t = 1$$ overshoots here:**
   At $$x^0 + v^{(1)} = 2$$, $$f(2) = e^2 - 8 + 2 = e^2 - 6 \approx +1.3891 > f(0) = 1.0000$$!
   The direction $$v^{(1)} = +2$$ points directly toward $$x^\star \approx 1.0986$$, but because $$e^x$$ curves up sharply past $$x = 1$$, we must damp $$t_1 < 1$$ via backtracking (which we will compute explicitly in Lesson 19-02!).

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
