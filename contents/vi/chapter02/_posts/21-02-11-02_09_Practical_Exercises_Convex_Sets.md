---
layout: post
title: "02-09 Bài Tập Thực Hành - Tập Convex"
chapter: "2"
order: 19
owner: "GitHub Copilot"
lang: vi
categories:
  - chapter02
lesson_type: required
redirect_from:
  - /contents/vi/chapter02/02_08_Practical_Exercises_Convex_Sets/
---

# Bài tập thực hành - Tập lồi

## **Bài tập 1: Kiểm tra tính lồi của tập hợp**

**Đề bài:** (Bài 2.1 từ Boyd & Vandenberghe)
Xác định tính lồi của các tập hợp sau:

a) $$S_1 = \{x \in \mathbb{R}^n : \lVert x \rVert_2 \leq 1\}$$

b) $$S_2 = \{x \in \mathbb{R}^n : \lVert x \rVert_\infty \leq 1\}$$

c) $$S_3 = \{x \in \mathbb{R}^n : x^T P x \leq 1\}$$ với $$P \succeq 0$$

d) $$S_4 = \{x \in \mathbb{R}^n : |x_i| \leq a_i, i = 1,\ldots,n\}$$ (với $$a_i \ge 0$$)

**Yêu cầu:**
1. Chứng minh tính lồi bằng định nghĩa
2. Kiểm tra lại bằng các phép toán bảo toàn tính lồi
3. Minh họa trong $$\mathbb{R}^2$$
4. Tìm các điểm cực biên (extreme points) của mỗi tập

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Chứng minh bằng định nghĩa**

**a) Hình cầu $$\ell_2$$:** $$S_1 = \{x : \lVert x \rVert_2 \leq 1\}$$

Với mọi $$x, y \in S_1$$ và $$\theta \in [0,1]$$:
$$\lVert \theta x + (1-\theta) y \rVert_2 \leq \theta \lVert x \rVert_2 + (1-\theta) \lVert y \rVert_2 \leq \theta \cdot 1 + (1-\theta) \cdot 1 = 1$$

$$\Rightarrow$$ $$S_1$$ là tập lồi.

**b) Hình cầu $$\ell_\infty$$:** $$S_2 = \{x : \max_i |x_i| \leq 1\}$$

$$\max_i |\theta x_i + (1-\theta) y_i| \leq \max_i (\theta |x_i| + (1-\theta) |y_i|) \leq \theta \max_i |x_i| + (1-\theta) \max_i |y_i| \leq 1$$

$$\Rightarrow$$ $$S_2$$ là tập lồi.

**c) Ellipsoid:** $$S_3 = \{x : x^T P x \leq 1\}$$ với $$P \succeq 0$$

$$(\theta x + (1-\theta) y)^T P (\theta x + (1-\theta) y) = \theta^2 x^T P x + 2\theta(1-\theta) x^T P y + (1-\theta)^2 y^T P y$$

Vì $$P \succeq 0$$, dạng toàn phương $$x^T P x$$ là hàm lồi, do đó tập mức dưới $$S_3$$ là tập lồi.

**d) Hình hộp chữ nhật (hyperrectangle):** $$S_4 = \prod_{i=1}^n [-a_i, a_i]$$

Tích Descartes của các tập lồi (các đoạn đóng) là một tập lồi.

**Bước 2: Các phép toán bảo toàn tính lồi**
- **a, b:** Tập mức dưới của hàm lồi (các hàm chuẩn)
- **c:** Tập mức dưới của dạng toàn phương lồi
- **d:** Tích Descartes của các đoạn đóng lồi

**Bước 3: Điểm cực biên**
- **a:** Biên $$\{x : \lVert x \rVert_2 = 1\}$$ (vô số điểm cực biên)
- **b:** Các đỉnh $$\{(\pm 1, \ldots, \pm 1)\}$$ ($$2^n$$ điểm cực biên; các điểm $$\pm e_i$$ là đỉnh của quả cầu $$\ell_1$$, không phải của quả cầu $$\ell_\infty$$)
- **c:** Phụ thuộc vào $$P$$: nếu $$P \succ 0$$, mọi điểm trên biên $$x^T P x = 1$$ đều là điểm cực biên; nếu $$P$$ suy biến, tập chứa trọn một đường thẳng nên không có điểm cực biên
- **d:** Các đỉnh $$\{(\pm a_1, \ldots, \pm a_n)\}$$ ($$2^n$$ điểm cực biên khi $$a_i > 0$$ với mọi $$i$$)

</details>

---

## **Bài tập 2: Các phép toán bảo toàn tính lồi**

**Đề bài:** (Bài 2.2 từ Boyd & Vandenberghe)
Cho hai tập lồi $$C_1, C_2 \subseteq \mathbb{R}^n$$. Chứng minh hoặc đưa ra phản ví dụ về tính lồi của:

a) **Giao:** $$C_1 \cap C_2$$

b) **Hợp:** $$C_1 \cup C_2$$

c) **Tổng Minkowski:** $$C_1 + C_2 = \{x + y : x \in C_1, y \in C_2\}$$

d) **Tích Descartes:** $$C_1 \times C_2$$

e) **Biến đổi affine:** $$f(C_1) = \{Ax + b : x \in C_1\}$$

**Yêu cầu:**
1. Chứng minh chặt chẽ cho các trường hợp đúng
2. Đưa ra phản ví dụ cho các trường hợp sai
3. Minh họa bằng các ví dụ cụ thể
4. Tổng quát hóa cho họ tập hợp bất kỳ

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Giao — LỒI**

