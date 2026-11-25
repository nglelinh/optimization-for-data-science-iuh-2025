---
layout: post
title: 13-09 Bài Tập Thực Hành - Ứng Dụng Tính Đối Ngẫu
chapter: '13'
order: 13
owner: GitHub Copilot
lang: vi
categories:
- chapter13
lesson_type: required
redirect_from:
  - /contents/vi/chapter13/13_08_Practical_Exercises_Duality_Applications/
---

Lý thuyết đối ngẫu chỉ thực sự thấm vào tư duy khi bạn tự tay đặt bút tính một hàm liên hợp, chứng minh một chuẩn đối ngẫu bằng bất đẳng thức Hölder, hay tự tay lập bài toán đối ngẫu cho Lasso và quy hoạch nón. Nhiều khái niệm tưởng chừng trừu tượng trên slide — như vì sao liên hợp của tổng hai hàm lại liên quan đến phép chập infimal, hay vì sao chuẩn đối ngẫu của chuẩn $$\ell_1$$ lại là $$\ell_\infty$$ — sẽ trở nên trong suốt ngay khi bạn hoàn thành vài bài tập tự luận cốt lõi.

Tuyển tập bài tập thực hành này chắt lọc những bài toán kinh điển từ Boyd & Vandenberghe, Rockafellar và Ben-Tal & Nemirovski. Trước khi bắt tay giải từng phần, hãy xem qua bản đồ chiến lược và một bài mẫu trình bày chuẩn để quen nhịp chứng minh.

## Kiến thức cần nhớ: Bốn kỹ năng chứng minh trọng tâm trong bài tập Chương 13

- **Chứng minh chuẩn đối ngẫu bằng hai chiều bất đẳng thức:** Để chứng minh $$\|y\|_* = M(y)$$, luôn đi theo hai bước chuẩn: (1) dùng bất đẳng thức (Hölder, Cauchy–Schwarz, hoặc bất đẳng thức tam giác) để chỉ ra $$y^T x \le M(y)$$ với mọi $$\|x\| \le 1$$; (2) chỉ ra một vectơ cụ thể $$x_0$$ có $$\|x_0\| \le 1$$ đạt đúng dấu bằng $$y^T x_0 = M(y)$$.
- **Tính hàm liên hợp theo từng miền giá trị của $$y$$:** Khi tính $$f^*(y) = \sup_x (y^T x - f(x))$$, luôn kiểm tra trước xem biểu thức có bị không bị chặn trên ($$+\infty$$) ở vùng $$y$$ nào không, sau đó mới giải phương trình đạo hàm $$\nabla f(x) = y$$ trên miền hữu hạn.
- **Lập đối ngẫu có hệ thống qua tách biến:** Với bài toán dạng $$\min_x f(x) + g(Ax)$$, đặt $$z = Ax$$ giúp chuẩn hóa quy trình lập đối ngẫu thành 3 dòng đại số không bao giờ nhầm dấu.
- **Kiểm tra chéo bằng ví dụ số nhỏ:** Sau khi tìm xong công thức tổng quát (cho chuẩn đối ngẫu, hàm liên hợp hay đối ngẫu Lasso), luôn thử thay một bộ số nguyên đơn giản vào cả hai vế để phát hiện tức thì lỗi sai dấu hay thiếu hệ số $$1/2$$.

### Giải thích: Bài mẫu chứng minh hàm liên hợp của hàm mũ âm logarit

**Bài toán mẫu:** Tính hàm liên hợp $$f^*(y)$$ của hàm $$f(x) = -\log x$$ với miền xác định $$\operatorname{dom} f = \{x \in \mathbb{R} : x > 0\}$$.

1. **Thiết lập bài toán cực đại hóa:**
   $$f^*(y) = \sup_{x > 0} \bigl(yx + \log x\bigr).$$
2. **Xét trường hợp $$y \ge 0$$:**
   Khi $$y \ge 0$$ và $$x \to +\infty$$, cả $$yx \ge 0$$ lẫn $$\log x \to +\infty$$ nên $$yx + \log x \to +\infty$$. Do đó $$f^*(y) = +\infty$$ với mọi $$y \ge 0$$.
3. **Xét trường hợp $$y < 0$$:**
   Đặt $$h(x) = yx + \log x$$ trên $$(0, +\infty)$$. Đạo hàm bậc nhất và bậc hai:
   $$h'(x) = y + \frac{1}{x} = 0 \iff x^\star = -\frac{1}{y} > 0, \qquad h''(x) = -\frac{1}{x^2} < 0.$$
   Vì $$h$$ lõm chặt trên $$(0, +\infty)$$, điểm $$x^\star = -1/y$$ là cực đại toàn cục duy nhất.
