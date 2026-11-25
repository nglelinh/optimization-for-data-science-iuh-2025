---
layout: post
title: 00-02-03 Eigenvalues and Eigenvectors
chapter: '00'
order: 10
owner: GitHub Copilot
lang: en
categories:
- chapter00
lesson_type: required
---

Why does gradient descent zig-zag painfully slowly down some quadratic valleys while racing straight to the bottom of others? The answer is hidden inside the eigenvalues and eigenvectors of the Hessian matrix. Eigenvectors reveal the natural, uncoupled axes of a symmetric transformation, and the ratio of the largest to smallest eigenvalue—the condition number—quantifies exactly how elongated the valley is.

## Background Knowledge Map: Spectral Geometry in Optimization

- **Invariant Directions ($$Av = \lambda v$$):** Eigenvectors are directions that $$A$$ only scales without rotating; along these axes, coupled multivariable dynamics decouple into independent 1D scalings.
- **Spectral Theorem for Symmetric Matrices:** Every real symmetric matrix (including every smooth Hessian) has real eigenvalues and an orthonormal eigenbasis $$Q = U \Lambda U^T$$.
- **Positive Definiteness via Eigenvalues:** $$Q \succ 0$$ if and only if all $$\lambda_i > 0$$ (strictly convex bowl), $$Q \succeq 0$$ if all $$\lambda_i \ge 0$$ (convex), and mixed signs signal a saddle point.
- **Condition Number ($$\kappa = \lambda_{\max}/\lambda_{\min}$$):** Measures eccentricity of quadratic level sets; large $$\kappa$$ slows first-order methods while Newton's method rescales the axes to make $$\kappa = 1$$.

### Step-by-Step Worked Example (Read Slowly): Eigen-Decomposition and Condition Number of a Hessian

Analyze the symmetric quadratic matrix $$Q = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$$ appearing in $$f(x) = \frac{1}{2}x^T Q x$$.

1. **Solve the characteristic equation $$\det(Q - \lambda I) = 0$$:**
   $$(5 - \lambda)(2 - \lambda) - 4 = \lambda^2 - 7\lambda + 6 = (\lambda - 6)(\lambda - 1) = 0 \implies \lambda_1 = 6, \; \lambda_2 = 1.$$
   Because both eigenvalues are strictly positive, $$Q \succ 0$$ and $$f$$ is strictly convex.
2. **Find unit eigenvectors:**
   - For $$\lambda_1 = 6$$: $$(Q - 6I)v = \begin{pmatrix} -1 & 2 \\ 2 & -4 \end{pmatrix}v = 0 \implies v_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix} \implies u_1 = \frac{1}{\sqrt{5}}\begin{pmatrix} 2 \\ 1 \end{pmatrix}$$.
   - For $$\lambda_2 = 1$$: $$(Q - I)v = \begin{pmatrix} 4 & 2 \\ 2 & 1 \end{pmatrix}v = 0 \implies v_2 = \begin{pmatrix} -1 \\ 2 \end{pmatrix} \implies u_2 = \frac{1}{\sqrt{5}}\begin{pmatrix} -1 \\ 2 \end{pmatrix}$$.
3. **Verify orthogonality and action:** $$u_1^T u_2 = \frac{-2 + 2}{5} = 0$$, and $$Q u_1 = \frac{1}{\sqrt{5}}\begin{pmatrix} 12 \\ 6 \end{pmatrix} = 6 u_1$$.
4. **Compute the condition number:** $$\kappa(Q) = \frac{\lambda_{\max}}{\lambda_{\min}} = \frac{6}{1} = 6$$, meaning the curvature along $$u_1$$ is six times steeper than along $$u_2$$.

This lesson covers eigenvalues and eigenvectors, which are crucial for understanding the behavior of linear transformations and quadratic functions in optimization.

---

## Definition and Intuition

When a matrix transforms a vector, it usually changes both the vector's direction and its length. However, **eigenvectors** are special vectors that, when transformed by a given matrix, only get scaled but do not change their direction.

### Mathematical Definition

For a square matrix $$\mathbf{A}$$ and a non-zero vector $$\mathbf{v}$$:

- $$\mathbf{v}$$ is an **eigenvector** of $$\mathbf{A}$$
- $$\lambda$$ is the corresponding **eigenvalue**

if they satisfy the **eigenvalue equation**:

$$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$$

### Geometric Interpretation

- **Eigenvectors:** Non-zero vectors that maintain their direction under the transformation $$\mathbf{A}$$
- **Eigenvalues:** The scalar factors by which the eigenvectors are scaled

**Visual Understanding:**
- If $$\lambda > 1$$: The eigenvector is stretched
- If $$0 < \lambda < 1$$: The eigenvector is shrunk
- If $$\lambda < 0$$: The eigenvector is scaled and flipped
- If $$\lambda = 0$$: The eigenvector is mapped to the zero vector

---

## Finding Eigenvalues and Eigenvectors

### Step 1: Find Eigenvalues

Rearrange the eigenvalue equation:
$$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$$
$$\mathbf{A}\mathbf{v} - \lambda\mathbf{v} = \mathbf{0}$$
$$(\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}$$

For a non-trivial solution ($$\mathbf{v} \neq \mathbf{0}$$), the matrix $$(\mathbf{A} - \lambda\mathbf{I})$$ must be singular, so:

$$\det(\mathbf{A} - \lambda\mathbf{I}) = 0$$

This is called the **characteristic equation**.

### Step 2: Find Eigenvectors

For each eigenvalue $$\lambda_i$$, solve the system:
$$(\mathbf{A} - \lambda_i\mathbf{I})\mathbf{v} = \mathbf{0}$$

The solutions form the **eigenspace** corresponding to $$\lambda_i$$.

---

## Detailed Example

Let's find the eigenvalues and eigenvectors of $$\mathbf{A} = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$$.

### Step 1: Find Eigenvalues

$$\mathbf{A} - \lambda\mathbf{I} = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix} - \lambda\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 3-\lambda & 1 \\ 0 & 2-\lambda \end{pmatrix}$$

$$\det(\mathbf{A} - \lambda\mathbf{I}) = (3-\lambda)(2-\lambda) - (1)(0) = (3-\lambda)(2-\lambda) = 0$$

This gives us $$\lambda_1 = 3$$ and $$\lambda_2 = 2$$.

### Step 2: Find Eigenvectors

**For $$\lambda_1 = 3$$:**
$$(\mathbf{A} - 3\mathbf{I})\mathbf{v} = \begin{pmatrix} 0 & 1 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

This gives us $$v_2 = 0$$ and $$v_1$$ can be any non-zero value. So $$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$ (or any scalar multiple).

**For $$\lambda_2 = 2$$:**
$$(\mathbf{A} - 2\mathbf{I})\mathbf{v} = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

