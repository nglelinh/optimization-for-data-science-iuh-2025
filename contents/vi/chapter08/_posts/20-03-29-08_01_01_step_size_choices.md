---
layout: post
title: '08-01-01 Lựa chọn kích thước bước'
chapter: '08'
order: 3
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Có nhiều cách khác nhau để chọn **kích thước bước** trong phương pháp subgradient.

Hãy xem xét kỹ hơn hai phương pháp sau:

- **Kích thước bước cố định**: $$t_k = t$$, với $$k = 1, 2, 3, ...$$
- **Kích thước bước giảm dần**: $$t_k$$ thỏa mãn các điều kiện sau:

>\begin{align}
> \sum_{k=1}^{\infty} t_k = \infty, \quad \sum_{k=1}^{\infty} t_k^{2} < \infty
>\end{align}

### Ví dụ về kích thước bước giảm dần

> $$\begin{align}
& t_k = \frac{1}{k}, k = 1,2,3,... 
& \sum_{k=1}^{\infty}t_k = \infty \quad 	ext{(Chuỗi điều hòa)} 
& \sum_{k=1 }^{\infty}t^2_k \approx 1.644934 < \infty \quad 	ext{(Bài toán Basel)} 
\end{align} $$

Một đặc điểm chính của kích thước bước trong phương pháp subgradient là nó phải được thiết lập trước, khác với gradient descent. Nói cách khác, không giống như tìm kiếm đường thẳng backtracking trong gradient descent, kích thước bước trong phương pháp subgradient không thích ứng với độ cong của hàm số.