<div class="textbook-proof" markdown="1">
**Chứng minh:** Với mọi $$x, y \in C_1 \cap C_2$$ và $$\theta \in [0,1]$$:
- $$x, y \in C_1 \Rightarrow \theta x + (1-\theta) y \in C_1$$ (vì $$C_1$$ lồi)
- $$x, y \in C_2 \Rightarrow \theta x + (1-\theta) y \in C_2$$ (vì $$C_2$$ lồi)
- $$\Rightarrow \theta x + (1-\theta) y \in C_1 \cap C_2$$
</div>

**Tổng quát hóa:** $$\bigcap_{i \in I} C_i$$ là tập lồi nếu mỗi $$C_i$$ là tập lồi.

**Bước 2: Hợp — KHÔNG LỒI**

**Phản ví dụ:** $$C_1 = \{(x,0) : x \geq 0\}$$, $$C_2 = \{(0,y) : y \geq 0\}$$

Cả hai tập đều lồi, nhưng $$C_1 \cup C_2$$ không lồi:
- $$(1,0) \in C_1 \cup C_2$$ và $$(0,1) \in C_1 \cup C_2$$
- $$\frac{1}{2}(1,0) + \frac{1}{2}(0,1) = (\frac{1}{2}, \frac{1}{2}) \notin C_1 \cup C_2$$

**Bước 3: Tổng Minkowski — LỒI**

<div class="textbook-proof" markdown="1">
**Chứng minh:** Với mọi $$z_1, z_2 \in C_1 + C_2$$:
- Viết $$z_1 = x_1 + y_1$$, $$z_2 = x_2 + y_2$$ với $$x_i \in C_1, y_i \in C_2$$
- $$\theta z_1 + (1-\theta) z_2 = \theta(x_1 + y_1) + (1-\theta)(x_2 + y_2)$$
- $$= (\theta x_1 + (1-\theta) x_2) + (\theta y_1 + (1-\theta) y_2)$$
- $$\in C_1 + C_2$$ (vì $$C_1, C_2$$ lồi)
</div>

**Bước 4: Tích Descartes — LỒI**

<div class="textbook-proof" markdown="1">
**Chứng minh:** Với mọi $$(x_1, y_1), (x_2, y_2) \in C_1 \times C_2$$:
$$\theta(x_1, y_1) + (1-\theta)(x_2, y_2) = (\theta x_1 + (1-\theta) x_2, \theta y_1 + (1-\theta) y_2) \in C_1 \times C_2$$
</div>

**Bước 5: Biến đổi affine — LỒI**

<div class="textbook-proof" markdown="1">
**Chứng minh:** Với mọi $$z_1, z_2 \in f(C_1)$$:
- Viết $$z_i = Ax_i + b$$ với $$x_i \in C_1$$
- $$\theta z_1 + (1-\theta) z_2 = A(\theta x_1 + (1-\theta) x_2) + b \in f(C_1)$$
</div>

</details>

---

## **Bài tập 3: Siêu phẳng phân tách**

**Đề bài:** (Bài 2.3 từ Boyd & Vandenberghe)
Cho hai tập lồi rời nhau $$C, D \subset \mathbb{R}^n$$ ($$C \cap D = \emptyset$$).

a) Chứng minh tồn tại siêu phẳng phân tách

b) Tìm một siêu phẳng phân tách cho mỗi cặp tập sau:
   - $$C = \{x : \lVert x \rVert_2 \leq 1\}$$, $$D = \{x : \lVert x - (3,0) \rVert_2 \leq 1\}$$
   - $$C = \{x : x_1 + x_2 \leq 1, x_1, x_2 \geq 0\}$$, $$D = \{(2,2)\}$$

**Yêu cầu:**
1. Chứng minh kiến thiết cho định lý siêu phẳng phân tách
2. Tính toán tường minh cho hai ví dụ trên
3. Minh họa hình học sự phân tách
4. Phân tích trường hợp hai tập tiếp xúc tại biên

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Định lý siêu phẳng phân tách**

<div class="textbook-theorem" markdown="1">
**Định lý:** Nếu $$C, D$$ là hai tập lồi không rỗng và rời nhau, thì tồn tại $$a \neq 0$$ và $$b \in \mathbb{R}$$ sao cho:
$$a^T x \leq b \leq a^T y, \quad \forall x \in C, y \in D$$
</div>

**Chứng minh kiến thiết (trường hợp $$C, D$$ đóng và ít nhất một tập bị chặn):**
1. Xét tập hiệu $$S = C - D = \{x - y : x \in C, y \in D\}$$ (là tập lồi)
2. Ta có $$0 \notin S$$ (vì $$C \cap D = \emptyset$$)
3. Tìm điểm $$s^* \in S$$ gần gốc tọa độ nhất: $$s^* = \arg\min_{s \in S} \lVert s \rVert_2$$
4. Viết $$s^* = x^* - y^*$$ ($$x^* \in C$$, $$y^* \in D$$). Đặt $$a = y^* - x^* = -s^*$$ và $$b = \frac{1}{2}(\lVert y^* \rVert_2^2 - \lVert x^* \rVert_2^2)$$ (siêu phẳng trung trực của đoạn $$x^* y^*$$). Điều kiện tối ưu của $$s^*$$ cho $$s^{*T}(s - s^*) \geq 0$$ với mọi $$s \in S$$, từ đó suy ra $$a^T x \leq b \leq a^T y$$.

**Bước 2: Ví dụ 1 — Hai hình cầu**
$$C = \{x : \lVert x \rVert_2 \leq 1\}$$, $$D = \{x : \lVert x - (3,0) \rVert_2 \leq 1\}$$

**Cách tiếp cận hình học:** Hai tâm đặt tại $$(0,0)$$ và $$(3,0)$$, cùng bán kính bằng 1. Đường thẳng phân tách vuông góc với đoạn nối hai tâm.

