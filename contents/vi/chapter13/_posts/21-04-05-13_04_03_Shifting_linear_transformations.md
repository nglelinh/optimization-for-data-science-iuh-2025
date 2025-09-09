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

Công thức đối ngẫu giúp dịch chuyển các biến đổi tuyến tính giữa các phần của hàm mục tiêu và các miền khác.

Hãy xem xét điều sau:
> $$ \min_x f(x) + g(Ax)$$

Biểu thức sau tương đương:
> $$min_{x,z} f(x) + g(z) \text { với điều kiện } Ax = z$$

Điều này dẫn đến quá trình đối ngẫu sau:
> $$\text {g(u)} = \min_{x,z} f(x) + g(z) + u^T(z - Ax)$$
> $$\qquad  = -\max_{x} (A^T u)^T x - f(x) - \max_{z} (-u)^T z - g(z)  $$
> $$\qquad = -\ f^* (A^T u) - g^* (-u) $$

Và đối ngẫu là:
> $$\max_u -f^*(A^Tu) - g^*(-u)$$

#### [Ví dụ]
Chuẩn và chuẩn đối ngẫu của chúng có mối quan hệ như sau: $$\| \cdot \|, \| \cdot \|^*$$, các bài toán 

> $$ \min_x f(x) +\| Ax \|$$
> 
> $$ \max_u -f^*(A^Tu) \text{ với điều kiện } \| u \|^* \leq 1$$

Biểu thức đầu tiên là nguyên thủy, và biểu thức thứ hai là đối ngẫu, có thể được giải trực tiếp.
