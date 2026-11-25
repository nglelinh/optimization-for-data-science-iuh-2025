---
layout: post
title: 03-04 Quasiconvex functions
chapter: '03'
order: 8
owner: Minjoo Lee
categories:
- chapter03
lang: en
---

Many important economic utility ratios, signal-to-noise objectives, and linear-fractional costs are *not* convex—their graphs can curve downward like $$\sqrt{|x|}$$ or flatten out like $$\log x$$—yet they still have a single valley with convex sublevel sets. **Quasiconvex functions** capture this exact generalization, allowing us to solve nonconvex ratio problems to global optimality via simple bisection over convex feasibility problems.

## Background Knowledge Map: Why Quasiconvexity Matters

- **Sublevel-Set Definition:** $$f$$ is quasiconvex iff every sublevel set $$S_\alpha = \{x : f(x) \le \alpha\}$$ is convex—a strictly weaker condition than convexity of the epigraph.
- **Unimodality Without Bowl Shape:** In 1D, quasiconvexity means $$f$$ is monotone or decreases then increases—no multiple valleys, though flat plateaus (spurious stationary points) can occur.
- **Modified Jensen & Calculus Tests:** The chord bound weakens from a weighted average to a maximum ($$f(\theta x + (1-\theta)y) \le \max\{f(x), f(y)\}$$), and the first-order condition constrains gradient direction only along sublevel boundaries.
- **Algorithmic Payoff (Bisection):** Even when $$f$$ is nonconvex, solving $$f(x) \le t$$ is a convex feasibility problem, letting bisection pinpoint the global minimum $$p^*$$ to $$\varepsilon$$ accuracy in $$\lceil \log_2((u-l)/\varepsilon)\rceil$$ steps.

### Step-by-Step Worked Example (Read Slowly): Why $$f(x) = \sqrt{|x|}$$ Is Quasiconvex but Not Convex

Examine $$f(x) = \sqrt{|x|}$$ on $$\mathbb{R}$$.

1. **Check convexity of all sublevel sets $$S_\alpha = \{x \in \mathbb{R} : \sqrt{|x|} \le \alpha\}$$:**
   - For $$\alpha < 0$$: $$S_\alpha = \emptyset$$ (convex).
   - For $$\alpha \ge 0$$: $$\sqrt{|x|} \le \alpha \iff |x| \le \alpha^2 \iff x \in [-\alpha^2, \alpha^2]$$, a closed interval (hence **convex**!).
   Therefore $$f(x) = \sqrt{|x|}$$ is **quasiconvex**.
2. **Disprove ordinary convexity with two points:** Take $$x = 0$$, $$y = 4$$, and $$\theta = 0.5$$:
   $$f(0.5(0) + 0.5(4)) = f(2) = \sqrt{2} \approx 1.414 > 0.5\sqrt{0} + 0.5\sqrt{4} = 1.$$
   Because the midpoint lies *above* the chord, $$f$$ is **not convex**.

This section introduces quasiconvex functions, their definitions, examples, and basic properties.