4. **Thay $$x^\star = -1/y$$ để thu công thức đóng và kiểm tra số:**
   $$f^*(y) = y\left(-\frac{1}{y}\right) + \log\left(-\frac{1}{y}\right) = -1 - \log(-y), \qquad \text{với } y < 0.$$
   *Kiểm tra nhanh tại $$x = 2, y = -0.5$$ (đúng tại $$y = f'(x) = -1/x$$):* $$f(2) = -\log 2$$, $$f^*(-0.5) = -1 - \log(0.5) = -1 + \log 2$$. Tổng $$f(2) + f^*(-0.5) = -1 = (-0.5) \cdot 2 = yx$$ — khớp hoàn hảo dấu bằng Fenchel–Young!

---

# Bài tập thực hành - Ứng dụng tính đối ngẫu

Các bài tập dưới đây được tham khảo từ Boyd & Vandenberghe (2004), Rockafellar (1970) và Ben-Tal & Nemirovski (2001).

---

## 📝 **Phần I: Chuẩn đối ngẫu (Dual Norms)**

### **Bài tập 1: Tính toán chuẩn đối ngẫu (Boyd & Vandenberghe, Ex. 3.7)**

Cho chuẩn $$\|x\|$$, chuẩn đối ngẫu được định nghĩa bởi:

$$
\|y\|_* = \max_{\|x\| \leq 1} y^T x
$$

**Yêu cầu:** Tìm chuẩn đối ngẫu cho các chuẩn sau:

a) $$\|x\|_1 = \sum_{i=1}^n |x_i|$$  
b) $$\|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2}$$  
c) $$\|x\|_\infty = \max_i |x_i|$$  
d) $$\|x\|_p = (\sum_{i=1}^n |x_i|^p)^{1/p}$$ với $$p \geq 1$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Công thức tổng quát:** Chuẩn đối ngẫu của $$\|\cdot\|_p$$ là $$\|\cdot\|_q$$ với $$\frac{1}{p} + \frac{1}{q} = 1$$.

---

**a) Chuẩn $$\ell_1$$:**

Cần tính:

$$
\|y\|_* = \max_{\|x\|_1 \leq 1} y^T x = \max_{\sum_i |x_i| \leq 1} \sum_i y_i x_i
$$

**Phân tích:**  
- Để cực đại hóa $$\sum_i y_i x_i$$, ta chọn các thành phần $$x_i$$ cùng dấu với $$y_i$$.
- Với ràng buộc $$\sum_i |x_i| \leq 1$$, ta dồn toàn bộ trọng số vào tọa độ có $$|y_i|$$ lớn nhất.

Đặt $$x_j = \text{sign}(y_j)$$ với $$j = \arg\max_i |y_i|$$ và các $$x_i = 0$$ với $$i \neq j$$. Khi đó:

$$
\|y\|_* = \max_i |y_i| = \|y\|_\infty
$$

**Kết luận:** $$(\|\cdot\|_1)_* = \|\cdot\|_\infty$$.

---

**b) Chuẩn $$\ell_2$$:**

$$
\|y\|_* = \max_{\|x\|_2 \leq 1} y^T x
$$

Theo bất đẳng thức Cauchy–Schwarz:

$$
y^T x \leq \|y\|_2 \|x\|_2 \leq \|y\|_2
$$

Dấu bằng đạt được khi $$x = \frac{y}{\|y\|_2}$$ (với $$y \neq 0$$).

**Kết luận:** $$(\|\cdot\|_2)_* = \|\cdot\|_2$$ (tự đối ngẫu).

---

**c) Chuẩn $$\ell_\infty$$:**

$$
\|y\|_* = \max_{\max_i |x_i| \leq 1} \sum_i y_i x_i
$$

Chọn $$x_i = \text{sign}(y_i)$$ cho mọi $$i$$ (thỏa mãn $$|x_i| \leq 1$$):

$$
\|y\|_* = \sum_i |y_i| = \|y\|_1
$$

**Kết luận:** $$(\|\cdot\|_\infty)_* = \|\cdot\|_1$$.

---

**d) Chuẩn $$\ell_p$$ tổng quát:**

Theo bất đẳng thức Hölder:

$$
y^T x \leq \|y\|_q \|x\|_p
$$

với $$\frac{1}{p} + \frac{1}{q} = 1$$.

Dấu bằng đạt được khi chọn $$x_i = c \cdot \text{sign}(y_i) |y_i|^{q-1}$$ (với hằng số chuẩn hóa $$c > 0$$ sao cho $$\|x\|_p = 1$$).

**Kết luận:** $$(\|\cdot\|_p)_* = \|\cdot\|_q$$ với $$\frac{1}{p} + \frac{1}{q} = 1$$.

