---
layout: post
title: 24-03 Solving integer programs
chapter: '24'
order: 4
owner: YoungJae Choung
categories:
- chapter24
lang: vi
---

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
