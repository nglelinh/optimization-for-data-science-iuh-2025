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

Many optimization problems in physics, finance, and engineering look hopelessly nonconvex at first glance—products of powers, ratios of norms, or awkward exponential constraints. Yet a surprisingly large fraction of them are *convex problems in disguise*. Just as switching from Cartesian to polar coordinates turns a messy circle equation into $$r = 1$$, monotone transformations and invertible changes of variables unmask hidden convexity without altering the true optimal solution.

## Background Knowledge Map: Discovering Hidden Convexity

1. **Monotone Increasing Objective Transformations**: If $$h: \mathbb{R} \to \mathbb{R}$$ is strictly increasing on the range of $$f$$, then minimizing $$h(f(x))$$ has the exact same set of optimal points $$X_{\mathrm{opt}}$$ as minimizing $$f(x)$$. Taking $$\ln(\cdot)$$ of a likelihood function or squaring a nonnegative norm $$\|Ax - b\|_2$$ are everyday applications that simplify derivatives or remove square roots.
2. **One-to-One Change of Variables**: If $$\phi: \mathbb{R}^n \to \mathbb{R}^n$$ is a bijection whose image covers the feasible domain, substituting $$x = \phi(z)$$ produces an equivalent problem in $$z$$, and optimal points map back via $$x^\star = \phi(z^\star)$$. Choosing $$\phi$$ cleverly (such as $$x_i = e^{z_i}$$ for positive variables) can turn multiplicative constraints into additive convex ones.
3. **Log-Sum-Exp and Geometric Programming**: A posynomial $$\sum_{k=1}^K c_k x_1^{a_{1k}} \cdots x_n^{a_{nk}}$$ (with $$c_k > 0, x_i > 0$$) is generally nonconvex in $$x$$. Setting $$x_i = e^{z_i}$$ and taking the logarithm of the objective and constraints converts every posynomial into $$\ln\!\left(\sum_k \exp(a_k^T z + b_k)\right)$$, which is convex in $$z$$.
4. **Preserving Equivalence vs. Changing Optimal Value**: A strictly increasing transformation $$h$$ preserves the *minimizers* $$x^\star$$, though the *optimal value* changes from $$f^\star$$ to $$h(f^\star)$$. Always invert $$h$$ and $$\phi$$ at the end when reporting the original problem's answer.

### Step-by-Step Worked Example (Read Slowly): Unmasking a Nonconvex-Looking Posynomial Program

Minimize $$f(x_1, x_2) = x_1^{-1} x_2^{-1}$$ subject to $$x_1 > 0,\; x_2 > 0$$ and $$x_1 + 4x_2 \le 8$$.

1. **Observe the apparent nonconvexity**: The objective $$f(x_1, x_2) = (x_1 x_2)^{-1}$$ is a monomial; in general geometric programs, products and powers with arbitrary exponents do not have positive semidefinite Hessians everywhere.
2. **Apply the change of variables $$x_1 = e^{z_1},\; x_2 = e^{z_2}$$** (a bijection from $$\mathbb{R}^2$$ onto $$\mathbb{R}^2_{++}$$):
   - Objective becomes $$e^{-z_1 - z_2}$$.
   - Constraint becomes $$e^{z_1} + 4e^{z_2} \le 8$$, or equivalently $$\frac{1}{8}e^{z_1} + \frac{1}{2}e^{z_2} \le 1$$.
3. **Apply the strictly increasing transformation $$h(u) = \ln(u)$$** to both the positive objective and both sides of the positive inequality constraint:
   $$\begin{aligned} \text{minimize}_{z_1, z_2} \quad & -z_1 - z_2 \\ \text{subject to} \quad & \ln\!\left(e^{z_1 - \ln 8} + e^{z_2 - \ln 2}\right) \le 0. \end{aligned}$$
   Now the objective is linear (convex) and the constraint is a log-sum-exp of affine functions (convex)!
4. **Solve the convex problem analytically**: By symmetry of minimizing $$-z_1 - z_2$$ subject to $$e^{z_1} + 4e^{z_2} = 8$$, the constraint binds and AM–GM (or Lagrange multipliers on the convex form) gives $$e^{z_1} = 4e^{z_2} = 4$$.
   - Hence $$z_1^\star = \ln 4$$ and $$z_2^\star = \ln 1 = 0$$.
5. **Map back to the original variables**: $$x_1^\star = e^{\ln 4} = 4$$, $$x_2^\star = e^0 = 1$$. Check feasibility: $$4 + 4(1) = 8 \le 8$$. The original optimal value is $$f^\star = (4 \cdot 1)^{-1} = \frac{1}{4}$$ (matching $$e^{-z_1^\star - z_2^\star} = e^{-\ln 4} = \frac{1}{4}$$).

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
