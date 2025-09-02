---
layout: post
title: 00.02 Basic Linear Algebra
chapter: '00'
order: 3
owner: GitHub Copilot
lang: en
categories:
- chapter00
---

### Vectors and Vector Spaces ($$\mathbb{R}^n$$)
- **Vectors:** Think of a vector as an arrow in space, representing both a direction and a magnitude (length). It's a list of numbers, like coordinates. For example, a vector in 2D space could be $$\mathbf{v} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$$, meaning 3 units along the x-axis and 4 units along the y-axis.
- **Vector Space ($$\mathbb{R}^n$$):** This is the collection of all possible vectors that have $$n$$ components (numbers).  
For instance, $$\mathbb{R}^2$$ includes all 2-component vectors (like $$\begin{pmatrix} x \\ y \end{pmatrix}$$), representing all points or arrows in a 2D plane. $$\mathbb{R}^3$$ is for 3D space, and so on.

---
### Matrices and Matrix Operations

- **Matrices:** A matrix is a rectangular grid of numbers, representing data, transformations, or systems of equations. Example: $$\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$$.

- **Matrix Addition:** Matrices are added by summing corresponding elements. Example: $$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix}$$.

- **Matrix Multiplication:** Matrix multiplication is complex. For $$\mathbf{A}_{m \times n}$$ and $$\mathbf{B}_{n \times p}$$, the product $$\mathbf{C}_{m \times p}$$ is formed by taking the dot product of rows from $$\mathbf{A}$$ and columns from $$\mathbf{B}$$. Example: $$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 \\ 6 \end{pmatrix} = \begin{pmatrix} 17 \\ 39 \end{pmatrix}$$.

---
### Linear Independence, Basis, Dimension

- **Linear Independence:** A set of vectors is "linearly independent" if no vector in the set can be created by scaling and adding the other vectors in the set. They all point in "different enough" directions.

In 2D, $$\begin{pmatrix} 1 \\ 0 \end{pmatrix}$$ and $$\begin{pmatrix} 0 \\ 1 \end{pmatrix}$$ are linearly independent. But $$\begin{pmatrix} 1 \\ 0 \end{pmatrix}$$ and $$\begin{pmatrix} 2 \\ 0 \end{pmatrix}$$ are linearly dependent.

---

- **Basis:** A basis for a vector space is a minimal set of linearly independent vectors that can be combined (scaled and added) to create *any* other vector in that space. It's like a fundamental set of building blocks.

**Example:** For $$\mathbb{R}^2$$, a common basis is $$\begin{pmatrix} 1 \\ 0 \end{pmatrix}$$ and $$\begin{pmatrix} 0 \\ 1 \end{pmatrix}$$. Any 2D vector $$\begin{pmatrix} x \\ y \end{pmatrix}$$ can be written as $$x \begin{pmatrix} 1 \\ 0 \end{pmatrix} + y \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$.

---

- **Dimension:** The dimension of a vector space is simply the number of vectors in any of its bases. It tells you how many independent directions are needed to describe the space.

**Example:** $$\mathbb{R}^2$$ has a dimension of 2, and $$\mathbb{R}^n$$ has a dimension of $$n$$.

---
### Norms of vector 

A norm is a function that assigns a "length" or "size" to a vector. It's a way to measure how "big" a vector is.
  1. **Non-negativity:** The length is always zero or positive. It's zero only if the vector itself is the zero vector. ($$\lvert \mathbf{x}\ \rvert \ge 0$$, and $$\lvert \mathbf{x}\ \rvert = 0$$ if and only if $$\mathbf{x} = \mathbf{0}$$)
  2. **Homogeneity:** If you scale a vector by a number, its length scales by the absolute value of that number. ($$\lvert t\mathbf{x}\ \rvert = \lvert t \rvert \lvert \mathbf{x}\ \rvert$$ for any scalar $$t$$)
  3. **Triangle Inequality:** The length of the sum of two vectors is less than or equal to the sum of their individual lengths ($$\lvert \mathbf{x} + \mathbf{y}\ \rvert \le \lvert \mathbf{x}\ \rvert + \lvert \mathbf{y}\ \rvert$$)

---

**Euclidean Norm (L2 Norm):** This is the most common and intuitively understood norm, representing the standard straight-line distance from the origin to the vector's endpoint in an n-dimensional Euclidean space. 

**Formula:** $$\lvert \mathbf{x} \rvert_2 = \sqrt{\sum_{i=1}^n x_i^2}$$ 

