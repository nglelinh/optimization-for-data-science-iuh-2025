---
layout: post
title: 00-03-01 Cơ sở Lý thuyết tập hợp
chapter: '00'
order: 12
owner: GitHub Copilot
lang: vi
categories:
- chapter00
lesson_type: required
---

Bài học này trình bày các khái niệm cơ bản của lý thuyết tập hợp — nền tảng toán học để mô tả bài toán tối ưu hóa, các ràng buộc và vùng khả thi.

---

## Giới thiệu về lý thuyết tập hợp

Lý thuyết tập hợp là nền tảng của toán học hiện đại và rất cần thiết để phát biểu chính xác các khái niệm tối ưu hóa. Một **tập hợp** là một sưu tập các đối tượng phân biệt, gọi là các phần tử của tập hợp đó.

### Ký hiệu cơ bản

- **Ký hiệu liệt kê tập hợp:** $$A = \{1, 2, 3, 4\}$$
- **Quan hệ thuộc:** $$x \in A$$ ($$x$$ thuộc $$A$$) hoặc $$x \notin A$$ ($$x$$ không thuộc $$A$$)
- **Tập rỗng:** $$\emptyset = \{\}$$ (tập hợp không chứa phần tử nào)
- **Ký hiệu theo tính chất đặc trưng:** $$A = \{x : P(x)\}$$ (tập hợp tất cả các phần tử $$x$$ thỏa mãn tính chất $$P(x)$$)

### Ví dụ

- $$A = \{1, 2, 3, 4\}$$ (liệt kê tường minh)
- $$B = \{x \in \mathbb{R} : x^2 < 4\} = (-2, 2)$$ (mô tả theo tính chất đặc trưng)
- $$C = \{x \in \mathbb{Z} : x \text{ là số chẵn}\}$$ (tập tất cả các số nguyên chẵn)

---

## Các phép toán tập hợp cơ bản

### Tập hợp và tập con

- **Tập con:** $$A \subseteq B$$ nghĩa là mọi phần tử của $$A$$ đều thuộc $$B$$.
- **Tập con thực sự:** $$A \subset B$$ nghĩa là $$A \subseteq B$$ và $$A \neq B$$.
- **Hai tập hợp bằng nhau:** $$A = B$$ khi và chỉ khi $$A \subseteq B$$ và $$B \subseteq A$$.

**Ví dụ:**
- $$\{1, 2\} \subseteq \{1, 2, 3, 4\}$$
- $$\{1, 2\} \subset \{1, 2, 3, 4\}$$
- $$\emptyset \subseteq A$$ với mọi tập hợp $$A$$

### Hợp và giao

**Hợp ($$A \cup B$$):** tập hợp tất cả các phần tử thuộc $$A$$ hoặc thuộc $$B$$ (hoặc cả hai):
$$A \cup B = \{x : x \in A \text{ hoặc } x \in B\}$$

**Giao ($$A \cap B$$):** tập hợp tất cả các phần tử thuộc đồng thời cả $$A$$ và $$B$$:
$$A \cap B = \{x : x \in A \text{ và } x \in B\}$$

**Ví dụ:**
- Nếu $$A = \{1, 2, 3\}$$ và $$B = \{3, 4, 5\}$$, thì:
  - $$A \cup B = \{1, 2, 3, 4, 5\}$$
  - $$A \cap B = \{3\}$$

**Hai tập hợp rời nhau:** $$A$$ và $$B$$ rời nhau nếu $$A \cap B = \emptyset$$.

### Phần bù và hiệu

**Phần bù ($$A^c$$):** tập hợp tất cả các phần tử không thuộc $$A$$ (trong một tập vũ trụ $$U$$ cho trước):
$$A^c = \{x \in U : x \notin A\}$$

**Hiệu tập hợp ($$A \setminus B$$):** tập hợp các phần tử thuộc $$A$$ nhưng không thuộc $$B$$:
$$A \setminus B = \{x : x \in A \text{ và } x \notin B\}$$

