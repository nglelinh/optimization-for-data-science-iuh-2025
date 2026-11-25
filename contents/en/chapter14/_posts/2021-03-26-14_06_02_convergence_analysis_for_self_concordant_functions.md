---
layout: post
title: 14-06-02 Convergence analysis for self-concordant functions
chapter: '14'
order: 14
owner: Minjoo Lee
categories:
- chapter14
lang: en
---

With self-concordance in hand, Nesterov and Nemirovskii delivered one of the cleanest theorems in all of optimization: damped Newton's method reaches $$\epsilon$$-accuracy in at most $$C(\alpha,\beta)(f(x^{(0)}) - f^\star) + \log_2\log_2(1/\epsilon)$$ iterations. Notice what is *missing* from that formula: no dimension $$n$$, no condition number $$\kappa$$, no Lipschitz constant $$L$$, and no strong convexity $$m$$!

## Background Knowledge Map: Scale-Free Complexity of Damped Newton

- **Pillar 1 — Universal Damped-Phase Constant:** Whenever $$\lambda(x) > \eta$$ (a pure numerical constant independent of $$f$$), backtracking reduces $$f(x)$$ by at least a fixed constant $$\gamma(\alpha,\beta) > 0$$ per step.
- **Pillar 2 — Universal Quadratic-Phase Threshold:** Once $$\lambda(x) \le \frac{1}{4}$$ (or $$\eta$$), unit step $$t = 1$$ is always accepted and $$\lambda(x^+) \le 2\lambda(x)^2$$ (strictly quadratic contraction in the Newton decrement).
- **Pillar 3 — Suboptimality Bound Directly from $$\lambda(x)$$:** When $$\lambda(x) < 1$$, self-concordance guarantees $$f(x) - f^\star \le \lambda(x)^2$$ (for $$\lambda(x) \le 0.68$$), turning $$\lambda(x)$$ into an exact, rigorous stopping certificate.
- **Pillar 4 — Affine-Invariant Total Iteration Count:** Because $$f(x^{(0)}) - f^\star$$ and $$\epsilon$$ are unchanged under $$x = Ay + b$$, the entire iteration bound is strictly affine invariant.

### Step-by-Step Worked Example (Read Slowly): Estimating Total Newton Steps from the Self-Concordant Bound

Suppose a self-concordant problem starts with initial gap $$f(x^{(0)}) - f^\star = 5$$, and we use standard backtracking parameters $$\alpha = 0.1, \beta = 0.5$$ where the theoretical damped-phase constant is roughly $$C(\alpha,\beta) = \frac{1}{\gamma} \approx 20 / \alpha\beta$$ (in Boyd & Vandenberghe, Theorem 9.6, $$C(\alpha,\beta) = \frac{20 - 8\alpha}{\alpha\beta(1-2\alpha)^2}$$, while in practice the damped phase is even faster). Let's trace the Phase-II quadratic finish from $$\lambda(x^{(k)}) = 0.25$$ using the self-concordant recursion $$\lambda(x^+) \le \frac{\lambda(x)^2}{(1 - \lambda(x))^2}$$:

1. **Step 0:** $$\lambda_0 = 0.25$$.
2. **Step 1:** $$\lambda_1 \le \frac{0.25^2}{(0.75)^2} = \frac{1}{9} \approx 0.1111$$.
3. **Step 2:** $$\lambda_2 \le \frac{(1/9)^2}{(8/9)^2} = \frac{1}{64} \approx 0.01563$$.
4. **Step 3:** $$\lambda_3 \le \frac{(1/64)^2}{(63/64)^2} = \frac{1}{3969} \approx 2.52 \times 10^{-4}$$.
5. **Step 4:** $$\lambda_4 \le \frac{(2.52 \times 10^{-4})^2}{(1 - 2.52 \times 10^{-4})^2} \approx 6.35 \times 10^{-8}$$, giving $$f(x) - f^\star \le \lambda_4^2 \approx 4.0 \times 10^{-15}$$! Just 4 steps take you from $$0.25$$ to machine precision, matching the $$\log_2\log_2(1/\epsilon)$$ term.

For self-concordant functions, the result of convergence analysis is as follows:

>Theorem (Nesterov and Nemirovskii): Newton's method with backtracking line search requires the following number of iterations to achieve $$f(x^{(k)})-f^{\star}\leq \epsilon$$:
>\begin{align}
>C(\alpha, \beta)\big( f(x^{(0)}-f^{\star} \big) + \log\log{(1/\epsilon)},
>\end{align}
>where $$C(\alpha, \beta)$$ is a constant depending on $$\alpha, \beta$$.

The proof above is similar to the convergence analysis for Newton's method, but uses the properties of self-concordant functions to organize the steps. (See [1], p.503)