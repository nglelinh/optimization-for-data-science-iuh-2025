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

Khi lái một chiếc máy bay xuyên qua sương mù, phi công không thể chỉ nhìn ra cửa sổ mà phải theo dõi đồng hồ độ cao, tốc độ và góc nghiêng. Trong phương pháp điểm trong gốc–đối ngẫu, vì các điểm lặp trung gian không còn bắt buộc phải khả thi, ta không thể tính khoảng cách đối ngẫu thực $$f(x) - g(u, v)$$ ở mọi bước. Thay vào đó, ta theo dõi ba "đồng hồ chỉ báo" là ba vector phần dư $$r_{\text{prim}}, r_{\text{dual}}, r_{\text{cent}}$$ cùng với **khoảng cách đối ngẫu thay thế** $$\eta = -h(x)^T u$$.

## Bản đồ kiến thức nền: Đọc hiểu các chỉ số hội tụ của bộ giải gốc–đối ngẫu

Bốn khái niệm dưới đây giải thích tại sao mọi bộ giải điểm trong công nghiệp đều in ra cột `p_res`, `d_res` và `gap` trên màn hình nhật ký:

- **Phần dư gốc (Primal Residual, $$r_{\text{prim}} = Ax - b$$):** Đo mức độ vi phạm ràng buộc đẳng thức. Khi $$r_{\text{prim}} = 0$$ cùng với $$h(x) \le 0$$, điểm $$x$$ chính thức là điểm khả thi của bài toán gốc.
- **Phần dư đối ngẫu (Dual Residual, $$r_{\text{dual}} = \nabla f(x) + \nabla h(x)u + A^T v$$):** Đo mức độ vi phạm điều kiện dừng của hàm Lagrange. Khi $$r_{\text{dual}} = 0$$ và $$u \ge 0$$, cặp $$(u, v)$$ thuộc miền xác định của hàm đối ngẫu $$g(u, v)$$ và cho ra một cận dưới hợp lệ cho $$p^\star$$.
- **Phần dư trung tâm (Centrality Residual, $$r_{\text{cent}} = Uh(x) + \tau\mathbf{1}$$):** Đo khoảng cách từ điểm hiện tại tới đường trung tâm ứng với tham số $$\tau$$. Khi $$\tau \to 0$$ và $$r_{\text{cent}} \to 0$$, điều kiện bù chặt được thỏa mãn.
- **Khoảng cách đối ngẫu thay thế (Surrogate Duality Gap, $$\eta = -h(x)^T u$$):** Vì $$h(x) < 0$$ và $$u > 0$$, đại lượng $$\eta$$ luôn dương. Khi cả $$r_{\text{prim}} = 0$$ và $$r_{\text{dual}} = 0$$, $$\eta$$ trùng khớp chính xác với khoảng cách đối ngẫu thực $$f(x) - g(u, v)$$; còn khi chưa khả thi, nó là thước đo thay thế tin cậy để điều chỉnh tham số $$\tau$$.

### Khung giải thích (nên đọc chậm): Tính ba phần dư và phân biệt khoảng cách đối ngẫu thay thế với khoảng cách thực

Xét bài toán quy hoạch tuyến tính 2 biến:

$$\min_{x_1, x_2} \; x_1 + 2x_2 \qquad \text{với điều kiện} \qquad x_1 + x_2 = 4, \quad h_1(x) = -x_1 \le 0, \quad h_2(x) = -x_2 \le 0.$$

Xét điểm lặp trung gian $$x = (3, 2)$$, $$u = (0.4, 0.6)$$, $$v = -1.2$$, với tham số $$\tau = 0.25$$:

1. **Phần dư gốc:** $$r_{\text{prim}} = x_1 + x_2 - 4 = 3 + 2 - 4 = +1$$ (chưa khả thi gốc).
2. **Phần dư đối ngẫu:** Với $$\nabla f(x) = (1, 2)^T$$, $$\nabla h(x) = -I$$, $$A^T = (1, 1)^T$$:
   $$r_{\text{dual}} = \begin{bmatrix} 1 \\ 2 \end{bmatrix} - \begin{bmatrix} 0.4 \\ 0.6 \end{bmatrix} + (-1.2)\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} -0.6 \\ 0.2 \end{bmatrix} \ne 0$$ (chưa khả thi đối ngẫu).
3. **Khoảng cách đối ngẫu thay thế:**
   $$\eta = -h(x)^T u = x_1 u_1 + x_2 u_2 = (3)(0.4) + (2)(0.6) = 1.2 + 1.2 = 2.4.$$
   Lưu ý: vì $$r_{\text{dual}} \ne 0$$, hàm Lagrange $$L(x, u, v)$$ không bị chặn dưới theo $$x$$, nên $$g(u, v) = -\infty$$ — khoảng cách đối ngẫu *thực* bằng $$+\infty$$, nhưng khoảng cách *thay thế* $$\eta = 2.4$$ vẫn hữu hạn và hoàn toàn đo đạc được!
4. **Phần dư trung tâm:**
   $$r_{\text{cent}} = \begin{bmatrix} -x_1 u_1 + \tau \\ -x_2 u_2 + \tau \end{bmatrix} = \begin{bmatrix} -1.2 + 0.25 \\ -1.2 + 0.25 \end{bmatrix} = \begin{bmatrix} -0.95 \\ -0.95 \end{bmatrix}.$$
5. **Bài học rút ra:** Do $$\eta$$ chỉ trở thành khoảng cách đối ngẫu thực khi điểm lặp khả thi, điều kiện dừng của thuật toán PD-IPM **bắt buộc** phải kiểm tra đồng thời cả ba: $$\|r_{\text{prim}}\|_2 \le \epsilon_{\text{feas}}$$, $$\|r_{\text{dual}}\|_2 \le \epsilon_{\text{feas}}$$ và $$\eta \le \epsilon$$.

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