---

**Bảng tóm tắt:**

| Chuẩn gốc | Chuẩn đối ngẫu | Quan hệ |
|-----------|----------------|---------|
| $$\|\cdot\|_1$$ | $$\|\cdot\|_\infty$$ | $$p=1, q=\infty$$ |
| $$\|\cdot\|_2$$ | $$\|\cdot\|_2$$ | Tự đối ngẫu |
| $$\|\cdot\|_\infty$$ | $$\|\cdot\|_1$$ | $$p=\infty, q=1$$ |
| $$\|\cdot\|_p$$ | $$\|\cdot\|_q$$ | $$1/p + 1/q = 1$$ |

</details>

---

### **Bài tập 2: Kiểm chứng tính chất chuẩn đối ngẫu**

Cho $$x = (3, 4)^T$$ và $$y = (0.6, 0.8)^T$$.

**Yêu cầu:**  
a) Tính $$\|x\|_1$$, $$\|x\|_2$$, $$\|x\|_\infty$$  
b) Tính $$\|y\|_1$$, $$\|y\|_2$$, $$\|y\|_\infty$$  
c) Kiểm chứng bất đẳng thức $$y^T x \leq \|y\|_* \|x\|$$ cho từng cặp chuẩn đối ngẫu

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Các chuẩn của $$x = (3,4)^T$$:**

$$
\begin{align}
\|x\|_1 &= |3| + |4| = 7 \\
\|x\|_2 &= \sqrt{3^2 + 4^2} = \sqrt{25} = 5 \\
\|x\|_\infty &= \max(|3|, |4|) = 4
\end{align}
$$

---

**b) Các chuẩn của $$y = (0.6, 0.8)^T$$:**

$$
\begin{align}
\|y\|_1 &= 0.6 + 0.8 = 1.4 \\
\|y\|_2 &= \sqrt{0.6^2 + 0.8^2} = \sqrt{0.36 + 0.64} = 1 \\
\|y\|_\infty &= \max(0.6, 0.8) = 0.8
\end{align}
$$

---

**c) Kiểm chứng bất đẳng thức:**

Trước hết tính tích vô hướng:

$$
y^T x = 0.6 \times 3 + 0.8 \times 4 = 1.8 + 3.2 = 5
$$

**Trường hợp 1:** Cặp $$\|x\|_1$$ và $$\|y\|_\infty$$ (vì $$(\|\cdot\|_1)_* = \|\cdot\|_\infty$$):

$$
y^T x = 5 \leq \|y\|_\infty \|x\|_1 = 0.8 \times 7 = 5.6
$$

✓ Thỏa mãn.

---

**Trường hợp 2:** Cặp $$\|x\|_2$$ và $$\|y\|_2$$ (tự đối ngẫu):

$$
y^T x = 5 \leq \|y\|_2 \|x\|_2 = 1 \times 5 = 5
$$

✓ Đạt dấu bằng (vì $$y = \frac{x}{\|x\|_2}$$).

---

**Trường hợp 3:** Cặp $$\|x\|_\infty$$ và $$\|y\|_1$$ (vì $$(\|\cdot\|_\infty)_* = \|\cdot\|_1$$):

$$
y^T x = 5 \leq \|y\|_1 \|x\|_\infty = 1.4 \times 4 = 5.6
$$

✓ Thỏa mãn.

</details>

---

## 📝 **Phần II: Hàm liên hợp (Conjugate Functions)**

### **Bài tập 3: Tính hàm liên hợp (Rockafellar, Ex. 12.B)**

Hàm liên hợp của $$f(x)$$ được định nghĩa là:

$$
f^*(y) = \sup_x (y^T x - f(x))
$$

**Yêu cầu:** Tính hàm liên hợp cho các hàm sau:

a) $$f(x) = \frac{1}{2}x^T Q x$$ với $$Q \succ 0$$  
b) $$f(x) = \|x\|_2$$  
c) $$f(x) = e^x$$ (với $$x \in \mathbb{R}$$)  
d) $$f(x) = I_C(x)$$ (hàm chỉ thị của tập $$C$$)

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Hàm bậc hai $$f(x) = \frac{1}{2}x^T Q x$$:**

$$
f^*(y) = \sup_x \left( y^T x - \frac{1}{2} x^T Q x \right)
$$

Điều kiện bậc nhất theo $$x$$: $$\nabla_x (y^T x - \frac{1}{2}x^T Q x) = y - Qx = 0 \Rightarrow x^* = Q^{-1} y$$.

Thế lại vào biểu thức:

$$
f^*(y) = y^T Q^{-1} y - \frac{1}{2} (Q^{-1}y)^T Q (Q^{-1}y)
$$

