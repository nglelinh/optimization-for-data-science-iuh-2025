---
layout: post
title: 15-01-02 Log barrier function & barrier method
chapter: '15'
order: 4
owner: Minjoo Lee
categories:
- chapter15
lang: en
---

Why specifically the *logarithm* $$-\log(-h_i(x))$$ instead of a simpler penalty like $$1/(-h_i(x))$$? Two miraculous mathematical facts single out the logarithm: its derivative $$-1/h_i(x)$$ scales naturally to form dual multipliers with an exact $$m/t$$ duality gap, and $$-\log(-u)$$ is **self-concordant**—meaning Newton's method never loses its affine-invariant polynomial-time guarantee!

## Background Knowledge Map: Anatomy of the Log-Barrier Formulation

- **Pillar 1 — Exact Form of the Log Barrier:** For convex $$C^2$$ inequalities $$h_1, \dots, h_m$$, $$\phi(x) = -\sum_{i=1}^m \log(-h_i(x))$$ has open convex domain $$\{x : h_i(x) < 0\ \forall i\}$$.
- **Pillar 2 — Equivalent Scaling ($$f + \frac{1}{t}\phi \iff tf + \phi$$):** Multiplying the objective by $$t > 0$$ does not change the minimizer $$x^*(t)$$, and keeps $$\phi(x)$$ unscaled so its self-concordance constant stays fixed at $$1$$.
- **Pillar 3 — Strictly Feasible Interior Assumption:** The barrier method requires Slater's condition (a nonempty strict interior where $$h_i(x) < 0$$ and $$Ax = b$$) so that $$\operatorname{dom}(\phi)$$ is nonempty.
- **Pillar 4 — Convexity Preservation:** Because $$-\log(-u)$$ is convex and nondecreasing on $$(-\infty, 0)$$ and each $$h_i$$ is convex, the composition $$-\log(-h_i(x))$$ is guaranteed convex by the scalar composition rule.

### Step-by-Step Worked Example (Read Slowly): Solving the Barrier Subproblem Exactly on a 1D Interval

Minimize $$f(x) = \frac{1}{2}x^2 - 3x$$ subject to $$0 \le x \le 2$$ (i.e., $$h_1(x) = -x \le 0$$ and $$h_2(x) = x - 2 \le 0$$). Note the unconstrained minimum is $$x = 3$$, so the true constrained optimum is $$x^\star = 2$$.

1. **Write the scaled barrier problem $$\min_{0 < x < 2} t\left(\frac{1}{2}x^2 - 3x\right) - \log(x) - \log(2 - x)$$:**
2. **Set the first derivative to zero:**
   $$t(x - 3) - \frac{1}{x} + \frac{1}{2 - x} = 0.$$
3. **Evaluate the root $$x^*(t)$$ at $$t = 1$$ vs. $$t = 10$$:**
   - At $$t = 1$$: test $$x = 1.5$$: $$1(1.5 - 3) - \frac{1}{1.5} + \frac{1}{0.5} = -1.5 - 0.667 + 2.0 = -0.167 < 0$$. Test $$x = 1.55$$: $$-1.45 - 0.645 + 2.222 = +0.127 > 0$$. So $$x^*(1) \approx 1.53$$.
   - At $$t = 10$$: test $$x = 1.9$$: $$10(-1.1) - 0.526 + 10 = -1.526 < 0$$. Test $$x = 1.92$$: $$10(-1.08) - 0.521 + 12.5 = +1.179 > 0$$. So $$x^*(10) \approx 1.91$$.
4. **Watch the progression:** As $$t$$ grows from $$1 \to 10 \to \infty$$, $$x^*(t)$$ moves smoothly from $$1.53 \to 1.91 \to 2.0 = x^\star$$ while staying strictly inside $$(0, 2)$$.

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>
Before introducing the barrier method, let's first see how the indicator function can be approximated by a barrier function.

## Approximation of indicator function
In the following figure, you can see the indicator function and the barrier function. The dotted line is the indicator function $$I_C$$, and the solid lines are the barrier function $$\phi(x) = -1/t\log(-x)$$ for $$t = 0.5, 1, 2$$. The barrier function smoothly approximates the indicator function, and when $$t=2$$, it provides the best approximation.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_function_01.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">$$\text{[Fig 1] barrier function }\phi(x) = -1/t\log(-x) [1]$$</figcaption>
</p>
</figure>


## Logarithmic barrier function
Suppose $$h_1, \cdots , h_m : \mathbb{R}^n \to \mathbb{R}$$ are convex and twice differentiable. For the set $$ \{x : h_i(x) \lt 0, i = 1, \cdots , m \}$$, the following function is called the logarithmic barrier function.

>
\begin{align}
\phi(x) = - \sum_{i=1}^{m} \log(-h_i(x))
\end{align}

Here, the set is assumed to be the interior of the feasible set $$C$$ and is non-empty.

## Barrier method

Using the barrier function, the original problem can be approximated as follows. Here, $$t\gt 0$$.
>
$$\begin{align}
&\min_{x}           && f(x) + \frac{1}{t} \phi(x) & \qquad      & \min_{x} && tf(x) + \phi(x) \\
&\text{subject to } && Ax = b                     & \iff \qquad & \text{subject to } && Ax = b \\
\end{align}$$

The method of solving the problem defined in this way using Newton's method is called the **barrier method**.
