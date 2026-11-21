---
layout: post
title: 15-11 Bài Tập Thực Hành - Phương Pháp Rào Cản
chapter: '15'
order: 17
owner: GitHub Copilot
lang: vi
categories:
- chapter15
lesson_type: required
redirect_from:
  - /contents/vi/chapter15/15_10_Practical_Exercises_Barrier_Method/
---

# Bài Tập Thực Hành - Phương Pháp Rào Cản (Barrier Method)

Các bài tập được tham khảo từ Boyd & Vandenberghe (2004), Nocedal & Wright (2006), và Nesterov (2004).

---

## 📝 **Phần I: Log-Barrier Function**

### **Bài tập 1: Tính Log-Barrier (Boyd & Vandenberghe, Ex. 11.1)**

Cho bài toán:

$$
\begin{align}
\min_{x} \quad & f(x) \\
\text{s.t.} \quad & h_i(x) \leq 0, \quad i = 1, \ldots, m
\end{align}
$$

Log-barrier function:

$$
\phi(x) = -\sum_{i=1}^m \log(-h_i(x))
$$

**Yêu cầu:**  
a) Tính $$\nabla \phi(x)$$ và $$\nabla^2 \phi(x)$$  
b) Cho $$f(x) = x^2$$, $$h_1(x) = x - 1$$, $$h_2(x) = -x - 1$$ (tức $$-1 \leq x \leq 1$$). Tính $$\phi(x)$$, $$\nabla \phi(x)$$, $$\nabla^2 \phi(x)$$  
c) Tại $$x = 0$$, tính các giá trị trên

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Gradient và Hessian của $$\phi(x)$$:**

**Gradient:**

$$
\nabla \phi(x) = -\sum_{i=1}^m \frac{1}{-h_i(x)} \nabla h_i(x) = \sum_{i=1}^m \frac{\nabla h_i(x)}{-h_i(x)}
$$

**Hessian:**

$$
\nabla^2 \phi(x) = \sum_{i=1}^m \left( \frac{\nabla^2 h_i(x)}{-h_i(x)} + \frac{\nabla h_i(x) \nabla h_i(x)^T}{h_i(x)^2} \right)
$$

---

**b) Ví dụ cụ thể:**

$$
f(x) = x^2, \quad h_1(x) = x - 1, \quad h_2(x) = -x - 1
$$

**Barrier function:**

$$
\phi(x) = -\log(-(x-1)) - \log(-(-x-1)) = -\log(1-x) - \log(1+x)
$$

**Gradient:**

$$
\nabla h_1(x) = 1, \quad \nabla h_2(x) = -1
$$

$$
\nabla \phi(x) = \frac{1}{1-x} + \frac{-1}{1+x} = \frac{1+x-(1-x)}{(1-x)(1+x)} = \frac{2x}{1-x^2}
$$

**Hessian:**

$$
\nabla^2 h_1(x) = 0, \quad \nabla^2 h_2(x) = 0
$$

$$
\nabla^2 \phi(x) = \frac{1}{(1-x)^2} + \frac{1}{(1+x)^2}
$$

$$
= \frac{(1+x)^2 + (1-x)^2}{(1-x^2)^2} = \frac{2(1+x^2)}{(1-x^2)^2}
$$

---

**c) Tại $$x = 0$$:**

$$
\phi(0) = -\log(1) - \log(1) = 0
$$

$$
\nabla \phi(0) = \frac{0}{1} = 0
$$

$$
\nabla^2 \phi(0) = \frac{2 \cdot 1}{1} = 2
$$

**Giải thích:** Tại tâm miền khả thi ($$x=0$$), barrier function đạt minimum, gradient = 0.

</details>

---

### **Bài tập 2: Central Path (Boyd & Vandenberghe, Ex. 11.2)**

Tiếp tục bài tập 1, xét barrier problem:

$$
\min_x \quad t f(x) + \phi(x) = t x^2 - \log(1-x) - \log(1+x)
$$

**Yêu cầu:**  
a) Tìm điều kiện FOC (First Order Condition)  
b) Giải FOC để tìm $$x^*(t)$$ (central path point)  
c) Tính $$x^*(1)$$, $$x^*(10)$$, $$x^*(100)$$  
d) Khi $$t \to \infty$$, $$x^*(t) \to ?$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) FOC:**

$$
\frac{d}{dx}\left( t x^2 - \log(1-x) - \log(1+x) \right) = 0
$$

