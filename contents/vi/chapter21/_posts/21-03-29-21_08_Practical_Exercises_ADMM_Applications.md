---
layout: post
title: 21-08 Bài Tập Thực Hành - ADMM Applications
chapter: '21'
order: 9
owner: GitHub Copilot
lang: vi
categories:
- chapter21
lesson_type: required
redirect_from:
  - /contents/vi/chapter21/21_07_Practical_Exercises_ADMM_Applications/
---

# Bài Tập Thực Hành - ADMM Applications

Các bài tập được tham khảo từ Boyd et al. (2011).

---

## 📝 **Bài tập 1: ADMM Basics**

$$\min f(x) + g(z)$$ s.t. $$Ax + Bz = c$$.

**Yêu cầu:**  
a) Viết scaled ADMM  
b) Apply to LASSO: $$\min \frac{1}{2}\|Ax - b\|^2 + \lambda\|x\|_1$$  
c) Iterate với toy example

<details>
<summary><strong>💡 Lời giải</strong></summary>

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

## 📝 **Bài tập 2: Consensus ADMM**

$$N$$ functions: $$\min \sum_{i=1}^N f_i(x)$$.

**Yêu cầu:**  
a) Reformulate với consensus $$x_i$$  
b) Global variable update  
c) Distributed implementation

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Consensus form:**

$$\min \sum_i f_i(x_i)$$ s.t. $$x_i = z \, \forall i$$

**b) ADMM:**

$$x_i^{(k+1)} = \arg\min_{x_i} \left[ f_i(x_i) + \frac{\rho}{2}\|x_i - z^{(k)} + u_i^{(k)}\|^2 \right]$$

$$z^{(k+1)} = \frac{1}{N}\sum_i (x_i^{(k+1)} + u_i^{(k)})$$

$$u_i^{(k+1)} = u_i^{(k)} + x_i^{(k+1)} - z^{(k+1)}$$

**c) Distributed:** Each node updates $$x_i$$, then average for $$z$$.

</details>

---

## 📝 **Bài tập 3: Total Variation Denoising**

$$\min \frac{1}{2}\|x - b\|^2 + \lambda \|Dx\|_1$$

với $$D$$ là difference operator.

**Yêu cầu:**  
a) ADMM formulation  
b) $$x$$-update (smooth)  
c) $$z$$-update (soft-thresholding)

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Split:** $$z = Dx$$

$$\min_x \frac{1}{2}\|x - b\|^2 + \lambda\|z\|_1$$ s.t. $$Dx - z = 0$$

**b) $$x$$-update:**

$$x^{(k+1)} = (I + \rho D^TD)^{-1}(b + \rho D^T(z^{(k)} - u^{(k)}))$$

(Solve linear system, often banded/fast)

**c) $$z$$-update:**

$$z^{(k+1)} = S_{\lambda/\rho}(Dx^{(k+1)} + u^{(k)})$$

</details>

---

## 📝 **Bài tập 4: Matrix Decomposition**

$$\min \|L\|_* + \lambda\|S\|_1$$ s.t. $$L + S = M$$.

**Yêu cầu:**  
a) $$L$$-update (SVD thresholding)  
b) $$S$$-update (soft-thresholding)  
c) Application: robust PCA

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) $$L$$-update:**

$$L^{(k+1)} = \arg\min_L \left[ \|L\|_* + \frac{\rho}{2}\|L + S^{(k)} - M + U^{(k)}\|_F^2 \right]$$

$$= \mathcal{S}_{1/\rho}(M - S^{(k)} - U^{(k)})$$

với $$\mathcal{S}_\tau(X) = U \text{diag}(\max(\sigma_i - \tau, 0)) V^T$$

**b) $$S$$-update:**

$$S^{(k+1)} = S_{\lambda/\rho}(M - L^{(k+1)} - U^{(k)})$$

**c) Robust PCA:** $$M = L + S$$ (low-rank + sparse)

</details>

---

## 📝 **Bài tập 5: Convergence và Parameter Tuning**

**Yêu cầu:**  
a) Chọn $$\rho$$  
b) Stopping criteria  
c) Adaptive $$\rho$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Choosing $$\rho$$:**

**Rule of thumb:** $$\rho \sim 1.0$$ for normalized data

**Balance:** primal vs dual residuals

**b) Stopping:**

$$\epsilon_{\text{pri}} = \sqrt{n}\epsilon_{\text{abs}} + \epsilon_{\text{rel}}\max(\|Ax\|, \|Bz\|, \|c\|)$$

$$\epsilon_{\text{dual}} = \sqrt{n}\epsilon_{\text{abs}} + \epsilon_{\text{rel}}\|A^T\nu\|$$

Stop khi $$\|r\| < \epsilon_{\text{pri}}$$ và $$\|s\| < \epsilon_{\text{dual}}$$

**c) Adaptive:**

```
if ||r|| > μ ||s||:
    ρ = τ_incr * ρ
elif ||s|| > μ ||r||:
    ρ = ρ / τ_decr
```

với $$\mu = 10$$, $$\tau = 2$$.

</details>

---

## 💡 **Tổng kết**

**ADMM Applications:**

| Problem | $$f(x)$$ | $$g(z)$$ | Use case |
|---------|----------|----------|----------|
| LASSO | $$\frac{1}{2}\|Ax-b\|^2$$ | $$\lambda\|z\|_1$$ | Sparse regression |
| Total variation | $$\frac{1}{2}\|x-b\|^2$$ | $$\lambda\|z\|_1$$ | Image denoising |
| Robust PCA | $$\|L\|_*$$ | $$\lambda\|S\|_1$$ | Outlier removal |
| Consensus | $$\sum f_i(x_i)$$ | $$0$$ | Distributed |

---

## 📚 **Tài liệu Tham khảo**

1. Boyd, S., et al. (2011). "Distributed Optimization via ADMM". *Foundations and Trends*.

