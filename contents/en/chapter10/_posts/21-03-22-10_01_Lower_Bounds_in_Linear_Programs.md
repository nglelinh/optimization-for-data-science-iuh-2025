---
layout: post
title: 10-01 Lower Bounds in Linear Programs
chapter: '10'
order: 2
owner: Wontak Ryu
categories:
- chapter10
lang: en
lesson_type: required
---

How do you prove a lower bound on the minimum value of a linear program without ever running the simplex method? The trick is as elementary as high-school algebra, yet it is the entire conceptual seed of duality theory: multiply each inequality constraint by a **nonnegative** weight (so the inequality sign never flips), add them up so the left-hand side matches the objective function $$c^\top x$$, and read off the resulting number on the right-hand side! Maximizing that right-hand side over all valid multiplier weights *is* the dual linear program.

## Key ideas: Building Lower Bounds from Linear Combinations

- **Pillar 1 — Sign Preservation Under Nonnegative Multipliers:** Multiplying $$a^\top x \ge b$$ by $$u \ge 0$$ preserves the direction $$u a^\top x \ge u b$$; multiplying an equality $$a^\top x = b$$ by *any* $$v \in \mathbb{R}$$ preserves equality. This sign discipline is why inequality dual variables are constrained ($$u \ge 0$$) while equality dual variables are free ($$v \in \mathbb{R}$$).
- **Pillar 2 — Matching Objective Coefficients (Dual Feasibility):** To conclude $$c^\top x \ge B$$ for all feasible $$x$$, the combined constraint coefficients on $$x$$ must match $$c$$ (or be $$\le c$$ when $$x \ge 0$$). Those coefficient-matching equations are literally the **dual constraints**.
- **Pillar 3 — Tightening the Lower Bound (Dual Objective):** Any valid choice of multipliers yields *some* lower bound $$B(u, v) \le p^\star$$. Searching for the *best* (largest) lower bound turns the bound-finding game into a maximization LP: $$\max_{u, v} B(u, v)$$.
- **Pillar 4 — Weak Duality as an Immediate Corollary:** Because every dual-feasible $$(u, v)$$ constructs a valid inequality $$c^\top x \ge B(u, v)$$ for every primal-feasible $$x$$, we obtain $$d^\star \le p^\star$$ automatically with zero extra proof machinery.

### Worked example: Deriving the Tightest Lower Bound by Hand

Minimize $$f(x, y) = 4x + 5y$$ subject to $$x + 2y \ge 6$$, $$3x + y \ge 8$$, and $$x, y \ge 0$$.

1. **Assign nonnegative multipliers $$u_1, u_2 \ge 0$$ to the two resource constraints:**
   $$u_1(x + 2y) + u_2(3x + y) \ge 6u_1 + 8u_2 \implies (u_1 + 3u_2)x + (2u_1 + u_2)y \ge 6u_1 + 8u_2.$$
2. **Enforce the bound $$4x + 5y \ge (u_1 + 3u_2)x + (2u_1 + u_2)y$$ for all $$x, y \ge 0$$:**
   Since $$x \ge 0$$ and $$y \ge 0$$, this holds whenever:
   $$u_1 + 3u_2 \le 4 \quad \text{and} \quad 2u_1 + u_2 \le 5, \qquad u_1, u_2 \ge 0.$$
3. **Maximize the lower bound $$6u_1 + 8u_2$$:**
   At the intersection of both dual constraints: $$u_1 + 3u_2 = 4$$ and $$2u_1 + u_2 = 5$$.
   - From the first: $$u_1 = 4 - 3u_2$$.
   - Substitute into the second: $$2(4 - 3u_2) + u_2 = 5 \implies 8 - 5u_2 = 5 \implies u_2^\star = 0.6$$, and $$u_1^\star = 4 - 1.8 = 2.2$$.
   - Best lower bound: $$6(2.2) + 8(0.6) = 13.2 + 4.8 = 18.0$$.
4. **Verify against the primal intersection:** Solving $$x + 2y = 6$$ and $$3x + y = 8$$ gives $$x^\star = 2, y^\star = 2$$, with primal value $$4(2) + 5(2) = 18.0$$—matching the dual bound to the last decimal!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

## Example 1: Form where the constraint contains the objective function

Suppose we want to find the lower bound value B of the optimal value for a given convex problem.

>$$
>\begin{align}
>B \leq \min_{x} f(x).
>\end{align}
>$$

Let's specifically consider the lower bound of linear programs. We will examine cases ranging from simple cases to generalized forms in order.
First, taking the simplest form of LP problem as an example

>$$
>\begin{align}
>&\min_{x, y}  
>& &{x+y} \\\\
>&\text{subject to} 
>& &{x + y \geq 2}\\\\
>& & &{x, y \geq 0.}\\\\
>\end{align}
>$$

The above problem already includes the lower bound of the objective function in the constraint, so we can easily see that $$B=2$$.

Furthermore, let's examine the case where the constraint does not include a lower bound.

