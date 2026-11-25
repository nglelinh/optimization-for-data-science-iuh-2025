---
layout: post
title: 15-03-01 Perturbed KKT conditions
chapter: "15"
order: 8
categories:
- chapter16
lang: en
---

Why are the exact KKT conditions so hard to solve directly with Newton's method? Because complementary slackness $$u_i^\star h_i(x^\star) = 0$$ forms a sharp L-shaped corner at the origin: either $$u_i = 0$$ or $$h_i = 0$$. The log barrier magically rounds that sharp L-corner into the smooth hyperbola $$u_i(t) h_i(x^*(t)) = -\frac{1}{t}$$—keeping every variable strictly nonzero so the Jacobian stays smooth and nonsingular!

## Key ideas: Exact KKT vs. Perturbed KKT

- **Pillar 1 — Stationarity Matches Exactly:** Dividing the barrier optimality condition $$t\nabla f(x^*(t)) - \sum \frac{1}{h_i}\nabla h_i + A^T w = 0$$ by $$t$$ and setting $$u_i(t) = -\frac{1}{t h_i(x^*(t))}$$, $$v(t) = \frac{1}{t}w$$ yields exact KKT stationarity $$\nabla f + \sum u_i \nabla h_i + A^T v = 0$$.
- **Pillar 2 — Strict Primal and Dual Feasibility:** Because $$h_i(x^*(t)) < 0$$ and $$t > 0$$, we automatically get $$u_i(t) > 0$$—meaning $$(u(t), v(t))$$ is *strictly dual feasible* at every single point on the central path!
- **Pillar 3 — Hyperbolic Complementarity ($$u_i h_i = -1/t$$):** The sole difference between central-path KKT and true KKT is replacing $$0$$ with $$-1/t$$.
- **Pillar 4 — Smooth Limit to Optimality:** As $$t \to \infty$$, the hyperbola $$u_i h_i = -1/t$$ hugs the coordinate axes tighter and tighter until it collapses onto exact complementary slackness $$u_i^\star h_i(x^\star) = 0$$.

### Worked example: Checking All Four Perturbed KKT Conditions Explicitly

Consider $$\min_{x} \frac{1}{2}x^2$$ subject to $$h_1(x) = 2 - x \le 0$$ (i.e., $$x \ge 2$$; true KKT solution: $$x^\star = 2, u_1^\star = 2$$). Solve the barrier problem at $$t = 1$$: $$\min_{x > 2} \frac{1}{2}x^2 - \log(x - 2)$$.

1. **Find $$x^*(1)$$ from stationarity:**
   $$x - \frac{1}{x - 2} = 0 \implies x^2 - 2x - 1 = 0 \implies x^*(1) = 1 + \sqrt{2} \approx 2.4142 \quad (\text{since } x > 2).$$
2. **Compute the central-path dual multiplier $$u_1(1)$$:**
   $$h_1(x^*(1)) = 2 - (1 + \sqrt{2}) = 1 - \sqrt{2} \approx -0.4142 < 0.$$
   $$u_1(1) = -\frac{1}{1 \cdot (1 - \sqrt{2})} = \frac{1}{\sqrt{2} - 1} = \sqrt{2} + 1 \approx 2.4142 > 0.$$
3. **Verify all four perturbed KKT conditions:**
   - Primal feasibility: $$h_1(2.4142) = -0.4142 < 0$$ (strictly feasible).
   - Dual feasibility: $$u_1(1) = 2.4142 > 0$$ (strictly feasible).
   - Stationarity: $$\nabla f(x^*(1)) + u_1(1)\nabla h_1(x^*(1)) = (1 + \sqrt{2}) + (1 + \sqrt{2})(-1) = 0$$ (exact!).
   - Perturbed complementarity: $$u_1(1) \cdot h_1(x^*(1)) = (\sqrt{2}+1)(1-\sqrt{2}) = 1 - 2 = -1 = -\frac{1}{t}$$ (exact!).

If we derive the KKT conditions from the barrier problem and the original formulation, we get the following.
## KKT conditions for barrier problem
The second term in the KKT conditions for the barrier problem is derived using the gradient of the log barrier function.
>
$$\begin{align}
t \nabla f(x^*(t)) - \sum_{i=1}^{m} \frac{1}{h_i(x^*(t))} \nabla h_i(x^*(t)) + A^Tw = 0  \\\ 
 Ax^*(t) = b, \quad h_i(x^*(t)) \lt 0, \quad i = 1, \cdots , m \\\
\end{align}$$

##  KKT conditions for the original problem
In the KKT conditions for the original problem, complementary slackness gives $$h_i(x^*) \cdot u_i^* = 0$$, but in practice, it is very difficult to know this boundary condition.
>
$$\begin{align}
\nabla f(x^*) + \sum_{i=1}^{m} u_i^* \nabla h_i(x^*) + A^Tv^* = 0 \\\ 
Ax^* = b, \quad h_i(x^*) \le 0, \quad u_i^* \ge 0,   \\\ 
h_i(x^*) \cdot u_i^* = 0,  \quad i = 1, \cdots , m \\\
\end{align}$$


## Redefinition of KKT conditions for barrier problem
So, what is the relationship between these two KKT conditions?

First, let $$u_i(t)$$ and $$v$$ be defined as follows:
>
$$\begin{align}
u_i(t) = - \frac{1}{t h_i(x^*(t))}, \quad v = \frac{1}{t}w
\end{align}$$

Let's redefine the KKT conditions for the barrier problem.

Looking at the redefined problem, we see that the KKT conditions are almost identical to those for the original problem. In this equation, $$u_i(t) \cdot   h_i(x^*(t)) = - \frac{1}{t}$$ becomes 0 as $$t \to \infty$$, which matches $$h_i(x^*) \cdot u_i^* = 0$$ in the original formulation.

>
$$\begin{align}
& \nabla f(x^*(t)) + \sum_{i=1}^{m} u_i(t) \nabla h_i(x^*(t)) + tA^Tv = 0  \\\ 
& Ax^*(t) = b, \quad u_i(t) \cdot   h_i(x^*(t)) = - \frac{1}{t}, \quad h_i(x^*(t)) \lt 0, \quad u_i(t) \gt 0 , \quad i = 1, \cdots , m \\\
\end{align}$$