$$
= y^T Q^{-1} y - \frac{1}{2} y^T Q^{-1} y = \frac{1}{2} y^T Q^{-1} y
$$

**Kết quả:** $$\boxed{f^*(y) = \frac{1}{2} y^T Q^{-1} y}$$

**Bất đẳng thức Fenchel tương ứng:**

$$
\frac{1}{2}x^T Q x + \frac{1}{2}y^T Q^{-1} y \geq x^T y
$$

---

**b) Chuẩn Euclidean $$f(x) = \|x\|_2$$:**

$$
f^*(y) = \sup_x (y^T x - \|x\|_2)
$$

**Phân tích:**
- Nếu $$\|y\|_2 \leq 1$$: theo bất đẳng thức Cauchy–Schwarz, $$y^Tx - \|x\|_2 \leq (\|y\|_2 - 1)\|x\|_2 \leq 0$$ với mọi $$x$$, và dấu bằng đạt tại $$x = 0$$.
- Nếu $$\|y\|_2 > 1$$: chọn $$x = ty$$ với $$t \to +\infty$$ thì $$y^T x - \|x\|_2 = t\|y\|_2(\|y\|_2 - 1) \to +\infty$$.

**Kết quả:**

$$
\boxed{f^*(y) = \begin{cases}
0 & \text{if } \|y\|_2 \leq 1 \\
\infty & \text{if } \|y\|_2 > 1
\end{cases}} = I_{\|y\|_2 \leq 1}(y)
$$

---

**c) Hàm mũ $$f(x) = e^x$$:**

$$
f^*(y) = \sup_x (yx - e^x)
$$

Điều kiện bậc nhất: $$y - e^x = 0 \Rightarrow x^* = \ln y$$ (chỉ tồn tại khi $$y > 0$$).

Thế vào biểu thức cho trường hợp $$y > 0$$:

$$
f^*(y) = y \ln y - e^{\ln y} = y \ln y - y
$$

Khi $$y = 0$$, $$\sup_x (-e^x) = 0$$ (khi $$x \to -\infty$$). Khi $$y < 0$$, cho $$x \to -\infty$$ thì $$yx - e^x \to +\infty$$.

**Kết quả:**

$$
\boxed{f^*(y) = \begin{cases}
y \ln y - y & \text{if } y > 0 \\
0 & \text{if } y = 0 \\
\infty & \text{if } y < 0
\end{cases}}
$$

---

**d) Hàm chỉ thị $$f(x) = I_C(x)$$:**

$$
f^*(y) = \sup_x (y^T x - I_C(x)) = \sup_{x \in C} y^T x
$$

**Kết quả:** $$\boxed{f^*(y) = \sup_{x \in C} y^T x}$$ (hàm hỗ trợ của tập $$C$$).

**Ví dụ minh họa:**
- $$C = \{x : \|x\|_2 \leq 1\}$$: $$f^*(y) = \|y\|_2$$
- $$C = \mathbb{R}^n_+$$: $$f^*(y) = I_{\{y \leq 0\}}(y)$$

</details>

---

### **Bài tập 4: Bất đẳng thức Fenchel (Boyd & Vandenberghe, Ex. 3.33)**

Cho $$f(x) = \frac{1}{2}\|x\|^2$$ và các vector $$x = (1, 2)^T$$, $$y = (3, 1)^T$$.

**Yêu cầu:**  
a) Tính $$f(x)$$ và $$f^*(y)$$  
b) Tính $$x^T y$$  
c) Kiểm chứng bất đẳng thức Fenchel: $$f(x) + f^*(y) \geq x^T y$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Tính $$f(x)$$ và $$f^*(y)$$:**

$$
f(x) = \frac{1}{2}(1^2 + 2^2) = \frac{1}{2}(1 + 4) = 2.5
$$

Với $$f(x) = \frac{1}{2}\|x\|^2$$ (tức $$Q = I$$), ta có $$f^*(y) = \frac{1}{2}\|y\|^2$$:

$$
f^*(y) = \frac{1}{2}\|y\|^2 = \frac{1}{2}(3^2 + 1^2) = \frac{1}{2}(9 + 1) = 5
$$

---

**b) Tính $$x^T y$$:**

$$
x^T y = 1 \times 3 + 2 \times 1 = 5
$$

---

**c) Kiểm chứng bất đẳng thức Fenchel:**

$$
f(x) + f^*(y) = 2.5 + 5 = 7.5 \geq 5 = x^T y
$$

✓ Thỏa mãn (chênh lệch: $$7.5 - 5 = 2.5$$).

