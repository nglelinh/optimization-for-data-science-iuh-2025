---
layout: post
title: 05-01 Linear Programming (LP)
chapter: '05'
order: 2
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
---

If both the objective function and constraint functions are affine, the optimization problem is called a *linear program* (LP). The general linear program is formulated as:

### General LP

>$$ \begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{Gx \preceq h}\\\\
>    & &&{Ax = b},\\\\
>    &\text{where } &&G \in \mathbb{R}^{m \times n} \text{ and } A \in \mathbb{R}^{p \times n}.
>\end{align} $$

* The constant $$+d$$ in the objective function does not affect the optimization process or result and can be omitted.
* If you want to maximize $$c^T x + d$$ under the same constraints, you can equivalently minimize $$-c^T x - d$$.
* The above problem seeks the minimizer $$x^*$$ of the affine function $$c^T x + d$$ over a polyhedral feasible set.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_01_geometric_interpretation_of_LP.png" alt="[Fig1] Geometric interpretation of LP [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Geometric interpretation of LP [1]</figcaption>
</p>
</figure>

## LP in Standard form
Any general LP can be reformulated into the following standard form:

### Standard form LP
>$$ \begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{A x = b} \\\\
>    & &&{x \succeq 0}.
>\end{align} $$

All general LPs can be converted to standard form using the following steps:

### Converting LPs to standard form
**Step 1.** Use slack variables $$s$$ to convert inequality constraints into equality constraints:
> $$ \begin{align}
>     &\text{minimize}_{x, s} &&{c^T x + d} \\\\
>     &\text{subject to } &&{Gx + s = h} \\\\
>     & &&{Ax = b},\\\\
>     & &&{s \succeq 0}.
> \end{align} $$

**Step 2.** Replace each variable $$x$$ with two nonnegative variables:
$$ x = x^{+}  - x^{-} $$, where $$ x^{+} \text{, } x^{-} \succeq 0 $$.

> $$ \begin{align}
>     &\text{minimize}_{x^{+}, x^{-}, s} &&{c^Tx^{+} - c^Tx^{-} + d} \\\\
>     &\text{subject to } &&{Gx^{+} - Gx^{-} + s = h} \\\\
>     & &&{Ax^{+} - Ax^{-} = b},\\\\
>     & &&{s \succeq 0}\\\\
>     & &&{x^{+} \succeq 0}, {x^{-} \succeq 0}.
> \end{align} $$

**Step 3.** Define $$ \tilde{x} $$, $$ \tilde{c} $$, $$ \tilde{b} $$, and $$ \tilde{A} $$ as follows:

> $$\tilde{x} =
> \begin{bmatrix}
> x^{+} \\\\
> x^{-} \\\\
> s
> \end{bmatrix}, 
> \tilde{c} =
> \begin{bmatrix}
> c \\\\
> -c \\\\
> 0
> \end{bmatrix},
> \tilde{b} =
> \begin{bmatrix}
> h \\\\
> b
> \end{bmatrix}
> $$, 
> $$
> \tilde{A} =
> \begin{bmatrix}
> G & -G & I\\\\
> A & -A & O
> \end{bmatrix}
> $$

**Step 4.** Substitute $$ \tilde{x} $$, $$ \tilde{c} $$, $$ \tilde{b} $$, and $$ \tilde{A} $$ into the problem from Step 2:

> $$ \begin{align}
>     &\text{minimize}_{\tilde{x}} &&{\tilde{c}^T \tilde{x} + d} \\\\
>     &\text{subject to} &&{\tilde{A} \tilde{x} = \tilde{b}} \\\\
>     & &&{\tilde{x} \succeq 0}.
> \end{align} $$

### Example 1) Diet program

This problem seeks the cheapest combination of foods that meets the nutritional requirements:

> $$ \begin{align}
>     &\text{minimize}_{x} &&{c^T x} \\\\
>     &\text{subject to } &&{Dx \succeq d} \\\\
>     & &&{x \succeq 0}.
> \end{align} $$

* $$ c_j $$: Cost per unit of food item j
* $$ d_i $$: Minimum recommended intake for nutrient i
* $$ D_{ij} $$: Amount of nutrient i in food item j
* $$ x_j $$: Amount of food item j in the diet

### Example 2)  Basis pursuit

An [Undetermined linear system](https://en.wikipedia.org/wiki/Underdetermined_system) is a linear system with more variables than equations. The problem of finding the sparsest solution to $$ X\beta = y $$ is defined as the following non-convex problem:

> $$ \begin{align}
>     &\text{minimize}_{\beta} &&{\|\beta\|_0} \\\\
>     &\text{subject to } &&{X\beta = y},\\\\
>     & \text{given } &&y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^\text{n x p} \text{, where } p > n.\\\\
> \end{align} \\
$$

* $$ {\| \beta \|_0} = \sum_{j=1}^p 1, \left\{ \beta_j \neq 0 \right\} $$

The non-convexity of this problem arises from the use of the $$ L_0 $$ norm in the objective function. By using the $$ L_1 $$ norm instead, which promotes sparsity, we can reformulate the problem as a convex one. This approach is known as *basis pursuit*.

> $$ \begin{align}
>     &\text{minimize}_{\beta} &&{\|\beta\|_1} \\\\
>     &\text{subject to } &&{X\beta = y},\\\\
>     & \text{given } &&y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^\text{n x p} \text{, where } p > n.
> \end{align} \\
$$

Basis pursuit can also be expressed as a linear program:

> $$ \begin{align}
>     &\text{minimize}_{\beta, z} &&{1^Tz} \\\\
>     &\text{subject to } &&{z \succeq \beta}\\\\
>     & &&{z \succeq -\beta}\\\\
>     & &&{X\beta = y}
> \end{align} $$

* Each component of $$z$$ must be greater than or equal to the absolute value of the corresponding component of $$\beta$$.
* The optimization process aims to increase the sparsity of both $$ z $$ and $$ \beta $$.

### Example 3)  Dantzig selector

Consider the case where there is noise in the data (i.e., $$ X\beta \approx y $$). The problem, known as the [Dantzig selector](https://statweb.stanford.edu/~candes/software/l1magic/downloads/papers/DantzigSelector.pdf), is formulated as follows:

> $$ \begin{align}
>     &\text{minimize}_{\beta} &&{\|\beta\|_1} \\\\
>     &\text{subject to } &&{\| X^T (y - X \beta) \|_{\infty} \leq \lambda},\\\\
>     &\text{given } &&y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^\text{n x p} \text{, where } p > n. \ \text{Here } \lambda \geq 0 \text{ is a hyper-parameter. }\\\\
> \end{align} \\
$$

* $$ y - X \beta \in \mathbb{R}^n $$ represents the residuals.
* The constraint $$ \|y - X \beta\|_{\infty} \leq \lambda $$ ensures that the maximum absolute residual is no greater than $$\lambda$$.
* This formulation seeks to minimize the residuals while keeping them within the bounds set by $$\lambda$$.

The Dantzig selector can also be transformed into a linear program:

> $$
> \begin{align}
>     &\text{minimize}_{\beta, z} &&{\|\beta\|_1} \\\\
>     &\text{subject to } &&{x_j^T (y - X \beta) \preceq \lambda}, \text{for all } j = 1 \dotsc p\\\\
>     & &&{-x_j^T (y - X \beta) \preceq \lambda}, \text{for all } j = 1 \dotsc p\\\\
>     & && z \succeq -\beta\\\\
>     & && z \succeq \beta,\\\\
>     & \text{given } &&y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^\text{n x p} \text{, where } p > n. \ \text{Here } x_j \text{ is a jth column of } X.\\\\
> \end{align}\\
> $$
