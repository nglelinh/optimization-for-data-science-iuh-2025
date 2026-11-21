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

Để định nghĩa thuật toán gốc-đối ngẫu, trước hết hãy định nghĩa ba loại phần dư (residual) và khoảng cách đối ngẫu thay thế (surrogate duality gap). Các phần dư và khoảng cách đối ngẫu thay thế là các đại lượng cần cực tiểu hóa trong thuật toán gốc-đối ngẫu.

## Các phần dư
Các phần dư đối ngẫu, trung tâm và gốc tại $$(x,u,v)$$ được định nghĩa như sau.

> $$r_{dual} = \nabla f(x) +\nabla h(x)u + A^Tv\\$$
> $$r_{cent} =  Uh(x) + τ\mathbb{1} \\ $$ 
> $$r_{prim} = Ax−b$$

Chúng tương ứng với từng hàng của hàm $$r(x,u,v)$$. **Phương pháp điểm trong gốc-đối ngẫu** thực hiện theo hướng làm cho ba phần dư này tiến về 0 chứ không liên tục ép chúng bằng 0. Điều này có nghĩa là trong quá trình thực hiện không cần phải khả thi.

Lý do $$r_{dual}$$ được gọi là phần dư đối ngẫu là vì, như trong phương trình dưới đây, nếu $$r_{dual} = 0$$ thì đảm bảo $$u, v$$ nằm trong miền xác định của $$g$$, tức là khả thi đối ngẫu.

>$$\begin{align}
& r_{dual} = \nabla f(x) +\nabla h(x)u + A^Tv = 0 \\\\
& \iff \min_{x} L(x,u,v) = g(u,v) \\\\
\end{align}$$

Tương tự, thỏa mãn $$r_{prim}=0$$ nghĩa là khả thi gốc, nên $$r_{prim}$$ được gọi là phần dư gốc.

## Khoảng cách đối ngẫu thay thế
Trong khi phương pháp chắn có khoảng cách đối ngẫu vì nó luôn khả thi, phương pháp điểm trong gốc-đối ngẫu dùng **khoảng cách đối ngẫu thay thế** vì không nhất thiết phải khả thi. **Khoảng cách đối ngẫu thay thế** được định nghĩa bởi công thức sau.

> $$−h(x)^Tu  \quad \text{for} \quad h(x) \le 0, u \ge 0$$ 

Nếu $$r_{dual} = 0$$ và $$r_{prim} = 0$$ thì khoảng cách đối ngẫu thay thế trở thành khoảng cách đối ngẫu thực sự. Nói cách khác, nếu khả thi gốc và khả thi đối ngẫu thì khoảng cách đối ngẫu thay thế bằng khoảng cách đối ngẫu thực $$\frac{m}{t}$$.

**[Tham khảo] Các điều kiện KKT nhiễu và tham số t** <br>

* Trong các điều kiện KKT nhiễu, tham số t là $$t = −\frac{m}{h(x)^Tu}$$. 
* Thông tin chi tiết xem [15-03-01 Điều kiện KKT nhiễu]({% multilang_post_url contents/chapter15/21-03-28-15_03_01_perturbed_kkt_conditions %}) và [15-03-02 Khoảng cách dưới tối ưu]({% multilang_post_url contents/chapter15/21-03-28-15_03_02_suboptimality_gap %})

Hơn nữa, nếu $$u > 0,h(x) < 0$$ và điều kiện sau được thỏa mãn thì $$(x,u,v)$$ nằm trên đường trung tâm.

> $$r(x,u,v) = 0$$ với $$\tau = -\frac{h(x)^Tu}{m}$$

Nói cách khác, phần dư bằng 0 tại các điểm nằm trên đường trung tâm.
