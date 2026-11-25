---
layout: post
title: 05-02 Quy Hoạch Bậc Hai (QP)
chapter: '05'
order: 4
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
lesson_type: required
---

Năm 1952, Harry Markowitz đặt một câu hỏi làm thay đổi hoàn toàn Phố Wall: nếu chỉ tối đa hóa lợi nhuận kỳ vọng bằng Quy hoạch Tuyến tính (LP), mô hình sẽ dồn 100% tiền vào đúng một cổ phiếu rủi ro nhất! Làm sao vừa tối đa hóa lợi nhuận tuyến tính $$\mu^T x$$, vừa giữ rủi ro phương sai $$x^T \Sigma x$$ ở mức thấp nhất? Câu trả lời chính là **Quy hoạch Bậc hai (Quadratic Programming - QP)** — bài toán giữ nguyên tập khả thi đa diện tuyến tính của LP nhưng nâng hàm mục tiêu lên dạng bậc hai lồi $$\frac{1}{2} x^T Q x + c^T x$$.

Từ tối ưu danh mục đầu tư, điều khiển dự báo mô hình (MPC) trên xe tự lái và tên lửa SpaceX, cho đến huấn luyện máy vector hỗ trợ (SVM) — QP là một trong những bài toán được giải hàng tỷ lần mỗi ngày trong công nghiệp.

## Bản đồ kiến thức nền: Cấu trúc đại số và hình học của QP

Để nắm vững QP cả về lý thuyết lẫn thực hành, hãy tập trung vào bốn trụ cột:

- **Điều kiện lồi $$Q \succeq 0$$ (Positive Semidefiniteness):** Hàm mục tiêu $$f(x) = \frac{1}{2} x^T Q x + c^T x$$ có Hessian là $$Q$$ (với $$Q = Q^T$$). Bài toán QP là lồi khi và chỉ khi $$Q \in \mathbb{S}_+^n$$ (mọi trị riêng của $$Q$$ đều không âm). Nếu $$Q \succ 0$$ (xác định dương chặt), hàm lồi chặt và nghiệm tối ưu là duy nhất!
- **Hình học Ellipsoid trên Đa diện:** Khác với LP (đường đồng mức là mặt phẳng song song nên nghiệm luôn ở đỉnh), đường đồng mức của QP là các **ellipsoid đồng tâm** quanh điểm cực tiểu tự do $$x_{\text{unc}} = -Q^{-1}c$$. Do đó, nghiệm tối ưu của QP có thể nằm ở đỉnh, giữa một cạnh/mặt, hoặc nằm gọn bên trong đa diện!
- **Chuyển đổi về dạng chuẩn & Hệ KKT tuyến tính:** Khi không có ràng buộc bất đẳng thức (chỉ có $$Ax = b$$), bài toán QP giải được chính xác bằng **một hệ phương trình tuyến tính KKT duy nhất**. Khi có ràng buộc bất đẳng thức $$Gx \le h$$, các thuật toán tập tích cực (active-set), điểm trong (interior-point) hoặc ADMM (như bộ giải OSQP) giải cực nhanh.
- **Mối liên hệ mật thiết với LP & Least Squares:** Đặt $$Q = 0$$ thì QP thu gọn về LP; bỏ hết ràng buộc và đặt $$Q = 2A^T A,\; c = -2A^T b$$ thì QP chính là Bình phương tối thiểu tuyến tính!

### Khung giải thích (nên đọc chậm): Giải tay bài toán phân bổ danh mục đầu tư Markowitz (QP 2 tài sản)

Giả sử bạn có 1 đơn vị vốn ($$x_1 + x_2 = 1,\; x_1, x_2 \ge 0$$) phân bổ vào 2 tài sản có ma trận hiệp phương sai rủi ro $$Q = \begin{pmatrix} 2 & 0 \\ 0 & 4 \end{pmatrix}$$ và lợi nhuận kỳ vọng $$\mu = (1,\; 2)^T$$. Ta giải QP:
$$\min_{x_1, x_2} \; \frac{1}{2} x^T Q x - \mu^T x = x_1^2 + 2x_2^2 - x_1 - 2x_2 \quad \text{s.t.} \quad x_1 + x_2 = 1,\; x_1, x_2 \ge 0.$$

1. **Bước 1 — Kiểm tra tính lồi:** $$Q = \operatorname{diag}(2, 4)$$ có trị riêng $$\lambda_1 = 2 > 0,\; \lambda_2 = 4 > 0 \implies Q \succ 0$$. Vậy QP lồi chặt và có nghiệm duy nhất.
2. **Bước 2 — Khử ràng buộc đẳng thức $$x_2 = 1 - x_1$$ (với $$x_1 \in [0, 1]$$):**
   $$\phi(x_1) = x_1^2 + 2(1 - x_1)^2 - x_1 - 2(1 - x_1) = x_1^2 + 2 - 4x_1 + 2x_1^2 - x_1 - 2 + 2x_1 = 3x_1^2 - 3x_1.$$
