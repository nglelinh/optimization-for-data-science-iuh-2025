---
layout: post
title: 04-05 Transformations and change of variables
chapter: '04'
order: 6
owner: YoungJae Choung
categories:
- chapter04
lang: en
---
This section discusses transformations and change of variables in convex optimization problems, which are useful for simplifying or reformulating problems.

The objective function or constraint functions can be modified while preserving the given optimization problem, and sometimes this can be used to discover the "hidden convexity" of the problem.

### Theorem 1
When function $$h : \mathbb{R} \rightarrow \mathbb{R}$$ is a monotone increasing transformation, the following relationship holds:

>$$
>\begin{align}
>   &\text{min}_{x} f(x) \text{ subject to } x \in C \\
>   \Longleftrightarrow \quad &\text{min}_{x} h(f(x)) \text{ subject to } x \in C
>\end{align}
>$$

### Theorem 2
If function $$\phi: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$$ is a one-to-one correspondence function and the image of $$\phi$$ covers the feasible set $$C$$, then the variables of the optimization problem can be changed as follows:   

>$$
>\begin{align}
>    &\min_{x} f(x) \text{ subject to } x \in C \\\\ 
>    \Longleftrightarrow \quad &\min_{y} f(\phi(y)) \text{ subject to } \phi(y) \in C
>\end{align}
>$$

### Example: geometric programming

A function $$f: \mathbb{R}_{++}^n \rightarrow \mathbb{R}$$ of the following form is called a **monomial**:
> $$f(x) = \gamma x_{1}^{a_{1}} x_{2}^{a_{2}} \dotsb x_{n}^{a_{n}} \text{ for } \gamma > 0, a_{1}, \dotsc, a_{n} \in \mathbb{R}.$$


Also, the sum of monomials is called a **posynomial**:
> $$g(x) = \sum_{k=1}^{p} \gamma_{k} x_{1}^{a_{k1}} x_{2}^{a_{k2}} \dotsb x_{n}^{a_{kn}} \text{ for } \gamma > 0, a\_1, \dotsc, a_{n} \in \mathbb{R}.$$


A **geometric program** is defined in the following form and is a non-convex problem:
>$$
\begin{align}
&\min_{x} &&f(x) \\
&\text{subject to } &&g_{i}(x) \leq 1, i = 1, \dotsc, m\\
&&&h_{j}(x) = 1, j = 1, \dotsc, r,\\\\
\end{align}\\
$$

>where $$f$$, $$g_{i}, i=1, \dotsc, m$$ are posynomials and $$h_{j}, j=1, \dotsc, r$$ are monomials.

Let's prove that a geometric program is equivalent to some convex problem.

### Proof:
>For $$f(x) = \gamma x_{1}^{a_{1}} x_{2}^{a_{2}} \dotsb x_{n}^{a_{n}}$$, if we let $$y_{i} = \log x_{i}$$ and $$b = \log \gamma$$, then $$f$$ can be transformed as follows, and by **Theorem 2**, this preserves the given optimization problem equivalently:
>$$\gamma (e^{y_{1}})^{a_{1}} (e^{y_{2}})^{a_{2}} \dotsb (e^{y_{n}})^{a_{n}} = e^{a^Ty + b}$$
>
>Also, a posynomial can be represented as $$\sum_{k=1}^{p} e^{a_{k}^{Ty} + b_{k}}$$.
>
>At this point, by **Theorem 1**, the logarithmic form $$\log \big( \sum_{k=1}^{p} e^{a_{k}^{Ty} + b_{k}} \big)$$ can also preserve the optimization problem equivalently.
>
>That is, the geometric program is equivalent to the following problem, which is a convex problem:
>
>$$
>\begin{align}
&\min_{x} \quad &&{log \big( \sum_{k=1}^{p_{0}} e^{a_{0k}^{Ty} + b_{0k}} \big)} \\
&\text{subject to} &&{
         log \big( \sum_{k=1}^{p_{i}} e^{a_{ik}^{Ty} + b_{ik}} \big)
         \leq 0
         , \quad i = 1, \dotsc, m
}\\
&&&c_{j}^{Ty} + d_{j} = 0, \quad j = 1, \dotsc, r\\\\
\end{align}
$$
