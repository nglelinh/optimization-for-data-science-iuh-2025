---
layout: post
title: 12-01 Karush-Kuhn-Tucker conditions
chapter: '12'
order: 2
owner: Wontak Ryu
categories:
- chapter12
lang: en
lesson_type: required
---

Why do the four KKT conditions—stationarity, complementary slackness, primal feasibility, and dual feasibility—capture optimality so completely? The answer is not a long list of messy calculus lemmas; it is a breathtakingly short chain of inequalities linking the primal objective $$f(x^\star)$$, the Lagrangian $$L(x^\star, u^\star, v^\star)$$, and the dual function $$g(u^\star, v^\star)$$! Watching how zero duality gap collapses that chain into equalities shows immediately why KKT is necessary under strong duality and sufficient under convexity.

## Background Knowledge Map: Proving Necessity & Sufficiency of KKT

- **Pillar 1 — The Collapse Chain Under Strong Duality (Necessity):** When $$f(x^\star) = g(u^\star, v^\star)$$, we have $$f(x^\star) = \inf_x L(x, u^\star, v^\star) \le L(x^\star, u^\star, v^\star) = f(x^\star) + \sum u_i^\star h_i(x^\star) \le f(x^\star)$$. Every inequality in the chain must be an equality!
- **Pillar 2 — Reading Stationarity & Complementary Slackness Off the Chain:** The first equality forces $$x^\star \in \arg\min_x L(x, u^\star, v^\star)$$ (giving stationarity $$0 \in \partial_x L(x^\star, u^\star, v^\star)$$); the second equality forces $$\sum u_i^\star h_i(x^\star) = 0$$, and since every term is $$\le 0$$, each individual term $$u_i^\star h_i(x^\star) = 0$$ (complementary slackness)!
- **Pillar 3 — Reverse Direction Under Convexity (Sufficiency):** When $$f, h_i$$ are convex and $$l_j$$ are affine, $$L(\cdot, u^\star, v^\star)$$ is convex in $$x$$. Stationarity then *guarantees* $$x^\star$$ minimizes $$L(\cdot, u^\star, v^\star)$$ globally, so $$g(u^\star, v^\star) = L(x^\star, u^\star, v^\star) = f(x^\star)$$ (via complementary slackness)—proving zero duality gap and global optimality!
- **Pillar 4 — Caution on Nonconvex & Degenerate Problems:** For nonconvex problems, KKT points can be local minima, saddle points, or even maxima; for convex problems without Slater's condition, an optimal primal point may exist with *no* finite KKT multiplier!

### Step-by-Step Worked Example (Read Slowly): A Convex Problem Where KKT Has No Solution (Slater Fails!)

Consider the convex problem $$\min_{x \in \mathbb{R}} f(x) = x$$ subject to $$h(x) = x^2 \le 0$$.

1. **Find the exact primal optimum by inspection:** The only real number with $$x^2 \le 0$$ is $$x^\star = 0$$, so $$x^\star = 0$$ is undeniably the unique global minimizer with $$f^\star = 0$$.
2. **Test the KKT stationarity condition at $$x^\star = 0$$:**
   - $$L(x, u) = x + u x^2$$.
   - Stationarity: $$\frac{\partial L}{\partial x}\Big|_{x=0} = 1 + 2 u (0) = 1 = 0$$ — **contradiction!**
3. **Why did KKT fail at the true global optimum?** Because $$h(x) = x^2 \le 0$$ has *no* strictly feasible point ($$x^2 < 0$$ is impossible), so **Slater's condition fails**! Geometrically, $$\nabla h(0) = 0$$ vanishes at the boundary, leaving no normal vector available to balance $$\nabla f(0) = 1$$. This 3-line counterexample permanently cements why Slater's condition is essential for KKT necessity!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Let us consider the following general optimization problem.

>$$
>\begin{align}
>    &\min_{x} &&{f(x)} \\\\
>    &\text{subject to } &&{h_i(x) \le 0, \text{ } i=1,\dots,m} \\\\
>    & &&{l_j(x) = 0, \text{ } j=1,\dots,r}.\\\\
>\end{align}
>$$

The **Karush–Kuhn–Tucker (KKT) conditions** or **KKT conditions** consist of the following conditions [3].

