---
layout: post
title: 06-03-04 Convergence analysis under strong convexity
chapter: '06'
order: 13
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

On a flat-bottomed convex valley, gradients fade gently near the minimum and gradient descent slows to $$O(1/k)$$. Now give the valley a guaranteed minimum upward curvature $$m > 0$$—strong convexity—and everything changes: gradients stay steep all the way to $$x^\star$$, and the error plummets *exponentially* fast, cutting digits of precision at a constant rate every few steps.

## Background Knowledge Map: Strong Convexity and Linear Convergence

1. **Quadratic Lower Bound ($$m$$-Strong Convexity)**: A function $$f$$ is $$m$$-strongly convex if $$f(x) - \frac{m}{2}\|x\|_2^2$$ is convex, equivalently
   $$f(y) \ge f(x) + \nabla f(x)^T(y - x) + \frac{m}{2}\|y - x\|_2^2 \quad \forall x, y$$
   (or $$\nabla^2 f(x) \succeq mI$$ when twice differentiable). This guarantees a *unique* global minimizer $$x^\star$$.
2. **The Polyak–Łojasiewicz (PL) Inequality**: Minimizing the quadratic lower bound over $$y$$ yields the crucial gradient-dominance bound
   $$\|\nabla f(x)\|_2^2 \ge 2m\bigl(f(x) - f^\star\bigr).$$
   In words: wherever you are still far from $$f^\star$$, the gradient *cannot* be tiny!
3. **One-Line Linear Convergence Proof**: Combining the $$L$$-smoothness drop $$f(x^+) - f^\star \le f(x) - f^\star - \frac{1}{2L}\|\nabla f(x)\|_2^2$$ with the PL inequality immediately gives
   $$f(x^{(k)}) - f^\star \le \left(1 - \frac{m}{L}\right)^k \bigl(f(x^{(0)}) - f^\star\bigr).$$
   With the tighter step $$t = \frac{2}{m + L}$$, the distance to $$x^\star$$ contracts even faster: $$\|x^{(k)} - x^\star\|_2 \le \left(\frac{L - m}{L + m}\right)^k \|x^{(0)} - x^\star\|_2$$.
4. **Role of the Condition Number $$\kappa = L/m$$**: Every $$\kappa$$ iterations cuts the error by a factor of $$e \approx 2.718$$, so achieving $$\varepsilon$$ accuracy requires only $$O(\kappa \log(1/\varepsilon))$$ steps—logarithmic in $$1/\varepsilon$$!

### Step-by-Step Worked Example (Read Slowly): Applying the PL Inequality to Ridge Regression

Consider the 1D Ridge objective $$f(x) = \frac{1}{2}(2x - 6)^2 + \frac{1}{2}(2)x^2 = 3x^2 - 12x + 18$$.

1. **Determine $$m$$, $$L$$, and $$x^\star$$**:
   - $$f'(x) = 6x - 12$$, $$f''(x) = 6$$. Here $$m = L = 6$$ (so $$\kappa = 1$$).
   - Setting $$f'(x) = 0$$ gives $$x^\star = 2$$ and $$f^\star = 3(4) - 24 + 18 = 6$$.
2. **Verify the PL inequality at $$x^{(0)} = 5$$**:
   - Suboptimality: $$f(5) - f^\star = (75 - 60 + 18) - 6 = 33 - 6 = 27$$.
   - Gradient squared: $$\|f'(5)\|_2^2 = (30 - 12)^2 = 18^2 = 324$$.
   - PL right-hand side: $$2m(f(5) - f^\star) = 2(6)(27) = 324$$ — exact equality!
3. **Verify linear convergence with conservative step $$t = 1/12$$** (pretending we overestimated $$L_{\mathrm{est}} = 12$$):
   - Guaranteed factor: $$1 - \frac{m}{L_{\mathrm{est}}} = 1 - \frac{6}{12} = 0.5$$.
   - Step 1: $$x^{(1)} = 5 - \frac{1}{12}(18) = 3.5$$, giving $$f(3.5) - f^\star = 3(3.5 - 2)^2 = 3(2.25) = 6.75$$.
   - Ratio: $$\frac{6.75}{27} = 0.25 \le 0.5$$ — geometric contraction verified!

If $$f$$ satisfies the following condition, it is strongly convex (assuming $$f$$ is twice differentiable and $$m > 0$$):
> $$ \begin{align}
f(y) \ge f(x) + \nabla f(x)^T(y-x) + \frac{m}{2} \| y-x \|_2^2, \quad \forall x, y
\end{align} $$

