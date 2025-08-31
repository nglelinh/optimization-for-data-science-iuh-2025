---
layout: post
title: 03-01-02 Examples of convex functions
chapter: "03"
order: 4
owner: "Minjoo Lee"
---

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
