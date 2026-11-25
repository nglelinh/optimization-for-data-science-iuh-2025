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

Mỗi ràng buộc trong bài toán thực tế — "ngân sách không vượt quá 10 tỷ", "sản lượng không âm", "tổng tỷ trọng danh mục bằng 100%" — thực chất đang cắt ra một tập hợp điểm trong không gian $$\mathbb{R}^n$$. Miền khả thi cuối cùng nơi thuật toán được phép tìm kiếm chính là phần **giao** của tất cả các tập hợp đó. Vì vậy, lý thuyết tập hợp không phải lý thuyết trừu tượng xa vời, mà là ngữ pháp cơ bản để phát biểu đúng mọi bài toán tối ưu có ràng buộc.

Bài học này củng cố ký hiệu tập hợp, các phép toán hợp–giao–bù, ánh xạ và tích Descartes gắn liền với không gian biến quyết định.

## Kiến thức cần nhớ: Ngữ pháp tập hợp trong tối ưu hóa

- **Ký hiệu và đặc tả tập hợp:** Cách viết miền khả thi theo thuộc tính $$D = \{x \in \mathbb{R}^n : g_i(x) \le 0, h_j(x) = 0\}$$ giúp phân biệt rõ biến quyết định, tham số và miền xác định.
- **Phép giao ($$\cap$$) và tính bảo toàn:** Giao của nhiều tập ràng buộc mô tả việc thỏa mãn *đồng thời* mọi điều kiện. Một phép màu lớn của Chương 02 là giao của họ bất kỳ các tập lồi luôn là tập lồi (còn phép hợp thì thường không!).
- **Tích Descartes ($$A \times B$$):** Là cách xây dựng không gian nhiều biến (như $$\mathbb{R}^n = \mathbb{R} \times \cdots \times \mathbb{R}$$) và đặc biệt là không gian $$\mathbb{R}^n \times \mathbb{R}$$ chứa **epigraph** (biểu đồ trên) của hàm số.
- **Ánh xạ, miền xác định và ảnh ngược:** Liên kết tập nghiệm của bài toán với ảnh ngược $$f^{-1}((-\infty, \alpha])$$ — chính là **tập mức dưới** (sublevel set) đóng vai trò trung tâm khi định nghĩa hàm lồi và hàm giả lồi.

### Giải thích: Dựng miền khả thi từ phép giao ba tập ràng buộc

Xét bài toán tìm cực tiểu của $$f(x_1, x_2) = -2x_1 - 3x_2$$ trên miền $$D = S_1 \cap S_2 \cap S_3 \subset \mathbb{R}^2$$ với:

- $$S_1 = \{(x_1, x_2) : x_1 + x_2 \le 4\}$$ (tổng tài nguyên không quá 4),
- $$S_2 = \{(x_1, x_2) : x_1 \ge 0,\ x_2 \ge 0\}$$ (không âm),
- $$S_3 = \{(x_1, x_2) : x_1 \le 3\}$$ (giới hạn sản phẩm 1).

1. **Xác định các đỉnh của tập giao $$D$$:**
   - Giao $$x_1 = 0$$ và $$x_2 = 0$$ cho đỉnh $$A = (0, 0)$$.
   - Giao $$x_1 = 3$$ và $$x_2 = 0$$ cho đỉnh $$B = (3, 0)$$.
   - Giao $$x_1 = 3$$ và $$x_1 + x_2 = 4$$ cho đỉnh $$C = (3, 1)$$.
   - Giao $$x_1 = 0$$ và $$x_1 + x_2 = 4$$ cho đỉnh $$E = (0, 4)$$.
2. **Đánh giá hàm mục tiêu tuyến tính tại bốn đỉnh:**
   - $$f(0, 0) = 0$$;
   - $$f(3, 0) = -6$$;
   - $$f(3, 1) = -2(3) - 3(1) = -9$$;
   - $$f(0, 4) = -2(0) - 3(4) = -12$$.
3. **Kết luận:** Điểm tối ưu toàn cục trên tập giao $$D$$ là $$x^* = (0, 4)$$ với $$f(x^*) = -12$$. Nếu bỏ bớt ràng buộc $$S_1$$, miền giao trở nên không bị chặn và hàm có thể giảm xuống $$-\infty$$!

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