3. **Bước 3 — Tìm cực tiểu:**
   $$\phi'(x_1) = 6x_1 - 3 = 0 \implies x_1^\star = 0.5.$$
   Vì $$0.5 \in [0, 1]$$, ta suy ra $$x_2^\star = 0.5$$.
4. **Bước 4 — So sánh với nghiệm LP (nếu bỏ số hạng bậc hai rủi ro):**
   Nếu giải LP $$\min (-x_1 - 2x_2)$$, ta sẽ đặt toàn bộ vốn vào tài sản 2: $$(0, 1)$$. Nhờ số hạng bậc hai rủi ro trong QP, nghiệm tối ưu tự động **đa dạng hóa** về $$(0.5, 0.5)$$ (nằm giữa đoạn thẳng khả thi, không nằm ở hai đỉnh!) với giá trị tối ưu $$f^\star = 3(0.25) - 3(0.5) = -0.75$$.

---

Một **bài toán quy hoạch bậc hai** (Quadratic Programming - QP) là bài toán tối ưu hóa lồi trong đó hàm mục tiêu là hàm bậc hai lồi và tất cả các ràng buộc đều là hàm affine. Dạng tổng quát của bài toán quy hoạch bậc hai được phát biểu như sau:

### Bài toán Quy hoạch Bậc hai tổng quát
$$
\begin{align}
    \text{minimize}_{x} \quad &\frac{1}{2}x^T P x + q^T x + r \\
    \text{subject to} \quad &Gx \preceq h \\
    &Ax = b
\end{align}
$$

**trong đó:**
- $$P \in \mathbb{S}_{+}^n$$ (ma trận đối xứng nửa xác định dương)
- $$G \in \mathbb{R}^{m \times n}$$ (ma trận ràng buộc bất đẳng thức)
- $$A \in \mathbb{R}^{p \times n}$$ (ma trận ràng buộc đẳng thức)
- $$x \in \mathbb{R}^n$$ (vectơ biến quyết định)

**Các tính chất chính của QP:**
- Hằng số $$r$$ trong hàm mục tiêu không làm thay đổi nghiệm tối ưu $$x^*$$ nên thường có thể bỏ qua khi giải.
- Nếu điều kiện $$P \in \mathbb{S}_{+}^n$$ không được thỏa mãn, bài toán không phải là bài toán lồi.
- Trong tối ưu hóa lồi, khi nhắc đến QP, điều kiện $$P \in \mathbb{S}_{+}^n$$ luôn được ngầm giả định.
- Về mặt hình học, bài toán QP tìm cực tiểu của một hàm bậc hai lồi trên một tập khả thi dạng đa diện.

### Nón nửa xác định dương $$\mathbb{S}_{+}^n$$

Ký hiệu $$\mathbb{S}_{+}^n$$ biểu diễn **nón các ma trận nửa xác định dương**, một khái niệm nền tảng trong tối ưu hóa lồi:

<div class="textbook-definition" markdown="1">
**Định nghĩa:**
> $$\mathbb{S}_{+}^n = \{ X \in \mathbb{S}^n : X \succeq 0 \}$$
</div>

**trong đó:**
- $$\mathbb{S}^n$$ là tập tất cả các **ma trận đối xứng** kích thước $$n \times n$$.
- $$X \succeq 0$$ có nghĩa là ma trận $$X$$ **nửa xác định dương** (bán xác định dương).

**Tính chất chính:**

1. **Điều kiện nửa xác định dương:** Một ma trận đối xứng $$P$$ là nửa xác định dương khi và chỉ khi:
   - Tất cả các giá trị riêng của $$P$$ đều không âm ($$\lambda_i \geq 0$$), hoặc tương đương
   - $$v^T P v \geq 0$$ với mọi vectơ $$v \in \mathbb{R}^n$$.

2. **Tính chất nón lồi:** $$\mathbb{S}_{+}^n$$ là một nón lồi, vì với mọi $$\theta_1, \theta_2 \geq 0$$ và $$A, B \in \mathbb{S}_{+}^n$$, ta có $$\theta_1 A + \theta_2 B \in \mathbb{S}_{+}^n$$.