**Nghiệm:** $$a = (1,0)$$, $$b = 1.5$$. Siêu phẳng phân tách là $$x_1 = 1.5$$.

**Kiểm tra:**
- $$\max_{x \in C} x_1 = 1 < 1.5$$
- $$\min_{x \in D} x_1 = 2 > 1.5$$

**Bước 3: Ví dụ 2 — Đơn hình và một điểm**
$$C = \{x : x_1 + x_2 \leq 1, x_1, x_2 \geq 0\}$$, $$D = \{(2,2)\}$$

**Cách tiếp cận:** Tìm điểm trong $$C$$ gần $$(2,2)$$ nhất bằng bài toán tối ưu:
$$\min_{x \in C} \lVert x - (2,2) \rVert_2^2$$

**Điều kiện KKT:** Điểm gần nhất là $$(1/2, 1/2)$$ (hình chiếu của $$(2,2)$$ lên cạnh $$x_1 + x_2 = 1$$), với khoảng cách $$\frac{3}{\sqrt{2}}$$.

**Nghiệm:** Chọn $$a = (1,1)$$ (cùng hướng với $$(2,2) - (1/2,1/2)$$) và $$b = 1.5$$, thu được siêu phẳng $$x_1 + x_2 = 1.5$$. Tổng quát, mọi $$b \in (1, 4)$$ đều tách được hai tập; siêu phẳng trung trực là $$x_1 + x_2 = 2.5$$.

</details>

---

## **Bài tập 4: Tính bao lồi**

**Đề bài:** (Bài 2.4 từ Boyd & Vandenberghe)
Tính bao lồi của các tập hợp sau:

a) $$S_1 = \{(0,0), (1,0), (0,1), (1,1)\}$$ trong $$\mathbb{R}^2$$

b) $$S_2 = \{x \in \mathbb{R}^3 : \lVert x \rVert_2 = 1, x_3 = 0\} \cup \{(0,0,1), (0,0,-1)\}$$

c) $$S_3 = \{(t, t^2) : t \in [-1,1]\}$$ trong $$\mathbb{R}^2$$

**Yêu cầu:**
1. Tính tường minh bao lồi
2. Xác định các điểm cực biên
3. Mô tả bằng hệ bất đẳng thức nếu có thể
4. Minh họa kết quả

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Tập hữu hạn điểm**
$$S_1 = \{(0,0), (1,0), (0,1), (1,1)\}$$

**Bao lồi:** Hình vuông đơn vị $$[0,1] \times [0,1]$$.

**Điểm cực biên:** Cả 4 điểm trong $$S_1$$ đều là điểm cực biên.

**Biểu diễn bằng bất đẳng thức:**
$$\text{conv}(S_1) = \{x : 0 \leq x_1 \leq 1, 0 \leq x_2 \leq 1\}$$

**Bước 2: Đường tròn và hai đỉnh**
$$S_2 = \{x \in \mathbb{R}^3 : x_1^2 + x_2^2 = 1, x_3 = 0\} \cup \{(0,0,1), (0,0,-1)\}$$

**Bao lồi:** Hình nón đôi (double cone):
$$\text{conv}(S_2) = \{x \in \mathbb{R}^3 : x_1^2 + x_2^2 \leq (1 - |x_3|)^2, |x_3| \leq 1\}$$

**Điểm cực biên:** Đường tròn $$\{x : x_1^2 + x_2^2 = 1, x_3 = 0\}$$ và hai đỉnh $$(0,0,\pm 1)$$.

**Bước 3: Cung parabol**
$$S_3 = \{(t, t^2) : t \in [-1,1]\}$$

**Bao lồi:** Miền nằm phía trên cung parabol và phía dưới dây cung $$x_2 = 1$$:
$$\text{conv}(S_3) = \{(x_1, x_2) : x_1^2 \leq x_2 \leq 1\}$$

**Điểm cực biên:**
- Mọi điểm $$(t, t^2)$$ với $$t \in [-1,1]$$ trên cung parabol (kể cả hai đầu mút $$(\pm 1, 1)$$)
- Các điểm trong của đoạn thẳng $$x_2 = 1$$ không phải là điểm cực biên

**Cách viết khác:**
$$\text{conv}(S_3) = \{(x_1, x_2) : x_2 \geq x_1^2,\ x_2 \leq 1\}$$ (điều kiện $$|x_1| \leq 1$$ tự suy ra).

</details>

---

## **Bài tập 5: Hình nón đối ngẫu**

**Đề bài:** (Bài 2.5 từ Boyd & Vandenberghe)
Tìm hình nón đối ngẫu của các hình nón sau:

a) $$K_1 = \mathbb{R}_+^n = \{x \in \mathbb{R}^n : x_i \geq 0, \forall i\}$$

b) $$K_2 = \{x \in \mathbb{R}^n : \lVert (x_1, \ldots, x_{n-1}) \rVert_2 \leq x_n\}$$ (hình nón bậc hai)

c) $$K_3 = \{x \in \mathbb{R}^n : \sum_{i=1}^{n-1} |x_i| \leq x_n\}$$ (hình nón $$\ell_1$$)

d) $$K_4 = \{X \in \mathbb{S}^n : X \succeq 0\}$$ (hình nón nửa xác định dương)

**Yêu cầu:**
1. Tính hình nón đối ngẫu $$K^* = \{y : y^T x \geq 0, \forall x \in K\}$$
2. Kiểm tra tính tự đối ngẫu (nếu có)
3. Thiết lập các quan hệ đối ngẫu
4. Giải thích ý nghĩa hình học

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Góc phần tư không âm**
$$K_1^* = \{y : y^T x \geq 0, \forall x \in \mathbb{R}_+^n\}$$

