---
layout: post
title: '10-06 The Double Duality Property: The Dual of the Dual Is the Primal'
chapter: "10"
order: 7
owner: "GitHub Copilot"
lang: en
categories:
  - chapter10
redirect_from:
  - /contents/en/chapter10/10_08_Dual_of_Dual_Property/
---

In linear algebra, transposing a matrix twice returns the exact original matrix: $$(A^\top)^\top = A$$. Linear programming duality obeys an equally striking symmetry called the **involution property**: if you take a primal LP, form its dual LP, and then take the dual of *that* dual LP, you land right back on the original primal problem! Far from being a mere algebraic curiosity, this symmetry proves that every theorem you prove for primal-to-dual relationships automatically works in reverse.

## Key ideas: Why LP Duality Is an Exact Involution

- **Pillar 1 — Standardizing the Dual Back to Minimization:** Because the dual of a minimization LP is a maximization LP, taking the dual a second time requires rewriting $$\max b^\top y$$ as $$-\min (-b^\top y)$$ and converting $$\le$$ inequalities into standard form—every sign flip cancels out cleanly on the second pass.
- **Pillar 2 — Double Transposition of Matrices:** The constraint matrix $$A$$ transposes to $$A^\top$$ in the first dual and back to $$(A^\top)^\top = A$$ in the second dual; similarly, the objective vector $$c$$ and right-hand side $$b$$ swap places twice and return to their starting positions.
- **Pillar 3 — Complete Primal–Dual Feasibility Classification:** Because the dual of the dual is the primal, the 4 possible status combinations of $$(P, D)$$ are symmetric: (Optimal, Optimal), (Unbounded, Infeasible), (Infeasible, Unbounded), or (Infeasible, Infeasible). Neither LP can be bounded-feasible while the other is infeasible!
- **Pillar 4 — Contrast with General Nonlinear Optimization (Preview of Ch. 11):** In Chapter 11, we will see that the dual of the dual of a *nonconvex* problem does **not** recover the original problem—it recovers its *convexified* (biconjugate) envelope instead! Involution holds unconditionally for LPs precisely because linear functions and polyhedra are already closed and convex.

### Worked example: Taking the Dual Twice on a Standard-Form LP

Start with the standard-form primal LP $$(P)$$:
$$\min_{x}\; 2x_1 + 5x_2 \quad \text{s.t.} \quad x_1 + 3x_2 = 7, \quad x_1, x_2 \ge 0.$$
Here $$c = (2, 5)^\top$$, $$A = (1, 3)$$, $$b = 7$$.

1. **First Dual $$(D)$$:**
   $$\max_{y \in \mathbb{R}}\; 7y \quad \text{s.t.} \quad \begin{pmatrix}1 \\ 3\end{pmatrix} y \le \begin{pmatrix}2 \\ 5\end{pmatrix} \iff y \le 2,\; 3y \le 5.$$
2. **Rewrite $$(D)$$ as a minimization LP with $$\le$$ constraints:**
   $$-\min_{y \in \mathbb{R}}\; (-7y) \quad \text{s.t.} \quad y \le 2,\quad 3y \le 5.$$
   Here $$\tilde{c} = (-7)$$, $$\tilde{G} = \begin{pmatrix}1 \\ 3\end{pmatrix}$$, $$\tilde{h} = \begin{pmatrix}2 \\ 5\end{pmatrix}$$ (and no equality constraints).
3. **Take the dual of the inner minimization (with multipliers $$z = (z_1, z_2)^\top \ge 0$$):**
   - Dual objective: $$-\tilde{h}^\top z = -(2z_1 + 5z_2)$$.
   - Dual constraint $$-\tilde{G}^\top z = \tilde{c}$$: $$-(z_1 + 3z_2) = -7 \iff z_1 + 3z_2 = 7$$.
   - Inner dual is $$\max_{z \ge 0} \{ -(2z_1 + 5z_2) : z_1 + 3z_2 = 7 \}$$.
4. **Restore the outer minus sign:**
   $$-\max_{z \ge 0} \{ -(2z_1 + 5z_2) : z_1 + 3z_2 = 7 \} = \min_{z \ge 0} \{ 2z_1 + 5z_2 : z_1 + 3z_2 = 7 \},$$
   which is **symbol-for-symbol identical** to the original primal $$(P)$$ (with $$z$$ renamed to $$x$$)!

In Linear Programming, a beautiful and important mathematical property is that **the dual of the dual problem is the original (primal) problem**. This property is called the **"involution" of duality** or the **"dual-of-the-dual theorem"**.

This is a basic property that expresses the perfect symmetry of LP duality theory, and it has deep significance in both theory and applications.

---

## Recap: The Standard Form of a Linear Program (the Primal Problem)

A linear program in primal form is usually written as follows:

$$
\begin{align}
\text{minimize} \quad & c^T x \label{eq:primal-obj} \\
\text{subject to} \quad & A x \geq b, \label{eq:primal-ineq} \\
& x \geq 0, \label{eq:primal-nonneg}
\end{align}
$$

where:

