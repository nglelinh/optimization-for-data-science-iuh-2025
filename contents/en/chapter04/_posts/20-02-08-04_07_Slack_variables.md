---
layout: post
title: 04-07 Slack variables
chapter: '04'
order: 8
owner: YoungJae Choung
categories:
- chapter04
lang: en
lesson_type: required
---

Imagine you have a budget cap of \$100 and you spend \$73. You can either write the inequality $$x \le 100$$, or you can name the unspent \$27 as a variable $$s = 27 \ge 0$$ and write the clean equation $$x + s = 100$$. That simple accounting move—introducing *slack variables*—is the backbone of the simplex method and interior-point solvers, turning awkward inequalities into structured equations plus simple nonnegativity boxes.

## Key ideas: Turning Inequalities into Structured Equalities

1. **Exact Reformulation of Inequalities**: Any inequality $$g_i(x) \le 0$$ is equivalent to introducing a scalar variable $$s_i \ge 0$$ and enforcing $$g_i(x) + s_i = 0$$. In linear programming, $$Gx \le h$$ becomes $$Gx + s = h,\; s \ge 0$$—keeping the equality constraint affine!
2. **The Convexity Trap for Nonlinear Inequalities**: Warning! If $$g_i(x)$$ is a *nonlinear* convex function (like $$x^2 - 1 \le 0$$), writing $$g_i(x) + s_i = 0$$ creates a *non-affine* equality constraint, which violates the standard convex-program rule. Therefore, slack variables preserve standard convexity **only for affine inequalities** (unless $$s_i$$ is kept in an inequality $$g_i(x) + s_i \le 0$$ or lifted into a cone constraint).
3. **Physical and Economic Meaning of Slack**: At an optimal solution $$(x^\star, s^\star)$$, the value $$s_i^\star = -g_i(x^\star)$$ measures unused resource or safety margin. When $$s_i^\star = 0$$, the constraint is *active* (a bottleneck); when $$s_i^\star > 0$$, the constraint is *inactive* (surplus capacity exists).
4. **Enabling Matrix Solvers and Duality**: Converting $$Gx \le h$$ to $$Gx + s = h, s \ge 0$$ lets simplex algorithms solve linear systems $$B x_B = h$$ at every pivot and lets interior-point methods place a clean logarithmic barrier $$-\sum_i \ln(s_i)$$ directly on the nonnegative slacks.

### Worked example: Converting a Production LP to Standard Slack Form

A small workshop produces $$x_1$$ chairs and $$x_2$$ tables to maximize profit $$3x_1 + 5x_2$$ (equivalently, minimize $$-3x_1 - 5x_2$$) subject to wood and labor limits:
$$2x_1 + x_2 \le 10, \qquad x_1 + 3x_2 \le 12, \qquad x_1, x_2 \ge 0.$$

1. **Introduce nonnegative slack variables $$s_1, s_2 \ge 0$$**:
   - $$s_1$$ represents unused wood hours: $$2x_1 + x_2 + s_1 = 10$$.
   - $$s_2$$ represents unused labor hours: $$x_1 + 3x_2 + s_2 = 12$$.
2. **Write the matrix standard form**: Let $$z = (x_1, x_2, s_1, s_2)^T \ge 0$$. Then the LP is
   $$\min_{z \ge 0} \quad [-3, -5, 0, 0]\,z \quad \text{subject to} \quad \begin{bmatrix} 2 & 1 & 1 & 0 \\ 1 & 3 & 0 & 1 \end{bmatrix} z = \begin{bmatrix} 10 \\ 12 \end{bmatrix}.$$
3. **Inspect candidate vertices via slack values**:
   - At $$(x_1, x_2) = (0, 0)$$: $$s_1 = 10, s_2 = 12$$ (all resources unused, profit $$= 0$$).
   - At $$(x_1, x_2) = (0, 4)$$: $$s_1 = 10 - 4 = 6$$ (6 wood hours left), $$s_2 = 12 - 12 = 0$$ (labor is binding), profit $$= 20$$.
   - At the intersection of both binding constraints ($$s_1 = 0, s_2 = 0$$): solving $$2x_1 + x_2 = 10$$ and $$x_1 + 3x_2 = 12$$ gives $$5x_2 = 14 \implies x_2^\star = 2.8$$ and $$x_1^\star = 3.6$$, with profit $$3(3.6) + 5(2.8) = 10.8 + 14.0 = 24.8$$.
4. **Verify slack interpretation**: Because $$s_1^\star = 0$$ and $$s_2^\star = 0$$, both wood and labor are completely exhausted at the optimal production plan $$(3.6, 2.8)$$.

# Slack Variables in Convex Optimization

## Introduction and Motivation

