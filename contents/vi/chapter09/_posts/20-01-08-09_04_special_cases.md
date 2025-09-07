---
layout: post
title: '09-04 Các trường hợp đặc biệt'
chapter: '09'
order: 5
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

# Các trường hợp đặc biệt

Phương pháp gradient gần kề cũng được gọi là gradient descent tổng hợp hoặc gradient descent tổng quát.

Tại sao nó được gọi là **"tổng quát"**? Lý do là phương pháp gradient gần kề bao gồm tất cả các trường hợp đặc biệt sau:

- $$h = 0 \to$$ gradient descent
- $$h = I_C \to$$ projected gradient descent 
- $$g = 0 \to$$ thuật toán tối ưu gần kề

Do đó, tất cả các thuật toán này đều có tốc độ hội tụ $$O(1/\epsilon)$$.

## Projected gradient descent
Khi $$I_C(x)$$ là hàm chỉ thị của một tập lồi đóng $$C \in \mathbb{R}^n$$, bài toán tối thiểu hóa $$g(x)$$ trên tập $$C$$ có thể được đổi dạng như sau. (Lưu ý: $$C$$ phải là một tập đóng để phép chiếu được định nghĩa rõ ràng.)

> $$ \min_{x \in C} g(x) \iff \min_x g(x) + I_C(x)$$
>
> $$I_C(x) = 
>\begin{cases}
>0, & x \in C \\
>\infty, & x \notin C
>\end{cases}$$

Lúc này, ánh xạ gần kề được định nghĩa như sau.

> $$
>\begin{align}
>\text{prox}_t(x)  
>&= \underset{z}{\text{argmin}} \frac{1}{2t} \lVert x−z \rVert_2^2 + I_C(z) \\
>& = \underset{z \in C}{\text{argmin}} \lVert x−z \rVert_2^2
>\end{align} $$

Kết quả là, ánh xạ gần kề $$\text{prox}_t(x) = P_C(x)$$ là toán tử chiếu lên $$C$$.

Bước cập nhật gradient gần kề là: $$x^+ = P_C (x−t \nabla g(x) )$$. Nói cách khác, sau khi thực hiện cập nhật gradient descent, bạn chiếu lên $$C$$.

Trong hình dưới đây, hình chữ nhật màu hồng là tập khả thi $$C$$, và vị trí hiện tại là điểm trên của hai điểm dưới hình chữ nhật. Sau khi thực hiện một bước gradient descent, bạn di chuyển ra ngoài $$C$$, vì vậy bạn chiếu ngược lại lên $$C$$ để trở về bên trong tập khả thi.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/projected_gradient_descent.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Hình 1] Projected Gradient Descent [3]]</figcaption>
</p>
</figure>

## Thuật toán tối ưu gần kề

Xem xét bài toán tối thiểu hóa một hàm lồi $$h$$ như sau. Ở đây, $$h$$ không cần khả vi và $$g(x) = 0$$.
>
\begin{align}
\min_x h(x)
\end{align}

Ánh xạ gần kề được định nghĩa là:
> $$
\begin{align}
x^{(k)} &= \text{prox}_{t_k} \big(x^{(k-1)} - t_k \nabla g ( x^{(k-1)} ) \big) , \qquad k = 1, 2, 3, ... \\
&= \text{prox}_{t_k} \big(x^{(k-1)} \big) ,  \qquad \qquad \qquad \qquad \; k = 1, 2, 3, ... \\
\end{align} $$

Do đó, bước cập nhật gradient gần kề là:
> $$x^+ = \underset{z}{\text{argmin}} \frac{1}{2t} \lVert x−z \rVert_2^2 + h(z)$$

Phương pháp gradient gần kề này, chỉ được định nghĩa bởi $$h$$ với $$g = 0$$, được gọi là **thuật toán tối ưu gần kề (PMA)**. Phương pháp này nhanh hơn các phương pháp subgradient, nhưng nếu ánh xạ gần kề không có dạng đóng, nó không thể được triển khai.

## Điều gì xảy ra nếu chúng ta không thể tính prox?
Về mặt lý thuyết, khi áp dụng gradient gần kề cho $$f = g + h$$, giả định rằng hàm prox có thể được tính toán chính xác. Tức là, giả định rằng điểm cực tiểu có thể được tìm thấy chính xác thông qua ánh xạ gần kề.
>  $$\text{prox}_t(x )= \underset{z}{\text{argmin}} \frac{1}{2t} \lVert x−z \rVert_2^2 + h(z)$$

Nói chung, không rõ điều gì xảy ra nếu điểm cực tiểu chỉ được xấp xỉ.
Tuy nhiên, nếu lỗi trong việc xấp xỉ toán tử prox có thể được kiểm soát chính xác, đã được chứng minh rằng tốc độ hội tụ ban đầu có thể được duy trì. (Schmidt et al. (2011), Convergence rates of inexact proximal-gradient methods for convex optimization)

Trong thực tế, nếu prox có thể được tính toán xấp xỉ, nó sẽ được thực hiện với độ chính xác cao.
