---
layout: post
title: '21-08 Practical Exercises - ADMM Applications'
chapter: '21'
order: 9
owner: GitHub Copilot
lang: en
categories:
- chapter21
lesson_type: required
redirect_from:
  - /contents/en/chapter21/21_07_Practical_Exercises_ADMM_Applications/
---

The best way to internalize ADMM is to derive a splitting from scratch, check every matrix dimension, and run 3–5 iterations by hand (and in Python) until you watch the primal residual $$r^k$$ and dual residual $$s^k$$ collapse together. Before diving into the Boyd et al. exercises below, work through this compact 1D Lasso warm-up so you can verify the exact interplay between the ridge $$\beta$$-update, the soft-thresholding $$\alpha$$-update, and the scaled dual accumulator $$w$$.

## Background Knowledge Map: Core ADMM Skills Tested in These Exercises

- **Scaled ADMM Formulation:** Translate any structured problem (Lasso, total variation, constrained QP, consensus) into $$\min f(x) + g(z) \text{ s.t. } Ax + Bz = c$$ and write the three scaled updates cleanly.
- **Closed-Form Proximal & Linear Oracles:** Recognize when the $$x$$-step is a cacheable Cholesky solve $$(A^T A + \rho I)^{-1}$$ and when the $$z$$-step is soft-thresholding, block shrinkage, singular-value thresholding, or Euclidean projection.
- **Residual-Based Stopping & Adaptive $$\rho$$:** Compute $$r^k = Ax^k + Bz^k - c$$ and $$s^k = \rho A^T B(z^k - z^{k-1})$$, and apply Boyd's residual-balancing rule (doubling/halving $$\rho$$ when $$\|r^k\|_2$$ and $$\|s^k\|_2$$ differ by a factor of 10).
- **Splitting Design Intuition:** Compare alternative auxiliary variable choices to ensure every subproblem is cheap and well-conditioned.

### Step-by-Step Worked Example (Read Slowly): Hand-Tracing Two Scaled ADMM Steps on 1D Lasso

Solve $$\min_x \frac{1}{2}(x - 3)^2 + |x|$$ (exact optimum $$x^\star = S_1(3) = 2$$) via the Lasso split $$\min \frac{1}{2}(x - 3)^2 + |z|$$ s.t. $$x - z = 0$$ with $$\rho = 1$$, starting from $$z^0 = 0, \; w^0 = 0$$.

1. **Write the three scaled updates:**
   - $$x^k = \frac{3 + (z^{k-1} - w^{k-1})}{2}$$,
   - $$z^k = S_1(x^k + w^{k-1})$$,
   - $$w^k = w^{k-1} + x^k - z^k$$.
2. **Iteration 1 ($$z^0 = 0, w^0 = 0$$):**
   - $$x^1 = \frac{3 + 0}{2} = 1.5$$.
   - $$z^1 = S_1(1.5 + 0) = 0.5$$.
   - $$w^1 = 0 + (1.5 - 0.5) = 1.0$$. (Primal residual $$r^1 = 1.0$$, dual residual $$s^1 = 0.5$$.)
3. **Iteration 2 ($$z^1 = 0.5, w^1 = 1.0$$):**
   - $$x^2 = \frac{3 + (0.5 - 1.0)}{2} = 1.25$$.
   - $$z^2 = S_1(1.25 + 1.0) = S_1(2.25) = 1.25$$!
   - $$w^2 = 1.0 + (1.25 - 1.25) = 1.0$$. (Notice $$r^2 = 0$$, and $$w^2 = 1.0 = w^\star$$!)
4. **Verify Iteration 3:**
   $$x^3 = \frac{3 + (1.25 - 1.0)}{2} = 1.625$$, $$z^3 = S_1(2.625) = 1.625$$, $$w^3 = 1.0$$—sliding straight along the feasible line $$x = z$$ directly into $$x^\star = z^\star = 2.0$$! Now try the full exercises below.

# Practical Exercises - ADMM Applications

The exercises are adapted from Boyd et al. (2011).

---

## 📝 **Exercise 1: ADMM Basics**

$$\min f(x) + g(z)$$ s.t. $$Ax + Bz = c$$.

**Tasks:**  
a) Write the scaled ADMM  
b) Apply it to LASSO: $$\min \frac{1}{2}\|Ax - b\|^2 + \lambda\|x\|_1$$  
c) Iterate on a toy example

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Scaled ADMM:**

$$x^{(k+1)} = \arg\min_x \left[ f(x) + \frac{\rho}{2}\|Ax + Bz^{(k)} - c + u^{(k)}\|^2 \right]$$

$$z^{(k+1)} = \arg\min_z \left[ g(z) + \frac{\rho}{2}\|Ax^{(k+1)} + Bz - c + u^{(k)}\|^2 \right]$$

$$u^{(k+1)} = u^{(k)} + Ax^{(k+1)} + Bz^{(k+1)} - c$$

**b) LASSO:** $$x - z = 0$$

$$x^{(k+1)} = (A^TA + \rho I)^{-1}(A^Tb + \rho(z^{(k)} - u^{(k)}))$$