$$
2tx + \frac{1}{1-x} - \frac{1}{1+x} = 0
$$

$$
2tx + \frac{2x}{1-x^2} = 0
$$

$$
x\left( 2t + \frac{2}{1-x^2} \right) = 0
$$

**Hai trường hợp:**
1. $$x = 0$$ (luôn là nghiệm do tính đối xứng)
2. $$2t + \frac{2}{1-x^2} = 0$$ (không có nghiệm thực vì vế trái > 0)

**Kết luận:** $$x^*(t) = 0$$ với mọi $$t > 0$$.

---

**b) Giải thích:**

Vì $$f(x) = x^2$$ đối xứng quanh $$x=0$$ và miền khả thi $$(-1, 1)$$ cũng đối xứng, nên central path là $$x^*(t) = 0$$ cho mọi $$t$$.

---

**c) Các giá trị:**

$$
x^*(1) = 0, \quad x^*(10) = 0, \quad x^*(100) = 0
$$

---

**d) Giới hạn:**

$$
\lim_{t \to \infty} x^*(t) = 0
$$

Đây chính là nghiệm của bài toán gốc: $$\min_{-1 \leq x \leq 1} x^2 = 0$$ tại $$x = 0$$.

**Lưu ý:** Đây là trường hợp đặc biệt. Thông thường, central path sẽ di chuyển khi $$t$$ tăng.

</details>

---

## 📝 **Phần II: Central Path Analysis**

### **Bài tập 3: Central Path cho LP (Nocedal & Wright, Ex. 14.1)**

Cho bài toán LP:

$$
\begin{align}
\min_{x} \quad & c^T x \\
\text{s.t.} \quad & Ax = b \\
& x \geq 0
\end{align}
$$

Với $$c = \begin{bmatrix} -1 \\ -1 \end{bmatrix}$$, $$A = \begin{bmatrix} 1 & 1 \end{bmatrix}$$, $$b = 1$$.

**Yêu cầu:**  
a) Viết barrier problem  
b) Tìm central path $$x^*(t)$$  
c) Tính $$\lim_{t \to \infty} x^*(t)$$  
d) So sánh với nghiệm primal-dual

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Barrier problem:**

$$
\min_x \quad t c^T x - \sum_{i=1}^2 \log x_i \quad \text{s.t.} \quad x_1 + x_2 = 1
$$

$$
= \min_x \quad -t(x_1 + x_2) - \log x_1 - \log x_2 \quad \text{s.t.} \quad x_1 + x_2 = 1
$$

---

**b) Tìm central path:**

**Lagrangian:**

$$
L(x, \nu) = -t(x_1 + x_2) - \log x_1 - \log x_2 - \nu(x_1 + x_2 - 1)
$$

**FOC:**

$$
\frac{\partial L}{\partial x_1} = -t - \frac{1}{x_1} - \nu = 0 \Rightarrow \frac{1}{x_1} = -t - \nu
$$

$$
\frac{\partial L}{\partial x_2} = -t - \frac{1}{x_2} - \nu = 0 \Rightarrow \frac{1}{x_2} = -t - \nu
$$

Từ hai phương trình → $$x_1 = x_2$$.

Từ $$x_1 + x_2 = 1$$: $$x_1 = x_2 = 0.5$$.

**Central path:**

$$
x^*(t) = \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix} \quad \forall t > 0
$$

**Dual variable:**

$$
\frac{1}{0.5} = -t - \nu \Rightarrow \nu = -t - 2
$$

---

**c) Giới hạn:**

$$
\lim_{t \to \infty} x^*(t) = \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix}
$$

**Kiểm tra với bài toán gốc:**

$$
\min -x_1 - x_2 \quad \text{s.t.} \quad x_1 + x_2 = 1, \quad x \geq 0
$$

Giá trị tối ưu: $$-1$$ tại bất kỳ $$x$$ thỏa $$x_1 + x_2 = 1$$, $$x \geq 0$$.

Tập nghiệm tối ưu: đoạn thẳng từ $$(0,1)$$ đến $$(1,0)$$.

Central path hội tụ đến **tâm analytic** của tập nghiệm ($$x_1 = x_2 = 0.5$$).

---

**d) So sánh primal-dual:**

**Dual problem:**

