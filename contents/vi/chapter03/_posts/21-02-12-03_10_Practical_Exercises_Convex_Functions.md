---
layout: post
title: 03-10 Bài Tập Thực Hành - Hàm Convex
chapter: '3'
order: 18
owner: GitHub Copilot
lang: vi
categories:
- chapter03
lesson_type: required
redirect_from:
  - /contents/vi/chapter03/03_09_Practical_Exercises_Convex_Functions/
---

# Bài tập thực hành - Hàm lồi

## 📝 **Bài tập 1: Kiểm tra tính lồi của hàm số**

**Đề bài:** (Bài 3.1 từ Boyd & Vandenberghe)
Xác định tính lồi của các hàm sau trên miền xác định tương ứng:

a) $$f(x) = x^2$$ trên $$\mathbb{R}$$

b) $$f(x) = e^{ax}$$ trên $$\mathbb{R}$$

c) $$f(x) = x \log x$$ trên $$\mathbb{R}_{++}$$

d) $$f(x) = -\log x$$ trên $$\mathbb{R}_{++}$$

e) $$f(x) = x^p$$ với $$p \geq 1$$ trên $$\mathbb{R}_+$$

f) $$f(x) = |x|^p$$ với $$p \geq 1$$ trên $$\mathbb{R}$$

**Yêu cầu:**
1. Kiểm tra bằng định nghĩa hàm lồi
2. Dùng điều kiện bậc hai khi hàm khả vi hai lần
3. Phân tích điều kiện của miền xác định
4. Minh họa đồ thị và tính lồi của các hàm

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: $$f(x) = x^2$$**

**Điều kiện bậc hai:** $$f''(x) = 2 > 0$$ với mọi $$x \in \mathbb{R}$$ $$\Rightarrow$$ lồi chặt trên $$\mathbb{R}$$.

**Kiểm tra bằng định nghĩa:**
$$f(\theta x + (1-\theta) y) = (\theta x + (1-\theta) y)^2 = \theta^2 x^2 + 2\theta(1-\theta)xy + (1-\theta)^2 y^2$$

$$\theta f(x) + (1-\theta) f(y) = \theta x^2 + (1-\theta) y^2$$

$$f(\theta x + (1-\theta) y) - [\theta f(x) + (1-\theta) f(y)] = -\theta(1-\theta)(x-y)^2 \leq 0$$

**Bước 2: $$f(x) = e^{ax}$$**

**Điều kiện bậc hai:** $$f''(x) = a^2 e^{ax} \geq 0$$ với mọi $$x \in \mathbb{R}$$ $$\Rightarrow$$ lồi trên $$\mathbb{R}$$ (lồi chặt khi $$a \neq 0$$).

**Bước 3: $$f(x) = x \log x$$**

**Miền xác định:** $$\mathbb{R}_{++}$$ ($$x > 0$$).

**Đạo hàm:** $$f'(x) = \log x + 1$$, $$f''(x) = \frac{1}{x} > 0$$ với $$x > 0$$ $$\Rightarrow$$ lồi chặt trên $$\mathbb{R}_{++}$$.

**Bước 4: $$f(x) = -\log x$$**

**Đạo hàm bậc hai:** $$f''(x) = \frac{1}{x^2} > 0$$ với $$x > 0$$ $$\Rightarrow$$ lồi chặt trên $$\mathbb{R}_{++}$$.

**Bước 5: $$f(x) = x^p$$ với $$p \geq 1$$**

- **Khi $$p = 1$$:** $$f(x) = x$$ là hàm tuyến tính $$\Rightarrow$$ lồi.
- **Khi $$p > 1$$:** $$f''(x) = p(p-1)x^{p-2} \geq 0$$ với $$x > 0$$ (và liên tục tại $$0$$) $$\Rightarrow$$ lồi trên $$\mathbb{R}_+$$.

**Bước 6: $$f(x) = |x|^p$$ với $$p \geq 1$$**

Hàm có tính đối xứng $$f(-x) = f(x)$$, tuy nhiên lồi trên từng nửa trục chưa đủ để kết luận lồi trên toàn bộ $$\mathbb{R}$$. Lập luận chặt chẽ: viết $$f(x) = g(|x|)$$ với $$g(t) = t^p$$ là hàm lồi và **không giảm** trên $$\mathbb{R}_+$$, còn $$|x|$$ là hàm lồi trên $$\mathbb{R}$$. Theo quy tắc hợp thành, hợp thành của hàm lồi không giảm với hàm lồi là hàm lồi, nên $$|x|^p$$ lồi trên $$\mathbb{R}$$.

</details>

---

## 📝 **Bài tập 2: Các phép toán bảo toàn tính lồi**

**Đề bài:** (Bài 3.2 từ Boyd & Vandenberghe)
Cho các hàm lồi $$f, g: \mathbb{R}^n \to \mathbb{R}$$. Xét tính lồi của:

a) $$h(x) = \alpha f(x) + \beta g(x)$$ với $$\alpha, \beta \geq 0$$

b) $$h(x) = \max\{f(x), g(x)\}$$

c) $$h(x) = f(Ax + b)$$ với $$A \in \mathbb{R}^{n \times m}$$, $$b \in \mathbb{R}^n$$

d) $$h(x) = \inf_{y \in C} f(x, y)$$ với $$C$$ là tập lồi và $$f(x, y)$$ lồi đồng thời theo $$(x, y)$$

e) $$h(x) = \int_0^\infty f(x, t)\, dt$$ (khi tích phân tồn tại và $$f(x, t)$$ lồi theo $$x$$ với mọi $$t \ge 0$$)

**Yêu cầu:**
1. Chứng minh tính lồi cho từng phép toán
2. Nêu phản ví dụ khi bỏ đi các giả thiết cần thiết
3. Đưa ra ví dụ cụ thể minh họa
4. Phân tích điều kiện để thu được tính lồi chặt

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Tổng trọng số không âm — LỒI**

**Định lý:** Nếu $$f, g$$ lồi và $$\alpha, \beta \geq 0$$, thì $$h(x) = \alpha f(x) + \beta g(x)$$ lồi.

**Chứng minh:**
$$h(\theta x + (1-\theta) y) = \alpha f(\theta x + (1-\theta) y) + \beta g(\theta x + (1-\theta) y)$$
$$\leq \alpha[\theta f(x) + (1-\theta) f(y)] + \beta[\theta g(x) + (1-\theta) g(y)]$$
$$= \theta[\alpha f(x) + \beta g(x)] + (1-\theta)[\alpha f(y) + \beta g(y)]$$
$$= \theta h(x) + (1-\theta) h(y)$$

