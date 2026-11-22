---
layout: post
title: '08-01-01 Lựa chọn kích thước bước'
chapter: '08'
order: 3
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
lesson_type: required
---

Có nhiều cách để lựa chọn **kích thước bước** trong phương pháp subgradient. Dưới đây là hai cách phổ biến:

- **Kích thước bước cố định**: $$t_k = t$$ với mọi $$k = 1, 2, 3, ...$$
- **Kích thước bước giảm dần**: dãy $$t_k$$ thỏa mãn đồng thời hai điều kiện:

>\begin{align}
> \sum_{k=1}^{\infty} t_k = \infty, \quad \sum_{k=1}^{\infty} t_k^{2} < \infty
>\end{align}

### Ví dụ về kích thước bước giảm dần

> $$\begin{align}
& t_k = \frac{1}{k}, k = 1,2,3,... \\
& \sum_{k=1}^{\infty}t_k = \infty \quad \text{(Chuỗi điều hòa)} \\
& \sum_{k=1}^{\infty}t^2_k \approx 1.644934 < \infty \quad \text{(Bài toán Basel)}
\end{align} $$

Một đặc điểm quan trọng của phương pháp subgradient là kích thước bước thường phải được chọn trước, khác với gradient descent. Nói cách khác, không giống tìm kiếm đường thẳng lùi (backtracking line search) trong gradient descent, kích thước bước ở đây không tự điều chỉnh theo độ cong cục bộ của hàm mục tiêu.