**Ví dụ với $$n = 2$$:**
Đối với ma trận đối xứng $$2 \times 2$$ dạng $$P = \begin{bmatrix} a & b \\ b & c \end{bmatrix}$$, điều kiện $$P \in \mathbb{S}_{+}^2$$ tương đương với:
- $$a \geq 0$$ và $$c \geq 0$$ (các phần tử trên đường chéo chính không âm),
- $$ac - b^2 \geq 0$$ (định thức không âm).

**Vai trò của điều kiện này trong QP:**
- Điều kiện $$P \in \mathbb{S}_{+}^n$$ đảm bảo hàm mục tiêu $$\frac{1}{2}x^T P x + q^T x + r$$ là hàm lồi.
- Nếu thiếu điều kiện này, hàm mục tiêu có thể có nhiều cực tiểu địa phương và bài toán không còn là bài toán lồi.
- Nhờ tính lồi, mọi cực tiểu địa phương của QP đều là cực tiểu toàn cục.

### Bất đẳng thức theo thành phần $$Gx \preceq h$$

Ký hiệu $$Gx \preceq h$$ biểu diễn hệ **ràng buộc bất đẳng thức tuyến tính theo từng thành phần**:

<div class="textbook-definition" markdown="1">
**Định nghĩa:**
$$Gx \preceq h \quad \Leftrightarrow \quad (Gx)_i \leq h_i \text{ với mọi } i = 1, 2, \ldots, m$$
</div>

**trong đó:**
- $$G \in \mathbb{R}^{m \times n}$$ là ma trận hệ số ràng buộc,
- $$x \in \mathbb{R}^n$$ là vectơ biến quyết định,
- $$h \in \mathbb{R}^m$$ là vectơ vế phải,
- $$m$$ là số lượng ràng buộc bất đẳng thức.

**Dạng khai triển:**
Bất đẳng thức vectơ $$Gx \preceq h$$ tương đương với hệ:
$$
\begin{align}
g_1^T x &\leq h_1 \\
g_2^T x &\leq h_2 \\
&\vdots \\
g_m^T x &\leq h_m
\end{align}
$$

trong đó $$g_i^T$$ là hàng thứ $$i$$ của ma trận $$G$$.

**Ví dụ:**
Xét $$G = \begin{bmatrix} 1 & 2 \\ -1 & 3 \\ 0 & -1 \end{bmatrix}$$, $$x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$$, và $$h = \begin{bmatrix} 5 \\ 2 \\ -1 \end{bmatrix}$$.

Khi đó $$Gx \preceq h$$ tương đương với hệ:
$$
\begin{align}
x_1 + 2x_2 &\leq 5 \\
-x_1 + 3x_2 &\leq 2 \\
-x_2 &\leq -1 \quad \text{(tức là } x_2 \geq 1\text{)}
\end{align}
$$

**Ý nghĩa hình học:**
- Mỗi bất đẳng thức $$g_i^T x \leq h_i$$ xác định một **nửa không gian** trong $$\mathbb{R}^n$$.
- Miền khả thi là **giao** của tất cả các nửa không gian này.
- Giao đó tạo thành một **tập đa diện** (polyhedron), hoặc một đa diện lồi bị chặn (polytope) nếu nó bị chặn.
- Do đó, ràng buộc $$Gx \preceq h$$ xác định **tập khả thi đa diện** của bài toán QP.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_02_geometric_interpretation_of_QP.png" alt="[Fig 1] Geometric interpretation of QP [1]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Minh họa hình học của bài toán QP [1]</figcaption>
</p>
</figure>

## QP ở dạng chuẩn

Dạng chuẩn của bài toán quy hoạch bậc hai được viết như sau:

### Bài toán QP dạng chuẩn
$$
\begin{align}
    \text{minimize}_{x} \quad &\frac{1}{2}x^T P x + q^T x + r \\
    \text{subject to} \quad &A x = b \\
    &x \succeq 0
\end{align}
$$

Mọi bài toán quy hoạch bậc hai tổng quát đều có thể đưa về dạng chuẩn theo các bước sau:

### Chuyển đổi QP tổng quát về dạng chuẩn

**Bước 1.** Đưa thêm vectơ biến phụ $$s \succeq 0$$ để chuyển ràng buộc bất đẳng thức thành ràng buộc đẳng thức:
$$
\begin{align}
    \text{minimize}_{x, s} \quad &\frac{1}{2}x^T P x + q^T x + r \\
    \text{subject to} \quad &Gx + s = h \\
    &Ax = b \\
    &s \succeq 0
\end{align}
$$

**Bước 2.** Tách biến tự do $$x$$ thành hiệu của hai biến không âm:
$$x = x^{+} - x^{-}, \quad \text{với } x^{+}, x^{-} \succeq 0$$

