---
layout: post
title: 20-6 Bài Tập Thực Hành - Dual Methods
chapter: '20'
order: 7
owner: GitHub Copilot
lang: vi
categories:
- chapter20
lesson_type: required
---

# Bài Tập Thực Hành - Dual Methods

Các bài tập được tham khảo từ Bertsekas (1999) và Boyd et al. (2011).

---

## 📝 **Bài tập 1: Dual Decomposition**

Minimize $$\sum_{i=1}^N f_i(x_i)$$ s.t. $$\sum x_i = c$$.

**Yêu cầu:**  
a) Viết Lagrangian và dual  
b) Decompose thành $$N$$ independent subproblems  
c) Update dual variable $$\nu$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Lagrangian:**

$$L(x, \nu) = \sum_i f_i(x_i) + \nu\left(\sum x_i - c\right)$$

$$= \sum_i [f_i(x_i) + \nu x_i] - \nu c$$

**Dual:**

$$g(\nu) = \sum_i \min_{x_i} [f_i(x_i) + \nu x_i] - \nu c$$

**Decomposition:** Solve $$N$$ problems in parallel!

**Dual update:** $$\nu^{(k+1)} = \nu^{(k)} + \alpha(\sum x_i^{(k)} - c)$$

</details>

---

## 📝 **Bài tập 2: Augmented Lagrangian**

$$\min f(x)$$ s.t. $$Ax = b$$.

**Yêu cầu:**  
a) Viết augmented Lagrangian $$L_\rho(x, \nu)$$  
b) So sánh với standard Lagrangian  
c) Derive dual ascent with quadratic penalty

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Augmented Lagrangian:**

$$L_\rho(x, \nu) = f(x) + \nu^T(Ax - b) + \frac{\rho}{2}\|Ax - b\|^2$$

**b) Advantage:**

**Standard:** $$g(\nu)$$ có thể non-differentiable

**Augmented:** Smoother dual, better conditioning

**c) ALM iterations:**

1. $$x^{(k+1)} = \arg\min_x L_\rho(x, \nu^{(k)})$$
2. $$\nu^{(k+1)} = \nu^{(k)} + \rho(Ax^{(k+1)} - b)$$

</details>

---

## 📝 **Bài tập 3: Method of Multipliers**

Apply ALM đến $$\min x_1^2 + x_2^2$$ s.t. $$x_1 + x_2 = 1$$.

**Yêu cầu:**  
a) Setup ALM  
b) Iterate từ $$\nu^{(0)} = 0$$, $$\rho = 1$$  
c) Compare với dual gradient

<details>
<summary><strong>💡 Lời giải</strong></summary>

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

## 📝 **Bài tập 4: Dual Gradient vs Dual Newton**

Maximize $$g(\nu)$$ bằng gradient ascent và Newton.

**Yêu cầu:**  
a) Gradient: $$\nu^{(k+1)} = \nu^{(k)} + \alpha \nabla g(\nu^{(k)})$$  
b) Newton: $$\nu^{(k+1)} = \nu^{(k)} - (\nabla^2 g)^{-1} \nabla g$$  
c) Compare convergence

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Dual gradient:**

$$\nabla g(\nu) = Ax^*(\nu) - b$$

$$\nu^{(k+1)} = \nu^{(k)} + \alpha(Ax^{(k)} - b)$$

**Linear convergence** (như subgradient nếu $$g$$ non-smooth)

**b) Dual Newton:**

$$\nabla^2 g(\nu) = A \frac{\partial x^*}{\partial \nu} A^T$$

**Quadratic convergence** nếu $$g$$ smooth and strongly concave.

**c) Tradeoff:**

- **Gradient:** Cheap per iteration
- **Newton:** Expensive (Hessian), fast convergence

</details>

---

## 📝 **Bài tập 5: Consensus Optimization**

$$N$$ agents minimize $$\sum f_i(x_i)$$ s.t. $$x_1 = x_2 = \cdots = x_N$$.

**Yêu cầu:**  
a) Dual decomposition  
b) Average consensus update  
c) Distributed implementation

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Lagrangian:**

$$L(x, \nu) = \sum_i f_i(x_i) + \sum_{i<j} \nu_{ij}(x_i - x_j)$$

**Dual:**

$$g(\nu) = \sum_i \min_{x_i} \left[ f_i(x_i) + \sum_j \nu_{ij}(x_i - x_j) \right]$$

**b) Update:**

Each agent $$i$$:

$$x_i^{(k+1)} = \arg\min_{x_i} \left[ f_i(x_i) + \sum_j \nu_{ij}^{(k)}(x_i - \bar{x}_j^{(k)}) \right]$$

$$\nu_{ij}^{(k+1)} = \nu_{ij}^{(k)} + \rho(x_i^{(k+1)} - x_j^{(k+1)})$$

**c) Communication:**

Each agent chỉ cần communicate với neighbors!

**Distributed consensus.**

</details>

---

## 💡 **Tổng kết**

| Method | Key Idea | Convergence |
|--------|----------|-------------|
| Dual decomposition | Parallel subproblems | Sublinear |
| Augmented Lagrangian | Quadratic penalty | Linear |
| Dual gradient | First-order | $$O(1/k)$$ |
| Dual Newton | Second-order | Quadratic |

---

## 📚 **Tài liệu Tham khảo**

1. Bertsekas, D. P. (1999). *Nonlinear Programming*. Athena Scientific.
2. Boyd, S., et al. (2011). "Distributed Optimization and Statistical Learning via ADMM".