$$
\max_{\nu} \quad \nu \quad \text{s.t.} \quad \begin{bmatrix} \nu \\ \nu \end{bmatrix} \leq \begin{bmatrix} -1 \\ -1 \end{bmatrix}
$$

$$\nu \leq -1$$ → $$\nu^* = -1$$.

**Duality gap:**

$$
\text{gap}(t) = c^T x^*(t) - b^T y(t)
$$

Điểm dual khả thi suy ra từ central path: $$\lambda_i(t) = \frac{1}{t x_i^*(t)} = \frac{2}{t}$$ và $$y(t) = \frac{\nu(t)}{t} = -1 - \frac{2}{t} \leq -1$$ (khả thi cho dual). Giá trị dual $$b^Ty(t) = -1 - \frac{2}{t}$$, nên

$$
\text{gap}(t) = -1 - \left(-1 - \frac{2}{t}\right) = \frac{2}{t} = \frac{m}{t}
$$

Gap **khác 0** với mọi $$t$$ hữu hạn và $$\to 0$$ khi $$t \to \infty$$ (đúng như công thức $$m/t$$ với $$m = 2$$).

**Lưu ý:** Công thức $$\text{gap} = m/t$$ luôn đúng trên central path; gap bằng 0 chỉ khi so với giá trị dual tối ưu $$\nu^* = -1$$, tức là khi $$t \to \infty$$.

</details>

---

## 📝 **Phần III: Perturbed KKT Conditions**

### **Bài tập 4: KKT Điều kiện với Barrier (Boyd & Vandenberghe, Ex. 11.4)**

Cho barrier problem:

$$
\min_x \quad t f(x) + \phi(x)
$$

**Yêu cầu:**  
a) Viết điều kiện KKT cho barrier problem  
b) Chứng minh: Nếu $$x^*(t)$$ thỏa KKT của barrier problem, thì tồn tại $$\lambda^*(t)$$ sao cho:

$$
\begin{align}
\nabla f(x^*(t)) + \sum_i \lambda_i^*(t) \nabla h_i(x^*(t)) &= 0 \\
\lambda_i^*(t) &= -\frac{1}{t h_i(x^*(t))} \\
h_i(x^*(t)) &< 0
\end{align}
$$

c) Tính $$\lambda_i^*(t) h_i(x^*(t))$$  
d) Khi $$t \to \infty$$, điều gì xảy ra?

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) KKT cho barrier problem:**

$$
\min_x \quad t f(x) + \phi(x) = t f(x) - \sum_i \log(-h_i(x))
$$

**FOC:**

$$
t \nabla f(x) + \nabla \phi(x) = 0
$$

$$
t \nabla f(x) + \sum_i \frac{\nabla h_i(x)}{-h_i(x)} = 0
$$

---

**b) Chứng minh perturbed KKT:**

Định nghĩa:

$$
\lambda_i^*(t) := -\frac{1}{t h_i(x^*(t))}
$$

Thay vào FOC:

$$
t \nabla f(x^*) + \sum_i \frac{\nabla h_i(x^*)}{-h_i(x^*)} = 0
$$

$$
\nabla f(x^*) + \sum_i \frac{1}{-t h_i(x^*)} \nabla h_i(x^*) = 0
$$

$$
\nabla f(x^*) + \sum_i \left(-\frac{1}{t h_i(x^*)}\right) \nabla h_i(x^*) = 0
$$

$$
\nabla f(x^*) + \sum_i \lambda_i^*(t) \nabla h_i(x^*) = 0
$$

✓ Đây chính là điều kiện stationarity của KKT!

**Tính feasibility:**

Vì $$x^*$$ strictly feasible cho barrier: $$h_i(x^*) < 0$$ ✓

**Dual feasibility:**

$$
\lambda_i^* = -\frac{1}{t h_i(x^*)} > 0 \quad \text{(vì } h_i(x^*) < 0 \text{)}
$$

✓

---

**c) Complementary slackness (perturbed):**

$$
\lambda_i^*(t) h_i(x^*(t)) = -\frac{1}{t h_i(x^*)} \cdot h_i(x^*) = -\frac{1}{t}
$$

**Không bằng 0!** Đây là **complementary slackness bị nhiễu**.

---

**d) Khi $$t \to \infty$$:**

$$
\lambda_i^*(t) h_i(x^*(t)) = -\frac{1}{t} \to 0
$$

**Perturbed KKT conditions** → **KKT conditions chính xác**.

