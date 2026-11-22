---
layout: post
title: '11-07 The Dual of the Dual in General Convex Optimization'
chapter: "11"
order: 8
owner: "GitHub Copilot"
lang: en
categories:
  - chapter11
redirect_from:
  - /contents/en/chapter11/11_09_Dual_of_Dual_General_Case/
---

In the previous chapter, we saw that for Linear Programming the property "the dual of the dual is the primal" always holds. Does this property still hold for general convex optimization problems? This lesson clarifies the question.

---

## **Recap: The Dual of the Dual in LP**

In Linear Programming we have the following beautiful property:

**Primal problem:**
$$
\begin{align}
\text{minimize} \quad & c^T x \\
\text{subject to} \quad & Ax \geq b, \\
& x \geq 0
\end{align}
$$

**Dual problem:**
$$
\begin{align}
\text{maximize} \quad & b^T y \\
\text{subject to} \quad & A^T y \leq c, \\
& y \geq 0
\end{align}
$$

**Dual of the dual = Primal** (always true for LP)

But does this still hold for general convex problems?

---

## **The General Convex Problem**

### **The General Case**

Consider a general convex problem (not only LP):

$$
\begin{align}
\text{minimize} \quad & f_0(x) \\
\text{subject to} \quad & f_i(x) \leq 0, \; i = 1, \ldots, m, \\
& h_j(x) = 0, \; j = 1, \ldots, p,
\end{align}
$$

where:
- $f_0, f_1, \ldots, f_m$ are convex functions
- $h_1, \ldots, h_p$ are affine functions
- $x \in \mathbb{R}^n$ is the decision variable

---

## **Constructing the Dual Problem**

### **The Lagrangian**

The dual is defined through the Lagrangian:

$$
\mathcal{L}(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{j=1}^p \nu_j h_j(x)
$$

with:
- $\lambda \in \mathbb{R}^m$, $\lambda \geq 0$: Lagrange multipliers for the inequalities
- $\nu \in \mathbb{R}^p$: Lagrange multipliers for the equalities

### **The Dual Function**

$$
g(\lambda, \nu) = \inf_x \mathcal{L}(x, \lambda, \nu)
$$

### **The Dual Problem**

$$
\begin{align}
\text{maximize} \quad & g(\lambda, \nu) \\
\text{subject to} \quad & \lambda \geq 0
\end{align}
$$

---

## **The Dual of the Dual for a Convex Problem**

### **The Key Question**

If we take the dual of the dual problem, do we get back the original primal problem?

### **The Result**

<div class="textbook-theorem" markdown="1">
**Theorem:** If the following conditions are satisfied:
1. The primal problem is **convex**
2. **Strong duality** holds (duality gap = 0)
3. A **constraint qualification** (such as Slater's condition) holds
</div>

Then:

$$
\boxed{\text{Dual of the dual} = \text{Primal}}
$$

### **Important Conditions**

**Slater's Condition:** There exists a strictly feasible point:
- $f_i(\tilde{x}) < 0$ for all $i = 1, \ldots, m$
- $h_j(\tilde{x}) = 0$ for all $j = 1, \ldots, p$

**Important note:** This does **not always hold** for non-convex problems!

**A remark on rigor:** Slater's condition guarantees strong duality; for the dual of the dual (the "bidual") to really recover exactly the primal problem, the primal problem must additionally be convex and "closed" (that is, the objective must be lower semicontinuous). For a non-convex problem, the dual of the dual in general only gives the convexified version of the primal problem (a convex relaxation).

---

## **Comparison: LP vs Convex Optimization**

| Property | Linear Programming | Convex Optimization |
|-----------|-------------------|---------------------|
| **Dual of the dual = Primal** | Always true | Needs conditions |
| **Strong Duality** | Always true (if feasible) | Needs Slater's condition |
| **Structure** | Perfect symmetry | Conditional symmetry |
| **Constraint Qualification** | Automatically satisfied | Must be checked |

---

## **Why Is LP Special?**

LP has special properties that make "dual of the dual = primal" always true:

### **1. Always Convex**

- Linear objective → convex
- The feasible region is a polyhedron → convex

### **2. Strong Duality Is Automatic**

- No need for Slater's condition
- It is enough that one of the two problems is feasible
- Duality gap = 0 (if an optimum exists)

### **3. Perfectly Symmetric Structure**

- Matrix: $(A^T)^T = A$
- Transposing twice returns the original
- Swapping $(b, c)$ twice returns $(b, c)$

### **4. Constraint Qualification**

- Slater's condition is automatically satisfied for LP
- No need to check strict feasibility

---

## **Illustrative Examples**

### **Example 1: Quadratic Programming - Convex Case**

**Primal problem:**
$$
\begin{align}
\text{minimize} \quad & \frac{1}{2}x^T Q x + c^T x \\
\text{subject to} \quad & Ax \leq b
\end{align}
$$

with $Q \succ 0$ (positive definite).

**Properties:**
- The objective is strictly convex
- The constraints are affine
- If feasible → Slater's condition holds
- **Dual of the dual = Primal** ✓

### **Example 2: Non-Convex Case**

**Primal problem:**
$$
\text{minimize} \quad -x^2 \quad \text{subject to} \quad 0 \leq x \leq 1
$$

**The problem:**
- The objective $-x^2$ is concave, not convex
- Strong duality fails
- **Dual of the dual ≠ Primal** ✗

**Demonstration:**

Primal optimal: $x^* = 1$, $p^* = -1$

Dual (with $\lambda_1 \geq 0$ for the constraint $-x \leq 0$ and $\lambda_2 \geq 0$ for the constraint $x - 1 \leq 0$):
$$
g(\lambda_1, \lambda_2) = \inf_{x \in \mathbb{R}} \left( -x^2 - \lambda_1 x + \lambda_2 (x - 1) \right) = -\infty \quad \text{for all } \lambda_1, \lambda_2 \geq 0,
$$
because $-x^2 \to -\infty$ as $|x| \to \infty$.

- The dual problem has optimal value $d^* = -\infty$
- $d^* = -\infty < p^* = -1$

→ The duality gap is positive (in fact infinite), and the dual of the dual does not return to the primal

### **Example 3: Convex but Slater Fails**

**The problem:**
$$
\text{minimize} \quad x^2 \quad \text{subject to} \quad x^2 \leq 0
$$

**Analysis:**
- The objective is convex ✓
- The feasible region consists of a single point: $x = 0$
- There is no strictly feasible point
- **Slater's condition fails** ✗

**Result:**
- Primal: $p^* = 0$
- Dual: $d^* = 0$ 
- Strong duality still holds (by luck)
- But the structure is not perfectly symmetric

---

## **Applications and Significance**

### **1. Analyzing the Duality Gap**

When the dual of the dual does not return to the primal:
- The duality gap > 0
- We need to check the convexity conditions
- Consider relaxation methods

### **2. Algorithm Design**

- **LP**: We may choose to solve the primal or the dual freely
- **Convex**: We must check the conditions before choosing
- **Non-convex**: The dual only gives a lower bound

### **3. Optimization Theory**

This property helps:
- Understand the structure of problems more deeply
- Develop optimality conditions (KKT)
- Design primal-dual algorithms

---

## **Practice Exercises**

### **Exercise 1: Checking Slater's Condition**

For the following problems, check Slater's condition and decide whether the dual of the dual equals the primal:

a) $\min x^2 + y^2$ s.t. $x + y \geq 2$

b) $\min e^x$ s.t. $x \geq 0$

