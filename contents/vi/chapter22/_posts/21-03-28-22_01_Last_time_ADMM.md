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
Xét bài toán tối ưu sau
> $$\begin{align}
> &\min_{x,z} &&f(x) + g(z)\\\\
> &\text{ subject to } &&Ax + Bz = c 
> \end{align}$$

Chuyển bài toán này sang dạng Augmented Lagrangian ta được như sau (với $$ρ > 0$$ nào đó).
> $$ L_ρ(x, z, u) = f(x) + g(z) + u^T(Ax + Bz − c) + \frac{ρ}{2} \| Ax + Bz − c \|^2_2$$

Phương trình trên trở nên lồi mạnh nhờ thêm số hạng $$\frac{ρ}{2} \| Ax + Bz − c \|^2_2$$, và có thể được biến đổi thành dạng hữu ích cho xử lý song song như phương trình sau.
* Để xem chứng minh chi tiết, hãy tham khảo nội dung chương trước.
ADMM: với $$k = 1, 2, 3, . . .$$
> $$x^{(k)} = argmin_{x} L_ρ(x, z^{(k−1)}, u^{(k−1)})$$
> $$z^{(k)} = argmin_{z} L_ρ(x^{(k)}  , z, u^{(k−1)})$$
> $$u^{(k)} = u^{(k−1)} + ρ(Ax^{(k)} + Bz^{(k)} − c)$$
 
## ADMM dạng có tỉ lệ
Hãy đổi biến đối ngẫu $$u$$ sang biến có tỉ lệ $$w = u/ρ$$. Khi đó các bước ADMM có thể được tính như sau.

> $$x^{(k)} = argmin_{x} f(x) + \frac{ρ}{2} \| Ax + Bz^{(k−1)} − c + w^{(k−1)} \|^2_2$$
> $$z^{(k)} = argmin_{z} g(z) + \frac{ρ}{2} \| Ax^{(k)} + Bz − c + w^{(k−1)} \|^2_2$$ 
> $$w^{(k)} = w^{(k−1)} + Ax^{(k)} + Bz^{(k)} − c$$
