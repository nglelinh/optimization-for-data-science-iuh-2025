---
layout: post
title: '08-01-07 Ví dụ: Giao của các tập hợp'
chapter: '08'
order: 9
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Hãy tưởng tượng bạn cần thiết kế một bộ lọc tín hiệu thỏa mãn đồng thời hàng chục yêu cầu kỹ thuật: năng lượng không vượt ngưỡng, biên độ trong miền tần số nằm trong dải cho phép, và hệ số thời gian bị giới hạn trong hộp cứng. Mỗi yêu cầu định nghĩa một tập lồi $$C_i$$, và câu hỏi của bạn không phải là "tối ưu hàm nào" mà là: *làm sao tìm được một điểm $$x$$ nằm trong giao $$C_1 \cap C_2 \cap \dots \cap C_m$$?*

Đây là bài toán khả thi lồi (convex feasibility problem) — một trong những bài toán xuất hiện dày đặc nhất trong xử lý ảnh, tái tạo chụp cắt lớp CT và điều khiển tự động. Điều kỳ diệu mà bài học này phơi bày là khi ta biến bài toán hình học ấy thành cực tiểu hóa khoảng cách lớn nhất $$f(x) = \max_{1 \le i \le m} \operatorname{dist}(x, C_i)$$ rồi áp dụng phương pháp subgradient với bước Polyak (vì biết chắc $$f^* = 0$$!), công thức đại số phức tạp tự rút gọn thành một hành động hình học đẹp như mơ: **ở mỗi bước, chọn tập lồi xa nhất và chiếu thẳng $$x$$ lên tập đó!**

## Kiến thức cần nhớ: Ba trụ cột nối giải tích không trơn với phép chiếu luân phiên

- **Hàm khoảng cách tới tập lồi và tính khả vi của nó:** Với tập lồi đóng khác rỗng $$C$$, hàm $$\operatorname{dist}(x, C) = \min_{y \in C} \|x - y\|_2$$ luôn lồi. Khi $$x \notin C$$, điểm chiếu $$P_C(x)$$ là duy nhất và hàm khoảng cách thực sự *khả vi* tại $$x$$ với gradient đơn vị $$\nabla \operatorname{dist}(x, C) = \frac{x - P_C(x)}{\|x - P_C(x)\|_2}$$.
- **Quy tắc dưới vi phân của hàm max hữu hạn (Danskin / Dubovitskii–Milyutin):** Với $$f(x) = \max_{1 \le i \le m} f_i(x)$$, dưới vi phân tại $$x$$ là bao lồi của các dưới vi phân thuộc những nhánh đang đạt cực đại $$I(x) = \{i : f_i(x) = f(x)\}$$. Để chạy thuật toán subgradient, ta chỉ cần nhặt một chỉ số $$j \in I(x)$$ và lấy đúng gradient của $$f_j$$.
- **Phép chiếu luân phiên (Alternating Projections / POCS) như trường hợp đặc biệt của bước Polyak:** Thay $$f^* = 0$$ và $$\|g^{(k)}\|_2 = 1$$ vào bước Polyak:
  $$x^{(k+1)} = x^{(k)} - \frac{\|x^{(k)} - P_{C_j}(x^{(k)})\|_2}{1^2} \cdot \frac{x^{(k)} - P_{C_j}(x^{(k)})}{\|x^{(k)} - P_{C_j}(x^{(k)})\|_2} = P_{C_j}(x^{(k)}).$$
  Hai ý tưởng tưởng như thuộc hai thế giới khác nhau — subgradient Polyak và chiếu tập lồi POCS — hóa ra là một!

### Giải thích: Tính tay tìm giao của đĩa tròn và nửa mặt phẳng bằng subgradient Polyak

Trong $$\mathbb{R}^2$$, xét hai tập lồi đóng:
- Đĩa đơn vị $$C_1 = \{x \in \mathbb{R}^2 : \|x\|_2 \le 1\}$$,
- Nửa mặt phẳng phải $$C_2 = \{x \in \mathbb{R}^2 : x_1 \ge 0.5\}$$.
Giao $$C_1 \cap C_2$$ khác rỗng (chứa điểm $$(0.5, 0)$$), nên $$f^* = 0$$. Bắt đầu từ $$x^{(0)} = (-2, 0)$$.

1. **Tính khoảng cách và hình chiếu tới từng tập tại $$x^{(0)} = (-2, 0)$$:**
   - Với $$C_1$$: chiếu lên đĩa đơn vị là $$P_{C_1}(-2, 0) = (-1, 0)$$, nên $$f_1(x^{(0)}) = \|(-2,0) - (-1,0)\|_2 = 1.0$$.
   - Với $$C_2$$: chiếu lên $$x_1 \ge 0.5$$ là $$P_{C_2}(-2, 0) = (0.5, 0)$$, nên $$f_2(x^{(0)}) = \|(-2,0) - (0.5,0)\|_2 = 2.5$$.
2. **Chọn nhánh lớn nhất và tính subgradient đơn vị:**
   $$f(x^{(0)}) = \max(1.0, 2.5) = 2.5$$ đạt tại $$j = 2$$.
   Subgradient tương ứng là:
   $$g^{(0)} = \frac{x^{(0)} - P_{C_2}(x^{(0)})}{\|x^{(0)} - P_{C_2}(x^{(0)})\|_2} = \frac{(-2.5, 0)}{2.5} = (-1, 0), \quad \|g^{(0)}\|_2 = 1.$$
