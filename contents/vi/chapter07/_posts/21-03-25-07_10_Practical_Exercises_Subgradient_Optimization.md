---
layout: post
title: 07-9 Bài Tập Thực Hành - Tối ưu Subgradient
chapter: '07'
order: 10
owner: GitHub Copilot
lang: vi
categories:
- chapter07
lesson_type: required
---

# Bài Tập Thực Hành - Tối ưu Subgradient (Subgradient Optimization)

Các bài tập được tham khảo từ Boyd & Vandenberghe (2004) và Shor (1985).

---

## 📝 **Phần I: Tính Subgradient**

### **Bài tập 1: Subgradient của Hàm Không Khả Vi**

Tính subgradient của các hàm sau tại điểm cho trước:

**a)** $$f(x) = |x|$$ tại $$x = 0$$

**b)** $$f(x) = \max\{x_1, x_2\}$$ tại $$x = (1, 1)^T$$

**c)** $$f(x) = \|x\|_1$$ tại $$x = (0, 0)^T$$

**d)** $$f(x) = \max\{x_1 + x_2, 2x_1 - x_2\}$$ tại $$x = (1, 0)^T$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) $$f(x) = |x|$$ tại $$x = 0$$:**

**Định nghĩa:** $$g \in \partial f(0)$$ nếu 

$$f(y) \geq f(0) + g(y - 0)$$ $$\forall y$$

$$|y| \geq 0 + gy \quad \forall y$$

- Với $$y > 0$$: $$y \geq gy$$ → $$g \leq 1$$
- Với $$y < 0$$: $$-y \geq gy$$ → $$g \geq -1$$

$$\partial f(0) = [-1, 1]$$

**Giải thích hình học:** Tập hợp tất cả slopes của các đường thẳng support tại $$x = 0$$.

---

**b) $$f(x) = \max\{x_1, x_2\}$$ tại $$x = (1, 1)$$:**

$$f(1, 1) = 1$$ (cả hai active)

**Active set:** $$I = \{1, 2\}$$

$$\partial f(x) = \text{conv}\{\nabla f_i(x) : i \in I\}$$

$$= \text{conv}\{(1, 0), (0, 1)\}$$

$$= \{(\lambda, 1-\lambda) : 0 \leq \lambda \leq 1\}$$

**Hình học:** Đoạn thẳng nối $$(1, 0)$$ và $$(0, 1)$$.

---

**c) $$f(x) = \|x\|_1 = |x_1| + |x_2|$$ tại $$x = (0, 0)$$:**

$$\partial f(0) = \partial |x_1| \times \partial |x_2|$$

$$= [-1, 1] \times [-1, 1]$$

$$= \{(g_1, g_2) : |g_1| \leq 1, |g_2| \leq 1\}$$

**Hình học:** Hình vuông $$[-1, 1]^2$$.

---

**d) $$f(x) = \max\{x_1 + x_2, 2x_1 - x_2\}$$ tại $$x = (1, 0)$$:**

$$f_1(1, 0) = 1 + 0 = 1$$

$$f_2(1, 0) = 2 - 0 = 2$$

$$\Rightarrow f(1, 0) = 2$$ (chỉ $$f_2$$ active)

$$\nabla f_2 = (2, -1)$$

$$\partial f(1, 0) = \{(2, -1)\}$$ (singleton vì chỉ 1 active)

</details>

---

## 📝 **Phần II: Subgradient Method**

### **Bài tập 2: Convergence Analysis**

Cho $$f(x) = |x - 2| + |x + 1|$$.

**Yêu cầu:**  
a) Tìm $$x^*$$ (minimizer)  
b) Với step size $$\alpha_k = \frac{1}{\sqrt{k}}$$, iterate từ $$x^{(0)} = 5$$  
c) Tính $$x^{(1)}, x^{(2)}, x^{(3)}$$  
d) Ước tính convergence rate

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Tìm $$x^*$$:**

$$f(x) = |x - 2| + |x + 1|$$

**Case analysis:**
- $$x < -1$$: $$f(x) = -(x-2) - (x+1) = -2x + 1$$ (giảm)
- $$-1 \leq x \leq 2$$: $$f(x) = -(x-2) + (x+1) = 3$$ (constant!)
- $$x > 2$$: $$f(x) = (x-2) + (x+1) = 2x - 1$$ (tăng)

$$f^* = 3$$, $$x^* \in [-1, 2]$$

---

**b) Subgradient method:**

$$x^{(k+1)} = x^{(k)} - \alpha_k g^{(k)}$$

với $$g^{(k)} \in \partial f(x^{(k)})$$.

