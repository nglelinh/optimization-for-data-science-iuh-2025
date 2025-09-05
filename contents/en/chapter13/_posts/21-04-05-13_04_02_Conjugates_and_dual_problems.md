---
layout: post
title: 13-04-02 Conjugates and dual problems
chapter: '13'
order: 7
owner: Wontak Ryu
categories:
- chapter13
lang: en
---
Conjugates can often be represented through the derivation of dual problems for Lagrangian minimization problems as follows:

> $$−f^{∗}(u) = \min_x f(x)−u^Tx$$

For example, consider the following expression:

> $$ \min_x  f(x) + g(x)$$

The following expression has constraints added to the above expression and is equivalent to it:

> $$ \min_{x,z} f(x) + g(z) \text{ subject to } x = z $$

Converting this to a Lagrange dual function gives:

> $$g(u) = \min_{x,z} f(x) + g(z) + u^T(z−x) = −f^{∗}(u)−g^{∗}(−u)$$

Therefore, the dual problem of the original expression can be defined as follows:
> $$ \max_u −f^{∗}(u)−g^{∗}(−u)$$

#### [Examples]
• Indicator function: The dual of $$ \min_x f(x) + I_C(x)$$ is as follows:
> $$ \max_u −f^{∗}(u)−I^{∗}_C(−u)$$
> 
> where $$I^{∗}_C$$ is the support function of $$C$$

• Norms: 

The dual of $$ \min_x f(x) + \rVert x \rVert $$ is as follows:
$$ \max_u −f^{∗}(u) \text{ subject to } \rVert u \rVert^{∗} ≤ 1 \text{ where } \rVert · \rVert_{∗} \text{ is the dual norm of } \rVert · \rVert$$
