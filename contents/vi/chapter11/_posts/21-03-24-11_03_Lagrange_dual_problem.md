---
layout: post
title: 11-3 Bài toán đối ngẫu Lagrange
chapter: '11'
order: 4
owner: Wontak Ryu
categories:
- chapter11
lang: vi
lesson_type: required
---

Xem xét bài toán tối ưu sau đây:
>
$$
\begin{alignat}{1}
\min_x & \quad f(x)  \\
s.t.   & \quad h_i(x) \leq 0, i=1,\dots,m  \\
       & \quad l_j(x) = 0, j=1,\dots,r
\end{alignat}
$$

Hàm đối ngẫu $$g(u,v)$$ thỏa mãn $$f^* \geq g(u,v)$$ với mọi $$u\geq 0$$ và $$v$$. Do đó, chúng ta có thể thu được cận dưới tốt nhất bằng cách tối đa hóa $$g(u,v)$$ trên tất cả $$u$$ và $$v$$ khả thi. Điều này được gọi là bài toán đối ngẫu Lagrange. 
>
$$
\begin{alignat}{1}
\max_{u,v} & \quad g(u,v)   \\
           s.t. & \quad u \geq 0
\end{alignat}
$$

Ở đây, nếu ta ký hiệu giá trị tối ưu đối ngẫu là $$g^*$$, thì $$f^* \geq g^*$$. Điều này được gọi là tính đối ngẫu yếu. Tính chất này luôn đúng ngay cả khi bài toán gốc không lồi. Hơn nữa, bài toán đối ngẫu luôn là một bài toán tối ưu lồi, ngay cả khi bài toán gốc không lồi.

Theo định nghĩa, $$g$$ là hàm lõm theo $$(u,v)$$, và $$u \geq 0$$ là một ràng buộc lồi. Do đó, bài toán đối ngẫu tương ứng với một bài toán tối đa hóa hàm lõm. 
>
\begin{alignat}{1}
 g(u,v) & = \min_x \{ f(x) + \sum_{i=1}^m u_i h_i(x) + \sum_{j=1}^r v_j l_j(x) \}  \\ 
        & = - \underbrace{\max_x \{ -f(x) - \sum_{i=1}^m u_i h_i(x) - \sum_{j=1}^r v_j l_j(x) \}}_{\text{pointwise maximum of convex functions in $(u,v)$}}
\end{alignat}




## Ví dụ: Tối thiểu hóa hàm bậc bốn không lồi
Hãy tối thiểu hóa hàm $$f(x)=x^4 - 50 x^2 + 100 x$$ với điều kiện $$x \geq -4.5$$.


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter11/dual-gen_13.png" width="70%">
  <figcaption style="text-align: center;">[Hình 4] Ví dụ về tối thiểu hóa hàm bậc bốn không lồi</figcaption>
</p>
</figure>

Trong trường hợp này, hàm đối ngẫu $$g$$ như sau: 
>
$$
\begin{equation}
 g(u) = \min_{i=1,2,3} \{F_i^4(u) - 50 F_i^2(u) + 100 F_i(u) \}
\end{equation}
$$

where, for $$i=1,2,3$$, 
>
$$
\begin{alignat}{1}
F_i(u) = & \frac{- a_i}{12\cdot 2^{1/3}} \left( 432(100-u)-(432^2(100-u)^2 - 4\cdot 1200^3)^{1/2} \right )^{1/3} \\ 
           & - 100 \cdot 2^{1/3} \frac{1}{\left( 432(100-u)-(432^2(100-u)^2 - 4\cdot 1200^3)^{1/2} \right )^{1/3}}
\end{alignat}
$$

và $$a_1=1, a_2 = (-1+i\sqrt{3})/2, a_3 = (-1-i \sqrt{3})/2$$.
Mặc dù khó xác định liệu $$g$$ có lõm hay không chỉ bằng cách nhìn vào hàm số, nhưng chúng ta có thể biết rằng $$g$$ là hàm lõm dưới tính chất lồi của tính đối ngẫu.