Slack variables are auxiliary variables introduced to transform inequality constraints into equality constraints. This transformation is fundamental in optimization theory and has practical applications in linear programming, interior-point methods, and many optimization algorithms.

**Why do we need slack variables?**
- Many optimization algorithms are designed to handle equality constraints more efficiently
- They provide a geometric interpretation of how "tight" a constraint is
- They are essential in the simplex method for linear programming
- They help in duality theory and sensitivity analysis

## Mathematical Formulation

Consider the standard convex optimization problem:

>$$
\begin{aligned}
&\min_x &&f(x) \\
&\text{subject to} &&g_{i}(x) \leq 0, \quad i = 1, \ldots, m\\
&&&Ax = b
\end{aligned}
>$$

By introducing **slack variables** $$s_i \geq 0$$ for each inequality constraint, we can reformulate this as:

>$$
\begin{aligned}
&\min_{x, s} &&f(x)\\
&\text{subject to} &&s_{i} \geq 0, \quad i = 1, \ldots, m\\
&&&g_{i}(x) + s_{i} = 0, \quad i = 1, \ldots, m\\
&&&Ax = b
\end{aligned}
$$

## Geometric Interpretation

The slack variable $$s_i$$ represents the "slack" or "margin" in the $$i$$-th constraint:

- **$$s_i > 0$$**: The constraint $$g_i(x) \leq 0$$ is **inactive** (not binding)
  - The point $$x$$ is in the interior of the feasible region defined by constraint $$i$$
  - We have $$g_i(x) = -s_i < 0$$

- **$$s_i = 0$$**: The constraint $$g_i(x) \leq 0$$ is **active** (binding)
  - The point $$x$$ lies exactly on the boundary defined by $$g_i(x) = 0$$
  - This constraint is "tight" at the optimal solution

## Practical Example: Resource Allocation

Consider a simple resource allocation problem:

**Original Problem:**
>$$
\begin{aligned}
&\max &&3x_1 + 2x_2 \\
&\text{subject to} &&x_1 + x_2 \leq 4 \quad \text{(labor hours)}\\
&&&2x_1 + x_2 \leq 6 \quad \text{(material units)}\\
&&&x_1, x_2 \geq 0
\end{aligned}
>$$

**With Slack Variables:**
>$$
\begin{aligned}
&\max &&3x_1 + 2x_2 \\
&\text{subject to} &&x_1 + x_2 + s_1 = 4\\
&&&2x_1 + x_2 + s_2 = 6\\
&&&x_1, x_2, s_1, s_2 \geq 0
\end{aligned}
>$$

**Interpretation:**
- $$s_1$$: unused labor hours
- $$s_2$$: unused material units
- If $$s_1 = 0$$ at optimum: all labor is utilized
- If $$s_2 > 0$$ at optimum: some material remains unused

## Important Properties and Considerations

### 1. Equivalence of Problems
The original and slack variable formulations are **mathematically equivalent**:
- Same optimal objective value
- Optimal $$x^*$$ is the same in both formulations
- The slack variables $$s_i^*$$ at optimum tell us which constraints are active

### 2. Convexity Preservation
**Critical Note:** The transformation preserves convexity **only when** $$g_i(x)$$ are **affine functions**.

- **If $$g_i(x) = a_i^T x - b_i$$ (affine)**: The reformulated problem remains convex
- **If $$g_i(x)$$ is nonlinear**: The equality constraint $$g_i(x) + s_i = 0$$ may destroy convexity

### 3. Dimensionality Impact
- Original problem: $$n$$ variables
- With slack variables: $$n + m$$ variables
- Trade-off: more variables but simpler constraint structure

## Example: Converting a Linear Program

**Original Form:**
>$$
\begin{aligned}
&\min &&c^T x \\
&\text{subject to} &&Ax \leq b\\
&&&x \geq 0
\end{aligned}
>$$

**Standard Form with Slack Variables:**
>$$
\begin{aligned}
&\min &&c^T x \\
&\text{subject to} &&Ax + s = b\\
&&&x, s \geq 0
\end{aligned}
>$$

Where $$s \in \mathbb{R}^m$$ is the vector of slack variables.

## Key Takeaways

1. **Transformation Tool**: Slack variables convert inequalities to equalities
2. **Geometric Meaning**: They measure constraint "tightness"
3. **Algorithm Enabler**: Essential for many optimization algorithms
4. **Convexity Condition**: Preserve convexity only for affine constraints
5. **Practical Insight**: Provide economic interpretation in resource problems

Understanding slack variables is crucial for:
- Implementing optimization algorithms
- Interpreting optimization results
- Analyzing constraint sensitivity
- Connecting theory with computational practice
