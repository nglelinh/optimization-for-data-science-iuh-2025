---
layout: post
title: 00-03-02 Tôpô trong Giải tích thực
chapter: '00'
order: 13
owner: GitHub Copilot
lang: vi
categories:
- chapter00
lesson_type: required
---

Bài học này trình bày các khái niệm tôpô thiết yếu trong giải tích thực — nền tảng để hiểu cấu trúc vùng khả thi, tính liên tục và sự tồn tại nghiệm tối ưu trong các bài toán tối ưu hóa.

---

## Giới thiệu về tôpô

Tôpô nghiên cứu những tính chất của không gian được bảo toàn dưới các phép biến đổi liên tục. Trong tối ưu hóa, các khái niệm tôpô giúp ta phân tích cấu trúc của vùng khả thi và hành vi của hàm số, đặc biệt là điều kiện để nghiệm tối ưu tồn tại.

### Không gian metric và khoảng cách

Trước khi xét các khái niệm tôpô, ta cần định nghĩa khoảng cách. Trong $$\mathbb{R}^n$$, **khoảng cách Euclid** chuẩn giữa hai điểm $$\mathbf{x}$$ và $$\mathbf{y}$$ là:

$$d(\mathbf{x}, \mathbf{y}) = \|\mathbf{x} - \mathbf{y}\|_2 = \sqrt{\sum_{i=1}^n (x_i - y_i)^2}$$

### Hình cầu mở và lân cận

**Hình cầu mở** tâm $$\mathbf{x}_0$$ với bán kính $$\epsilon > 0$$ được định nghĩa là:

$$B(\mathbf{x}_0, \epsilon) = \{\mathbf{y} \in \mathbb{R}^n : d(\mathbf{x}_0, \mathbf{y}) < \epsilon\}$$

Đây là tập hợp tất cả các điểm cách $$\mathbf{x}_0$$ một khoảng nhỏ hơn hẳn $$\epsilon$$.

**Ví dụ:**
- Trong $$\mathbb{R}$$: $$B(0, 1) = (-1, 1)$$ (khoảng mở).
- Trong $$\mathbb{R}^2$$: $$B(\mathbf{0}, 1) = \{(x, y) : x^2 + y^2 < 1\}$$ (đĩa đơn vị mở).

---

## Tập mở

Một **tập mở** là tập hợp **không chứa bất kỳ điểm biên nào của nó**.

### Định nghĩa chính thức

Một tập $$S \subseteq \mathbb{R}^n$$ được gọi là **mở** nếu với mọi điểm $$\mathbf{x} \in S$$, tồn tại một số thực dương $$\epsilon > 0$$ sao cho hình cầu mở $$B(\mathbf{x}, \epsilon)$$ nằm hoàn toàn trong $$S$$:

$$\forall \mathbf{x} \in S, \exists \epsilon > 0 : B(\mathbf{x}, \epsilon) \subseteq S$$

### Ý nghĩa trực quan

Với một tập mở, tại bất kỳ điểm nào thuộc tập, ta luôn có thể dịch chuyển một đoạn đủ nhỏ theo mọi hướng mà vẫn nằm bên trong tập hợp đó.

### Ví dụ về tập mở

**Trong $$\mathbb{R}$$:**
- $$(0, 1) = \{x : 0 < x < 1\}$$
- $$(-\infty, 5) = \{x : x < 5\}$$
- Toàn bộ $$\mathbb{R}$$

**Trong $$\mathbb{R}^2$$:**
- $$\{(x, y) : x^2 + y^2 < 1\}$$ (đĩa đơn vị mở)
- $$\{(x, y) : x > 0, y > 0\}$$ (góc phần tư thứ nhất, không bao gồm các trục tọa độ)
- Toàn bộ $$\mathbb{R}^2$$

**Trong $$\mathbb{R}^n$$:**
- Mọi hình cầu mở $$B(\mathbf{x}_0, r)$$
- Toàn bộ $$\mathbb{R}^n$$
- $$\emptyset$$ (tập rỗng, là tập mở theo quy ước hiển nhiên)

### Tính chất của tập mở

1. Hợp của một họ bất kỳ các tập mở là tập mở.
2. Giao của hữu hạn các tập mở là tập mở.
3. $$\mathbb{R}^n$$ và $$\emptyset$$ đều là tập mở.

---

## Tập đóng

Một **tập đóng** là tập hợp chứa mọi điểm biên của nó. Tương đương, tập $$S$$ đóng khi và chỉ khi phần bù $$\mathbb{R}^n \setminus S$$ của nó là một **tập mở**.

