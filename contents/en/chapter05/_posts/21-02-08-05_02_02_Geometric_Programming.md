---
layout: post
title: 05-02-02 Geometric Programming
chapter: '05'
order: 6
owner: Copilot
categories:
- chapter05
lang: en
---

When chip designers size transistors on a microprocessor—trading off area, power dissipation, and signal delay—every physical law is a product of powers like $$c\, w_1^{a_1} w_2^{a_2}$$. Written directly in transistor widths $$w_i > 0$$, the problem looks wildly nonconvex. Yet one logarithmic change of variables flips the entire circuit-sizing problem into a smooth convex program solvable to global optimality in milliseconds: that is the magic of Geometric Programming (GP).

## Background Knowledge Map: Monomials, Posynomials, and Log-Space Convexity

1. **Monomials vs. Posynomials**: On the strictly positive orthant $$\mathbb{R}^n_{++}$$, a *monomial* is a single term $$f(x) = c x_1^{a_1}\cdots x_n^{a_n}$$ with $$c > 0$$ and arbitrary real exponents $$a_i \in \mathbb{R}$$. A *posynomial* is any finite sum of monomials $$f(x) = \sum_{k=1}^K c_k x_1^{a_{1k}}\cdots x_n^{a_{nk}}$$ (with all $$c_k > 0$$).
2. **GP Standard-Form Rules**: A Geometric Program minimizes a posynomial $$f_0(x)$$ subject to posynomial upper bounds $$f_i(x) \le 1$$ and *monomial* equalities $$h_j(x) = 1$$. (Equality constraints must be monomials—not sums—so that taking logs turns them into affine equalities!)
3. **The Exponential Change of Variables**: Setting $$x_i = e^{y_i}$$ (so $$y_i = \ln x_i \in \mathbb{R}$$) and applying $$\ln(\cdot)$$ to the objective and constraints turns every monomial $$c \prod x_i^{a_i}$$ into an affine function $$a^T y + \ln c$$, and every posynomial into a convex *log-sum-exp* function $$\ln\bigl(\sum_k \exp(a_k^T y + b_k)\bigr)$$.
4. **Why GP Matters Beyond Circuits**: Beyond VLSI gate sizing, GPs model wireless power control, aircraft wing design, structural truss optimization, and maximum-likelihood estimation for logistic/multinomial models.

### Step-by-Step Worked Example (Read Slowly): Designing a Minimum-Surface-Area Box via GP

Design a closed rectangular box of dimensions $$w, h, d > 0$$ with volume $$whd = 8$$ that minimizes total surface area $$2wh + 2wd + 2hd$$.

1. **Recognize the Geometric Program structure**:
   - Objective $$f_0(w, h, d) = 2wh + 2wd + 2hd$$ is a **posynomial** (sum of three monomials with positive coefficients).
   - Equality constraint $$\frac{1}{8}whd = 1$$ is a **monomial equality**.
2. **Transform to convex form via $$w = e^{y_1},\; h = e^{y_2},\; d = e^{y_3}$$**:
   - Monomial equality becomes $$y_1 + y_2 + y_3 - \ln 8 = 0$$ (an affine equality!).
   - Taking $$\ln$$ of the objective gives the convex log-sum-exp problem:
     $$\min_{y \in \mathbb{R}^3} \quad \ln\!\left(2e^{y_1 + y_2} + 2e^{y_1 + y_3} + 2e^{y_2 + y_3}\right) \quad \text{s.t.} \quad y_1 + y_2 + y_3 = \ln 8.$$
3. **Solve the convex problem using symmetry / KKT**: Differentiating the Lagrangian $$\ln(S) + \nu(y_1 + y_2 + y_3 - \ln 8)$$ with respect to each $$y_i$$ gives equal partial derivatives when all three exponentials match: $$y_1 = y_2 = y_3$$.
   - From $$3y_1 = \ln 8 = 3\ln 2$$, we get $$y_1^\star = y_2^\star = y_3^\star = \ln 2$$.
4. **Transform back to physical dimensions**:
   $$w^\star = h^\star = d^\star = e^{\ln 2} = 2.$$
   Check volume: $$2 \cdot 2 \cdot 2 = 8$$. Minimum surface area: $$2(4) + 2(4) + 2(4) = 24$$.

In this section, we will see a class of problems that appear non-convex when looking at the objective function and constraint functions, but can be transformed into convex form through several techniques.

First, we need some definitions:

## 1. Monomials and Posynomials

A function $$f: \mathbb{R}^n \to \mathbb{R}$$ with domain $$\text{dom } f = \mathbb{R}^n_{++}$$ (all elements are positive) has the form:

$$f(x) = c x_1^{a_1} x_2^{a_2} \ldots x_n^{a_n} \quad \quad (24)$$

where $$c > 0$$ and $$a_i \in \mathbb{R}$$, is called a **monomial function**.

A sum of monomials:

$$f(x) = \sum_{k=1}^K c_k x_1^{a_{1k}} x_2^{a_{2k}} \ldots x_n^{a_{nk}} \quad \quad (25)$$

where $$c_k > 0$$, is called a **posynomial function**, or simply a **posynomial**.

## 2. Geometric Programming

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

## 3. Transforming GP to Convex Form

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