---

**c) Iterations:**

$$x^{(0)} = 5 > 2$$

$$\partial f(5) = \{\text{sign}(5-2)\} + \{\text{sign}(5+1)\} = \{1\} + \{1\} = \{2\}$$

$$g^{(0)} = 2$$

$$\alpha_0 = \frac{1}{\sqrt{1}} = 1$$

$$x^{(1)} = 5 - 1 \cdot 2 = 3$$

---

$$x^{(1)} = 3 > 2$$

$$g^{(1)} = 2$$

$$\alpha_1 = \frac{1}{\sqrt{2}} \approx 0.707$$

$$x^{(2)} = 3 - 0.707 \cdot 2 = 1.586$$

---

$$x^{(2)} = 1.586 \in [-1, 2]$$ (optimal region!)

$$\partial f(1.586) = \{\text{sign}(1.586 - 2) + \text{sign}(1.586 + 1)\} = \{-1 + 1\} = \{0\}$$ (trong khoảng $$(-1, 2)$$, $$f$$ là hằng số nên khả vi với gradient 0)

$$g^{(2)} = 0 \Rightarrow x^{(3)} = x^{(2)} = 1.586$$ (đã hội tụ đến tập nghiệm tối ưu)

---

**d) Convergence rate:**

With $$\alpha_k = \frac{1}{\sqrt{k}}$$:

$$f(x_{\text{best}}^{(k)}) - f^* \leq \frac{R^2 + G^2 \sum_{i=1}^k \alpha_i^2}{2\sum_{i=1}^k \alpha_i}$$

$$\sum_{i=1}^k \frac{1}{\sqrt{i}} \approx 2\sqrt{k}$$

$$\sum_{i=1}^k \frac{1}{i} \approx \log k$$

$$\Rightarrow O\left(\frac{\log k}{\sqrt{k}}\right) = O\left(\frac{1}{\sqrt{k}}\right)$$

**Sublinear convergence** (slower than gradient descent!)

</details>

---

## 📝 **Phần III: Step Size Rules**

### **Bài tập 3: So sánh Step Size Strategies**

Cho $$f(x) = \max\{x_1, x_2, -x_1 - x_2 + 1\}$$.

**Yêu cầu:**  
a) Tìm $$x^*$$ graphically  
b) Compare 3 step size rules:
   - Constant: $$\alpha_k = 0.1$$
   - Diminishing: $$\alpha_k = \frac{1}{k}$$
   - Square summable: $$\alpha_k = \frac{1}{k^{0.6}}$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Graphical solution:**

$$f(x) = \max\{x_1, x_2, 1 - x_1 - x_2\}$$

**Intersection points:**
- $$x_1 = x_2$$: Line $$x_1 = x_2$$
- $$x_1 = 1 - x_1 - x_2$$: $$2x_1 + x_2 = 1$$
- $$x_2 = 1 - x_1 - x_2$$: $$x_1 + 2x_2 = 1$$

Giải hệ $$x_1 = x_2$$ và $$2x_1 + x_2 = 1$$:

$$3x_1 = 1 \Rightarrow x_1 = \frac{1}{3}$$

$$x^* = \left(\frac{1}{3}, \frac{1}{3}\right)$$, $$f^* = \frac{1}{3}$$

---

**b) Step size comparison:**

**Từ $$x^{(0)} = (1, 1)$$:**

$$f_1 = 1$$, $$f_2 = 1$$, $$f_3 = -1$$ → max là $$f_1, f_2$$ (tie)

$$\partial f(1, 1) = \text{conv}\{(1, 0), (0, 1)\}$$

Chọn $$g = (0.5, 0.5)$$ (midpoint)

---

**Constant $$\alpha_k = 0.1$$:**

$$x^{(1)} = (1, 1) - 0.1(0.5, 0.5) = (0.95, 0.95)$$

$$x^{(2)} = (0.90, 0.90)$$

$$x^{(3)} = (0.85, 0.85)$$

...

**Hội tụ đến lân cận của $$x^*$$ (bán kính $$O(\alpha)$$), nhưng không đạt chính xác.**

---

**Diminishing $$\alpha_k = \frac{1}{k}$$:**

$$x^{(1)} = (1, 1) - 1 \cdot (0.5, 0.5) = (0.5, 0.5)$$

$$x^{(2)} = (0.5, 0.5) - 0.5 \cdot (0.5, 0.5) = (0.25, 0.25)$$ (với $$g^{(1)} = (0.5, 0.5)$$)

