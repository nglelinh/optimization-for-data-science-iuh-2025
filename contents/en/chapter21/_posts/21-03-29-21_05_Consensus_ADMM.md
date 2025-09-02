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