**Phân tích:** $$y^T x = \sum_{i=1}^n y_i x_i \geq 0$$ với mọi $$x_i \geq 0$$ $$\Rightarrow y_i \geq 0, \forall i$$.

**Kết quả:** $$K_1^* = \mathbb{R}_+^n = K_1$$ (tự đối ngẫu).

**Bước 2: Hình nón bậc hai**
$$K_2 = \{x : \lVert (x_1, \ldots, x_{n-1}) \rVert_2 \leq x_n\}$$

**Đối ngẫu:** $$K_2^* = \{y : y^T x \geq 0, \forall x \in K_2\} = K_2$$ (tự đối ngẫu).

**Ý tưởng chứng minh:** Áp dụng bất đẳng thức Cauchy–Schwarz và tính thuần nhất của chuẩn $$\ell_2$$.

**Bước 3: Hình nón $$\ell_1$$**
$$K_3 = \{x : \sum_{i=1}^{n-1} |x_i| \leq x_n\}$$

**Đối ngẫu:** $$K_3^* = \{y : \lVert (y_1, \ldots, y_{n-1}) \rVert_\infty \leq y_n\}$$.

**Kiểm chứng:** Dựa trên tính đối ngẫu giữa chuẩn $$\ell_1$$ và chuẩn $$\ell_\infty$$.

**Bước 4: Hình nón nửa xác định dương (PSD)**
$$K_4 = \{X \in \mathbb{S}^n : X \succeq 0\}$$

**Đối ngẫu:** $$K_4^* = \{Y \in \mathbb{S}^n : \text{tr}(YX) \geq 0, \forall X \succeq 0\} = K_4$$ (tự đối ngẫu).

<div class="textbook-proof" markdown="1">
**Chứng minh:** $$Y \succeq 0 \Leftrightarrow \text{tr}(YX) \geq 0, \forall X \succeq 0$$.
</div>

</details>

---

## **Bài tập 6: Phép chiếu lên tập lồi**

**Đề bài:** (Bài 2.6 từ Boyd & Vandenberghe)
Tính hình chiếu Euclidean của điểm $$x_0$$ lên tập lồi $$C$$:

$$\text{proj}_C(x_0) = \arg\min_{x \in C} \lVert x - x_0 \rVert_2$$

a) $$C = \{x : a^T x = b\}$$ (siêu phẳng)

b) $$C = \{x : a^T x \leq b\}$$ (nửa không gian)

c) $$C = \{x : \lVert x \rVert_2 \leq r\}$$ (hình cầu $$\ell_2$$)

d) $$C = \{x : \lVert x \rVert_\infty \leq r\}$$ (hình cầu $$\ell_\infty$$)

**Yêu cầu:**
1. Tìm công thức nghiệm đóng
2. Kiểm tra điều kiện tối ưu
3. Phân tích tính duy nhất của hình chiếu
4. Xây dựng thuật toán tính toán

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Phép chiếu lên siêu phẳng**
$$C = \{x : a^T x = b\}$$

**Hàm Lagrange:** $$L(x,\lambda) = \frac{1}{2}\lVert x - x_0 \rVert_2^2 + \lambda(a^T x - b)$$

**Điều kiện tối ưu:** $$x - x_0 + \lambda a = 0 \Rightarrow x = x_0 - \lambda a$$

**Ràng buộc:** $$a^T(x_0 - \lambda a) = b \Rightarrow \lambda = \frac{a^T x_0 - b}{\lVert a \rVert_2^2}$$

**Nghiệm:** $$\text{proj}_C(x_0) = x_0 - \frac{a^T x_0 - b}{\lVert a \rVert_2^2} a$$

**Bước 2: Phép chiếu lên nửa không gian**
$$C = \{x : a^T x \leq b\}$$

**Xét hai trường hợp:**
- Nếu $$a^T x_0 \leq b$$: $$\text{proj}_C(x_0) = x_0$$
- Nếu $$a^T x_0 > b$$: chiếu lên siêu phẳng biên $$a^T x = b$$

**Nghiệm:**
$$\text{proj}_C(x_0) = \begin{cases} 
x_0 & \text{nếu } a^T x_0 \leq b \\
x_0 - \frac{a^T x_0 - b}{\lVert a \rVert_2^2} a & \text{nếu } a^T x_0 > b
\end{cases}$$

**Bước 3: Phép chiếu lên hình cầu $$\ell_2$$**
$$C = \{x : \lVert x \rVert_2 \leq r\}$$

**Xét hai trường hợp:**
- Nếu $$\lVert x_0 \rVert_2 \leq r$$: $$\text{proj}_C(x_0) = x_0$$
- Nếu $$\lVert x_0 \rVert_2 > r$$: chiếu theo phương bán kính lên mặt cầu biên

**Nghiệm:**
$$\text{proj}_C(x_0) = \begin{cases}
x_0 & \text{nếu } \lVert x_0 \rVert_2 \leq r \\
r \frac{x_0}{\lVert x_0 \rVert_2} & \text{nếu } \lVert x_0 \rVert_2 > r
\end{cases}$$

**Bước 4: Phép chiếu lên hình cầu $$\ell_\infty$$**
$$C = \{x : \lVert x \rVert_\infty \leq r\}$$

**Phép chiếu theo từng thành phần:**
$$[\text{proj}_C(x_0)]_i = \begin{cases}
x_{0i} & \text{nếu } |x_{0i}| \leq r \\
r \cdot \text{sign}(x_{0i}) & \text{nếu } |x_{0i}| > r
\end{cases}$$

