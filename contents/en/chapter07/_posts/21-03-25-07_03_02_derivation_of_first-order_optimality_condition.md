---
layout: post
title: 07-03-02 Derivation of First-Order Optimality Condition
chapter: '07'
order: 8
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
lesson_type: required
---

Back in Chapter 04, we proved the constrained first-order optimality condition $$\nabla f(x^\star)^T(y - x^\star) \ge 0$$ for all $$y \in C$$ using a directional-derivative argument along line segments. Now watch how the machinery of Chapter 07—indicator functions, the sum rule, and normal cones—re-derives that exact theorem in three effortless algebraic lines, revealing it as a special case of $$0 \in \partial(f + I_C)(x^\star)$$.

## Background Knowledge Map: Bridging Nonsmooth Calculus and Constrained Optimality

1. **Encoding Constraints Inside the Objective**: Rewrite $$\min_{x \in C} f(x)$$ as $$\min_{x \in \mathbb{R}^n} \bigl(f(x) + I_C(x)\bigr)$$. No constraints remain—only an extended-real-valued convex objective.
2. **Applying the Sum Rule (Under Qualification)**: Assuming $$f$$ is convex and differentiable (and $$C$$ is convex), $$\partial(f + I_C)(x^\star) = \{\nabla f(x^\star)\} + \partial I_C(x^\star) = \{\nabla f(x^\star)\} + N_C(x^\star)$$.
3. **Unpacking $$0 \in \{\nabla f(x^\star)\} + N_C(x^\star)$$**: This says precisely that $$-\nabla f(x^\star) \in N_C(x^\star)$$. By the definition of the normal cone, $$(-\nabla f(x^\star))^T(y - x^\star) \le 0$$ for all $$y \in C$$—flipping the sign gives $$\nabla f(x^\star)^T(y - x^\star) \ge 0$$ for all $$y \in C$$!
4. **Immediate Generalization to Nonsmooth Constrained Problems**: If $$f$$ is *not* differentiable, the exact same derivation works unchanged: $$x^\star$$ minimizes $$f$$ over $$C$$ iff there exists a subgradient $$g \in \partial f(x^\star)$$ such that $$g^T(y - x^\star) \ge 0$$ for all $$y \in C$$.

### Step-by-Step Worked Example (Read Slowly): Deriving Optimality on the Probability Simplex

Minimize $$f(x) = \frac{1}{2}(x_1 - 2)^2 + \frac{1}{2}(x_2 - 0)^2$$ over the 2D probability simplex $$C = \{x \in \mathbb{R}^2 : x_1 \ge 0,\; x_2 \ge 0,\; x_1 + x_2 = 1\}$$.

1. **Compute $$\nabla f(x)$$**: $$\nabla f(x) = (x_1 - 2,\; x_2)^T$$.
2. **Check the candidate vertex $$x^\star = (1, 0) \in C$$**:
   - Gradient at $$x^\star$$: $$\nabla f(1, 0) = (-1,\; 0)^T$$, so $$-\nabla f(1, 0) = (1,\; 0)^T$$.
3. **Verify $$-\nabla f(x^\star) \in N_C(x^\star)$$ directly**:
   For any feasible $$y = (y_1, y_2) \in C$$, we have $$y_1 \le 1$$, so $$y_1 - 1 \le 0$$. Therefore:
   $$(-\nabla f(x^\star))^T (y - x^\star) = 1(y_1 - 1) + 0(y_2 - 0) = y_1 - 1 \le 0.$$
   Equivalently, $$\nabla f(x^\star)^T(y - x^\star) = 1 - y_1 \ge 0$$ for every $$y \in C$$!
4. **Conclusion**: Because $$0 = \nabla f(1, 0) + (-\nabla f(1, 0)) \in \{\nabla f(1, 0)\} + N_C(1, 0)$$, $$x^\star = (1, 0)$$ is the exact constrained minimizer (with $$f^\star = 0.5$$).

### **First-order optimality condition:**

If $$f$$ is convex and differentiable, the subgradient optimality condition coincides with the first-order optimality condition, as shown below.

$$x^* \text{ is optimal} \quad \Longleftrightarrow \quad \nabla f(x^*)^T(y - x^*) \geq 0, \text{ for all } y \in C$$

### Proof
>
$$
\begin{alignat}{2}
f(x^{*}) = \min_{x\in C} f(x)  \quad & \Longleftrightarrow & & \quad f(x^{*}) = \min_x f(x) + I_C(x) \\
                      \quad & \Longleftrightarrow & &\quad 0 \in \partial(f(x^{*}) + I_C(x^{*})) \\
                      \quad & \Longleftrightarrow & &\quad 0 \in \{\nabla f(x^{*}) \} + \mathcal{N}_C(x^{*}) \\
                      \quad & \Longleftrightarrow & &\quad - \nabla f(x^{*}) \in \mathcal{N}_C(x^{*}) \\
                      \quad & \Longleftrightarrow & &\quad - \nabla f(x^{*})^Tx^{*} \geq -\nabla f(x^{*})^Ty, \text{ for all }  y \in C \\
                      \quad & \Longleftrightarrow & &\quad \nabla f(x^{*})^T(y-x^{*}) \geq 0, \text{ for all } y \in C 
\end{alignat}
$$