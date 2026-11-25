---
layout: post
title: 24-03 Solving integer programs
chapter: '24'
order: 4
owner: YoungJae Choung
categories:
- chapter24
lang: en
---

If an integer program with 100 binary variables has $$2^{100} \approx 1.26 \times 10^{30}$$ candidate solutions, how can a commercial solver find the certified global optimum in under a second? It never enumerates the haystack. Instead, every modern MIP solver runs a disciplined **primal–dual squeeze**: primal heuristics hunt for better feasible integer solutions to push the upper bound $$U$$ down, while relaxations and cuts push the certified lower bound $$L$$ up. The moment $$U - L \le \varepsilon$$, global optimality is mathematically guaranteed—even though $$99.999999\%$$ of the search space was never visited.

## Background Knowledge Map: Complexity and the Primal–Dual Bounding Template

- **NP-Hardness in Worst Case vs. Tractability in Practice:** Integer linear programming is NP-complete (Karp 1972), meaning no known polynomial-time algorithm works for all instances. Yet structured real-world instances yield rapidly to strong relaxations and aggressive pruning.
- **Primal Bounds (Upper Bounds for Minimization):** Any feasible integer point $$\hat{x} \in \mathcal{F}$$ immediately certifies $$f^\star \le f(\hat{x}) = U$$. Solvers generate primal bounds via rounding, feasibility pumps, local search, and integer relaxation solutions.
- **Dual Bounds (Lower Bounds for Minimization):** Solving any relaxation over a superset $$\tilde{\mathcal{F}} \supseteq \mathcal{F}$$ (or minimizing a lower-bounding objective $$\tilde{f} \le f$$) certifies $$L = \tilde{f}^\star \le f^\star$$.
- **Optimality Gap & Certified Termination:** The relative MIP gap $$\frac{U - L}{|U|}$$ measures exact worst-case suboptimality. Stopping at a $$0.1\%$$ gap delivers a solution provably within $$0.1\%$$ of global optimality without spending hours proving the last decimal place.

### Step-by-Step Worked Example (Read Slowly): Tracking Primal/Dual Bounds and the MIP Gap

Suppose we minimize a discrete cost $$f(x)$$ over integer feasible set $$\mathcal{F}$$, and our solver executes three rounds of relaxation refinement and primal heuristics:

1. **Initialization:**
   - LP relaxation solves to $$x_{\text{LP}}$$ with objective $$L_0 = 80$$.
   - Rounding $$x_{\text{LP}}$$ yields a feasible integer solution $$x^{(0)} \in \mathcal{F}$$ with cost $$U_0 = 100$$.
   - Current absolute gap: $$U_0 - L_0 = 20$$; relative gap: $$\frac{100 - 80}{100} = 20.0\%$$.
2. **Round 1 (Add a valid inequality + run local search):**
   - Tightened relaxation raises the lower bound to $$L_1 = 88$$.
   - Local search improves the incumbent integer solution to $$U_1 = 92$$.
   - Absolute gap drops from $$20$$ to $$4$$; relative gap drops to $$\frac{92 - 88}{92} \approx 4.35\%$$.
3. **Round 2 (Branching certifies all subproblems $$\ge 92$$):**
   - Every remaining leaf relaxation has lower bound $$\ge 92$$, so the global dual bound becomes $$L_2 = 92$$.
   - Since $$L_2 = U_1 = 92$$, the gap is $$0\%$$: the incumbent with cost $$92$$ is **provably globally optimal**, without ever evaluating the remaining exponentially many integer vectors!

After transforming the mathematical formulation of Integer programming, techniques such as relaxation are needed to solve the problem. Let's examine the constraints that appear in integer programs and what approaches are taken to address the problem.

## Hardness of integer programs
Solving Integer program problems is much more difficult than solving convex optimization problems. General Integer programming is [NP-hard](https://en.wikipedia.org/wiki/NP-hardness), requiring at least polynomial time without even knowing the possibility of solvability. In this case, by removing constraints on integer constraints and performing convex relaxation, we can obtain a lower bound that approaches the optimal value.<br><br>
When solving problems using convex relaxation, the following limitations may occur:


 * Finding a feasible integer solution can become difficult.
 * The optimal solution obtained under relaxation conditions may be distant from the optimal solution obtained with integer programming.
 * The value after approximation (rounding) may differ from the optimal value.


## Algorithmic template for solving integer programs
When $$X$$ is convex and includes integrality constraints, the integer program is as follows:

> $$ z : = \min_{x \in X} f(x) $$

Unlike convex optimization, there are no direct "optimality conditions" that prove a feasible point $$x* \in X$$ is optimal. Instead, we can use a method that finds approximations of the optimal by finding lower bound $$ \underline{z} \leq z$$ and upper bound $$ \bar{z} \geq z$$ while approaching $$\underline{z} = \bar{z}$$.

### Algorithmic template
Observing the decreasing sequence of upper bounds,
> $$\bar{z_1} \geq \bar{z_2} \geq \dotsc \bar{z_s} \geq z$$

Observing the increasing sequence of lower bounds,
> $$\underline{z_1} \leq \underline{z_2} \leq \dotsc \underline{z_t} \leq z $$

For any $$\epsilon > 0$$, the value of $$z$$ is determined within the range where $$\bar{z_s} - \underline{z_t} \leq \epsilon$$.

### Primal bounds
According to the previous $$z$$ formula, for any feasible $$x \in X$$, $$f(x) \geq z$$ always holds, and in this case, $$f(x)$$ is an upper bound. However, since we cannot always find a feasible $$x$$, if the $$x$$ value is included in the corresponding set, the problem can be solved easily, but this may not always be the case.


### Dual bounds
Usually also called lower bounds, their values are found through relaxation. Detailed explanations are added in the next section.
