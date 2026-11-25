---
layout: post
title: 00-02-01 Vectors and Vector Spaces
chapter: '00'
order: 8
owner: GitHub Copilot
lang: en
categories:
- chapter00
lesson_type: required
---

When an operations researcher schedules 500 flights or a data scientist tunes 500 regression weights, those 500 numbers are not a messy list—they are a single point in $$\mathbb{R}^{500}$$. Thinking in vector spaces lets us ask sharp structural questions: are some decision variables redundant (linearly dependent)? What is the true number of independent degrees of freedom (dimension)? And can we re-express our problem in a cleaner basis where constraints decouple?

## Key ideas: Geometry of $$\mathbb{R}^n$$ for Optimization

- **Vectors & Subspaces:** Feasible perturbations around an equality-constrained point $$Ax = b$$ always form a linear subspace $$\{d : Ad = 0\}$$ closed under addition and scaling.
- **Linear Independence:** Guarantees that no feature column or constraint direction is a redundant combination of the others—essential for unique least-squares and simplex basic solutions.
- **Basis & Coordinate Representation:** A basis provides a minimal, non-redundant coordinate system so every vector in the space has a *unique* expansion $$x = \sum c_i v_i$$.
- **Dimension:** Counts the true degrees of freedom of a subspace, letting us track how many variables remain free after imposing linear equality constraints.

### Worked example: Verifying a Basis and Finding Unique Coordinates in $$\mathbb{R}^3$$

Consider the three vectors $$v_1 = (1, 1, 0)^T$$, $$v_2 = (0, 1, 1)^T$$, and $$v_3 = (1, 0, 1)^T$$, and target vector $$b = (3, 4, 3)^T$$.

1. **Test linear independence via the determinant:** Assemble $$V = [v_1\; v_2\; v_3]$$:
   $$\det(V) = \det\begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} = 1(1\cdot 1 - 0\cdot 1) - 0 + 1(1\cdot 1 - 1\cdot 0) = 1 + 1 = 2 \neq 0.$$
   Because $$\det(V) \neq 0$$, the three vectors are linearly independent and form a basis of $$\mathbb{R}^3$$ (dimension 3).
2. **Solve for the unique coordinates $$c_1 v_1 + c_2 v_2 + c_3 v_3 = b$$:**
   $$c_1 + c_3 = 3, \qquad c_1 + c_2 = 4, \qquad c_2 + c_3 = 3.$$
   Adding all three equations gives $$2(c_1 + c_2 + c_3) = 10 \implies c_1 + c_2 + c_3 = 5$$.
3. **Subtract each equation from the sum:**
   $$c_2 = 5 - 3 = 2, \qquad c_3 = 5 - 4 = 1, \qquad c_1 = 5 - 3 = 2.$$
4. **Verify directly:** $$2(1, 1, 0)^T + 2(0, 1, 1)^T + 1(1, 0, 1)^T = (3, 4, 3)^T = b$$.

This lesson introduces vectors, vector spaces, and fundamental concepts that form the foundation for understanding linear algebra in optimization contexts.

---

## Vectors and Vector Spaces ($$\mathbb{R}^n$$)

### What is a Vector?

- **Vectors:** Think of a vector as an arrow in space, representing both a direction and a magnitude (length). Mathematically, it's an ordered list of numbers, like coordinates. For example, a vector in 2D space could be $$\mathbf{v} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$$, meaning 3 units along the x-axis and 4 units along the y-axis.

- **Geometric vs Algebraic View:**
  - **Geometric:** Vectors are arrows with direction and magnitude
  - **Algebraic:** Vectors are ordered lists of real numbers

### Vector Spaces

- **Vector Space ($$\mathbb{R}^n$$):** This is the collection of all possible vectors that have $$n$$ components (numbers). For instance, $$\mathbb{R}^2$$ includes all 2-component vectors, representing all points or arrows in a 2D plane.

- **Examples:**
  - $$\mathbb{R}^2 = \left\{\begin{pmatrix} x \\ y \end{pmatrix} : x, y \in \mathbb{R}\right\}$$ (the plane)
  - $$\mathbb{R}^3 = \left\{\begin{pmatrix} x \\ y \\ z \end{pmatrix} : x, y, z \in \mathbb{R}\right\}$$ (3D space)

### Vector Operations

**Vector Addition:**
$$\mathbf{u} + \mathbf{v} = \begin{pmatrix} u_1 \\ u_2 \\ \vdots \\ u_n \end{pmatrix} + \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix} = \begin{pmatrix} u_1 + v_1 \\ u_2 + v_2 \\ \vdots \\ u_n + v_n \end{pmatrix}$$

**Scalar Multiplication:**
$$c\mathbf{v} = c \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix} = \begin{pmatrix} cv_1 \\ cv_2 \\ \vdots \\ cv_n \end{pmatrix}$$

---

## Linear Independence, Basis, and Dimension

### Linear Independence

A set of vectors $$\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k\}$$ is **linearly independent** if the only solution to:

$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0}$$

is $$c_1 = c_2 = \cdots = c_k = 0$$.

**Intuitive Understanding:** A set of vectors is "linearly independent" if no vector in the set can be created by scaling and adding the other vectors in the set. They all point in "different enough" directions.

**Example in $$\mathbb{R}^2$$:**
- $$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$ and $$\mathbf{v}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$ are linearly independent
- $$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$ and $$\mathbf{v}_2 = \begin{pmatrix} 2 \\ 4 \end{pmatrix}$$ are linearly dependent (since $$\mathbf{v}_2 = 2\mathbf{v}_1$$)

