---
layout: post
title: '17-02-02 Khoảng cách đối ngẫu thay thế và các phần dư'
chapter: '17'
order: 5
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---

Để xây dựng thuật toán gốc-đối ngẫu, trước hết ta định nghĩa ba loại phần dư (residual) và đại lượng khoảng cách đối ngẫu thay thế (surrogate duality gap). Đây là các đại lượng mà thuật toán cần đưa về $$0$$.

## Các phần dư
Tại điểm $$(x, u, v)$$, ba phần dư đối ngẫu, trung tâm và gốc được định nghĩa lần lượt như sau:

> $$r_{dual} = \nabla f(x) +\nabla h(x)u + A^Tv\\$$
> $$r_{cent} =  Uh(x) + \tau\mathbb{1} \\ $$ 
> $$r_{prim} = Ax-b$$

Ba đại lượng này tương ứng với ba khối hàng của vector phần dư $$r(x, u, v)$$. **Phương pháp điểm trong gốc-đối ngẫu** điều chỉnh điểm lặp sao cho cả ba phần dư tiến dần về $$0$$, thay vì ép buộc chúng luôn bằng $$0$$ ở mọi bước; vì vậy các điểm lặp trung gian không nhất thiết phải khả thi.

Sở dĩ $$r_{dual}$$ được gọi là phần dư đối ngẫu vì khi $$r_{dual} = 0$$ (cùng với $$u \ge 0$$), điểm $$(u, v)$$ nằm trong miền xác định của hàm đối ngẫu $$g$$, tức là khả thi đối ngẫu:

>$$\begin{align}
& r_{dual} = \nabla f(x) +\nabla h(x)u + A^Tv = 0 \\\\
& \iff \min_{x} L(x,u,v) = g(u,v) \\\\
\end{align}$$

Tương tự, điều kiện $$r_{prim} = 0$$ (cùng với $$h(x) \le 0$$) biểu thị tính khả thi gốc, nên $$r_{prim}$$ được gọi là phần dư gốc.

## Khoảng cách đối ngẫu thay thế
Trong khi phương pháp chắn luôn duy trì điểm khả thi nên có khoảng cách đối ngẫu thực sự ở mọi vòng lặp, phương pháp điểm trong gốc-đối ngẫu không đòi hỏi tính khả thi trung gian nên sử dụng **khoảng cách đối ngẫu thay thế (surrogate duality gap)**, được định nghĩa là:

> $$-h(x)^Tu  \quad \text{với} \quad h(x) \le 0, u \ge 0$$ 

Khi $$r_{dual} = 0$$ và $$r_{prim} = 0$$ (tức là điểm lặp đồng thời khả thi gốc và khả thi đối ngẫu), khoảng cách đối ngẫu thay thế trở thành khoảng cách đối ngẫu thực sự $$\frac{m}{t}$$.

**[Tham khảo] Các điều kiện KKT bị nhiễu và tham số $$t$$** <br>

* Trong hệ điều kiện KKT bị nhiễu, tham số $$t$$ liên hệ với cặp $$(x, u)$$ theo công thức $$t = -\frac{m}{h(x)^Tu}$$. 
* Xem chi tiết tại [15-03-01 Điều kiện KKT nhiễu]({% multilang_post_url contents/chapter15/21-03-28-15_03_01_perturbed_kkt_conditions %}) và [15-03-02 Khoảng cách dưới tối ưu]({% multilang_post_url contents/chapter15/21-03-28-15_03_02_suboptimality_gap %}).

Hơn nữa, nếu $$u > 0, h(x) < 0$$ và thỏa mãn

> $$r(x,u,v) = 0$$ với $$\tau = -\frac{h(x)^Tu}{m}$$

thì $$(x, u, v)$$ nằm chính xác trên đường trung tâm. Nói cách khác, tại mọi điểm thuộc đường trung tâm, toàn bộ phần dư đều bằng $$0$$.
