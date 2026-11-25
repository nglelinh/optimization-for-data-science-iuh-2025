---
layout: post
title: 14-02-03 Local convergence analyisis
chapter: '14'
order: 8
owner: Minjoo Lee
categories:
- chapter14
lang: en
---

Pure Newton's method is a high-performance race car with no brakes: start close enough to the finish line and it accelerates quadratically—turning an error of $$10^{-2}$$ into $$10^{-4}$$, then $$10^{-8}$$, then $$10^{-16}$$ in just three steps. Start too far away on a flat inflection region, however, and it can launch itself straight toward infinity. Local convergence theory draws the exact boundary between those two worlds.

## Background Knowledge Map: Anatomy of Local Convergence

- **Pillar 1 — Nonsingular Jacobian at the Root ($$F'(x^\star)$$ invertible):** Ensures the linear model around $$x^\star$$ is well-posed and gives a local contraction radius $$\delta > 0$$.
- **Pillar 2 — Superlinear Convergence from Continuity Alone:** Using first-order Taylor expansion $$0 = F(x^\star) = F(x^k) + F'(x^k)(x^\star - x^k) + o(\|x^k - x^\star\|)$$ immediately yields $$\|x^{k+1} - x^\star\| / \|x^k - x^\star\| \to 0$$.
- **Pillar 3 — Quadratic Convergence from Lipschitz Jacobian:** When $$\|F'(x) - F'(y)\| \le M\|x-y\|$$, the Taylor remainder shrinks to $$O(\|x^k - x^\star\|^2)$$, yielding $$\|x^{k+1} - x^\star\| \le K\|x^k - x^\star\|^2$$.
- **Pillar 4 — Failure Modes Outside the Local Basin:** If $$x^{(0)}$$ lands where $$F'(x^{(0)}) \approx 0$$ or the curvature bends away from the root (such as $$F(x) = \arctan(x)$$ at $$|x^{(0)}| > 1.3917$$), pure Newton oscillates or diverges.

### Step-by-Step Worked Example (Read Slowly): Contrasting Quadratic Convergence vs. Divergence on $$F(x) = \arctan(x)$$

Consider finding the unique root $$x^\star = 0$$ of $$F(x) = \arctan(x)$$, where $$F'(x) = \frac{1}{1+x^2}$$. The Newton update is
$$x^{(k+1)} = x^{(k)} - (1 + (x^{(k)})^2)\arctan(x^{(k)}).$$

1. **Inside the local basin ($$x^{(0)} = 0.5$$):**
   - $$x^{(1)} = 0.5 - (1.25)\arctan(0.5) \approx 0.5 - 1.25(0.46365) = -0.07956$$.
   - $$x^{(2)} = -0.07956 - (1.00633)(-0.07939) \approx +0.000336$$.
   - $$x^{(3)} \approx -2.5 \times 10^{-11}$$! (Here convergence is even *cubic* because $$F''(0) = 0$$!)
2. **Outside the local basin ($$x^{(0)} = 2.0$$):**
   - $$x^{(1)} = 2.0 - (1 + 4)\arctan(2.0) \approx 2.0 - 5(1.10715) = -3.5357$$.
   - $$x^{(2)} = -3.5357 - (1 + 12.501)(-1.2951) \approx +13.95$$.
   - The iterates explode alternating in sign! This exact failure is why we add backtracking line search in Section 14-04.

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
});
</script>

The second important property of Newton's method is that convergence is guaranteed near the solution when certain conditions are satisfied. This is called local convergence. Since the pure Newton's method we have discussed from [14-01]({% multilang_post_url contents/chapter14/2021-03-26-14_01_newton_method %}) does not guarantee convergence, we later devise the damped Newton's method that ensures convergence by adjusting the step size using the same backtracking line search covered in [Chapter 6]({% multilang_post_url contents/chapter06/21-03-20-06_00_gradient_descent %}), and analyze its convergence.


>Theorem: Let $$F : \mathbb{R}^{n}\, \rightarrow  \, \mathbb{R}^{n}$$ be continuously differentiable, and let $$x^{\star} \in \mathbb{R}^{n}$$ be a root of function $$F$$, i.e., $$F(x^{\star})=0$$.
>If $$F^{'}(x^{\star})$$ is non-singular, then the following (a) and (b) are satisfied: \\
>(a) If there exists a positive $$\delta$$ (>0) such that $$\| x^{(0)}-x^{\star} \|<\delta$$ and Newton's method is defined, then the following equation (converges superlinearly) is satisfied:
>\begin{align}
>\lim_{ k \rightarrow \infty } \frac{ \|\| x^{ (k+1) }-x^{ \star } \|\| } { \|\| x^{ (k) }-x^{ \star } \|\| } =0.
>\end{align} \\
>(b) If $$F^{'}$$ is Lipschitz continuous near $$x^{\star}$$, then there exists a positive K (>0) such that the following equation (quadratic convergence) is satisfied:
>\begin{align}
>\|\|x^{ (k+1) } - x^{ \star }\|\| \leq K \|\| x^{ (k) }-x^{ \star }\|\|^{2}.
>\end{align}

## Proof of (a)
>We organize $$F(x^{\star})$$ up to 1st order using Taylor expansion. Since 2nd order and higher terms are bounded by a constant multiple of the norm of the 1st order term, we can represent it using little-o notation as follows:
>\begin{align}
>0=F(x^{\star}) = F(x^{k}) +\nabla F(x^{k})(x^{\star}-x^{k})+o(\|\|x^{k}-x^{\star}\|\|).\\
>\end{align}
>Multiply both sides by $$\nabla F(x^{k})^{-1}$$ and organize. Since little-o is treated as a constant term, it can be ignored.
>\begin{align}
>x^{k}-x^{\star}-\nabla F(x^{k})^{-1} F(x^{k}) = o(\|\|x^{k}-x^{\star}\|\|).
>\end{align}
>Using Newton's method $$x^{k+1}=x^{k}-\nabla F(x^{k})^{-1}F(x^{k})$$, we can obtain the following result:
>\begin{align}
>x^{k+1}-x^{\star}=o(\|\|x^{k}-x^{\star}\|\|),
>\end{align}
>Therefore, when $$x^{k} \neq x^{\star}$$, we can prove (a) using the limit-definition of little-o [[wikipedia](https://en.wikipedia.org/wiki/Big_O_notation)].

>\begin{align}
>\lim_{k\rightarrow \infty} \frac{\|\|x^{k+1}-x^{\star}\|\|}{\|\|x^{k}-x^{\star}\|\|} = \lim_{k\rightarrow \infty}\frac{o(\|\|x^{k}-x^{\star}\|\|)}{\|\|x^{k}-x^{\star}\|\|}.
>\end{align}

## Proof of (b)
The process is identical to proving that the convergence rate in the Damped phase of [[14-05]({% multilang_post_url contents/chapter14/2021-03-26-14_05_convergence_analysis %})] is quadratic. Therefore, it is omitted.

## Example : divergence case
We briefly examine an example where convergence is not guaranteed with pure Newton's method.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/1_.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig 1] pure Newton's method applied on root finding : divergence case </figcaption>
</p>
</figure>

[image-link](https://slideplayer.com/slide/4998677/)

As shown in the figure, depending on the initial point $$x_0$$, the solution can diverge.
