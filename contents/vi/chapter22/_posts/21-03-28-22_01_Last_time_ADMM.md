---
layout: post
title: '22-01 Nhắc lại: ADMM'
chapter: '22'
order: 2
owner: YoungJae Choung
categories:
- chapter22
lang: vi
---


## Nhắc lại: ADMM

Xét bài toán tối ưu có ràng buộc đẳng thức sau:
> $$\begin{align}
> &\min_{x,z} &&f(x) + g(z)\\\\
> &\text{ subject to } &&Ax + Bz = c 
> \end{align}$$

Với tham số $$\rho > 0$$, hàm Lagrangian tăng cường (Augmented Lagrangian) tương ứng có dạng:
> $$ L_\rho(x, z, u) = f(x) + g(z) + u^T(Ax + Bz − c) + \frac{\rho}{2} \| Ax + Bz − c \|^2_2$$

Việc bổ sung số hạng phạt bậc hai $$\frac{\rho}{2} \| Ax + Bz − c \|^2_2$$ giúp cải thiện điều kiện hội tụ của bài toán, đồng thời ADMM vẫn duy trì khả năng tách biến thuận tiện cho tính toán song song thông qua các bước cập nhật luân phiên sau (chứng minh chi tiết đã trình bày ở chương trước).

Các bước lặp ADMM với $$k = 1, 2, 3, \ldots$$:
> $$x^{(k)} = \arg\min_{x} L_\rho(x, z^{(k−1)}, u^{(k−1)})$$
> $$z^{(k)} = \arg\min_{z} L_\rho(x^{(k)}, z, u^{(k−1)})$$
> $$u^{(k)} = u^{(k−1)} + \rho(Ax^{(k)} + Bz^{(k)} − c)$$

## ADMM dạng chuẩn hóa (scaled form)

Đặt biến đối ngẫu chuẩn hóa $$w = u/\rho$$, các bước cập nhật ADMM được viết gọn như sau:

> $$x^{(k)} = \arg\min_{x} f(x) + \frac{\rho}{2} \| Ax + Bz^{(k−1)} − c + w^{(k−1)} \|^2_2$$
> $$z^{(k)} = \arg\min_{z} g(z) + \frac{\rho}{2} \| Ax^{(k)} + Bz − c + w^{(k−1)} \|^2_2$$ 
> $$w^{(k)} = w^{(k−1)} + Ax^{(k)} + Bz^{(k)} − c$$