**Bước 2: Maximum theo điểm — LỒI**

**Định lý:** $$h(x) = \max\{f(x), g(x)\}$$ lồi nếu $$f, g$$ lồi.

**Chứng minh:**
$$h(\theta x + (1-\theta) y) = \max\{f(\theta x + (1-\theta) y), g(\theta x + (1-\theta) y)\}$$
$$\leq \max\{\theta f(x) + (1-\theta) f(y), \theta g(x) + (1-\theta) g(y)\}$$
$$\leq \theta \max\{f(x), g(x)\} + (1-\theta) \max\{f(y), g(y)\}$$
$$= \theta h(x) + (1-\theta) h(y)$$

**Tổng quát hóa:** $$\sup_{t \in T} f_t(x)$$ lồi nếu mỗi $$f_t$$ đều lồi.

**Bước 3: Hợp thành với ánh xạ affine — LỒI**

**Định lý:** $$h(x) = f(Ax + b)$$ lồi nếu $$f$$ lồi.

**Chứng minh:**
$$h(\theta x + (1-\theta) y) = f(A(\theta x + (1-\theta) y) + b)$$
$$= f(\theta(Ax + b) + (1-\theta)(Ay + b))$$
$$\leq \theta f(Ax + b) + (1-\theta) f(Ay + b)$$
$$= \theta h(x) + (1-\theta) h(y)$$

**Bước 4: Cực tiểu hóa từng phần — LỒI**

**Định lý:** $$h(x) = \inf_{y \in C} f(x, y)$$ lồi theo $$x$$ nếu $$f(x, y)$$ lồi đồng thời theo $$(x, y)$$ và $$C$$ là tập lồi.

**Chứng minh:** Với mọi $$\epsilon > 0$$, chọn $$y_1, y_2 \in C$$ sao cho $$f(x_k, y_k) \leq h(x_k) + \epsilon$$ ($$k = 1, 2$$). Vì $$C$$ lồi nên $$\bar{y} = \theta y_1 + (1-\theta) y_2 \in C$$, do đó:
$$h(\theta x_1 + (1-\theta) x_2) \leq f(\theta x_1 + (1-\theta) x_2, \bar{y})$$
$$\leq \theta f(x_1, y_1) + (1-\theta) f(x_2, y_2) \leq \theta h(x_1) + (1-\theta) h(x_2) + \epsilon$$
Cho $$\epsilon \to 0$$, ta thu được:
$$h(\theta x_1 + (1-\theta) x_2) \leq \theta h(x_1) + (1-\theta) h(x_2)$$
(Lưu ý: cần chọn hai điểm $$y_1, y_2$$ riêng biệt và dùng tính lồi **đồng thời** theo $$(x, y)$$; dùng chung một $$y$$ không đủ để chứng minh.)

**Bước 5: Tích phân — LỒI**

**Định lý:** $$h(x) = \int_0^\infty f(x, t)\, dt$$ lồi nếu $$f(x, t)$$ lồi theo $$x$$ với mọi $$t \ge 0$$.

**Chứng minh:** Với mỗi $$t \ge 0$$, $$f(\theta x + (1-\theta) y, t) \leq \theta f(x, t) + (1-\theta) f(y, t)$$. Lấy tích phân hai vế theo $$t$$ (tích phân có tính tuyến tính và bảo toàn bất đẳng thức), ta thu được $$h(\theta x + (1-\theta) y) \leq \theta h(x) + (1-\theta) h(y)$$.

</details>

---

## 📝 **Bài tập 3: Hàm liên hợp**

**Đề bài:** (Bài 3.3 từ Boyd & Vandenberghe)
Tính hàm liên hợp $$f^*(y) = \sup_x (y^T x - f(x))$$ cho các hàm sau:

a) $$f(x) = \frac{1}{2}x^T Q x$$ với $$Q \succ 0$$

b) $$f(x) = \lVert x \rVert_2$$

c) $$f(x) = \lVert x \rVert_1$$

d) $$f(x) = \log \sum_{i=1}^n e^{x_i}$$ (log-sum-exp)

e) $$f(x) = \max_{i=1,\ldots,n} x_i$$

**Yêu cầu:**
1. Tính hàm liên hợp bằng cách giải bài toán cực đại hóa
2. Kiểm tra các tính chất đối ngẫu liên hợp
3. Xác định miền xác định của từng hàm liên hợp
4. Giải thích ý nghĩa hình học

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Hàm bậc hai**
$$f(x) = \frac{1}{2}x^T Q x$$ với $$Q \succ 0$$

**Bài toán tối ưu:** $$\sup_x (y^T x - \frac{1}{2}x^T Q x)$$

**Điều kiện bậc nhất:** $$y - Qx = 0 \Rightarrow x^* = Q^{-1} y$$

**Hàm liên hợp:**
$$f^*(y) = y^T Q^{-1} y - \frac{1}{2}y^T Q^{-1} Q Q^{-1} y = \frac{1}{2}y^T Q^{-1} y$$

**Miền xác định:** $$\mathbb{R}^n$$ (do $$Q \succ 0$$).

**Bước 2: Chuẩn Euclidean**
$$f(x) = \lVert x \rVert_2$$

**Bài toán tối ưu:** $$\sup_x (y^T x - \lVert x \rVert_2)$$

**Phân tích các trường hợp:**
- Nếu $$\lVert y \rVert_2 \leq 1$$: theo bất đẳng thức Cauchy–Schwarz, $$y^T x - \lVert x \rVert_2 \leq (\lVert y \rVert_2 - 1)\lVert x \rVert_2 \leq 0$$, nên supremum bằng $$0$$ (đạt tại $$x = 0$$).
- Nếu $$\lVert y \rVert_2 > 1$$: chọn $$x = t y$$ với $$t \to +\infty$$, biểu thức tiến tới $$+\infty$$.

**Hàm liên hợp:**
$$f^*(y) = \begin{cases} 0 & \text{nếu } \lVert y \rVert_2 \leq 1 \\ +\infty & \text{nếu } \lVert y \rVert_2 > 1 \end{cases}$$

**Miền xác định:** Hình cầu đơn vị $$\{y : \lVert y \rVert_2 \leq 1\}$$.

**Bước 3: Chuẩn $$\ell_1$$**
$$f(x) = \lVert x \rVert_1 = \sum_{i=1}^n |x_i|$$