**Example:** For a 2D vector $$\mathbf{x} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$$, its Euclidean norm is $$\lvert \mathbf{x} \rvert_2 = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$. Similarly, for a 3D vector $$\mathbf{y} = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$$, its L2 norm would be $$\lvert \mathbf{y}\ \rvert_2 = \sqrt{1^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$$.

---

**Properties and Significance:** The Euclidean norm satisfies the three defining properties of any norm, making it a fundamental concept in linear algebra and functional analysis:
1.  **Non-negativity:** $$\lvert \mathbf{x}\ \rvert_2 \ge 0$$, and $$\lvert \mathbf{x}\ \rvert_2 = 0$$ if and only if $$\mathbf{x} = \mathbf{0}$$ (the zero vector).
2.  **Absolute Homogeneity:** For any scalar $$c \in \mathbb{R}$$, $$\lvert c\mathbf{x}\ \rvert_2 = \lvert c \rvert\lvert \mathbf{x}\ \rvert_2$$.
3.  **Triangle Inequality:** For any vectors $$\mathbf{x}, \mathbf{y} \in \mathbb{R}^n$$, $$\lvert \mathbf{x} + \mathbf{y}\ \rvert_2 \le \lvert \mathbf{x}\ \rvert_2 + \lvert \mathbf{y}\ \rvert_2$$.
The L2 norm is particularly important because it is induced by the standard Euclidean inner product (dot product): $$\lvert \mathbf{x}\ \rvert_2 = \sqrt{\mathbf{x} \cdot \mathbf{x}}$$. This intrinsic connection makes it central to defining concepts like orthogonality, projections, and angles between vectors. It is widely used across various fields, including machine learning (e.g., as a component of Mean Squared Error loss functions, L2 regularization in Ridge Regression to penalize large weights and prevent overfitting), optimization algorithms, signal processing, and physics for calculating vector magnitudes and distances in real-world applications.

---

**Manhattan Norm (L1 Norm):** Also known as the Taxicab Norm or City Block Distance, the L1 norm represents the sum of the absolute values of the vector's components. Its name derives from the idea of navigating a grid-like city (like Manhattan), where one can only move along horizontal or vertical streets, not diagonally.

**Formula:** $$\lvert \mathbf{x}\ \rvert_1 = \sum_{i=1}^n \lvert x_i \rvert$$

**Example:** For $$\mathbf{x} = \begin{pmatrix} 3 \\ -4 \end{pmatrix}$$, its Manhattan norm is $$\lvert \mathbf{x}\ \rvert_1 = \lvert 3 \rvert + \lvert -4 \rvert = 3 + 4 = 7$$. For a 3D vector $$\mathbf{y} = \begin{pmatrix} 1 \\ -2 \\ 2 \end{pmatrix}$$, its L1 norm would be $$\lvert \mathbf{y}\ \rvert_1 = \lvert 1 \rvert + \lvert -2 \rvert + \lvert 2 \rvert = 1 + 2 + 2 = 5$$.

**Properties and Significance:** The L1 norm also satisfies the three fundamental properties of a norm (non-negativity, absolute homogeneity, and triangle inequality). Geometrically, the "unit ball" (the set of all vectors with norm 1) in L1 space is a hyperoctahedron (a square in 2D, an octahedron in 3D). This "pointy" shape at the axes is crucial for its applications. The L1 norm is particularly valued in:
*   **Robustness to Outliers:** Unlike the L2 norm, which squares errors and thus heavily penalizes large deviations, the L1 norm treats all errors linearly, making it less sensitive to outliers.
*   **Feature Selection and Sparsity:** In machine learning, L1 regularization (Lasso Regression) is known to promote sparse solutions, meaning it drives some coefficients to exactly zero. This effectively performs automatic feature selection, simplifying models and improving interpretability by identifying the most important features.
*   **Compressed Sensing:** The L1 norm plays a vital role in compressed sensing, where it is used to recover sparse signals from incomplete measurements.

---

**Maximum Norm (L-infinity Norm):** Also known as the Chebyshev Norm or Uniform Norm, the L-infinity norm defines the magnitude of a vector as the largest absolute value among its components. It represents the maximum deviation of any single component from zero.

**Formula:** $$\lvert \mathbf{x}\ \rvert_\infty = \max_{i} \lvert x_i \rvert$$

**Example:** For $$\mathbf{x} = \begin{pmatrix} 3 \\ -4 \end{pmatrix}$$, its maximum norm is $$\lvert \mathbf{x}\ \rvert_\infty = \max(\lvert 3 \rvert, \lvert -4 \rvert) = \max(3, 4) = 4$$. For a 3D vector $$\mathbf{y} = \begin{pmatrix} 1 \\ -5 \\ 2 \end{pmatrix}$$, its L-infinity norm would be $$\lvert \mathbf{y}\ \rvert_\infty = \max(\lvert 1 \rvert, \lvert -5 \rvert, \lvert 2 \rvert) = \max(1, 5, 2) = 5$$.

These three norms (L1, L2, and L-infinity) are specific instances of the more general **Lp-norm**, defined as $$\lvert \mathbf{x}\ \rvert_p = \left(\sum_{i=1}^n \lvert x_i \rvert^p\right)^{1/p}$$ for $$p \ge 1$$. As $$p \to \infty$$, the Lp-norm converges to the L-infinity norm, demonstrating a continuous spectrum of ways to measure vector magnitude, each with unique geometric interpretations and practical implications.

---
### Inner Products (Dot Product)

- An inner product is a way to multiply two vectors to get a single scalar (a number). It tells us something about how much the vectors point in the same direction and also relates to their lengths.

- **Dot Product:** The most common inner product. For two vectors $$\mathbf{x} = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}$$ and $$\mathbf{y} = \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix}$$, it's calculated by multiplying corresponding components and summing the results.

  **Formula:** $$\mathbf{x}^T \mathbf{y} = \sum_{i=1}^n x_i y_i$$

  **Example:** For $$\mathbf{x} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$ and $$\mathbf{y} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$$, $$\mathbf{x}^T \mathbf{y} = (1 \times 3) + (2 \times 4) = 3 + 8 = 11$$.