**Viết gọn:** $$\text{proj}_C(x_0) = \text{clip}(x_0, -r, r)$$

</details>

---

## **Bài tập 7: Điểm cực biên và đỉnh của polytope**

**Đề bài:** (Bài 2.7 từ Boyd & Vandenberghe)
Cho polytope $$P = \{x : Ax \leq b\}$$ trong $$\mathbb{R}^n$$.

a) Chứng minh $$x \in P$$ là điểm cực biên khi và chỉ khi có $$n$$ ràng buộc độc lập tuyến tính hoạt động (đạt dấu bằng) tại $$x$$

b) Tìm tất cả các điểm cực biên của:
   - $$P_1 = \{x \in \mathbb{R}^2 : x_1 + x_2 \leq 1, x_1 \geq 0, x_2 \geq 0\}$$
   - $$P_2 = \{x \in \mathbb{R}^3 : x_1 + x_2 + x_3 \leq 1, x_i \geq 0\}$$

c) Kiểm chứng định lý Krein–Milman: $$P = \text{conv}(\text{các điểm cực biên})$$

**Yêu cầu:**
1. Chứng minh chặt chẽ đặc trưng đại số của điểm cực biên
2. Liệt kê có hệ thống các đỉnh
3. Minh họa hình học
4. Đề xuất thuật toán tìm đỉnh

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Định lý đặc trưng**

<div class="textbook-theorem" markdown="1">
**Định lý:** $$x \in P$$ là điểm cực biên $$\Leftrightarrow$$ có $$n$$ ràng buộc độc lập tuyến tính hoạt động tại $$x$$.
</div>

**Chứng minh ($$\Leftarrow$$):** Giả sử có $$n$$ ràng buộc hoạt động độc lập tuyến tính: $$A_I x = b_I$$ với $$A_I$$ có hạng đầy đủ $$n$$.

Nếu $$x = \theta y + (1-\theta) z$$ với $$y, z \in P$$ và $$\theta \in (0,1)$$:
- $$A_I y \leq b_I$$ và $$A_I z \leq b_I$$
- $$b_I = A_I x = \theta A_I y + (1-\theta) A_I z \leq b_I$$
- $$\Rightarrow A_I y = A_I z = b_I$$
- Vì $$A_I$$ có hạng đầy đủ nên $$y = z = x$$.

<div class="textbook-proof" markdown="1">
**Chứng minh ($$\Rightarrow$$):** Dùng phản chứng — nếu số ràng buộc độc lập tuyến tính hoạt động tại $$x$$ nhỏ hơn $$n$$, tồn tại hướng $$d \neq 0$$ thỏa mãn $$A_I d = 0$$ sao cho $$x \pm \varepsilon d \in P$$ với $$\varepsilon > 0$$ đủ nhỏ, nên $$x$$ không phải điểm cực biên.
</div>

**Bước 2: Ví dụ 1 — Đơn hình 2D**
$$P_1 = \{x : x_1 + x_2 \leq 1, x_1 \geq 0, x_2 \geq 0\}$$

**Các tổ hợp ràng buộc hoạt động:**
- $$\{x_1 = 0, x_2 = 0\}$$: đỉnh $$(0,0)$$
- $$\{x_1 = 0, x_1 + x_2 = 1\}$$: đỉnh $$(0,1)$$
- $$\{x_2 = 0, x_1 + x_2 = 1\}$$: đỉnh $$(1,0)$$

**Tập điểm cực biên:** $$\{(0,0), (0,1), (1,0)\}$$.

**Bước 3: Ví dụ 2 — Đơn hình 3D**
$$P_2 = \{x : x_1 + x_2 + x_3 \leq 1, x_1, x_2, x_3 \geq 0\}$$

**Liệt kê có hệ thống:** Chọn 3 trong 4 ràng buộc để đặt dấu bằng.

**Các điểm cực biên:**
- $$(0,0,0)$$: $$\{x_1 = 0, x_2 = 0, x_3 = 0\}$$
- $$(1,0,0)$$: $$\{x_2 = 0, x_3 = 0, x_1 + x_2 + x_3 = 1\}$$
- $$(0,1,0)$$: $$\{x_1 = 0, x_3 = 0, x_1 + x_2 + x_3 = 1\}$$
- $$(0,0,1)$$: $$\{x_1 = 0, x_2 = 0, x_1 + x_2 + x_3 = 1\}$$

**Bước 4: Kiểm chứng định lý Krein–Milman**
$$P_1 = \text{conv}\{(0,0), (0,1), (1,0)\}$$
$$P_2 = \text{conv}\{(0,0,0), (1,0,0), (0,1,0), (0,0,1)\}$$

</details>

---

## **Bài tập 8: Bất đẳng thức tổng quát**

**Đề bài:** (Bài 2.8 từ Boyd & Vandenberghe)
Cho hình nón thích hợp $$K \subseteq \mathbb{R}^n$$ và bất đẳng thức tổng quát $$\preceq_K$$.

a) Kiểm chứng các tính chất của $$\preceq_K$$:
   - Phản xạ: $$x \preceq_K x$$
   - Phản đối xứng: $$x \preceq_K y, y \preceq_K x \Rightarrow x = y$$
   - Bắc cầu: $$x \preceq_K y, y \preceq_K z \Rightarrow x \preceq_K z$$

b) Với $$K = \mathbb{S}_+^n$$, kiểm chứng:
   - $$A \preceq B \Rightarrow A + C \preceq B + C$$
   - $$A \preceq B, C \succeq 0 \Rightarrow CAC \preceq CBC$$

