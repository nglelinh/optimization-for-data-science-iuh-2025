---
layout: post
title: 15-01 Barrier method and log barrier function
chapter: '15'
order: 2
owner: Minjoo Lee
categories:
- chapter15
lang: en
---

You already know how to use Newton's method when constraints are linear equalities $$Ax = b$$ (Chapter 14). How do we reuse that exact same Newton machinery when inequalities $$h_i(x) \le 0$$ enter the picture? Instead of inventing a separate combinatorial solver to guess active constraints, we fold all $$m$$ inequalities into the objective using a smooth **logarithmic barrier**—reducing the hardest convex problem class to a sequence of equality-constrained Newton solves.

## Key ideas: Bridging Equality-Constrained Newton to Inequalities

- **Pillar 1 — Reduction Strategy:** Inequality constraints $$h_i(x) \le 0$$ are absorbed into the objective so that only linear equalities $$Ax = b$$ remain explicit.
- **Pillar 2 — Strict Interior Domain:** Because $$\log(-h_i(x))$$ is finite only when $$h_i(x) < 0$$, every iterate stays strictly inside the feasible set—never touching or crossing a boundary wall.
- **Pillar 3 — Twice-Differentiable & Convex:** Whenever each $$h_i$$ is convex and $$C^2$$, the log barrier $$\phi(x) = -\sum_{i=1}^m \log(-h_i(x))$$ is also convex and $$C^2$$, making equality-constrained Newton directly applicable.
- **Pillar 4 — Parameterized Accuracy ($$t > 0$$):** Scaling $$f(x)$$ by $$t$$ (solving $$\min tf(x) + \phi(x)$$ s.t. $$Ax = b$$) controls the trade-off between staying well-centered away from walls (small $$t$$) and hugging the true optimal boundary (large $$t$$).

### Worked example: Reducing a Box-Constrained Problem to Unconstrained Smooth Minimization

Consider minimizing $$f(x) = (x - 2)^2$$ subject to $$-1 \le x \le 1$$ (written as $$h_1(x) = x - 1 \le 0$$ and $$h_2(x) = -x - 1 \le 0$$; true constrained optimum is $$x^\star = 1$$).

1. **Write the logarithmic barrier on $$(-1, 1)$$:**
   $$\phi(x) = -\log(1 - x) - \log(1 + x) = -\log(1 - x^2).$$
2. **Form the barrier subproblem for $$t = 1$$:**
   $$\min_{x \in (-1, 1)} \; (x - 2)^2 - \log(1 - x^2).$$
3. **Evaluate at the center $$x = 0$$ vs. near the wall $$x = 0.99$$:**
   - At $$x = 0$$: objective is $$(-2)^2 - \log(1) = 4.00$$.
   - At $$x = 0.7$$: objective is $$(-1.3)^2 - \log(0.51) \approx 1.69 + 0.673 = 2.363$$ (much lower!).
   - At $$x = 0.99$$: objective is $$(-1.01)^2 - \log(0.0199) \approx 1.02 + 3.917 = 4.937$$ (the barrier wall repels $$x$$ back inside!).
4. **Conclusion:** Smooth repulsion creates a clean interior minimum near $$x^*(1) \approx 0.71$$ where Newton's method converges effortlessly.

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

In the previous chapter, we explored how to solve an **equality constrained smooth problem** using Newton's method. In this chapter, we will look at methods for solving **inequality and equality constrained smooth problems**.

The basic idea is to transform the problem into an equality constrained smooth problem and solve it using Newton's method. This approach is called the **interior method**, and in this chapter, we will focus on one type of interior method: the **barrier method**.