$$x^*(t) \to x^*$$, $$\lambda^*(t) \to \lambda^*$$ (nghiệm tối ưu thực sự).

**Duality gap:**

$$
\text{gap}(t) = f(x^*(t)) - g(\lambda^*(t), \nu^*(t)) = \frac{m}{t}
$$

với $$m$$ = số ràng buộc inequality.

</details>

---

## 📝 **Phần IV: Convergence Analysis**

### **Bài tập 5: Duality Gap và Convergence (Boyd & Vandenberghe, Theorem 11.2)**

Cho barrier method với parameter $$t^{(k)} = \mu^k t^{(0)}$$, $$\mu > 1$$.

**Yêu cầu:**  
a) Chứng minh duality gap sau $$k$$ iterations: $$\text{gap}^{(k)} = \frac{m}{t^{(k)}}$$  
b) Để đạt $$\text{gap} < \epsilon$$, cần bao nhiêu outer iterations?  
c) Với $$m = 100$$, $$\mu = 10$$, $$\epsilon = 10^{-6}$$, tính số iterations  
d) Tổng số Newton iterations (giả sử mỗi outer iteration cần $$\approx 10$$ Newton steps)

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Duality gap:**

Tại iteration $$k$$, central path point $$x^*(t^{(k)})$$ thỏa perturbed KKT:

$$
\lambda_i^*(t^{(k)}) h_i(x^*(t^{(k)})) = -\frac{1}{t^{(k)}}
$$

**Duality gap:**

$$
\eta(t^{(k)}) = f(x^*(t^{(k)})) - g(\lambda^*(t^{(k)}), \nu^*(t^{(k)}))
$$

Theo lý thuyết barrier method (Boyd & Vandenberghe, Theorem 11.2):

$$
\eta(t) = \frac{m}{t}
$$

với $$m$$ = số ràng buộc inequality.

---

**b) Số iterations cần thiết:**

Điều kiện: $$\frac{m}{t^{(k)}} < \epsilon$$

$$
t^{(k)} > \frac{m}{\epsilon}
$$

Với $$t^{(k)} = \mu^k t^{(0)}$$:

$$
\mu^k t^{(0)} > \frac{m}{\epsilon}
$$

$$
k > \frac{\log(m/(\epsilon t^{(0)}))}{\log \mu}
$$

Nếu bắt đầu với $$t^{(0)} = 1$$:

$$
k > \frac{\log(m/\epsilon)}{\log \mu}
$$

---

**c) Tính số cụ thể:**

$$
k > \frac{\log(100/10^{-6})}{\log 10} = \frac{\log(10^8)}{\log 10} = 8
$$

**Số outer iterations:** $$k > 8$$ nên cần $$k = 9$$ (với $$k = 8$$ thì $$\text{gap} = m/\mu^8 = 10^{-6} = \epsilon$$, chưa nhỏ hơn $$\epsilon$$ một cách chặt)

---

**d) Tổng Newton iterations:**

Giả sử mỗi outer iteration cần $$\approx 10$$ Newton steps:

$$
\text{Total Newton iters} \approx 9 \times 10 = 90
$$

**Phân tích:**
- Barrier method với $$\mu$$ cố định: $$O(\log(m/\epsilon))$$ outer iterations
- Với $$\mu = 1 + 1/\sqrt{m}$$ (short-step): $$O(\sqrt{m}\log(m/\epsilon))$$ outer iterations, mỗi iteration chỉ cần $$O(1)$$ Newton step
- Tổng số Newton steps (lý thuyết): $$O(\sqrt{m} \log(m/\epsilon))$$

Với bài toán này ($$\mu = 10$$ large): ít outer iterations nhưng có thể cần nhiều Newton steps hơn mỗi iteration.

</details>

---

## 📝 **Phần V: Feasibility và Phase I**

### **Bài tập 6: Phase I Method (Nocedal & Wright, Ex. 14.3)**

Tìm điểm strictly feasible cho:

$$
\begin{align}
& x_1 + x_2 \leq 1 \\
& x_1 - x_2 \leq 0.5 \\
& -x_1 \leq 0 \\
& -x_2 \leq 0
\end{align}
$$

**Yêu cầu:**  
a) Viết Phase I problem:

$$
\min_{x, s} \quad s \quad \text{s.t.} \quad h_i(x) \leq s, \quad i=1,\ldots,m
$$