### Định nghĩa theo dãy

Một tập $$S$$ là **đóng** nếu nó chứa mọi điểm giới hạn của mình. Nghĩa là, nếu một dãy điểm $$(\mathbf{x}_n)$$ trong $$S$$ hội tụ về $$\mathbf{x}$$ thì $$\mathbf{x}$$ cũng thuộc $$S$$:

$$\text{Nếu } \mathbf{x}_n \in S \text{ với mọi } n \text{ và } \lim_{n \to \infty} \mathbf{x}_n = \mathbf{x}, \text{ thì } \mathbf{x} \in S$$

### Ví dụ về tập đóng

**Trong $$\mathbb{R}$$:**
- $$[0, 1] = \{x : 0 \leq x \leq 1\}$$
- $$[a, \infty) = \{x : x \geq a\}$$
- $$\{0\}$$ (tập gồm một điểm)
- $$\mathbb{Z}$$ (tập các số nguyên)

**Trong $$\mathbb{R}^2$$:**
- $$\{(x, y) : x^2 + y^2 \leq 1\}$$ (đĩa đơn vị đóng)
- $$\{(x, y) : x \geq 0, y \geq 0\}$$ (góc phần tư thứ nhất, bao gồm cả các trục tọa độ)
- $$\{(0, 0)\}$$ (tập gồm một điểm)

**Trong $$\mathbb{R}^n$$:**
- Mọi hình cầu đóng $$\overline{B}(\mathbf{x}_0, r) = \{\mathbf{x} : d(\mathbf{x}, \mathbf{x}_0) \leq r\}$$
- Toàn bộ $$\mathbb{R}^n$$
- $$\emptyset$$ (tập rỗng)
- Mọi tập hữu hạn

### Tính chất của tập đóng

1. Giao của một họ bất kỳ các tập đóng là tập đóng.
2. Hợp của hữu hạn các tập đóng là tập đóng.
3. $$\mathbb{R}^n$$ và $$\emptyset$$ đều là tập đóng.

### Lưu ý quan trọng

Một tập hợp có thể rơi vào một trong bốn trường hợp:
- **Mở nhưng không đóng:** $$(0, 1)$$
- **Đóng nhưng không mở:** $$[0, 1]$$
- **Vừa mở vừa đóng:** $$\mathbb{R}^n$$, $$\emptyset$$
- **Không mở cũng không đóng:** $$[0, 1)$$, $$(0, 1]$$

---

## Biên, phần trong và bao đóng

### Biên

**Biên** của tập $$S$$, ký hiệu $$\partial S$$, là tập các điểm nằm ở "rìa" của $$S$$. Một điểm $$\mathbf{x}$$ là **điểm biên** của $$S$$ nếu mọi hình cầu mở tâm $$\mathbf{x}$$ đều giao với cả $$S$$ lẫn phần bù $$S^c$$:

$$\partial S = \{\mathbf{x} : \forall \epsilon > 0, B(\mathbf{x}, \epsilon) \cap S \neq \emptyset \text{ and } B(\mathbf{x}, \epsilon) \cap S^c \neq \emptyset\}$$

### Phần trong

**Phần trong** của tập $$S$$, ký hiệu $$S^\circ$$ hay $$\text{int}(S)$$, là tập tất cả các điểm nằm hoàn toàn bên trong $$S$$ (không chứa điểm biên):

$$S^\circ = \{\mathbf{x} \in S : \exists \epsilon > 0, B(\mathbf{x}, \epsilon) \subseteq S\}$$

### Bao đóng

**Bao đóng** của tập $$S$$, ký hiệu $$\overline{S}$$ hay $$\text{cl}(S)$$, là tập đóng nhỏ nhất chứa $$S$$:

$$\overline{S} = S \cup \partial S$$

### Ví dụ minh họa

Với khoảng $$S = [0, 1)$$ trong $$\mathbb{R}$$:
- **Phần trong:** $$S^\circ = (0, 1)$$
- **Biên:** $$\partial S = \{0, 1\}$$
- **Bao đóng:** $$\overline{S} = [0, 1]$$

Với đĩa mở $$S = \{(x, y) : x^2 + y^2 < 1\}$$ trong $$\mathbb{R}^2$$:
- **Phần trong:** $$S^\circ = S$$ (vì $$S$$ đã là tập mở)
- **Biên:** $$\partial S = \{(x, y) : x^2 + y^2 = 1\}$$ (đường tròn đơn vị)
- **Bao đóng:** $$\overline{S} = \{(x, y) : x^2 + y^2 \leq 1\}$$ (đĩa đơn vị đóng)

