---
layout: post
title: 'Practical Exercises - Subgradient Methods'
chapter: "08"
order: 11
owner: "GitHub Copilot"
lang: en
categories:
  - chapter08
lesson_type: required
---

# Practical Exercises - Subgradient Methods

The exercises are adapted from Boyd et al. (2003) and Nesterov (2009).

---

## **Exercise 1: Dual Subgradient for an LP**

Given the LP: $$\min c^Tx$$ s.t. $$Ax = b$$, $$x \geq 0$$ with $$c = (1,2)^T$$, $$A = [1,1]$$, $$b = 3$$.

**a)** Write the dual problem  
**b)** Compute a subgradient  
**c)** Carry out dual subgradient iterations

<details markdown="1">
<summary><strong>Solution</strong></summary>

**Lagrangian:** $$L(x,\nu) = c^Tx + \nu(b - Ax)$$, so $$g(\nu) = 3\nu + \inf_{x \geq 0}(c - A^T\nu)^Tx$$, which is finite when $$A^T\nu \leq c$$.

**Dual:** $$\max 3\nu$$ s.t. $$\nu \leq 1$$

**Subgradient:** $$g'(\nu) = b - Ax^*(\nu) = 3$$ (with $$x^*=0$$ when $$\nu \le 1$$)

**Solution:** $$\nu^* = 1$$ (the dual value $$3$$ equals the primal value at $$x = (3, 0)$$)

Projected gradient ascent onto $$\nu \leq 1$$ with $$\alpha = 0.1$$ from $$\nu^{(0)} = 0$$ gives $$0.3, 0.6, 0.9, 1$$, converging to $$\nu^* = 1$$ after 4 steps.

</details>

---

## **Exercise 2: Stochastic Subgradient**

Given $$\min \frac{1}{n}\sum_i \max(0, 1 - y_i w^T x_i)$$ with 3 data points.

**a)** Write the stochastic update  
**b)** Compare with the batch method

<details markdown="1">
<summary><strong>Solution</strong></summary>

The stochastic method picks one random sample per iteration:

$$w^{(k+1)} = w^{(k)} - \alpha_k g_i$$

with $$g_i = -y_i x_i$$ if the margin is violated (and $$g_i = 0$$ otherwise).

**Advantage:** cheaper per iteration, and it keeps making progress when the batch method stalls.

</details>

---

## **Exercise 3: Polyak-Ruppert Averaging**

Given $$f(x) = \max\{2x, -x+3\}$$.

**a)** Find $$x^*$$  
**b)** Compare $$x^{(k)}$$ with the averaged iterate $$\bar{x}^{(k)}$$

<details markdown="1">
<summary><strong>Solution</strong></summary>

**$$x^* = 1$$** (the intersection point)

**Averaging:** $$\bar{x}^{(k)} = \frac{1}{k}\sum_{i=1}^k x^{(i)}$$

It smooths out oscillations and converges faster to $$x^*$$.

</details>

---

## **Exercise 4: Mirror Descent on the Simplex**

Given $$f(x) = c^Tx$$ on the simplex $$\Delta_3$$.

**a)** Use the entropic mirror map $$\psi(x) = \sum x_i \log x_i$$  
**b)** Derive the update rule

<details markdown="1">
<summary><strong>Solution</strong></summary>

**Update:**

$$x_i^{(k+1)} \propto x_i^{(k)} e^{-\alpha c_i}$$

Normalize so that $$\sum x_i = 1$$.

**Advantage:** handles the simplex constraint naturally and is geometry-aware.

</details>

---

## **Exercise 5: Cutting Plane Method**

Given $$f(x) = \max\{x^2, (x-2)^2\}$$.

**a)** Build cutting planes $$\ell_k(x) = f(x^{(k)}) + g^{(k)}(x - x^{(k)})$$  
**b)** Minimize the lower bound $$\hat{f}(x) = \max_k \ell_k(x)$$

<details markdown="1">
<summary><strong>Solution</strong></summary>

From $$x^{(0)} = 0$$:

$$\ell_0(x) = 4 - 4x$$

From $$x^{(1)} = 1$$:

$$\ell_1(x) = 1 + 2(x-1) = 2x - 1$$

Minimize $$\max\{4-4x, 2x-1\}$$ → $$x^{(2)} = \frac{5}{6}$$

Iterate until the gap closes.

</details>

---

## **Summary**

| Method | Convergence | Best for |
|--------|-------------|----------|
| Dual Subgradient | $$O(1/\sqrt{k})$$ | LP, convex programs |
| Stochastic | $$O(1/\sqrt{k})$$ | Large-scale ML |
| Averaged | $$O(1/\sqrt{k})$$ | Reducing oscillations |
| Mirror Descent | $$O(1/\sqrt{k})$$ | Constrained domains |
| Bundle/Cutting | $$O(1/k)$$ | Non-smooth, few variables |

---

## **References**

1. Boyd, S., et al. (2003). "Subgradient Methods". Stanford.
2. Nesterov, Y. (2009). "Primal-dual subgradient methods".
3. Beck, A., & Teboulle, M. (2003). "Mirror descent".
