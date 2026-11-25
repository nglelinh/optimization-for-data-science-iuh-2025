---
layout: post
title: 07-02-02 Phép tính gradient dưới
chapter: '07'
order: 5
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
---

Nếu mỗi lần gặp một hàm tổng hợp như $$f(x) = \frac{1}{2}\|Ax - b\|_2^2 + \lambda\|x\|_1 + \max(x_1, 2x_2)$$ ta đều phải quay về kiểm tra định nghĩa gốc $$f(y) \ge f(x) + g^T(y - x)$$ với mọi $$y$$, thì việc tính toán sẽ trở thành cơn ác mộng. May mắn thay, giống hệt bảng đạo hàm trong giải tích 1, vi phân dưới sở hữu một bộ **Phép tính Vi phân dưới (Subgradient Calculus)** cực kỳ gọn gàng và trực quan!

Tuy nhiên, hãy chú ý một khác biệt tinh tế: trong giải tích cổ điển, đạo hàm của $$-f$$ là $$-\nabla f$$, nhưng trong giải tích lồi, **quy tắc nhân hằng số chỉ đúng với hằng số DƯƠNG $$a > 0$$** (vì nhân với số âm biến hàm lồi thành hàm lõm!). Nắm vững 5 quy tắc trong bài này sẽ giúp bạn tính $$\partial f(x)$$ của mọi mô hình học máy trong vài giây.

## Bản đồ kiến thức nền: Năm quy tắc vàng của Phép tính Vi phân dưới

Hãy ghi nhớ năm quy tắc cốt lõi sau cùng trực giác đi kèm:

- **Quy tắc 1 — Nhân hằng số dương (Scaling):** Với $$a > 0$$, $$\partial (af)(x) = a \cdot \partial f(x)$$. (Không áp dụng cho $$a < 0$$ vì $$af$$ không còn lồi!)
- **Quy tắc 2 — Phép cộng (Sum Rule / Tổng Minkowski):** $$\partial (f_1 + f_2)(x) = \partial f_1(x) + \partial f_2(x) = \{g_1 + g_2 : g_1 \in \partial f_1(x),\; g_2 \in \partial f_2(x)\}$$ (đúng dưới điều kiện giao phần trong miền xác định khác rỗng — luôn đúng khi hàm xác định trên toàn $$\mathbb{R}^n$$!).
- **Quy tắc 3 — Hợp thành với ánh xạ affine (Affine Composition):** Nếu $$h(x) = f(Ax + b)$$, thì $$\partial h(x) = A^T \partial f(Ax + b)$$ — hoàn toàn giống quy tắc dây chuyền (chain rule)!
- **Quy tắc 4 — Cực đại hữu hạn theo điểm (Pointwise Maximum):** Nếu $$f(x) = \max_{i=1,\dots,m} f_i(x)$$, gọi $$I(x) = \{i : f_i(x) = f(x)\}$$ là tập các hàm **đang tích cực** (đạt cực đại tại $$x$$). Khi đó:
  $$\partial f(x) = \operatorname{conv}\left(\bigcup_{i \in I(x)} \partial f_i(x)\right)$$
  — tức là **bao lồi** của tất cả các subgradient thuộc các nhánh đang đạt cực đại tại $$x$$!
- **Quy tắc 5 — Cực đại tổng quát (Supremum over infinite index set):** Mở rộng tương tự sang $$f(x) = \sup_{s \in S} f_s(x)$$ bằng bao lồi đóng của các nhánh đạt cực đại (ví dụ tìm subgradient của trị riêng lớn nhất $$\lambda_{\max}(X) = \max_{\|v\|_2=1} v^T X v$$!).

### Khung giải thích (nên đọc chậm): Áp dụng đồng thời 3 quy tắc để tính $$\partial f(x)$$ của một hàm hợp phức tạp

Xét hàm $$f(x) = \max(0,\; 2x - 4) + 3|x - 2|$$ tại điểm gãy khúc kép $$x = 2$$:

1. **Bước 1 — Tách thành tổng $$f(x) = f_1(x) + f_2(x)$$ (Quy tắc 2):**
   - $$f_1(x) = \max(0,\; 2x - 4)$$.
   - $$f_2(x) = 3|x - 2|$$.
