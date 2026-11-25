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

You might worry that dual optimization is only useful when you can compute the Fenchel conjugate $$f^\ast(y)$$ in closed form. Remarkably, **Danskin's theorem** frees you from ever writing down $$f^\ast$$ explicitly: to find a subgradient (or exact gradient) of the dual function $$g(u) = -f^\ast(-A^T u) - b^T u$$, you just minimize the Lagrangian over $$x$$ once and plug the minimizer $$x^+(u)$$ straight into the residual $$A x^+(u) - b$$!

## Key ideas: Computing Dual Gradients Without Closed-Form Conjugates

- **Lagrangian–Conjugate Identity:** The dual objective $$g(u) = \inf_x \{f(x) + u^T(Ax - b)\} = -f^\ast(-A^T u) - b^T u$$ expresses dual maximization directly in terms of the convex conjugate $$f^\ast$$.
- **Danskin's Subgradient Formula:** Any primal minimizer $$x^{(k)} \in \arg\min_x \{f(x) + (u^{(k-1)})^T A x\}$$ belongs to $$\partial f^\ast(-A^T u^{(k-1)})$$, which immediately gives $$A x^{(k)} - b \in \partial g(u^{(k-1)})$$—no closed-form differentiation of $$f^\ast$$ needed!
- **Differentiability vs. Subgradients:** If $$f$$ is *strictly* convex, the minimizer $$x^{(k)}$$ is unique and $$g(u)$$ is continuously differentiable (dual gradient ascent); if $$f$$ is merely convex (e.g., an LP or $$\ell_1$$ norm), $$x^{(k)}$$ may be non-unique and we get a dual *subgradient* method requiring diminishing step sizes.
- **Primal Recovery Warning:** Even when $$g(u^{(k)}) \to g^\star$$, the raw primal iterates $$x^{(k)}$$ need not converge to $$x^\star$$ unless $$f$$ is strictly convex; for general convex $$f$$, averaging the primal iterates (or adding an augmented Lagrangian penalty) is needed to recover feasibility.

### Worked example: Dual Gradient Ascent Without Writing $$f^\ast$$

Minimize $$f(x) = e^{x_1} + e^{x_2}$$ subject to $$x_1 + x_2 = 2$$ (exact optimum by symmetry: $$x_1^\star = x_2^\star = 1$$, $$f^\star = 2e$$, $$u^\star = -e \approx -2.7183$$).

1. **Solve the primal Lagrangian minimization for a given $$u < 0$$:**
   $$\min_{x_1, x_2} \; e^{x_1} + e^{x_2} + u(x_1 + x_2 - 2) \implies e^{x_i} = -u \implies x_1(u) = x_2(u) = \ln(-u).$$
   Notice we never even formed the entropy conjugate $$f^\ast(y) = y\ln y - y$$!
2. **Evaluate the dual gradient at $$u^0 = -1$$:**
   - Primal minimizer: $$x^{(1)} = (\ln 1, \ln 1)^T = (0, 0)^T$$.
   - Dual gradient: $$\nabla g(-1) = A x^{(1)} - b = (0 + 0) - 2 = -2$$.
3. **Update $$u$$ with step size $$t = 0.5$$:**
   $$u^1 = u^0 + 0.5(-2) = -1 - 1 = -2.$$
4. **Check Iteration 2 at $$u^1 = -2$$:**
   - Primal minimizer: $$x^{(2)} = (\ln 2, \ln 2)^T \approx (0.6931, 0.6931)^T$$.
   - Dual residual shrank from $$-2.0$$ to $$2\ln 2 - 2 \approx -0.6137$$, and $$u^2 = -2 + 0.5(-0.6137) \approx -2.3069$$, climbing smoothly toward $$u^\star = -e \approx -2.7183$$!

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