3. **Cập nhật theo bước Polyak ($$f^* = 0$$):**
   $$t_1 = \frac{f(x^{(0)}) - 0}{\|g^{(0)}\|_2^2} = \frac{2.5}{1} = 2.5 \implies x^{(1)} = (-2, 0) - 2.5(-1, 0) = (0.5, 0) = P_{C_2}(x^{(0)}).$$
   Kiểm tra điểm mới $$x^{(1)} = (0.5, 0)$$: $$\|x^{(1)}\|_2 = 0.5 \le 1$$ (thuộc $$C_1$$) và $$x_1^{(1)} = 0.5 \ge 0.5$$ (thuộc $$C_2$$). Ta chạm đích $$f(x^{(1)}) = 0$$ ngay sau đúng 1 bước!

Xét bài toán tìm một điểm thuộc giao của nhiều tập lồi đóng $$C_1, C_2, \dots, C_m$$.

Định nghĩa $$f_i(x)$$ là khoảng cách từ điểm $$x$$ đến tập $$C_i$$, và $$f(x)$$ là khoảng cách lớn nhất từ $$x$$ đến tất cả các tập $$C_i$$ ($$i=1,...,m$$):
>
$$ \begin{align}
f_i(x) & = \mathbb{dist}(x, C_i), i=1,...,m \\
f(x) & = \max_{1,...,m}\text{ }f_i(x)
\end{align} $$

Bài toán tìm giao của các tập lồi có thể được phát biểu thành bài toán tối ưu sau:

>
$$ \begin{align}
min_{x}\text{ }f(x)
\end{align} $$

Việc tìm một điểm chung của các tập lồi tương đương với việc tìm điểm $$x$$ cực tiểu hóa khoảng cách lớn nhất $$f(x)$$ đến các tập $$C_i$$. Hàm mục tiêu $$f(x)$$ là hàm lồi. Nếu giao của tất cả các tập là khác rỗng, thì giá trị tối ưu là $$f^* = 0$$ và mọi điểm tối ưu đều thỏa mãn $$x^* \in C_1 \cap C_2 \cap ... \cap C_m$$.

## Gradient của hàm khoảng cách

Trong [bài trước]({% multilang_post_url contents/chapter07/21-03-25-07_03_05_example_distance_to_convex_set %}), khoảng cách đến một tập lồi đóng $$C$$ được định nghĩa là $$dist(x, C_i) = \min_{y \in C} \lVert y-x \rVert _2$$, và với $$x \notin C$$, gradient của hàm này là:

>
$$ \begin{align}
\partial dist(x,C) = \frac{x-P_C(x)}{ \Vert x-P_C(x) \Vert_2}
\end{align} $$

trong đó $$P_C(x)$$ là phép chiếu Euclid của $$x$$ lên tập $$C$$.

## Vi phân dưới của giá trị lớn nhất hữu hạn theo điểm

Vi phân dưới của hàm giá trị lớn nhất hữu hạn theo điểm $$f(x)=max_{i=1,...,m}\text{ }f_i(x)$$ là:

>
$$ \begin{align}
\partial f(x) = \text{conv}\left(\bigcup_{i:f_i(x)=f(x)} \partial f_i(x)\right)
\end{align} $$

Nói cách khác, $$\partial f(x)$$ là bao lồi của hợp các vi phân dưới $$\partial f_i(x)$$ ứng với những chỉ số $$i$$ đạt cực đại $$f_i(x) = f(x)$$. Đặc biệt, nếu $$f_i(x) = f(x)$$ và $$g_i \in \partial f_i(x)$$ thì $$g_i \in \partial f(x)$$.

## Suy ra công thức cập nhật subgradient

Nhắc lại từ [chương trước]({% multilang_post_url contents/chapter07/21-03-25-07_03_05_example_distance_to_convex_set %}), với $$x \notin C_i$$, hàm $$dist(x, C_i)$$ có gradient là:

>$$Nhắc lại:$$
$$ \begin{align}
g_i = \nabla f_i(x) = \frac{x-P_{C_i}(x)}{ \Vert x-P_{C_i}(x) \Vert_2}
\end{align} $$

Nếu giao của các tập lồi khác rỗng, ta biết ngay $$f^*=0$$ nên có thể áp dụng kích thước bước Polyak. Hơn nữa, vì vector $$x-P_{C_i}(x)$$ đã được chuẩn hóa, ta có $$ \Vert g \Vert_2^{2}=1$$. Thay vào công thức kích thước bước Polyak $$t_k = \{\frac{f^{(k-1)}-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}}\}$$, bước cập nhật subgradient trở thành:

>
$$ \begin{align}
x^{(k)} & = x^{(k-1)} - t_{k}⋅g_{k-1} \\
& = x^{(k-1)} - \frac{f^{(k-1)}-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}} \frac{x^{(k-1)}-P_{C_i}(x)}{ \Vert x^{(k-1)}-P_{C_i}(x) \Vert_2}  \\
& = x^{(k-1)} - f(x^{k-1}) \frac{x^{(k-1)}-P_{C_i}(x)}{ \Vert x^{(k-1)}-P_{C_i}(x) \Vert_2}
\end{align} $$

Do $$f(x^{(k-1)}) = dist(x^{(k-1)}, C_i) = \Vert x^{(k-1)}-P_{C_i}(x^{(k-1)}) \Vert_2$$ với $$C_i$$ là tập xa $$x^{(k-1)}$$ nhất, công thức cập nhật rút gọn thành:

>
$$ \begin{align}
x^{(k)} = P_{C_i}(x^{(k-1)})
\end{align} $$

Về mặt hình học, ở mỗi bước thuật toán chiếu điểm hiện tại lên **tập lồi xa nhất** (tập có khoảng cách lớn nhất tới điểm hiện tại).

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter08/08_01_projection.png" alt="projection" width="60%" height="60%">
</p>
  <figcaption style="text-align: center;">[Fig 2] Alternating Projection Algorithm [10]</figcaption>
</figure>
