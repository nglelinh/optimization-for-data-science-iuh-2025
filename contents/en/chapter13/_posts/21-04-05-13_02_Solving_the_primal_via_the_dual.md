---
layout: post
title: 13-02 Solving the primal via the dual
chapter: '13'
order: 3
owner: Wontak Ryu
categories:
- chapter13
lang: en
lesson_type: required
---

Imagine allocating power across 10,000 wireless channels to maximize total throughput subject to a single total power budget $$\sum_{i=1}^{10000} x_i = P$$. Solving a 10,000-variable constrained problem directly looks daunting—until you dualize that single budget constraint. Suddenly, the 10,000 variables decouple completely into 10,000 trivial 1D problems coordinated by a *single* scalar price $$v$$.

## Background Knowledge Map: Decomposition Through Scalar Duality

- **Pillar 1 — Separable Objective Structure:** When $$f(x) = \sum_{i=1}^n f_i(x_i)$$ has no cross-terms, the only coupling between coordinates is the linear constraint $$a^T x = b$$.
- **Pillar 2 — Dualizing the Coupling Constraint:** Moving $$v(b - a^T x)$$ into the Lagrangian turns the minimization over $$\mathbb{R}^n$$ into $$n$$ independent 1D minimizations, each producing $$-f_i^*(a_i v)$$.
- **Pillar 3 — Dimensionality Collapse ($$n \to 1$$):** The dual problem $$\min_v \sum_{i=1}^n f_i^*(a_i v) - bv$$ lives in $$\mathbb{R}^1$$ regardless of how large $$n$$ is, making 1D bisection or Newton's method instantaneous.
- **Pillar 4 — Strict Convexity Guarantees Unique Recovery:** Once $$v^\star$$ is found, each coordinate is recovered independently via the stationarity condition $$\nabla f_i(x_i^\star) = a_i v^\star$$, which yields a unique primal optimum whenever each $$f_i$$ is strictly convex.

### Step-by-Step Worked Example (Read Slowly): Solving a 3-Variable Separable Problem via a 1D Dual

Minimize $$f(x) = \frac{1}{2}x_1^2 + x_2^2 + \frac{3}{2}x_3^2$$ subject to $$x_1 + 2x_2 + 3x_3 = 14$$ (so $$a = (1, 2, 3)^T$$, $$b = 14$$).

1. **Compute each 1D conjugate $$f_i^*(s) = \max_{x_i}(s x_i - f_i(x_i))$$:**
   - For $$f_1(x_1) = \frac{1}{2}x_1^2$$: $$x_1 = s \implies f_1^*(s) = \frac{1}{2}s^2$$.
   - For $$f_2(x_2) = x_2^2$$: $$2x_2 = s \implies x_2 = \frac{s}{2} \implies f_2^*(s) = \frac{1}{4}s^2$$.
   - For $$f_3(x_3) = \frac{3}{2}x_3^2$$: $$3x_3 = s \implies x_3 = \frac{s}{3} \implies f_3^*(s) = \frac{1}{6}s^2$$.
2. **Assemble the 1D dual objective $$\phi(v) = \sum_{i=1}^3 f_i^*(a_i v) - bv$$:**
   $$\phi(v) = \frac{1}{2}(1v)^2 + \frac{1}{4}(2v)^2 + \frac{1}{6}(3v)^2 - 14v = \left(\frac{1}{2} + 1 + \frac{3}{2}\right)v^2 - 14v = 3v^2 - 14v.$$
3. **Solve the scalar dual:** Set $$\phi'(v) = 6v - 14 = 0 \implies v^\star = \frac{7}{3}$$.
4. **Recover $$x^\star$$ coordinate-by-coordinate from $$f_i'(x_i^\star) = a_i v^\star$$:**
   - $$x_1^\star = 1 \cdot \frac{7}{3} = \frac{7}{3}$$,
   - $$2x_2^\star = 2 \cdot \frac{7}{3} \implies x_2^\star = \frac{7}{3}$$,
   - $$3x_3^\star = 3 \cdot \frac{7}{3} \implies x_3^\star = \frac{7}{3}$$.
5. **Verify feasibility and strong duality:** $$x_1^\star + 2x_2^\star + 3x_3^\star = \frac{7}{3}(1+2+3) = 14$$. Primal cost is $$\left(\frac{1}{2}+1+\frac{3}{2}\right)\left(\frac{7}{3}\right)^2 = 3 \cdot \frac{49}{9} = \frac{49}{3}$$, and dual value is $$-\phi(7/3) = 14\cdot\frac{7}{3} - 3\cdot\frac{49}{9} = \frac{98-49}{3} = \frac{49}{3}$$.

### An important consequence of stationarity
Under the condition of strong duality, when dual solution $$u^{\star}, v^{\star}$$ is given, the primal solution $$x^{\star}$$ can be found by solving the following Lagrangian:

> $$ \min_x f(x) + \sum_{i=1}^m u_i^{\star} h_i(x) + \sum_{j=1}^r v^{\star}_i l_j(x)$$

Often, the solution to such unconstrained problems can be represented by explicitly bringing the characteristics of the primal solution through the dual solution.

Moreover, if the solution to this problem is unique, the dual solution becomes the primal solution $$x^{\star}$$.
This is very useful when solving the dual problem is easier than solving the primal problem directly.


### Example from B & V page 249:
> $$ \min_x \sum_{i=1}^n f_i(x_i) \qquad \text{ subject to }\qquad a^Tx = b$$


> $$\begin{align}
> g(v) &= \min_x \sum_{i=1}^n f_i(x_i) + v(b−a^Tx) \\\
> &= bv + \min_x \sum_{i=1}^n f_i(x_i) −va^Tx \\\
> &= bv + \min_x \sum_{i=1}^n f_i(x_i) −v \sum_{i=1}^n a_ix_i \\\
> &= bv + \sum_{i=1}^n (\underbrace{\min_{x_i} \{ f_i(x_i) − a_ivx_i \}}_{-f^{*}_i(a_iv)}) \\\
> &= bv − \sum_{i=1}^n f^{*}_i (a_iv)
> \end{align}$$
 
Here $$f^{*}$$ denotes the conjugate of $$f_i$$.

Therefore, the dual problem can be represented as follows:
> $$ \max_v bv − \sum^n_{i=1} f^{*}_i (a_iv)$$

Also, by multiplying by minus (-), the maximum problem can be represented as the following minimum problem:
> $$ \min_v \sum^n_{i=1} f^{*}_i (a_iv) − bv$$

This is a convex minimization problem in scalar variables that can be solved much more easily than the primal problem.

When $$v^{\star}$$ is given, the primal solution $$x^{\star}$$ can be solved as follows:
> $$ \min_{x} \sum^n_{i=1} (f_i(x_i) − a_iv^{\star}x_i)$$

The strict convexity of each $$f_i$$ means that this has a unique solution.
That is, $$x^{\star}$$ is obtained through the calculation of $$∇f_i(x_i) = a_iv^{\star}$$ for each $$i$$.

