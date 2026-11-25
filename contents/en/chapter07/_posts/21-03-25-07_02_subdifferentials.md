---
layout: post
title: 07-02 Sub-differentials
chapter: '07'
order: 3
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
lesson_type: required
---

At a kink, picking just one subgradient tells only part of the story—to test optimality or combine functions algebraically, we need the *entire collection* of valid slopes at once. That set, denoted $$\partial f(x)$$, is the **subdifferential**. Even when $$f$$ is nonsmooth (or even nonconvex!), $$\partial f(x)$$ obeys remarkably clean topological laws that make set-valued calculus possible.

## Key ideas: Structural Properties of the Subdifferential

1. **Always Closed and Convex**: By definition, $$\partial f(x) = \bigcap_{y \in \operatorname{dom}(f)} \{g \in \mathbb{R}^n : g^T(y - x) \le f(y) - f(x)\}$$. Because it is an intersection of closed halfspaces in $$g$$, $$\partial f(x)$$ is *always* a closed convex set—even if $$f$$ itself is nonconvex!
2. **Non-Empty and Bounded on the Interior**: For any finite convex function $$f: \mathbb{R}^n \to \mathbb{R}$$, $$\partial f(x)$$ is guaranteed to be non-empty and compact (closed and bounded) at every $$x \in \mathbb{R}^n$$. (At boundary points of a restricted domain, $$\partial f(x)$$ can be empty—for instance, $$f(x) = -\sqrt{x}$$ on $$x \ge 0$$ has $$\partial f(0) = \emptyset$$ because its slope is $$-\infty$$.)
3. **Singleton Characterization of Differentiability**: For a convex function $$f$$, $$f$$ is differentiable at $$x$$ if and only if $$\partial f(x)$$ contains exactly one element, in which case $$\partial f(x) = \{\nabla f(x)\}$$.
4. **Directional Derivatives via Support Function**: The directional derivative of $$f$$ at $$x$$ in direction $$v$$ equals the maximum inner product over the subdifferential: $$f'(x; v) = \max_{g \in \partial f(x)} g^T v$$.

### Worked example: Computing the Full Subdifferential of a Piecewise-Linear Function

Compute $$\partial f(x)$$ at every point $$x \in \mathbb{R}$$ for $$f(x) = \max\{-2x,\; x - 3,\; 3x - 9\}$$.

1. **Locate where the three linear branches intersect**:
   - $$-2x = x - 3 \implies 3x = 3 \implies x = 1$$ (value $$-2$$; third branch is $$3(1) - 9 = -6 < -2$$).
   - $$x - 3 = 3x - 9 \implies 2x = 6 \implies x = 3$$ (value $$0$$; first branch is $$-6 < 0$$).
   - Therefore:
     $$f(x) = \begin{cases} -2x & x < 1, \\ x - 3 & 1 \le x \le 3, \\ 3x - 9 & x > 3. \end{cases}$$
2. **Write $$\partial f(x)$$ on each smooth interval and each kink**:
   - $$x < 1$$: $$\partial f(x) = \{-2\}$$.
   - $$x = 1$$ (branches $$-2x$$ and $$x - 3$$ tie): $$\partial f(1) = \operatorname{conv}\{-2, 1\} = [-2, 1]$$.
   - $$1 < x < 3$$: $$\partial f(x) = \{1\}$$.
   - $$x = 3$$ (branches $$x - 3$$ and $$3x - 9$$ tie): $$\partial f(3) = \operatorname{conv}\{1, 3\} = [1, 3]$$.
   - $$x > 3$$: $$\partial f(x) = \{3\}$$.
3. **Spot the global minimizer immediately**: The only point where $$0 \in \partial f(x)$$ is $$x^\star = 1$$ (since $$0 \in [-2, 1]$$), giving $$f^\star = -2$$!

The subdifferential $$\partial f(x)$$ of a convex function $$f$$ at a point $$x$$ is the set of all subgradients at $$x$$:

>
\begin{equation}
\partial f(x) = \{g \in \mathbb{R}^n | \text{g is a subgradient of f at x} \}
\end{equation}

The subdifferential has the following properties:

- $$\partial f(x)$$ is always a closed convex set, whether $$f$$ is convex or not.
- If $$f$$ is convex, $$\partial f(x)$$ always contains at least one element; if $$f$$ is not convex, it may be empty.
- If $$f$$ is differentiable and convex at $$x$$, then $$\partial f(x) = \{\nabla f(x)\}$$.
- If $$\partial f(x) = \{g\}$$, then $$f$$ is differentiable at $$x$$ and $$\nabla f(x) = g$$.

