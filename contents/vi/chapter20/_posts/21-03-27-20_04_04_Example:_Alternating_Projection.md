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