## Example 2: Form where the objective function can be expressed as a linear combination of constraints (1)

>$$
>\begin{align}
>&\min_{x, y}  
>& & {x+3y} \\\\
>&\text{subject to} 
>& &{x + y \geq 2}\\\\
>& & &{x, y \geq 0.}\\\\
>\end{align}
>$$

If $$x,\, y$$ are feasible, then multiplying the three constraints by scalar values and adding or subtracting them still satisfies all three constraints. Therefore, for such an LP problem, the process of multiplying constraints by scalar values and adding or subtracting them, i.e., expressing the objective function as a linear combination of constraints, is possible, and as a result, we can find $$B$$. 

>$$
>\begin{align}
>& &{x + y \geq 2}\\\\
>&{+} &{0x \geq 0}\\\\
>&{+} &{2y \geq 0}\\\\
>&{=} &{x + 3y \geq 2}\\\\
>
>& &{\text{Lower bound}\ B = 2.}
>\end{align}
>$$

Generalizing further by applying arbitrary variables to represent the objective function, we get the following:

>$$
>\begin{align}
>&\min_{x, y}  
>& &{px+qy} \\\\
>&\text{subject to} 
>& &{x + y \geq 2}\\\\
>& & &{x, y \geq 0.}\\\\
>\end{align}
>$$

Similar to the second example, by multiplying the constraints by scalar values a, b, c respectively, the objective function can be expressed as a linear combination of these three.

 >$$
 >\begin{align}
 >& &{a(x+y) \geq 2a} \\\\
 >&{+} &{bx \geq 0} \\\\
 >&{+} &{cy \geq 0} \\\\
 >&{=} &{(a+b)x+(a+c)y \geq 2a} \\\\
 >&&\text{Lower bound}\ B=2a, \\
 >&&\text{for any satisfying a,b,c below}\\\\
 >& &{a + b = p}\\\\
 >& &{a + c = q}\\\\
 >& &{a,b,c \geq 0.}\\\\
 >\end{align}
 >$$


For the lower bound to satisfy being 2a as above, since the inequality sign would be reversed in the process of multiplying by scalar values and this would not hold, the conditions $$a, b, c$$ must be positive and the sum of scalar values must equal the objective function, i.e., the conditions $$a+b = p$$ and $$a+c = q$$ must be satisfied.

A new optimization problem can be defined by maximizing the lower bound result obtained as above. In this case, the conditions that satisfy the lower bound become the constraints in this problem. 

>$$
>\begin{align}
>&\max_{a, b, c}  
>& &{2a} \\\\
>&\text{subject to} 
>& &{a + b = p}\\\\
>& & &{a + c = q}\\\\
>& & &{a, b, c \geq 0}\\\\
>\end{align}
>$$

The original LP problem above is called the primal LP, and the form that redefines the optimization problem by maximizing the lower bound in the primal LP is called the dual LP. Note that the number of optimization variables in the dual problem equals the number of constraints in the primal problem.

>$$
>\begin{align}
>\text{Primal LP}\qquad
>&\qquad \min_{x, y}  &{px+qy} \\\\
>&\qquad \text{subject to} &{x + y \geq 2}\\\\
>&\qquad &{x, y \geq 0}\\\\
>\\\\
>\\\\
>\text{Dual LP}\qquad
>&\qquad \max_{a, b, c}  &{2a} \\\\
>&\qquad \text{subject to} &{a + b = p}\\\\
>&\qquad &{a + c = q}\\\\
>&\qquad &{a, b, c \geq 0}\\\\
>\end{align}
>$$

## Example 3: Form where the objective function can be expressed as a linear combination of constraints (2)

As a final example, let's examine a form where the inequality signs in the constraints are reversed and equality constraints are included.

>$$
>\begin{align}
>&\min_{x, y}  &{px+qy} \\\\
>&\text{subject to} &{x \geq 0}\\\\
>& &{y \leq 1}\\\\
>& &{3x + y = 2}\\\\
>\\\\
>& &{ax \geq 0}\\\\
>&{+} &{-by \geq -b}\\\\
>&{+} &{3cx + cy = 2c}\\\\
>&{=} &{(a+3c)x+(-b+c)y \geq 2c-b}
>\\\\
>\\\\
>&& \text{Lower bound}  \ B=2c-b, \\
>&& \text{for any satisfying a,b,c below}\\\\
>& &{a + 3c = p}\\\\
>& &{-b + c = q}\\\\
>& &{a,b \geq 0}\\\\
>\end{align}
>$$

Here, c is a scalar value multiplied to both sides of the equality, so any value can be multiplied without restriction.

Consequently, the dual LP can be defined as follows.

>$$
>\begin{align}
>&\qquad \max_{a, b, c}  &{2c-b} \\\\
>&\qquad \text{subject to} &{a + 3c = p}\\\\
>&\qquad &{-b + c = q}\\\\
>&\qquad &{a, b \geq 0}\\\\
>\end{align}
>$$
