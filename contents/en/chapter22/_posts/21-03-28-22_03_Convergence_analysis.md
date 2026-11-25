---
layout: post
title: 22-03 Convergence analysis
chapter: '22'
order: '4'
owner: YoungJae Choung
categories:
- chapter22
lang: en
---

Why does Frank–Wolfe converge at the universal rate $$O(1/k)$$ without ever mentioning a Euclidean Lipschitz constant $$L$$ or choosing a metric? The secret lies in Martin Jaggi’s 2011 geometric reformulation: instead of bounding curvature in Euclidean norm, we measure how far $$f$$ bends above its linear tangent *strictly inside* the feasible set $$C$$ via the affine-invariant curvature constant $$M$$. That single definition unlocks both a clean induction proof and one of optimization’s rarest superpowers—complete invariance under invertible linear transformations of the coordinates.

## Key ideas: Curvature Constant, Affine Invariance, and Inexact Oracles

- **Jaggi’s Curvature Constant $$M$$:** Defined as $$M = \sup_{x, s \in C,\ \gamma \in (0,1]} \frac{2}{\gamma^2}\bigl(f(y) - f(x) - \langle \nabla f(x), y - x \rangle\bigr)$$ with $$y = (1-\gamma)x + \gamma s$$, $$M$$ bounds the quadratic remainder along feasible line segments. Whenever $$\nabla f$$ is $$L$$-Lipschitz, $$M \le L \cdot \operatorname{diam}(C)^2$$.
- **The One-Step Descent Recurrence:** Combining the curvature bound with the optimality of $$s_k$$ and convexity of $$f$$ produces the key contraction inequality $$h_k \le (1 - \gamma_k) h_{k-1} + \frac{M}{2}\gamma_k^2$$ for suboptimality $$h_k = f(x^{(k)}) - f(x^\star)$$, which telescopes cleanly under $$\gamma_k = \frac{2}{k+1}$$ to give $$h_k \le \frac{2M}{k+2}$$.
- **Affine Invariance:** Because both the inner product $$\langle \nabla f(x), s - x \rangle$$ and the curvature constant $$M$$ depend only on linear functionals and convex combinations, reparameterizing $$x = A\tilde{x}$$ leaves the Frank–Wolfe trajectory identical—unlike projected gradient descent, whose Euclidean projection distorts under rescaling.
- **Robustness to Inexact LMOs:** In massive matrix problems, computing the exact top singular vector is unnecessary. Solving the LMO up to additive error $$\frac{\delta M \gamma_k}{2}$$ preserves the exact $$O(1/k)$$ rate with constant scaled merely by $$(1 + \delta)$$.

### Worked example: Computing $$M$$ and Checking the $$O(1/k)$$ Bound by Hand

Let $$f(x) = \frac{1}{2}(x - 1)^2$$ on the compact interval $$C = [0, 2]$$, starting at $$x^{(0)} = 0$$ (where $$f(x^{(0)}) = 0.5$$ and $$f(x^\star) = f(1) = 0$$).

1. **Compute the exact curvature constant $$M$$:** For any $$x, s \in [0, 2]$$ and $$y = x + \gamma(s - x)$$, the exact Taylor remainder of this quadratic is
   $$f(y) - f(x) - f'(x)(y - x) = \frac{1}{2}(y - x)^2 = \frac{1}{2}\gamma^2 (s - x)^2.$$
   Therefore,
   $$M = \max_{x, s \in [0, 2]} \frac{2}{\gamma^2} \cdot \frac{1}{2}\gamma^2 (s - x)^2 = \max_{x, s \in [0, 2]} (s - x)^2 = (2 - 0)^2 = 4.$$
2. **Evaluate the theoretical upper bound at $$k = 1, 2$$:** Using $$f(x^{(k)}) - f^\star \le \frac{2M}{k+2}$$, we get:
   - At $$k = 1$$: bound $$= \frac{8}{3} \approx 2.667$$.
   - At $$k = 2$$: bound $$= \frac{8}{4} = 2.000$$.