Tại $$(0.25, 0.25)$$: $$f_3 = 0.5$$ lớn nhất, $$g^{(2)} = (-1, -1)$$ nên $$x^{(3)} = (0.25, 0.25) + \frac{1}{3}(1, 1) \approx (0.583, 0.583)$$ (iterate dao động quanh $$x^*$$ và biên độ giảm dần).

...

**Hội tụ đến $$x^*$$, nhưng rất chậm (cận $$O(1/\log k)$$ vì $$\sum_{i \le k} 1/i \approx \log k$$).**

---

**Square summable $$\alpha_k = \frac{1}{k^{0.6}}$$:**

$$\sum \alpha_k = \sum \frac{1}{k^{0.6}} = \infty$$ ✓

$$\sum \alpha_k^2 = \sum \frac{1}{k^{1.2}} < \infty$$ ✓

**Hội tụ đến $$x^*$$ với cận $$O(1/k^{0.4})$$ (vì $$\sum_{i \le k} \alpha_i \sim k^{0.4}$$), nhanh hơn $$\alpha_k = 1/k$$ nhưng vẫn là hội tụ sublinear.**

</details>

---

## 📝 **Phần IV: Polyak Step Size**

### **Bài tập 4: Polyak's Step Size for $$\ell_1$$ Minimization**

$$\min_{x} \|x\|_1 \quad \text{s.t.} \quad Ax = b$$

với $$A = [1, 2, 3]$$, $$b = 6$$.

**Yêu cầu:**  
a) Viết Lagrangian  
b) Tìm dual function  
c) Maximize dual bằng subgradient với Polyak step size

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Lagrangian:**

$$L(x, \nu) = \|x\|_1 + \nu^T(Ax - b)$$

$$= \sum_i (|x_i| + \nu a_i x_i) - \nu b$$

---

**b) Dual function:**

$$g(\nu) = \inf_x L(x, \nu)$$

$$= \inf_x \sum_i (|x_i| + \nu a_i x_i) - \nu b$$

Minimize mỗi $$x_i$$ độc lập:

$$\inf_{x_i} (|x_i| + \nu a_i x_i) = \begin{cases}
0 & \text{if } |\nu a_i| \leq 1 \\
-\infty & \text{otherwise}
\end{cases}$$

$$g(\nu) = \begin{cases}
-\nu b & \text{if } |\nu a_i| \leq 1 \, \forall i \\
-\infty & \text{otherwise}
\end{cases}$$

Với $$A = [1, 2, 3]$$:

$$|\nu| \leq 1, \quad |2\nu| \leq 1, \quad |3\nu| \leq 1$$

$$\Rightarrow |\nu| \leq \frac{1}{3}$$

$$g(\nu) = -6\nu$$ for $$|\nu| \leq \frac{1}{3}$$

---

**c) Dual maximization:**

$$\max_{\nu} \quad -6\nu \quad \text{s.t.} \quad -\frac{1}{3} \leq \nu \leq \frac{1}{3}$$

**Obvious:** $$\nu^* = -\frac{1}{3}$$, $$g^* = 2$$

**Subgradient của $$g(\nu) = -6\nu$$:** $$s = -6$$ (với bài toán cực đại hóa hàm lõm $$g$$ ta dùng subgradient ascent).

**Polyak step size** (biết $$g^* = 2$$):

$$\alpha_k = \frac{g^* - g(\nu^{(k)})}{\|s^{(k)}\|^2}, \qquad \nu^{(k+1)} = \Pi_{[-1/3,\,1/3]}\left(\nu^{(k)} + \alpha_k s^{(k)}\right)$$

Từ $$\nu^{(0)} = 0$$: $$g(0) = 0$$

$$\alpha_0 = \frac{2 - 0}{36} = \frac{1}{18}$$

$$\nu^{(1)} = 0 + \frac{1}{18} \cdot (-6) = -\frac{1}{3}$$ ✓ (nằm trong miền xác định)

**Hội tụ trong 1 bước!** ($$g(-1/3) = 2 = g^*$$, và nghiệm gốc là $$x^* = (0, 0, 2)$$ với $$\|x^*\|_1 = 2$$.)

</details>

---

## 📝 **Phần V: Projected Subgradient**

### **Bài tập 5: Projected Subgradient for Constrained Optimization**

$$\min_{x} \|x - c\|_1 \quad \text{s.t.} \quad \|x\|_2 \leq R$$

với $$c = (2, 3)^T$$, $$R = 2$$.

**Yêu cầu:**  
a) Viết projected subgradient update  
b) Iterate từ $$x^{(0)} = (0, 0)$$  
c) Tìm nghiệm exact

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Projected subgradient:**