**Điều kiện xảy ra dấu bằng:** Khi $$y \in \partial f(x)$$, tức $$y = \nabla f(x) = x$$. Ở đây $$\nabla f(x) = (1,2)^T \neq (3,1)^T = y$$, nên dấu bằng không xảy ra.

</details>

---

## 📝 **Phần III: Đối ngẫu của bài toán LASSO**

### **Bài tập 5: Xây dựng LASSO đối ngẫu (Boyd & Vandenberghe, Ex. 6.15)**

Xét bài toán LASSO nguyên thủy:

$$
\min_x \frac{1}{2}\|Ax - b\|^2 + \lambda \|x\|_1
$$

**Yêu cầu:**
a) Thiết lập bài toán đối ngẫu  
b) Giải thích mối liên hệ giữa nghiệm nguyên thủy và nghiệm đối ngẫu  
c) Với $$A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}$$, $$b = \begin{bmatrix} 1 \\ 1 \\ 3 \end{bmatrix}$$, $$\lambda = 0.5$$, hãy tìm nghiệm đối ngẫu

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Thiết lập bài toán đối ngẫu:**

Đặt biến phụ $$r = Ax - b$$, bài toán nguyên thủy trở thành:

$$
\begin{align}
\min_{x,r} \quad & \frac{1}{2}\|r\|^2 + \lambda \|x\|_1 \\
\text{s.t.} \quad & Ax - r = b
\end{align}
$$

Hàm Lagrangian tương ứng:

$$
L(x, r, \nu) = \frac{1}{2}\|r\|^2 + \lambda \|x\|_1 + \nu^T(Ax - r - b)
$$

Cực tiểu hóa theo $$x$$:

$$
\min_x \left( \lambda \|x\|_1 + \nu^T A x \right) = \begin{cases}
0 & \text{if } \|A^T \nu\|_\infty \leq \lambda \\
-\infty & \text{otherwise}
\end{cases}
$$

Cực tiểu hóa theo $$r$$ (đạt tại $$r = \nu$$):

$$
\min_r \left( \frac{1}{2}\|r\|^2 - \nu^T r \right) = -\frac{1}{2}\|\nu\|^2
$$

**Hàm đối ngẫu:**

$$
g(\nu) = -\frac{1}{2}\|\nu\|^2 - \nu^T b
$$

với ràng buộc $$\|A^T \nu\|_\infty \leq \lambda$$.

**Bài toán đối ngẫu (đổi dấu để viết dưới dạng cực tiểu hóa):**

$$
\boxed{
\begin{align}
\min_{\nu} \quad & \frac{1}{2}\|\nu\|^2 + \nu^T b \\
\text{s.t.} \quad & \|A^T \nu\|_\infty \leq \lambda
\end{align}
}
$$

---

**b) Quan hệ giữa nghiệm nguyên thủy và đối ngẫu:**

Từ các điều kiện KKT:
- $$r^* = \nu^*$$ (biến đối ngẫu chính là phần dư $$Ax^* - b$$).
- Nếu $$|(A^T \nu^*)_i| < \lambda$$ thì $$x_i^* = 0$$.
- Các chỉ số có $$|(A^T \nu^*)_i| = \lambda$$ tạo thành tập chỉ số tích cực (active set) chứa các thành phần có thể khác $$0$$ của $$x^*$$.

**Khôi phục nghiệm nguyên thủy từ nghiệm đối ngẫu:**

$$
x^* = \text{(nghiệm của bài toán rút gọn trên tập chỉ số tích cực)}
$$

---

**c) Tính nghiệm số:**

Với dữ liệu:

$$
A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}, \quad
b = \begin{bmatrix} 1 \\ 1 \\ 3 \end{bmatrix}, \quad
\lambda = 0.5
$$

**Bài toán đối ngẫu cụ thể:**

$$
\begin{align}
\min_{\nu} \quad & \frac{1}{2}(\nu_1^2 + \nu_2^2 + \nu_3^2) + \nu_1 + \nu_2 + 3\nu_3 \\
\text{s.t.} \quad & \max(|\nu_1 + \nu_3|, |\nu_2 + \nu_3|) \leq 0.5
\end{align}
$$

**Giải bài toán:**

Nếu xét nghiệm không ràng buộc (điều kiện bậc nhất):

$$
\nu_1 + 1 = 0 \Rightarrow \nu_1 = -1 \\
\nu_2 + 1 = 0 \Rightarrow \nu_2 = -1 \\
\nu_3 + 3 = 0 \Rightarrow \nu_3 = -3
$$

Kiểm tra ràng buộc:

$$
\max(|-1 - 3|, |-1 - 3|) = 4 > 0.5
$$

Điểm này không khả thi, nên ràng buộc phải tích cực.

