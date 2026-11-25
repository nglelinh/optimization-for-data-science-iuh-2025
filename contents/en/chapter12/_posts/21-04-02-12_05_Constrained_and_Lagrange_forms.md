---
layout: post
title: 12-05 Constrained and Lagrange forms
chapter: '12'
order: 6
owner: Wontak Ryu
categories:
- chapter12
lang: en
---

Open two statistics textbooks on Lasso or Ridge regression and you will see two seemingly different optimization problems: one minimizes loss subject to a hard norm budget $$\|\beta\|_1 \le t$$ (**Constrained form**), while the other minimizes loss plus a penalty $$\lambda \|\beta\|_1$$ (**Lagrange form**). Are these two problems really the same? Using the KKT conditions, this lesson proves a clean, exact equivalence—and flags the one subtle edge case (strictly non-binding budgets vs. zero multipliers) where the two forms part ways!

## Key ideas: Bridging Constrained (C) and Lagrange (L) Forms

- **Pillar 1 — Comparing the Two Stationarity Equations:** For convex $$f, h$$, the constrained form $$\min \{ f(x) : h(x) \le t \}$$ has KKT stationarity $$0 \in \partial f(x^\star) + \lambda^\star \partial h(x^\star)$$ with $$\lambda^\star \ge 0$$ and $$\lambda^\star(h(x^\star) - t) = 0$$; the unconstrained Lagrange form $$\min_x f(x) + \lambda h(x)$$ has stationarity $$0 \in \partial f(x^\star) + \lambda \partial h(x^\star)$$.
- **Pillar 2 — From (C) to (L) via Slater's Condition:** If $$x^\star$$ solves (C) and Slater's condition holds, KKT guarantees a multiplier $$\lambda^\star \ge 0$$ such that $$0 \in \partial f(x^\star) + \lambda^\star \partial h(x^\star)$$, meaning $$x^\star$$ *also* solves (L) for $$\lambda = \lambda^\star$$!
- **Pillar 3 — From (L) to (C) via Tight Budget $$t = h(x^\star)$$:** Conversely, if $$x^\star$$ solves (L) for some $$\lambda \ge 0$$, simply setting $$t = h(x^\star)$$ makes primal feasibility ($$h(x^\star) \le t$$) and complementary slackness ($$\lambda(h(x^\star) - t) = 0$$) hold *identically*, so $$x^\star$$ solves (C) with $$t = h(x^\star)$$!
- **Pillar 4 — Subtle Caveat (Why the Mapping $$\lambda \leftrightarrow t$$ Is Not Always 1-to-1):** If $$f$$ is not strictly convex (or if $$t$$ exceeds the unconstrained minimum's norm), a single $$\lambda$$ can correspond to a *whole set* of solutions with different values of $$h(x)$$, and for nonconvex $$f, h$$, the Lagrange form can actually *miss* constrained optima located on nonconvex dents of the Pareto frontier!

### Worked example: Mapping $$\lambda \leftrightarrow t$$ Explicitly on 1D Ridge Regression

Let $$f(x) = \frac{1}{2}(x - 4)^2$$ and $$h(x) = \frac{1}{2}x^2$$.

1. **Solve the Lagrange Form (L) for any $$\lambda \ge 0$$:**
   $$\min_x\; \frac{1}{2}(x - 4)^2 + \frac{\lambda}{2} x^2 \implies (x - 4) + \lambda x = 0 \implies x_L^\star(\lambda) = \frac{4}{1 + \lambda}.$$
   - For $$\lambda = 1$$: $$x_L^\star(1) = \frac{4}{2} = 2$$, with $$h(2) = \frac{1}{2}(2^2) = 2$$.
2. **Solve the Constrained Form (C) with budget $$t = 2$$ (i.e., $$\frac{1}{2}x^2 \le 2 \iff |x| \le 2$$):**
   - Since the unconstrained minimum $$x = 4$$ lies outside $$[-2, 2]$$, the constraint binds at $$x_C^\star(2) = 2$$!
   - KKT stationarity: $$(2 - 4) + \lambda^\star (2) = 0 \implies \lambda^\star = 1$$—recovering the exact Lagrange parameter!
3. **Check the non-binding regime ($$t = 12 \implies |x| \le \sqrt{24} \approx 4.90$$):**
   - Now $$x = 4$$ is strictly feasible ($$h(4) = 8 < 12$$), so complementary slackness forces $$\lambda^\star = 0$$ for *every* $$t \ge 8$$—confirming that $$\lambda(t) = \max\!\left(0,\; \frac{4}{\sqrt{2t}} - 1\right)$$ maps $$t \in (0, 8]$$ bijectively onto $$\lambda \in [0, \infty)$$ and collapses all $$t \ge 8$$ onto $$\lambda = 0$$!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
displayAlign: "center"
});
</script>

In statistics and machine learning, we often move between **constrained form** and **Lagrange form**. Let us define the constrained form and Lagrangian form as follows.

### Constrained Form ((C) hereafter)

>$$
>\min_x \: f(x) \quad \text{ subject to } h(x) \le t,\\\\
>\text{where } t \in \mathbb{R} \text{ is a tuning parameter.}
>$$

### Lagrange Form ((L) hereafter)

>$$
>\min_x \: f(x) + \lambda \cdot h(x),\\\\
>\text{where } \lambda \ge 0 \text{ is a tuning parameter.}
>$$

When $$f, h$$ are convex, let us examine the cases where the two problems yield the same solution.

1. **(C) to (L):** When (C) is strictly feasible (satisfies Slater's condition) and satisfies strong duality, if there exists a dual solution $$\lambda^\star \ge 0$$ that minimizes the following objective function for the solution $$x^\star$$ of (C), then $$x^\star$$ is also a solution of (L).

$$f(x) + \lambda \cdot (h(x) - t)$$

2. **(L) to (C):** If $$x^\star$$ is a solution of (L) and (C) with $$t = h(x^\star)$$ satisfies the KKT conditions, then $$x^\star$$ is also a solution of (C). This is because $$\lambda^\star, x^\star$$ that satisfy the KKT conditions of (L) also satisfy the KKT conditions of (C) with $$t = h(x^\star)$$.

>**$$\rightarrow$$ KKT conditions of (L):**
>
> $$
> \begin{align}
> \nabla_x f(x^\star) + \lambda^\star \nabla_x h(x^\star) &= 0\\\\
> \lambda^\star &\ge 0\\\\
> \end{align}
> $$
>
>
>**$$\rightarrow$$ KKT conditions of (C) with $$t = h(x^\star)$$:**
>
> $$
> \begin{align}
> \nabla_x f(x^\star) + \lambda^\star \nabla_x h(x^\star) &= 0\\\\
> \lambda^\star &\ge 0\\\\
> \lambda^\star (\underbrace{h(x^\star) - h(x^\star)}_{=0}) &= 0
> \end{align}
> $$

In conclusion, 1 and 2 show the following relationships respectively.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter12/conclusion.png" alt="" width="70%" height="70%">
  <figcaption style="text-align: center;">[Fig1] Conclusion [3]</figcaption>
</p>
</figure>

So, under what circumstances do (C) and (L) show perfect equivalence?<br/>
For example, when $$h(x) \ge 0$$ (such as norm), $$t = 0$$, and $$\lambda = \infty$$, perfect equivalence is shown. Due to the given conditions, the constraint in (C) becomes $$h(x) = 0$$, and by setting $$\lambda$$ to $$\infty$$, (L) also imposes the same constraint ($$h(x) = 0$$).

### Try it yourself: constrained vs. Lagrange form

<div class="opx-explainer" data-opx="cl" data-lang="en"></div>
