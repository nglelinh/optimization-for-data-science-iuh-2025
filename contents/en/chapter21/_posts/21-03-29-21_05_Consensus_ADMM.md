---
layout: post
title: 21-05 Consensus ADMM
chapter: '21'
order: 6
owner: Hooncheol Shin
categories:
- chapter21
lang: en
---

Suppose your training dataset is 500 gigabytes—far too big to fit on a single server, so you shard it across $$B = 100$$ machines, each holding its own local empirical loss $$f_i(x)$$. How do you minimize $$\sum_{i=1}^B f_i(x)$$ without shipping raw data over the network? **Consensus ADMM** gives every machine its own local parameter copy $$x_i$$, enforces the agreement constraint $$x_i = z$$ with a central consensus vector $$z$$, and turns the global $$z$$-update into a single **exact average** $$\bar{x}^{(k)}$$—producing a clean, fault-tolerant map-reduce optimization loop!

## Background Knowledge Map: Distributed Map-Reduce via Consensus ADMM

- **Variable Replication ($$x_i = z$$):** Rewriting $$\min_x \sum_{i=1}^B f_i(x)$$ as $$\min \sum_{i=1}^B f_i(x_i) \text{ s.t. } x_i = z$$ decouples all $$B$$ local losses completely during the $$x$$-update, allowing all $$B$$ workers to compute $$\operatorname{prox}_{f_i/\rho}(z^{k-1} - w_i^{k-1})$$ in parallel.
- **Exact Averaging in the $$z$$-Update:** Minimizing $$\sum_{i=1}^B \frac{\rho}{2}\|x_i^k - z + w_i^{k-1}\|_2^2$$ over $$z$$ yields $$z^k = \bar{x}^k + \bar{w}^{k-1}$$. Because $$\bar{w}^k = \bar{w}^{k-1} + \bar{x}^k - z^k = 0$$ for all $$k \ge 1$$, the consensus update simplifies to the pure average $$z^k = \bar{x}^k$$!
- **Regularized Consensus (Adding $$g(z)$$):** Adding a global regularizer $$g(z)$$ (like $$\lambda\|z\|_1$$ for distributed Lasso) keeps all worker updates identical and changes only the coordinator step to $$z^k = \operatorname{prox}_{g/(B\rho)}(\bar{x}^k + \bar{w}^{k-1})$$.
- **Zero-Mean Dual Invariant ($$\sum_i w_i^k = 0$$):** The dual variables act as local disagreement memories whose sum vanishes across the cluster, pulling stubborn workers smoothly toward the shared global optimum without sharing private data.

### Step-by-Step Worked Example (Read Slowly): Two-Machine Consensus ADMM with Zero-Mean Duals

Minimize $$f_1(x) + f_2(x) = \frac{1}{2}(x - 1)^2 + \frac{1}{2}(x - 5)^2$$ across $$B = 2$$ machines (exact global optimum $$x^\star = 3$$). Split as $$x_1 = z, \; x_2 = z$$ with $$\rho = 1$$, starting from $$z^0 = 0, \; w_1^0 = 0, \; w_2^0 = 0$$.

1. **Iteration 1 (Parallel worker updates + coordinator average):**
   - Machine 1: $$x_1^1 = \arg\min_{x_1} \frac{1}{2}(x_1 - 1)^2 + \frac{1}{2}(x_1 - 0)^2 = \frac{1 + 0}{2} = 0.5$$.
   - Machine 2: $$x_2^1 = \arg\min_{x_2} \frac{1}{2}(x_2 - 5)^2 + \frac{1}{2}(x_2 - 0)^2 = \frac{5 + 0}{2} = 2.5$$.
   - Coordinator average: $$z^1 = \frac{x_1^1 + x_2^1}{2} = \frac{0.5 + 2.5}{2} = 1.5$$.
   - Local dual updates: $$w_1^1 = 0 + (0.5 - 1.5) = -1.0$$, $$w_2^1 = 0 + (2.5 - 1.5) = +1.0$$. (Notice $$w_1^1 + w_2^1 = 0$$!)
2. **Iteration 2 (Watch consensus hit the exact optimum!):**
   - Machine 1: $$x_1^2 = \frac{1 + (z^1 - w_1^1)}{2} = \frac{1 + (1.5 - (-1.0))}{2} = \frac{3.5}{2} = 1.75$$.
   - Machine 2: $$x_2^2 = \frac{5 + (z^1 - w_2^1)}{2} = \frac{5 + (1.5 - 1.0)}{2} = \frac{5.5}{2} = 2.75$$.
   - Coordinator average: $$z^2 = \frac{1.75 + 2.75}{2} = 2.25$$ (moving straight toward $$3.0$$!).
   - Dual updates: $$w_1^2 = -1.0 + (1.75 - 2.25) = -1.5$$, $$w_2^2 = +1.0 + (2.75 - 2.25) = +1.5$$ (again $$w_1^2 + w_2^2 = 0$$, converging to $$w_1^\star = -2, w_2^\star = +2$$!).