---

## Tập compact

**Tập compact** là một trong những khái niệm quan trọng nhất của lý thuyết tối ưu hóa.

### Đặc trưng trong không gian Euclid

**Định lý Heine–Borel:** Trong không gian Euclid $$\mathbb{R}^n$$, một tập hợp là compact khi và chỉ khi nó vừa **đóng** vừa **bị chặn**.

- **Bị chặn:** tập $$S$$ bị chặn nếu nó nằm trong một hình cầu mở đủ lớn, tức tồn tại $$M > 0$$ và $$\mathbf{x}_0$$ sao cho $$S \subseteq B(\mathbf{x}_0, M)$$.
- **Đóng:** như định nghĩa ở phần trên.

### Ví dụ về tập compact

**Trong $$\mathbb{R}$$:**
- $$[a, b]$$ (mọi đoạn đóng và bị chặn)
- $$\{0\}$$ (tập gồm một điểm)
- Mọi tập hữu hạn

**Trong $$\mathbb{R}^2$$:**
- $$\{(x, y) : x^2 + y^2 \leq 1\}$$ (đĩa đơn vị đóng)
- $$[0, 1] \times [0, 1]$$ (hình vuông đơn vị đóng)
- Mọi tập hữu hạn điểm

**Trong $$\mathbb{R}^n$$:**
- Mọi hình cầu đóng $$\overline{B}(\mathbf{x}_0, r)$$
- Mọi hình hộp đóng và bị chặn $$[a_1, b_1] \times [a_2, b_2] \times \cdots \times [a_n, b_n]$$

### Các tập không compact

- $$(0, 1)$$ (bị chặn nhưng không đóng)
- $$[0, \infty)$$ (đóng nhưng không bị chặn)
- $$\mathbb{R}^n$$ (không bị chặn)
- $$\{1, 1/2, 1/3, 1/4, \ldots\}$$ (bị chặn nhưng không đóng, vì điểm giới hạn $$0$$ không thuộc tập)

---

## Tính liên tục của hàm số

### Liên tục tại một điểm

Hàm số $$f: A \to \mathbb{R}$$ được gọi là **liên tục tại điểm** $$\mathbf{c} \in A$$ nếu với mọi $$\varepsilon > 0$$, tồn tại $$\delta > 0$$ sao cho với mọi $$\mathbf{x} \in A$$:

$$\|\mathbf{x} - \mathbf{c}\| < \delta \implies |f(\mathbf{x}) - f(\mathbf{c})| < \varepsilon$$

**Ý nghĩa trực quan:** biến thiên đủ nhỏ ở đầu vào dẫn đến biến thiên nhỏ ở đầu ra.

### Liên tục trên một tập hợp

Hàm $$f$$ **liên tục trên $$A$$** nếu nó liên tục tại mọi điểm thuộc $$A$$.

### Đặc trưng qua dãy

Hàm $$f$$ liên tục tại $$\mathbf{c}$$ khi và chỉ khi với mọi dãy $$(\mathbf{x}_n)$$ trong $$A$$ hội tụ về $$\mathbf{c}$$:

$$\lim_{n \to \infty} f(\mathbf{x}_n) = f(\mathbf{c})$$

---

## Các định lý quan trọng cho tối ưu hóa

### Định lý giá trị cực trị (Extreme Value Theorem)

**Nếu $$f$$ liên tục trên một tập compact khác rỗng $$K$$ thì $$f$$ đạt giá trị lớn nhất và giá trị nhỏ nhất trên $$K$$.**

Đây là kết quả nền tảng trong tối ưu hóa: nó đảm bảo mọi hàm mục tiêu liên tục đều có nghiệm tối ưu trên vùng khả thi compact.

**Ý tưởng chứng minh:** Tính compact đảm bảo cận trên đúng (supremum) và cận dưới đúng (infimum) của $$f$$ trên $$K$$ thực sự đạt được tại các điểm thuộc $$K$$.

### Định lý giá trị trung gian (Intermediate Value Theorem)

**Nếu $$f$$ liên tục trên đoạn $$[a, b]$$ và $$y$$ nằm giữa $$f(a)$$ và $$f(b)$$ thì tồn tại $$c \in [a, b]$$ sao cho $$f(c) = y$$.**

Định lý này giúp chứng minh sự tồn tại nghiệm của các phương trình dạng $$f(x) = 0$$.

### Định lý Bolzano–Weierstrass

