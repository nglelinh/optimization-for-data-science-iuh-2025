---
layout: post
title: 15-03 Properties and interpretation
chapter: "15"
order: 7
owner: "Minjoo Lee"
categories:
- chapter16
lang: en
---

At first glance, replacing a constrained optimization problem with a log-barrier objective $$tf(x) + \phi(x)$$ looks like a rough heuristic approximation. How do we know $$x^*(t)$$ is actually close to $$x^\star$$—and *how close* is it? Section 15-03 reveals the magic behind the scenes: the optimality conditions of the barrier problem are *identical* to the true KKT conditions except for a single controlled perturbation $$u_i h_i = -1/t$$, which hands us an exact, universal suboptimality bound $$m/t$$.

## Background Knowledge Map: Connecting the Barrier to KKT & Duality

- **Pillar 1 — Dual Multipliers Born Automatically:** Every central-path point $$x^*(t)$$ defines strictly positive dual variables $$u_i(t) = -\frac{1}{t h_i(x^*(t))} > 0$$ without solving a separate dual problem.
- **Pillar 2 — Relaxed Complementary Slackness:** Instead of the sharp KKT condition $$u_i^\star h_i(x^\star) = 0$$, the central path obeys the smooth hyperbolic condition $$u_i(t) h_i(x^*(t)) = -\frac{1}{t}$$.
- **Pillar 3 — Exact Primal-Dual Gap ($$m/t$$):** Evaluating the Lagrange dual function at $$(u(t), v(t))$$ gives $$g(u(t), v(t)) = f(x^*(t)) - \frac{m}{t}$$, proving $$f(x^*(t)) - f^\star \le \frac{m}{t}$$.
- **Pillar 4 — Foundation for Primal-Dual IPMs:** Viewing the barrier method as homotopy continuation on $$u_i h_i = -\mu$$ directly paves the road to Chapter 17's Primal-Dual Interior-Point Methods.

### Step-by-Step Worked Example (Read Slowly): Extracting Dual Variables and the Gap on a 1D Problem

Recall from Section 15-02 the 1D LP $$\min x$$ s.t. $$h_1(x) = -x \le 0$$, $$h_2(x) = x - 1 \le 0$$ ($$m = 2$$ constraints), where at $$t = 2$$ we found $$x^*(2) = 1 - \frac{\sqrt{2}}{2} \approx 0.2929$$.

1. **Compute the barrier-induced dual multipliers $$u_i(t) = -\frac{1}{t h_i(x^*(t))}$$:**
   - $$u_1(2) = -\frac{1}{2(-0.2929)} = \frac{1}{0.5858} \approx 1.7071 > 0$$.
   - $$u_2(2) = -\frac{1}{2(0.2929 - 1)} = \frac{1}{1.4142} \approx 0.7071 > 0$$.
2. **Verify KKT stationarity $$\nabla f(x) + u_1 \nabla h_1 + u_2 \nabla h_2 = 0$$:**
   $$1 + (1.7071)(-1) + (0.7071)(+1) = 1 - 1.7071 + 0.7071 = 0!$$
3. **Verify perturbed complementarity and the $$m/t$$ bound:**
   - $$u_1(2)h_1(x^*(2)) = -0.5 = -\frac{1}{t}$$ and $$u_2(2)h_2(x^*(2)) = -0.5 = -\frac{1}{t}$$.
   - Suboptimality gap: $$f(x^*(2)) - f^\star = 0.2929 - 0 = 0.2929 \le \frac{m}{t} = \frac{2}{2} = 1.0$$!

In this section, we will derive the KKT conditions for the barrier problem and the original problem to see what differences exist. We will also calculate the suboptimality gap for the solutions to both problems.