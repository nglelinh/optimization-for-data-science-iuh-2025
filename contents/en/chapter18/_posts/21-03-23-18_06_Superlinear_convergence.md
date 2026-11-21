---
layout: post
title: 18-06 Superlinear convergence
chapter: '18'
order: '7'
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

# Assumption 1:

> The Hessian matrix $$G$$ is Lipschitz continuous at $$x^\ast$$, that is,
>
> $$
> \| G(x) - G(x^\ast) \| \le L \| x - x^\ast \|,
> $$
>
> for all $$x$$ near $$x^\ast$$, where $$L$$ is a positive constant.

# Assumption 2: Wolfe conditions

> Assume $$t$$ is chosen (via backtracking) so that
>
> $$
> f(x + tp) \le f(x) + \alpha_1 t \nabla f(x)^T p
> $$
>
> and
>
> $$
> \nabla f(x + tp)^T p \ge \alpha_2 \nabla f(x)^T p
> $$
>
> for $$0 < \alpha_1 < \alpha_2 < 1.$$

* The first condition of the Wolfe conditions ensures that too large a $$t$$ is not selected.
* The second condition of the Wolfe conditions ensures that too small a $$t$$ is not selected.

DFP and BFGS show superlinear convergence under the above two assumptions. (reference: [Rate of convergence on Wikipedia](https://en.wikipedia.org/wiki/Rate_of_convergence))

>$$
>\lim_{k \rightarrow \infty} \frac{ \| x^{k+1} - x^\ast \| }{ \| x^k - x^\ast \| } = 0.
>$$

# Dennis-Moré Theorem

When the search direction of a quasi-Newton method approximates the Newton direction well enough near the solution, and the step length satisfies the Wolfe conditions during convergence, there is a sufficient condition on the search direction for superlinear convergence [14].

>Assume $$f$$ is twice continuously differentiable and $$x^k \rightarrow x^\ast$$ such that $$\nabla f(x^\ast) = 0$$ and $$\nabla^2 f(x^\ast)$$ is positive definite. Suppose
>
>$$
>\lim_{k \rightarrow \infty} \frac{\| \nabla f(x^k) + \nabla^2 f(x^k) p^k \| }{\| p^k \|} = 0.
>$$
>
>If the search direction $$p^k$$ satisfies the condition above, then there is a $$k_0$$ such that:
>
> 1. For $$k \ge k_0$$, the step length $$t_k = 1$$ satisfies the Wolfe conditions.
> 2. In that case, for $$k \ge k_0$$ with $$t_k = 1$$, $$x^k \rightarrow x^\ast$$ with superlinear convergence.