- $$x \in \mathbb{R}^n$$ is the vector of decision variables
- $$c \in \mathbb{R}^n$$ is the vector of objective coefficients
- $$A \in \mathbb{R}^{m \times n}$$ is the constraint matrix
- $$b \in \mathbb{R}^m$$ is the right-hand-side vector

**Note:** An LP can be written in many different forms (maximization, equality constraints, etc.), but we can always convert it to this standard form without loss of generality.

### **Illustrative Example:**

Consider the simple problem:

$$
\begin{align}
\text{minimize} \quad & 2x_1 + 3x_2 \\
\text{subject to} \quad & x_1 + x_2 \geq 4, \\
& 2x_1 + x_2 \geq 5, \\
& x_1, x_2 \geq 0.
\end{align}
$$

Here:
- $c = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$
- $A = \begin{bmatrix} 1 & 1 \\ 2 & 1 \end{bmatrix}$
- $b = \begin{bmatrix} 4 \\ 5 \end{bmatrix}$

---

## Constructing the Dual Problem

The dual problem is constructed from the primal problem to provide bounds and information about optimality (for example, sensitivity analysis and optimality conditions).

For the primal problem above, the dual problem is defined as follows:

$$
\begin{align}
\text{maximize} \quad & b^T y \label{eq:dual-obj} \\
\text{subject to} \quad & A^T y \leq c, \label{eq:dual-ineq} \\
& y \geq 0, \label{eq:dual-nonneg}
\end{align}
$$

where $y \in \mathbb{R}^m$ is the vector of dual variables.

### **Meaning:**

