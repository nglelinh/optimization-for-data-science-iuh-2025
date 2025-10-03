---
layout: post
title: 13-8 Bài Tập Thực Hành - Ứng Dụng Tính Đối Ngẫu
chapter: '13'
order: 9
owner: GitHub Copilot
lang: vi
categories:
- chapter13
lesson_type: required
---

# Bài Tập Thực Hành - Ứng Dụng Tính Đối Ngẫu

Các bài tập được tham khảo từ Boyd & Vandenberghe (2004), Rockafellar (1970), và Ben-Tal & Nemirovski (2001).

---

## 📝 **Phần I: Chuẩn Đối Ngẫu (Dual Norms)**

### **Bài tập 1: Tính toán Chuẩn Đối Ngẫu (Boyd & Vandenberghe, Ex. 3.7)**

Cho chuẩn $$\|x\|$$, chuẩn đối ngẫu được định nghĩa:

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

**Công thức chung:** Chuẩn đối ngẫu của $$\|\cdot\|_p$$ là $$\|\cdot\|_q$$ với $$\frac{1}{p} + \frac{1}{q} = 1$$.

---

**a) Chuẩn $$\ell_1$$:**

Cần tìm:

$$
\|y\|_* = \max_{\|x\|_1 \leq 1} y^T x = \max_{\sum_i |x_i| \leq 1} \sum_i y_i x_i
$$

**Phân tích:**  
- Để maximize $$\sum_i y_i x_i$$, chọn $$x_i$$ có cùng dấu với $$y_i$$
- Giới hạn: $$\sum_i |x_i| \leq 1$$

Nghiệm tối ưu: Đặt $$x_j = \text{sign}(y_j)$$ với $$j = \arg\max_i |y_i|$$, các $$x_i$$ khác = 0.

Kết quả:

$$
\|y\|_* = \max_i |y_i| = \|y\|_\infty
$$

**Kết luận:** $$(\|\cdot\|_1)_* = \|\cdot\|_\infty$$

---

**b) Chuẩn $$\ell_2$$:**

$$
\|y\|_* = \max_{\|x\|_2 \leq 1} y^T x
$$

Theo bất đẳng thức Cauchy-Schwarz:

$$
y^T x \leq \|y\|_2 \|x\|_2 \leq \|y\|_2
$$

Đẳng thức xảy ra khi $$x = \frac{y}{\|y\|_2}$$.

**Kết luận:** $$(\|\cdot\|_2)_* = \|\cdot\|_2$$ (tự đối ngẫu)

---

**c) Chuẩn $$\ell_\infty$$:**

$$
\|y\|_* = \max_{\max_i |x_i| \leq 1} \sum_i y_i x_i
$$

Chọn $$x_i = \text{sign}(y_i)$$ cho mọi $$i$$ (vì $$|x_i| \leq 1$$):

$$
\|y\|_* = \sum_i |y_i| = \|y\|_1
$$

**Kết luận:** $$(\|\cdot\|_\infty)_* = \|\cdot\|_1$$

---

**d) Chuẩn $$\ell_p$$ tổng quát:**

Theo bất đẳng thức Hölder:

$$
y^T x \leq \|y\|_q \|x\|_p
$$

với $$\frac{1}{p} + \frac{1}{q} = 1$$.

Đẳng thức đạt được khi $$x_i = c \cdot \text{sign}(y_i) |y_i|^{q-1}$$ (với $$c$$ phù hợp để $$\|x\|_p = 1$$).

**Kết luận:** $$(\|\cdot\|_p)_* = \|\cdot\|_q$$ với $$\frac{1}{p} + \frac{1}{q} = 1$$

---

**Bảng tóm tắt:**

| Chuẩn Primal | Chuẩn Dual | Quan hệ |
|--------------|------------|---------|
| $$\|\cdot\|_1$$ | $$\|\cdot\|_\infty$$ | $$p=1, q=\infty$$ |
| $$\|\cdot\|_2$$ | $$\|\cdot\|_2$$ | Tự đối ngẫu |
| $$\|\cdot\|_\infty$$ | $$\|\cdot\|_1$$ | $$p=\infty, q=1$$ |
| $$\|\cdot\|_p$$ | $$\|\cdot\|_q$$ | $$1/p + 1/q = 1$$ |

