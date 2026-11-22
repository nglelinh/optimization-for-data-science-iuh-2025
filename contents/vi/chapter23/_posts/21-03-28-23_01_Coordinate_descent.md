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

Trong chương này, chúng ta giới thiệu một phương pháp gọi là coordinate descent, cực kỳ đơn giản, hiệu quả và có khả năng mở rộng cao. Trước hết, hãy bắt đầu bằng một vài câu hỏi và trả lời đơn giản.

**Q1. Khi hàm $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ lồi và khả vi, nếu điểm mà $$f$$ đạt cực tiểu dọc theo từng trục tọa độ là $$x$$, thì $$x$$ có phải là điểm cực tiểu toàn cục không?**

**A1: Có. Vì $$\nabla f(x) = 0$$ nên $$x$$ là điểm cực tiểu toàn cục của $$f$$.**

Câu hỏi trên tương đương với việc hỏi liệu $$f(x + \delta e_i) \ge f(x)$$ có thỏa mãn với mọi $$\delta, i$$ hay không, trong đó $$e_i = (0, \dots, 1, \dots, 0) \in \mathbb{R}^n$$ là vector cơ sở chuẩn thứ $$i$$. Nghĩa là, vì ta không thể làm $$f$$ nhỏ hơn bằng cách di chuyển theo bất kỳ trục tọa độ nào từ $$x$$, nên các đạo hàm riêng theo mọi trục đều bằng 0.

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

**Q2. Vậy khi $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ là hàm lồi nhưng 'không khả vi', điểm $$x$$ mà $$f$$ đạt cực tiểu dọc theo từng trục tọa độ có luôn là điểm cực tiểu toàn cục không?**

**A2: Không. Trong trường hợp này, ta không thể khẳng định $$x$$ là điểm cực tiểu toàn cục của $$f$$. (Phản ví dụ: Hình 2 bên dưới)** 

Quan sát các đường đồng mức ở bên phải của phản ví dụ dưới đây, ta thấy dù điểm được đánh dấu không phải cực tiểu toàn cục, $$f$$ không thể giảm thêm bằng cách di chuyển theo bất kỳ trục tọa độ nào. (Để làm $$f$$ nhỏ hơn, ta phải có thể di chuyển vào bên trong đường đồng mức.) Đó là vì tại vị trí này, toàn bộ vùng bên trong của đường đồng mức nằm giữa hai tiếp tuyến song song với các trục tọa độ. Ngược lại, khi $$f$$ là hàm lồi khả vi, tại mọi điểm trên đường đồng mức chỉ có một tiếp tuyến duy nhất, nên hiện tượng này không xảy ra.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/non-smooth_function.png" alt="[Hình 2] Phản ví dụ: hàm lồi không trơn f [3]">
  <figcaption style="text-align: center;">$$[Hình 2] \; Phản \; ví \; dụ: \; hàm \; lồi \; không \; trơn \; f \; [3]$$ </figcaption>
</p>
</figure>
<br/>

**Q3. Khi $$f$$ có thể biểu diễn thành tổng của một hàm lồi khả vi $$g$$ và một hàm lồi $$h$$, điểm $$x$$ mà $$f$$ đạt cực tiểu dọc theo từng trục tọa độ có luôn là điểm cực tiểu toàn cục không? (Tức là $$f(x) = g(x) + \sum_{i=1}^{n} h_i(x_i)$$)**

**A3. Có. Vì nó thỏa mãn điều sau với mọi $$y$$.**
$$\begin{align}
f(y) - f(x) &\ge \nabla g(x)^T (y-x) + \sum_{i=1}^{n} \big[ h_i(y_i) - h_i(x_i) \big] \\\\
&= \sum_{i=1}^{n} \big[ \underbrace{\nabla_i g(x) (y_i - x_i) + h_i(y_i) - h_i(x_i)}_{\ge 0} \big] \ge 0
\end{align}$$

<div class="textbook-proof" markdown="1">
**Chứng minh:**
</div>

>Đặt $$F_i(x_i) = g(x_i ; x_{-i}) + h_i(x_i)$$. ($$g(x_i ; x_{-i})$$ nghĩa là chỉ coi phần tử thứ $$i$$ của $$x$$ là biến, còn các phần tử còn lại là giá trị cố định.)
>
> $$
> \begin{align}
> & \: 0 \in \partial F_i (x_i) \\\\
> \Leftrightarrow & \: 0 \in \{ \nabla_i g(x) \} + \partial h_i(x_i)\\\\
> \Leftrightarrow & \: - \nabla_i g(x) \in \partial h_i(x\_i)
> \end{align}
> $$

Theo [định nghĩa của dưới đạo hàm (subgradient)]({% multilang_post_url contents/chapter07/21-03-25-07_01_subgradient %}),

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

Điểm cực tiểu của $$f(x) = g(x) + \sum_{i=1}^{n} h_i(x_i)$$ với $$g$$ lồi, khả vi và $$h_i$$ lồi có thể tìm được bằng **coordinate descent**. Coordinate descent lặp lại chu trình sau. (Giả sử đã đặt giá trị khởi tạo $$x^{(0)}$$ phù hợp.)

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

* Quá trình tìm $$x_{i+1}^{(k)}, \dots, x_{n}^{(k)}$$ dùng $$x_i^{(k)}$$ mới thu được trong chu trình thứ $$k$$.
* Thứ tự các trục tọa độ trong chu trình có thể được chỉ định tùy ý.
* Có thể gộp hai hay nhiều trục tọa độ lại và xử lý như các khối.

Coordinate descent giới thiệu ở trên tương ứng với cực tiểu hóa chính xác theo từng tọa độ. Một cách tiếp cận khác là cực tiểu hóa không chính xác theo từng tọa độ bằng gradient. (Giả sử $$f$$ là hàm lồi khả vi)

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
