---
layout: post
title: 03-07 Euclidean Norm - L2 - is Convex
chapter: '03'
order: 15
owner: AI Assistant
categories:
- chapter03
lang: en
---

The Euclidean norm $$f(x) = \|x\|_2$$ is the workhorse of geometry, group-Lasso regularization, and second-order cone programming—yet it carries a subtle twist: it is *not* differentiable at the origin $$x = 0$$, so a naive Hessian test alone cannot cover all of $$\mathbb{R}^n$$. Proving its convexity three distinct ways—directly via the triangle inequality, algebraically via Cauchy–Schwarz, and differentially via its rank-$$(n-1)$$ Hessian away from zero—builds deep intuition for nonsmooth convex functions.

## Background Knowledge Map: Three Complementary Proofs of $$\|x\|_2$$ Convexity

- **Triangle Inequality + Homogeneity (Cleanest):** In two lines, $$\|\theta x + (1-\theta)y\|_2 \le \|\theta x\|_2 + \|(1-\theta)y\|_2 = \theta\|x\|_2 + (1-\theta)\|y\|_2$$—working for *every* norm on $$\mathbb{R}^n$$ with zero calculus.
- **Cauchy–Schwarz Expansion:** Squaring both sides of the triangle inequality reduces convexity of $$\|x\|_2$$ directly to $$x^T y \le \|x\|_2 \|y\|_2$$, revealing that equality holds only along nonnegative rays $$y = \alpha x$$.
- **Hessian on $$\mathbb{R}^n \setminus \{0\}$$:** $$\nabla^2 \|x\|_2 = \frac{1}{\|x\|_2}\left(I - \frac{xx^T}{\|x\|_2^2}\right)$$ is a scaled orthogonal projection matrix onto $$x^\perp$$—positive semidefinite with eigenvalue $$0$$ along the radial ray $$x$$ and $$1/\|x\|_2$$ orthogonal to $$x$$.
- **Nonsmooth Kink at $$0$$:** Because the cone tip at $$x = 0$$ is nondifferentiable, optimizing $$\|x\|_2$$ requires subgradients (the unit ball $$\|g\|_2 \le 1$$), foreshadowing nonsmooth optimization.

### Step-by-Step Worked Example (Read Slowly): Inspecting the Hessian of $$\|x\|_2$$ at $$x = (3, 4)^T$$

Evaluate the gradient and Hessian of $$f(x) = \|x\|_2$$ at $$x = (3, 4)^T$$ (where $$\|x\|_2 = 5$$).

1. **Compute the gradient:**
   $$\nabla f(x) = \frac{x}{\|x\|_2} = \begin{pmatrix} 3/5 \\ 4/5 \end{pmatrix}.$$
2. **Compute the Hessian $$\nabla^2 f(x) = \frac{1}{\|x\|_2}\left(I - \frac{xx^T}{\|x\|_2^2}\right)$$:**
   $$\frac{xx^T}{25} = \frac{1}{25}\begin{pmatrix} 9 & 12 \\ 12 & 16 \end{pmatrix} \implies \nabla^2 f(3, 4) = \frac{1}{5}\begin{pmatrix} 16/25 & -12/25 \\ -12/25 & 9/25 \end{pmatrix} = \frac{1}{125}\begin{pmatrix} 16 & -12 \\ -12 & 9 \end{pmatrix}.$$
3. **Compute eigenvalues to read the geometry:**
   - Trace $$= \frac{16 + 9}{125} = \frac{1}{5}$$, Determinant $$= \frac{16(9) - (-12)^2}{125^2} = 0$$.
   - Therefore the eigenvalues are $$\lambda_1 = 1/5 > 0$$ (curving upward tangentially around the circle of radius 5) and $$\lambda_2 = 0$$ (completely linear along the radial direction $$x = (3, 4)^T$$). Thus $$\nabla^2 f(3, 4) \succeq 0$$.

The **Euclidean norm** (also called the $$\ell_2$$-norm) of a vector $$x \in \mathbb{R}^n$$ is defined as:

$$\|x\|_2 = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2} = \sqrt{x^T x}$$

We will prove that this function is convex using three different methods:
1. **Definition-based proof** using Jensen's inequality
2. **Second derivative test** (Hessian analysis)
3. **Triangle inequality approach**

## Method 1: Definition-Based Proof

<div class="textbook-theorem" markdown="1">
**Theorem**: The Euclidean norm $$f(x) = \|x\|_2$$ is convex on $$\mathbb{R}^n$$.
</div>

**Proof**: 
To prove convexity, we need to show that for any $$x, y \in \mathbb{R}^n$$ and $$\theta \in [0,1]$$:

$$\|\theta x + (1-\theta) y\|_2 \leq \theta \|x\|_2 + (1-\theta) \|y\|_2$$

Let $$z = \theta x + (1-\theta) y$$. Then:

$$\begin{align}
\|z\|_2^2 &= \|\theta x + (1-\theta) y\|_2^2 \\
&= (\theta x + (1-\theta) y)^T (\theta x + (1-\theta) y) \\
&= \theta^2 x^T x + 2\theta(1-\theta) x^T y + (1-\theta)^2 y^T y \\
&= \theta^2 \|x\|_2^2 + 2\theta(1-\theta) x^T y + (1-\theta)^2 \|y\|_2^2
\end{align}$$

By the **Cauchy-Schwarz inequality**: $$x^T y \leq \|x\|_2 \|y\|_2$$

Therefore:
$$\|z\|_2^2 \leq \theta^2 \|x\|_2^2 + 2\theta(1-\theta) \|x\|_2 \|y\|_2 + (1-\theta)^2 \|y\|_2^2$$

The right-hand side can be factored as:
$$\theta^2 \|x\|_2^2 + 2\theta(1-\theta) \|x\|_2 \|y\|_2 + (1-\theta)^2 \|y\|_2^2 = (\theta \|x\|_2 + (1-\theta) \|y\|_2)^2$$

Taking square roots of both sides:
$$\|\theta x + (1-\theta) y\|_2 \leq \theta \|x\|_2 + (1-\theta) \|y\|_2$$

This proves that the Euclidean norm is convex. $$\square$$

## Method 2: Second Derivative Test (Hessian Analysis)

For twice-differentiable functions, we can use the **second derivative test**: a function is convex if its Hessian matrix is positive semidefinite.

**Analysis**: 
The Euclidean norm $$f(x) = \|x\|_2 = \sqrt{x^T x}$$ is not differentiable at $$x = 0$$. However, for $$x \neq 0$$, we can compute:

$$\frac{\partial f}{\partial x_i} = \frac{x_i}{\|x\|_2}$$

$$\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{1}{\|x\|_2} \delta_{ij} - \frac{x_i x_j}{\|x\|_2^3}$$

The Hessian matrix is:
$$H = \frac{1}{\|x\|_2} I - \frac{1}{\|x\|_2^3} x x^T = \frac{1}{\|x\|_2} \left( I - \frac{x x^T}{\|x\|_2^2} \right)$$

**Verification of positive semidefiniteness**:
For any vector $$v \in \mathbb{R}^n$$:
$$v^T H v = \frac{1}{\|x\|_2} \left( \|v\|_2^2 - \frac{(x^T v)^2}{\|x\|_2^2} \right)$$

By Cauchy-Schwarz inequality: $$(x^T v)^2 \leq \|x\|_2^2 \|v\|_2^2$$

Therefore: $$\|v\|_2^2 - \frac{(x^T v)^2}{\|x\|_2^2} \geq 0$$

This shows $$H \succeq 0$$, confirming convexity for $$x \neq 0$$.

## Method 3: Triangle Inequality Approach

**Alternative Proof using Minkowski Inequality**:

The Euclidean norm satisfies the **triangle inequality**:
$$\|x + y\|_2 \leq \|x\|_2 + \|y\|_2$$

For convexity, let $$u = \theta x$$ and $$v = (1-\theta) y$$ where $$\theta \in [0,1]$$:
$$\|\theta x + (1-\theta) y\|_2 = \|u + v\|_2 \leq \|u\|_2 + \|v\|_2 = \theta \|x\|_2 + (1-\theta) \|y\|_2$$

This directly establishes the convexity condition.


## Key Properties and Applications

### Properties of Euclidean Norm Convexity

1. **Strict Convexity**: The Euclidean norm is actually **strictly convex** on any line not passing through the origin.

2. **Homogeneity**: $$\|\alpha x\|_2 = \lvert\alpha\rvert \|x\|_2$$ for any scalar $$\alpha$$.

3. **Subadditivity**: $$\|x + y\|_2 \leq \|x\|_2 + \|y\|_2$$ (Triangle inequality).

### Applications in Optimization

The convexity of the Euclidean norm has important implications:

1. **Least Squares Problems**: The objective function $$\|Ax - b\|_2^2$$ is convex.

2. **Regularization**: $$\ell_2$$-regularization terms like $$\lambda \|x\|_2$$ preserve convexity.

3. **Constrained Optimization**: Norm constraints $$\|x\|_2 \leq r$$ define convex feasible sets.

## Conclusion

We have proven that the Euclidean norm is convex using three different approaches:

1. **Direct definition**: Using Jensen's inequality and Cauchy-Schwarz
2. **Second derivative test**: Showing the Hessian is positive semidefinite  
3. **Triangle inequality**: Leveraging the fundamental norm property

This convexity property is fundamental in optimization theory and has wide-ranging applications in machine learning, signal processing, and numerical analysis.

The interactive visualization above demonstrates how the convexity condition $$\|\theta x + (1-\theta) y\|_2 \leq \theta \|x\|_2 + (1-\theta) \|y\|_2$$ holds for any choice of points and convex combination parameter $$\theta$$.
