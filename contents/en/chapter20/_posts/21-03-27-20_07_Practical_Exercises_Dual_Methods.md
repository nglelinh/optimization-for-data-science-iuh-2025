---
layout: post
title: '20-07 Practical Exercises - Dual Methods'
chapter: '20'
order: 15
owner: GitHub Copilot
lang: en
categories:
- chapter20
lesson_type: required
redirect_from:
  - /contents/en/chapter20/20_06_Practical_Exercises_Dual_Methods/
---

Mastering dual methods means being able to move fluidly between three representations of the same constrained problem: the **primal Lagrangian**, the **dual ascent / decomposition update**, and the **scaled ADMM splitting**. Before working through the exercises below (adapted from Bertsekas and Boyd et al.), test your intuition on this quick warm-up comparing plain dual decomposition against Augmented Lagrangian on a 2-variable equality problem—seeing firsthand how $$\rho$$ stabilizes the dual trajectory.

## Key ideas: Key Techniques Practiced in These Exercises

- **Deriving Decomposed Subproblems:** Separate $$\sum_i f_i(x_i) + \nu^T(\sum_i A_i x_i - c)$$ into $$N$$ independent scalar or vector minimizations and compute the exact dual ascent residual.
- **Constructing Augmented Lagrangians:** Add $$\frac{\rho}{2}\|Ax - b\|_2^2$$, solve the regularized primal step, and verify that updating $$\nu^{k+1} = \nu^k + \rho(Ax^{k+1} - b)$$ enforces dual feasibility automatically.
- **Designing ADMM Splittings:** Introduce auxiliary variables $$z$$ so that the $$x$$-update is a clean linear solve (Cholesky cacheable!) and the $$z$$-update is a closed-form proximal operator (soft-thresholding or projection).
- **Monitoring Stopping Criteria:** Track both primal residual $$\|r^{(k)}\|_2$$ and dual residual $$\|s^{(k)}\|_2$$ to diagnose whether $$\rho$$ is too large (tiny $$r$$, huge $$s$$) or too small (huge $$r$$, tiny $$s$$).

### Worked example: Diagnosing $$\rho$$ Imbalance from Residuals

Suppose you run ADMM on $$\min_{x,z} \frac{1}{2}(x - 10)^2 + \frac{1}{2}z^2$$ s.t. $$x - z = 0$$ from $$z^0 = 0, w^0 = 0$$ (exact optimum $$x^\star = z^\star = 5$$). Compare one iteration with tiny $$\rho = 0.1$$ vs. balanced $$\rho = 1$$:

1. **With $$\rho = 0.1$$ (under-penalized):**
   - $$x^1 = \frac{10 + 0.1(0)}{1 + 0.1} = \frac{10}{1.1} \approx 9.091$$.
   - $$z^1 = \frac{0.1(9.091)}{1 + 0.1} \approx 0.826$$.
   - Primal residual: $$|r^1| = |9.091 - 0.826| = 8.265$$ (huge!); Dual residual: $$|s^1| = \rho |z^1 - z^0| = 0.1(0.826) = 0.083$$ (tiny!).
   - Ratio $$|r^1| / |s^1| \approx 100$$—immediately signaling that $$\rho$$ is too small and should be increased!
2. **With $$\rho = 1.0$$ (balanced):**
   - $$x^1 = \frac{10}{2} = 5.0$$, $$z^1 = \frac{5}{2} = 2.5$$.
   - Primal residual: $$|r^1| = 2.5$$; Dual residual: $$|s^1| = 1.0(2.5) = 2.5$$.
   - Ratio $$|r^1| / |s^1| = 1.0$$—perfectly balanced, cutting the error in half every single step! Keep this residual-balance diagnostic in mind as you work through the exercises below.

# Practical Exercises - Dual Methods

The exercises are adapted from Bertsekas (1999) and Boyd et al. (2011).

---

## 📝 **Exercise 1: Dual Decomposition**

Minimize $$\sum_{i=1}^N f_i(x_i)$$ s.t. $$\sum x_i = c$$.

**Tasks:**  
a) Write the Lagrangian and the dual  
b) Decompose into $$N$$ independent subproblems  
c) Update the dual variable $$\nu$$

<details>
<summary><strong>💡 Solution</strong></summary>

**Lagrangian:**

$$L(x, \nu) = \sum_i f_i(x_i) + \nu\left(\sum x_i - c\right)$$

$$= \sum_i [f_i(x_i) + \nu x_i] - \nu c$$

**Dual:**

$$g(\nu) = \sum_i \min_{x_i} [f_i(x_i) + \nu x_i] - \nu c$$

**Decomposition:** Solve the $$N$$ problems in parallel!

**Dual update:** $$\nu^{(k+1)} = \nu^{(k)} + \alpha(\sum x_i^{(k)} - c)$$

</details>

---

## 📝 **Exercise 2: Augmented Lagrangian**

$$\min f(x)$$ s.t. $$Ax = b$$.

**Tasks:**  
a) Write the augmented Lagrangian $$L_\rho(x, \nu)$$  
b) Compare it with the standard Lagrangian  
c) Derive dual ascent with a quadratic penalty

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Augmented Lagrangian:**

