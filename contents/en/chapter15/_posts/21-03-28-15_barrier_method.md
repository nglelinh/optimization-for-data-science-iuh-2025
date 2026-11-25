---
layout: post
title: 15 Barrier Method
chapter: "15"
order: 1
categories:
- chapter16
owner: "Minjoo Lee"
lang: en
---

Newton's method conquers smooth unconstrained and equality-constrained problems in a handful of steps—but the moment you add a single inequality constraint $$h_i(x) \le 0$$, the optimum usually sits on a sharp corner of the feasible set where derivatives break down and you don't know which constraints are active. The **Barrier Method** sidesteps the combinatorial boundary nightmare completely: it erects an invisible, infinitely smooth repulsive force field along every wall $$h_i(x) = 0$$ and glides straight through the *interior* to the optimal corner.

## Key ideas: The Architecture of Interior-Point Barrier Methods

- **Pillar 1 — Smooth Interiorization via Log Barriers:** Replacing the hard indicator $$I_C(x)$$ with $$\frac{1}{t}\phi(x) = -\frac{1}{t}\sum_{i=1}^m \log(-h_i(x))$$ converts inequality constraints into a smooth equality-constrained problem solvable by Newton's method.
- **Pillar 2 — The Central Path & Perturbed KKT:** As $$t$$ grows from small to large, the barrier minimizers $$x^*(t)$$ trace a smooth curve called the **central path**, automatically producing strictly feasible dual multipliers $$u_i(t) = -1/(t h_i(x^*(t)))$$ satisfying $$u_i(t)h_i(x^*(t)) = -1/t$$.
- **Pillar 3 — Exact $$m/t$$ Suboptimality Certificate:** Every central-path point $$x^*(t)$$ is guaranteed to satisfy $$f(x^*(t)) - f^\star \le m/t$$, giving an exact stopping rule that depends only on the number of inequalities $$m$$ and $$t$$.
- **Pillar 4 — Path-Following & Phase-I Feasibility:** Increasing $$t \leftarrow \mu t$$ with warm-started Newton centering steps achieves polynomial-time convergence—once a Phase-I feasibility problem hands us a strictly feasible starting point.

### Worked example: Watching the Barrier Push a Solution to the Boundary

Minimize $$f(x) = x$$ subject to $$x \ge 0$$ (so $$m = 1$$, $$h_1(x) = -x \le 0$$, true optimum $$x^\star = 0$$, $$f^\star = 0$$).

1. **Form the barrier objective for parameter $$t > 0$$:**
   $$\min_{x > 0} \; t x - \log(x).$$
2. **Solve the optimality condition exactly:**
   $$\frac{d}{dx}(tx - \log x) = t - \frac{1}{x} = 0 \implies x^*(t) = \frac{1}{t}.$$
3. **Trace the central path as $$t$$ increases ($$\mu = 10$$):**
   - $$t = 1 \implies x^*(1) = 1.0$$, gap $$f(x^*(1)) - f^\star = 1.0 = \frac{1}{1}$$.
   - $$t = 10 \implies x^*(10) = 0.1$$, gap $$= 0.1 = \frac{1}{10}$$.
   - $$t = 1000 \implies x^*(1000) = 0.001$$, gap $$= 0.001 = \frac{1}{1000}$$.
4. **Notice the exact $$m/t$$ bound:** Here $$m = 1$$ and $$f(x^*(t)) - f^\star = \frac{1}{t} = \frac{m}{t}$$ with exact equality!

In this chapter, we will look at one of the 2nd-order methods, the **Barrier Method**.

The **Barrier Method** is a technique for solving **inequality constraint and equality constrained smooth problems**, which are considered the most difficult among 2nd-order method problems.

(For reference, using the gradient to solve an optimization problem is called a 1st-order method, and using the Hessian is called a 2nd-order method.)

## References and further readings
* S. Boyd and L. Vandenberghe (2004), "Convex optimization", Chapter 11
* A. Nemirovski (2004), "Interior-point polynomial time methods in convex programming", Chapter 4
* J. Nocedal and S. Wright (2006), "Numerical optimization", Chapters 14 and 19