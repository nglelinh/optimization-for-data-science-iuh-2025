---
layout: post
title: 05-02 Quadratic Programming (QP)
chapter: '05'
order: 3
owner: Hooncheol Shin
categories:
- chapter05
lang: en
lesson_type: required
---

A **Quadratic Program** (QP) is a convex optimization problem where the objective function is a convex quadratic function and all constraint functions are affine. The general quadratic program is formulated as:

### General Quadratic Program
$$
\begin{align}
    \text{minimize}_{x} \quad &\frac{1}{2}x^T P x + q^T x + r \\
    \text{subject to} \quad &Gx \preceq h \\
    &Ax = b
\end{align}
$$

**where:**
- $$P \in \mathbb{S}_{+}^n$$ (positive semidefinite matrix)
- $$G \in \mathbb{R}^{m \times n}$$ (inequality constraint matrix)  
- $$A \in \mathbb{R}^{p \times n}$$ (equality constraint matrix)
- $$x \in \mathbb{R}^n$$ (decision variable)

**Key Properties of QP:**
- The constant $$r$$ in the objective function does not affect the optimization process or result and can be omitted.
- If $$P \in \mathbb{S}_{+}^n$$ is not satisfied, the problem is not convex.
- Even if not explicitly stated, QP assumes $$P \in \mathbb{S}_{+}^n$$.
- The above problem seeks the minimizer $$x^*$$ of the convex quadratic function $$\frac{1}{2}x^T P x + q^T x + r$$ over a polyhedral feasible set.

### Understanding $$\mathbb{S}_{+}^n$$ (Positive Semidefinite Cone)

The notation $$\mathbb{S}_{+}^n$$ represents the **positive semidefinite cone**, which is a fundamental concept in convex optimization:

**Definition:**
> $$\mathbb{S}_{+}^n = \{ X \in \mathbb{S}^n : X \succeq 0 \}$$

**where:**
- $$\mathbb{S}^n$$ is the set of all $$n \times n$$ **symmetric matrices**
- $$X \succeq 0$$ means matrix $$X$$ is **positive semidefinite**

**Key Properties:**

1. **Positive semidefinite condition**: A matrix $$P$$ is positive semidefinite if:
   - All eigenvalues of $$P$$ are non-negative ($$\lambda_i \geq 0$$)
   - For any vector $$v$$, we have $$v^T P v \geq 0$$

2. **Convex cone property**: $$\mathbb{S}_{+}^n$$ is a convex cone because if $$\theta_1, \theta_2 \geq 0$$ and $$A, B \in \mathbb{S}_{+}^n$$, then $$\theta_1 A + \theta_2 B \in \mathbb{S}_{+}^n$$

**Example for $$n=2$$:**
For a $$2 \times 2$$ matrix $$P = \begin{bmatrix} a & b \\ b & c \end{bmatrix}$$, the condition $$P \in \mathbb{S}_{+}^2$$ requires:
- $$a \geq 0$$ (diagonal elements non-negative)
- $$c \geq 0$$ (diagonal elements non-negative)  
- $$ac \geq b^2$$ (determinant non-negative)

**Why is this important for QP?**
- The condition $$P \in \mathbb{S}_{+}^n$$ ensures that the quadratic function $$(1/2)x^T P x + q^T x + r$$ is **convex**
- Without this condition, the problem may have multiple local minima and would not be a convex optimization problem
- This guarantees that any local minimum is also a global minimum

### Understanding $$Gx \preceq h$$ (Component-wise Inequality)

The notation $$Gx \preceq h$$ represents **component-wise inequality constraints**, which is a compact way to write multiple linear inequality constraints:

**Definition:**
$$Gx \preceq h \quad \Leftrightarrow \quad (Gx)_i \leq h_i \text{ for all } i = 1, 2, \ldots, m$$

**where:**
- $$G \in \mathbb{R}^{m \times n}$$ is the constraint matrix
- $$x \in \mathbb{R}^n$$ is the decision variable vector
- $$h \in \mathbb{R}^m$$ is the right-hand side vector
- $$m$$ is the number of inequality constraints

**Expanded Form:**
The single matrix inequality $$Gx \preceq h$$ is equivalent to the system:
$$
\begin{align}
g_1^T x &\leq h_1 \\
g_2^T x &\leq h_2 \\
&\vdots \\
g_m^T x &\leq h_m
\end{align}
$$

where $$g_i^T$$ is the $$i$$-th row of matrix $$G$$.

**Example:**
Consider $$G = \begin{bmatrix} 1 & 2 \\ -1 & 3 \\ 0 & -1 \end{bmatrix}$$, $$x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$$, and $$h = \begin{bmatrix} 5 \\ 2 \\ -1 \end{bmatrix}$$

Then $$Gx \preceq h$$ means:
$$
\begin{align}
x_1 + 2x_2 &\leq 5 \\
-x_1 + 3x_2 &\leq 2 \\
-x_2 &\leq -1 \quad \text{(i.e., } x_2 \geq 1\text{)}
\end{align}
$$