---
### Linear transformation

A matrix acts as an operator that takes an input vector and produces an output vector, effectively changing its position, orientation, magnitude, or a combination of these in space.

A transformation (or function, or mapping) takes an input and produces an output. In linear algebra, a **linear transformation** is a special type of transformation that maps vectors from one vector space to another (or the same space) while preserving the operations of vector addition and scalar multiplication. Every linear transformation can be uniquely represented by a matrix.

---
### How a Matrix Transforms a Vector (Matrix-Vector Multiplication)

The process by which a matrix transforms a vector is through **matrix-vector multiplication**. If $$\mathbf{A}$$ is an $$m \times n$$ matrix and $$\mathbf{v}$$ is an $$n \times 1$$ column vector, their product $$\mathbf{Av}$$ is an $$m \times 1$$ column vector. The number of columns in the matrix must equal the number of rows (components) in the vector for the multiplication to be defined.

Let $$\mathbf{A}$$ be an $$m \times n$$ matrix and $$\mathbf{v}$$ be an $$n \times 1$$ column vector:
$$ \mathbf{A} = \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix}, \quad \mathbf{v} = \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix} $$
The transformed vector, $$\mathbf{w} = \mathbf{Av}$$, is calculated as:
$$ \mathbf{w} = \mathbf{Av} = \begin{pmatrix} a_{11}v_1 + a_{12}v_2 + \dots + a_{1n}v_n \\ a_{21}v_1 + a_{22}v_2 + \dots + a_{2n}v_n \\ \vdots \\ a_{m1}v_1 + a_{m2}v_2 + \dots + a_{mn}v_n \end{pmatrix} $$
Each component of the resulting vector $$\mathbf{w}$$ is the dot product of the corresponding row of $$\mathbf{A}$$ with the vector $$\mathbf{v}$$.

Alternatively, the product $$\mathbf{Av}$$ can be seen as a linear combination of the columns of $$\mathbf{A}$$, where the coefficients are the components of $$\mathbf{v}$$. If $$\mathbf{A} = \begin{pmatrix} \mathbf{c}_1 & \mathbf{c}_2 & \dots & \mathbf{c}_n \end{pmatrix}$$, where $$\mathbf{c}_i$$ are the column vectors of $$\mathbf{A}$$, then:
$$ \mathbf{Av} = v_1 \mathbf{c}_1 + v_2 \mathbf{c}_2 + \dots + v_n \mathbf{c}_n $$
---
### Geometric Interpretation

Geometrically, when a matrix transforms a vector, it maps the point represented by the original vector to a new point in space. This mapping can involve:

*   **Changing the length (magnitude)** of the vector.
*   **Changing the direction** of the vector.
*   **Changing the dimension** of the vector (e.g., mapping a 3D vector to a 2D vector, or vice-versa, if $$m \neq n$$).