This gives us $$v_1 + v_2 = 0$$, so $$v_2 = -v_1$$. Thus $$\mathbf{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$$ (or any scalar multiple).

### Verification

Let's verify our results:
- $$\mathbf{A}\mathbf{v}_1 = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \end{pmatrix} = 3\begin{pmatrix} 1 \\ 0 \end{pmatrix} = 3\mathbf{v}_1$$ ✓
- $$\mathbf{A}\mathbf{v}_2 = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 2 \\ -2 \end{pmatrix} = 2\begin{pmatrix} 1 \\ -1 \end{pmatrix} = 2\mathbf{v}_2$$ ✓

---

## Properties and Important Theorems

### Key Properties

1. **Sum of eigenvalues = trace of matrix:**
   $$\sum_{i=1}^n \lambda_i = \text{tr}(\mathbf{A}) = \sum_{i=1}^n a_{ii}$$

2. **Product of eigenvalues = determinant of matrix:**
   $$\prod_{i=1}^n \lambda_i = \det(\mathbf{A})$$

3. **Eigenvectors corresponding to different eigenvalues are linearly independent**

4. **If $$\mathbf{A}$$ is symmetric, all eigenvalues are real and eigenvectors are orthogonal**

### Eigenvalue Multiplicity

- **Algebraic multiplicity:** How many times $$\lambda$$ appears as a root of the characteristic polynomial
- **Geometric multiplicity:** The dimension of the eigenspace (number of linearly independent eigenvectors)

For any eigenvalue: geometric multiplicity ≤ algebraic multiplicity

---

## Diagonalization

A matrix $$\mathbf{A}$$ is **diagonalizable** if it can be written as:

$$\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$$

where:
- $$\mathbf{D}$$ is a diagonal matrix of eigenvalues
- $$\mathbf{P}$$ is a matrix whose columns are the corresponding eigenvectors

### Benefits of Diagonalization

1. **Easy computation of powers:** $$\mathbf{A}^k = \mathbf{P}\mathbf{D}^k\mathbf{P}^{-1}$$
2. **Understanding behavior:** The eigenvalues determine the transformation's behavior along each eigenvector direction

---

## Applications in Optimization

Eigenvalues and eigenvectors are crucial in optimization for several reasons:

### 1. Quadratic Forms and Definiteness

For a quadratic function $$f(\mathbf{x}) = \mathbf{x}^T\mathbf{Q}\mathbf{x}$$:

- **Positive definite** ($$f(\mathbf{x}) > 0$$ for $$\mathbf{x} \neq \mathbf{0}$$): All eigenvalues of $$\mathbf{Q}$$ are positive
- **Positive semidefinite** ($$f(\mathbf{x}) \geq 0$$): All eigenvalues are non-negative
- **Negative definite** ($$f(\mathbf{x}) < 0$$ for $$\mathbf{x} \neq \mathbf{0}$$): All eigenvalues are negative
- **Indefinite** ($$f(\mathbf{x})$$ can be positive or negative): Mixed positive and negative eigenvalues

### 2. Second-Order Optimality Conditions

For a function $$f(\mathbf{x})$$ at a critical point $$\mathbf{x}^*$$ (where $$\nabla f(\mathbf{x}^*) = \mathbf{0}$$):

- **Local minimum:** Hessian $$\nabla^2 f(\mathbf{x}^*)$$ is positive definite (all eigenvalues > 0)
- **Local maximum:** Hessian is negative definite (all eigenvalues < 0)
- **Saddle point:** Hessian is indefinite (mixed eigenvalues)

### 3. Principal Component Analysis (PCA)

PCA finds the directions of maximum variance in data:
- Eigenvectors of the covariance matrix give the principal directions
- Eigenvalues give the variance along each principal direction

### 4. Convergence Analysis

In iterative optimization algorithms:
- The **condition number** $$\kappa = \frac{\lambda_{\max}}{\lambda_{\min}}$$ affects convergence speed
- Large condition numbers lead to slow convergence

### 5. Newton's Method

Newton's method uses the inverse Hessian:
$$\mathbf{x}_{k+1} = \mathbf{x}_k - [\nabla^2 f(\mathbf{x}_k)]^{-1} \nabla f(\mathbf{x}_k)$$

The eigenvalues of the Hessian determine the method's behavior and convergence rate.

---

## Example: Optimization Application

Consider minimizing $$f(x, y) = 2x^2 + 3y^2 + 2xy$$.

The Hessian is: $$\mathbf{H} = \begin{pmatrix} 4 & 2 \\ 2 & 6 \end{pmatrix}$$

**Finding eigenvalues:**
$$\det(\mathbf{H} - \lambda\mathbf{I}) = (4-\lambda)(6-\lambda) - 4 = \lambda^2 - 10\lambda + 20 = 0$$

$$\lambda = \frac{10 \pm \sqrt{100-80}}{2} = \frac{10 \pm 2\sqrt{5}}{2} = 5 \pm \sqrt{5}$$

Since both eigenvalues are positive ($$\lambda_1 = 5 + \sqrt{5} > 0$$ and $$\lambda_2 = 5 - \sqrt{5} > 0$$), the Hessian is positive definite, confirming that the origin is a global minimum.

The condition number is $$\kappa = \frac{5 + \sqrt{5}}{5 - \sqrt{5}} \approx 4.24$$, indicating reasonably good conditioning for optimization algorithms.

Understanding eigenvalues and eigenvectors provides deep insights into the geometric and analytical properties of optimization problems, enabling better algorithm design and convergence analysis.
