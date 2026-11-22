---
layout: post
title: 13-02 Giải bài toán nguyên thủy thông qua đối ngẫu
chapter: '13'
order: 3
owner: Wontak Ryu
categories:
- chapter13
lang: vi
lesson_type: required
---

### Một hệ quả quan trọng của điều kiện dừng

Khi tính đối ngẫu mạnh được thỏa mãn và ta đã tìm được nghiệm đối ngẫu tối ưu $$(u^{\star}, v^{\star})$$, nghiệm nguyên thủy tối ưu $$x^{\star}$$ có thể được xác định bằng cách cực tiểu hóa hàm Lagrangian sau:

> $$ \min_x f(x) + \sum_{i=1}^m u_i^{\star} h_i(x) + \sum_{j=1}^r v^{\star}_j l_j(x)$$

Trong nhiều trường hợp, bài toán không ràng buộc này cho phép biểu diễn tường minh đặc trưng của nghiệm nguyên thủy theo nghiệm đối ngẫu. Đặc biệt, nếu bài toán cực tiểu hóa Lagrangian trên có nghiệm duy nhất, thì nghiệm đó chính là nghiệm nguyên thủy tối ưu $$x^{\star}$$. Cách tiếp cận này rất hữu ích khi bài toán đối ngẫu dễ giải hơn nhiều so với bài toán nguyên thủy.

### Ví dụ (Boyd & Vandenberghe, trang 249)

Xét bài toán tách biến có một ràng buộc đẳng thức tuyến tính:

> $$ \min_x \sum_{i=1}^n f_i(x_i) \qquad \text{ với điều kiện }\qquad a^Tx = b$$

Hàm đối ngẫu Lagrange được tính như sau:

> $$\begin{align}
> g(v) &= \min_x \sum_{i=1}^n f_i(x_i) + v(b−a^Tx) \\\
> &= bv + \min_x \sum_{i=1}^n f_i(x_i) −va^Tx \\\
> &= bv + \min_x \sum_{i=1}^n f_i(x_i) −v \sum_{i=1}^n a_ix_i \\\
> &= bv + \sum_{i=1}^n (\underbrace{\min_{x_i} \{ f_i(x_i) − a_ivx_i \}}_{-f^{*}_i(a_iv)}) \\\
> &= bv − \sum_{i=1}^n f^{*}_i (a_iv)
> \end{align}$$

Ở đây $$f_i^{*}$$ là hàm liên hợp của $$f_i$$.

Do đó, bài toán đối ngẫu là:

> $$ \max_v bv − \sum^n_{i=1} f^{*}_i (a_iv)$$

Đổi dấu hàm mục tiêu để chuyển về dạng cực tiểu hóa, ta được:

> $$ \min_v \sum^n_{i=1} f^{*}_i (a_iv) − bv$$

Đây là bài toán tối ưu hóa lồi chỉ theo một biến vô hướng $$v$$, nên thường dễ giải hơn nhiều so với bài toán nguyên thủy có $$n$$ biến.

Sau khi tìm được $$v^{\star}$$, nghiệm nguyên thủy $$x^{\star}$$ được xác định từ:

> $$ \min_{x} \sum^n_{i=1} (f_i(x_i) − a_iv^{\star}x_i)$$

Nếu mỗi hàm $$f_i$$ lồi chặt, bài toán này có nghiệm duy nhất; khi các $$f_i$$ khả vi, từng thành phần $$x_i^{\star}$$ được tìm trực tiếp bằng cách giải phương trình $$\nabla f_i(x_i) = a_i v^{\star}$$ với mỗi $$i$$.