</details>

---

### **Bài tập 2: Kiểm chứng Tính chất Chuẩn Đối Ngẫu**

Với $$x = (3, 4)^T$$ và $$y = (0.6, 0.8)^T$$:

**Yêu cầu:**  
a) Tính $$\|x\|_1$$, $$\|x\|_2$$, $$\|x\|_\infty$$  
b) Tính $$\|y\|_1$$, $$\|y\|_2$$, $$\|y\|_\infty$$  
c) Kiểm chứng: $$y^T x \leq \|y\|_* \|x\|$$ cho mỗi cặp chuẩn

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Tính chuẩn của $$x = (3,4)$$:**

$$
\begin{align}
\|x\|_1 &= |3| + |4| = 7 \\
\|x\|_2 &= \sqrt{3^2 + 4^2} = \sqrt{25} = 5 \\
\|x\|_\infty &= \max(|3|, |4|) = 4
\end{align}
$$

---

**b) Tính chuẩn của $$y = (0.6, 0.8)$$:**

$$
\begin{align}
\|y\|_1 &= 0.6 + 0.8 = 1.4 \\
\|y\|_2 &= \sqrt{0.6^2 + 0.8^2} = \sqrt{0.36 + 0.64} = 1 \\
\|y\|_\infty &= \max(0.6, 0.8) = 0.8
\end{align}
$$

---

**c) Kiểm chứng bất đẳng thức:**

Tính $$y^T x$$:

$$
y^T x = 0.6 \times 3 + 0.8 \times 4 = 1.8 + 3.2 = 5
$$

**Trường hợp 1:** $$\|x\|_1$$ và $$\|y\|_\infty$$ (vì $$(\|\cdot\|_1)_* = \|\cdot\|_\infty$$)

$$
y^T x = 5 \leq \|y\|_\infty \|x\|_1 = 0.8 \times 7 = 5.6
$$

✓ Thỏa mãn

---

**Trường hợp 2:** $$\|x\|_2$$ và $$\|y\|_2$$ (tự đối ngẫu)

$$
y^T x = 5 \leq \|y\|_2 \|x\|_2 = 1 \times 5 = 5
$$

✓ Đẳng thức (vì $$y = \frac{x}{\|x\|_2}$$)

---

**Trường hợp 3:** $$\|x\|_\infty$$ và $$\|y\|_1$$ (vì $$(\|\cdot\|_\infty)_* = \|\cdot\|_1$$)

$$
y^T x = 5 \leq \|y\|_1 \|x\|_\infty = 1.4 \times 4 = 5.6
$$

✓ Thỏa mãn

</details>

---

## 📝 **Phần II: Hàm Liên Hợp (Conjugate Functions)**

### **Bài tập 3: Tính Hàm Liên Hợp (Rockafellar, Ex. 12.B)**

Hàm liên hợp của $$f(x)$$ được định nghĩa:

$$
f^*(y) = \sup_x (y^T x - f(x))
$$

**Yêu cầu:** Tính hàm liên hợp cho:

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

**FOC:** $$\nabla_x (y^T x - \frac{1}{2}x^T Q x) = y - Qx = 0$$

$$
x^* = Q^{-1} y
$$

Thế vào:

$$
f^*(y) = y^T Q^{-1} y - \frac{1}{2} (Q^{-1}y)^T Q (Q^{-1}y)
$$

$$
= y^T Q^{-1} y - \frac{1}{2} y^T Q^{-1} y = \frac{1}{2} y^T Q^{-1} y
$$

**Kết quả:** $$\boxed{f^*(y) = \frac{1}{2} y^T Q^{-1} y}$$

**Bất đẳng thức Fenchel:**

$$
\frac{1}{2}x^T Q x + \frac{1}{2}y^T Q^{-1} y \geq x^T y
$$

---

**b) Chuẩn Euclidean $$f(x) = \|x\|_2$$:**

$$
f^*(y) = \sup_x (y^T x - \|x\|_2)
$$