Bài toán tách rời theo từng tọa độ: $$\sup_{x_i} (y_i x_i - |x_i|)$$ cho mỗi $$i$$.
- Nếu $$|y_i| \leq 1$$: supremum bằng 0 (đạt tại $$x_i = 0$$).
- Nếu $$|y_i| > 1$$: supremum bằng $$+\infty$$.

**Hàm liên hợp:**
$$f^*(y) = \begin{cases} 0 & \text{nếu } \lVert y \rVert_\infty \leq 1 \\ +\infty & \text{nếu } \lVert y \rVert_\infty > 1 \end{cases}$$

**Bước 4: Hàm log-sum-exp**
$$f(x) = \log \sum_{i=1}^n e^{x_i}$$

**Bài toán tối ưu:** $$\sup_x \left(\sum_{i=1}^n y_i x_i - \log \sum_{i=1}^n e^{x_i}\right)$$

**Điều kiện bậc nhất:** $$y_i = \frac{e^{x_i}}{\sum_j e^{x_j}}$$, suy ra $$y$$ phải là vector xác suất ($$y \geq 0$$, $$\sum y_i = 1$$).

**Hàm liên hợp:** $$f^*(y) = \sum_{i=1}^n y_i \log y_i$$ (hàm entropy âm, với quy ước $$0 \log 0 = 0$$).

**Miền xác định:** Đơn hình xác suất $$\{y : y \geq 0, \sum y_i = 1\}$$.

**Bước 5: Hàm max**
$$f(x) = \max_{i=1,\ldots,n} x_i$$

**Hàm liên hợp:**
$$f^*(y) = \begin{cases} 0 & \text{nếu } y \geq 0, \sum y_i = 1 \\ +\infty & \text{trường hợp khác} \end{cases}$$

**Miền xác định:** Đơn hình xác suất.

</details>

---

## 📝 **Bài tập 4: Dưới vi phân và điều kiện tối ưu**

**Đề bài:** (Bài 3.4 từ Boyd & Vandenberghe)
Tính tập dưới vi phân $$\partial f(x) = \{g : f(y) \geq f(x) + g^T(y - x), \forall y\}$$ cho:

a) $$f(x) = |x|$$

b) $$f(x) = \max\{0, x\}$$ (hàm ReLU)

c) $$f(x) = \lVert x \rVert_1$$

d) $$f(x) = \lVert x \rVert_2$$

**Yêu cầu:**
1. Tính tường minh các tập dưới vi phân
2. Kiểm tra điều kiện tối ưu $$0 \in \partial f(x^*)$$
3. Phân tích tại các điểm không khả vi
4. Áp dụng vào bài toán tối ưu

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Giá trị tuyệt đối $$f(x) = |x|$$**

- **Khi $$x > 0$$:** $$f$$ khả vi, $$\partial f(x) = \{1\}$$.
- **Khi $$x < 0$$:** $$f$$ khả vi, $$\partial f(x) = \{-1\}$$.
- **Khi $$x = 0$$:** Điểm không khả vi. Điều kiện $$\partial f(0) = \{g : |y| \geq g \cdot y, \forall y\}$$ tương đương $$|g| \leq 1$$, suy ra $$\partial f(0) = [-1, 1]$$.

**Bước 2: Hàm ReLU $$f(x) = \max\{0, x\}$$**

- **Khi $$x > 0$$:** $$f(x) = x$$, $$\partial f(x) = \{1\}$$.
- **Khi $$x < 0$$:** $$f(x) = 0$$, $$\partial f(x) = \{0\}$$.
- **Khi $$x = 0$$:** $$\partial f(0) = \{g : \max\{0, y\} \geq g \cdot y, \forall y\}$$.
  - Với $$y > 0$$: $$y \geq g \cdot y \Rightarrow g \leq 1$$.
  - Với $$y < 0$$: $$0 \geq g \cdot y \Rightarrow g \geq 0$$.
  - Suy ra $$\partial f(0) = [0, 1]$$.

**Bước 3: Chuẩn $$\ell_1$$ $$f(x) = \lVert x \rVert_1$$**

Viết $$f(x) = \sum_{i=1}^n |x_i|$$. Vì hàm tách rời theo từng tọa độ nên:
$$\partial f(x) = \partial f_1(x_1) \times \cdots \times \partial f_n(x_n)$$

với $$\partial f_i(x_i) = \begin{cases} \{1\} & \text{nếu } x_i > 0 \\ \{-1\} & \text{nếu } x_i < 0 \\ [-1, 1] & \text{nếu } x_i = 0 \end{cases}$$

Tóm lại: $$\partial f(x) = \{g : g_i = \text{sign}(x_i) \text{ nếu } x_i \neq 0,\; |g_i| \leq 1 \text{ nếu } x_i = 0\}$$.

**Bước 4: Chuẩn Euclidean $$f(x) = \lVert x \rVert_2$$**

- **Khi $$x \neq 0$$:** $$f$$ khả vi, $$\partial f(x) = \left\{\frac{x}{\lVert x \rVert_2}\right\}$$.
- **Khi $$x = 0$$:** $$\partial f(0) = \{g : \lVert y \rVert_2 \geq g^T y, \forall y\}$$. Theo bất đẳng thức Cauchy–Schwarz, điều kiện này tương đương $$\lVert g \rVert_2 \leq 1$$, nên $$\partial f(0) = \{g : \lVert g \rVert_2 \leq 1\}$$ (hình cầu đơn vị).

</details>

---

## 📝 **Bài tập 5: Bất đẳng thức Jensen và ứng dụng**

**Đề bài:** (Bài 3.5 từ Boyd & Vandenberghe)
a) Chứng minh bất đẳng thức Jensen: Nếu $$f$$ là hàm lồi, $$\lambda_i \geq 0$$ và $$\sum_{i=1}^n \lambda_i = 1$$, thì:
$$f\left(\sum_{i=1}^n \lambda_i x_i\right) \leq \sum_{i=1}^n \lambda_i f(x_i)$$

b) Áp dụng bất đẳng thức Jensen để chứng minh:
   - Bất đẳng thức trung bình cộng – trung bình nhân (AM–GM): $$\frac{x_1 + \cdots + x_n}{n} \geq \sqrt[n]{x_1 \cdots x_n}$$ (với $$x_i > 0$$)
   - Bất đẳng thức Hölder: $$\sum_{i=1}^n |x_i y_i| \leq \left(\sum_{i=1}^n |x_i|^p\right)^{1/p} \left(\sum_{i=1}^n |y_i|^q\right)^{1/q}$$ (với $$p, q > 1, \frac{1}{p} + \frac{1}{q} = 1$$)