**Geometric Interpretation:**
- Each inequality $$g_i^T x \leq h_i$$ defines a **half-space** in $$\mathbb{R}^n$$
- The feasible region is the **intersection** of all these half-spaces
- This intersection forms a **polyhedron** (or polytope if bounded)
- The constraint $$Gx \preceq h$$ defines the **polyhedral feasible set** for the QP

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_02_geometric_interpretation_of_QP.png" alt="[Fig 1] Geometric interpretation of QP [1]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Geometric interpretation of QP [1]</figcaption>
</p>
</figure>

## QP in Standard Form

The standard form of a quadratic program is:

### Standard Form QP
$$
\begin{align}
    \text{minimize}_{x} \quad &\frac{1}{2}x^T P x + q^T x + r \\
    \text{subject to} \quad &A x = b \\
    &x \succeq 0
\end{align}
$$

Any general quadratic program can be converted to standard form using the following steps:

### Converting QPs to Standard Form

**Step 1.** Use slack variables $$s$$ to convert inequality constraints into equality constraints:
$$
\begin{align}
    \text{minimize}_{x, s} \quad &\frac{1}{2}x^T P x + q^T x + r \\
    \text{subject to} \quad &Gx + s = h \\
    &Ax = b \\
    &s \succeq 0
\end{align}
$$

**Step 2.** Replace $$x$$ with two nonnegative variables:
$$x = x^{+} - x^{-}, \quad \text{where } x^{+}, x^{-} \succeq 0$$

$$
\begin{align}
    \text{minimize}_{x^{+}, x^{-}, s} \quad &\frac{1}{2}(x^{+} - x^{-})^T P (x^{+} - x^{-}) + q^T x^{+} - q^T x^{-} + r\\
    \text{subject to} \quad &Gx^{+} - Gx^{-} + s = h \\
    &Ax^{+} - Ax^{-} = b \\
    &s \succeq 0 \\
    &x^{+} \succeq 0, \quad x^{-} \succeq 0
\end{align}
$$

**Step 3.** Define $$\tilde{x}$$, $$\tilde{q}$$, $$\tilde{b}$$, $$\tilde{A}$$, $$\tilde{P}$$:

$$
\tilde{x} =
\begin{bmatrix}
x^{+} \\
x^{-} \\
s
\end{bmatrix}, \quad
\tilde{q} =
\begin{bmatrix}
q \\
-q \\
0
\end{bmatrix}, \quad
\tilde{b} =
\begin{bmatrix}
h \\
b
\end{bmatrix}
$$

$$
\tilde{A} =
\begin{bmatrix}
G & -G & I \\
A & -A & O
\end{bmatrix}, \quad
\tilde{P} =
\begin{bmatrix}
 P & -P & O \\
-P &  P & O \\
 O &  O & O
\end{bmatrix}
$$

**Step 4.** Substitute the expressions from Step 3 into the formulation:

$$
\begin{align}
    \text{minimize}_{\tilde{x}} \quad &\frac{1}{2}\tilde{x}^T \tilde{P} \tilde{x} + \tilde{q}^T \tilde{x} + r \\
    \text{subject to} \quad &\tilde{A} \tilde{x} = \tilde{b} \\
    &\tilde{x} \succeq 0
\end{align}
$$

## Linear Programming as a Special Case of QP

If the quadratic term is removed from the objective function of a quadratic program, it takes the form of a linear program. Thus, LP is a special case of QP, denoted as LP $$\subseteq$$ QP.

### Recall: General LP
$$
\begin{align}
    \text{minimize}_{x} \quad &c^T x + d \\
    \text{subject to} \quad &Gx \preceq h \\
    &Ax = b
\end{align}
$$
where $$G \in \mathbb{R}^{m \times n}$$ and $$A \in \mathbb{R}^{p \times n}$$.

### Example 1: Portfolio Optimization

This problem involves appropriately trading off performance and risk in creating a financial portfolio.

$$
\begin{align}
    \text{maximize}_{x} \quad &\mu^T x - \frac{\gamma}{2}x^T P x \\
    \text{subject to} \quad &\mathbf{1}^Tx = 1 \\
    &x \succeq 0
\end{align}
$$

**where:**
- $$\mu$$: expected assets' returns
- $$P$$: covariance matrix of assets' returns  
- $$\gamma$$: risk aversion parameter (hyperparameter)
- $$x$$: portfolio holdings (percentages)



### Example 2: Support Vector Machines

Support Vector Machines (SVM) are an example of a quadratic program. Below is C-SVM, a variant of SVM. A detailed explanation of SVM is beyond the scope of this chapter and will therefore be omitted.

$$
\begin{align}
    \text{minimize}_{\beta, \beta_0, \xi} \quad &\frac{1}{2} \| \beta \|_2^2 + C \sum_{i=1}^{n} \xi_i \\
    \text{subject to} \quad &\xi_i \geq 0, \quad i = 1, \ldots, n \\
    &y_i (x_i^T \beta + \beta_0) \geq 1 - \xi_i, \quad i = 1, \ldots, n
\end{align}
$$

**given:** $$y \in \{-1, 1\}^n$$ and $$X \in \mathbb{R}^{n \times p}$$ having rows $$x_1, \ldots, x_n$$.

### Example 3: Least-Squares in Regression

The problem of minimizing the following convex quadratic function corresponds to an (unconstrained) QP:
$$\| Ax - b \|_2^2 = x^T A^TA x - 2b^TAx + b^Tb$$

