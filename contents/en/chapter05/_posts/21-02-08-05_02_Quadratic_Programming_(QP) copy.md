---
layout: post
title: 05-02 Quadratic Programming (QP)
chapter: '05'
order: 4
owner: Hooncheol Shin
categories:
- chapter05
lang: en
lesson_type: required
---

Linear Programming always pushes solutions to sharp corners—great for shipping containers, terrible for financial portfolios where putting 100% of your wealth into a single stock is reckless. By adding a smooth convex quadratic bowl $$\frac{1}{2}x^T P x$$ to the objective, Quadratic Programming (QP) balances linear rewards against quadratic risk or energy, producing interior diversification and powering everything from Markowitz portfolios to Support Vector Machines and Model Predictive Control.

## Background Knowledge Map: Structure and Geometry of Quadratic Programs

1. **Positive Semidefiniteness ($$P \in \mathbb{S}_+^n$$) Guarantees Convexity**: The Hessian of $$f(x) = \frac{1}{2}x^T P x + q^T x + r$$ is the constant matrix $$P$$ (assuming $$P = P^T$$). Requiring $$P \succeq 0$$ ensures the objective is globally convex; if $$P \succ 0$$ (positive definite), the objective is strictly convex and any feasible QP has a unique global minimizer.
2. **Ellipsoidal Level Sets Meeting a Polyhedron**: Unlike LPs whose optima sit at vertices, a QP's ellipsoidal contours can kiss the *interior* of a polyhedral face or even sit strictly inside the feasible set. Active-set QP solvers identify which linear inequalities bind and solve equality-constrained KKT linear systems on that face.
3. **Canonical Applications**:
   - *Markowitz Portfolio Optimization*: minimize variance $$\frac{1}{2}w^T \Sigma w$$ subject to expected return $$\mu^T w \ge R$$ and $$\mathbf{1}^T w = 1, w \ge 0$$.
   - *Hard/Soft-Margin SVM*: minimize $$\frac{1}{2}\|w\|_2^2 + C\sum_i \xi_i$$ subject to linear margin inequalities.
   - *Constrained Least Squares*: minimize $$\frac{1}{2}\|Ax - b\|_2^2 = \frac{1}{2}x^T(A^T A)x - (A^T b)^T x + \frac{1}{2}b^T b$$ with box/linear constraints.
4. **Equality-Constrained QP = One Linear System**: When a QP has only affine equalities $$Ax = b$$ (no inequalities), its KKT optimality conditions reduce to a single symmetric indefinite linear system $$\begin{bmatrix} P & A^T \\ A & 0 \end{bmatrix}\begin{bmatrix} x^\star \\ \nu^\star \end{bmatrix} = \begin{bmatrix} -q \\ b \end{bmatrix}$$.

### Step-by-Step Worked Example (Read Slowly): Solving an Equality-Constrained QP via the KKT System

Minimize $$f(x_1, x_2) = x_1^2 + 2x_2^2 - 2x_1 - 8x_2$$ subject to $$x_1 + x_2 = 3$$.

1. **Put into standard QP form $$\frac{1}{2}x^T P x + q^T x$$**:
   $$P = \begin{bmatrix} 2 & 0 \\ 0 & 4 \end{bmatrix} \succ 0, \qquad q = \begin{bmatrix} -2 \\ -8 \end{bmatrix}, \qquad A = \begin{bmatrix} 1 & 1 \end{bmatrix}, \qquad b = 3.$$
   Because $$P \succ 0$$, the solution is guaranteed to be unique.
2. **Assemble the KKT system $$Px + A^T \nu = -q,\; Ax = b$$**:
   $$\begin{cases} 2x_1 + \nu = 2 \\ 4x_2 + \nu = 8 \\ x_1 + x_2 = 3. \end{cases}$$
3. **Solve for $$(x_1^\star, x_2^\star, \nu^\star)$$**:
   - From the first two equations: $$x_1 = 1 - \frac{\nu}{2}$$ and $$x_2 = 2 - \frac{\nu}{4}$$.
   - Substitute into $$x_1 + x_2 = 3$$:
     $$\left(1 - \frac{\nu}{2}\right) + \left(2 - \frac{\nu}{4}\right) = 3 \implies 3 - \frac{3\nu}{4} = 3 \implies \nu^\star = 0.$$
   - Therefore $$x_1^\star = 1$$ and $$x_2^\star = 2$$!
4. **Interpret the zero multiplier**: Why did $$\nu^\star = 0$$? Because the unconstrained minimizer of $$f$$ is $$x_{\mathrm{unc}} = -P^{-1}q = (1, 2)^T$$, which *already* satisfies $$1 + 2 = 3$$! The equality constraint happens to pass straight through the bottom of the quadratic bowl, giving optimal value $$f^\star = 1^2 + 2(2)^2 - 2(1) - 8(2) = 1 + 8 - 2 - 16 = -9$$.

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

<div class="textbook-definition" markdown="1">
**Definition:**
> $$\mathbb{S}_{+}^n = \{ X \in \mathbb{S}^n : X \succeq 0 \}$$
</div>

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

<div class="textbook-definition" markdown="1">
**Definition:**
$$Gx \preceq h \quad \Leftrightarrow \quad (Gx)_i \leq h_i \text{ for all } i = 1, 2, \ldots, m$$
</div>

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