Linear transformations have specific properties: they always map the origin to the origin, and they transform lines into lines (or points) and parallelograms into parallelograms (or lines/points).

---
### Common Types of 2D Transformations Represented by Matrices

Here are some common linear transformations in 2D space and their corresponding matrices:

### a. Scaling
Changes the length of the vector along the x and y axes.
Let $$s_x$$ be the scaling factor for the x-axis and $$s_y$$ for the y-axis.
**Scaling Matrix:**
$$ \mathbf{S} = \begin{pmatrix} s_x & 0 \\ 0 & s_y \end{pmatrix} $$
**Transformation:**
$$ \mathbf{v}' = \mathbf{Sv} = \begin{pmatrix} s_x & 0 \\ 0 & s_y \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} s_x x \\ s_y y \end{pmatrix} $$

### b. Rotation
Rotates the vector around the origin by an angle $$\theta$$ (counter-clockwise).
**Rotation Matrix:**
$$ \mathbf{R} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} $$
**Transformation:**
$$ \mathbf{v}' = \mathbf{Rv} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x\cos\theta - y\sin\theta \\ x\sin\theta + y\cos\theta \end{pmatrix} $$

### c. Reflection
Reflects the vector across a line or plane.
**Reflection across the x-axis:**
$$ \mathbf{F}_x = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} $$
**Reflection across the y-axis:**
$$ \mathbf{F}_y = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} $$
**Reflection across the line $$y=x$$:**
$$ \mathbf{F}_{y=x} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} $$

### d. Shear(**Cắt**)

Skews the vector, shifting points in one direction proportional to their coordinate in another direction.
**Horizontal Shear (x-shear by factor $$k$$):**
$$ \mathbf{H}_x = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix} $$
**Vertical Shear (y-shear by factor $$k$$):**
$$ \mathbf{H}_y = \begin{pmatrix} 1 & 0 \\ k & 1 \end{pmatrix} $$

### e. Projection
Projects the vector onto a subspace (e.g., an axis or a line).
**Projection onto the x-axis:**
$$ \mathbf{P}_x = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} $$
**Projection onto the y-axis:**
$$ \mathbf{P}_y = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} $$

### Properties of Linear Transformations

A transformation $$T(\mathbf{v}) = \mathbf{Av}$$ is linear if and only if it satisfies two properties for any vectors $$\mathbf{u}, \mathbf{v}$$ and any scalar $$c$$:

1.  **Additivity:** The transformation of a sum of vectors is the sum of their transformations.
    $$ \mathbf{A}(\mathbf{u} + \mathbf{v}) = \mathbf{Au} + \mathbf{Av} $$
2.  **Homogeneity of Degree 1:** The transformation of a scalar multiple of a vector is the scalar multiple of its transformation.
    $$ \mathbf{A}(c\mathbf{v}) = c(\mathbf{Av}) $$

These properties ensure that linear transformations preserve the structure of vector spaces, making them incredibly useful in various fields.

### Applications

The concept of a matrix transforming a vector is fundamental to:

*   **Computer Graphics:** For rendering 2D and 3D objects (scaling, rotation, translation, projection).
*   **Physics and Engineering:** Describing forces, rotations, stress, strain, and solving systems of linear equations.
*   **Data Science and Machine Learning:** Principal Component Analysis (PCA), neural networks, and various data manipulations.
*   **Quantum Mechanics:** Representing quantum states and operators.

In essence, a matrix provides a concise and powerful way to describe how vectors (and thus points or directions in space) are manipulated or moved, forming the bedrock of many mathematical and computational disciplines.

---
### Eigenvalues and Eigenvectors (Giá trị riêng và Vector riêng)

When a matrix transforms a vector, it usually changes both its direction and its length.

- **Eigenvectors:** These are special, non-zero vectors that, when transformed by a given matrix, only get scaled (stretched or shrunk) but do not change their direction. They point in the "natural" directions of the transformation.

- **Eigenvalues:** These are the scalar factors by which the eigenvectors are scaled. Each eigenvector has a corresponding eigenvalue.

- The relationship is defined by the equation: $$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$$, where $$\mathbf{A}$$ is the matrix, $$\mathbf{v}$$ is the eigenvector, and $$\lambda$$ is the eigenvalue.

- **Example:** If a matrix represents a scaling operation, the eigenvectors would be along the axes of scaling, and the eigenvalues would be the scaling factors.