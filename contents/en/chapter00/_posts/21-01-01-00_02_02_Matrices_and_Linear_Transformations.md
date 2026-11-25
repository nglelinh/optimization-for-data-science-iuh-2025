---
layout: post
title: 00-02-02 Matrices and Linear Transformations
chapter: '00'
order: 9
owner: GitHub Copilot
lang: en
categories:
- chapter00
lesson_type: required
---

A matrix is far more than a rectangular spreadsheet of numbers—it is a geometric operator that rotates, stretches, shears, and projects entire spaces. In optimization, every linear equality constraint $$Ax = b$$ asks which inputs $$x$$ land on a target $$b$$ under the transformation $$A$$, and the geometry of the solution set is governed completely by $$A$$'s column space (what is reachable) and nullspace (what directions remain invisible to $$A$$).

## Key ideas: Matrices as Geometric Operators

- **Matrix Multiplication as Composition:** Multiplying $$BAx$$ applies linear map $$A$$ followed by $$B$$—the algebraic reason matrix products are associative yet generally non-commutative.
- **Column Space (Range):** $$\mathcal{R}(A) = \{Ax : x \in \mathbb{R}^n\}$$ defines the exact set of right-hand sides $$b$$ for which $$Ax = b$$ is feasible.
- **Nullspace (Kernel):** $$\mathcal{N}(A) = \{v : Av = 0\}$$ collects all feasible step directions that leave $$Ax = b$$ unchanged, turning any single feasible point $$x_p$$ into the full affine feasible set $$x_p + \mathcal{N}(A)$$.
- **Rank–Nullity Theorem:** $$\text{rank}(A) + \dim(\mathcal{N}(A)) = n$$ balances the number of independent constraints against the remaining free optimization dimensions.

### Worked example: Parameterizing a Feasible Set via Nullspace

Consider the underdetermined linear constraint system $$Ax = b$$ with

$$A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 3 \end{pmatrix}, \qquad b = \begin{pmatrix} 4 \\ 9 \end{pmatrix}.$$

1. **Row-reduce $$[A \mid b]$$ to RREF:** Subtract $$2 \times R_1$$ from $$R_2$$:
   $$\begin{pmatrix} 1 & 2 & 1 & \mid & 4 \\ 0 & 0 & 1 & \mid & 1 \end{pmatrix} \xrightarrow{R_1 \leftarrow R_1 - R_2} \begin{pmatrix} 1 & 2 & 0 & \mid & 3 \\ 0 & 0 & 1 & \mid & 1 \end{pmatrix}.$$
2. **Read off rank and free variables:** Pivot columns are columns 1 and 3, so $$\text{rank}(A) = 2$$ and $$x_2 = t \in \mathbb{R}$$ is free ($$\dim\mathcal{N}(A) = 3 - 2 = 1$$, confirming Rank–Nullity $$2 + 1 = 3$$).
3. **Write the complete feasible set:**
   $$x_1 = 3 - 2t, \quad x_2 = t, \quad x_3 = 1 \implies x(t) = \begin{pmatrix} 3 \\ 0 \\ 1 \end{pmatrix} + t\begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}.$$
4. **Verify both parts:** $$A x_p = (3 + 0 + 1,\; 6 + 0 + 3)^T = (4, 9)^T = b$$ and $$A v = (-2 + 2 + 0,\; -4 + 4 + 0)^T = (0, 0)^T$$. Any optimization over $$Ax = b$$ now collapses to a 1D problem in $$t$$.

This lesson covers matrices, matrix operations, and linear transformations, which are fundamental tools for representing and solving optimization problems.

---

## Matrices and Matrix Operations

### What is a Matrix?

A **matrix** is a rectangular grid of numbers arranged in rows and columns. Matrices represent data, transformations, systems of equations, and relationships between variables.

**General Form:**
$$\mathbf{A} = \begin{pmatrix} 
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}$$

This is an $$m \times n$$ matrix ($$m$$ rows, $$n$$ columns).

**Example:**
$$\mathbf{A} = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$$ is a $$2 \times 3$$ matrix.

### Matrix Addition

Matrices are added by summing corresponding elements. Both matrices must have the same dimensions.

$$\mathbf{A} + \mathbf{B} = \begin{pmatrix} a_{11} + b_{11} & a_{12} + b_{12} \\ a_{21} + b_{21} & a_{22} + b_{22} \end{pmatrix}$$

**Example:**
$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix}$$

### Scalar Multiplication

Multiply every element of the matrix by the scalar:

$$c\mathbf{A} = \begin{pmatrix} ca_{11} & ca_{12} \\ ca_{21} & ca_{22} \end{pmatrix}$$

### Matrix Multiplication

For matrices $$\mathbf{A}_{m \times n}$$ and $$\mathbf{B}_{n \times p}$$, the product $$\mathbf{C}_{m \times p}$$ is formed by taking the dot product of rows from $$\mathbf{A}$$ and columns from $$\mathbf{B}$$:

$$c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$$

**Example:**
$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8 \\ 3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8 \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$

**Important:** Matrix multiplication is **not commutative**: $$\mathbf{AB} \neq \mathbf{BA}$$ in general.

---

## Linear Transformations

A **linear transformation** is a function $$T: \mathbb{R}^n \to \mathbb{R}^m$$ that preserves vector addition and scalar multiplication. Every linear transformation can be represented by a matrix.

### Definition

A transformation $$T(\mathbf{v}) = \mathbf{Av}$$ is linear if and only if:

1. **Additivity:** $$T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$$
2. **Homogeneity:** $$T(c\mathbf{v}) = cT(\mathbf{v})$$

