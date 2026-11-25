---
layout: post
title: 03-01-02 Examples of convex functions
chapter: '03'
order: 4
owner: Minjoo Lee
categories:
- chapter03
lang: en
---

Just as Chapter 02 built a periodic table of convex sets, this lesson builds the periodic table of **convex functions**. From affine maps, quadratics, and norms to indicator functions $$I_C(x)$$ (which encode hard constraints directly inside an objective) and support functions $$S_C(y)$$ (which measure the farthest reach of a set in direction $$y$$), these atoms are the exact building blocks recognized by disciplined convex programming tools like CVXPY.

## Background Knowledge Map: Essential Convex Function Atoms

- **Smooth Atoms (Affine, Quadratic, Exponential, Negative Log):** Affine functions are simultaneously convex and concave; quadratics $$\frac{1}{2}x^T P x + q^T x + r$$ are convex iff $$P \succeq 0$$.
- **Norms & Pointwise Maxima:** Every norm is convex by homogeneity and the triangle inequality; $$\max_i x_i$$ is convex and piecewise-linear, modeling worst-case costs.
- **Indicator Function ($$I_C(x)$$):** Equals $$0$$ on $$C$$ and $$+\infty$$ outside $$C$$; it is convex iff $$C$$ is a convex set, letting us rewrite constrained minimization $$\min_{x \in C} f(x)$$ as unconstrained $$\min_x (f(x) + I_C(x))$$.
- **Support Function ($$S_C(y) = \sup_{x \in C} y^T x$$):** Always convex in $$y$$ (even if $$C$$ is nonconvex!) because it is a pointwise supremum of affine functions of $$y$$.

### Step-by-Step Worked Example (Read Slowly): Computing a Support Function Explicitly

Compute the support function $$S_C(y) = \sup_{x \in C} y^T x$$ of the unit $$\ell_\infty$$ box $$C = [-1, 1]^2$$, and evaluate it at $$y = (3, -2)^T$$.

1. **Maximize each coordinate independently over $$x_i \in [-1, 1]$$:**
   $$S_C(y) = \sup_{-1 \le x_1 \le 1} (y_1 x_1) + \sup_{-1 \le x_2 \le 1} (y_2 x_2).$$
   To make $$y_i x_i$$ as large as possible, choose $$x_i = +1$$ if $$y_i > 0$$ and $$x_i = -1$$ if $$y_i < 0$$, yielding $$y_i x_i = |y_i|$$.
2. **Identify the resulting convex function:**
   $$S_C(y) = |y_1| + |y_2| = \|y\|_1.$$
3. **Evaluate at $$y = (3, -2)^T$$:** The maximizing vertex is $$x^* = (1, -1)^T \in C$$, giving
   $$S_C(3, -2) = 3(1) + (-2)(-1) = 3 + 2 = 5 = \|(3, -2)^T\|_1.$$
   Thus the support function of the $$\ell_\infty$$ unit ball is precisely the convex $$\ell_1$$ norm!

This section reviews representative examples of convex functions, including:

* Exponential function
* Power function
* Affine
* Quadratic
* Least squares loss
* Norm
* Indicator function
* Support function
* Max function

## Univariate function
* Exponential function:
For any real number $$a$$, $$e^{ax}$$ is convex.
> $$e^{ax}$$ is convex for any $$a \in \mathbb{R}$$

* Power function:
For $$x, a \in \mathbb{R}_{+}$$, depending on the range of $$a$$, $$x^a$$ can be convex or concave.
> $$x^{a}$$ is convex on $$\mathbb{R}_{+}$$ for any $$a \geq 1$$ or $$a \leq 0$$
> $$x^{a}$$ is concave on $$\mathbb{R}_{+}$$ for any $$0 \leq a \leq 1$$

## Affine function
As covered in [03-01-01]({% multilang_post_url contents/chapter03/21-02-12-03_01_01_convex_functions_definition %}), all affine functions are both convex and concave.

* On $$\mathbb{R}$$ and $$\mathbb{R}^n$$:
> $$a^Tx + b$$ is convex and concave

* On $$\mathbb{R}^{m \times n}$$:
> $$\text{tr}(A^TX) + b = \sum_{i=1}^m\sum_{j=1}^n A_{ij}X_{ij} + b$$ is convex and concave

## Quadratic function
Consider the quadratic function $$f(x)=\frac{1}{2}x^TPx+q^Tx+r$$, where $$\nabla f(x)= Px+q$$ and $$\nabla^2f(x) = P$$. If $$P$$ is positive semidefinite, then $$f(x)$$ is convex.
For $$P \succeq 0$$:
> $$f(x)=\frac{1}{2}x^TPx+q^Tx+r$$ is convex with $$P \in \mathbb{S}^n, q \in \mathbb{R}^n, r \in \mathbb{R}$$

**Q: Why is $$f(x)$$ convex if $$P$$ is positive semidefinite?**
A: In a quadratic function, the second derivative is the Hessian matrix. The Hessian determines the curvature of the function, and if it is positive semidefinite, the function curves upwards. (That is, the curvature in the direction of the Hessian's eigenvectors is nonnegative.) Thus, if the second derivative is positive semidefinite, the function is convex.

## Least squares loss
For any matrix $$A$$, $$A^TA$$ is always positive semidefinite, which means that $$\left \| Ax - b \right \|_{2}^{2}$$ is always convex.

> $$f(x) = \| Ax - b \|_{2}^{2}$$ is convex for any $$A$$

## Norm
All norms on $$\mathbb{R}^n$$ are convex.
Let $$f:\mathbb{R}^n \mapsto \mathbb{R}$$ be a norm. By definition,
>$$
\begin{aligned}
f(\theta x+(1−\theta)y) \le \theta f(x)+(1−\theta)f(y), \text{  with } \theta \le \theta \le 1, \text{ for all } x,y \in \text{dom} f,
\end{aligned}
$$
>$$
\begin{aligned}
\|x\|_{p} = \left(\sum_{i=1}^{n} x_i^p\right)^{1/p} \text{ for } p \geq 1, \|x\| = \max_{i=1,.., n} |x_i|\\
\end{aligned} 
$$

## Indicator function
For a given set $$C$$, if the indicator function is defined as infinity ($$\infty$$) for elements not in $$C$$ and as zero for elements in $$C$$, then the indicator function is convex.

In other words, by defining the function to be infinitely large outside the set $$C$$ and zero within it, the convexity property is preserved.

>$$I_{C} (x) =
\begin{cases}
0, & x \in C\\
\infty, & x \notin C\\
\end{cases}
$$

## Support function
Consider a set $$C$$. Regardless of whether $$C$$ is convex, the support function of $$C$$ is convex.
> $$I_{C}^{*} (x)$$ = $$\max_{y\in C} x^Ty$$ is convex

For more on the definition of the support function, refer to the [Wikipedia definition](https://en.wikipedia.org/wiki/Support_function).

## Max function
The max function of a finite collection of convex functions is convex.
In other words, the upper envelope formed by connecting the maxima of a set of convex functions is convex.
> $$f(x) = \max \{x_1,..., x_n\}$$ is convex
