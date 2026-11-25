---
layout: post
title: 20-04-03 ADMM in Scaled Form
chapter: '20'
order: 11
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

Writing out both the linear term $$u^T(Ax + Bz - c)$$ and the quadratic term $$\frac{\rho}{2}\|Ax + Bz - c\|_2^2$$ in every ADMM derivation is clutter waiting to cause a sign error. Simply defining the **scaled dual variable** $$w = u / \rho$$ and completing the square folds both terms into a single clean squared norm $$\frac{\rho}{2}\|Ax + Bz - c + w\|_2^2$$! Not only is scaled ADMM far easier to memorize and code, it also reveals what $$w^{(k)}$$ really is: the **running cumulative sum of all past primal residuals**.

## Background Knowledge Map: Completing the Square in Scaled ADMM

- **Scaled Dual Variable ($$w = u / \rho$$):** Absorbing the linear Lagrangian term into the quadratic penalty via $$u^T r + \frac{\rho}{2}\|r\|_2^2 = \frac{\rho}{2}\|r + w\|_2^2 - \frac{\rho}{2}\|w\|_2^2$$ eliminates the cross-term completely (since $$-\frac{\rho}{2}\|w\|_2^2$$ does not depend on $$x$$ or $$z$$).
- **Running Sum of Residuals:** The dual update simplifies to $$w^{(k)} = w^{(k-1)} + (Ax^{(k)} + Bz^{(k)} - c) = w^{(0)} + \sum_{j=1}^k r^{(j)}$$—literally an integral controller (the "I" term in PID control!) accumulating past constraint violations until they cancel out.
- **Direct Bridge to Proximal Operators:** When $$A = I, B = -I, c = 0$$, the scaled $$x$$- and $$z$$-updates become pure proximal operators: $$x^{(k)} = \operatorname{prox}_{f/\rho}(z^{(k-1)} - w^{(k-1)})$$ and $$z^{(k)} = \operatorname{prox}_{g/\rho}(x^{(k)} + w^{(k-1)})$$.
- **Exact Algebraic Equivalence:** Scaled and unscaled ADMM produce the *exact* same primal iterates $$(x^{(k)}, z^{(k)})$$ at every step; scaled form is strictly preferred in practice for cleaner implementation and numerical readability.

### Step-by-Step Worked Example (Read Slowly): Solving a Constrained Box-Quadratic via Scaled ADMM

Minimize $$\frac{1}{2}(x - 3)^2$$ subject to $$x \in [0, 1]$$ by splitting $$\min_{x,z} \frac{1}{2}(x - 3)^2 + I_{[0,1]}(z)$$ s.t. $$x - z = 0$$ (exact optimum $$x^\star = z^\star = 1$$). Use scaled ADMM with $$\rho = 2$$ starting from $$z^0 = 0, \; w^0 = 0$$.

1. **Write the three scaled ADMM updates:**
   - $$x^{(k)} = \arg\min_x \frac{1}{2}(x - 3)^2 + \frac{2}{2}(x - z^{(k-1)} + w^{(k-1)})^2 = \frac{3 + 2(z^{(k-1)} - w^{(k-1)})}{3}$$.
   - $$z^{(k)} = \Pi_{[0, 1]}\!\big(x^{(k)} + w^{(k-1)}\big)$$.
   - $$w^{(k)} = w^{(k-1)} + x^{(k)} - z^{(k)}$$.
2. **Iteration 1 ($$z^0 = 0, w^0 = 0$$):**
   - $$x^1 = \frac{3 + 0}{3} = 1.0$$.
   - $$z^1 = \Pi_{[0,1]}(1.0 + 0) = 1.0$$.
   - $$w^1 = 0 + (1.0 - 1.0) = 0$$.
   Wait—check dual optimality! At $$x^1 = 1$$, $$\nabla f(1) = -2$$, so we need $$w^\star = u^\star/\rho = 2/2 = 1$$. Let's check Iteration 2: $$x^2 = \frac{3 + 2(1 - 0)}{3} = \frac{5}{3} \approx 1.667$$!
   - $$z^2 = \Pi_{[0,1]}(5/3 + 0) = 1.0$$.
   - $$w^2 = 0 + (5/3 - 1) = 2/3 \approx 0.667$$.
3. **Iteration 3 ($$z^2 = 1, w^2 = 2/3$$):**
   - $$x^3 = \frac{3 + 2(1 - 2/3)}{3} = \frac{11}{9} \approx 1.222$$.
   - $$z^3 = \Pi_{[0,1]}(11/9 + 2/3) = 1.0$$.
   - $$w^3 = 2/3 + (11/9 - 1) = 8/9 \approx 0.889$$ (approaching $$w^\star = 1$$!).
   Notice how $$w^{(k)}$$ accumulates the exact force needed to hold $$x^{(k)}$$ against the wall $$x = 1$$!

# ADMM in Scaled Form

ADMM can be expressed in scaled form by substituting the dual variable $$u$$ with $$w = u/\rho$$. The ADMM steps can then be written as follows: 
> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg\min_x f(x) + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c + w^{(k-1)} \rVert_2^2  \\
> z^{(k)} & = \arg\min_z g(x) + \frac{\rho}{2} \lVert Ax^{(k)} + Bz - c + w^{(k-1)} \rVert_2^2  \\
> w^{(k)} & = w^{(k-1)} + Ax^{(k)} + Bz^{(k)} - c 
> \end{alignat}
> $$

## Equivalence to Original Form

We can show that the above equations are equivalent to the original form through the following process:

> $$
> \begin{align}
> x^{(k)} & = \arg\min_x f(x) + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c + w^{(k-1)} \rVert_2^2  \\
> & = \arg\min_x f(x)  + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c \rVert_2^2  + \rho w^{(k-1)T} (Ax + Bz^{(k-1)} - c)  + \frac{\rho}{2}\lVert w^{(k-1)} \rVert_2^2 \\
> & = \arg\min_x f(x)  + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c \rVert_2^2  + u^{(k-1)T} (Ax + Bz^{(k-1)} - c) \\
> \end{align}
> $$

where we used $$u^{(k-1)} = \rho w^{(k-1)}$$ and dropped the constant term.

## Interpretation of Scaled Variable

Here, $$w^{(k)}$$ can be viewed as the sum of residuals up to iteration $$k$$:

> $$
> \begin{equation}
> w^{(k)} = w^{(0)} + \sum_{i=1}^k (Ax^{(i)} + Bz^{(i)} - c) 
> \end{equation}
> $$

This scaled form is often more convenient for implementation and analysis.