b) Giải Phase I problem bằng barrier method  
c) Nếu nghiệm có $$s^* < 0$$, chọn strictly feasible point

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Phase I problem:**

$$
\begin{align}
\min_{x_1, x_2, s} \quad & s \\
\text{s.t.} \quad & x_1 + x_2 - 1 \leq s \\
& x_1 - x_2 - 0.5 \leq s \\
& -x_1 \leq s \\
& -x_2 \leq s
\end{align}
$$

**Tương đương:**

$$
\min_{x, s} \quad s \quad \text{s.t.} \quad h_i(x) - s \leq 0
$$

---

**b) Giải bằng analytic center:**

**Barrier problem:**

$$
\min_{x, s} \quad t \cdot s - \sum_i \log(-(h_i(x) - s))
$$

Với $$t$$ lớn, nghiệm gần với:

$$
\min_s \quad s \quad \text{s.t.} \quad h_i(x) \leq s
$$

tức $$s^* = \max_i h_i(x)$$.

**Nghiệm:** Phase I problem là một LP trong 3 biến $$(x_1, x_2, s)$$. Tại nghiệm tối ưu, ba ràng buộc $$h_1, h_3, h_4$$ cùng chặt:

$$x_1 + x_2 - 1 = -x_1 = -x_2 = s \;\Rightarrow\; x_1 = x_2 = -s,\quad -2s - 1 = s \;\Rightarrow\; s = -\tfrac{1}{3}$$

**Nghiệm:** $$x^* = \left(\tfrac{1}{3}, \tfrac{1}{3}\right)$$, $$s^* = -\tfrac{1}{3}$$.

**Kiểm tra:**

$$
\begin{align}
h_1 &= \tfrac{1}{3} + \tfrac{1}{3} - 1 = -\tfrac{1}{3} \\
h_2 &= \tfrac{1}{3} - \tfrac{1}{3} - 0.5 = -0.5 \\
h_3 &= -\tfrac{1}{3} \\
h_4 &= -\tfrac{1}{3}
\end{align}
$$

$$s = \max_i h_i = -\tfrac{1}{3}$$. (Điểm $$x = (0.25, 0.25)$$ cũng khả thi với $$s = -0.25$$ nhưng chưa tối ưu cho Phase I vì $$-0.25 > -\tfrac{1}{3}$$.)

---

**c) Strictly feasible point:**

Vì $$s^* = -\tfrac{1}{3} < 0$$, bài toán **feasible** và $$x = (\tfrac{1}{3}, \tfrac{1}{3})$$ thỏa mãn **chặt** cả bốn bất đẳng thức ($$h_i = -\tfrac{1}{3}, -0.5, -\tfrac{1}{3}, -\tfrac{1}{3} < 0$$).

Trong thực tế chỉ cần một điểm bất kỳ có $$s < 0$$ (ví dụ $$x = (0.25, 0.25)$$ với $$s = -0.25$$) là đủ làm điểm khởi đầu cho barrier method.

</details>

---

## 📝 **Phần VI: Bài toán Tổng hợp**

### **Bài tập 7: Portfolio Optimization với Barrier (Boyd & Vandenberghe, Ex. 11.10)**

$$
\begin{align}
\min_x \quad & x^T \Sigma x \\
\text{s.t.} \quad & \mu^T x \geq r_{\min} \\
& \mathbf{1}^T x = 1 \\
& x \geq 0
\end{align}
$$

Với $$\Sigma = \begin{bmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{bmatrix}$$, $$\mu = \begin{bmatrix} 0.10 \\ 0.15 \end{bmatrix}$$, $$r_{\min} = 0.12$$.

**Yêu cầu:**  
a) Viết barrier problem  
b) Tính central path tại $$t = 1, 10, 100$$  
c) Phân tích convergence

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Barrier problem:**

Viết lại:

$$
\begin{align}
\min_x \quad & x^T \Sigma x \\
\text{s.t.} \quad & -\mu^T x + r_{\min} \leq 0 \quad \text{(inequality 1)} \\
& \mathbf{1}^T x = 1 \quad \text{(equality)} \\
& -x_i \leq 0, \quad i=1,2 \quad \text{(inequalities 2, 3)}
\end{align}
$$

**Barrier function:**

$$
\phi(x) = -\log(-(-\mu^T x + r_{\min})) - \sum_{i=1}^2 \log x_i
$$