c) Suy ra bất đẳng thức log-sum

**Yêu cầu:**
1. Chứng minh chặt chẽ bằng quy nạp
2. Giải thích ý nghĩa hình học
3. Nêu ứng dụng trong lý thuyết xác suất
4. Mở rộng sang trường hợp liên tục

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Chứng minh bất đẳng thức Jensen**

**Trường hợp cơ sở ($$n = 2$$):** Chính là định nghĩa hàm lồi.

**Bước quy nạp:** Giả sử bất đẳng thức đúng với $$n-1$$ điểm, ta chứng minh cho $$n$$ điểm. Nếu $$\lambda_n = 1$$ thì các $$\lambda_i = 0$$ ($$i < n$$) nên bất đẳng thức hiển nhiên đúng. Ngược lại, đặt $$\mu = \sum_{i=1}^{n-1} \lambda_i = 1 - \lambda_n > 0$$:

$$f\left(\sum_{i=1}^n \lambda_i x_i\right) = f\left(\mu \cdot \frac{\sum_{i=1}^{n-1} \lambda_i x_i}{\mu} + (1-\mu) x_n\right)$$

Theo tính lồi của $$f$$:
$$\leq \mu f\left(\frac{\sum_{i=1}^{n-1} \lambda_i x_i}{\mu}\right) + (1-\mu) f(x_n)$$

Theo giả thiết quy nạp:
$$\leq \mu \sum_{i=1}^{n-1} \frac{\lambda_i}{\mu} f(x_i) + \lambda_n f(x_n) = \sum_{i=1}^n \lambda_i f(x_i)$$

**Bước 2: Bất đẳng thức AM–GM**

Xét hàm lồi $$f(x) = -\log x$$ trên $$\mathbb{R}_{++}$$ với các trọng số bằng nhau $$\lambda_i = \frac{1}{n}$$:

$$-\log\left(\frac{x_1 + \cdots + x_n}{n}\right) \leq \frac{1}{n}\sum_{i=1}^n (-\log x_i) = -\frac{1}{n}\log(x_1 \cdots x_n)$$

Đổi dấu hai vế và lấy hàm mũ:
$$\log\left(\frac{x_1 + \cdots + x_n}{n}\right) \geq \log\sqrt[n]{x_1 \cdots x_n} \Rightarrow \frac{x_1 + \cdots + x_n}{n} \geq \sqrt[n]{x_1 \cdots x_n}$$

**Bước 3: Bất đẳng thức Hölder**

Với hai số mũ liên hợp $$\frac{1}{p} + \frac{1}{q} = 1$$ ($$p, q > 1$$), áp dụng bất đẳng thức Jensen cho hàm lồi $$f(t) = e^t$$ với trọng số $$\frac{1}{p}$$ và $$\frac{1}{q}$$ thu được **bất đẳng thức Young** cho mọi $$a, b > 0$$:
$$ab = e^{\frac{1}{p}\log a^p + \frac{1}{q}\log b^q} \leq \frac{1}{p}a^p + \frac{1}{q}b^q$$

Chuẩn hóa bằng cách đặt $$a_i = \frac{|x_i|}{\lVert x \rVert_p}$$ và $$b_i = \frac{|y_i|}{\lVert y \rVert_q}$$ rồi cộng theo $$i$$:
$$\sum_i a_i b_i \leq \frac{1}{p}\sum_i a_i^p + \frac{1}{q}\sum_i b_i^q = \frac{1}{p} + \frac{1}{q} = 1$$
hay tương đương:
$$\sum |x_i y_i| \leq \left(\sum |x_i|^p\right)^{1/p} \left(\sum |y_i|^q\right)^{1/q}$$

**Bước 4: Bất đẳng thức log-sum**

**Phát biểu:** Với mọi $$a_i, b_i > 0$$:
$$\sum_{i=1}^n a_i \log \frac{a_i}{b_i} \geq \left(\sum_{i=1}^n a_i\right) \log \frac{\sum_{i=1}^n a_i}{\sum_{i=1}^n b_i}$$

**Chứng minh:** Áp dụng bất đẳng thức Jensen cho hàm lồi $$f(t) = t \log t$$ tại các điểm $$t_i = \frac{a_i}{b_i}$$ với các trọng số $$\lambda_i = \frac{b_i}{\sum_j b_j}$$.

</details>

---

## 📝 **Bài tập 6: Hàm giả lồi**

**Đề bài:** (Bài 3.6 từ Boyd & Vandenberghe)
a) Kiểm tra tính giả lồi của các hàm sau:
   - $$f(x) = \frac{x_1}{x_2}$$ trên $$\{x : x_2 > 0\}$$
   - $$f(x) = x_1^2 / x_2$$ trên $$\{x : x_2 > 0\}$$
   - $$f(x) = \log(x_1) - \log(x_2)$$ trên $$\mathbb{R}_{++}^2$$

b) Chứng minh $$f$$ giả lồi $$\Leftrightarrow$$ mọi tập mức dưới $$\{x \in \text{dom}f : f(x) \leq \alpha\}$$ đều là tập lồi

c) Nêu các phép toán bảo toàn tính giả lồi

**Yêu cầu:**
1. Kiểm tra bằng phương pháp phân tích tập mức dưới
2. Kiểm tra điều kiện bậc nhất
3. Phân tích các phép biến đổi đơn điệu
4. So sánh với tính lồi thông thường

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Hàm tỉ số $$f(x) = \frac{x_1}{x_2}$$**

**Tập mức dưới:** $$S_\alpha = \{x : x_1 \leq \alpha x_2,\; x_2 > 0\} = \{x : x_1 - \alpha x_2 \leq 0,\; x_2 > 0\}$$.

Đây là giao của hai nửa không gian nên là tập lồi với mọi $$\alpha \in \mathbb{R}$$ $$\Rightarrow f$$ là hàm giả lồi.

**Bước 2: Hàm $$f(x) = \frac{x_1^2}{x_2}$$**

**Tập mức dưới:** $$S_\alpha = \{x : x_1^2 \leq \alpha x_2,\; x_2 > 0\}$$.
- **Với $$\alpha < 0$$:** $$S_\alpha = \emptyset$$ (tập rỗng, là tập lồi).
- **Với $$\alpha = 0$$:** $$S_0 = \{x : x_1 = 0,\; x_2 > 0\}$$ (một tia mở, là tập lồi).
- **Với $$\alpha > 0$$:** $$S_\alpha = \{x : |x_1| \leq \sqrt{\alpha x_2},\; x_2 > 0\}$$ là tập lồi (thực tế $$x_1^2/x_2$$ còn là hàm lồi, vì là hàm phối cảnh của $$x_1^2$$).

