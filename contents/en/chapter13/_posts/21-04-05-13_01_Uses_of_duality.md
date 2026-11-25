---
layout: post
title: 13-01 Uses of duality
chapter: '13'
order: 2
owner: Wontak Ryu
categories:
- chapter13
lang: en
---

A classic headache in numerical optimization is deciding *when to stop*. If an iterative solver slows down and the objective barely changes from step $$k$$ to step $$k+1$$, have you actually reached the optimum, or are you merely crawling across a flat plateau? The duality gap removes the guesswork: it replaces heuristic stopping rules with a rigorous mathematical guarantee of how far you can possibly be from $$f^\star$$.

## Background Knowledge Map: Certificates and Primal Recovery

- **Pillar 1 — Weak Duality as a Lower-Bound Engine:** Because $$g(u,v) \le f^\star$$ holds unconditionally for every dual-feasible $$(u,v)$$, any primal-feasible $$x$$ immediately traps $$f^\star$$ inside $$[g(u,v), f(x)]$$.
- **Pillar 2 — The Duality Gap as a Stopping Criterion:** Rearranging weak duality gives $$f(x) - f^\star \le f(x) - g(u,v)$$. Terminating when $$f(x) - g(u,v) \le \varepsilon$$ guarantees $$\varepsilon$$-suboptimality with zero assumptions on step sizes.
- **Pillar 3 — Strong Duality & Lagrangian Minimization:** When $$f^\star = g^\star$$, any primal optimum $$x^\star$$ must minimize $$L(x, u^\star, v^\star)$$ over all $$x$$. Thus solving the dual first pins down the primal via an unconstrained minimization.
- **Pillar 4 — Uniqueness & Direct Primal Extraction:** Whenever $$x \mapsto L(x, u^\star, v^\star)$$ has a unique minimizer (e.g., strictly convex $$f$$), that minimizer is automatically primal feasible and equals $$x^\star$$.

### Step-by-Step Worked Example (Read Slowly): Certifying Suboptimality and Recovering $$x^\star$$

Suppose we minimize $$f(x) = x_1^2 + 2x_2^2$$ subject to $$x_1 + x_2 = 6$$.

1. **Construct the Lagrangian and dual function:**
   $$L(x_1, x_2, v) = x_1^2 + 2x_2^2 + v(6 - x_1 - x_2).$$
   Setting $$\nabla_x L = 0$$ gives $$2x_1 = v \implies x_1 = \frac{v}{2}$$ and $$4x_2 = v \implies x_2 = \frac{v}{4}$$. Substituting back:
   $$g(v) = \frac{v^2}{4} + 2\frac{v^2}{16} + 6v - \frac{3v^2}{4} = 6v - \frac{3}{8}v^2.$$
2. **Test a suboptimal feasible pair for the duality gap:** Pick primal feasible $$x = (3, 3)$$ (since $$3+3=6$$) and dual feasible $$v = 6$$.
   - Primal value: $$f(3,3) = 9 + 18 = 27$$.
   - Dual value: $$g(6) = 36 - \frac{3}{8}(36) = 36 - 13.5 = 22.5$$.
   - Duality gap: $$27 - 22.5 = 4.5$$, proving $$f(3,3) - f^\star \le 4.5$$ without solving the primal!
3. **Solve the scalar dual:** Maximize $$g(v) = 6v - \frac{3}{8}v^2$$ by setting $$g'(v) = 6 - \frac{3}{4}v = 0 \implies v^\star = 8$$, giving $$g(8) = 48 - 24 = 24$$.
4. **Recover the primal from $$v^\star = 8$$:** Because $$L(\cdot, 8)$$ is strictly convex, its unique minimizer is
   $$x_1^\star = \frac{8}{2} = 4, \qquad x_2^\star = \frac{8}{4} = 2.$$
   Check: $$x_1^\star + x_2^\star = 6$$ and $$f(4,2) = 16 + 8 = 24 = g(8)$$, confirming zero duality gap.

### Two key uses of duality
Let's revisit the two key characteristics of duality covered in Chapter 11.

• When $$x$$ is primal feasible and $$u,v$$ are dual feasible, the difference between the primal problem $$f(x)$$ and the dual problem $$g(u,v)$$ is called the **duality gap** between $$x$$ and $$u,v$$.
> $$f(x)-f^{\star}  \le f(x)-g(u, v)$$

When the duality gap is 0, this is called zero duality gap, which means that the solution to the dual problem is optimal.
Also, the upper bound $$g(u, v)$$ is always less than or equal to the optimal value $$f^{\star}$$. For detailed reasons, please refer to the content in [[Chapter 11]]({% multilang_post_url contents/chapter11/21-03-24-11_00_Duality_in_General_Programs %}).
Therefore, the following derivation is possible.

#### [Proof]
> $$\begin{align*}
> f^{\star} &\ge g(u, v) \\
> -f^{\star} &\le -g(u, v) \\
> f(x)-f^{\star} &\le \underbrace{f(x)-g(u, v)}_{\text{duality gap}}\\
> g^{\star}-g(x) &\le \underbrace{f(x)-g(u, v)}_{\text{duality gap}}\\
> \end{align*}$$


Moreover, the duality gap can be used as a stopping criterion for algorithms.
• When dual optimal $$u^{\star}, v^{\star}$$ are given, under the condition of strong duality, the primal solution minimizes the Lagrangian $$L (x, u^{\star}, v^{\star})$$ for all $$x$$ (i.e., satisfies the stationarity condition).

This can be used for computing the primal solution.