$$
\begin{align}
    \text{minimize}_{x^{+}, x^{-}, s} \quad &\frac{1}{2}(x^{+} - x^{-})^T P (x^{+} - x^{-}) + q^T x^{+} - q^T x^{-} + r\\
    \text{subject to} \quad &Gx^{+} - Gx^{-} + s = h \\
    &Ax^{+} - Ax^{-} = b \\
    &s \succeq 0 \\
    &x^{+} \succeq 0, \quad x^{-} \succeq 0
\end{align}
$$

**Bước 3.** Định nghĩa các biến và ma trận khối $$\tilde{x}$$, $$\tilde{q}$$, $$\tilde{b}$$, $$\tilde{A}$$, $$\tilde{P}$$:

$$
\tilde{x} =
\begin{bmatrix}
x^{+} \\
x^{-} \\
s
\end{bmatrix}, \quad
\tilde{q} =
\begin{bmatrix}
q \\
-q \\
0
\end{bmatrix}, \quad
\tilde{b} =
\begin{bmatrix}
h \\
b
\end{bmatrix}
$$

$$
\tilde{A} =
\begin{bmatrix}
G & -G & I \\
A & -A & O
\end{bmatrix}, \quad
\tilde{P} =
\begin{bmatrix}
 P & -P & O \\
-P &  P & O \\
 O &  O & O
\end{bmatrix}
$$

**Bước 4.** Thay các biểu thức ở Bước 3 vào bài toán ở Bước 2 để thu được dạng chuẩn:

$$
\begin{align}
    \text{minimize}_{\tilde{x}} \quad &\frac{1}{2}\tilde{x}^T \tilde{P} \tilde{x} + \tilde{q}^T \tilde{x} + r \\
    \text{subject to} \quad &\tilde{A} \tilde{x} = \tilde{b} \\
    &\tilde{x} \succeq 0
\end{align}
$$

## Quy hoạch tuyến tính là trường hợp đặc biệt của QP

Khi ma trận $$P = 0$$ (tức loại bỏ số hạng bậc hai khỏi hàm mục tiêu), bài toán QP trở thành bài toán quy hoạch tuyến tính (LP). Vì vậy LP là một trường hợp đặc biệt của QP, ký hiệu $$\text{LP} \subseteq \text{QP}$$.

### Nhắc lại: LP tổng quát
$$
\begin{align}
    \text{minimize}_{x} \quad &c^T x + d \\
    \text{subject to} \quad &Gx \preceq h \\
    &Ax = b
\end{align}
$$
trong đó $$G \in \mathbb{R}^{m \times n}$$ và $$A \in \mathbb{R}^{p \times n}$$.

### Ví dụ 1: Tối ưu hóa danh mục đầu tư

Bài toán này cân bằng giữa lợi suất kỳ vọng và rủi ro khi phân bổ tỷ trọng cho một danh mục tài sản tài chính:

$$
\begin{align}
    \text{maximize}_{x} \quad &\mu^T x - \frac{\gamma}{2}x^T P x \\
    \text{subject to} \quad &\mathbf{1}^Tx = 1 \\
    &x \succeq 0
\end{align}
$$

**trong đó:**
- $$\mu$$: vectơ lợi suất kỳ vọng của các tài sản,
- $$P$$: ma trận hiệp phương sai của lợi suất tài sản,
- $$\gamma > 0$$: tham số mức độ ngại rủi ro (siêu tham số),
- $$x$$: vectơ tỷ trọng phân bổ vốn vào từng tài sản.

### Ví dụ 2: Máy vectơ hỗ trợ (SVM)

Máy vectơ hỗ trợ (SVM) là một ví dụ điển hình của bài toán quy hoạch bậc hai. Dưới đây là mô hình C-SVM (chi tiết lý thuyết SVM nằm ngoài phạm vi chương này):

$$
\begin{align}
    \text{minimize}_{\beta, \beta_0, \xi} \quad &\frac{1}{2} \| \beta \|_2^2 + C \sum_{i=1}^{n} \xi_i \\
    \text{subject to} \quad &\xi_i \geq 0, \quad i = 1, \ldots, n \\
    &y_i (x_i^T \beta + \beta_0) \geq 1 - \xi_i, \quad i = 1, \ldots, n
\end{align}
$$

**cho trước:** $$y \in \{-1, 1\}^n$$ và ma trận dữ liệu $$X \in \mathbb{R}^{n \times p}$$ có các hàng là $$x_1^T, \ldots, x_n^T$$.

### Ví dụ 3: Bình phương tối thiểu trong hồi quy

Bài toán cực tiểu hóa tổng bình phương sai số sau đây là một bài toán QP không ràng buộc:
$$\| Ax - b \|_2^2 = x^T A^TA x - 2b^TAx + b^Tb$$
