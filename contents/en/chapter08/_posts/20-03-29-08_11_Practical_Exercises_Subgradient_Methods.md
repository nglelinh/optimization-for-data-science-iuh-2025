---
layout: post
title: '08-11 Practical Exercises - Subgradient Methods'
chapter: "08"
order: 19
owner: "GitHub Copilot"
lang: en
categories:
  - chapter08
lesson_type: required
redirect_from:
  - /contents/en/chapter08/08_10_Practical_Exercises_Subgradient_Methods/
---

Reading convergence proofs is only half of learning nonsmooth optimization; the real intuition clicks when you compute a dual subgradient by hand, watch Polyak–Ruppert averaging smooth out stochastic noise, or see mirror descent adapt to the geometry of a probability simplex. These practical exercises bridge textbook theory and real solver design, taking you from basic dual subgradient steps on a linear program all the way to mirror descent and cutting-plane methods.

## Key ideas: Advanced Subgradient Variants in Practice

- **Pillar 1 — Dual Subgradient Ascent:** Maximizing a concave Lagrange dual $$q(\lambda) = \inf_x (c^\top x + \lambda^\top(Ax - b))$$ is equivalent to minimizing $$-q(\lambda)$$. By Danskin's theorem, the constraint residual $$Ax(\lambda) - b$$ is a subgradient of $$q(\lambda)$$, turning dual ascent into a price-adjustment mechanism.
- **Pillar 2 — Polyak–Ruppert Iterate Averaging:** Instead of returning the noisy final iterate $$x^{(k)}$$ or tracking only the single best point, averaging $$\bar{x}^{(k)} = \frac{1}{k}\sum_{i=1}^k x^{(i)}$$ exploits Jensen's inequality ($$f(\bar{x}^{(k)}) \le \frac{1}{k}\sum f(x^{(i)})$$) to stabilize stochastic trajectories and achieve optimal variance constants.
- **Pillar 3 — Mirror Descent & Non-Euclidean Geometry:** Replacing the Euclidean squared distance $$\frac{1}{2}\|x - y\|_2^2$$ with a Bregman divergence (such as KL divergence on the simplex) produces multiplicative-weights / exponentiated-gradient updates whose dimension dependence improves from $$O(\sqrt{n})$$ to $$O(\sqrt{\log n})$$.
- **Pillar 4 — Cutting-Plane & Localization Methods:** Rather than discarding past subgradients, cutting-plane methods accumulate linear underestimators $$f(y) \ge f(x^{(i)}) + g^{(i)\top}(y - x^{(i)})$$ into a polyhedral model that slices the feasible region in half, trading higher per-step cost for faster $$O(n \log(1/\varepsilon))$$ convergence in low-to-moderate dimensions.

### Worked example: Jensen's Inequality in Action for Polyak–Ruppert Averaging

Consider minimizing $$f(x) = |x|$$ ($$x^\star = 0, f^\star = 0$$) where a noisy subgradient loop oscillates around the origin through the four iterates $$x^{(1)} = 0.8,\; x^{(2)} = -0.6,\; x^{(3)} = 0.4,\; x^{(4)} = -0.2$$.

1. **Compute the individual objective values:**
   $$f(x^{(1)}) = 0.8, \quad f(x^{(2)}) = 0.6, \quad f(x^{(3)}) = 0.4, \quad f(x^{(4)}) = 0.2.$$
   The average of the objective values is $$\frac{0.8 + 0.6 + 0.4 + 0.2}{4} = 0.50$$, and the best single iterate has $$f_{\text{best}}^{(4)} = 0.20$$.
2. **Compute the Polyak–Ruppert averaged iterate $$\bar{x}^{(4)}$$:**
   $$\bar{x}^{(4)} = \frac{0.8 + (-0.6) + 0.4 + (-0.2)}{4} = \frac{0.4}{4} = 0.10.$$
3. **Evaluate $$f(\bar{x}^{(4)})$$ and compare:**
   $$f(\bar{x}^{(4)}) = |0.10| = 0.10 < 0.20 = f_{\text{best}}^{(4)} < 0.50 = \frac{1}{4}\sum_{i=1}^4 f(x^{(i)}).$$
4. **Why it works:** Opposite-sign oscillations cancel out when you average the *iterates* before evaluating $$f$$, making $$\bar{x}^{(4)}$$ twice as accurate as even the best single point visited! Keep this exact cancellation mechanism in mind as you work through Exercises 1–5 below.

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