**Giả sử** cả hai ràng buộc cùng chặt ở biên âm: $$\nu_1 + \nu_3 = \nu_2 + \nu_3 = -0.5$$. Do tính đối xứng, đặt $$\nu_1 = \nu_2 = a$$ và $$\nu_3 = -0.5 - a$$.

Sử dụng đồng nhất thức $$\frac{1}{2}\|\nu\|^2 + \nu^Tb = \frac{1}{2}\|\nu + b\|^2 - \frac{1}{2}\|b\|^2$$, ta cực tiểu hóa:

$$\min_a \; \frac{1}{2}\left[2(a+1)^2 + (2.5 - a)^2\right]$$

Lấy đạo hàm theo $$a$$ bằng $$0$$: $$2(a+1) - (2.5 - a) = 0 \Rightarrow a = \frac{1}{6}$$.

**Nghiệm đối ngẫu:**

$$
\nu^* = \left(\tfrac{1}{6}, \tfrac{1}{6}, -\tfrac{2}{3}\right)^T, \qquad \tfrac{1}{2}\|\nu^*\|^2 + \nu^{*T}b = \tfrac{1}{4} - \tfrac{5}{3} = -\tfrac{17}{12}
$$

Tức giá trị tối ưu của bài toán đối ngẫu (dạng cực đại hóa) là $$\frac{17}{12} \approx 1.4167$$.

**Kiểm chứng với bài toán nguyên thủy:** Nghiệm nguyên thủy $$x^* = \left(\tfrac{7}{6}, \tfrac{7}{6}\right)^T$$ cho phần dư $$Ax^* - b = \left(\tfrac{1}{6}, \tfrac{1}{6}, -\tfrac{2}{3}\right)^T = \nu^*$$ ✓ (đúng hệ thức $$r^* = \nu^*$$) và giá trị mục tiêu nguyên thủy $$\frac{1}{2}\|r^*\|^2 + \lambda\|x^*\|_1 = \frac{1}{4} + 0.5 \cdot \frac{7}{3} = \frac{17}{12}$$ ✓, khoảng cách đối ngẫu bằng $$0$$.

</details>

---

## 📝 **Phần IV: Nón đối ngẫu (Dual Cones)**

### **Bài tập 6: Tính nón đối ngẫu (Boyd & Vandenberghe, Ex. 2.36)**

Nón đối ngẫu của nón $$K$$ được định nghĩa là:

$$
K^* = \{ y : y^T x \geq 0, \forall x \in K \}
$$

**Yêu cầu:** Tìm nón đối ngẫu cho các nón sau:

a) $$K = \mathbb{R}^n_+ = \{x : x \geq 0\}$$  
b) $$K = \{(t, x) : \|x\|_2 \leq t\}$$ (nón bậc hai — second-order cone)  
c) $$K = \mathbb{S}^n_+$$ (nón ma trận nửa xác định dương)

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Nón không âm $$K = \mathbb{R}^n_+$$:**

Cần tìm các vector $$y$$ sao cho $$y^T x \geq 0$$ với mọi $$x \geq 0$$.

Chọn $$x = e_i$$ (vector cơ sở chuẩn thứ $$i$$):

$$
y^T e_i = y_i \geq 0
$$

Điều kiện này đúng với mọi $$i$$ khi và chỉ khi $$y \geq 0$$.

**Kết luận:** $$\boxed{K^* = \mathbb{R}^n_+}$$ (tự đối ngẫu).

---

**b) Nón bậc hai (Second-order cone):**

$$
K = \{(t, x) : t \in \mathbb{R}, x \in \mathbb{R}^{n-1}, \|x\|_2 \leq t\}
$$

Cần tìm $$(s, y)$$ sao cho:

$$
st + y^T x \geq 0, \quad \forall \|x\|_2 \leq t
$$

Xét trường hợp bất lợi nhất theo $$x$$ (với $$y \neq 0$$): chọn $$x = -\frac{t}{\|y\|_2} y$$ (thỏa $$\|x\|_2 = t$$), ta được:

$$
st - t\|y\|_2 = t(s - \|y\|_2) \geq 0
$$

Để bất đẳng thức đúng với mọi $$t > 0$$, điều kiện cần và đủ là $$s \geq \|y\|_2$$ (khi $$y = 0$$, điều kiện là $$s \geq 0$$, vẫn khớp).

**Kết luận:** $$\boxed{K^* = K}$$ (tự đối ngẫu).

---

**c) Nón ma trận nửa xác định dương $$K = \mathbb{S}^n_+$$:**

Cần tìm các ma trận đối xứng $$Y$$ sao cho:

$$
\text{tr}(Y X) \geq 0, \quad \forall X \succeq 0
$$

