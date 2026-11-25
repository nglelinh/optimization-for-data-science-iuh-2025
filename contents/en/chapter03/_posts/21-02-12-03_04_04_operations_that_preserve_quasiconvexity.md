---
layout: post
title: 03-04-04 Operations that preserve quasiconvexity
chapter: '03'
order: 12
owner: Minjoo Lee
categories:
- chapter03
lang: en
---

Because adding two quasiconvex functions can easily create a double-humped non-quasiconvex landscape, you need a different set of construction rules than for ordinary convexity. Most importantly, representing a quasiconvex function through a 1-parameter family of *convex* functions $$\phi_t(x) \le 0$$ turns quasiconvex optimization directly into a sequence of standard convex feasibility checks via bisection.

## Background Knowledge Map: Preserving and Solving Quasiconvexity

- **Nonnegative Weighted Maximum:** $$\max_i w_i f_i(x)$$ ($$w_i \ge 0$$) and arbitrary pointwise suprema preserve quasiconvexity—sublevel sets simply intersect!
- **Composition Rules:** Composing a quasiconvex function with an affine map or a *nondecreasing* scalar function $$h$$ preserves quasiconvexity (no convexity required of $$h$$!).
- **Partial Minimization:** $$g(x) = \inf_{y \in C} f(x, y)$$ is quasiconvex whenever $$f(x, y)$$ is jointly quasiconvex and $$C$$ is a convex set.
- **Convex Representation ($$f(x) \le t \iff \phi_t(x) \le 0$$):** Replacing a quasiconvex objective with a family of convex inequalities $$\phi_t(x) \le 0$$ (nonincreasing in $$t$$) is the exact bridge that lets convex solvers minimize quasiconvex objectives via bisection.

### Step-by-Step Worked Example (Read Slowly): Bisection via a Convex Family $$\phi_t(x)$$

Minimize the quasiconvex linear-fractional objective $$f(x) = \frac{x + 3}{x + 1}$$ over the convex interval $$x \in [0, 4]$$.

1. **Construct the convex representing family $$\phi_t(x)$$:** For $$x \ge 0$$ (so $$x + 1 > 0$$),
   $$f(x) \le t \iff x + 3 \le t(x + 1) \iff \phi_t(x) = (1 - t)x + (3 - t) \le 0.$$
   For each fixed $$t$$, $$\phi_t(x)$$ is affine (hence convex) in $$x$$.
2. **Bracket the optimum with convex feasibility checks:**
   - Test $$t = 2$$: $$\phi_2(x) = -x + 1 \le 0 \iff x \ge 1$$. Since $$[1, 4] \neq \emptyset$$, $$t = 2$$ is **feasible** ($$p^* \le 2$$).
   - Test $$t = 1.2$$: $$\phi_{1.2}(x) = -0.2x + 1.8 \le 0 \iff x \ge 9$$. Since $$[9, \infty) \cap [0, 4] = \emptyset$$, $$t = 1.2$$ is **infeasible** ($$p^* > 1.2$$).
3. **Identify the exact threshold:** Feasibility holds on $$[0, 4]$$ iff $$\frac{3 - t}{t - 1} \le 4 \iff 3 - t \le 4t - 4 \iff 5t \ge 7 \iff t \ge 1.4$$, giving $$p^* = 1.4$$ attained at $$x^* = 4$$.

This section discusses operations that preserve the quasiconvexity of functions.

## Nonnegative weighted maximum

When $$f$$ is a quasiconvex function, the nonnegative weighted maximum $$f$$ is quasiconvex.
>$$f = \max\{w_1f_1, ... ,w_mf_m\}$$ with $$w_i \geq 0$$ is quasiconvex

This concept can be extended as follows:
>$$f(x) = \sup_{y \in C}(w(y)g(x,y))$$ with $$w(y) \geq 0$$, 
>where $$g(x,y)$$ is quasiconvex in $$x$$ for each $$y$$.

<br>

## Composition

If $$g : \mathbb{R}^n \mapsto \mathbb{R}$$ is quasiconvex and $$h : \mathbb{R} \mapsto \mathbb{R}$$ is nondecreasing, then the composition $$f$$ satisfies quasiconvexity.
> $$f = h \circ g$$ is quasiconvex if $$h$$ is nondecreasing and $$g$$ is quasiconvex.
 
Composing a quasiconvex function with affine or linear-fractional transformations results in a quasiconvex function.
If $$f$$ is quasiconvex, then $$g(x) = f(Ax + b)$$ is also quasiconvex, and $$\tilde{g}(x) = f((Ax + b)/(c^Tx + d))$$ is also quasiconvex on the set $$\{x \mid c^Tx + d > 0, (Ax + b)/(c^Tx + d) \in \text{dom}f\}$$.

<br>

## Minimization

If $$f(x, y)$$ satisfies quasiconvexity and $$C$$ is a convex set, then the following condition holds:
> $$g(x) = \inf_{y \in C} f(x,y)$$ is quasiconvex if $$f$$ is quasiconvex in $$(x,y)$$ and $$C$$ is a convex set.

<br>

## Representation via family of convex functions

The sublevel sets of a quasiconvex function $$f$$ can be represented by inequalities of convex functions. A family of convex functions is $$\phi_t : \mathbb{R}^n \mapsto \mathbb{R}$$ for $$t \in \mathbb{R}$$, defined as follows:
>$$f(x) \leq t \Longleftrightarrow \phi_t(x) \leq 0$$

That is, the $$t$$-sublevel set of quasiconvex function $$f(x)$$ becomes the 0-sublevel set of convex function $$\phi_t$$. Here, $$t$$ represents the index of convex function $$\phi$$. For all $$x \in \mathbb{R}^n$$, the following is satisfied:
>$$\phi_t(x) \leq 0 \Rightarrow \phi_s(x) \leq 0 \text{ for } s \geq t$$

