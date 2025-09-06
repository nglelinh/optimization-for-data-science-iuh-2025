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