Sử dụng phân tích trị riêng $$X = \sum_i \lambda_i v_i v_i^T$$ với $$\lambda_i \geq 0$$:

$$
\text{tr}(Y X) = \sum_i \lambda_i v_i^T Y v_i \geq 0
$$

Điều này đúng với mọi $$\lambda_i \geq 0$$ và mọi vector $$v_i$$ khi và chỉ khi $$v^T Y v \geq 0$$ với mọi $$v$$, tức $$Y \succeq 0$$.

**Kết luận:** $$\boxed{K^* = \mathbb{S}^n_+}$$ (tự đối ngẫu).

</details>

---

### **Bài tập 7: Kiểm chứng tính chất nón bậc hai**

Cho $$x = (2, 1, 1)^T$$ và $$y = (1.5, 0.5, 0.5)^T$$.

**Yêu cầu:**
a) Kiểm tra $$x$$ có thuộc nón bậc hai (SOC) hay không  
b) Kiểm tra $$y$$ có thuộc SOC hay không  
c) Tính $$y^T x$$ và kiểm chứng tính chất nón đối ngẫu

<details>
<summary><strong>💡 Lời giải</strong></summary>

Xét nón bậc hai $$K = \{(t, u) \in \mathbb{R} \times \mathbb{R}^2 : \|u\|_2 \leq t\}$$.

---

**a) Kiểm tra $$x = (2, 1, 1)^T$$** (với $$t = 2$$, $$u = (1, 1)^T$$):

$$
\|(1, 1)\|_2 = \sqrt{2} \approx 1.414 \leq 2
$$

✓ Suy ra $$x \in K$$.

---

**b) Kiểm tra $$y = (1.5, 0.5, 0.5)^T$$:**

$$
\|(0.5, 0.5)\|_2 = \frac{\sqrt{2}}{2} \approx 0.707 \leq 1.5
$$

✓ Suy ra $$y \in K$$.

---

**c) Kiểm chứng tính chất nón đối ngẫu:**

Vì nón bậc hai tự đối ngẫu nên $$y \in K = K^*$$, do đó phải có $$y^T x \geq 0$$ với mọi $$x \in K$$. Tính trực tiếp:

$$
y^T x = 1.5 \times 2 + 0.5 \times 1 + 0.5 \times 1 = 3 + 0.5 + 0.5 = 4 \geq 0
$$

✓ Thỏa mãn.

</details>

---

## 📝 **Phần V: Đối ngẫu trong quy hoạch nửa xác định (SDP Duality)**

### **Bài tập 8: Cặp bài toán nguyên thủy–đối ngẫu SDP (Ben-Tal & Nemirovski, Ex. 4.3)**

Xét bài toán SDP nguyên thủy:

$$
\begin{align}
\min_{X} \quad & \text{tr}(C X) \\
\text{s.t.} \quad & \text{tr}(A_i X) = b_i, \quad i = 1, \ldots, m \\
& X \succeq 0
\end{align}
$$

**Yêu cầu:**  
a) Viết bài toán đối ngẫu  
b) Trình bày điều kiện đối ngẫu mạnh và hệ KKT  
c) Với $$C = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$, $$A_1 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$$, $$b_1 = 1$$, tìm nghiệm nguyên thủy và đối ngẫu

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Bài toán đối ngẫu:**

Hàm Lagrangian:

$$
L(X, y) = \text{tr}(CX) - \sum_i y_i (\text{tr}(A_i X) - b_i)
$$

$$
= \text{tr}\left( \left(C - \sum_i y_i A_i\right) X \right) + \sum_i y_i b_i
$$

Cực tiểu hóa theo $$X \succeq 0$$ (với $$M = C - \sum_i y_i A_i$$):

$$
\min_{X \succeq 0} \text{tr}(MX) = \begin{cases}
0 & \text{if } M \succeq 0 \\
-\infty & \text{otherwise}
\end{cases}
$$

**Bài toán đối ngẫu:**

$$
\boxed{
\begin{align}
\max_{y} \quad & \sum_i y_i b_i \\
\text{s.t.} \quad & C - \sum_i y_i A_i \succeq 0
\end{align}
}
$$

---

**b) Đối ngẫu mạnh và điều kiện KKT:**

Điều kiện Slater: tồn tại ma trận xác định dương $$\tilde{X} \succ 0$$ thỏa $$\text{tr}(A_i \tilde{X}) = b_i$$ với mọi $$i$$. Khi đó tính **đối ngẫu mạnh** được thỏa mãn ($$p^* = d^*$$) và tồn tại nghiệm tối ưu đối ngẫu.

