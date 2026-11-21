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

Trước khi tìm hiểu **phương pháp Newton proximal (proximal Newton method)** trong chương này, trước hết hãy ôn lại **proximal gradient descent**.

Chi tiết xem [09 Proximal Gradient Descent and Acceleration]({% multilang_post_url contents/chapter09/20-01-08-09_proximal_gradient_descent_and_acceleration %}).

## Proximal gradient descent
**Proximal gradient descent** áp dụng cho các bài toán có dạng sau.

>$$f(x) = g(x) + h(x)$$

* $$g$$ lồi và khả vi. (**dom**$$(g) = \mathbb{R}^n$$)
* $$h$$ lồi, không khả vi và "đơn giản".


#### Thuật toán
Proximal gradient descent bắt đầu từ điểm ban đầu $$x^{(0)}$$ và lặp lại cập nhật sau.

>$$x^{(k)} = \text{prox}_{t_k}(x^{(k-1)} - t_k \nabla g(x^{(k-1)}) ),\quad k=1,2,3,...$$

Ở đây $$\text{prox}_{t}(\cdot)$$ là toán tử proximal gắn với $$h$$.

> \begin{align}
\text{prox}_{t}(x) = \underset{z}{\text{argmin}}  \frac{1}{2t} \parallel x - z \parallel_2^2 + h(z)
\end{align}

Cập nhật này cũng có thể được viết dưới dạng chuẩn hóa bằng gradient tổng quát $$G_{t}$$.

> \begin{align}
> x^{(k)} = x^{(k-1)} - t_k \cdot G_{t_k}(x^{(k-1)}), \space \space \text{where} \space G_{t}(x) = \frac{x-\text{prox}_{t} (x - t \nabla g(x))}{t} \\\\
> \end{align}

#### Hiệu năng
* Hiệu năng của **proximal gradient descent** phụ thuộc vào $$h$$. Nếu $$h$$ là một hàm phức tạp, đặc biệt nếu prox của nó không có dạng đóng, thì mỗi lần cực tiểu hóa đòi hỏi nhiều tính toán và phương pháp có thể rất chậm.

* Nó có cùng tốc độ hội tụ với gradient descent trên $$g$$. Tuy nhiên, vì toán tử prox được tính ở mỗi vòng lặp, phương pháp chỉ hữu ích khi prox có thể tính hiệu quả.

## Động lực
Trong **proximal gradient descent**, hàm khả vi $$g$$ được xấp xỉ bằng khai triển Taylor bậc hai, hàm không khả vi $$h$$ được cộng vào để tạo thành hàm mục tiêu, và hàm mục tiêu này được cực tiểu hóa lặp đi lặp lại. Điều này có thể viết thành bài toán bậc hai sau.

Chi tiết về suy diễn xem [09-01 Proximal gradient descent]({% multilang_post_url contents/chapter09/20-01-08-09_01_proximal_gradient_descent %}).

> $$
> \begin{align}
x^+ & = \underset{z}{\text{argmin}}  \, \frac{1}{2t} \parallel x - t \nabla g(x) - z \parallel_2 ^2 + h(z) \\\\
> & = \underset{z}{\text{argmin}} \ \nabla g(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2 + h(z) \\\\
> \end{align}
> $$

Số hạng thứ nhất và thứ hai của biểu thức thứ hai đến từ xấp xỉ Taylor bậc hai của $$g$$: ta bỏ số hạng hằng $$g(x)$$ và (như trong gradient descent) thay Hessian $$\nabla^2 g(x)$$ bằng $$\frac{1}{t} I$$ (độ cong cầu, spherical curvature).

Hình sau cho thấy cách $$g$$ được cực tiểu hóa thông qua xấp xỉ bậc hai này trong mỗi bước cập nhật của proximal gradient descent.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.01_01_proximal_gradient_descent.png" alt="[Hình 1] Các bước cập nhật của proximal gradient descent [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Các bước cập nhật của proximal gradient descent [3]</figcaption>
</p>
</figure>

Khác biệt giữa gradient descent và phương pháp Newton là ở chỗ có dùng Hessian cục bộ $$\nabla^2 g(x)$$ trong xấp xỉ bậc hai hay không. Vậy điều gì xảy ra nếu ta dùng $$\nabla^2 g(x)$$ thay cho $$\frac{1}{t} I$$ trong biểu thức trên?

Đây chính là ý tưởng đằng sau **phương pháp Newton proximal**, sẽ được mô tả ở phần tiếp theo.