$$L_\rho(x, \nu) = f(x) + \nu^T(Ax - b) + \frac{\rho}{2}\|Ax - b\|^2$$

**b) Advantage:**

**Standard:** $$g(\nu)$$ may be non-differentiable

**Augmented:** smoother dual, better conditioning

**c) ALM iterations:**

1. $$x^{(k+1)} = \arg\min_x L_\rho(x, \nu^{(k)})$$
2. $$\nu^{(k+1)} = \nu^{(k)} + \rho(Ax^{(k+1)} - b)$$

</details>

---

## 📝 **Exercise 3: Method of Multipliers**

Apply ALM to $$\min x_1^2 + x_2^2$$ s.t. $$x_1 + x_2 = 1$$.

**Tasks:**  
a) Set up the ALM  
b) Iterate from $$\nu^{(0)} = 0$$, $$\rho = 1$$  
c) Compare with dual gradient ascent

<details>
<summary><strong>💡 Solution</strong></summary>

**a) ALM:**

$$L_\rho(x, \nu) = x_1^2 + x_2^2 + \nu(x_1 + x_2 - 1) + \frac{1}{2}(x_1 + x_2 - 1)^2$$

**b) $$x$$-minimization:**

$$\nabla_x L = (2x_1 + \nu + (x_1 + x_2 - 1), 2x_2 + \nu + (x_1 + x_2 - 1)) = 0$$

$$3x_1 + x_2 = 1 - \nu$$

$$x_1 + 3x_2 = 1 - \nu$$

Solution: $$x_1 = x_2 = \frac{1-\nu}{4}$$

**Iteration 0:** $$\nu = 0$$ → $$x = (0.25, 0.25)$$

Residual: $$0.5 - 1 = -0.5$$

$$\nu^{(1)} = 0 + 1(-0.5) = -0.5$$

**Iteration 1:** $$x = (0.375, 0.375)$$, $$\nu^{(2)} = -0.75$$

Converges to $$x^* = (0.5, 0.5)$$, $$\nu^* = -1$$

</details>

---

## 📝 **Exercise 4: Dual Gradient vs Dual Newton**

Maximize $$g(\nu)$$ with gradient ascent and with Newton's method.

**Tasks:**  
a) Gradient: $$\nu^{(k+1)} = \nu^{(k)} + \alpha \nabla g(\nu^{(k)})$$  
b) Newton: $$\nu^{(k+1)} = \nu^{(k)} - (\nabla^2 g)^{-1} \nabla g$$  
c) Compare the convergence

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Dual gradient:**

$$\nabla g(\nu) = Ax^*(\nu) - b$$

$$\nu^{(k+1)} = \nu^{(k)} + \alpha(Ax^{(k)} - b)$$

**Rate:** sublinear $$O(1/k)$$ in general (as for the subgradient method if $$g$$ is non-smooth); linear when $$g$$ is strongly concave, i.e. when $$f$$ is smooth and $$A$$ has full row rank.

**b) Dual Newton:**

$$\nabla^2 g(\nu) = A \frac{\partial x^*}{\partial \nu} A^T$$

**Quadratic convergence** (locally) if $$g$$ is smooth and strongly concave.

**c) Tradeoff:**

- **Gradient:** cheap per iteration
- **Newton:** expensive (Hessian), fast convergence

</details>

---

## 📝 **Exercise 5: Consensus Optimization**

$$N$$ agents minimize $$\sum f_i(x_i)$$ s.t. $$x_1 = x_2 = \cdots = x_N$$.

**Tasks:**  
a) Dual decomposition  
b) Average consensus update  
c) Distributed implementation

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Lagrangian:**

$$L(x, \nu) = \sum_i f_i(x_i) + \sum_{i<j} \nu_{ij}(x_i - x_j)$$

**Dual:**

$$g(\nu) = \sum_i \min_{x_i} \left[ f_i(x_i) + \sum_j \nu_{ij}(x_i - x_j) \right]$$

**b) Update:**

Each agent $$i$$:

$$x_i^{(k+1)} = \arg\min_{x_i} \left[ f_i(x_i) + \sum_j \nu_{ij}^{(k)}(x_i - \bar{x}_j^{(k)}) \right]$$

$$\nu_{ij}^{(k+1)} = \nu_{ij}^{(k)} + \rho(x_i^{(k+1)} - x_j^{(k+1)})$$

**c) Communication:**

Each agent only needs to communicate with its neighbors!

**Distributed consensus.**

</details>

---

## 💡 **Summary**

| Method | Key Idea | Convergence |
|--------|----------|-------------|
| Dual decomposition | Parallel subproblems | Sublinear |
| Augmented Lagrangian | Quadratic penalty | Linear |
| Dual gradient | First-order | $$O(1/k)$$ |
| Dual Newton | Second-order | Quadratic |

---

## 📚 **References**

1. Bertsekas, D. P. (1999). *Nonlinear Programming*. Athena Scientific.
2. Boyd, S., et al. (2011). "Distributed Optimization and Statistical Learning via ADMM".