$$x^{(k+1)} = \Pi_C\left(x^{(k)} - \alpha_k g^{(k)}\right)$$

với $$C = \{x : \|x\|_2 \leq R\}$$, $$g^{(k)} \in \partial f(x^{(k)})$$.

**Projection onto $$\ell_2$$ ball:**

$$\Pi_C(y) = \begin{cases}
y & \text{if } \|y\| \leq R \\
R \frac{y}{\|y\|} & \text{if } \|y\| > R
\end{cases}$$

---

**b) Iterations:**

$$x^{(0)} = (0, 0)$$

$$\partial f(0, 0) = \partial \|(0, 0) - (2, 3)\|_1 = \partial(|{-2}| + |{-3}|)$$

Subgradient: $$g = \text{sign}(x - c) = (-1, -1)$$

Chọn $$\alpha_0 = 1$$:

$$\tilde{x}^{(1)} = (0, 0) - 1 \cdot (-1, -1) = (1, 1)$$

$$\|\tilde{x}^{(1)}\| = \sqrt{2} < 2$$ → no projection needed

$$x^{(1)} = (1, 1)$$

---

$$g^{(1)} = \text{sign}((1, 1) - (2, 3)) = (-1, -1)$$

$$\tilde{x}^{(2)} = (1, 1) + (1, 1) = (2, 2)$$

$$\|\tilde{x}^{(2)}\| = 2\sqrt{2} > 2$$ → project!

$$x^{(2)} = 2 \cdot \frac{(2, 2)}{2\sqrt{2}} = \frac{2}{\sqrt{2}}(1, 1) = (\sqrt{2}, \sqrt{2})$$

---

**c) Exact solution:**

Minimize $$\|x - c\|_1$$ over $$\|x\| \leq 2$$.

**Unconstrained optimum:** $$x = c = (2, 3)$$

$$\|c\| = \sqrt{13} > 2$$ → infeasible!

**Constrained optimum:** Vì $$c$$ nằm ngoài hình cầu, nghiệm nằm trên biên $$\|x\|_2 = 2$$. (Lưu ý: chiếu $$c$$ lên hình cầu chỉ tối ưu cho khoảng cách $$\ell_2$$, không phải $$\ell_1$$.) Trên biên với $$x_1 < 2$$, $$x_2 < 3$$:

$$f(x) = (2 - x_1) + (3 - x_2) = 5 - (x_1 + x_2)$$

nên bài toán trở thành $$\max\; x_1 + x_2$$ trên đường tròn $$x_1^2 + x_2^2 = 4$$, đạt tại $$x_1 = x_2 = \sqrt{2}$$:

$$x^* = (\sqrt{2}, \sqrt{2}) \approx (1.414, 1.414)$$

**Objective:** $$f(x^*) = 5 - 2\sqrt{2} \approx 2.172$$ (điểm chiếu $$\frac{2}{\sqrt{13}}(2,3)$$ cho $$2.227$$, tệ hơn). Đây chính là điểm mà projected subgradient đạt được tại $$x^{(2)}$$.

</details>

---

## 💡 **Tổng kết**

### **Subgradient Method Properties:**

| Aspect | Gradient Descent | Subgradient Method |
|--------|------------------|-------------------|
| **Applicability** | Smooth $$f$$ | Non-smooth $$f$$ |
| **Convergence** | Linear ($$O(\rho^k)$$) | Sublinear ($$O(1/\sqrt{k})$$) |
| **Step size** | Fixed or line search | Diminishing or Polyak |
| **Descent** | Always decreases | May increase! |
| **Usage** | Well-behaved $$f$$ | $$\ell_1$$, max, constraints |

### **Step Size Rules:**

1. **Constant $$\alpha$$:** Converges to neighborhood
2. **Diminishing $$\frac{1}{k}$$:** Hội tụ chính xác nhưng rất chậm (cận $$O(1/\log k)$$)
3. **Square summable $$\frac{1}{k^{0.6}}$$:** Hội tụ chính xác với cận $$O(1/k^{0.4})$$, nhanh hơn $$\frac{1}{k}$$
4. **Polyak:** Fast if $$f^*$$ known

### **Khi nào dùng Subgradient:**
- Non-differentiable $$f$$ ($$\ell_1$$, max)
- Simple per-iteration cost needed
- Willing to accept slow convergence
- Constraints via projection

---

## 📚 **Tài liệu Tham khảo**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Section 3.1.

2. **Shor, N. Z.** (1985). *Minimization Methods for Non-Differentiable Functions*. Springer.

3. **Polyak, B. T.** (1987). *Introduction to Optimization*. Optimization Software.