# Consensus ADMM

## Basic Consensus ADMM

Consider the following problem:
>$$
>\begin{align}
>\min_{x}\sum^{B}_{i=1} f_{i}(x)
>\end{align}
>$$

To solve this problem with ADMM, we need to introduce constraints. Here, we want to transform the equation into a form that is easy to operate in parallel. This approach, called consensus ADMM, reparametrizes the equation as follows:
>$$
>\begin{align}
>&\min_{x_{1},...,x_{B},x} &&\sum^{B}_{i=1} f_{i}(x_{i})\\\\
>&\text{subject to } &&x_{i}=x, i = 1,...B
>\end{align}
>$$

## ADMM Algorithm

This allows us to compute decomposable ADMM steps:

>$$
>\begin{align}
>x^{(k)}_{i} &= \underset{x_{i}}{\operatorname{argmin}} f_{i}(x_{i})+\frac{\rho}{2}||x_{i}-x^{(k-1)}+w_{i}^{(k-1)}||_{2}^{2}, i=1,...B\\\\
>x^{(k)} &=\frac{1}{B}\sum_{i=1}^{B}(x_{i}^{(k)}+w_{i}^{(k-1)})\\\\
>w_{i}^{(k)} &=w_{i}^{(k-1)}+x_{i}^{(k)}-x^{(k)}, i=1,...,B
>\end{align}
>$$

## Simplified Form

Additionally, we can define $$\overline{x}=\frac{1}{B}\sum_{i=1}^{B}x_{i}, \overline{w}=\frac{1}{B}\sum_{i=1}^{B}w_{i}$$. With this, we can easily verify that $$\overline{w}^{(k)}=0$$ for iterations $$k>1$$, and the second equation of the ADMM update simplifies to $$x^{(k)}=\overline{x}^{(k)}$$. Therefore, we can simplify the ADMM update equations as follows:

>$$
>\begin{align}
>x^{(k)}_{i} &= \underset{x_{i}}{\operatorname{argmin}} f_{i}(x_{i})+\frac{\rho}{2}||x_{i}-\overline{x}^{(k-1)}+w_{i}^{(k-1)}||_{2}^{2},  i=1,...B\\\\
>w_{i}^{(k)} &=w_{i}^{(k-1)}+x_{i}^{(k)}-\overline{x}^{(k)},  i=1,...,B.
>\end{align}
>$$

## Intuition

The $$x_{i}$$ updates for $$i = 1,...,B$$ can be computed in parallel.

From the simplified equations, we can gain intuition about consensus ADMM. Each $$x_{i}$$ update tries to minimize $$f_{i}(x_{i})$$ while simultaneously using $$l_{2}$$ regularization to align each $$x_{i}$$ with the average $$\overline{x}$$. If $$x_{i}$$ becomes larger than the average, $$w_{i}$$ increases. Therefore, the regularization in the next step will reduce the enlarged $$x_{i}$$.

## General consensus ADMM
## General Consensus ADMM

Consensus ADMM can be generalized to a more general form. Let's look at the form of problems with affine transformations of $$x$$ and arbitrary function $$g$$:

>$$
>\begin{align}
>\min_{x}\sum_{i=1}^{B} f_{i}(a^{T}_{i}x+b_{i})+g(x)
>\end{align}
>$$

For this equation as well, we reparameterize by adding constraints:
>$$
>\begin{align}
>&\min_{x_{1},..x_{B},x} &&\sum^{B}_{i=1}f_{i}(a_{i}^{T}x+b)+g(x)\\\\
>&\text{subject to } &&x_{i} = x, i=1,...B
>\end{align}
>$$ 

We can then derive decomposable ADMM updates:
>$$
>\begin{align}
>x_{i}^{(k)} &= \underset{x_{i}}{\operatorname{argmin}}f_{i}(a_{i}^{T}x+b_{i})+\frac{\rho}{2}||x_{i}-x^{(k-1)}+w_{i}^{(k-1)}||^{2}_{2}+g(x)\\\\
>x^{(k)}&=\underset{x}{\operatorname{argmin}} \frac{B\rho}{2}||x-\overline{x}^{(k)}-\overline{w}^{(k-1)}||^{2}_{2}+g(x)\\\\
>w_{i}^{(k)}&=w_{i}^{(k-1)}+x_{i}^{(k)}-x^{(k)}, i=1,...B
>\end{align}
>$$ 

## Key Differences

The differences between generalized consensus ADMM and the consensus ADMM derived above can be summarized as follows:

* Because the ADMM step equations do not simplify, $$\overline{w}^{(k)}=0$$ is no longer satisfied.
* $$x_{i}, i=1,...,B$$ can be updated in parallel.
* Each $$x_{i}$$ update can be thought of as minimizing the corresponding partial loss with $$l_2$$ regularization.
* The $$x$$ update is a proximal operation for the arbitrary function $$g$$ (generally a regularizer).
* Different ADMM algorithms are derived depending on how the reparameterization is done. 

For more detailed information, see the [reference papers]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %}).