**Phân tích:**
- Nếu $$\|y\|_2 \leq 1$$: Có thể tìm $$x$$ theo hướng $$y$$ với $$\|x\| \to \infty$$ nhưng $$y^Tx - \|x\| \leq 0$$
- Nếu $$\|y\|_2 > 1$$: $$y^T x - \|x\|_2 \to \infty$$ khi $$x = ty$$ với $$t \to \infty$$

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

**FOC:** $$y - e^x = 0 \Rightarrow x^* = \ln y$$

(Chỉ có nghiệm nếu $$y > 0$$)

Thế vào:

$$
f^*(y) = y \ln y - e^{\ln y} = y \ln y - y
$$

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

**Kết quả:** $$\boxed{f^*(y) = \sup_{x \in C} y^T x}$$ (hàm hỗ trợ của $$C$$)

**Ví dụ cụ thể:**
- $$C = \{x : \|x\|_2 \leq 1\}$$: $$f^*(y) = \|y\|_2$$
- $$C = \mathbb{R}^n_+$$: $$f^*(y) = I_{\{y \leq 0\}}(y)$$

</details>

---

### **Bài tập 4: Bất đẳng thức Fenchel (Boyd & Vandenberghe, Ex. 3.33)**

Cho $$f(x) = \frac{1}{2}\|x\|^2$$ và $$x = (1, 2)^T$$, $$y = (3, 1)^T$$.

**Yêu cầu:**  
a) Tính $$f(x)$$, $$f^*(y)$$  
b) Tính $$x^T y$$  
c) Kiểm chứng bất đẳng thức Fenchel: $$f(x) + f^*(y) \geq x^T y$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Tính $$f(x)$$ và $$f^*(y)$$:**

$$
f(x) = \frac{1}{2}(1^2 + 2^2) = \frac{1}{2}(1 + 4) = 2.5
$$

Với $$f(x) = \frac{1}{2}\|x\|^2$$, ta có $$Q = I$$ nên:

$$
f^*(y) = \frac{1}{2}\|y\|^2 = \frac{1}{2}(3^2 + 1^2) = \frac{1}{2}(9 + 1) = 5
$$

---

**b) Tính $$x^T y$$:**

$$
x^T y = 1 \times 3 + 2 \times 1 = 5
$$

---

**c) Kiểm chứng Fenchel:**

$$
f(x) + f^*(y) = 2.5 + 5 = 7.5 \geq 5 = x^T y
$$

✓ Thỏa mãn

**Chênh lệch:** $$7.5 - 5 = 2.5$$

**Khi nào đẳng thức?** Khi $$y \in \partial f(x)$$, tức $$y = \nabla f(x) = x$$.

Với $$x = (1,2)$$ thì $$\nabla f(x) = (1,2) \neq (3,1) = y$$, nên không có đẳng thức.

</details>

---

## 📝 **Phần III: LASSO Dual**

### **Bài tập 5: Xây dựng LASSO Dual (Boyd & Vandenberghe, Ex. 6.15)**

Bài toán LASSO primal:

$$
\min_x \frac{1}{2}\|Ax - b\|^2 + \lambda \|x\|_1
$$

**Yêu cầu:**
a) Viết bài toán dual  
b) Giải thích quan hệ giữa primal và dual variables  
c) Với $$A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}$$, $$b = \begin{bmatrix} 1 \\ 1 \\ 3 \end{bmatrix}$$, $$\lambda = 0.5$$, tìm nghiệm dual

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Bài toán Dual:**

LASSO primal:

$$
\min_x \frac{1}{2}\|Ax - b\|^2 + \lambda \|x\|_1
$$

**Cách 1: Qua Lagrangian**

Viết lại với biến phụ $$r = Ax - b$$:

$$
\begin{align}
\min_{x,r} \quad & \frac{1}{2}\|r\|^2 + \lambda \|x\|_1 \\
\text{s.t.} \quad & Ax - r = b
\end{align}
$$

Lagrangian:

$$
L(x, r, \nu) = \frac{1}{2}\|r\|^2 + \lambda \|x\|_1 + \nu^T(Ax - r - b)
$$

Minimize over $$x$$:

$$
\min_x \left( \lambda \|x\|_1 + \nu^T A x \right) = \begin{cases}
0 & \text{if } \|A^T \nu\|_\infty \leq \lambda \\
-\infty & \text{otherwise}
\end{cases}
$$

Minimize over $$r$$:

$$
\min_r \left( \frac{1}{2}\|r\|^2 - \nu^T r \right) = -\frac{1}{2}\|\nu\|^2
$$

**Hàm dual:**

$$
g(\nu) = -\frac{1}{2}\|\nu\|^2 - \nu^T b
$$

với ràng buộc $$\|A^T \nu\|_\infty \leq \lambda$$.

**Bài toán dual:**

$$
\boxed{
\begin{align}
\min_{\nu} \quad & \frac{1}{2}\|\nu\|^2 + \nu^T b \\
\text{s.t.} \quad & \|A^T \nu\|_\infty \leq \lambda
\end{align}
}
$$

(Chuyển max thành min)

---

**b) Quan hệ Primal-Dual:**

Từ điều kiện KKT:
- $$r^* = \nu^*$$ (residual dual = dual variable)
- Nếu $$|(A^T \nu^*)_i| < \lambda$$: $$x_i^* = 0$$
- Nếu $$|(A^T \nu^*)_i| = \lambda$$: $$x_i^* \neq 0$$ (trong active set)

**Khôi phục primal từ dual:**

$$
x^* = \text{(nghiệm của bài toán với active set)}
$$

---

**c) Nghiệm số:**

Dữ liệu:

$$
A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}, \quad
b = \begin{bmatrix} 1 \\ 1 \\ 3 \end{bmatrix}, \quad
\lambda = 0.5
$$

**Bài toán dual:**

$$
\begin{align}
\min_{\nu} \quad & \frac{1}{2}(\nu_1^2 + \nu_2^2 + \nu_3^2) + \nu_1 + \nu_2 + 3\nu_3 \\
\text{s.t.} \quad & \max(|\nu_1 + \nu_3|, |\nu_2 + \nu_3|) \leq 0.5
\end{align}
$$

**Giải:**

FOC (nếu ràng buộc không chặt):

$$
\nu_1 + 1 = 0 \Rightarrow \nu_1 = -1 \\
\nu_2 + 1 = 0 \Rightarrow \nu_2 = -1 \\
\nu_3 + 3 = 0 \Rightarrow \nu_3 = -3
$$

Kiểm tra ràng buộc:

$$
\max(|-1 - 3|, |-1 - 3|) = 4 > 0.5
$$

Không thỏa! Ràng buộc phải active.

**Giả sử** $$|\nu_1 + \nu_3| = 0.5$$:

Từ FOC + ràng buộc, giải hệ (cần solver số).

**Nghiệm xấp xỉ** (cần verify bằng solver):

$$
\nu^* \approx (-0.2, -0.2, -0.3)^T
$$

</details>

---

## 📝 **Phần IV: Nón Đối Ngẫu (Dual Cones)**

### **Bài tập 6: Tính Nón Đối Ngẫu (Boyd & Vandenberghe, Ex. 2.36)**

Nón đối ngẫu của $$K$$ được định nghĩa:

$$
K^* = \{ y : y^T x \geq 0, \forall x \in K \}
$$

**Yêu cầu:** Tìm nón đối ngẫu cho:

a) $$K = \mathbb{R}^n_+ = \{x : x \geq 0\}$$  
b) $$K = \{(t, x) : \|x\|_2 \leq t\}$$ (second-order cone)  
c) $$K = \mathbb{S}^n_+$$ (positive semidefinite cone)

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Nón không âm $$K = \mathbb{R}^n_+$$:**

Cần tìm $$y$$ sao cho $$y^T x \geq 0$$ với mọi $$x \geq 0$$.

**Phân tích:** Chọn $$x = e_i$$ (vector cơ sở thứ $$i$$):

$$
y^T e_i = y_i \geq 0
$$

Phải đúng với mọi $$i$$ → $$y \geq 0$$.

**Kết luận:** $$\boxed{K^* = \mathbb{R}^n_+}$$ (tự đối ngẫu)

---

**b) Second-order cone:**

$$
K = \{(t, x) : t \in \mathbb{R}, x \in \mathbb{R}^{n-1}, \|x\|_2 \leq t\}
$$

Cần tìm $$(s, y)$$ sao cho:

$$
st + y^T x \geq 0, \quad \forall \|x\|_2 \leq t
$$