**Yêu cầu:**
1. Chứng minh chặt chẽ các tính chất
2. Đưa ra phản ví dụ cho hình nón không thích hợp
3. Nêu ứng dụng trong tối ưu hóa
4. Liên hệ với hình nón đối ngẫu

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Các tính chất của bất đẳng thức tổng quát**

<div class="textbook-definition" markdown="1">
**Định nghĩa:** $$x \preceq_K y \Leftrightarrow y - x \in K$$
</div>

**Phản xạ:** $$x \preceq_K x \Leftrightarrow x - x = 0 \in K$$ (đúng vì $$K$$ là hình nón nên chứa $$0$$).

**Phản đối xứng:** $$x \preceq_K y, y \preceq_K x$$
- $$\Rightarrow y - x \in K$$ và $$x - y \in K$$
- $$\Rightarrow y - x \in K \cap (-K)$$
- Vì $$K$$ nhọn nên $$K \cap (-K) = \{0\}$$
- $$\Rightarrow y - x = 0 \Rightarrow x = y$$

**Bắc cầu:** $$x \preceq_K y, y \preceq_K z$$
- $$\Rightarrow y - x \in K, z - y \in K$$
- $$\Rightarrow z - x = (z - y) + (y - x) \in K + K = K$$
- $$\Rightarrow x \preceq_K z$$

**Bước 2: Bất đẳng thức ma trận**

**Tính chất 1:** $$A \preceq B \Rightarrow A + C \preceq B + C$$

<div class="textbook-proof" markdown="1">
**Chứng minh:**
- $$A \preceq B \Rightarrow B - A \succeq 0$$
- $$(B + C) - (A + C) = B - A \succeq 0$$
- $$\Rightarrow A + C \preceq B + C$$
</div>

**Tính chất 2:** $$A \preceq B, C \succeq 0 \Rightarrow CAC \preceq CBC$$

<div class="textbook-proof" markdown="1">
**Chứng minh:**
- Ta có $$B - A \succeq 0$$ và $$C$$ đối xứng ($$C \succeq 0$$)
- Với mọi vector $$x$$: $$x^T(CBC - CAC)x = (Cx)^T(B - A)(Cx) \geq 0$$
- $$\Rightarrow CBC - CAC \succeq 0$$ (không cần giả thiết $$C$$ khả nghịch; thực tế chỉ cần $$C$$ đối xứng)
- $$\Rightarrow CAC \preceq CBC$$
</div>

**Bước 3: Phản ví dụ cho hình nón không thích hợp**

**Hình nón không nhọn:** $$K = \{x \in \mathbb{R}^2 : x_1 = 0\}$$
- $$K \cap (-K) = K \neq \{0\}$$
- Tính phản đối xứng không còn đúng

**Hình nón không đặc:** $$K = \mathbb{R}_+ \times \{0\} \subset \mathbb{R}^2$$
- Phần trong rỗng
- Bất đẳng thức nghiêm ngặt $$\prec_K$$ không xác định được

</details>

---

## **Bài tập 9: Tổ hợp lồi và định lý Carathéodory**

**Đề bài:** (Bài 2.9 từ Boyd & Vandenberghe)
a) Chứng minh định lý Carathéodory: Mọi điểm trong $$\text{conv}(S)$$ (với $$S \subseteq \mathbb{R}^n$$) đều biểu diễn được dưới dạng tổ hợp lồi của tối đa $$n+1$$ điểm thuộc $$S$$.

b) Áp dụng cho:
   - $$S = \{(1,0), (0,1), (-1,0), (0,-1)\}$$ trong $$\mathbb{R}^2$$
   - $$S = \{e_i : i = 1,\ldots,n\} \cup \{0\}$$ trong $$\mathbb{R}^n$$

c) Xây dựng thuật toán tìm biểu diễn tối giản

**Yêu cầu:**
1. Chứng minh đầy đủ định lý Carathéodory
2. Tính toán tường minh cho hai ví dụ
3. Trình bày thuật toán
4. Giải thích ý nghĩa hình học

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Chứng minh định lý Carathéodory**

<div class="textbook-theorem" markdown="1">
**Định lý:** Nếu $$x \in \text{conv}(S)$$ với $$S \subseteq \mathbb{R}^n$$, thì $$x$$ viết được dưới dạng:
$$x = \sum_{i=1}^{n+1} \lambda_i x_i$$
với $$x_i \in S$$, $$\lambda_i \geq 0$$ và $$\sum \lambda_i = 1$$.
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh:**
1. Giả sử $$x = \sum_{i=1}^k \lambda_i x_i$$ với $$k > n+1$$
2. Các vector $$\{x_1 - x_k, \ldots, x_{k-1} - x_k\}$$ phụ thuộc tuyến tính trong $$\mathbb{R}^n$$
3. Tồn tại các số $$\mu_1, \dots, \mu_{k-1}$$ không đồng thời bằng 0 sao cho $$\sum_{i=1}^{k-1} \mu_i (x_i - x_k) = 0$$
4. Đặt $$\mu_k = -\sum_{i=1}^{k-1} \mu_i$$, ta thu được $$\sum_{i=1}^k \mu_i x_i = 0$$ và $$\sum_{i=1}^k \mu_i = 0$$
5. Khi đó $$x = \sum_{i=1}^k (\lambda_i - t\mu_i) x_i$$ với mọi $$t \in \mathbb{R}$$
6. Chọn $$t = \min\{\lambda_i/\mu_i : \mu_i > 0\}$$: mọi hệ số mới vẫn $$\geq 0$$, tổng vẫn bằng 1 (do $$\sum \mu_i = 0$$), và có ít nhất một hệ số triệt tiêu, nhờ đó giảm được $$k$$ đi ít nhất 1. Lặp lại cho tới khi $$k \le n+1$$.
</div>

