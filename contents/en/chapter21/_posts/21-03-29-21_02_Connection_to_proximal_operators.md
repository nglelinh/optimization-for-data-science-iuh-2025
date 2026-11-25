---
layout: post
title: 21-02 Connection to proximal operators
chapter: '21'
order: 3
owner: Hooncheol Shin
categories:
- chapter21
lang: en
---

At first glance, ADMM looks like a constrained-optimization algorithm built around equality constraints $$Ax + Bz = c$$. Yet set $$A = I, B = -I, c = 0$$ on the unconstrained composite problem $$\min_x f(x) + g(x)$$, and something remarkable happens: **ADMM becomes a pure proximal-operator machine**—alternating $$\operatorname{prox}_{f/\rho}$$ and $$\operatorname{prox}_{g/\rho}$$! Unlike proximal gradient descent (which demands that one term be differentiable), ADMM can minimize the sum of *two completely nondifferentiable* functions as long as each has a fast proximal map!

## Background Knowledge Map: ADMM as Symmetrical Proximal Splitting

- **Canonical Consensus Split ($$x = z$$):** Rewriting $$\min_x f(x) + g(x)$$ as $$\min_{x,z} f(x) + g(z) \text{ s.t. } x - z = 0$$ gives scaled ADMM updates $$x^k = \operatorname{prox}_{f/\rho}(z^{k-1} - w^{k-1})$$ and $$z^k = \operatorname{prox}_{g/\rho}(x^k + w^{k-1})$$.
- **No Smoothness Required on Either Block:** Proximal gradient (ISTA/FISTA) requires $$\nabla f$$ to exist and be $$L$$-Lipschitz; proximal ADMM handles nonsmooth $$f$$ and nonsmooth $$g$$ symmetrically (for instance, $$\ell_1$$ loss $$+$$ $$\ell_1$$ penalty, or two set indicators $$I_C + I_D$$).
- **Exact Equivalence to Douglas–Rachford Splitting:** Defining the reflected variable $$v^k = z^k + w^k$$ shows that proximal ADMM is algebraically identical to **Douglas–Rachford operator splitting** applied to the monotone inclusion $$0 \in \partial f(x) + \partial g(x)$$.
- **Moreau Decomposition Shortcut:** When $$\operatorname{prox}_{g/\rho}$$ is hard to compute directly but $$\operatorname{prox}_{\rho g^\ast}$$ is easy (e.g., projecting onto an $$\ell_\infty$$ dual ball), Moreau's identity $$v = \operatorname{prox}_{g/\rho}(v) + \frac{1}{\rho}\operatorname{prox}_{\rho g^\ast}(\rho v)$$ computes the ADMM update in one line!

### Step-by-Step Worked Example (Read Slowly): Minimizing the Sum of Two Nonsmooth Functions via Proximal ADMM

Minimize $$f(x) + g(x) = \underbrace{|x - 2|}_{f(x)} + \underbrace{|x|}_{g(x)}$$ (neither function is differentiable at its kink! Optimal set is the entire interval $$x^\star \in [0, 2]$$ with value $$2$$). Run proximal ADMM with $$\rho = 1$$ starting from $$z^0 = 3, \; w^0 = 0$$.

1. **Write both proximal operators (for $$\rho = 1$$):**
   - $$\operatorname{prox}_{f}(v) = \arg\min_x |x - 2| + \frac{1}{2}(x - v)^2 = 2 + S_1(v - 2)$$.
   - $$\operatorname{prox}_{g}(v) = \arg\min_z |z| + \frac{1}{2}(z - v)^2 = S_1(v)$$.
2. **Iteration 1 ($$z^0 = 3, w^0 = 0$$):**
   - $$x^1 = \operatorname{prox}_f(3 - 0) = 2 + S_1(1) = 2 + 0 = 2.0$$.
   - $$z^1 = \operatorname{prox}_g(2.0 + 0) = S_1(2.0) = 1.0$$.
   - $$w^1 = 0 + (2.0 - 1.0) = 1.0$$.
