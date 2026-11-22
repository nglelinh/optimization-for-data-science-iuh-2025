---
layout: post
title: 13-04-03 Dịch chuyển biến đổi tuyến tính
chapter: '13'
order: 8
owner: Wontak Ryu
categories:
- chapter13
lang: vi
---

Kỹ thuật lập bài toán đối ngẫu cho phép dịch chuyển phép biến đổi tuyến tính từ một thành phần này sang thành phần khác của hàm mục tiêu.

Xét bài toán sau:

> $$ \min_x f(x) + g(Ax)$$

Ta viết lại bài toán ở dạng tương đương bằng cách đặt $$z = Ax$$:

> $$\min_{x,z} f(x) + g(z) \text{ với điều kiện } Ax = z$$

Từ đó tính hàm đối ngẫu Lagrange:

> $$g(u) = \min_{x,z} \left(f(x) + g(z) + u^T(z - Ax)\right)$$
> $$\qquad  = -\max_{x} \left((A^T u)^T x - f(x)\right) - \max_{z} \left((-u)^T z - g(z)\right)$$
> $$\qquad = -f^* (A^T u) - g^* (-u) $$

Vậy bài toán đối ngẫu là:

> $$\max_u -f^*(A^Tu) - g^*(-u)$$

#### Ví dụ

Với một chuẩn $$\| \cdot \|$$ và chuẩn đối ngẫu tương ứng $$\| \cdot \|_{*}$$, xét cặp bài toán:

> $$ \min_x f(x) + \| Ax \|$$
> 
> $$ \max_u -f^*(A^Tu) \text{ với điều kiện } \| u \|_{*} \leq 1$$

Bài toán thứ nhất là bài toán nguyên thủy, còn bài toán thứ hai là bài toán đối ngẫu tương ứng, trong đó ma trận $$A$$ đã được chuyển sang tác động lên đối số của $$f^*$$ dưới dạng $$A^T u$$.
