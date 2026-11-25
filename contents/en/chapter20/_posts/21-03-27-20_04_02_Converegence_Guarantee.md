---
layout: post
title: 20-04-02 Convergence Guarantee
chapter: '20'
order: 10
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

One of the reasons ADMM became a staple across machine learning, signal processing, and control is how *forgiving* its convergence theorem is: you do not need $$f$$ or $$g$$ to be differentiable, you do not need strong convexity, and you do not even need $$A$$ or $$B$$ to have full rank! As long as $$f$$ and $$g$$ are closed, proper, convex functions and the unaugmented Lagrangian has a saddle point, ADMM is guaranteed to drive primal residuals to zero and converge to the exact optimal objective for *every* $$\rho > 0$$.

## Key ideas: What ADMM Guarantees—and What It Does Not

- **Three Core Convergence Pillars:** Under minimal convexity + saddle-point assumptions, ADMM guarantees: (1) primal residual $$r^{(k)} = Ax^{(k)} + Bz^{(k)} - c \to 0$$, (2) objective value $$f(x^{(k)}) + g(z^{(k)}) \to p^\star$$, and (3) dual multiplier $$u^{(k)} \to u^\star$$.
- **Lyapunov Energy Proof Intuition:** Defining the energy $$V^k = \frac{1}{\rho}\|u^k - u^\star\|_2^2 + \rho\|B(z^k - z^\star)\|_2^2$$, Boyd et al. show $$V^{k+1} \le V^k - \rho\|r^{k+1}\|_2^2 - \rho\|B(z^{k+1} - z^k)\|_2^2$$. Telescoping this inequality immediately proves $$\sum_k (\|r^k\|^2 + \|B(z^k - z^{k-1})\|^2) < \infty$$!
- **Why Primal Iterates May Not Converge Without Extra Assumptions:** If $$f$$ or $$g$$ is not strictly convex (e.g., an LP with a flat optimal face), $$f(x^k) + g(z^k) \to p^\star$$ and $$r^k \to 0$$ still hold, though individual iterates $$(x^k, z^k)$$ need not settle on a single point unless $$A, B$$ have full column rank.
- **Rate Landscape ($$O(1/k)$$ vs. Linear):** Ergodic ADMM converges at $$O(1/k)$$ generally, and jumps to **linear convergence** when at least one block is smooth and strongly convex (Deng & Yin; Nishihara et al.)—making it ideal for modest-to-medium accuracy ($$10^{-3}\text{–}10^{-5}$$) at massive scale.

### Worked example: Verifying Monotonic Decay of the ADMM Lyapunov Function

Using the exact iterates from Lesson 20-04-01 ($$\min \frac{1}{2}(x-4)^2 + \frac{1}{2}z^2$$ s.t. $$x - z = 0$$, $$\rho = 1$$, exact optimum $$x^\star = z^\star = u^\star = 2$$):
- $$k = 0$$: $$z^0 = 0, \; u^0 = 0$$.
- $$k = 1$$: $$x^1 = 2, \; z^1 = 1, \; u^1 = 1, \; r^1 = 1$$.
- $$k = 2$$: $$x^2 = 2, \; z^2 = 1.5, \; u^2 = 1.5, \; r^2 = 0.5$$.

1. **Compute the Lyapunov energy $$V^k = \|u^k - u^\star\|^2 + \|z^k - z^\star\|^2$$:**
   - $$V^0 = (0 - 2)^2 + (0 - 2)^2 = 4 + 4 = 8.0$$.
   - $$V^1 = (1 - 2)^2 + (1 - 2)^2 = 1 + 1 = 2.0$$.
   - $$V^2 = (1.5 - 2)^2 + (1.5 - 2)^2 = 0.25 + 0.25 = 0.5$$.
2. **Verify the exact dissipation inequality $$V^{k+1} \le V^k - \|r^{k+1}\|^2 - \|z^{k+1} - z^k\|^2$$:**
   - From $$k = 0 \to 1$$: $$V^0 - \|r^1\|^2 - \|z^1 - z^0\|^2 = 8 - 1^2 - 1^2 = 6.0 \ge 2.0 = V^1$$ $$\checkmark$$!
   - From $$k = 1 \to 2$$: $$V^1 - \|r^2\|^2 - \|z^2 - z^1\|^2 = 2 - 0.5^2 - 0.5^2 = 1.5 \ge 0.5 = V^2$$ $$\checkmark$$!
3. **Insight:**
   Because $$V^k \ge 0$$ drops by at least $$\|r^{k+1}\|^2 + \|z^{k+1} - z^k\|^2$$ at every step, the sum of squared residuals is bounded above by $$V^0 = 8$$—guaranteeing $$r^k \to 0$$ and $$s^k \to 0$$!

# Convergence Guarantee for ADMM

Under appropriate conditions on $$f$$ and $$g$$ (note that $$A$$ and $$B$$ do not need to be full rank), ADMM satisfies the following for all $$\rho > 0$$:

* **Residual convergence**: As $$k \to \infty$$, $$r^{(k)} = Ax^{(k)} + Bz^{(k)} - c \to 0$$, meaning the primal iterates approach feasibility.

* **Objective convergence**: $$f(x^{(k)}) + g(z^{(k)}) \to f^{\ast} + g^{\ast}$$, where $$f^{\ast} + g^{\ast}$$ is the optimal primal objective value.

* **Dual convergence**: $$u^{(k)} \to u^{\ast}$$, where $$u^{\ast}$$ is the dual solution.

The exact convergence rate is not yet fully understood, and much research is currently ongoing in this area. Roughly speaking, ADMM performs similarly to or slightly better than first-order methods. 