3. **Iteration 2 ($$z^1 = 1.0, w^1 = 1.0$$):**
   - $$x^2 = \operatorname{prox}_f(1.0 - 1.0) = 2 + S_1(-2) = 2 + (-1) = 1.0$$.
   - $$z^2 = \operatorname{prox}_g(1.0 + 1.0) = S_1(2.0) = 1.0$$.
   - $$w^2 = 1.0 + (1.0 - 1.0) = 1.0$$.
4. **Exact convergence in 2 steps!**
   At $$k = 2$$, $$x^2 = z^2 = 1.0 \in [0, 2]$$ with primal residual $$r^2 = 0$$ and dual residual $$s^2 = 1.0 - 1.0 = 0$$—solving a *completely nondifferentiable* composite problem cleanly without subgradient step-size tuning!

# Connection to Proximal Operators

Consider an optimization problem with a single variable that separates into two functions:
>$$
>\begin{align}
>\min_{x} f(x)+g(x)
>\end{align}
>$$

This can also be expressed by adding a constraint:
>$$
>\begin{align}
>\min_{x, z} f(x)+g(z) \qquad \text{subject to  }x=z
>\end{align}
>$$

## ADMM Steps in Proximal Form

The ADMM steps for this problem are:
>$$
>\begin{align}
>&x^{(k)} = {\operatorname{prox}}_{f,\frac{1}{\rho}}(z^{(k-1)}-w^{(k-1)})\\\\
>&z^{(k)} = {\operatorname{prox}}_{g,\frac{1}{\rho}}(x^{(k)}+w^{(k-1)})\\\\
>&w^{(k)}=w^{(k-1)}+x^{(k)}-z^{(k)}
>\end{align}
>$$

where $${\operatorname{prox}}_{f,\frac{1}{\rho}}$$ and $${\operatorname{prox}}_{g,\frac{1}{\rho}}$$ are the proximal operators of $$f$$ and $$g$$ respectively, with parameter $$\frac{1}{\rho}$$.

## Proximal Operator Definition

Recall that for a convex function $$f$$, the [proximal operator]({% multilang_post_url contents/chapter19/21-03-24-19_01_01_Reminder:_proximal_gradient_descent %}) is defined as:
>$$
>\begin{align}
>{\operatorname{prox}}_{f, \lambda}(v) = \underset{x}{\operatorname{argmin}}\left(f(x)+\frac{1}{2\lambda}||x-v||_{2}^{2}\right). 
>\end{align}
>$$

## Derivation of Proximal Updates

The process of deriving ADMM updates in terms of proximal operators is as follows.

Let $$x^{+}, z^{+}, w^{+}$$ be the updated values of $$x, z, w$$ after one step.

### Update for x:
>$$
>\begin{align}
>x^{+}& = \underset{x}{\operatorname{argmin}}f(x)+\frac{\rho}{2}||x-z+w||^{2}_{2}\\\\
>& =\underset{x}{\operatorname{argmin}}\frac{1}{2\cdot\frac{1}{\rho}}||(z-w)-x||^{2}_{2}+f(x)\\\\
>& ={\operatorname{prox}}_{f,\frac{1}{\rho}}(z-w)
>\end{align}
>$$

### Update for z:
>$$
>\begin{align}
>z^{+}& = \underset{z}{\operatorname{argmin}}g(z)+\frac{\rho}{2}||x^{+}-z+w||^{2}_{2}\\\\
>& =\underset{z}{\operatorname{argmin}}\frac{1}{2\cdot\frac{1}{\rho}}||(x^{+}+w)-z||^{2}_{2}+g(z)\\\\
>& ={\operatorname{prox}}_{g,\frac{1}{\rho}}(x^{+}+w)
>\end{align}
>$$

## Key Insight

The original ADMM constraint is $$Ax+Bz = c$$, while here the constraint is $$x=z$$. That is, when the linear transformation relationship between $$x$$ and $$z$$ is the identity, we can transform the original ADMM updates into proximal updates.