**Bước 2: Ví dụ 1 — Bốn đỉnh hình vuông xoay**
$$S = \{(1,0), (0,1), (-1,0), (0,-1)\}$$

**Bao lồi:** Hình vuông xoay $$45^\circ$$ (hình thoi).

**Chặn Carathéodory:** Tối đa $$n+1 = 3$$ điểm.

**Ví dụ:** $$(0,0) = \frac{1}{4}(1,0) + \frac{1}{4}(0,1) + \frac{1}{4}(-1,0) + \frac{1}{4}(0,-1)$$ có thể rút gọn thành biểu diễn tối giản $$(0,0) = \frac{1}{2}(1,0) + \frac{1}{2}(-1,0)$$ (chỉ gồm 2 điểm).

**Bước 3: Ví dụ 2 — Cơ sở chính tắc và gốc tọa độ**
$$S = \{e_1, \ldots, e_n, 0\}$$

**Bao lồi:** Đơn hình chuẩn $$\{x : \sum x_i \leq 1, x_i \geq 0\}$$.

**Biểu diễn:** Mọi điểm $$x$$ viết được duy nhất thành $$x = \sum_{i=1}^n x_i e_i + (1 - \sum x_i) \cdot 0$$, sử dụng tối đa $$n+1$$ điểm (đạt đúng chặn Carathéodory).

**Bước 4: Thuật toán rút gọn biểu diễn**

```
Algorithm: Minimal Convex Combination
Input: Point x, set S
Output: Minimal convex combination

1. Find any representation x = Σ λᵢ xᵢ
2. While |active set| > n+1:
   a. Solve Σ μᵢ xᵢ = 0, Σ μᵢ = 0 with some μᵢ ≠ 0
   b. Find t = min{λᵢ/μᵢ : μᵢ > 0}
   c. Update λᵢ ← λᵢ - t μᵢ
   d. Remove zero coefficients
3. Return minimal representation
```

</details>

---

## **Bài tập 10: Cấu trúc mặt của tập lồi**

**Đề bài:** (Bài 2.10 từ Boyd & Vandenberghe)
Cho tập lồi $$C$$ và siêu phẳng hỗ trợ $$H = \{x : a^T x = \alpha\}$$ với $$\sup_{x \in C} a^T x = \alpha$$.

a) Chứng minh $$F = C \cap H$$ là một mặt (face) của $$C$$

b) Phân loại các mặt của:
   - Hình lập phương đơn vị $$[0,1]^n$$
   - Đơn hình đơn vị $$\{x : \sum x_i \leq 1, x_i \geq 0\}$$
   - Hình cầu $$\ell_2$$ $$\{x : \lVert x \rVert_2 \leq 1\}$$

c) Mô tả cấu trúc dàn mặt (face lattice)

**Yêu cầu:**
1. Chứng minh chặt chẽ tính chất mặt
2. Liệt kê đầy đủ cho ba ví dụ
3. Phân tích số chiều của các mặt
4. Mô tả cấu trúc dàn mặt

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Đặc trưng của mặt**

<div class="textbook-definition" markdown="1">
**Định nghĩa:** $$F$$ là một mặt (face) của $$C$$ nếu:
- $$F \subseteq C$$
- $$F$$ là tập lồi
- Nếu $$x \in F$$ và $$x = \theta y + (1-\theta) z$$ với $$y, z \in C$$, $$\theta \in (0,1)$$, thì $$y, z \in F$$
</div>

<div class="textbook-theorem" markdown="1">
**Định lý:** Nếu $$H$$ là siêu phẳng hỗ trợ của $$C$$, thì $$F = C \cap H$$ là một mặt của $$C$$.
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh:**
1. $$F \subseteq C$$ (theo định nghĩa)
2. $$F$$ là tập lồi (giao của hai tập lồi $$C$$ và $$H$$)
3. Nếu $$x \in F$$ và $$x = \theta y + (1-\theta) z$$ với $$y, z \in C$$, $$\theta \in (0,1)$$:
   - $$\alpha = a^T x = \theta a^T y + (1-\theta) a^T z$$
   - Vì $$a^T y \leq \alpha$$ và $$a^T z \leq \alpha$$ (do $$y, z \in C$$), nên bắt buộc $$a^T y = a^T z = \alpha$$
   - $$\Rightarrow y, z \in F$$
</div>

**Bước 2: Các mặt của hình lập phương đơn vị**
$$C = [0,1]^n$$

**Phân loại theo số chiều:**
- **Chiều 0:** $$2^n$$ đỉnh thuộc $$\{0,1\}^n$$
- **Chiều 1:** $$n \cdot 2^{n-1}$$ cạnh
- **Chiều $$k$$:** Các mặt thu được bằng cách cố định $$n-k$$ tọa độ nhận giá trị trong $$\{0,1\}$$
- **Chiều $$n-1$$:** $$2n$$ mặt bên (facets) $$\{x_i = 0\}$$ và $$\{x_i = 1\}$$
- **Chiều $$n$$:** Chính tập $$C$$

**Tổng số mặt khác rỗng:** $$3^n$$ (mỗi tọa độ có 3 lựa chọn: tự do trong $$[0,1]$$, bằng 0 hoặc bằng 1; tính cả mặt rỗng $$\emptyset$$ là $$3^n + 1$$).

**Bước 3: Các mặt của đơn hình đơn vị**
$$C = \{x : \sum x_i \leq 1, x_i \geq 0\}$$