$$
= -\log(\mu^T x - r_{\min}) - \log x_1 - \log x_2
$$

**Barrier problem:**

$$
\min_x \quad t \cdot x^T \Sigma x - \log(\mu^T x - r_{\min}) - \log x_1 - \log x_2
$$

s.t. $$\mathbf{1}^T x = 1$$

---

**b) Central path (numerical):**

**Lagrangian:**

$$
L = t x^T \Sigma x - \log(\mu^T x - r_{\min}) - \sum_i \log x_i - \nu(x_1 + x_2 - 1)
$$

**FOC:**

$$
2t \Sigma x - \frac{\mu}{\mu^T x - r_{\min}} - \begin{bmatrix} 1/x_1 \\ 1/x_2 \end{bmatrix} - \nu \mathbf{1} = 0
$$

$$
x_1 + x_2 = 1
$$

**Giải hệ (cần numerical solver):**

Với dữ liệu cho trước, approximate solutions:

**$$t = 1$$:**

$$x^*(1) \approx (0.247, 0.753)$$

(với $$t$$ nhỏ, thành phần rào cản chiếm ưu thế nên nghiệm gần tâm analytic của miền khả thi)

**$$t = 10$$:**

$$x^*(10) \approx (0.282, 0.718)$$

**$$t = 100$$:**

$$x^*(100) \approx (0.448, 0.552)$$ (và $$x^*(1000) \approx (0.571, 0.429)$$)

Hội tụ đến nghiệm tối ưu: $$x^* = (0.6, 0.4)$$ (ràng buộc return chặt: $$0.10(0.6)+0.15(0.4)=0.12$$; $$x^T\Sigma x = 0.0336$$).

---

**c) Convergence analysis:**

**Duality gap:**

$$m = 3$$ inequality constraints

$$
\text{gap}(t) = \frac{3}{t}
$$

- $$t = 1$$: gap = 3
- $$t = 10$$: gap = 0.3
- $$t = 100$$: gap = 0.03

Để gap $$< 10^{-6}$$: cần $$t > 3 \times 10^6$$.

Với $$\mu = 10$$:

$$
k > \frac{\log(3 \times 10^6)}{\log 10} \approx 6.5 \Rightarrow k = 7 \text{ iterations}
$$

</details>

---

## 💡 **Tổng kết và Chiến lược**

### **Log-Barrier Function:**
- $$\phi(x) = -\sum_i \log(-h_i(x))$$
- $$\nabla \phi(x) = \sum_i \frac{\nabla h_i(x)}{-h_i(x)}$$
- $$\phi(x) \to \infty$$ khi $$x$$ đến biên

### **Central Path:**
- $$x^*(t)$$ = nghiệm của $$\min t f(x) + \phi(x)$$
- Khi $$t \to \infty$$: $$x^*(t) \to x^*$$ (nghiệm tối ưu)
- Central path characterization: perturbed KKT

### **Perturbed KKT:**
- $$\nabla f(x^*) + \sum_i \lambda_i^* \nabla h_i(x^*) = 0$$
- $$\lambda_i^* = -\frac{1}{t h_i(x^*)}$$
- $$\lambda_i^* h_i(x^*) = -\frac{1}{t} \to 0$$ khi $$t \to \infty$$

### **Convergence:**
- Duality gap: $$\eta(t) = \frac{m}{t}$$
- Outer iterations: $$O(\log(m/\epsilon) / \log \mu)$$
- Với $$\mu = 10$$: $$\approx \log_{10}(m/\epsilon)$$ iterations
- Mỗi iteration: solve barrier problem bằng Newton method

### **Phase I Method:**
- Tìm strictly feasible point
- $$\min_{x,s} s$$ s.t. $$h_i(x) \leq s$$
- Nếu $$s^* < 0$$: feasible, chọn $$x^*$$

---

## 📚 **Tài liệu Tham khảo**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 11.

2. **Nocedal, J., & Wright, S. J.** (2006). *Numerical Optimization* (2nd ed.). Springer. Chapter 14, 19.

3. **Nesterov, Y.** (2004). *Introductory Lectures on Convex Optimization*. Springer. Chapter 4.

4. **Wright, S. J.** (1997). *Primal-Dual Interior-Point Methods*. SIAM.

5. **Ben-Tal, A., & Nemirovski, A.** (2001). *Lectures on Modern Convex Optimization*. SIAM. Chapter 4.

