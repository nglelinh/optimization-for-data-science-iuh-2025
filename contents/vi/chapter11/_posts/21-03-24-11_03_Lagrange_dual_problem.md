---
layout: post
title: 11-03 Bài toán đối ngẫu Lagrange
chapter: '11'
order: 4
owner: Wontak Ryu
categories:
- chapter11
lang: vi
lesson_type: required
---

Xét bài toán tối ưu tổng quát sau:

>
$$
\begin{alignat}{1}
\min_x & \quad f(x)  \\
s.t.   & \quad h_i(x) \leq 0, i=1,\dots,m  \\
       & \quad l_j(x) = 0, j=1,\dots,r
\end{alignat}
$$

Hàm đối ngẫu $$g(u,v)$$ thỏa mãn $$f^* \geq g(u,v)$$ với mọi $$u \geq 0$$ và $$v$$. Để tìm cận dưới chặt nhất có thể cho $$f^*$$, ta cực đại hóa $$g(u,v)$$ trên miền $$u \geq 0$$. Bài toán thu được gọi là **bài toán đối ngẫu Lagrange**:

>
$$
\begin{alignat}{1}
\max_{u,v} & \quad g(u,v)   \\
           s.t. & \quad u \geq 0
\end{alignat}
$$

Ký hiệu giá trị tối ưu của bài toán đối ngẫu là $$g^*$$, khi đó ta luôn có $$f^* \geq g^*$$. Tính chất này được gọi là **tính đối ngẫu yếu (weak duality)** và luôn đúng bất kể bài toán gốc có lồi hay không. Hơn nữa, **bài toán đối ngẫu luôn là một bài toán tối ưu lồi**, ngay cả khi bài toán gốc không lồi.

Thật vậy, theo định nghĩa, $$g(u,v)$$ là hàm lõm theo $$(u,v)$$ và ràng buộc $$u \geq 0$$ xác định một tập lồi, nên bài toán đối ngẫu là bài toán cực đại hóa một hàm lõm trên một tập lồi:

>
$$
\begin{alignat}{1}
 g(u,v) & = \min_x \{ f(x) + \sum_{i=1}^m u_i h_i(x) + \sum_{j=1}^r v_j l_j(x) \}  \\ 
        & = - \underbrace{\max_x \{ -f(x) - \sum_{i=1}^m u_i h_i(x) - \sum_{j=1}^r v_j l_j(x) \}}_{\text{pointwise maximum of convex functions in $(u,v)$}}
\end{alignat}
$$

## Ví dụ: Cực tiểu hóa hàm bậc bốn không lồi

Xét bài toán cực tiểu hóa hàm không lồi $$f(x) = x^4 - 50x^2 + 100x$$ với ràng buộc $$x \geq -4.5$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter11/dual-gen_13.png" width="70%">
  <figcaption style="text-align: center;">[Hình 4] Ví dụ về tối thiểu hóa hàm bậc bốn không lồi</figcaption>
</p>
</figure>

Trong ví dụ này, hàm đối ngẫu $$g(u)$$ có biểu thức phức tạp:

>
$$
\begin{equation}
 g(u) = \min_{i=1,2,3} \{F_i^4(u) - 50 F_i^2(u) + 100 F_i(u) \}
\end{equation}
$$

trong đó, với $$i = 1, 2, 3$$:

>
$$
\begin{alignat}{1}
F_i(u) = & \frac{- a_i}{12\cdot 2^{1/3}} \left( 432(100-u)-(432^2(100-u)^2 - 4\cdot 1200^3)^{1/2} \right )^{1/3} \\ 
           & - 100 \cdot 2^{1/3} \frac{1}{\left( 432(100-u)-(432^2(100-u)^2 - 4\cdot 1200^3)^{1/2} \right )^{1/3}}
\end{alignat}
$$

và $$a_1 = 1$$, $$a_2 = (-1 + i\sqrt{3})/2$$, $$a_3 = (-1 - i\sqrt{3})/2$$.

Nếu chỉ nhìn vào công thức giải tích trên thì rất khó kiểm tra trực tiếp tính lõm của $$g$$; tuy nhiên, theo tính chất tổng quát của hàm đối ngẫu Lagrange, ta biết chắc chắn rằng $$g(u)$$ là một hàm lõm.