**Cấu trúc mặt:**
- **Đỉnh:** $$\{0, e_1, \ldots, e_n\}$$ ($$n+1$$ đỉnh)
- **Cạnh:** Các đoạn thẳng nối từng cặp đỉnh
- **Mặt bên (facets):** $$\{x_i = 0\}$$ và $$\{\sum x_i = 1\}$$
- **Mặt tổng quát:** Thu được bằng cách đặt một tập con các ràng buộc bất đẳng thức về dấu bằng

**Bước 4: Các mặt của hình cầu $$\ell_2$$**
$$C = \{x : \lVert x \rVert_2 \leq 1\}$$

**Cấu trúc mặt:**
- **Chiều 0:** Mọi điểm biên đơn lẻ $$\{x\}$$ với $$\lVert x \rVert_2 = 1$$ (vô số điểm cực biên); gốc tọa độ **không** phải là một mặt
- **Chiều $$n$$:** Chính tập $$C$$ (cùng mặt rỗng $$\emptyset$$)
- **Không có mặt nào khác:** Vì hình cầu lồi chặt nên mọi siêu phẳng hỗ trợ chỉ tiếp xúc tại đúng một điểm; bản thân mặt cầu biên không lồi nên không phải là mặt

**Cấu trúc dàn:** $$\emptyset \subset \{x\} \subset C$$ với mỗi $$x$$ trên mặt cầu (không có dây chuyền nào dài hơn 3 phần tử).

</details>

---

## Mẹo thực hành

#### **Khi kiểm tra tính lồi:**
- Dùng trực tiếp định nghĩa: kiểm tra $$\theta x + (1-\theta) y \in C$$
- Áp dụng các phép toán bảo toàn tính lồi
- Kiểm tra xem tập có phải là tập mức dưới của một hàm lồi hay không

#### **Khi tính bao lồi:**
- Xác định trước các điểm cực biên
- Dùng định lý Carathéodory để giới hạn số điểm trong tổ hợp lồi
- Kiểm chứng lại bằng các siêu phẳng hỗ trợ

#### **Khi làm việc với hình nón đối ngẫu:**
- Nhớ định nghĩa: $$K^* = \{y : y^T x \geq 0, \forall x \in K\}$$
- Tận dụng tính tự đối ngẫu của các hình nón quen thuộc ($$\mathbb{R}_+^n$$, hình nón bậc hai, $$\mathbb{S}_+^n$$)
- Liên hệ với bất đẳng thức tổng quát đối ngẫu

---

## **Tổng kết**

### **Các tập lồi quan trọng:**

| Tập | Định nghĩa | Ghi chú / Ví dụ |
|-----|------------|-----------------|
| **Tập affine** | $$\{x : Ax = b\}$$ | Không gian con, siêu phẳng |
| **Bao lồi** | $$\text{conv}(S) = \{\sum \theta_i x_i : \sum \theta_i = 1, \theta_i \geq 0\}$$ | Tập lồi nhỏ nhất chứa $$S$$ |
| **Hình nón** | $$\theta x \in C$$ $$\forall x \in C, \theta \geq 0$$ | Góc phần tư không âm |
| **Đa diện** | $$\{x : Ax \leq b, Cx = d\}$$ | Giao của các nửa không gian và siêu phẳng |
| **Ellipsoid** | $$\{x : (x-x_c)^TP^{-1}(x-x_c) \leq 1\}$$ | $$P \succ 0$$ |
| **Hình cầu chuẩn** | $$\{x : \|x - x_c\| \leq r\}$$ | Hình cầu $$\ell_1, \ell_2, \ell_\infty$$ |

### **Các phép toán bảo toàn tính lồi:**

| Phép toán | Biểu thức / Ví dụ |
|-----------|-------------------|
| **Giao** | $$C_1 \cap C_2$$ lồi nếu $$C_1, C_2$$ lồi |
| **Ánh xạ affine** | $$f(C) = \{Ax + b : x \in C\}$$ |
| **Hàm phối cảnh** | $$P(x, t) = x/t$$ |
| **Hàm tuyến tính-phân thức** | $$f(x) = \frac{Ax + b}{c^Tx + d}$$ |

### **Phân tách và hỗ trợ:**

- **Siêu phẳng phân tách:** Tồn tại $$a \ne 0$$ sao cho $$a^Tx \leq b$$ $$\forall x \in C_1$$ và $$a^Tx \geq b$$ $$\forall x \in C_2$$
- **Siêu phẳng hỗ trợ:** $$\{x : a^Tx = a^Tx_0\}$$ tại điểm biên $$x_0$$
- **Hình nón đối ngẫu:** $$K^* = \{y : y^Tx \geq 0, \forall x \in K\}$$
- **Hình nón tự đối ngẫu:** $$K^* = K$$ (ví dụ: góc phần tư không âm, hình nón nửa xác định dương)

### **Các định lý quan trọng:**

- **Carathéodory:** Mọi điểm trong $$\text{conv}(S) \subset \mathbb{R}^n$$ là tổ hợp lồi của tối đa $$n+1$$ điểm thuộc $$S$$
- **Radon:** Mọi tập gồm $$n+2$$ điểm trong $$\mathbb{R}^n$$ đều chia được thành 2 tập con rời nhau có bao lồi giao nhau
- **Helly:** Nếu $$C_1, \ldots, C_m$$ là các tập lồi trong $$\mathbb{R}^n$$ ($$m \geq n+1$$) và mọi họ con gồm $$n+1$$ tập đều có giao khác rỗng, thì $$\bigcap_{i=1}^m C_i \neq \emptyset$$

---

## Tài liệu tham khảo

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press.
   - Chapter 2: Convex Sets
   - Exercises 2.1-2.27

2. **Rockafellar, R. T.** (1970). *Convex Analysis*. Princeton University Press.

3. **Ziegler, G. M.** (1995). *Lectures on Polytopes*. Springer-Verlag.
