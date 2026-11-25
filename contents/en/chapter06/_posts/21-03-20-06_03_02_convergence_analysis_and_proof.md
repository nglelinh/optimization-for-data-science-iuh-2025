---
layout: post
title: 06-03-02 Convergence analysis & Proof
chapter: '06'
order: 11
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

How do you prove that a greedy local rule—just following the negative gradient—must eventually land arbitrarily close to the global minimum? The proof is one of the crown jewels of convex analysis: combine the quadratic upper bound with convexity's linear lower bound, and watch the squared distances $$\|x^{(i)} - x^\star\|_2^2$$ telescope like a collapsing accordion, leaving a clean $$O(1/k)$$ error bound.

## Key ideas: Anatomy of the $$O(1/k)$$ Telescoping Proof

1. **Step 1 — Smoothness Gives a Drop**: From $$t \le 1/L$$, each step reduces the objective by at least $$\frac{t}{2}\|\nabla f(x^{(i)})\|_2^2$$:
   $$f(x^{(i+1)}) \le f(x^{(i)}) - \frac{t}{2}\|\nabla f(x^{(i)})\|_2^2.$$
2. **Step 2 — Convexity Bridges to $$x^\star$$**: Convexity gives $$f(x^{(i)}) \le f(x^\star) + \nabla f(x^{(i)})^T(x^{(i)} - x^\star)$$. Substituting this into Step 1 expresses $$f(x^{(i+1)}) - f(x^\star)$$ purely in terms of $$\nabla f(x^{(i)})$$ and $$(x^{(i)} - x^\star)$$.
3. **Step 3 — Completing the Square Creates a Telescope**: Using the algebraic identity
   $$u^T v - \frac{t}{2}\|u\|_2^2 = \frac{1}{2t}\Bigl(\|v\|_2^2 - \|v - tu\|_2^2\Bigr)$$
   with $$u = \nabla f(x^{(i)})$$ and $$v = x^{(i)} - x^\star$$ yields
   $$f(x^{(i+1)}) - f(x^\star) \le \frac{1}{2t}\Bigl(\|x^{(i)} - x^\star\|_2^2 - \|x^{(i+1)} - x^\star\|_2^2\Bigr).$$
4. **Step 4 — Summing & Monotonicity**: Summing from $$i = 0$$ to $$k - 1$$ cancels all intermediate distance terms, and because $$f(x^{(k)}) \le f(x^{(i)})$$ for all $$i \le k$$, we get $$f(x^{(k)}) - f(x^\star) \le \frac{\|x^{(0)} - x^\star\|_2^2}{2tk}$$.

### Worked example: Checking the Telescoping Inequality Numerically

Apply gradient descent to $$f(x) = \frac{1}{2}x^2$$ (so $$L = 1$$, $$x^\star = 0$$, $$f^\star = 0$$) from $$x^{(0)} = 4$$ with $$t = 0.5 \le 1/L$$ for $$k = 3$$ steps, and verify every term of the telescoping proof!

1. **Compute the iterates and objective values**:
   - $$x^{(0)} = 4$$, $$f(x^{(0)}) = 8$$, $$\|x^{(0)} - x^\star\|^2 = 16$$.
   - $$x^{(1)} = 4 - 0.5(4) = 2$$, $$f(x^{(1)}) = 2$$, $$\|x^{(1)} - x^\star\|^2 = 4$$.
   - $$x^{(2)} = 2 - 0.5(2) = 1$$, $$f(x^{(2)}) = 0.5$$, $$\|x^{(2)} - x^\star\|^2 = 1$$.
   - $$x^{(3)} = 1 - 0.5(1) = 0.5$$, $$f(x^{(3)}) = 0.125$$, $$\|x^{(3)} - x^\star\|^2 = 0.25$$.
2. **Verify the single-step telescoping inequality $$f(x^{(i+1)}) - f^\star \le \frac{1}{2t}(\|x^{(i)}\|^2 - \|x^{(i+1)}\|^2)$$** (with $$\frac{1}{2t} = 1$$):
   - $$i = 0$$: $$2 \le 1(16 - 4) = 12$$ (holds!).
   - $$i = 1$$: $$0.5 \le 1(4 - 1) = 3$$ (holds!).
   - $$i = 2$$: $$0.125 \le 1(1 - 0.25) = 0.75$$ (holds!).
3. **Sum all three inequalities and check the final $$O(1/k)$$ bound**:
   - Left sum: $$2 + 0.5 + 0.125 = 2.625 \ge 3 \cdot f(x^{(3)}) = 0.375$$.
   - Right telescoping sum: $$(16 - 4) + (4 - 1) + (1 - 0.25) = 16 - 0.25 = 15.75 \le 16$$.
   - Final bound at $$k = 3$$: $$f(x^{(3)}) = 0.125 \le \frac{16}{2(0.5)(3)} = \frac{16}{3} \approx 5.333$$ — verified!

Suppose $$f$$ is convex and differentiable with $$dom(f) = \mathbb{R}^n$$, and $$\nabla f$$ is Lipschitz continuous with constant $$L > 0$$:

>$$ \| \nabla f(x) - \nabla f(y) \|_2 \le L \| x - y \|_2 $$ for any $$x, y$$

Reference: [[Wikipedia: Lipschitz continuity](https://en.wikipedia.org/wiki/Lipschitz_continuity)]

## Convergence Theorem
**Gradient descent** with fixed step size $$t \le 1/L$$ satisfies:
>$$
\begin{align}
f(x^{(k)}) - f^* \le  \frac{ \| x^{(0)} - x^* \|^2_2 }{2tk}
\end{align}
$$

With fixed step size, the convergence rate is $$O(1/k)$$. To achieve $$f(x^{(k)}) - f^* \le \epsilon$$, $$O(1/\epsilon)$$ iterations are needed.

## Proof
If $$\nabla f$$ is Lipschitz continuous and $$f$$ is convex, then $$f$$ has a quadratic upper bound (see [06-03-02]({% multilang_post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %})).

> $$
\begin{align}
f(y) \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \| y - x \|^2_2 \quad \forall x, y
\end{align}
$$

For gradient descent $$x^+ = x - t \nabla f(x)$$, substitute $$y = x^+$$:

>$$
\begin{align}
f(x^+) & \le f(x) - t ( 1 - \frac{Lt}{2} )\| \nabla f(x) \|^2_2 \\\
& \le f(x) -  \frac{t}{2} \| \nabla f(x) \|^2_2 \quad \text{if } t \le 1/L
\end{align}
$$

Thus, $$f(x^+) < f(x)$$ and gradient descent converges.