$$\Rightarrow f$$ là hàm giả lồi.

**Bước 3: Hiệu logarithm $$f(x) = \log x_1 - \log x_2$$**

Viết lại thành $$f(x) = \log\left(\frac{x_1}{x_2}\right)$$. Vì $$\log$$ là hàm đơn điệu tăng và $$\frac{x_1}{x_2}$$ là hàm giả lồi trên $$\mathbb{R}_{++}^2$$, nên $$f$$ cũng là hàm giả lồi.

**Bước 4: Định lý đặc trưng**

**Định lý:** $$f$$ thỏa mãn bất đẳng thức Jensen biến đổi $$\Leftrightarrow$$ mọi tập mức dưới $$S_\alpha$$ đều là tập lồi.

**Chứng minh ($$\Rightarrow$$):** Với mọi $$x, y \in S_\alpha$$, ta có $$f(x) \leq \alpha$$ và $$f(y) \leq \alpha$$. Khi đó:
$$f(\theta x + (1-\theta) y) \leq \max\{f(x), f(y)\} \leq \alpha \Rightarrow \theta x + (1-\theta) y \in S_\alpha$$

**Chứng minh ($$\Leftarrow$$):** Đặt $$\alpha = \max\{f(x), f(y)\}$$, khi đó $$x, y \in S_\alpha$$. Vì $$S_\alpha$$ lồi nên $$\theta x + (1-\theta) y \in S_\alpha$$, suy ra:
$$f(\theta x + (1-\theta) y) \leq \alpha = \max\{f(x), f(y)\}$$

**Bước 5: Các phép toán bảo toàn tính giả lồi**
- **Maximum trọng số không âm:** $$\max\{w_1 f_1, w_2 f_2\}$$ ($$w_1, w_2 \ge 0$$) là giả lồi.
- **Hợp thành với hàm không giảm:** $$g \circ f$$ là giả lồi nếu $$g$$ không giảm và $$f$$ giả lồi.
- **Cực tiểu hóa từng phần:** $$\inf_{y \in C} f(x, y)$$ là giả lồi nếu $$f(x, y)$$ giả lồi đồng thời theo $$(x, y)$$ và $$C$$ lồi.
- **Lưu ý về phép cộng:** Tổng của hai hàm giả lồi nhìn chung **không** bảo toàn tính giả lồi.

</details>

---

## 📝 **Bài tập 7: Hàm log-lõm và log-lồi**

**Đề bài:** (Bài 3.7 từ Boyd & Vandenberghe)
a) Kiểm tra tính log-lõm / log-lồi của:
   - Mật độ Gauss: $$f(x) = e^{-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)}$$ (với $$\Sigma \succ 0$$)
   - Hàm Gamma: $$\Gamma(x) = \int_0^\infty t^{x-1} e^{-t}\, dt$$ (lưu ý: $$\Gamma$$ thực ra **log-lồi**, không phải log-lõm, trên $$x > 0$$: mỗi hàm $$x \mapsto t^{x-1}e^{-t} = e^{(x-1)\log t - t}$$ là log-affine, và tích phân của họ hàm log-lồi là log-lồi)
   - Định thức: $$\det(X)$$ trên $$\mathbb{S}_{++}^n$$

b) Nêu ứng dụng trong xác suất và thống kê

c) Phân tích mối liên hệ với tính lồi

**Yêu cầu:**
1. Kiểm tra bằng điều kiện bậc hai
2. Phân tích các phép toán bảo toàn
3. Nêu các ứng dụng thống kê
4. Phân tích ý nghĩa đối với tối ưu hóa

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Mật độ Gauss**

$$f(x) = e^{-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)} \implies \log f(x) = -\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)$$

**Hessian:** $$\nabla^2 \log f(x) = -\Sigma^{-1} \preceq 0 \Rightarrow \log f$$ lõm $$\Rightarrow f$$ là hàm log-lõm.

**Bước 2: Hàm định thức**

$$f(X) = \det(X)$$ trên $$\mathbb{S}_{++}^n \implies \log f(X) = \log \det(X)$$

Vì $$\log \det(X)$$ là hàm lõm trên $$\mathbb{S}_{++}^n$$ (có thể chứng minh qua phép hạn chế lên đường thẳng $$X + tV$$ và tính đạo hàm bậc hai), nên $$\det(X)$$ là hàm log-lõm.

**Bước 3: Các tính chất bảo toàn**
- **Phép nhân:** Nếu $$f, g$$ log-lõm thì $$fg$$ log-lõm (vì $$\log(fg) = \log f + \log g$$ là tổng hai hàm lõm).
- **Lũy thừa không âm:** Nếu $$f$$ log-lõm và $$\alpha \geq 0$$ thì $$f^\alpha$$ log-lõm.
- **Tích phân:** Tính log-lõm được bảo toàn khi lấy tích phân theo một nhóm biến (phân phối biên).

**Bước 4: Ứng dụng trong thống kê**
- **Ước lượng hợp lý cực đại (MLE):** Hàm hợp lý log-lõm dẫn đến hàm log-likelihood lõm, đưa bài toán MLE về bài toán tối ưu lồi.
- **Tính đơn đỉnh:** Mọi hàm mật độ log-lõm đều đơn đỉnh (giả lõm).
- **Bất đẳng thức tập trung:** Các độ đo xác suất log-lõm thỏa mãn nhiều bất đẳng thức tập trung chuẩn mực.

**Bước 5: Ý nghĩa trong tối ưu hóa**
- **Quy hoạch hình học (GP):** Sử dụng các hàm log-lồi.
- **Phương pháp hàm rào cản (barrier):** Hàm $$-\log \det(X)$$ là hàm rào cản chuẩn cho hình nón nửa xác định dương.
- **Họ phân phối mũ:** Hàm phân hoạch logarithm (log-partition function) là hàm lồi theo tham số tự nhiên.

</details>

---

## 📝 **Bài tập 8: Hàm phối cảnh và epigraph**

