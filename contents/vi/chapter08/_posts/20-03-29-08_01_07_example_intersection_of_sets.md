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


Giả sử chúng ta muốn tìm điểm giao của nhiều tập lồi đóng.

Đầu tiên, hãy định nghĩa $$f_i(x)$$ là khoảng cách từ điểm $$x$$ đến tập $$C_i$$, và $$f(x)$$ là khoảng cách tối đa từ $$x$$ đến tất cả các tập $$C_i, i=1,...,m$$:
>
$$ \begin{align}
f_i(x) & = \mathbb{dist}(x, C_i), i=1,...,m \\
f(x) & = \max_{1,...,m}\text{ }f_i(x)
\end{align} $$

Sử dụng hai hàm này, bài toán tìm giao của các tập lồi có thể được công thức hóa thành bài toán tối thiểu hóa sau:

>
$$ \begin{align}
min_{x}\text{ }f(x)
\end{align} $$

Bài toán tìm điểm giao của các tập lồi tương đương với việc tìm điểm $$x$$ tối thiểu hóa khoảng cách tối đa $$f(x)$$ đến các tập $$C_i$$. Trong trường hợp này, hàm mục tiêu $$f(x)$$ là lồi. Nếu tất cả các tập đều có điểm giao chung, thì $$f^* = 0$$ và điểm tối ưu là $$x^* \in C_1 \cap C_2 \cap ... \cap C_m$$.

## Gradient của hàm khoảng cách

Trong [phần trước]({% multilang_post_url contents/chapter07/21-03-25-07_03_05_example_distance_to_convex_set %}), chúng ta đã định nghĩa khoảng cách đến một tập lồi là $$dist(x, C_i) = \min_{y \in C} \lVert y-x \rVert _2$$, và thấy rằng gradient của hàm này là:

>
$$ \begin{align}
\partial dist(x,C) = \frac{x-P_C(x)}{ \Vert x-P_C(x) \Vert_2}
\end{align} $$

Ở đây, $$P_C(x)$$ là phép chiếu của điểm $$x$$ lên tập $$C$$.

## Subdifferential của maximum hữu hạn theo điểm

Subdifferential của hàm finite pointwise maximum $$f(x)=max_{i=1,...,m}\text{ }f_i(x)$$ được định nghĩa như sau.

>
$$ \begin{align}
\partial f(x) = \text{conv}\left(\bigcup_{i:f_i(x)=f(x)} \partial f_i(x)\right)
\end{align} $$

Tức là, subdifferential của $$x$$ được định nghĩa là convex hull của hợp tất cả các subdifferential $$\partial f_i(x), i=1,...,m$$ tại điểm đó.

Nếu $$f_i(x) = f(x)$$ và $$g_i \in \partial f_i(x)$$ thì $$g_i \in \partial f(x)$$.

## Suy ra các bước cập nhật subgradient

Trong [chương trước]({% multilang_post_url contents/chapter07/21-03-25-07_03_05_example_distance_to_convex_set %}), $$dist(x, C_i)$$ có subgradient như sau.

>$$Nhắc lại:$$
$$ \begin{align}
g_i = \nabla f_i(x) = \frac{x-P_{C_i}(x)}{ \Vert x-P_{C_i}(x) \Vert_2}
\end{align} $$

Nếu có điểm giao của các tập lồi thì chúng ta có thể biết ngay rằng $$f^*=0$$ nên có thể sử dụng kích thước bước Polyak. Nhìn vào công thức subgradient trên, $$x-P_{c_i}(x)$$ ở dạng chuẩn hóa nên $$ \Vert g \Vert_2^{2}=1$$. Cuối cùng, thay các giá trị đã biết vào kích thước bước Polyak $$t_k = \{\frac{f^{(k-1)}-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}}\}$$, chúng ta có thể suy ra công thức phương pháp subgradient như sau.

>
$$ \begin{align}
x^{(k)} & = x^{(k-1)} - t_{k}⋅g_{k-1} \\
& = x^{(k-1)} - \frac{f^{(k-1)}-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}} \frac{x^{(k-1)}-P_{C_i}(x)}{ \Vert x^{(k-1)}-P_{C_i}(x) \Vert_2}  \\
& = x^{(k-1)} - f(x^{k-1}) \frac{x^{(k-1)}-P_{C_i}(x)}{ \Vert x^{(k-1)}-P_{C_i}(x) \Vert_2}
\end{align} $$


Ở đây kích thước Polyak $$f(x^{(k-1)})$$ là $$dist(x_i^{(k-1)}, C_i) =  \Vert x^{(k-1)}-P_{C_i}(x) \Vert_2$$ nên phương pháp subgradient được tổng kết như sau.

>
$$ \begin{align}
x^{(k)} = P_{C_i}(x^{(k-1)})
\end{align} $$

Bài toán này khi biểu diễn bằng hình vẽ có dạng lặp lại phép chiếu lên hàm lồi gần nhất ở mỗi bước.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter08/08_01_projection.png" alt="projection" width="60%" height="60%">
</p>
  <figcaption style="text-align: center;">[Fig 2] Alternating Projection Algorithm [10]</figcaption>
</figure>
