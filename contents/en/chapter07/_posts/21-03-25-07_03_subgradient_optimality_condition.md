---
layout: post
title: 07-03 Subgradient Optimality Condition
chapter: '07'
order: 6
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
---

In smooth unconstrained calculus, the crown jewel is Fermat's rule: $$f'(x^\star) = 0$$. In convex optimization—even with sharp corners, norms, and hard constraints—that entire theory collapses into a single, astonishingly clean statement: $$x^\star$$ is a global minimizer **if and only if** $$0 \in \partial f(x^\star)$$. Section 07-03 unpacks this universal optimality law and applies it to constrained optimization, Lasso regression, soft-thresholding, and set-distance functions.

## Background Knowledge Map: Roadmap of Subgradient Optimality

1. **Universal Necessary & Sufficient Condition**: $$f(x^\star) = \min_x f(x) \iff 0 \in \partial f(x^\star)$$. Remarkably, this equivalence holds for *any* function $$f$$ (even nonconvex!), though for nonconvex functions $$\partial f(x^\star)$$ may be empty at local minima—whereas for convex functions it characterizes every global minimizer.
2. **Recovering Constrained First-Order Optimality**: Writing $$\min_{x \in C} f(x)$$ as $$\min_x (f(x) + I_C(x))$$ gives $$0 \in \partial f(x^\star) + N_C(x^\star)$$. When $$f$$ is smooth, $$-\nabla f(x^\star) \in N_C(x^\star) \iff \nabla f(x^\star)^T(y - x^\star) \ge 0\;\forall y \in C$$.
3. **Deriving Closed-Form Proximal & Sparsity Operators**: Applying $$0 \in \partial\bigl(\frac{1}{2}\|y - \beta\|_2^2 + \lambda\|\beta\|_1\bigr)$$ immediately yields the **soft-thresholding** operator, explaining mathematically why Lasso zeroes out weak features.
4. **Geometric Applications**: Computing $$\partial\,\mathrm{dist}(x, C)$$ connects subgradients directly to Euclidean projections $$P_C(x)$$, underpinning projection and splitting algorithms in later chapters.

### Step-by-Step Worked Example (Read Slowly): Solving a Constrained Nonsmooth Problem via $$0 \in \partial f + N_C$$

Minimize $$f(x) = |x - 3|$$ subject to $$x \in C = [-1, 2]$$.

1. **Convert to unconstrained form using $$I_C(x)$$**: Minimize $$F(x) = |x - 3| + I_{[-1, 2]}(x)$$, so optimality requires $$0 \in \partial |x^\star - 3| + N_{[-1, 2]}(x^\star)$$.
2. **Test the interior $$x \in (-1, 2)$$**:
   - Here $$x < 3$$, so $$\partial |x - 3| = \{-1\}$$, and since $$x$$ is interior to $$C$$, $$N_C(x) = \{0\}$$.
   - Sum: $$\{-1\} + \{0\} = \{-1\} \not\ni 0$$ (no interior optimum).
3. **Test the right boundary $$x^\star = 2$$**:
   - Here $$2 < 3$$, so $$\partial |x - 3|\big|_{x=2} = \{-1\}$$.
   - The normal cone at the right endpoint of $$[-1, 2]$$ is $$N_{[-1, 2]}(2) = [0, +\infty)$$.
   - Sum: $$\{-1\} + [0, +\infty) = [-1, +\infty) \ni 0$$! (Explicitly, $$-1 + (+1) = 0$$ with $$+1 \in N_C(2)$$.)
4. **Conclusion**: $$x^\star = 2$$ is certified as the global minimizer, with $$f^\star = |2 - 3| = 1$$.

In this section, we examine optimality conditions using subgradients, and provide several examples to illustrate their application and usefulness.