c) $\min -\log x$ s.t. $x \leq 1$, $x > 0$

### **Exercise 2: Comparing LP and QP**

Consider the two problems:

**LP:** $\min c^T x$ s.t. $Ax \leq b$

**QP:** $\min \frac{1}{2}x^T Q x$ s.t. $Ax \leq b$ with $Q \succ 0$

a) Construct the dual of each problem

b) Check the property "dual of the dual = primal"

c) Compare the required conditions

### **Exercise 3: A Non-Convex Example**

Consider the problem:
$$
\min_{x \in \mathbb{R}} x^3 \quad \text{s.t.} \quad x \geq 1
$$

a) Solve the primal problem

b) Construct the dual problem

c) Show that the dual of the dual does not return to the primal

---

## **Summary**

### **Main Conclusions**

1. **LP**: Dual of the dual = Primal (always true)

2. **Convex Optimization**: Dual of the dual = Primal (needs conditions)
   - Needs: Convexity + Strong duality + Constraint qualification

3. **Non-Convex**: Dual of the dual ≠ Primal (usually not true)

### **Important Conditions**

| Condition | LP | Convex | Non-Convex |
|-----------|-------|---------|------------|
| Convexity | ✓ (automatic) | ✓ (must check) | ✗ |
| Strong Duality | ✓ (if feasible) | ✓ (needs Slater) | ✗ (usually) |
| Dual = Dual = Primal | ✓ | ✓ (conditional) | ✗ |

### **Applications**

- Designing primal-dual algorithms
- Sensitivity analysis
- Checking optimality
- Relaxation methods

---

## **References**

1. **Boyd, S., & Vandenberghe, L. (2004).** *Convex Optimization.* Cambridge University Press.
   - Chapter 5: Duality (especially Sections 5.2 and 5.3)

2. **Rockafellar, R. T. (1970).** *Convex Analysis.* Princeton University Press.
   - Chapter 31: Duality correspondences

3. **Bertsekas, D. P. (1999).** *Nonlinear Programming* (2nd ed.). Athena Scientific.
   - Chapter 6: Duality and convex analysis

4. **Nesterov, Y. (2018).** *Lectures on Convex Optimization.* Springer.
   - Chapter 3: Duality Theory (Section 3.4)

---

**Connections with other chapters:**
- **Chapter 10**: The dual of the dual in LP (a special case)
- **Chapter 12**: KKT conditions (an application of duality)
- **Chapters 15 and 17**: The barrier method and primal-dual interior-point methods (algorithms based on duality)
