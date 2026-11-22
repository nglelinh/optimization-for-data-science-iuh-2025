---
layout: post
title: '19-01-01 Nhắc lại: proximal gradient descent'
chapter: '19'
order: 3
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

Trước khi đi vào **phương pháp Newton proximal (proximal Newton method)**, hãy ôn lại ngắn gọn **proximal gradient descent**.

Xem chi tiết tại [09 Proximal Gradient Descent and Acceleration]({% multilang_post_url contents/chapter09/20-01-08-09_proximal_gradient_descent_and_acceleration %}).

## Proximal gradient descent
**Proximal gradient descent** áp dụng cho bài toán tối ưu hàm tổng hợp có dạng:

>$$f(x) = g(x) + h(x)$$

* $$g$$ lồi và khả vi với $$\operatorname{dom}(g) = \mathbb{R}^n$$.
* $$h$$ lồi, có thể không khả vi nhưng có cấu trúc "đơn giản".


#### Thuật toán
Bắt đầu từ điểm khởi tạo $$x^{(0)}$$, thuật toán lặp lại phép cập nhật:

>$$x^{(k)} = \text{prox}_{t_k}(x^{(k-1)} - t_k \nabla g(x^{(k-1)}) ),\quad k=1,2,3,\dots$$

trong đó $$\text{prox}_{t}(\cdot)$$ là toán tử proximal ứng với hàm $$h$$:

> \begin{align}
\text{prox}_{t}(x) = \underset{z}{\text{argmin}} \ \frac{1}{2t} \parallel x - z \parallel_2^2 + h(z)
\end{align}

Phép cập nhật này cũng có thể được viết lại dưới dạng tương tự gradient descent nhờ ánh xạ gradient tổng quát $$G_{t}$$:

> \begin{align}
> x^{(k)} = x^{(k-1)} - t_k \cdot G_{t_k}(x^{(k-1)}), \space \space \text{với} \space G_{t}(x) = \frac{x-\text{prox}_{t} (x - t \nabla g(x))}{t} \\\\
> \end{align}

#### Hiệu năng
* Hiệu năng của **proximal gradient descent** phụ thuộc trực tiếp vào $$h$$. Nếu $$h$$ phức tạp — đặc biệt khi toán tử prox không có nghiệm dạng đóng — thì mỗi vòng lặp sẽ tốn kém và thuật toán chạy chậm.

* Thuật toán có cùng tốc độ hội tụ theo số vòng lặp với gradient descent trên $$g$$, nhưng chỉ thực sự hiệu quả khi toán tử prox được tính nhanh ở mỗi bước.

## Động lực
Trong **proximal gradient descent**, ở mỗi bước ta xấp xỉ hàm khả vi $$g$$ bằng mô hình bậc hai cục bộ, giữ nguyên phần không khả vi $$h$$ và cực tiểu hóa tổng hai thành phần đó (xem chi tiết tại [09-01 Proximal gradient descent]({% multilang_post_url contents/chapter09/20-01-08-09_01_proximal_gradient_descent %})):

> $$
> \begin{align}
x^+ & = \underset{z}{\text{argmin}}  \, \frac{1}{2t} \parallel x - t \nabla g(x) - z \parallel_2 ^2 + h(z) \\\\
> & = \underset{z}{\text{argmin}} \ \nabla g(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2 + h(z) \\\\
> \end{align}
> $$

Hai số hạng đầu tiên của biểu thức thứ hai xuất phát từ khai triển Taylor bậc hai của $$g$$ (bỏ hằng số $$g(x)$$), trong đó ma trận Hessian $$\nabla^2 g(x)$$ được thay đơn giản bằng $$\frac{1}{t} I$$ (độ cong đẳng hướng — spherical curvature).

Hình dưới đây minh họa cách xấp xỉ bậc hai được dùng để cập nhật nghiệm trong proximal gradient descent.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.01_01_proximal_gradient_descent.png" alt="[Hình 1] Các bước cập nhật của proximal gradient descent [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Các bước cập nhật của proximal gradient descent [3]</figcaption>
</p>
</figure>

Điểm khác biệt cốt lõi giữa gradient descent và phương pháp Newton là việc sử dụng Hessian cục bộ $$\nabla^2 g(x)$$ trong mô hình bậc hai. Nếu thay $$\frac{1}{t} I$$ bằng đúng ma trận Hessian $$\nabla^2 g(x)$$ trong bài toán con ở trên, ta thu được **phương pháp Newton proximal**, sẽ được trình bày ở phần tiếp theo.