2. **Bước 2 — Tính $$\partial f_1(2)$$ bằng Quy tắc cực đại hữu hạn (Quy tắc 4):**
   Tại $$x = 2$$: nhánh 1 bằng $$0$$ (đạo hàm $$0$$), nhánh 2 bằng $$2(2) - 4 = 0$$ (đạo hàm $$2$$). Cả hai nhánh đều đạt cực đại!
   $$\partial f_1(2) = \operatorname{conv}\{0,\; 2\} = [0,\; 2].$$
3. **Bước 3 — Tính $$\partial f_2(2)$$ bằng Quy tắc nhân dương + hợp thành affine (Quy tắc 1 & 3):**
   Vì $$x - 2 = 0$$, $$\partial |x - 2|\big|_{x=2} = [-1, 1]$$. Nhân với $$3 > 0$$:
   $$\partial f_2(2) = 3 \cdot [-1, 1] = [-3,\; 3].$$
4. **Bước 4 — Cộng Minkowski hai đoạn đóng:**
   $$\partial f(2) = [0, 2] + [-3, 3] = [0 + (-3),\; 2 + 3] = [-3,\; 5].$$
   Kiểm tra nhanh: $$0 \in [-3, 5] \implies x^\star = 2$$ là điểm cực tiểu toàn cục của $$f(x)$$ (với $$f^\star = 0$$)!

---

Các quy tắc cơ bản sau đây áp dụng cho vi phân dưới của các hàm lồi:

### Nhân với hằng số dương (Tỷ lệ)

>
$$
\eqalign{
	\text{nếu } & a>0, \\
	\text{thì } &\partial (af) = a\cdot \partial f
}
$$

### Phép cộng

>
$$\partial(f_1 + f_2) = \partial f_1 + \partial f_2$$

Ở đây, tổng của hai tập hợp được định nghĩa theo nghĩa tổng Minkowski: $$A+B= \{a+b:a\in A, b \in B\}$$.

### Hợp thành với ánh xạ affine

>
$$
\eqalign{
	\text{nếu } & g(x)=f(Ax+b), \\
	\text{thì } & \partial g(x) = A^T \partial f(Ax+b)
}
$$

### Giá trị lớn nhất hữu hạn theo điểm

>
$$
\eqalign{
	\text{nếu } & f(x)=\max_{i=1,\dots,m} f_i(x), \\
	\text{thì } & \partial f(x) = \text{conv}\left(\bigcup_{i:f_i(x)=f(x)} \partial f_i(x)\right)
}
$$

Nói cách khác, $$\partial f(x)$$ là bao lồi của hợp các vi phân dưới của những hàm thành phần đạt giá trị lớn nhất $$f(x)$$ tại điểm $$x$$.

### Giá trị lớn nhất tổng quát theo điểm

>$$
\eqalign{
	\text{nếu } & f(x) = \max_{s \in S} f_s(x),\\ 
	\text{thì } & \partial f(x) \supseteq cl \left \{ \text{conv} \left(\bigcup_{s:f_s(x)=f(x)} \partial f_s(x)\right) \right\}
}
$$

Vì $$S$$ có thể là một tập vô hạn, hợp của vô số tập hợp chưa chắc đã là tập đóng. Do đó, cần lấy bao đóng để đảm bảo tập thu được là tập đóng giống như vi phân dưới.

Nếu tập $$S$$ compact (đóng và bị chặn) và các hàm $$f_s$$ liên tục theo $$s$$, thì dấu bao hàm trở thành đẳng thức.

Ví dụ, xét chuẩn $$p$$ của vector $$x$$ viết dưới dạng giá trị lớn nhất theo điểm:
>
\begin{equation}
f(x) =  \vert  \vert x \vert  \vert \_p = \max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx, \qquad 1/p + 1/q =1
\end{equation}

Đặt $$f_z(x)=z^Tx$$. Khi đó, mọi $$z^*$$ thỏa mãn $$f(x)=f_{z^*}(x)$$ đều thuộc tập $$\arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx$$. Vì $$\partial f_{z^*}(x)=\{z^*\}$$, hợp $$\bigcup \partial f_{z^*}(x)$$ chính là tập $$\arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx$$.

Do $$S=\{z: \vert  \vert z \vert  \vert _q \leq 1\}$$ là tập compact và $$f_z(x)=z^Tx$$ tuyến tính, theo quy tắc giá trị lớn nhất tổng quát theo điểm, việc lấy bao lồi rồi lấy bao đóng của $$\bigcup \partial f_{z^*}(x)$$ không bổ sung thêm phần tử nào mới. Do đó, vi phân dưới của $$f(x)$$ là:

>
\begin{equation}
\partial f(x) = \arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^T x
\end{equation}
