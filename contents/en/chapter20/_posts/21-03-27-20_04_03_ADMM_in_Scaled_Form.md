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