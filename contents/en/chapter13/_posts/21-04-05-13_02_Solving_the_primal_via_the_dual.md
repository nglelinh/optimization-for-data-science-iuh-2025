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

