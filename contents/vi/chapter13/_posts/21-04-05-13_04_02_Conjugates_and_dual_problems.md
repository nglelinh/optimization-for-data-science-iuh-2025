---
layout: post
title: 13-04-02 Hàm liên hợp và bài toán đối ngẫu
chapter: '13'
order: 7
owner: Wontak Ryu
categories:
- chapter13
lang: vi
---

Hàm liên hợp thường xuất hiện trực tiếp khi suy dẫn bài toán đối ngẫu từ bài toán cực tiểu hóa hàm Lagrangian, thông qua hệ thức:

> $$-f^{*}(u) = \min_x (f(x) - u^Tx)$$

Chẳng hạn, xét bài toán tổng hai hàm không ràng buộc:

> $$ \min_x  f(x) + g(x)$$

Ta đưa thêm biến phụ và ràng buộc đẳng thức để viết lại bài toán tương đương:

> $$ \min_{x,z} f(x) + g(z) \text{ với điều kiện } x = z $$

Hàm đối ngẫu Lagrange tương ứng là:

> $$g(u) = \min_{x,z} \left(f(x) + g(z) + u^T(z - x)\right) = -f^{*}(u) - g^{*}(-u)$$

Do đó, bài toán đối ngẫu của bài toán gốc là:

> $$ \max_u -f^{*}(u) - g^{*}(-u)$$

#### Ví dụ

* **Hàm chỉ thị:** Đối ngẫu của $$\min_x f(x) + I_C(x)$$ là:
> $$ \max_u -f^{*}(u) - I^{*}_C(-u)$$
> 
> trong đó $$I^{*}_C$$ là hàm hỗ trợ của tập $$C$$.

* **Hàm chuẩn:** Đối ngẫu của $$\min_x f(x) + \lVert x \rVert$$ là:

> $$ \max_u -f^{*}(u) \text{ với điều kiện } \lVert u \rVert_{*} \le 1$$, trong đó $$\lVert \cdot \rVert_{*}$$ là chuẩn đối ngẫu của $$\lVert \cdot \rVert$$.