### Basis

A **basis** for a vector space is a minimal set of linearly independent vectors that can be combined (scaled and added) to create *any* other vector in that space. It's like a fundamental set of building blocks.

**Properties of a Basis:**
1. The vectors are linearly independent
2. They span the entire vector space
3. Every vector in the space can be written uniquely as a linear combination of basis vectors

**Standard Basis for $$\mathbb{R}^n$$:**
$$\mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}, \mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{pmatrix}, \ldots, \mathbf{e}_n = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{pmatrix}$$

### Dimension

The **dimension** of a vector space is simply the number of vectors in any of its bases. It tells you how many independent directions are needed to describe the space.

- $$\dim(\mathbb{R}^2) = 2$$
- $$\dim(\mathbb{R}^3) = 3$$
- $$\dim(\mathbb{R}^n) = n$$

---

## Norms of Vectors

A **norm** is a function that assigns a "length" or "size" to a vector. It generalizes the concept of distance from the origin.

### Properties of Norms

Any norm $$\|\cdot\|$$ must satisfy three properties:

1. **Non-negativity:** $$\|\mathbf{x}\| \geq 0$$, and $$\|\mathbf{x}\| = 0$$ if and only if $$\mathbf{x} = \mathbf{0}$$
2. **Homogeneity:** $$\|t\mathbf{x}\| = |t| \|\mathbf{x}\|$$ for any scalar $$t$$
3. **Triangle Inequality:** $$\|\mathbf{x} + \mathbf{y}\| \leq \|\mathbf{x}\| + \|\mathbf{y}\|$$

### Common Norms

**Euclidean Norm (L2 Norm):**
$$\|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^n x_i^2} = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}$$

This is the "ordinary" distance we're familiar with.

**Manhattan Norm (L1 Norm):**
$$\|\mathbf{x}\|_1 = \sum_{i=1}^n |x_i| = |x_1| + |x_2| + \cdots + |x_n|$$

Also called "taxicab norm" - the distance a taxi would travel in a city with a grid layout.

**Maximum Norm (L∞ Norm):**
$$\|\mathbf{x}\|_\infty = \max_{i} |x_i|$$

The largest component in absolute value.

**Example:** For $$\mathbf{x} = \begin{pmatrix} 3 \\ -4 \\ 1 \end{pmatrix}$$:
- $$\|\mathbf{x}\|_2 = \sqrt{3^2 + (-4)^2 + 1^2} = \sqrt{26} \approx 5.1$$
- $$\|\mathbf{x}\|_1 = |3| + |-4| + |1| = 8$$
- $$\|\mathbf{x}\|_\infty = \max\{|3|, |-4|, |1|\} = 4$$

---

## Inner Products (Dot Product)

The **dot product** (or inner product) is the most common way to multiply two vectors, producing a scalar result.

### Definition

For two vectors $$\mathbf{x}$$ and $$\mathbf{y}$$ in $$\mathbb{R}^n$$:

$$\mathbf{x}^T \mathbf{y} = \mathbf{x} \cdot \mathbf{y} = \sum_{i=1}^n x_i y_i = x_1 y_1 + x_2 y_2 + \cdots + x_n y_n$$

### Geometric Interpretation

$$\mathbf{x} \cdot \mathbf{y} = \|\mathbf{x}\| \|\mathbf{y}\| \cos \theta$$

where $$\theta$$ is the angle between the vectors.

### Properties

1. **Commutative:** $$\mathbf{x} \cdot \mathbf{y} = \mathbf{y} \cdot \mathbf{x}$$
2. **Distributive:** $$\mathbf{x} \cdot (\mathbf{y} + \mathbf{z}) = \mathbf{x} \cdot \mathbf{y} + \mathbf{x} \cdot \mathbf{z}$$
3. **Homogeneous:** $$(c\mathbf{x}) \cdot \mathbf{y} = c(\mathbf{x} \cdot \mathbf{y})$$

### Special Cases

- **Orthogonal vectors:** $$\mathbf{x} \cdot \mathbf{y} = 0$$ (perpendicular)
- **Parallel vectors:** $$\mathbf{x} \cdot \mathbf{y} = \pm \|\mathbf{x}\| \|\mathbf{y}\|$$
- **Self dot product:** $$\mathbf{x} \cdot \mathbf{x} = \|\mathbf{x}\|_2^2$$

### Example

For $$\mathbf{x} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$ and $$\mathbf{y} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$$:

$$\mathbf{x}^T \mathbf{y} = (1)(3) + (2)(4) = 3 + 8 = 11$$

---

## Applications in Optimization

Understanding vectors and vector spaces is crucial for optimization because:

1. **Decision Variables:** Optimization problems often involve finding the best values for multiple variables, naturally represented as vectors.

2. **Gradients:** The gradient of a function is a vector pointing in the direction of steepest increase.

3. **Constraints:** Linear constraints in optimization can be expressed using dot products: $$\mathbf{a}^T \mathbf{x} \leq b$$.

4. **Distance and Similarity:** Different norms provide different ways to measure distances between solutions or the size of changes.

5. **Orthogonality:** Many optimization concepts rely on perpendicularity, such as the relationship between gradients and level curves.

6. **Linear Combinations:** Feasible regions are often defined as linear combinations of vectors (convex hulls, cones, etc.).

The vector space framework provides the mathematical foundation for formulating and solving optimization problems systematically.
