---
layout: post
title: "20 Dual Methods"
chapter: '20'
order: 1
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

Imagine coordinating a thousand power generators across a continent to meet a single shared electricity demand $$\sum_{i=1}^{1000} x_i = b$$. Solving the coupled primal problem in one central computer requires gathering every plant's private cost curve $$f_i(x_i)$$ into one giant matrix. **Dual methods** flip the script using the timeless logic of economics: broadcast a single **price** $$u$$ for the shared constraint, let every generator optimize its own cost independently in parallel, and then nudge the price up or down based on whether total supply fell short or overshot $$b$$. This chapter traces that idea from raw dual ascent all the way to the **Augmented Lagrangian** and **ADMM**.

## Background Knowledge Map: The Ladder of Dual Optimization Methods

- **Dual Ascent & Conjugate Smoothness:** Converting $$\min f(x) \text{ s.t. } Ax = b$$ into $$\max_u -f^\ast(-A^T u) - b^T u$$ turns hard equality constraints into an unconstrained dual problem whose gradient is simply the constraint residual $$A x(u) - b$$ (whenever $$f$$ is strictly convex).
- **Dual Decomposition (Parallel Pricing):** When $$f(x) = \sum_{i=1}^B f_i(x_i)$$ is separable across blocks, fixing the dual price $$u$$ completely decouples the primal minimization into $$B$$ independent subproblems—enabling distributed optimization across servers or agents.
- **Augmented Lagrangian (Method of Multipliers):** Plain dual ascent demands strong convexity of $$f$$ and careful step sizes to converge. Adding the quadratic penalty $$\frac{\rho}{2}\|Ax - b\|_2^2$$ smooths the dual dramatically and guarantees convergence under far weaker assumptions—at the cost of coupling the blocks together.
- **ADMM (Best of Both Worlds):** Alternating minimization over $$x$$ and $$z$$ in an augmented Lagrangian restores block separability while keeping the robust convergence guarantees of the method of multipliers.

### Step-by-Step Worked Example (Read Slowly): Pricing a 2-Agent Resource Split via Dual Ascent

Minimize $$\frac{1}{2}x_1^2 + \frac{1}{2}(2x_2^2)$$ subject to $$x_1 + x_2 = 3$$ (exact optimum: $$x_1^\star = 2, x_2^\star = 1, u^\star = -2$$).

1. **Form the Lagrangian and decouple the primal minimizers for any price $$u$$:**
   $$L(x_1, x_2, u) = \left(\tfrac{1}{2}x_1^2 + u x_1\right) + \left(x_2^2 + u x_2\right) - 3u.$$
   Minimizing independently gives $$x_1(u) = -u$$ and $$x_2(u) = -\frac{u}{2}$$.
2. **Take one dual ascent step from $$u^0 = 0$$ with step size $$t = 1$$:**
   - Primal response at $$u^0 = 0$$: $$x_1^1 = 0, \; x_2^1 = 0$$.
   - Constraint residual: $$r^1 = x_1^1 + x_2^1 - 3 = -3$$ (shortfall of 3 units!).
   - Price update: $$u^1 = u^0 + t(r^1) = 0 + 1(-3) = -3$$.
3. **Check Iteration 2 at $$u^1 = -3$$:**
   - Primal response: $$x_1^2 = 3, \; x_2^2 = 1.5$$ (total supply $$4.5$$, surplus of $$+1.5$$!).
   - Price update: $$u^2 = -3 + 1(1.5) = -1.5$$.
   Notice $$u^k$$ oscillates straight into $$u^\star = -2$$ (errors $$-2 \to +1 \to -0.5 \to +0.25 \dots$$, halving every step!), and the agents *never once shared their cost functions with each other*!

In this chapter we study ways of solving problems using the dual: the dual subgradient method, the dual decomposition method, and the augmented Lagrangian method, and we take a brief look at the idea of the Alternating Direction Method of Multipliers (ADMM).

First, let us briefly review two topics from earlier chapters: the proximal Newton method and conjugate functions.

## Review: proximal Newton method
Consider the problem
>\begin{equation}
\min_x g(x) + h(x)
\end{equation}

Here $$g$$ and $$h$$ are convex, $$g$$ is twice differentiable, and $$h$$ is simple.

The proximal Newton method starts from an initial point $$x^{(0)} \in \mathbb{R}^n$$. First, we find a direction that is good for both $$g$$ and $$h$$:
>\begin{alignat}{1}
v^{(k)} & = \arg \min_v \nabla g({x^{(k-1)}})^T v +  \frac{1}{2} v^T \nabla^2 g(x^{(k-1)}) v + h(x^{(k-1)} + v) 
\end{alignat}

Then we update the next iterate along this direction:
>\begin{equation}
x^{(k)} = x^{(k-1)} + t_k v^{(k)}, \quad k=1,2,3,\dots 
\end{equation}

Here $$t_k$$ is the step size, determined by backtracking.

These two steps are repeated.

> * Each iteration is very expensive (computing $$v^{(k)}$$ is generally very hard).
* However, under suitable conditions, very few iterations are needed to converge, and the method has a local quadratic convergence rate.


## Review: conjugate function
For $$f: \mathbb{R}^n \to \mathbb{R}$$, the conjugate function is defined as
>\begin{equation}
f^*(y) = \max_x y^Tx - f(x)
\end{equation}

(1) The conjugate can be written as follows, which is a form that frequently appears in dual problems.
>\begin{equation}
-f^{\ast}(y) = \min_x f(x) - y^Tx
\end{equation}

(2) If $$f$$ is closed and convex, then $$f^{**} = f$$. Moreover,
>\begin{equation}
x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz
\end{equation}
#### Proof ####
First we prove $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x)$$.

#### Step 1: $$y \in \partial f(x) \Longrightarrow x \in \partial f^{\ast}(y)$$
>
Assume $$y \in \partial f(x)$$. Then $$x$$ belongs to the set $$M_y$$ of maximizers of $$z \mapsto y^Tz - f(z)$$, i.e. $$x \in M_y$$. <br> Hence $$f^{\ast}(y) = y^Tx - f(x)$$, and for every $$w$$ we have $$f^{\ast}(w) \ge w^Tx - f(x) = f^{\ast}(y) + x^T(w - y)$$. This says exactly that $$x \in \partial f^{\ast}(y)$$.

####  Step 2: $$x \in \partial f^{\ast}(y) \Longrightarrow y \in \partial f(x)$$
>
By Step 1 applied to $$f^{\ast}$$, if $$x \in  \partial f^{\ast}(y)$$ then $$y \in \partial f^{\ast\ast}(x)$$. Since $$f^{\ast\ast}=f$$, we get $$y \in \partial f(x)$$.

Steps 1 and 2 prove $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x)$$.
#### Step 3: $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$
>
Finally, $$y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$ follows directly from the definition of the subgradient. <br>
Together with the above, this proves $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$.


(3) If $$f$$ is strictly convex, then
> $$
> \begin{equation}
> \nabla f^{\ast}(y) = \arg\min_z f(z) - y^T z
> \end{equation}
> $$

#### Proof

>If $$f$$ is strictly convex, $$f(z)-y^Tz$$ has a unique minimizer $$z$$,
>and by the proof of (2) above, this minimizer must be $$\nabla f^{\ast}(y)$$.

In other words, if $$f$$ is strictly convex, then the subdifferential of $$f^{\ast}$$ consists of a single element, which is the gradient. Hence $$f^{\ast}$$ is a differentiable function.