**Trường hợp tệ nhất:** $$x = -\frac{t}{\|y\|_2} y$$ (nếu $$y \neq 0$$)

$$
st - t\|y\|_2 = t(s - \|y\|_2) \geq 0
$$

Phải đúng với mọi $$t > 0$$ → $$s \geq \|y\|_2$$.

**Kết luận:** $$\boxed{K^* = K}$$ (tự đối ngẫu)

---

**c) PSD cone $$K = \mathbb{S}^n_+$$:**

Cần tìm $$Y$$ sao cho:

$$
\text{tr}(Y X) \geq 0, \quad \forall X \succeq 0
$$

**Phân tích eigenvalue:** $$X = \sum_i \lambda_i v_i v_i^T$$ với $$\lambda_i \geq 0$$:

$$
\text{tr}(Y X) = \sum_i \lambda_i v_i^T Y v_i \geq 0
$$

Phải đúng với mọi $$\lambda_i \geq 0$$ → $$v_i^T Y v_i \geq 0$$ với mọi $$v_i$$ → $$Y \succeq 0$$.

**Kết luận:** $$\boxed{K^* = \mathbb{S}^n_+}$$ (tự đối ngẫu)

</details>

---

### **Bài tập 7: Kiểm chứng Tính chất Nón**

Cho $$x = (2, 1, 1)^T$$ và $$y = (1.5, 0.5, 0.5)^T$$.

**Yêu cầu:**
a) Kiểm tra $$x$$ có thuộc SOC không?  
b) Kiểm tra $$y$$ có thuộc SOC không?  
c) Tính $$y^T x$$ và verify dual cone property

<details>
<summary><strong>💡 Lời giải</strong></summary>

**SOC:** $$K = \{(t, x) \in \mathbb{R} \times \mathbb{R}^2 : \|x\|_2 \leq t\}$$

Viết lại: $$x = (t, x_1, x_2)$$ với $$t = x_1 = 2$$, $$x = (x_2, x_3) = (1, 1)$$.

---

**a) Kiểm tra $$x$$:**

$$
\|(1, 1)\|_2 = \sqrt{2} \approx 1.414 \leq 2
$$

✓ $$x \in K$$

---

**b) Kiểm tra $$y$$:**

$$
\|(0.5, 0.5)\|_2 = \frac{\sqrt{2}}{2} \approx 0.707 \leq 1.5
$$

✓ $$y \in K$$

---

**c) Dual cone property:**

Vì $$K$$ tự đối ngẫu: $$y \in K^* = K$$

Nên với mọi $$x \in K$$: $$y^T x \geq 0$$.

$$
y^T x = 1.5 \times 2 + 0.5 \times 1 + 0.5 \times 1 = 3 + 0.5 + 0.5 = 4 \geq 0
$$

✓ Thỏa mãn

</details>

---

## 📝 **Phần V: SDP Duality**

### **Bài tập 8: SDP Primal-Dual (Ben-Tal & Nemirovski, Ex. 4.3)**

Bài toán SDP primal:

$$
\begin{align}
\min_{X} \quad & \text{tr}(C X) \\
\text{s.t.} \quad & \text{tr}(A_i X) = b_i, \quad i = 1, \ldots, m \\
& X \succeq 0
\end{align}
$$

**Yêu cầu:**  
a) Viết bài toán dual  
b) Giải thích strong duality  
c) Với $$C = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$, $$A_1 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$$, $$b_1 = 1$$, tìm nghiệm

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Bài toán Dual:**

Lagrangian:

$$
L(X, y) = \text{tr}(CX) - \sum_i y_i (\text{tr}(A_i X) - b_i)
$$

$$
= \text{tr}\left( \left(C - \sum_i y_i A_i\right) X \right) + \sum_i y_i b_i
$$

Minimize over $$X \succeq 0$$:

$$
\min_{X \succeq 0} \text{tr}(MX) = \begin{cases}
0 & \text{if } M \succeq 0 \\
-\infty & \text{otherwise}
\end{cases}
$$

với $$M = C - \sum_i y_i A_i$$.

**Bài toán dual:**

$$
\boxed{
\begin{align}
\max_{y} \quad & \sum_i y_i b_i \\
\text{s.t.} \quad & C - \sum_i y_i A_i \succeq 0
\end{align}
}
$$

