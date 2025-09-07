---
layout: post
title: 05-02-02 Geometric Programming
chapter: '05'
order: 9
owner: Copilot
categories:
- chapter05
lang: en
---

In this section, we will see a class of problems that appear non-convex when looking at the objective function and constraint functions, but can be transformed into convex form through several techniques.

First, we need some definitions:

## 5.2.1. Monomials and Posynomials

A function $$f: \mathbb{R}^n \to \mathbb{R}$$ with domain $$\text{dom } f = \mathbb{R}^n_{++}$$ (all elements are positive) has the form:

$$f(x) = c x_1^{a_1} x_2^{a_2} \ldots x_n^{a_n} \quad \quad (24)$$

where $$c > 0$$ and $$a_i \in \mathbb{R}$$, is called a **monomial function**.

A sum of monomials:

$$f(x) = \sum_{k=1}^K c_k x_1^{a_{1k}} x_2^{a_{2k}} \ldots x_n^{a_{nk}} \quad \quad (25)$$

where $$c_k > 0$$, is called a **posynomial function**, or simply a **posynomial**.

## 5.2.2. Geometric Programming

An optimization problem of the form:

$$\begin{align}
x &= \arg\min_x f_0(x) \\
\text{subject to: } &f_i(x) \leq 1, \quad i = 1, 2, \ldots, m \quad \quad (26) \\
&h_j(x) = 1, \quad j = 1, 2, \ldots, p
\end{align}$$

where $$f_0, f_1, \ldots, f_m$$ are posynomials and $$h_1, \ldots, h_p$$ are monomials, is called **Geometric Programming (GP)**. The condition $$x \succ 0$$ is implicit.

Note that if $$f$$ is a posynomial and $$h$$ is a monomial, then $$f/h$$ is a posynomial.

**Example:**

$$\begin{align}
(x, y, z) &= \arg\min_{x,y,z} x/y \\
\text{subject to: } &1 \leq x \leq 2 \\
&x^3 + 2y/z \leq \sqrt{y} \\
&x/y = z
\end{align}$$

This can be rewritten in GP form:

$$\begin{align}
(x, y, z) &= \arg\min_{x,y,z} xy^{-1} \\
\text{subject to: } &x^{-1} \leq 1 \\
&(1/2)x \leq 1 \\
&x^3 y^{-1/2} + 2y^{1/2}z^{-1} \leq 1 \\
&xy^{-1}z^{-1} = 1
\end{align}$$

This problem is clearly nonconvex since both the objective function and constraint functions are not convex.

## 5.2.3. Transforming GP to Convex Form

GP can be transformed to convex form as follows:

Let $$y_i = \log(x_i)$$, i.e., $$x_i = \exp(y_i)$$. If $$f$$ is a monomial function of $$x$$, then:

$$f(x) = c(\exp(y_1))^{a_1} \ldots (\exp(y_n))^{a_n} = \exp(a^T y + b)$$

where $$b = \log(c)$$. Now, the function $$g(y) = \exp(a^T y + b)$$ is a convex function in $$y$$. (The reader can prove by definition that the composition of two convex functions is a convex function. In this case, both the $$\exp$$ function and the affine function are convex functions.)

Similarly, the posynomial in equation (25) can be written as:

$$f(x) = \sum_{k=1}^K \exp(a_k^T y + b_k)$$

where $$a_k = [a_{1k}, \ldots, a_{nk}]^T$$ and $$b_k = \log(c_k)$$. Now, the posynomial has been written as a sum of $$\exp$$ functions of affine functions (and is therefore a convex function, recall that the sum of convex functions is convex).

The GP problem (26) is rewritten as:

$$\begin{align}
y &= \arg\min_y \sum_{k=1}^{K_0} \exp(a_{0k}^T y + b_{0k}) \\
\text{subject to: } &\sum_{k=1}^{K_i} \exp(a_{ik}^T y + b_{ik}) \leq 1, \quad i = 1, \ldots, m \quad \quad (27) \\
&\exp(g_j^T y + h_j) = 1, \quad j = 1, \ldots, p
\end{align}$$

where $$a_{ik} \in \mathbb{R}^n$$, $$i = 1, \ldots, p$$ and $$g_i \in \mathbb{R}^n$$.

With the observation that the function $$\log \sum_{i=1}^m \exp(g_i(x))$$ is a convex function if $$g_i$$ are convex functions (we omit the proof), we can rewrite problem (27) in convex form by taking the $$\log$$ of the functions as follows:

**GP in convex form:**

$$\begin{align}
\text{minimize}_y \quad &\tilde{f}_0(y) = \log\left(\sum_{k=1}^{K_0} \exp(a_{0k}^T y + b_{0k})\right) \\
\text{subject to: } &\tilde{f}_i(y) = \log\left(\sum_{k=1}^{K_i} \exp(a_{ik}^T y + b_{ik})\right) \leq 0, \quad i = 1, \ldots, m \quad \quad (28) \\
&\tilde{h}_j(y) = g_j^T y + h_j = 0, \quad j = 1, \ldots, p
\end{align}$$

Now we can say that GP is equivalent to a convex optimization problem because the objective function and inequality constraint functions in (28) are all convex functions, while the equality constraints are in affine form. This form is often called a **geometric program in convex form** (to distinguish it from the original definition of GP).