- The dual problem is also an LP
- By **weak duality**: the optimal value of the dual gives a lower bound on the optimal value of the primal
- If **strong duality** holds (it always does for feasible LPs, under mild conditions such as Slater's condition), the optimal values of the two problems are equal

### **Example (continued):**

The dual of the problem above is:

$$
\begin{align}
\text{maximize} \quad & 4y_1 + 5y_2 \\
\text{subject to} \quad & y_1 + 2y_2 \leq 2, \\
& y_1 + y_2 \leq 3, \\
& y_1, y_2 \geq 0.
\end{align}
$$

---

## **Step 3: Constructing the Dual of the Dual**

Now we treat the dual problem we just constructed as a new primal problem and apply the duality rules once more.

### **Step 3.1: Convert the Dual to "Primal-Like" Form**

To make the duality rules easier to apply, we turn the maximization problem into a minimization problem by flipping the sign of the objective:

$$
\begin{align}
\text{minimize} \quad & -b^T y \\
\text{subject to} \quad & -A^T y \geq -c, \\
& y \geq 0.
\end{align}
$$

### **Step 3.2: Apply the Duality Rules**

Applying the duality rules to this problem:

- New dual variable: $z \in \mathbb{R}^n$ (same dimension as $x$ in the original primal problem)
- New objective: maximize $(-c)^T z$ (that is, $-\min c^T z$; after flipping the sign back, we get minimize $c^T z$)
- New constraints: from $-A^T y \geq -c$ and the duality rules, we get:
  - The constraint matrix of the new dual is $(-A^T)^T = -A$
  - The constraint becomes: $-A z \leq -b$
  - Simplifying: $A z \geq b$
- Non-negativity: $z \geq 0$

### **Step 3.3: The Result**

The dual of the dual is:

$$
\begin{align}
\text{minimize} \quad & c^T z \\
\text{subject to} \quad & A z \geq b, \\
& z \geq 0.
\end{align}
$$

**This is exactly the original primal problem!** (with $z$ simply being another name for $x$)

### **Example (continued):**

The dual of the dual for the example problem:

From the dual:
$$
\text{maximize } 4y_1 + 5y_2 \text{ s.t. } y_1 + 2y_2 \leq 2, \; y_1 + y_2 \leq 3, \; y_1, y_2 \geq 0
$$

Convert to minimization form:
$$
\text{minimize } -4y_1 - 5y_2 \text{ s.t. } -y_1 - 2y_2 \geq -2, \; -y_1 - y_2 \geq -3, \; y_1, y_2 \geq 0
$$

Its dual (with variables $z_1, z_2$) is the problem of maximizing $-2z_1 - 3z_2$ (equivalent to minimizing $2z_1 + 3z_2$ after flipping the sign of the objective):
$$
\begin{align}
\text{minimize} \quad & 2z_1 + 3z_2 \\
\text{subject to} \quad & z_1 + z_2 \geq 4, \\
& 2z_1 + z_2 \geq 5, \\
& z_1, z_2 \geq 0.
\end{align}
$$

**It is indeed the original primal problem!**

---

## **Step 4: Why Is This Property True? (Mathematical Explanation)**

This property comes from the **symmetry in the Lagrangian formulation** of LP.

### **4.1. The Lagrangian**

The Lagrangian of the primal problem is:

$$
\mathcal{L}(x, y) = c^T x - y^T (A x - b),
$$

where $y \geq 0$ are the Lagrange multipliers of the inequalities.

### **4.2. The Primal-Dual Relationship**

- **Primal problem**: $\min_{x \geq 0} \sup_{y \geq 0} \mathcal{L}(x, y)$
- **Dual problem**: $\max_{y \geq 0} \inf_{x \geq 0} \mathcal{L}(x, y)$

The min-max theorem (for convex-concave functions such as this linear Lagrangian) gives a symmetry:

$$
\min_x \max_y \mathcal{L}(x, y) = \max_y \min_x \mathcal{L}(x, y)
$$

When we apply duality twice, we swap min and max twice and return to the starting position.

### **4.3. The Matrix View**

The dualization process consists of:
- Transposing the matrix: $A \to A^T$
- Reversing the direction of the inequalities: $\geq$ becomes $\leq$ (or vice versa)
- Swapping the roles of $b$ and $c$

When applied twice:
- $(A^T)^T = A$ (transposing twice returns the original matrix)
- Reversing the direction twice returns the original direction
- Swapping $(b, c)$ twice returns $(b, c)$

**Conclusion:** The mathematical structure returns to where it started!

### **4.4. A Geometric Illustration**

Imagine a geometric transformation (such as a reflection across a plane):
- Applied once: we get the mirror image
- Applied twice: we return to the original position

The property "the dual of the dual is the primal" is similar: it is an **involution** (a transformation that gives the original result when applied twice).

---

## **Detailed Example: A Production Problem**

### **Primal Problem (P)**

A company produces two products, A and B. The profit from each unit of A is 3 million and from B is 5 million. There are two limited resources:
- Material: A needs 2 kg/unit, B needs 1 kg/unit, with 8 kg in total
- Time: A needs 1 hour/unit, B needs 2 hours/unit, with 10 hours in total

Find the production quantities that maximize profit.

**Formulation:**

$$
\begin{align}
\text{maximize} \quad & 3x_1 + 5x_2 \\
\text{subject to} \quad & 2x_1 + x_2 \leq 8, \\
& x_1 + 2x_2 \leq 10, \\
& x_1, x_2 \geq 0.
\end{align}
$$

Converted to standard form (minimize):

$$
\begin{align}
\text{minimize} \quad & -3x_1 - 5x_2 \\
\text{subject to} \quad & -2x_1 - x_2 \geq -8, \\
& -x_1 - 2x_2 \geq -10, \\
& x_1, x_2 \geq 0.
\end{align}
$$

### **Dual Problem (D)**

The dual has an economic meaning: find the shadow prices of the resources that **minimize** the total value of the resources, while ensuring that the resource value used by each unit of a product is not less than that product's profit. Since (P) is a maximization problem with $$\leq$$ constraints, its dual is a **minimization** problem with $$\geq$$ constraints:

$$
\begin{align}
\text{minimize} \quad & 8y_1 + 10y_2 \\
\text{subject to} \quad & 2y_1 + y_2 \geq 3, \\
& y_1 + 2y_2 \geq 5, \\
& y_1, y_2 \geq 0.
\end{align}
$$

### **Dual of the Dual (DD)**

(D) is already in the standard form "minimize, $$\geq$$ constraints, non-negative variables", with objective coefficients $$(8, 10)$$, constraint matrix $$\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$ and right-hand side $$(3, 5)$$. Applying the duality rules (new variables $$z_1, z_2$$):

$$
\begin{align}
\text{maximize} \quad & 3z_1 + 5z_2 \\
\text{subject to} \quad & 2z_1 + z_2 \leq 8, \\
& z_1 + 2z_2 \leq 10, \\
& z_1, z_2 \geq 0.
\end{align}
$$

**This is exactly the original primal problem (P)!**

**Numerical check:** (P) is optimal at $$(x_1, x_2) = (2, 4)$$ with profit $$3 \cdot 2 + 5 \cdot 4 = 26$$. (D) is optimal at $$(y_1, y_2) = (\tfrac{1}{3}, \tfrac{7}{3})$$ with value $$8 \cdot \tfrac{1}{3} + 10 \cdot \tfrac{7}{3} = 26$$. The two values are equal, as strong duality predicts.

---

## **Extension: General Convex Optimization**

The property "the dual of the dual is the primal" has been proved for Linear Programming. Does it still hold for general convex optimization problems?

**Result:** For convex optimization, the property is **conditional**:
- Slater's condition must hold
- Strong duality is required
- It does **not hold** for non-convex problems

**For details**, see **Chapter 11, Lesson 11-09**: "The Dual of the Dual in General Convex Optimization", where we analyze in depth:
- The conditions required for this property
- LP vs convex optimization
- Examples where the dual of the dual ≠ the primal
- Applications in algorithm design

---

## **References**

1. **Boyd, S., & Vandenberghe, L. (2004).** *Convex Optimization.* Cambridge University Press.
   - Chapter 5: Duality (especially Section 5.2 on LP duality)

2. **Bertsimas, D., & Tsitsiklis, J. N. (1997).** *Introduction to Linear Optimization.* Athena Scientific.
   - Chapter 4: Duality Theory

3. **Nesterov, Y. (2018).** *Lectures on Convex Optimization.* Springer.
   - Chapter 3: Duality in Convex Optimization

4. **Dantzig, G. B. (1963).** *Linear Programming and Extensions.* Princeton University Press.
   - Foundational work on LP duality