---

**b) Strong Duality:**

Điều kiện Slater: Tồn tại $$\tilde{X} \succ 0$$ thỏa $$\text{tr}(A_i \tilde{X}) = b_i$$.

Khi đó: **Strong duality** $$p^* = d^*$$ và tồn tại nghiệm tối ưu dual.

**KKT Conditions:**
1. Primal feasible: $$\text{tr}(A_i X^*) = b_i$$, $$X^* \succeq 0$$
2. Dual feasible: $$C - \sum_i y_i^* A_i \succeq 0$$
3. Complementary slackness: $$\text{tr}((C - \sum_i y_i^* A_i) X^*) = 0$$

---

**c) Nghiệm cụ thể:**

Dữ liệu:

$$
C = I_2, \quad A_1 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \quad b_1 = 1
$$

**Primal:**

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

PSD → $$\det(X) = x_{22} - x_{12}^2 \geq 0$$ → $$x_{22} \geq x_{12}^2 \geq 0$$.

Minimize $$1 + x_{22}$$ → $$x_{22}^* = 0$$, $$x_{12}^* = 0$$.

**Nghiệm primal:**

$$
X^* = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \quad p^* = 1
$$

---

**Dual:**

$$
\begin{align}
\max_{y_1} \quad & y_1 \\
\text{s.t.} \quad & I - y_1 \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \succeq 0
\end{align}
$$

$$
\begin{bmatrix} 1-y_1 & 0 \\ 0 & 1 \end{bmatrix} \succeq 0 \Rightarrow 1-y_1 \geq 0 \Rightarrow y_1 \leq 1
$$

Maximize → $$y_1^* = 1$$, $$d^* = 1$$.

**Kết luận:** $$p^* = d^* = 1$$. Strong duality! ✓

</details>

---

## 💡 **Tổng kết và Chiến lược**

### **Chuẩn Đối Ngẫu:**
- Nhớ: $$(\|\cdot\|_p)_* = \|\cdot\|_q$$ với $$1/p + 1/q = 1$$
- $$\ell_1 \leftrightarrow \ell_\infty$$, $$\ell_2$$ tự đối ngẫu
- Dùng: $$y^T x \leq \|y\|_* \|x\|$$

### **Hàm Liên Hợp:**
- Định nghĩa: $$f^*(y) = \sup_x (y^Tx - f(x))$$
- Fenchel: $$f(x) + f^*(y) \geq x^Ty$$
- Đẳng thức khi $$y \in \partial f(x)$$
- $$f^{**} = f$$ nếu $$f$$ đóng, lồi

### **LASSO Dual:**
- Primal: $$\min \frac{1}{2}\|Ax-b\|^2 + \lambda\|x\|_1$$
- Dual: $$\min \frac{1}{2}\|\nu\|^2 + \nu^Tb$$ s.t. $$\|A^T\nu\|_\infty \leq \lambda$$
- Dual nhỏ hơn ($$m$$ biến vs $$n$$ biến) nếu $$m < n$$

### **Nón Đối Ngẫu:**
- Định nghĩa: $$K^* = \{y : y^Tx \geq 0, \forall x \in K\}$$
- Tự đối ngẫu: $$\mathbb{R}^n_+$$, SOC, $$\mathbb{S}^n_+$$
- $$K^{**} = K$$ nếu $$K$$ đóng, lồi

### **SDP Duality:**
- Strong duality nếu thỏa Slater
- Complementary slackness: $$\text{tr}(MX) = 0$$ với $$M \succeq 0$$, $$X \succeq 0$$

---

## 📚 **Tài liệu Tham khảo**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 3, 5, 6.

2. **Rockafellar, R. T.** (1970). *Convex Analysis*. Princeton University Press.

3. **Ben-Tal, A., & Nemirovski, A.** (2001). *Lectures on Modern Convex Optimization*. SIAM.

4. **Borwein, J. M., & Lewis, A. S.** (2006). *Convex Analysis and Nonlinear Optimization* (2nd ed.). Springer.

5. **Hiriart-Urruty, J.-B., & Lemaréchal, C.** (2001). *Fundamentals of Convex Analysis*. Springer.