3. **Run two exact Frank–Wolfe steps with $$\gamma_k = \frac{2}{k+1}$$:**
   - **Step $$k = 1$$ ($$\gamma_1 = 1$$):** $$f'(x^{(0)}) = 0 - 1 = -1 < 0$$, so $$s^{(0)} = 2$$. Then $$x^{(1)} = (1 - 1)(0) + 1(2) = 2$$, giving $$h_1 = f(2) - 0 = 0.5 \le 2.667$$.
   - **Step $$k = 2$$ ($$\gamma_2 = \frac{2}{3}$$):** $$f'(x^{(1)}) = 2 - 1 = +1 > 0$$, so $$s^{(1)} = 0$$. Then $$x^{(2)} = \frac{1}{3}(2) + \frac{2}{3}(0) = \frac{2}{3}$$, giving $$h_2 = f\!\left(\frac{2}{3}\right) = \frac{1}{2}\left(-\frac{1}{3}\right)^2 = \frac{1}{18} \approx 0.0556 \le 2.000$$.
4. **Verify affine invariance:** Rescale via $$x = 10\tilde{x}$$ so $$\tilde{C} = [0, 0.2]$$ and $$\tilde{f}(\tilde{x}) = \frac{1}{2}(10\tilde{x} - 1)^2$$. Then $$\tilde{f}'' = 100$$ while $$\operatorname{diam}(\tilde{C})^2 = 0.04$$, so $$\tilde{M} = 100 \times 0.04 = 4 = M$$—identical!

## Convergence analysis

To find out the convergence characteristics of the Frank-Wolfe method, it is necessary to define the curvature constant of $$f$$ for $$C$$ as follows [Jaggi (2011)]:

>$$M = \max_{x,s,y\in C, y = (1−\gamma)x+\gamma s} \frac{2}{\gamma^2} \Bigl( f(y) − f(x) − \nabla f(x)^T(y − x) \Bigr)$$

where $$\gamma \in [0, 1]$$. Through $$M$$, we can actually measure how far the function tends to be from linear approximation. Here $$M = 0$$ indicates that $$f$$ is linear. $$f(y) - f(x) - \nabla f(x)^T(y - x)$$ is called the Bregman divergence defined by $$f$$.

>**Theorem**: The conditional gradient method using fixed step size $$\gamma_k = 2/(k + 1), k = 1,2,3, ...$$ satisfies the following:
>
>$$f(x^{(k)}) − f^{*} \leq \frac{2M}{k + 2}$$

The number of iterations required to satisfy $$f(x^{(k)}) − f^{*} \leq \epsilon$$ is $$O(1/\epsilon)$$. We want to prove this theory by induction. However, before moving on to the direct proof, we want to introduce one concept that needs to be addressed.

## Basic inequality

The **key inequality** used to prove Frank-Wolfe convergence speed is as follows:

>$$f(x^{(k)}) \leq f(x^{(k−1)}) − \gamma_k g(x^{(k−1)}) + \frac{\gamma^2_k}{2}M$$

where $$g(x) = \max_{s\in C} \nabla f(x)^T(x − s)$$ means the duality gap discussed earlier, and by induction, the ratio follows this inequality.

### [Proof]

To prove the basic inequality, we specify $$x^+ = x^{(k)}, x = x^{(k−1)}, s = s^{(k−1)}, \gamma = \gamma_k$$. Then we organize as follows:

>$$\begin{align}
>f(x^+) &= f\bigl( x + \gamma(s − x) \bigr) \\
>&\leq f(x) + \gamma\nabla f(x)^T(s − x) + \frac{\gamma^2}{2}M \\
>&= f(x) − \gamma g(x) + \frac{\gamma^2}{2}M
>\end{align}$$

In the above equation, the second line used the definition of $$M$$, and the third line used the definition of $$g$$.

Now, using the basic inequality, we use induction to prove our convergence rate theorem. For the case $$k=1$$, we can easily verify that the theorem is satisfied. For any case $$k > 1$$, we assume that $$f(x^{(k−1)}) − f^{*} \leq 2M/(k + 1)$$ is satisfied.

Let's recall the duality gap $$g(x)$$ mentioned earlier:

>$$g(x^{(k−1)}) \leq f(x^{(k−1)}) − f^{*}$$

Let's apply $$\gamma_k = 2/(k + 1)$$ and the basic inequality:

>$$f(x^{(k)}) \leq f(x^{(k−1)}) − 2(f(x^{(k−1)}) − f^{*})/(k + 1) + 4M/2(k + 1)^2$$
>
>$$f(x^{(k)}) − f^{*} \leq (1 − 2/(k + 1))(f(x^{(k−1)}) − f^{*}) + 2M/(k + 1)^2$$
>
>$$f(x^{(k)}) − f^{*} \leq (k − 1)/(k + 1) \times 2M/(k + 1) + 2M/(k + 1)^2 \leq 2M/(k + 2)$$

The proven convergence speed matches the speed known for projected gradient descent when $$\nabla f$$ is Lipschitz. Let's compare the assumptions. In fact, if $$\nabla f$$ is Lipschitz with constant $$L$$, then when $$\text{diam}^2(C) = \max_{x,s\in C} \|x − s\|^2$$, we have $$M \leq \text{diam}^2(C) \cdot L$$. To verify this, we need to remember that $$\nabla f$$ with constant $$L$$ Lipschitz is equivalent to the following:

>$$f(y) − f(x) − \nabla f(x)^T(y − x) \leq \frac{L}{2} \| y − x \|^2_2$$

Maximizing over all $$y = (1-\gamma) x + \gamma s$$ and multiplying by $$\frac{2}{\gamma^2}$$:

>$$M \leq \max_{x,s,y\in C, y=(1−\gamma)x+\gamma s} \frac{2}{\gamma^2} \cdot \frac{L}{2} \| y − x \|^2_2 = \max_{x,s\in C} L \| x − s \|^2_2$$

The boundary of $$M$$ has been determined. Basically, we assume that the bounded curvature is not greater than the curvature assumed for proximal gradient.

## Affine invariance

Let's think about the concepts we learned earlier:

* **Gradient Descent**: $$x^+ = x − t\nabla f(x)$$
* **Pure Newton's Method**: $$x^+ = x − \nabla^2 f(x)^{−1}\nabla f(x)$$

Gradient descent is not affine invariant. That is, scaling coordinates affects the performance of gradient descent. On the other hand, Newton's method is affine invariant. That is, the algorithm behaves the same under all affine transformations of variables. The conditional gradient method is similar to gradient descent but is affine invariant.

**Important property of Frank-Wolfe**: The update is **affine invariant**.

Given nonsingular $$A : \mathbb{R}^n → \mathbb{R}^n$$, we can define $$x = Ax', h(x') = f(Ax')$$. Then Frank-Wolfe for $$h(x')$$ can be computed as follows:

>$$\begin{array}{rcl}
>s' & = & \arg\min_{z\in A^{−1}C} \nabla h(x')^Tz \\
>(x')^+ & = & (1 − \gamma)x' + \gamma s'
>\end{array}$$

Multiplying by $$A$$ gives the same Frank-Wolfe update performed on $$f(x)$$. Even the convergence analysis is affine invariant. The curvature constant $$M$$ of $$h$$ is as follows:

>$$M = \max_{x',s',y'\in A^{−1}C, y'=(1−\gamma)x'+\gamma s'} \frac{2}{\gamma^2} \Bigl( h(y') − h(x') − \nabla h(x')^T(y' − x') \Bigr)$$

Since $$\nabla h(x')^T(y' − x') = \nabla f(x)^T(y − x)$$, it matches $$f$$. However, the affine invariance of the boundary of $$M$$ is not intuitive:

>$$M \leq \max_{x,s\in C} L\|x − s\|^2_2$$

If the diameter of the given $$C$$ is not affine invariant, this is worth considering.

## Inexact updates

We analyzed inaccurate Frank-Wolfe updates [Jaggi (2011)].

Choose $$s^{(k−1)}$$ such that:

>$$\nabla f(x^{(k−1)})^Ts^{(k−1)} \leq \min_{s\in C} \nabla f(x^{(k−1)})^Ts + \frac{M\gamma_k}{2} \cdot \delta$$

where $$\delta \geq 0$$ is an inaccuracy parameter. Using this, we basically get the following ratio:

>**Theorem**: The conditional gradient method using fixed step size $$\gamma_k=2/(k+1), k=1,2,3, ...$$ and inaccuracy parameter $$\delta \geq 0$$ satisfies the following:
>
>$$f(x^{(k)}) − f^{*} \leq \frac{2M}{k + 2} (1 + \delta)$$

**Note**: The optimization error at step $$k$$ is $$\frac{M\gamma_k}{2} \cdot \delta$$. Since $$\gamma_k → 0$$, the error disappears over time as intended.