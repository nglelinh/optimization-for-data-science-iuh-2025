---
layout: post
title: 13-02 Giải bài toán nguyên thủy thông qua đối ngẫu
chapter: '13'
order: 3
owner: Wontak Ryu
categories:
- chapter13
lang: vi
lesso_type: required
---

### Một hệ quả quan trọng của điều kiện dừng
Trong điều kiện đối ngẫu mạnh, khi nghiệm đối ngẫu $$u^{\star}, v^{\star}$$ được cho, nghiệm nguyên thủy $$x^{\star}$$ có thể được tìm bằng cách giải Lagrangian sau:

> $$ \min_x f(x) + \sum_{i=1}^m u_i^{\star} h_i(x) + \sum_{j=1}^r v^{\star}_i l_j(x)$$

Thông thường, nghiệm của các bài toán không ràng buộc như vậy có thể được biểu diễn bằng cách thể hiện rõ ràng các đặc điểm của nghiệm nguyên thủy thông qua nghiệm đối ngẫu.

Hơn nữa, nếu nghiệm của bài toán này là duy nhất, nghiệm đối ngẫu trở thành nghiệm nguyên thủy $$x^{\star}$$.
Điều này rất hữu ích khi việc giải bài toán đối ngẫu dễ dàng hơn việc giải trực tiếp bài toán nguyên thủy.


### Ví dụ từ B & V trang 249:
> $$ \min_x \sum_{i=1}^n f_i(x_i) \qquad \text{ với điều kiện }\qquad a^Tx = b$$


> $$\begin{align}
> g(v) &= \min_x \sum_{i=1}^n f_i(x_i) + v(b−a^Tx) \\\
> &= bv + \min_x \sum_{i=1}^n f_i(x_i) −va^Tx \\\
> &= bv + \min_x \sum_{i=1}^n f_i(x_i) −v \sum_{i=1}^n a_ix_i \\\
> &= bv + \sum_{i=1}^n (\underbrace{\min_{x_i} \{ f_i(x_i) − a_ivx_i \}}_{-f^{*}_i(a_iv)}) \\\
> &= bv − \sum_{i=1}^n f^{*}_i (a_iv)
> \end{align}$$
 
Ở đây $$f^{*}$$ biểu thị hàm liên hợp của $$f_i$$.

Do đó, bài toán đối ngẫu có thể được biểu diễn như sau:
> $$ \max_v bv − \sum^n_{i=1} f^{*}_i (a_iv)$$

Ngoài ra, bằng cách nhân với dấu âm (-), bài toán cực đại có thể được biểu diễn thành bài toán cực tiểu sau:
> $$ \min_v \sum^n_{i=1} f^{*}_i (a_iv) − bv$$

Đây là một bài toán tối ưu hóa lồi với các biến vô hướng có thể được giải dễ dàng hơn nhiều so với bài toán nguyên thủy.

Khi $$v^{\star}$$ được cho, nghiệm nguyên thủy $$x^{\star}$$ có thể được giải như sau:
> $$ \min_{x} \sum^n_{i=1} (f_i(x_i) − a_iv^{\star}x_i)$$

Tính lồi chặt của mỗi $$f_i$$ có nghĩa là bài toán này có nghiệm duy nhất.
Tức là, $$x^{\star}$$ được thu được thông qua tính toán $$∇f_i(x_i) = a_iv^{\star}$$ cho mỗi $$i$$.