* $$0 \in \partial \big( f(x) + \sum_{i=1}^{m} \lambda_i h_i(x) + \sum_{j=1}^{r} \nu_j l_j(x) \big)$$ (Stationarity): When $$\lambda, \nu$$ are fixed, the subdifferential with respect to $$x$$ contains 0. 
* $$\lambda_i \cdot h_i(x) = 0 \text{ for all } i$$ (Complementary Slackness):  At least one of $$\lambda_i$$ and $$h_i$$ has value 0.
* $$h_i(x) \le 0, l_j(x) = 0 \text{ for all } i, j$$ (Primal Feasibility): Indicates whether the constraints of the primal problem are satisfied.
* $$\lambda_i \ge 0 \text{ for all } i$$ (Dual Feasibility): Indicates whether the constraints of the dual problem are satisfied.

## Sufficiency
For a convex primal problem, when there exist $$x^\star, \lambda^\star, \nu^\star$$ that satisfy the KKT conditions, the following process shows that $$x^\star, \lambda^\star, \nu^\star$$ are primal & dual solutions with zero duality gap.

>$$
>\begin{align}
>    g(\lambda^\star, \nu^\star) &= \min_x L(x, \lambda^\star, \nu^\star) \\\\
>                                &= L(x^\star, \lambda^\star, \nu^\star) \\\\
>                                &= f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) \\\\
>                                &= f(x^\star)
>\end{align}
>$$

1. $$L(x,\lambda^\star,\nu^\star) = f(x) + \sum_{i=1}^{m} \lambda_i^\star h_i(x) + \sum_{j=1}^{r} \nu_j^\star l_j(x)$$ is a convex function. (sum of convex functions) 
2. $$0 \in \partial \big( f(x^\star) + \sum_{i=1}^{m} \lambda_i^\star h_i(x^\star) + \sum_{j=1}^{r} \nu_j^\star l_j(x^\star) \big)$$therefore $$\min_x L(x, \lambda^\star, \nu^\star) = L(x^\star, \lambda^\star, \nu^\star)$$.
3. By complementary slackness and primal feasibility, $$f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) = f(x^\star)$$.

## Necessity
When $$x^\star, \lambda^\star, \nu^\star$$ are primal & dual solutions with zero duality gap (for example, satisfying Slater's condition), all the inequalities below become equalities, so in this problem $$x^\star, \lambda^\star, \nu^\star$$ satisfy the KKT conditions.
>$$
>\begin{align}
>    f(x^\star) &= g(\lambda^\star, \nu^\star) \\\\
>                   &= \min_x  \big( f(x) + \sum_{i=1}^{m} \lambda_i^\star h_i(x) + \sum_{j=1}^{r} \nu_j^\star l_j(x) \big) \\\\
>                   &\le f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) \\\\
>                   &\le f(x^\star)
>\end{align}
>$$

1. $$f(x^\star) = g(\lambda^\star, \nu^\star)$$ means zero duality gap.
2. To satisfy $$f(x^\star) + \sum_{i=1}^m \underbrace{\lambda_i^\star h_i(x^\star)}_{0} + \sum_{j=1}^r \underbrace{\nu_j^\star l_j(x^\star)}_{0} = f(x^\star)$$, complementary slackness and primal feasibility must be satisfied.
3. If $$f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) = f(x^\star)$$ is satisfied, all inequalities in the above derivation become equalities.

## Putting it together
In summary, KKT conditions are:

* Sufficient conditions for primal & dual solutions with zero duality gap.
* If strong duality holds, they become necessary conditions for primal & dual solutions.

That is, for problems that satisfy strong duality, the following relationship holds.
>$$
>\begin{align}
>    x^\star, \lambda^\star, \nu^\star \text{ are primal and dual solutions} \\\\
>    \Leftrightarrow x^\star, \lambda^\star, \nu^\star \text{ satisfy the KKT conditions} \\\\
>\end{align}
>$$

### KKT through water-filling in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/kkt-water-filling_en.mp4"></video>
</div>

Solving water-filling with α = (0.1, 0.4, 0.8, 1.2) through the four KKT conditions, reading the meaning of λ, and three wrong guesses that KKT rules out.