**Đề bài:** (Bài 3.8 từ Boyd & Vandenberghe)
a) Cho hàm lồi $$f: \mathbb{R}^n \to \mathbb{R}$$. Chứng minh hàm phối cảnh:
$$g(x, t) = t f(x/t)$$ với $$t > 0$$
là hàm lồi trên $$\{(x, t) : x/t \in \text{dom}(f),\; t > 0\}$$

b) Áp dụng cho các ví dụ:
   - $$f(x) = \lVert x \rVert_2 \Rightarrow g(x,t) = \lVert x \rVert_2$$
   - $$f(x) = x^2 \Rightarrow g(x,t) = x^2/t$$
   - $$f(x) = e^x \Rightarrow g(x,t) = t e^{x/t}$$

c) Chứng minh đặc trưng epigraph của tính lồi

**Yêu cầu:**
1. Chứng minh chặt chẽ tính lồi của hàm phối cảnh
2. Giải thích ý nghĩa hình học
3. Liên hệ với hình nón bậc hai
4. Phân tích đặc trưng epigraph

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Tính lồi của hàm phối cảnh**

**Định lý:** Nếu $$f$$ lồi thì $$g(x,t) = tf(x/t)$$ lồi trên $$\text{dom}(g) = \{(x,t) : x/t \in \text{dom}(f),\; t > 0\}$$.

**Chứng minh:** Với mọi $$(x_1, t_1), (x_2, t_2) \in \text{dom}(g)$$ và $$\theta \in [0,1]$$:

$$g(\theta(x_1, t_1) + (1-\theta)(x_2, t_2)) = (\theta t_1 + (1-\theta) t_2) f\left(\frac{\theta x_1 + (1-\theta) x_2}{\theta t_1 + (1-\theta) t_2}\right)$$

Nhận xét rằng:
$$\frac{\theta x_1 + (1-\theta) x_2}{\theta t_1 + (1-\theta) t_2} = \frac{\theta t_1}{\theta t_1 + (1-\theta) t_2} \cdot \frac{x_1}{t_1} + \frac{(1-\theta) t_2}{\theta t_1 + (1-\theta) t_2} \cdot \frac{x_2}{t_2}$$

Đây là một tổ hợp lồi của $$\frac{x_1}{t_1}$$ và $$\frac{x_2}{t_2}$$ vì hai trọng số đều không âm và có tổng bằng 1. Do $$f$$ lồi:
$$f\left(\frac{\theta x_1 + (1-\theta) x_2}{\theta t_1 + (1-\theta) t_2}\right) \leq \frac{\theta t_1}{\theta t_1 + (1-\theta) t_2} f(x_1/t_1) + \frac{(1-\theta) t_2}{\theta t_1 + (1-\theta) t_2} f(x_2/t_2)$$

Nhân hai vế với $$\theta t_1 + (1-\theta) t_2 > 0$$, ta thu được:
$$g(\theta(x_1, t_1) + (1-\theta)(x_2, t_2)) \leq \theta t_1 f(x_1/t_1) + (1-\theta) t_2 f(x_2/t_2) = \theta g(x_1, t_1) + (1-\theta) g(x_2, t_2)$$

**Bước 2: Các ví dụ ứng dụng**

- **Ví dụ 1:** $$f(x) = \lVert x \rVert_2 \Rightarrow g(x,t) = t \lVert x/t \rVert_2 = \lVert x \rVert_2$$ (chuẩn bất biến qua phép phối cảnh).
- **Ví dụ 2:** $$f(x) = x^2 \Rightarrow g(x,t) = t(x/t)^2 = x^2/t$$. Epigraph của nó liên hệ trực tiếp với hình nón bậc hai:
  $$\{(x,t,s) : x^2/t \leq s,\; t > 0\} = \{(x,t,s) : \lVert (2x,\ s-t) \rVert_2 \leq s+t,\; t > 0\}$$
  (do $$(2x)^2 + (s-t)^2 \leq (s+t)^2 \Leftrightarrow x^2 \leq st$$).
- **Ví dụ 3:** $$f(x) = e^x \Rightarrow g(x,t) = te^{x/t}$$, dẫn tới hình nón mũ (exponential cone) trong tối ưu hóa hình nón.

**Bước 3: Đặc trưng epigraph**

**Định lý:** $$f$$ lồi $$\Leftrightarrow$$ $$\text{epi}(f) = \{(x,t) : x \in \text{dom}(f),\; f(x) \leq t\}$$ là tập lồi.

- **Chiều thuận ($$\Rightarrow$$):** Với $$(x_1, t_1), (x_2, t_2) \in \text{epi}(f)$$, ta có:
  $$f(\theta x_1 + (1-\theta) x_2) \leq \theta f(x_1) + (1-\theta) f(x_2) \leq \theta t_1 + (1-\theta) t_2$$
  suy ra $$(\theta x_1 + (1-\theta) x_2, \theta t_1 + (1-\theta) t_2) \in \text{epi}(f)$$.
- **Chiều đảo ($$\Leftarrow$$):** Với mọi $$x_1, x_2 \in \text{dom}(f)$$, chọn $$t_1 = f(x_1)$$ và $$t_2 = f(x_2)$$; tính lồi của $$\text{epi}(f)$$ suy ra ngay $$(\theta x_1 + (1-\theta)x_2, \theta f(x_1) + (1-\theta)f(x_2)) \in \text{epi}(f)$$, tức $$f(\theta x_1 + (1-\theta)x_2) \leq \theta f(x_1) + (1-\theta)f(x_2)$$.

</details>

---

## 📝 **Bài tập 9: Hàm ma trận và tính lồi**

**Đề bài:** (Bài 3.9 từ Boyd & Vandenberghe)
Phân tích tính lồi của các hàm ma trận sau:

a) $$f(X) = \text{tr}(X)$$ trên $$\mathbb{S}^n$$

b) $$f(X) = \text{tr}(X^2)$$ trên $$\mathbb{S}^n$$

c) $$f(X) = \lambda_{\max}(X)$$ trên $$\mathbb{S}^n$$

d) $$f(X) = \det(X)$$ trên $$\mathbb{S}_{++}^n$$

e) $$f(X) = -\log \det(X)$$ trên $$\mathbb{S}_{++}^n$$

**Yêu cầu:**
1. Kiểm tra tính lồi / lõm
2. Tính tập dưới vi phân
3. Nêu ứng dụng trong quy hoạch nửa xác định (SDP)
4. Liên hệ với các thuật toán tối ưu

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Hàm vết $$f(X) = \text{tr}(X)$$**