**Hiệu đối xứng:** $$(A \setminus B) \cup (B \setminus A) = (A \cup B) \setminus (A \cap B)$$

### Các luật của phép toán tập hợp

**Luật giao hoán:**
- $$A \cup B = B \cup A$$
- $$A \cap B = B \cap A$$

**Luật kết hợp:**
- $$(A \cup B) \cup C = A \cup (B \cup C)$$
- $$(A \cap B) \cap C = A \cap (B \cap C)$$

**Luật phân phối:**
- $$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$$
- $$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$$

**Luật De Morgan:**
- $$(A \cup B)^c = A^c \cap B^c$$
- $$(A \cap B)^c = A^c \cup B^c$$

---

## Các tập số quan trọng

Nắm rõ hệ thống phân cấp các tập số giúp xác định chính xác miền biến của bài toán tối ưu hóa:

### Số tự nhiên
$$\mathbb{N} = \{1, 2, 3, 4, \ldots\}$$
(Đôi khi bao gồm cả số 0: $$\mathbb{N}_0 = \{0, 1, 2, 3, \ldots\}$$)

### Số nguyên
$$\mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}$$

### Số hữu tỉ
$$\mathbb{Q} = \left\{\frac{p}{q} : p, q \in \mathbb{Z}, q \neq 0\right\}$$

Gồm mọi số có thể biểu diễn dưới dạng phân số của hai số nguyên.

### Số thực
$$\mathbb{R}$$ gồm tất cả các số hữu tỉ và số vô tỉ (như $$\pi$$, $$e$$, $$\sqrt{2}$$).

### Số phức
$$\mathbb{C} = \{a + bi : a, b \in \mathbb{R}, i^2 = -1\}$$

**Quan hệ bao hàm:** $$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$$

---

## Hàm số: Miền xác định và miền giá trị

Một **hàm số** $$f: A \to B$$ là quy tắc gán cho mỗi phần tử thuộc tập $$A$$ đúng một phần tử thuộc tập $$B$$.

### Các khái niệm chính

- **Miền xác định (domain):** tập $$A$$ gồm tất cả các giá trị đầu vào hợp lệ.
- **Tập đích (codomain):** tập $$B$$ chứa các giá trị đầu ra có thể nhận.
- **Miền giá trị / ảnh (range):** tập hợp tất cả các giá trị đầu ra thực tế: $$\text{Range}(f) = \{f(x) : x \in A\} \subseteq B$$.

**Ví dụ:** Với $$f: \mathbb{R} \to \mathbb{R}$$ định nghĩa bởi $$f(x) = x^2$$:
- Miền xác định: $$\mathbb{R}$$
- Tập đích: $$\mathbb{R}$$
- Miền giá trị: $$[0, \infty)$$

### Phân loại ánh xạ (hàm số)

**Đơn ánh (injective):** hai phần tử khác nhau trong miền xác định có ảnh khác nhau:
$$f(x_1) = f(x_2) \implies x_1 = x_2$$

**Toàn ánh (surjective):** mọi phần tử trong tập đích đều là ảnh của ít nhất một phần tử trong miền xác định:
Với mọi $$y \in B$$, tồn tại $$x \in A$$ sao cho $$f(x) = y$$.

**Song ánh (bijective):** vừa là đơn ánh vừa là toàn ánh, tạo ra sự tương ứng một-một giữa miền xác định và tập đích.

**Ví dụ:**
- $$f(x) = 2x$$ từ $$\mathbb{R}$$ vào $$\mathbb{R}$$ là song ánh.
- $$f(x) = x^2$$ từ $$\mathbb{R}$$ vào $$\mathbb{R}$$ không là đơn ánh và cũng không là toàn ánh.
- $$f(x) = x^2$$ từ $$[0, \infty)$$ vào $$[0, \infty)$$ là song ánh.

---

## Bất đẳng thức