$$z^{(k+1)} = S_{\lambda/\rho}(x^{(k+1)} + u^{(k)})$$

$$u^{(k+1)} = u^{(k)} + x^{(k+1)} - z^{(k+1)}$$

</details>

---

## 📝 **Exercise 2: Consensus ADMM**

$$N$$ functions: $$\min \sum_{i=1}^N f_i(x)$$.

**Tasks:**  
a) Reformulate with consensus variables $$x_i$$  
b) Global variable update  
c) Distributed implementation

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Consensus form:**

$$\min \sum_i f_i(x_i)$$ s.t. $$x_i = z \, \forall i$$

**b) ADMM:**

$$x_i^{(k+1)} = \arg\min_{x_i} \left[ f_i(x_i) + \frac{\rho}{2}\|x_i - z^{(k)} + u_i^{(k)}\|^2 \right]$$

$$z^{(k+1)} = \frac{1}{N}\sum_i (x_i^{(k+1)} + u_i^{(k)})$$

$$u_i^{(k+1)} = u_i^{(k)} + x_i^{(k+1)} - z^{(k+1)}$$

**c) Distributed:** each node updates $$x_i$$, then the results are averaged to get $$z$$.

</details>

---

## 📝 **Exercise 3: Total Variation Denoising**

$$\min \frac{1}{2}\|x - b\|^2 + \lambda \|Dx\|_1$$

where $$D$$ is the difference operator.

**Tasks:**  
a) ADMM formulation  
b) $$x$$-update (smooth)  
c) $$z$$-update (soft-thresholding)

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Split:** $$z = Dx$$

$$\min_x \frac{1}{2}\|x - b\|^2 + \lambda\|z\|_1$$ s.t. $$Dx - z = 0$$

**b) $$x$$-update:**

$$x^{(k+1)} = (I + \rho D^TD)^{-1}(b + \rho D^T(z^{(k)} - u^{(k)}))$$

(Solve a linear system, often banded and therefore fast)

**c) $$z$$-update:**

$$z^{(k+1)} = S_{\lambda/\rho}(Dx^{(k+1)} + u^{(k)})$$

</details>

---

## 📝 **Exercise 4: Matrix Decomposition**

$$\min \|L\|_* + \lambda\|S\|_1$$ s.t. $$L + S = M$$.

**Tasks:**  
a) $$L$$-update (SVD thresholding)  
b) $$S$$-update (soft-thresholding)  
c) Application: robust PCA

<details>
<summary><strong>💡 Solution</strong></summary>

**a) $$L$$-update:**

$$L^{(k+1)} = \arg\min_L \left[ \|L\|_* + \frac{\rho}{2}\|L + S^{(k)} - M + U^{(k)}\|_F^2 \right]$$

$$= \mathcal{S}_{1/\rho}(M - S^{(k)} - U^{(k)})$$

where $$\mathcal{S}_\tau(X) = U \text{diag}(\max(\sigma_i - \tau, 0)) V^T$$

**b) $$S$$-update:**

$$S^{(k+1)} = S_{\lambda/\rho}(M - L^{(k+1)} - U^{(k)})$$

**c) Robust PCA:** $$M = L + S$$ (low-rank + sparse)

</details>

---

## 📝 **Exercise 5: Convergence and Parameter Tuning**

**Tasks:**  
a) Choose $$\rho$$  
b) Stopping criteria  
c) Adaptive $$\rho$$

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Choosing $$\rho$$:**

**Rule of thumb:** $$\rho \sim 1.0$$ for normalized data

**Balance:** primal vs dual residuals

**b) Stopping:**

$$\epsilon_{\text{pri}} = \sqrt{n}\epsilon_{\text{abs}} + \epsilon_{\text{rel}}\max(\|Ax\|, \|Bz\|, \|c\|)$$

$$\epsilon_{\text{dual}} = \sqrt{n}\epsilon_{\text{abs}} + \epsilon_{\text{rel}}\|A^T\nu\|$$

Stop when $$\|r\| < \epsilon_{\text{pri}}$$ and $$\|s\| < \epsilon_{\text{dual}}$$

**c) Adaptive:**

```
if ||r|| > μ ||s||:
    ρ = τ_incr * ρ
elif ||s|| > μ ||r||:
    ρ = ρ / τ_decr
```

with $$\mu = 10$$, $$\tau = 2$$.

</details>

---

## 💡 **Summary**

**ADMM Applications:**

| Problem | $$f(x)$$ | $$g(z)$$ | Use case |
|---------|----------|----------|----------|
| LASSO | $$\frac{1}{2}\|Ax-b\|^2$$ | $$\lambda\|z\|_1$$ | Sparse regression |
| Total variation | $$\frac{1}{2}\|x-b\|^2$$ | $$\lambda\|z\|_1$$ | Image denoising |
| Robust PCA | $$\|L\|_*$$ | $$\lambda\|S\|_1$$ | Outlier removal |
| Consensus | $$\sum f_i(x_i)$$ | $$0$$ | Distributed |

---

## 📚 **References**

1. Boyd, S., et al. (2011). "Distributed Optimization via ADMM". *Foundations and Trends*.
