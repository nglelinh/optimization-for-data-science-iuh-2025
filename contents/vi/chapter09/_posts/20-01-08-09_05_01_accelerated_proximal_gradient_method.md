---
layout: post
title: '09-05-01 Phương pháp gradient gần kề tăng tốc'
chapter: '09'
order: 7
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

# Phương pháp gradient gần kề tăng tốc

Khi bổ sung kỹ thuật tăng tốc, phương pháp gradient gần kề đạt được tốc độ hội tụ tối ưu $$O(1/\sqrt{\epsilon})$$. Trong chuỗi nghiên cứu của mình, Nesterov đã đề xuất bốn phương pháp nổi tiếng, trong đó có ba phương pháp tăng tốc:

- 1983: Phương pháp tăng tốc đầu tiên cho các hàm trơn
- 1988: Một biến thể tăng tốc khác cho các hàm trơn
- 2005: Kỹ thuật làm trơn hàm không trơn kết hợp với phương pháp tăng tốc năm 1983
- 2007: Phương pháp tăng tốc cho các bài toán tối ưu tổng hợp

Dưới đây, chúng ta trình bày phương pháp của Beck và Teboulle (2008), mở rộng phương pháp Nesterov (1983) cho lớp hàm tổng hợp.

## Thuật toán gradient gần kề tăng tốc
Tương tự các bài trước, giả sử $$g$$ là hàm lồi khả vi và $$h$$ là hàm lồi. Xét bài toán:
> 
\begin{align}
\min_x g(x) + h(x)
\end{align}

**Phương pháp gradient gần kề tăng tốc** tận dụng hướng dịch chuyển của bước trước để tránh đổi hướng đột ngột ở bước tiếp theo. Nói cách khác, thuật toán bổ sung một thành phần động lượng tạo quán tính theo hướng tiến triển gần nhất.

Khởi tạo $$x^{(0)} = x^{(-1)} \in \mathbb{R}^n$$. Tại mỗi bước $$k = 1, 2, 3, \dots$$, ta tính điểm ngoại suy $$v$$ có xét đến động lượng, rồi áp dụng bước gradient gần kề tại $$v$$:

> $$
\begin{align}
v & = x^{(k-1)} + \frac{k-2}{k + 1}  (x^{(k-1)} −x^{(k-2)}) \\
x^{(k)} & = \text{prox}_{t_k} (v − t_k \nabla g(v)), k = 1,2,3,...  \\
\end{align} $$

- Ở bước đầu tiên ($$k = 1$$), vì $$x^{(0)} - x^{(-1)} = 0$$, điểm $$v$$ trùng với $$x^{(0)}$$ nên bước cập nhật giống hệt phương pháp gradient gần kề tiêu chuẩn.
- Từ các bước sau trở đi, $$v$$ được dịch thêm một lượng động lượng theo hướng $$x^{(k-1)} - x^{(k-2)}$$. Khi $$k$$ tăng, trọng số động lượng tăng dần và tiến về $$1$$.
- Khi $$h = 0$$, thuật toán trở về **phương pháp gradient tăng tốc (accelerated gradient method)**.

Hình dưới đây minh họa sự biến thiên của trọng số động lượng theo $$k$$. Ở các giá trị $$k$$ đầu tiên, trọng số có giá trị âm, nhưng tại $$k = 1$$ hiệu $$x^{(0)} - x^{(-1)} = 0$$ nên thành phần động lượng triệt tiêu và không gây ảnh hưởng. Khi $$k$$ tăng, trọng số tiến gần về $$1$$, giúp duy trì quán tính mạnh hơn và tăng tốc độ hội tụ.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/momentum_weight.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Hình 1] Trọng số động lượng [3]</figcaption>
</figure>

## Ví dụ trên bài toán Lasso
Khi áp dụng phương pháp gradient gần kề tăng tốc cho bài toán Lasso đã xét trước đó, đồ thị hội tụ dưới đây cho thấy tốc độ hội tụ vượt trội so với cả phương pháp subgradient và phương pháp gradient gần kề tiêu chuẩn.

Có thể quan sát một đoạn ở giữa đồ thị mà giá trị hàm mục tiêu tạm thời tăng lên — hiện tượng này được gọi là "gợn sóng Nesterov" (Nesterov ripples). Điều này cho thấy phương pháp gradient gần kề tăng tốc không đảm bảo giảm đơn điệu giá trị hàm mục tiêu ở mọi bước lặp.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/accelerated_proximal_gradient.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Hình 2] Gradient Gần kề Tăng tốc [3]</figcaption>
</figure>