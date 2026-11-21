---
layout: post
title: 06-03-06 Can we do better?
chapter: '06'
order: 13
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Gradient descent có tốc độ hội tụ $$O(1/\epsilon)$$ đối với các bài toán biểu diễn bởi hàm lồi, khả vi và có gradient liên tục Lipschitz. Liệu có phương pháp bậc nhất nào nhanh hơn gradient descent không?

### Phương pháp bậc nhất
Một phương pháp bậc nhất biểu diễn bước cập nhật tại vòng lặp thứ $$k$$ như sau: điểm $$x^{(k)}$$ nằm trong không gian sinh bởi các gradient từ vị trí ban đầu $$x^{(0)}$$ đến $$x^{(k−1)}$$.

> $$x^{(k)} \in x^{(0)} + $$ **span**$$\{∇f(x^{(0)}),∇f(x^{(1)}),...,∇f(x^{(k−1)})\}$$

###  Định lý (Nesterov)
Định lý của Nesterov cho một cận dưới về tốc độ hội tụ của các phương pháp bậc nhất.

> **Định lý Nesterov** Với mọi $$k ≤ (n−1)/2$$ và điểm xuất phát $$x^{(0)}$$, tồn tại một hàm $$f$$ sao cho mọi phương pháp bậc nhất đều thỏa mãn điều kiện sau (trong đó $$n$$ là số chiều):<br>
\begin{align}
f(x^{(k)})−f^{\star} ≥ \frac{3L \lVert x^{(0)} −x^{\star} \rVert_2^2}{32(k + 1)^2 }\\\
\end{align}

Vì cận dưới trong định lý Nesterov có $$k^2$$ ở mẫu số, tốc độ hội tụ là $$O(1/k^2)$$. Hơn nữa, số vòng lặp cần thiết là $$O(1/\sqrt{\epsilon})$$. Chúng ta sẽ xem xét nội dung này chi tiết hơn ở phần sau.
