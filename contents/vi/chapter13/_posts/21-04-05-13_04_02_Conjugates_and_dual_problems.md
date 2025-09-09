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
Hàm liên hợp thường có thể được biểu diễn thông qua việc suy dẫn các bài toán đối ngẫu cho các bài toán tối thiểu hóa Lagrangian như sau:

> $$−f^{∗}(u) = \min_x f(x)−u^Tx$$

Ví dụ, hãy xem xét biểu thức sau:

> $$ \min_x  f(x) + g(x)$$

Biểu thức sau đây có thêm ràng buộc vào biểu thức trên và tương đương với nó:

> $$ \min_{x,z} f(x) + g(z) \text{ với điều kiện } x = z $$

Chuyển đổi điều này thành hàm đối ngẫu Lagrange cho:

> $$g(u) = \min_{x,z} f(x) + g(z) + u^T(z−x) = −f^{∗}(u)−g^{∗}(−u)$$

Do đó, bài toán đối ngẫu của biểu thức gốc có thể được định nghĩa như sau:
> $$ \max_u −f^{∗}(u)−g^{∗}(−u)$$

#### [Ví dụ]
• Hàm chỉ thị: Đối ngẫu của $$ \min_x f(x) + I_C(x)$$ như sau:
> $$ \max_u −f^{∗}(u)−I^{∗}_C(−u)$$
> 
> trong đó $$I^{∗}_C$$ là hàm hỗ trợ của $$C$$

• Chuẩn: 

Đối ngẫu của $$ \min_x f(x) + \rVert x \rVert $$ như sau:
$$ \max_u −f^{∗}(u) \text{ với điều kiện } \rVert u \rVert^{∗} ≤ 1 \text{ trong đó } \rVert · \rVert_{∗} \text{ là chuẩn đối ngẫu của } \rVert · \rVert$$