Here, $$f$$ has a quadratic lower bound, and the constant $$m$$ is determined by the minimum eigenvalue of the Hessian of $$f$$.

For any convex function $$g$$, $$f$$ is strongly convex if:
> $$ \begin{align}
g(x) = f(x) - \frac{m}{2} \| x \|_2^2 \quad \text{is convex for all } x \text{ and } m > 0
\end{align} $$

## Convergence Theorem
Given Lipschitz continuity and strong convexity, the following theorem holds (where $$L$$ is the Lipschitz constant and $$m$$ is the strong convexity constant):

**Gradient descent** with fixed step size ($$t \le 2/(m + L)$$) or backtracking line search satisfies:
> $$ \begin{align}
f(x^{(k)}) - f^* \le c^k \frac{L}{2} \| x^{(0)} - x^* \|_2^2, \quad c = (1 - \frac{m}{L}), \quad 0 < c < 1
\end{align} $$

## Proof
If $$\nabla f$$ is Lipschitz continuous and $$f$$ is strongly convex, then $$f$$ has a quadratic upper bound (see [06-03-02]({% multilang_post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %})).

For gradient descent $$x^+ = x - t \nabla f(x)$$, the optimal $$t$$ is $$1/L$$, yielding:
> $$ \begin{align}
f(x^+) \le f(x) -  \frac{1}{2L} \| \nabla f(x) \|_2^2
\end{align} $$

Subtracting $$f(x^*)$$ from both sides:
> $$ \begin{align}
f(x^+) - f(x^*) \le f(x) - f(x^*) -  \frac{1}{2L} \| \nabla f(x) \|_2^2
\end{align} $$

Since Gradient Descent satisfies the condition:
> $$ \begin{align}
f(x) - f(x^*) \le \frac{1}{2m} \| \nabla f(x) \|_2^2
\end{align} $$

We can substitute to get:
> $$ \begin{align}
f(x^+) - f(x^*) & \le f(x) - f(x^*) -  \frac{m}{L} ( f(x) - f(x^*) ) \\
& =  (1 -  \frac{m}{L} ) ( f(x) - f(x^*) ) \\
& = c  ( f(x) - f(x^*) ) \\
\end{align} $$

Iterating this process gives:
> $$ \begin{align}
f(x^{(k)}) - f(x^*) \le c^k ( f(x^{(0)}) - f(x^*) ) \\
\end{align} $$

From the Taylor expansion of the function with $$y = x^{(0)}$$ and $$x = x^*$$:
> $$ \begin{align}
f(y) \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \lVert y - x \rVert^2_2  \space \space \forall x, y
\end{align} $$

And since the function is convex, we have:
> $$ \begin{align}
f(x^{(0)}) & \le f(x^{*}) + \nabla f(x^{*})^T (x^{(0)}- x^{*} ) + \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2 \\\\
& =  f(x^{*}) + \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2 \\\\
\end{align} $$

Rearranging gives:
> $$ \begin{align}
f(x^{(0)}) - f(x^{*}) & \le \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2 \\\\
\end{align} $$

Substituting this into the previous inequality results in:
> $$ \begin{align}
f(x^{(k)}) - f(x^{*}) & \le c^k \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2  \\\
\end{align} $$

This proves the Convergence Theorem for Gradient Descent under Strong Convexity.

## Linear convergence
When $$f$$ is strongly convex, the convergence rate becomes $$O(c^k)$$, which is exponential.
To achieve $$f(x^{(k)}) - f^{*} \le \epsilon$$, it requires $$O(\log(1/\epsilon)$$ iterations.
(Without strong convexity, it would require $$O(1/\epsilon)$$ iterations.)

The convergence rate $$O(c^k)$$ appears linear on a semi-log plot, as shown below.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06.03_01_01_Line_Convergence.png" alt="Line_Convergence" width="60%" height="60%">
  <figcaption style="text-align: center;">[Fig 1] Linear convergence [1]</figcaption>
</p>
</figure>

Here, the constant $$c$$ in $$O(c^k)$$ is given by $$1 - \frac{m}{L}$$ and depends on the condition number $$L/m$$. A larger condition number results in slower convergence (where the condition number is the ratio of the largest eigenvalue to the smallest eigenvalue).

The *algebra* of this proof — descent lemma plus a lower bound that turns $$\|\nabla f\|^2$$ into a function-value gap — still works if strong convexity is weakened to the Polyak–Łojasiewicz inequality. That optional modern-rate story, and the overparameterized least-squares example where minimizers are not unique, is [28-05 The PL condition and modern rates]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}).

