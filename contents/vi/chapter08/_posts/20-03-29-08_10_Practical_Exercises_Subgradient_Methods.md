---
layout: post
title: "08-10 Bài Tập Thực Hành - Phương pháp Subgradient"
chapter: "08"
order: 11
owner: "GitHub Copilot"
lang: vi
categories:
  - chapter08
lesson_type: required
---

# Bài Tập Thực Hành - Phương pháp Subgradient

Các bài tập được tham khảo từ Boyd et al. (2003) và Nesterov (2009).

---

## **Bài tập 1: Dual Subgradient cho LP**

Cho bài toán LP: $$\min c^Tx$$ s.t. $$Ax = b$$, $$x \geq 0$$ với $$c = (1,2)^T$$, $$A = [1,1]$$, $$b = 3$$.

**a)** Viết dual problem  
**b)** Tính subgradient  
**c)** Thực hiện dual subgradient iterations

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

**Dual:** $$\max -3\nu$$ s.t. $$\nu \leq 1$$

**Solution:** $$\nu^* = 1$$

Iterations với $$\alpha = 0.1$$ từ $$\nu^{(0)} = 0$$ hội tụ đến $$\nu^* = 1$$ sau 4 bước.

</details>

---

## **Bài tập 2: Stochastic Subgradient**

Cho $$\min \frac{1}{n}\sum_i \max(0, 1 - y_i w^T x_i)$$ với 3 điểm dữ liệu.

**a)** Viết stochastic update  
**b)** So sánh với batch method

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

Stochastic chọn ngẫu nhiên 1 sample mỗi iteration:

$$w^{(k+1)} = w^{(k)} - \alpha_k g_i$$

với $$g_i = -y_i x_i$$ nếu margin violated.

**Advantage:** Cheaper per-iteration, makes progress khi batch stalls.

</details>

---

## **Bài tập 3: Polyak-Ruppert Averaging**

Cho $$f(x) = \max\{2x, -x+3\}$$.

**a)** Tìm $$x^*$$  
**b)** So sánh $$x^{(k)}$$ vs averaged $$\bar{x}^{(k)}$$

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

**$$x^* = 1$$** (intersection point)

**Averaging:** $$\bar{x}^{(k)} = \frac{1}{k}\sum_{i=1}^k x^{(i)}$$

Smooths oscillations và converges faster đến $$x^*$$.

</details>

---

## **Bài tập 4: Mirror Descent trên Simplex**

Cho $$f(x) = c^Tx$$ trên simplex $$\Delta_3$$.

**a)** Sử dụng entropic mirror map $$\psi(x) = \sum x_i \log x_i$$  
**b)** Derive update rule

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

**Update:**

$$x_i^{(k+1)} \propto x_i^{(k)} e^{-\alpha c_i}$$

Normalize để $$\sum x_i = 1$$.

**Advantage:** Naturally handles simplex constraints, geometry-aware.

</details>

---

## **Bài tập 5: Cutting Plane Method**

Cho $$f(x) = \max\{x^2, (x-2)^2\}$$.

**a)** Build cutting planes $$\ell_k(x) = f(x^{(k)}) + g^{(k)}(x - x^{(k)})$$  
**b)** Minimize lower bound $$\hat{f}(x) = \max_k \ell_k(x)$$

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

Từ $$x^{(0)} = 0$$:

$$\ell_0(x) = 4 - 4x$$

Từ $$x^{(1)} = 1$$:

$$\ell_1(x) = 1 + 2(x-1) = 2x - 1$$

Minimize $$\max\{4-4x, 2x-1\}$$ → $$x^{(2)} = \frac{5}{6}$$

Iterate until gap closes.

</details>

---

## **Tổng kết**

| Method | Convergence | Best for |
|--------|-------------|----------|
| Dual Subgradient | $$O(1/\sqrt{k})$$ | LP, convex programs |
| Stochastic | $$O(1/\sqrt{k})$$ | Large-scale ML |
| Averaged | $$O(1/\sqrt{k})$$ | Reduce oscillations |
| Mirror Descent | $$O(1/\sqrt{k})$$ | Constrained domains |
| Bundle/Cutting | $$O(1/k)$$ | Non-smooth, few vars |

---

## **Tài liệu Tham khảo**

1. Boyd, S., et al. (2003). "Subgradient Methods". Stanford.
2. Nesterov, Y. (2009). "Primal-dual subgradient methods".
3. Beck, A., & Teboulle, M. (2003). "Mirror descent".
