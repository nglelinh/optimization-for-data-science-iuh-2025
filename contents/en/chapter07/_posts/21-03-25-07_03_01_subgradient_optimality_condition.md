---
layout: post
title: 07-03-01 Subgradient Optimality Condition
chapter: '07'
order: 7
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
lesson_type: required
---

Some of the deepest theorems in mathematics have the shortest proofs. The **Subgradient Optimality Condition**—$$x^\star$$ minimizes $$f$$ globally if and only if $$0 \in \partial f(x^\star)$$—takes literally two lines to prove straight from the definition of a subgradient, yet it replaces separate optimality tests for smooth, nonsmooth, and constrained convex problems with one unified criterion.

## Background Knowledge Map: Why $$0 \in \partial f(x^\star)$$ Works Universally

1. **Direct Equivalence with the Definition**: Plugging $$g = 0$$ into the subgradient inequality $$f(y) \ge f(x^\star) + g^T(y - x^\star)$$ gives $$f(y) \ge f(x^\star) + 0 = f(x^\star)$$ for all $$y$$—which is *literally* the definition of $$x^\star$$ being a global minimizer!
2. **No Differentiability Needed**: Unlike Fermat's theorem $$f'(x^\star) = 0$$, which fails at kinks (like $$|x|$$ at $$0$$), $$0 \in \partial f(x^\star)$$ handles smooth valleys, sharp V-shaped bottoms, and flat plateaus identically.
3. **Geometric Meaning — Horizontal Supporting Hyperplane**: Saying $$0 \in \partial f(x^\star)$$ means you can slide a completely *flat, horizontal* plane $$z = f(x^\star)$$ underneath the graph of $$f$$ touching at $$x^\star$$—proving no point of the graph dips below $$f(x^\star)$$.
4. **Why Convexity Still Matters for Computation**: Although the two-line equivalence holds for any function, a nonconvex function has an *empty* global subdifferential at local (non-global) minima. Convexity guarantees $$\partial f(x)$$ is non-empty and computable via local calculus rules.

### Step-by-Step Worked Example (Read Slowly): Finding the Geometric Median in 1D via $$0 \in \partial f(x^\star)$$

Minimize the sum of absolute deviations $$f(x) = |x - 1| + |x - 4| + |x - 10|$$ over $$x \in \mathbb{R}$$.

1. **Write the subdifferential $$\partial f(x)$$ using the addition rule**:
   $$\partial f(x) = \partial |x - 1| + \partial |x - 4| + \partial |x - 10|.$$
2. **Check the candidate $$x = 4$$ (the median of $$\{1, 4, 10\}$$)**:
   - Since $$4 > 1$$: $$\partial |x - 1|\big|_{x=4} = \{+1\}$$.
   - Since $$4 = 4$$: $$\partial |x - 4|\big|_{x=4} = [-1, 1]$$.
   - Since $$4 < 10$$: $$\partial |x - 10|\big|_{x=4} = \{-1\}$$.
   - Minkowski sum: $$\partial f(4) = \{1\} + [-1, 1] + \{-1\} = [-1, 1]$$.
3. **Verify $$0 \in \partial f(4)$$**: Since $$0 \in [-1, 1]$$ (picking $$g_1 = 1, g_2 = 0, g_3 = -1$$ sums to $$0$$), $$x^\star = 4$$ is certified as the **exact global minimizer** with $$f(4) = 3 + 0 + 6 = 9$$! (Notice that for an even number of points, say $$\{1, 4, 6, 10\}$$, $$0 \in \partial f(x)$$ holds on the entire median interval $$[4, 6]$$.)

### Lemma

For any function $$f$$, the condition that $$x^*$$ is a minimizer of $$f$$ and that $$0$$ is a subgradient at $$x^*$$ are equivalent:

> $$
\begin{equation}
f(x^*) = \min_x f(x) \Longleftrightarrow 0 \in \partial f(x^*)
\end{equation}
$$

### Proof
>
$$
\begin{align}
&f(x^*) = \min_x f(x)\\
\Longleftrightarrow &f(y) \geq f(x^*) \text{ for all } y\\
\Longleftrightarrow &f(y) \geq f(x^*) + 0^T(y-x^*)\\
\Longleftrightarrow &0 \in \partial f(x^*)
\end{align}
$$

Note that convexity of $$f$$ is not used in this proof, so this optimality condition applies even to non-convex functions.

