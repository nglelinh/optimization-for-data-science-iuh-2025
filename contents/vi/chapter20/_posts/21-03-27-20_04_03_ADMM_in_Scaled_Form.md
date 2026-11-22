---
layout: post
title: '20-04-03 ADMM dạng có tỉ lệ (Scaled Form)'
chapter: '20'
order: 11
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

# ADMM dạng có tỉ lệ

ADMM có thể được viết gọn hơn dưới dạng có tỉ lệ (scaled form) bằng cách đổi biến đối ngẫu $$w = u/\rho$$. Khi đó, các bước lặp của ADMM trở thành:
> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg\min_x f(x) + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c + w^{(k-1)} \rVert_2^2  \\
> z^{(k)} & = \arg\min_z g(z) + \frac{\rho}{2} \lVert Ax^{(k)} + Bz - c + w^{(k-1)} \rVert_2^2  \\
> w^{(k)} & = w^{(k-1)} + Ax^{(k)} + Bz^{(k)} - c 
> \end{alignat}
> $$

## Chứng minh tương đương với dạng ban đầu

Khai triển số hạng bình phương ở bước cập nhật $$x^{(k)}$$:

> $$
> \begin{align}
> x^{(k)} & = \arg\min_x f(x) + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c + w^{(k-1)} \rVert_2^2  \\
> & = \arg\min_x f(x)  + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c \rVert_2^2  + \rho w^{(k-1)T} (Ax + Bz^{(k-1)} - c)  + \frac{\rho}{2}\lVert w^{(k-1)} \rVert_2^2 \\
> & = \arg\min_x f(x)  + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c \rVert_2^2  + u^{(k-1)T} (Ax + Bz^{(k-1)} - c) \\
> \end{align}
> $$

trong đó ta thay $$u^{(k-1)} = \rho w^{(k-1)}$$ và lược bỏ hằng số $$\frac{\rho}{2}\lVert w^{(k-1)} \rVert_2^2$$ không phụ thuộc vào $$x$$. Biến đổi cho bước cập nhật $$z^{(k)}$$ hoàn toàn tương tự.

## Ý nghĩa của biến đối ngẫu có tỉ lệ

Từ quy tắc cập nhật ở trên, $$w^{(k)}$$ chính là tổng tích lũy các phần dư gốc từ đầu cho đến vòng lặp thứ $$k$$:

> $$
> \begin{equation}
> w^{(k)} = w^{(0)} + \sum_{i=1}^k (Ax^{(i)} + Bz^{(i)} - c) 
> \end{equation}
> $$

Dạng có tỉ lệ gọn gàng hơn và thường thuận tiện hơn cả trong phân tích lý thuyết lẫn cài đặt thuật toán.
