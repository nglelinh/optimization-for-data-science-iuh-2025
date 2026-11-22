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