Bất đẳng thức là công cụ quen thuộc trong tối ưu hóa vì phần lớn ràng buộc được biểu diễn dưới dạng bất đẳng thức.

### Các ký hiệu bất đẳng thức cơ bản

- $$a < b$$: $$a$$ nhỏ hơn hẳn $$b$$
- $$a \leq b$$: $$a$$ nhỏ hơn hoặc bằng $$b$$
- $$a > b$$: $$a$$ lớn hơn hẳn $$b$$
- $$a \geq b$$: $$a$$ lớn hơn hoặc bằng $$b$$

### Tính chất của bất đẳng thức

1. **Tính bắc cầu:** Nếu $$a \leq b$$ và $$b \leq c$$, thì $$a \leq c$$.
2. **Cộng hai vế:** Nếu $$a \leq b$$, thì $$a + c \leq b + c$$ với mọi $$c \in \mathbb{R}$$.
3. **Nhân với số dương:** Nếu $$a \leq b$$ và $$c > 0$$, thì $$ac \leq bc$$.
4. **Nhân với số âm:** Nếu $$a \leq b$$ và $$c < 0$$, thì $$ac \geq bc$$ (chiều bất đẳng thức đảo ngược).

### Ký hiệu khoảng

- **Khoảng mở:** $$(a, b) = \{x \in \mathbb{R} : a < x < b\}$$
- **Đoạn đóng:** $$[a, b] = \{x \in \mathbb{R} : a \leq x \leq b\}$$
- **Khoảng nửa mở:** $$[a, b)$$, $$(a, b]$$
- **Khoảng không bị chặn:** $$(-\infty, a)$$, $$[a, \infty)$$, $$(-\infty, \infty) = \mathbb{R}$$

---

## Ứng dụng trong tối ưu hóa

Các khái niệm của lý thuyết tập hợp xuất hiện trực tiếp trong mô hình hóa và phân tích bài toán tối ưu hóa:

### 1. Vùng khả thi

**Vùng khả thi** là tập hợp tất cả các điểm thỏa mãn đồng thời mọi ràng buộc:
$$S = \{x \in \mathbb{R}^n : g_i(x) \leq 0, i = 1, \ldots, m; h_j(x) = 0, j = 1, \ldots, p\}$$

### 2. Tập mức

Với hàm số $$f: \mathbb{R}^n \to \mathbb{R}$$, **tập mức** tại mức $$c$$ là:
$$L_c = \{x \in \mathbb{R}^n : f(x) = c\}$$

### 3. Điều kiện ràng buộc

Các tính chất hình học và tôpô của tập ràng buộc (chẳng hạn tính đóng hoặc có phần trong khác rỗng) ảnh hưởng trực tiếp đến sự tồn tại và đặc trưng của nghiệm tối ưu.

### 4. Phân tích hội tụ

Ngôn ngữ tập hợp, dãy số và giới hạn giúp phân tích xem thuật toán tối ưu hóa có hội tụ về nghiệm tối ưu hay không.

### 5. Các phép toán tập hợp trong bài toán tối ưu

- **Giao:** xác định tập điểm thỏa mãn đồng thời nhiều ràng buộc.
- **Hợp:** gộp các vùng khả thi từ nhiều kịch bản khác nhau.
- **Phần bù:** xác định miền không khả thi.

**Ví dụ:** Trong quy hoạch tuyến tính, vùng khả thi có dạng:
$$S = \{x \in \mathbb{R}^n : Ax \leq b, x \geq 0\} = \bigcap_{i=1}^{m} \{x : a_i^T x \leq b_i\} \cap \{x : x \geq 0\}$$

Đây là giao của các nửa không gian đóng, minh họa cách phép toán tập hợp xuất hiện tự nhiên khi xây dựng bài toán tối ưu hóa.

Nắm vững lý thuyết tập hợp cung cấp nền tảng chặt chẽ để phát biểu chính xác các bài toán tối ưu hóa và phân tích tính chất của chúng một cách có hệ thống.
