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