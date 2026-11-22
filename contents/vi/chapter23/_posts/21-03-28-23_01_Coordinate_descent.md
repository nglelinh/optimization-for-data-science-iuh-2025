---
layout: post
title: 23-01 Phương Pháp Coordinate Descent
chapter: '23'
order: 2
owner: YoungJae Choung
categories:
- chapter23
lang: vi
---

Chương này giới thiệu phương pháp hạ theo tọa độ (coordinate descent) — một thuật toán tối ưu đơn giản, hiệu quả và có khả năng mở rộng tốt. Trước khi đi vào công thức, hãy bắt đầu với ba câu hỏi nền tảng về điều kiện tối ưu theo từng trục tọa độ.

**Q1. Với hàm $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ lồi và khả vi, nếu điểm $$x$$ làm cực tiểu $$f$$ dọc theo từng trục tọa độ, thì $$x$$ có phải là điểm cực tiểu toàn cục không?**

**A1. Có. Khi đó $$\nabla f(x) = 0$$ nên $$x$$ là điểm cực tiểu toàn cục của $$f$$.**

Điều kiện cực tiểu theo từng trục tọa độ nghĩa là $$f(x + \delta e_i) \ge f(x)$$ với mọi $$\delta \in \mathbb{R}$$ và mọi $$i = 1, \dots, n$$, trong đó $$e_i = (0, \dots, 1, \dots, 0) \in \mathbb{R}^n$$ là vector cơ sở chuẩn thứ $$i$$. Vì không thể làm giảm $$f$$ khi dịch chuyển dọc theo bất kỳ trục tọa độ nào từ $$x$$, mọi đạo hàm riêng tại $$x$$ đều bằng 0:

$$
\nabla f(x) = \big( \frac{\partial f}{\partial x_1}(x), \dots, \frac{\partial f}{\partial x_n}(x) \big) = (0, \dots, 0) = 0
$$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/smooth_function.png" alt="[Hình 1] Hàm lồi trơn f [3]">
  <figcaption style="text-align: center;">$$[Hình 1] \; Hàm \; lồi \; trơn \; f \; [3]$$ </figcaption>
</p>
</figure>


<br/>

**Q2. Nếu $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ là hàm lồi nhưng *không khả vi*, điểm $$x$$ đạt cực tiểu dọc theo từng trục tọa độ có luôn là cực tiểu toàn cục không?**

**A2. Không. Trong trường hợp này, $$x$$ chưa chắc là điểm cực tiểu toàn cục của $$f$$ (xem phản ví dụ ở Hình 2).** 

Quan sát các đường đồng mức bên phải ở Hình 2: dù điểm đánh dấu không phải cực tiểu toàn cục, giá trị $$f$$ vẫn không thể giảm nếu chỉ đi dọc theo các trục tọa độ (muốn giảm $$f$$, ta phải đi vào phần bên trong của đường đồng mức). Nguyên nhân là tại điểm góc không trơn đó, toàn bộ phần bên trong đường đồng mức nằm kẹp giữa hai đường thẳng song song với các trục tọa độ. Khi $$f$$ khả vi, mỗi điểm trên đường đồng mức chỉ có duy nhất một tiếp tuyến nên hiện tượng kẹt này không xảy ra.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/non-smooth_function.png" alt="[Hình 2] Phản ví dụ: hàm lồi không trơn f [3]">
  <figcaption style="text-align: center;">$$[Hình 2] \; Phản \; ví \; dụ: \; hàm \; lồi \; không \; trơn \; f \; [3]$$ </figcaption>
</p>
</figure>
<br/>

**Q3. Nếu $$f$$ là tổng của một hàm lồi khả vi $$g$$ và một hàm lồi không trơn *tách được theo từng tọa độ*, tức $$f(x) = g(x) + \sum_{i=1}^{n} h_i(x_i)$$, thì điểm $$x$$ cực tiểu theo từng trục tọa độ có luôn là cực tiểu toàn cục không?**

**A3. Có. Với mọi $$y \in \mathbb{R}^n$$, ta luôn có:**

$$\begin{align}
f(y) - f(x) &\ge \nabla g(x)^T (y-x) + \sum_{i=1}^{n} \big[ h_i(y_i) - h_i(x_i) \big] \\\\
&= \sum_{i=1}^{n} \big[ \underbrace{\nabla_i g(x) (y_i - x_i) + h_i(y_i) - h_i(x_i)}_{\ge 0} \big] \ge 0
\end{align}$$

<div class="textbook-proof" markdown="1">
**Chứng minh:**
</div>