Hàm tuyến tính: $$\text{tr}(\theta X + (1-\theta) Y) = \theta \text{tr}(X) + (1-\theta) \text{tr}(Y)$$, nên vừa lồi vừa lõm. Dưới vi phân: $$\partial f(X) = \{I\}$$.

**Bước 2: Vết của bình phương $$f(X) = \text{tr}(X^2)$$**

Trên $$\mathbb{S}^n$$, $$\text{tr}(X^2) = \sum_{i,j} X_{ij}^2$$ là tổng các hàm bình phương lồi nên là hàm lồi chặt. Dưới vi phân: $$\partial f(X) = \{2X\}$$.

**Bước 3: Giá trị riêng lớn nhất $$f(X) = \lambda_{\max}(X)$$**

Theo đặc trưng biến phân: $$\lambda_{\max}(X) = \max_{\lVert v \rVert_2 = 1} v^T X v$$. Đây là giá trị lớn nhất theo điểm của họ các hàm tuyến tính $$X \mapsto v^T X v$$ nên là hàm lồi.

**Dưới vi phân:** $$\partial f(X) = \text{conv}\{vv^T : v \text{ là vector riêng đơn vị ứng với } \lambda_{\max}(X)\}$$.

**Bước 4: Hàm định thức $$f(X) = \det(X)$$**

Vì $$\log \det(X)$$ lõm trên $$\mathbb{S}_{++}^n$$ nên $$\det(X)$$ là hàm log-lõm, nhưng bản thân $$\det(X)$$ không lồi cũng không lõm trên $$\mathbb{S}_{++}^n$$ (khi $$n \ge 2$$). Tuy nhiên, trung bình nhân các giá trị riêng $$\det(X)^{1/n} = (\prod \lambda_i)^{1/n}$$ là hàm lõm.

**Bước 5: Logarithm âm của định thức $$f(X) = -\log \det(X)$$**

Hàm $$-\log \det(X)$$ lồi chặt trên $$\mathbb{S}_{++}^n$$, với đạo hàm $$\partial f(X) = \{-X^{-1}\}$$ và dạng bậc hai của Hessian:
$$\nabla^2 f(X)[H, H] = \text{tr}(X^{-1} H X^{-1} H) > 0 \quad \text{với mọi } H \in \mathbb{S}^n, H \neq 0$$

**Ứng dụng:**
- **Hàm rào cản trong SDP:** $$-\log \det(X)$$ làm hàm rào cản cho ràng buộc $$X \succ 0$$ trong các phương pháp điểm trong.
- **Ước lượng hợp lý cực đại:** Ước lượng ma trận hiệp phương sai.
- **Thiết kế thí nghiệm tối ưu:** Thiết kế tối ưu kiểu D (D-optimal design).

</details>

---

## 📝 **Bài tập 10: Ứng dụng trong tối ưu hóa lồi**

**Đề bài:** (Bài 3.10 từ Boyd & Vandenberghe)
Phát biểu các bài toán sau dưới dạng bài toán tối ưu lồi:

a) **Hồi quy vững (robust regression):** Cực tiểu hóa tổng các hàm mất mát Huber
b) **Cực đại hóa entropy:** Với các ràng buộc mô-men tuyến tính
c) **Cực đại hóa trung bình nhân:** $$\max \prod_{i=1}^n x_i^{1/n}$$ với ràng buộc tuyến tính
d) **Cực tiểu hóa entropy tương đối:** $$\min \sum_{i=1}^n x_i \log(x_i/y_i)$$ với ràng buộc tuyến tính

**Yêu cầu:**
1. Xây dựng dạng bài toán tối ưu lồi tương ứng
2. Phân tích điều kiện tối ưu
3. Đề xuất thuật toán giải
4. Nêu ứng dụng thực tế

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Hồi quy vững**

**Bài toán:** $$\min_\beta \sum_{i=1}^n \phi(y_i - x_i^T \beta)$$ với hàm mất mát Huber:
$$\phi(u) = \begin{cases} \frac{1}{2}u^2 & |u| \leq M \\ M|u| - \frac{1}{2}M^2 & |u| > M \end{cases}$$

Hàm $$\phi$$ lồi vì là hàm bậc hai từng khúc có đạo hàm không giảm. Có thể viết lại thành bài toán quy hoạch bậc hai (QP):
$$\min_{\beta,r,s} \frac{1}{2}\sum_{i=1}^n r_i^2 + M\sum_{i=1}^n s_i$$
$$\text{với ràng buộc} \quad |y_i - x_i^T \beta| \leq r_i + s_i, \quad 0 \leq r_i \leq M, \quad s_i \geq 0$$

**Bước 2: Cực đại hóa entropy**

**Bài toán:** $$\max_x -\sum_{i=1}^n x_i \log x_i \quad \text{với ràng buộc} \quad \sum_{i=1}^n a_{ij} x_i = b_j, \quad x_i \geq 0$$

**Dạng tối ưu lồi:** $$\min_x \sum_{i=1}^n x_i \log x_i$$

**Điều kiện tối ưu (khi nghiệm nằm trong miền dương):**
$$\log x_i + 1 + \sum_{j=1}^m \lambda_j a_{ij} = 0 \Rightarrow x_i^* = e^{-1 - \sum_j \lambda_j a_{ij}}$$
(phân phối cực đại entropy có dạng họ hàm mũ).

**Bước 3: Cực đại hóa trung bình nhân**

**Bài toán:** $$\max_{x \geq 0} \prod_{i=1}^n x_i^{1/n} \quad \text{với ràng buộc} \quad Ax \leq b$$

Lấy logarithm để chuyển về bài toán tương đương $$\max_x \frac{1}{n}\sum_{i=1}^n \log x_i$$, hay dạng tối ưu lồi:
$$\min_x -\sum_{i=1}^n \log x_i \quad \text{với ràng buộc} \quad Ax \leq b, \quad x > 0$$

Bài toán này phù hợp tự nhiên với phương pháp rào cản logarithm, và xuất hiện trong thiết kế thí nghiệm tối ưu cũng như bài toán thương lượng Nash.

**Bước 4: Cực tiểu hóa entropy tương đối**

**Bài toán:** $$\min_x \sum_{i=1}^n x_i \log \frac{x_i}{y_i} \quad \text{với ràng buộc} \quad Ax = b, \quad x \geq 0$$

Phân kỳ Kullback–Leibler (entropy tương đối) là hàm lồi theo biến thứ nhất $$x$$.