**Các điều kiện KKT:**
1. Khả thi nguyên thủy: $$\text{tr}(A_i X^*) = b_i$$ và $$X^* \succeq 0$$.
2. Khả thi đối ngẫu: $$C - \sum_i y_i^* A_i \succeq 0$$.
3. Điều kiện bù yếu: $$\text{tr}((C - \sum_i y_i^* A_i) X^*) = 0$$.

---

**c) Giải với dữ liệu cụ thể:**

Cho:

$$
C = I_2, \quad A_1 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \quad b_1 = 1
$$

**Bài toán nguyên thủy:**

$$
\begin{align}
\min_{X} \quad & x_{11} + x_{22} \\
\text{s.t.} \quad & x_{11} = 1 \\
& X \succeq 0
\end{align}
$$

Từ $$x_{11} = 1$$ và $$X \succeq 0$$:

$$
X = \begin{bmatrix} 1 & x_{12} \\ x_{12} & x_{22} \end{bmatrix} \succeq 0
$$

Điều kiện nửa xác định dương cho $$\det(X) = x_{22} - x_{12}^2 \geq 0 \Rightarrow x_{22} \geq x_{12}^2 \geq 0$$.

Cực tiểu hóa $$1 + x_{22}$$ đạt được tại $$x_{22}^* = 0$$ và $$x_{12}^* = 0$$.

**Nghiệm nguyên thủy:**

$$
X^* = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \quad p^* = 1
$$

---

**Bài toán đối ngẫu:**

$$
\begin{align}
\max_{y_1} \quad & y_1 \\
\text{s.t.} \quad & I - y_1 \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \succeq 0
\end{align}
$$

$$
\begin{bmatrix} 1-y_1 & 0 \\ 0 & 1 \end{bmatrix} \succeq 0 \Rightarrow 1-y_1 \geq 0 \Rightarrow y_1 \leq 1
$$

Cực đại hóa $$y_1$$ cho $$y_1^* = 1$$ và $$d^* = 1$$.

**Kết luận:** $$p^* = d^* = 1$$, tính đối ngẫu mạnh được thỏa mãn ✓.

</details>

---

## 💡 **Tổng kết và chiến lược**

### **Chuẩn đối ngẫu**
- Ghi nhớ: $$(\|\cdot\|_p)_* = \|\cdot\|_q$$ với $$1/p + 1/q = 1$$.
- Cặp $$\ell_1 \leftrightarrow \ell_\infty$$; chuẩn $$\ell_2$$ tự đối ngẫu.
- Bất đẳng thức tổng quát: $$y^T x \leq \|y\|_* \|x\|$$.

### **Hàm liên hợp**
- Định nghĩa: $$f^*(y) = \sup_x (y^Tx - f(x))$$.
- Bất đẳng thức Fenchel: $$f(x) + f^*(y) \geq x^Ty$$ (dấu bằng khi $$y \in \partial f(x)$$).
- Tính đối hợp: $$f^{**} = f$$ nếu $$f$$ đóng và lồi.

### **Đối ngẫu của LASSO**
- Bài toán nguyên thủy: $$\min \frac{1}{2}\|Ax-b\|^2 + \lambda\|x\|_1$$.
- Bài toán đối ngẫu: $$\min \frac{1}{2}\|\nu\|^2 + \nu^Tb$$ với điều kiện $$\|A^T\nu\|_\infty \leq \lambda$$.
- Bài toán đối ngẫu có số chiều nhỏ hơn ($$m$$ biến so với $$n$$ biến) khi $$m < n$$.

### **Nón đối ngẫu**
- Định nghĩa: $$K^* = \{y : y^Tx \geq 0, \forall x \in K\}$$.
- Các nón tự đối ngẫu quan trọng: $$\mathbb{R}^n_+$$, nón bậc hai (SOC) và $$\mathbb{S}^n_+$$.
- Tính đối hợp: $$K^{**} = K$$ nếu $$K$$ là nón đóng và lồi.

### **Đối ngẫu trong SDP**
- Tính đối ngẫu mạnh được đảm bảo khi điều kiện Slater thỏa mãn.
- Điều kiện bù yếu có dạng: $$\text{tr}(MX) = 0$$ với $$M \succeq 0$$ và $$X \succeq 0$$.

---

## 📚 **Tài liệu tham khảo**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 3, 5, 6.

2. **Rockafellar, R. T.** (1970). *Convex Analysis*. Princeton University Press.

3. **Ben-Tal, A., & Nemirovski, A.** (2001). *Lectures on Modern Convex Optimization*. SIAM.

4. **Borwein, J. M., & Lewis, A. S.** (2006). *Convex Analysis and Nonlinear Optimization* (2nd ed.). Springer.

5. **Hiriart-Urruty, J.-B., & Lemaréchal, C.** (2001). *Fundamentals of Convex Analysis*. Springer.
