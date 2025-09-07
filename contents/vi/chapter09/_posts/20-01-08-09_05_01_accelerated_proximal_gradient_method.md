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

Nếu phương pháp gradient gần kề được tăng tốc, nó có thể đạt được tốc độ hội tụ tối ưu $$O(1/\sqrt{\epsilon})$$. Nesterov đã đề xuất bốn phương pháp, trong đó ba phương pháp là các phương pháp tăng tốc:

- 1983: Phương pháp tăng tốc ban đầu cho các hàm trơn
- 1988: Một phương pháp tăng tốc khác cho các hàm trơn
- 2005: Kỹ thuật làm trơn các hàm không trơn cùng với phương pháp tăng tốc ban đầu
- 2007: Phương pháp tăng tốc cho các hàm tổng hợp

Bây giờ, hãy xem xét phương pháp của Beck và Teboulle (2008), mở rộng phương pháp của Nesterov (1983) cho các hàm tổng hợp.

## Phương pháp gradient gần kề tăng tốc
Như trước, giả sử $$g$$ là hàm lồi và khả vi, và $$h$$ là hàm lồi. Bài toán được định nghĩa là:
> 
\begin{align}
\min_x g(x) + h(x)
\end{align}

**Phương pháp gradient gần kề tăng tốc** xem xét hướng mà $$x$$ đang di chuyển để hướng không thay đổi đột ngột khi di chuyển đến vị trí tiếp theo. Nói cách khác, nó tạo động lượng cho hướng tiến triển, tạo quán tính để tiếp tục di chuyển theo cùng hướng như trước.

Giá trị ban đầu của thuật toán được đặt là $$x^{(0)} = x^{(-1)} \in \mathbb{R}^n$$. Sau đó, sau khi tính toán vị trí $$v$$ xem xét động lượng, gradient gần kề được thực hiện.

> $$
\begin{align}
v & = x^{(k-1)} + \frac{k-2}{k + 1}  (x^{(k-1)} −x^{(k-2)}) \\
x^{(k)} & = \text{prox}_{t_k} (v − t_k \nabla g(v)), k = 1,2,3,...  \\
\end{align} $$

- Trong bước đầu tiên $$k = 1$$, $$x^{(k-1)} −x^{(k-2)}$$ bằng không, vì vậy nó giống như cập nhật gradient gần kề.
- Trong các bước tiếp theo, $$v$$ có động lượng theo hướng trước đó $$x^{(k-1)} −x^{(k-2)}$$. Khi $$k$$ tăng, trọng số động lượng tăng và hội tụ về 1.
- Khi $$h = 0$$, điều này giống như **phương pháp gradient tăng tốc**.

Hình dưới đây cho thấy cách trọng số động lượng thay đổi khi $$k$$ thay đổi.

Trong hình này, giá trị âm khi k = 0, nhưng vì số hạng động lượng bằng không vào thời điểm đó, nên nó không gây ra vấn đề gì. Khi k tăng, trọng số tiến gần 1, vì vậy giá trị được cập nhật nhiều hơn và giúp hội tụ nhanh hơn.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/momentum_weight.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Hình 1] Trọng số động lượng [3]</figcaption>
</p>
</figure>

## Ví dụ Lasso
Nếu chúng ta áp dụng gradient gần kề tăng tốc cho ví dụ Lasso đã thấy trước đó, chúng ta sẽ nhận được kết quả như được hiển thị trong hình dưới đây. Có thể thấy rằng gradient gần kề tăng tốc có hiệu suất nhanh hơn nhiều so với các phương pháp subgradient hoặc gradient gần kề.

Có một phần ở giữa đồ thị nhảy lên, được gọi là "gợn sóng Nesterov". Do đó, gradient gần kề tăng tốc không giảm đơn điệu và không phải là phương pháp giảm.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/accelerated_proximal_gradient.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Hình 2] Gradient Gần kề Tăng tốc [3]</figcaption>
</p>
</figure>