**Điều kiện tối ưu:**
$$\log \frac{x_i}{y_i} + 1 + (A^T \lambda)_i - \mu_i = 0$$ (với $$\mu \geq 0$$ là nhân tử của $$x \geq 0$$; khi nghiệm có $$x_i > 0$$ thì $$\mu_i = 0$$).

**Dạng nghiệm:** $$x_i^* = y_i e^{-(A^T \lambda^*)_i - 1}$$.

**Ứng dụng:** Lý thuyết thông tin (dung lượng kênh), thống kê (ước lượng hợp lý cực đại có phân phối tiên nghiệm) và học máy (tối ưu hóa có chuẩn hóa).

</details>

---

## 💡 Mẹo thực hành

#### **Khi kiểm tra tính lồi:**
- **Điều kiện bậc hai:** Kiểm tra $$f''(x) \geq 0$$ hoặc $$\nabla^2 f(x) \succeq 0$$.
- **Định nghĩa trực tiếp:** Kiểm tra $$f(\theta x + (1-\theta) y) \leq \theta f(x) + (1-\theta) f(y)$$.
- **Quy tắc hợp thành:** Áp dụng các phép toán bảo toàn tính lồi.

#### **Khi tính hàm liên hợp:**
- **Dùng định nghĩa:** Giải bài toán $$f^*(y) = \sup_x (y^T x - f(x))$$.
- **Điều kiện bậc nhất:** Tìm $$x^*$$ thỏa mãn $$y \in \partial f(x^*)$$.
- **Ý nghĩa hình học:** Liên hệ với các siêu phẳng hỗ trợ epigraph của $$f$$.

#### **Khi làm việc với dưới vi phân:**
- **Trường hợp khả vi:** $$\partial f(x) = \{\nabla f(x)\}$$.
- **Trường hợp không khả vi:** Áp dụng định nghĩa hoặc các quy tắc tính dưới vi phân.
- **Điều kiện tối ưu:** $$x^*$$ là điểm cực tiểu toàn cục khi và chỉ khi $$0 \in \partial f(x^*)$$.

---

## 💡 **Tổng kết**

### **Định nghĩa và tiêu chuẩn kiểm tra tính lồi:**

| Phương pháp | Điều kiện | Khi nào dùng |
|-------------|-----------|--------------|
| **Định nghĩa** | $$f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta)f(y)$$ | Chứng minh trực tiếp |
| **Bậc nhất** | $$f(y) \geq f(x) + \nabla f(x)^T(y-x)$$ | Hàm khả vi |
| **Bậc hai** | $$\nabla^2 f(x) \succeq 0$$ | Hàm khả vi hai lần |
| **Epigraph** | $$\text{epi}(f)$$ là tập lồi | Tiếp cận hình học |

### **Các phép toán bảo toàn tính lồi:**

| Phép toán | Kết quả |
|-----------|---------|
| **Tổng trọng số không âm** | $$\sum \alpha_i f_i$$ với $$\alpha_i \geq 0$$ |
| **Hợp thành với ánh xạ affine** | $$f(Ax + b)$$ |
| **Maximum theo điểm** | $$f(x) = \max\{f_1(x), \ldots, f_m(x)\}$$ |
| **Supremum theo điểm** | $$g(x) = \sup_{y \in \mathcal{A}} f(x, y)$$ |
| **Hợp thành tổng quát** | $$h \circ g$$ ($$h$$ lồi không giảm, $$g$$ lồi) |
| **Cực tiểu hóa từng phần** | $$g(x) = \inf_y f(x, y)$$ nếu $$f$$ lồi đồng thời theo $$(x,y)$$ |
| **Hàm phối cảnh** | $$g(x, t) = tf(x/t)$$ |

### **Các ví dụ hàm lồi tiêu biểu:**

| Tên hàm | Biểu thức | Miền xác định | Lồi? |
|---------|-----------|---------------|------|
| **Hàm mũ** | $$e^{ax}$$ | $$\mathbb{R}$$ | ✓ |
| **Hàm lũy thừa** | $$x^a$$ | $$\mathbb{R}_{++}$$ | ✓ ($$a \geq 1$$ hoặc $$a \leq 0$$) |
| **Logarithm âm** | $$-\log x$$ | $$\mathbb{R}_{++}$$ | ✓ |
| **Chuẩn** | $$\|x\|_p$$ ($$p \ge 1$$) | $$\mathbb{R}^n$$ | ✓ |
| **Hàm max** | $$\max\{x_1, \ldots, x_n\}$$ | $$\mathbb{R}^n$$ | ✓ |
| **Hàm bậc hai** | $$x^TQx$$ | $$\mathbb{R}^n$$ | ✓ (nếu $$Q \succeq 0$$) |
| **Log-sum-exp** | $$\log(\sum e^{x_i})$$ | $$\mathbb{R}^n$$ | ✓ |

### **Hàm liên hợp:**

- **Định nghĩa:** $$f^*(y) = \sup_x (y^Tx - f(x))$$
- **Bất đẳng thức Fenchel:** $$f(x) + f^*(y) \geq x^Ty$$
- **Liên hợp kép:** $$f^{**} = f$$ (nếu $$f$$ đóng và lồi)
- **Ví dụ:**
  - $$(x^2/2)^* = y^2/2$$
  - $$(\|x\|)^* = I_{\|y\|_* \leq 1}$$ (hàm chỉ thị hình cầu đơn vị theo chuẩn đối ngẫu)
  - $$(-\log x)^* = -\log(-y) - 1$$ (với $$y < 0$$)

### **Dưới vi phân:**

- **Định nghĩa:** $$g \in \partial f(x)$$ nếu $$f(y) \geq f(x) + g^T(y-x)$$ với mọi $$y$$
- **Điều kiện tối ưu:** $$x^*$$ tối ưu $$\Leftrightarrow$$ $$0 \in \partial f(x^*)$$
- **Quy tắc tính toán:**
  - $$\partial(\alpha f) = \alpha \partial f$$ (với $$\alpha > 0$$)
  - $$\partial(f_1 + f_2) = \partial f_1 + \partial f_2$$
  - $$\partial \max\{f_1, f_2\} = \text{conv}\{\partial f_i : f_i(x) = f(x)\}$$

---

## 📚 Tài liệu tham khảo

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press.
   - Chapter 3: Convex Functions
   - Exercises 3.1-3.54

2. **Rockafellar, R. T.** (1970). *Convex Analysis*. Princeton University Press.

3. **Hiriart-Urruty, J.-B., & Lemaréchal, C.** (1993). *Convex Analysis and Minimization Algorithms*. Springer.