**Mọi dãy bị chặn trong $$\mathbb{R}^n$$ đều có ít nhất một dãy con hội tụ.**

Kết quả này là công cụ quan trọng khi chứng minh tính hội tụ của các thuật toán tối ưu hóa lặp.

### Định lý xấp xỉ Weierstrass

**Mọi hàm liên tục trên một đoạn đóng và bị chặn đều có thể được xấp xỉ đều bằng đa thức.**

Định lý này là cơ sở lý thuyết cho việc sử dụng các xấp xỉ đa thức trong thiết kế thuật toán tối ưu hóa.

---

## Ứng dụng trong tối ưu hóa

### 1. Sự tồn tại nghiệm

**Vùng khả thi compact đảm bảo nghiệm tối ưu tồn tại:**
- Nếu vùng khả thi $$S$$ compact (khác rỗng) và hàm mục tiêu $$f$$ liên tục thì bài toán $$\min_{\mathbf{x} \in S} f(\mathbf{x})$$ luôn có nghiệm.

### 2. Điều kiện chính quy của ràng buộc

Các tính chất tôpô của tập ràng buộc quyết định hiệu lực của điều kiện tối ưu và thuật toán:
- **Điểm chính quy:** điểm mà gradient của các ràng buộc hoạt động độc lập tuyến tính.
- **Phương pháp điểm trong:** đòi hỏi vùng khả thi có phần trong khác rỗng.

### 3. Phân tích hội tụ

Các tính chất tôpô giúp phân tích hành vi dãy nghiệm sinh ra bởi thuật toán:
- **Tính đóng:** đảm bảo điểm giới hạn của dãy điểm khả thi vẫn thuộc vùng khả thi.
- **Tính compact:** đảm bảo dãy lặp bị chặn luôn trích ra được dãy con hội tụ.

### 4. Cực trị địa phương và toàn cục

Khái niệm lân cận được dùng để phân biệt cực trị địa phương và toàn cục:
- **Cực tiểu địa phương:** $$f(\mathbf{x}^*) \leq f(\mathbf{x})$$ với mọi $$\mathbf{x}$$ khả thi thuộc một lân cận nào đó của $$\mathbf{x}^*$$.
- **Cực tiểu toàn cục:** $$f(\mathbf{x}^*) \leq f(\mathbf{x})$$ với mọi $$\mathbf{x}$$ thuộc toàn bộ vùng khả thi.

### 5. Phân tích vùng khả thi

Phân loại cấu trúc tập ràng buộc:
- **Ràng buộc bất đẳng thức/đẳng thức tuyến tính:** xác định các tập đóng (nửa không gian đóng, siêu phẳng).
- **Ràng buộc phi tuyến:** có thể tạo ra tập không mở cũng không đóng (nếu có bất đẳng thức nghiêm ngặt).
- **Vùng khả thi compact:** đảm bảo tồn tại nghiệm tối ưu cho hàm mục tiêu liên tục.

### Ví dụ: Tối ưu danh mục đầu tư

Xét bài toán cực tiểu hóa rủi ro danh mục đầu tư với các ràng buộc:

$$\begin{align}
\min_{\mathbf{w}} \quad & \mathbf{w}^T \mathbf{\Sigma} \mathbf{w} \\
\text{s.t.} \quad & \mathbf{1}^T \mathbf{w} = 1 \\
& \mathbf{w} \geq \mathbf{0}
\end{align}$$

Vùng khả thi $$S = \{\mathbf{w} : \mathbf{1}^T \mathbf{w} = 1, \mathbf{w} \geq \mathbf{0}\}$$ có các tính chất:
- **Đóng:** là giao của các tập đóng.
- **Bị chặn:** ràng buộc $$\mathbf{1}^T \mathbf{w} = 1$$ kết hợp với $$\mathbf{w} \geq \mathbf{0}$$ kéo theo $$0 \leq w_i \leq 1$$ với mọi $$i$$.
- **Compact:** vì vừa đóng vừa bị chặn trong $$\mathbb{R}^n$$.

Do hàm mục tiêu $$\mathbf{w}^T \mathbf{\Sigma} \mathbf{w}$$ liên tục và $$S$$ là tập compact khác rỗng, định lý giá trị cực trị đảm bảo bài toán luôn có danh mục tối ưu.

Tôpô và giải tích thực cung cấp cơ sở chặt chẽ để chứng minh sự tồn tại nghiệm và tính hội tụ của các thuật toán tối ưu hóa, phục vụ cả phân tích lý thuyết lẫn triển khai thực tế.
