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

Here is one of the most counterintuitive facts in all of optimization theory: **BFGS converges superlinearly even though its Hessian approximation $$B_k$$ almost never converges to the true Hessian $$\nabla^2 f(x^\star)$$!** How can an algorithm mimic Newton's method so closely that $$\|x^{k+1} - x^\star\| / \|x^k - x^\star\| \to 0$$ while getting the Hessian wrong in almost every direction? The answer is the celebrated **Dennis–Moré characterization**: $$B_k$$ only needs to match the true Hessian *along the search direction $$p_k$$ itself*.

## Background Knowledge Map: The Machinery Behind Superlinear Convergence

- **Q-Superlinear Convergence:** A sequence converges Q-superlinearly if $$\lim_{k\to\infty} \frac{\|x^{k+1} - x^\star\|}{\|x^k - x^\star\|} = 0$$—strictly faster than any linear rate $$\rho^k$$, meaning the number of accurate digits accelerates at every iteration.
- **The Dennis–Moré Necessary & Sufficient Condition:** For $$x^{k+1} = x^k + p_k$$ with $$p_k = -B_k^{-1} \nabla f(x^k)$$, the iterates converge superlinearly *if and only if*:
  $$\lim_{k \to \infty} \frac{\|(B_k - \nabla^2 f(x^\star))\, p_k\|}{\|p_k\|} = 0.$$
  Notice this is a *directional* condition, vastly weaker than $$\|B_k - \nabla^2 f(x^\star)\| \to 0$$.
- **Unit Step Acceptance ($$\alpha_k = 1$$):** Superlinear convergence requires the line search to eventually accept the full quasi-Newton step $$\alpha_k = 1$$ without damping; under the Wolfe conditions with $$c_1 < 1/2$$, the Dennis–Moré condition guarantees $$\alpha_k = 1$$ is accepted for all sufficiently large $$k$$.
- **Trace–Determinant Potential Function (Byrd–Nocedal):** Proving BFGS satisfies Dennis–Moré uses the Lyapunov potential $$\psi(B) = \operatorname{tr}(B) - \log \det(B)$$, showing that even if $$B_k$$ starts poorly scaled, the sum $$\sum_k \|(B_k - G^\star) s_k\|^2 / \|s_k\|^2$$ is finite—forcing its terms to vanish!

### Step-by-Step Worked Example (Read Slowly): Satisfying Dennis–Moré Without $$B_k \to G^\star$$

Suppose the true Hessian at $$x^\star$$ is $$G^\star = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}$$, and at iteration $$k \ge 1$$ our quasi-Newton matrix and step direction are:
$$B_k = \begin{bmatrix} 1 + \frac{1}{k} & 0 \\ 0 & 5 \end{bmatrix}, \qquad p_k = \begin{bmatrix} 1 \\ \frac{1}{k} \end{bmatrix}.$$

1. **Check whether $$B_k$$ converges to $$G^\star$$:**
   $$B_k - G^\star = \begin{bmatrix} \frac{1}{k} & 0 \\ 0 & 3 \end{bmatrix} \implies \|B_k - G^\star\|_2 = 3 \quad \text{for all } k \ge 1.$$
   So $$B_k$$ *never* converges to $$G^\star$$—its second diagonal entry is permanently off by $$150\%$$!
2. **Now evaluate the Dennis–Moré ratio:**
   $$(B_k - G^\star) p_k = \begin{bmatrix} \frac{1}{k} & 0 \\ 0 & 3 \end{bmatrix}\begin{bmatrix} 1 \\ \frac{1}{k} \end{bmatrix} = \begin{bmatrix} \frac{1}{k} \\ \frac{3}{k} \end{bmatrix} \implies \|(B_k - G^\star) p_k\|_2 = \frac{\sqrt{1^2 + 3^2}}{k} = \frac{\sqrt{10}}{k}.$$
   Meanwhile, $$\|p_k\|_2 = \sqrt{1 + \frac{1}{k^2}} \ge 1$$. Therefore:
   $$\frac{\|(B_k - G^\star) p_k\|_2}{\|p_k\|_2} = \frac{\sqrt{10}}{k \sqrt{1 + 1/k^2}} \;\xrightarrow{k \to \infty}\; 0!$$
3. **Numerical check at $$k = 100$$:**
   Matrix error is still $$3.0$$, yet the directional Dennis–Moré error is only $$\frac{3.162}{100.005} \approx 0.0316$$—confirming that BFGS only needs accurate curvature in the subspace where the steps actually move!

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