These can be combined into: $$T(c_1\mathbf{u} + c_2\mathbf{v}) = c_1T(\mathbf{u}) + c_2T(\mathbf{v})$$

### Matrix-Vector Multiplication

If $$\mathbf{A}$$ is an $$m \times n$$ matrix and $$\mathbf{v}$$ is an $$n \times 1$$ column vector, their product $$\mathbf{Av}$$ is an $$m \times 1$$ column vector:

$$ \mathbf{w} = \mathbf{Av} = \begin{pmatrix} 
a_{11}v_1 + a_{12}v_2 + \cdots + a_{1n}v_n \\
a_{21}v_1 + a_{22}v_2 + \cdots + a_{2n}v_n \\
\vdots \\
a_{m1}v_1 + a_{m2}v_2 + \cdots + a_{mn}v_n
\end{pmatrix} $$

**Example:**
$$\begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 4 \\ 5 \end{pmatrix} = \begin{pmatrix} 2 \cdot 4 + 1 \cdot 5 \\ 0 \cdot 4 + 3 \cdot 5 \end{pmatrix} = \begin{pmatrix} 13 \\ 15 \end{pmatrix}$$

---

## Common 2D Transformations

Understanding geometric transformations helps visualize how matrices affect vectors.

### Scaling

**Scaling Matrix:**
$$\mathbf{S} = \begin{pmatrix} s_x & 0 \\ 0 & s_y \end{pmatrix}$$

- Scales x-coordinates by $$s_x$$ and y-coordinates by $$s_y$$
- **Example:** $$\begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$$ doubles x-values and triples y-values

### Rotation

**Rotation Matrix (counter-clockwise by angle $$\theta$$):**
$$\mathbf{R} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

- **Example:** 90° rotation: $$\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$
- Transforms $$(x, y) \mapsto (-y, x)$$

### Reflection

**Reflection across x-axis:**
$$\mathbf{F}_x = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**Reflection across y-axis:**
$$\mathbf{F}_y = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$$

**Reflection across line $$y = x$$:**
$$\mathbf{F}_{y=x} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

### Shearing

**Horizontal Shear:**
$$\mathbf{H} = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$$

Transforms $$(x, y) \mapsto (x + ky, y)$$

---

## Special Types of Matrices

### Identity Matrix

The **identity matrix** $$\mathbf{I}$$ acts like the number 1 for matrix multiplication:

$$\mathbf{I}_n = \begin{pmatrix} 
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1
\end{pmatrix}$$

**Property:** $$\mathbf{AI} = \mathbf{IA} = \mathbf{A}$$ for any compatible matrix $$\mathbf{A}$$.

### Transpose

The **transpose** $$\mathbf{A}^T$$ flips a matrix across its main diagonal:

$$\text{If } \mathbf{A} = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}, \text{ then } \mathbf{A}^T = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$$

**Properties:**
- $$(\mathbf{A}^T)^T = \mathbf{A}$$
- $$(\mathbf{A} + \mathbf{B})^T = \mathbf{A}^T + \mathbf{B}^T$$
- $$(\mathbf{AB})^T = \mathbf{B}^T\mathbf{A}^T$$

### Symmetric Matrices

A matrix is **symmetric** if $$\mathbf{A} = \mathbf{A}^T$$:

$$\mathbf{A} = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 5 \\ 3 & 5 & 6 \end{pmatrix}$$

Symmetric matrices have special properties important in optimization.

### Inverse Matrix

The **inverse** $$\mathbf{A}^{-1}$$ of a square matrix $$\mathbf{A}$$ satisfies:

$$\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$$

**For 2×2 matrices:**
$$\mathbf{A}^{-1} = \frac{1}{\det(\mathbf{A})} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

where $$\mathbf{A} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$ and $$\det(\mathbf{A}) = ad - bc$$.

**Note:** Not all matrices have inverses. A matrix is **invertible** (non-singular) if and only if its determinant is non-zero.

---

## Applications in Optimization

Matrices and linear transformations are fundamental in optimization for several reasons:

### 1. System of Linear Equations

Many optimization problems involve solving $$\mathbf{Ax} = \mathbf{b}$$:
- **Unique solution:** $$\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}$$ (when $$\mathbf{A}$$ is invertible)
- **Least squares:** Minimize $$\|\mathbf{Ax} - \mathbf{b}\|^2$$ when no exact solution exists

### 2. Quadratic Forms

Quadratic functions appear frequently in optimization:
$$f(\mathbf{x}) = \mathbf{x}^T\mathbf{Q}\mathbf{x} + \mathbf{c}^T\mathbf{x} + d$$

The matrix $$\mathbf{Q}$$ determines the curvature properties of the function.

### 3. Linear Programming

Standard form: Minimize $$\mathbf{c}^T\mathbf{x}$$ subject to $$\mathbf{Ax} = \mathbf{b}$$, $$\mathbf{x} \geq \mathbf{0}$$

### 4. Constraint Representation

- **Equality constraints:** $$\mathbf{Ax} = \mathbf{b}$$
- **Inequality constraints:** $$\mathbf{Ax} \leq \mathbf{b}$$

### 5. Transformations of Variables

Change of variables: $$\mathbf{y} = \mathbf{T}\mathbf{x}$$ can simplify optimization problems.

### Example: Portfolio Optimization

In finance, we might minimize portfolio risk:
$$\text{minimize } \mathbf{w}^T\mathbf{\Sigma}\mathbf{w}$$

where $$\mathbf{w}$$ is the vector of portfolio weights and $$\mathbf{\Sigma}$$ is the covariance matrix of asset returns.

Understanding matrices and linear transformations provides the tools to formulate, analyze, and solve a wide variety of optimization problems efficiently.