>Đặt $$F_i(x_i) = g(x_i ; x_{-i}) + h_i(x_i)$$, trong đó $$g(x_i ; x_{-i})$$ coi thành phần thứ $$i$$ là biến số còn tất cả các thành phần khác giữ cố định. Vì $$x_i$$ cực tiểu hóa $$F_i$$:
>
> $$
> \begin{align}
> & \: 0 \in \partial F_i (x_i) \\\\
> \Leftrightarrow & \: 0 \in \{ \nabla_i g(x) \} + \partial h_i(x_i)\\\\
> \Leftrightarrow & \: - \nabla_i g(x) \in \partial h_i(x_i)
> \end{align}
> $$

Theo [định nghĩa của dưới đạo hàm (subgradient)]({% multilang_post_url contents/chapter07/21-03-25-07_01_subgradient %}), ta suy ra với mọi $$y_i$$:

> $$
> \begin{align}
> & h_i(y_i) \ge h_i(x_i) - \nabla_i g(x) (y_i - x_i)\\\\
> \Leftrightarrow & \nabla_i g(x) (y_i - x_i) + h_i(y_i) - h_i(x_i) \ge 0.
> \end{align}
> $$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/separable_non-smooth.png" alt="[Hình 3] Hàm lồi f có các phần không trơn tách được [3]">
  <figcaption style="text-align: center;">$$[Hình 3] \; Hàm \; lồi \; f \; có \; các \; phần \; không \; trơn \; tách \; được \; [3]$$ </figcaption>
</p>
</figure>
<br/>

## Kết luận

Điểm cực tiểu của hàm có dạng $$f(x) = g(x) + \sum_{i=1}^{n} h_i(x_i)$$ (với $$g$$ lồi khả vi và các $$h_i$$ lồi) có thể tìm bằng **coordinate descent**. Xuất phát từ một điểm khởi tạo $$x^{(0)}$$, thuật toán lặp lại chu trình cập nhật sau:

>**Coordinate Descent:** <br/>
>$$\:$$ Với $$k = 1,2,3,\dots$$,
>
>$$
>\begin{align}
>x_1^{(k)} &\in \text{arg}\min_{x_1} \: f(x_1, x_2^{(k-1)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_2^{(k)} &\in \text{arg}\min_{x_2} \: f(x_1^{(k)}, x_2, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_3^{(k)} &\in \text{arg}\min_{x_3} \: f(x_1^{(k)}, x_2^{(k)}, x_3, \dots, x_n^{(k-1)})\\\\
>& \dots\\\\
>x_n^{(k)} &\in \text{arg}\min_{x_n} \: f(x_1^{(k)}, x_2^{(k)}, x_3^{(k)}, \dots, x_n)
>\end{align}
>$$

### Lưu ý:

* Trong chu trình thứ $$k$$, bước cập nhật các tọa độ $$x_{i+1}^{(k)}, \dots, x_{n}^{(k)}$$ sử dụng ngay giá trị mới $$x_i^{(k)}$$ vừa tính được.
* Thứ tự duyệt các tọa độ trong mỗi chu trình có thể chọn tùy ý (tuần hoàn, ngẫu nhiên hoặc theo quy tắc tham lam).
* Có thể nhóm nhiều tọa độ thành từng khối để cập nhật đồng thời (block coordinate descent).

Phiên bản trên thực hiện cực tiểu hóa chính xác theo từng tọa độ. Ngoài ra, với hàm $$f$$ lồi và khả vi, ta cũng có thể dùng phiên bản cực tiểu hóa không chính xác bằng một bước gradient theo từng tọa độ:

>**Coordinate Descent (cực tiểu hóa không chính xác theo từng tọa độ):** <br/>
>$$\:$$ Với $$k = 1,2,3,\dots$$,
>
>$$
>\begin{align}
>x_1^{(k)} &= x_1^{(k-1)} - t_{k,1} \cdot \nabla_1 f(x_1^{(k-1)}, x_2^{(k-1)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_2^{(k)} &= x_2^{(k-1)} - t_{k,2} \cdot \nabla_2 f(x_1^{(k)}, x_2^{(k-1)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_3^{(k)} &= x_3^{(k-1)} - t_{k,3} \cdot \nabla_3 f(x_1^{(k)}, x_2^{(k)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>& \dots\\\\
>x_n^{(k)} &= x_n^{(k-1)} - t_{k,n} \cdot \nabla_n f(x_1^{(k)}, x_2^{(k)}, x_3^{(k)}, \dots, x_n^{(k-1)})
>\end{align}
>$$
