---
layout: post
title: 15-05 Convergence analysis
chapter: "15"
order: 11
categories:
- chapter16
owner: "Minjoo Lee"
lang: en
---

How many outer centering loops does the barrier method need to slash the duality gap from $$10^4$$ down to $$10^{-8}$$? Because $$t^{(k)} = \mu^k t^{(0)}$$ grows geometrically, the suboptimality gap $$\frac{m}{\mu^k t^{(0)}}$$ decays *linearly* at rate $$1/\mu$$—meaning every single outer iteration adds a fixed number of accurate decimal digits, requiring only $$O(\log(m / (t^{(0)}\epsilon)))$$ outer steps!

## Background Knowledge Map: Outer-Loop Complexity of the Barrier Method

- **Pillar 1 — Exact Geometric Decay of the Gap:** After $$k$$ updates of $$t^{(k)} = \mu^k t^{(0)}$$, the guaranteed suboptimality satisfies $$f(x^{(k)}) - f^\star \le \frac{m}{\mu^k t^{(0)}}$$.
- **Pillar 2 — Closed-Form Outer Iteration Formula:** Solving $$\frac{m}{\mu^k t^{(0)}} \le \epsilon$$ for $$k$$ yields exactly $$k = \left\lceil \frac{\log(m/(t^{(0)}\epsilon))}{\log \mu} \right\rceil$$ (plus 1 for the initial centering at $$t^{(0)}$$).
- **Pillar 3 — Linear Outer Rate vs. Quadratic Inner Rate:** Although the outer loop converges linearly ($$O(\log(1/\epsilon))$$) rather than quadratically ($$O(\log\log(1/\epsilon))$$), each outer step slashes the error by a huge factor $$\mu \approx 10\text{–}20$$, so 6–10 outer steps suffice for machine precision.
- **Pillar 4 — Logarithmic Dependence on $$m$$:** Doubling the number of constraints $$m$$ adds at most $$\frac{\log 2}{\log \mu} < 1$$ extra outer iteration—explaining why barrier methods scale effortlessly to thousands of inequalities.

### Step-by-Step Worked Example (Read Slowly): Computing Exact Outer Iterations as $$m$$ Scales 100×

Fix $$t^{(0)} = 1$$, $$\mu = 10$$, and target accuracy $$\epsilon = 10^{-5}$$. Compare two problems: Problem A with $$m = 10$$ constraints and Problem B with $$m = 1{,}000$$ constraints.

1. **Problem A ($$m = 10$$):**
   - Ratio: $$\frac{m}{t^{(0)}\epsilon} = \frac{10}{1 \cdot 10^{-5}} = 10^6$$.
   - Outer centering steps (including initial $$t^{(0)}$$): $$\frac{\log_{10}(10^6)}{\log_{10}(10)} + 1 = 6 + 1 = 7$$ centering steps.
2. **Problem B ($$m = 1{,}000$$ — 100× more constraints!):**
   - Ratio: $$\frac{m}{t^{(0)}\epsilon} = \frac{1000}{10^{-5}} = 10^8$$.
   - Outer centering steps: $$\frac{\log_{10}(10^8)}{\log_{10}(10)} + 1 = 8 + 1 = 9$$ centering steps!
3. **Insight:** Increasing the number of constraints by **100×** added only **2** extra outer iterations!

Assuming the centering step in the barrier method is solved exactly, we can obtain the following convergence results.

## Convergence Theorem
After $$k$$ centering steps, the **barrier method** satisfies the following equation. (Here, $$k$$ is the number of outer iterations.)
>$$\begin{align}
f(x^{(k)}) - f^{*} \le  \frac{m}{\mu^k t^{(0)}}
\end{align}$$

That is, to reach the desired accuracy level $$\epsilon$$ with the barrier method, you need the following number of centering steps plus one for the first centering step.

>$$\begin{align}
\frac{log(m/(t^{(0)}\epsilon))}{\log \mu} + 1
\end{align}$$

Therefore, we see that the convergence is linear, with $$O(\log 1/\epsilon )$$.

Newton's method has quadratic convergence with $$O(\log \log 1/\epsilon ) $$, but in this case, the problem is very difficult, so linear convergence is not such a bad result.

For the definitions of linear and quadratic convergence, refer to the Wiki.<br>
* Reference: [Rate of convergence](https://en.wikipedia.org/wiki/Rate_of_convergence)