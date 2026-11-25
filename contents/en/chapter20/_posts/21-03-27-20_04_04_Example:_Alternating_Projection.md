---
layout: post
title: 20-04-04 Example - Alternating Projection
chapter: '20'
order: 12
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

Finding a point in the intersection $$C \cap D$$ of two closed convex sets is one of the oldest problems in applied mathematics—from CT image reconstruction to phase retrieval and feasibility of linear matrix inequalities. Classical **von Neumann alternating projections** simply bounce back and forth ($$x \to \Pi_C(x) \to \Pi_D(x)$$), which can zig-zag painfully slowly when $$C$$ and $$D$$ meet at a shallow angle. Applying scaled ADMM to $$\min I_C(x) + I_D(z) \text{ s.t. } x = z$$ turns out to rediscover **Dykstra's / Douglas–Rachford splitting**, using the dual memory $$w$$ to push past shallow angles!

## Key ideas: ADMM on Set Indicators vs. Naive Alternating Projection

- **Feasibility as Composite Minimization:** Encoding $$x \in C \cap D$$ as $$\min_{x,z} I_C(x) + I_D(z)$$ subject to $$x = z$$ turns set intersection into a standard ADMM problem whose proximal operators are Euclidean projections $$\Pi_C$$ and $$\Pi_D$$!
- **The Dual Offset Makes the Difference:** Plain alternating projection updates $$x^k = \Pi_C(z^{k-1}), \; z^k = \Pi_D(x^k)$$. Scaled ADMM updates $$x^k = \Pi_C(z^{k-1} - w^{k-1}), \; z^k = \Pi_D(x^k + w^{k-1}), \; w^k = w^{k-1} + x^k - z^k$$—where $$w$$ remembers the normal direction of the boundary!
- **Equivalence to Douglas–Rachford Splitting:** Eliminating $$w$$ shows that ADMM on $$I_C + I_D$$ is algebraically identical to Douglas–Rachford reflection-projection splitting, which converges even when $$C$$ and $$D$$ are tangent!
- **Scaling Invariance ($$\rho$$ Cancels Out):** Because $$I_C$$ and $$I_D$$ only take values $$0$$ and $$+\infty$$, dividing by $$\rho > 0$$ does not change the indicator function at all—making ADMM alternating projection completely **parameter-free**!

### Worked example: Intersecting a Line and a Box via ADMM Projection

Find a point in $$C \cap D \subset \mathbb{R}^2$$ where $$C = \{(x_1, x_2) : x_2 = 1\}$$ (horizontal line) and $$D = \{(x_1, x_2) : x_1 = x_2\}$$ (the $$45^\circ$$ diagonal). Clearly $$C \cap D = \{(1, 1)\}$$. Start from $$z^0 = (0, 0)^T, \; w^0 = (0, 0)^T$$.

1. **Recall the two projections:**
   $$\Pi_C(a, b) = (a, 1), \qquad \Pi_D(a, b) = \left(\frac{a+b}{2}, \frac{a+b}{2}\right).$$
2. **Iteration 1 ($$z^0 = (0,0), w^0 = (0,0)$$):**
   - $$x^1 = \Pi_C(z^0 - w^0) = \Pi_C(0, 0) = (0, 1)$$.
   - $$z^1 = \Pi_D(x^1 + w^0) = \Pi_D(0, 1) = (0.5, 0.5)$$.
   - $$w^1 = w^0 + x^1 - z^1 = (0, 0) + (-0.5, +0.5) = (-0.5, 0.5)$$.
3. **Iteration 2 (watch how $$w^1$$ accelerates past naive alternating projection!):**
   - $$x^2 = \Pi_C(z^1 - w^1) = \Pi_C(0.5 - (-0.5), \; 0.5 - 0.5) = \Pi_C(1.0, \; 0.0) = (1.0, \; 1.0)!$$
   - $$z^2 = \Pi_D(x^2 + w^1) = \Pi_D(0.5, \; 1.5) = (1.0, \; 1.0)!$$
   - $$w^2 = (-0.5, 0.5) + (0, 0) = (-0.5, 0.5)$$.
4. **Compare with naive alternating projection:**
   ADMM hit the **exact** intersection $$(1, 1)$$ in **2 iterations**! By contrast, naive alternating projection gives $$(0, 1) \to (0.5, 0.5) \to (0.5, 1) \to (0.75, 0.75) \to \dots$$—needing infinitely many steps to reach $$(1, 1)$$!

# Example: Alternating Projection

Consider the problem of finding a point in the intersection of convex sets $$C, D \in \mathbb{R}^n$$:
>\begin{equation}
\min_x I_C(x) + I_D(x)    
\end{equation}

where $$I_C(x)$$ and $$I_D(x)$$ are indicator functions for sets $$C$$ and $$D$$ respectively.

To reformulate this problem in ADMM form, we express it as follows: 
> $$
> \begin{equation}
> \min_{x,z} I_C(x) + I_D(x) \quad \text{subject to} \quad x - z = 0   
> \end{equation}
> $$

## ADMM Algorithm for Alternating Projection

Each ADMM cycle involves two projections:
> $$
> \begin{alignat}{1}
> x^{(k)} & = P_C \left( z^{(k-1)} - w^{(k-1)} \right) \\
> z^{(k)} & = P_D \left( x^{(k)} + w^{(k-1)} \right) \\
> w^{(k)} & = w^{(k-1)} + x^{(k)} - z^{(k)}
> \end{alignat}
> $$

where $$P_C$$ and $$P_D$$ denote the projection operators onto sets $$C$$ and $$D$$ respectively.

## Derivation

The update for $$x^{(k)}$$ is derived as follows:

> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg\min_x I_C(x) + \frac{\rho}{2} \lVert x - z^{(k-1)} + w^{(k-1)} \rVert_2^2 \\
> & = P_C \left( z^{(k-1)} - w^{(k-1)} \right)
> \end{alignat}
> $$

Similarly, the update for $$z^{(k)}$$ is derived as:

> $$
> \begin{alignat}{1}
> z^{(k)} & = \arg\min_z I_D(z) + \frac{\rho}{2} \lVert x^{(k)} - z + w^{(k-1)} \rVert_2^2 \\
> & = P_D \left( x^{(k)} + w^{(k-1)} \right)
> \end{alignat}
> $$

## Comparison with Classical Method

This method is similar to the classical alternating projection method but is often more efficient and robust in practice.  
