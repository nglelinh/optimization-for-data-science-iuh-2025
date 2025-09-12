---
layout: post
title: 11-2 Hàm đối ngẫu Lagrange
chapter: '11'
order: 3
owner: Wontak Ryu
categories:
- chapter11
lang: vi
lesson_type: required
---

Gọi $$C$$ là tập khả thi của bài toán gốc và $$f^*$$ là giá trị tối ưu của bài toán gốc. Tối thiểu hóa $$L(x,u,v)$$ trên tất cả $$x$$ cho ta cận dưới sau đây.

>
$$
\begin{equation}
f^* \geq \min_{x \in C} L(x,u,v) \geq \min_x L(x,u,v) := g(u,v)
\end{equation}
$$

Ở đây, $$g(u,v)$$ được gọi là hàm đối ngẫu Lagrange và cung cấp một cận dưới cho $$f^*$$ với bất kỳ $$u\geq 0$$, $$v$$ khả thi đối ngẫu nào.

Ví dụ, trong hình dưới đây

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter11/dual-gen_7.png" width="70%">
  <figcaption style="text-align: center;">[Hình 2] Ví dụ về hàm đối ngẫu Lagrangian[1]</figcaption>
</p>
</figure>


* Đường nằm ngang đứt nét biểu thị hàm $$f^*$$.
* Biến đối ngẫu là $$\lambda$$.
* Đường liền nét biểu thị $$g(\lambda)$$.



## Ví dụ: Chương trình bậc hai
###  1) Xác định dương ($$Q \succ 0$$)

Xem xét bài toán bậc hai sau đây (ở đây $$Q \succ 0$$)
>
$$
\begin{alignat}{1}
\min_x  & \quad \frac{1}{2}x^T Q x + c^T x \\\\
       s.t. & \quad Ax = b, \\\\
            & \quad x \geq 0
\end{alignat}
$$

Khi đó,

#### Hàm Lagrangian:
>
$$
\begin{equation}
L(x,u,v) = \frac{1}{2}x^T Q x + c^T x - u^Tx + v^T (Ax-b)
\end{equation}
$$

#### Hàm đối ngẫu Lagrangian:

Từ biểu thức trên, để tối thiểu hóa hàm Lagrangian, ta lấy đạo hàm theo $$x$$ và tìm $$x^*$$ sao cho đạo hàm bằng không.
\begin{equation}
Qx - (c-u+A^T v) = 0,
\end{equation}
Tức là,
\begin{equation}
Qx = (c-u+A^T v)
\end{equation}
Lúc này, vì $$Q$$ là positive definite nên tồn tại ma trận nghịch đảo, do đó khi tìm $$x^*$$, ta có $$x^* = Q^{-1}(c - u + A^Tv)$$. Vậy nên, khi thay $$x^*$$ vào hàm Lagrangian, ta được kết quả dưới đây.

$$
\begin{alignat}{1}
& (c - u + A^T v)^T (Q^{-1})^T Q Q^{-1}(c - u + A^T v) - (c - u + A^T v)^T Q^{-1} (c - u + A^T v) - b^T v \\\
= & (c - u + A^T v)^T Q^{-1}(c - u + A^T v) - (c - u + A^T v)^T Q^{-1} (c - u + A^T v) - b^T v \\\
= & -\frac{1}{2} (c-u+A^Tv)^T Q^{-1} (c-u+A^T v) - b^T v
\end{alignat}
$$

Do đó,
>
$$
\begin{equation}
g(u,v) = \min_x L(x,u,v) = -\frac{1}{2} (c-u+A^Tv)^T Q^{-1} (c-u+A^T v) - b^T v
\end{equation}
$$

Với mọi $$u \geq 0$$ và $$v$$, điều này tương ứng với một cận dưới của giá trị tối ưu gốc $$f^*$$.

### 2) Nửa xác định dương ($$Q \succeq 0$$)
Cùng bài toán như trên, nhưng lần này nếu $$Q \succeq 0$$,

#### Hàm Lagrangian:
>
$$
\begin{equation}
L(x,u,v) = \frac{1}{2}x^T Q x + c^T x - u^Tx + v^T (Ax-b)
\end{equation}
$$

#### Hàm đối ngẫu Lagrangian:
Giống như khi $$Q$$ là positive definite, ta cần tìm $$x^*$$ thỏa mãn phương trình dưới đây.

$$
\begin{equation}
Qx = (c-u+A^T v)
\end{equation}
$$
Lúc này, vì $$Q$$ là positive semi-definite nên có thể không tồn tại ma trận nghịch đảo. Do đó, ta cần xem xét hai trường hợp sau:

(1) $$c-u+A^T v \in col(Q)$$. Trong trường hợp này, tồn tại $$x^*$$ thỏa mãn $$Qx = (c-u+A^T v)$$, có thể tìm được bằng cách sử dụng nghịch đảo tổng quát $$Q^+$$ (nghịch đảo giả Moore-Penrose, $$Q^+ = (Q^TQ)^{-1}Q^T$$).
(2) $$c-u+A^T v \notin col(Q)$$. Trong trường hợp này, không tồn tại $$x^*$$ thỏa mãn $$Qx = (c-u+A^T v)$$, nghĩa là không có $$x^*$$ nào tối thiểu hóa $$L(x,u,v)$$, và giá trị tối thiểu của $$L(x,u,v)$$ là $$-\infty$$.

Từ hai trường hợp này, hàm đối ngẫu Lagrangian có thể được tóm tắt như sau:
>
$$
g(u,v) =
\begin{cases}
-\frac{1}{2} (c-u+A^T v)^T Q^{+} (c - u + A^T v) - b^T v  & \text{if $c-u+A^T v \perp \text{null}(Q)$} \\\\
-\infty  & \text{otherwise}
\end{cases}
$$

Với mọi $$u\geq 0$$, $$v$$ thỏa mãn $$c-u+A^Tv \perp \text{null}(Q)$$, $$g(u,v)$$ là một cận dưới không tầm thường của $$f^*$$.

## Ví dụ: Chương trình bậc hai trong 2D

Ví dụ, trong hình sau đây, $$f(x_1,x_2)$$ là một hàm bậc hai trên các biến lớn hơn 0 ($$x\ge0$$), và hàm đối ngẫu $$g(u_1,u_2)$$ là một hàm bậc hai trên các biến lớn hơn 0 ($$u\ge0$$).

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter11/dual-gen_10.png" width="70%">
  <figcaption style="text-align: center;">[Hình 3] Ví dụ về chương trình bậc hai trong 2D</figcaption>
</p>
</figure>

* Điểm màu xanh là giá trị tối ưu đối ngẫu, và điểm màu đỏ là giá trị tối ưu gốc.
* Với mọi $$u>0$$, hàm đối ngẫu $$g(u)$$ cung cấp một cận dưới cho $$f^*$$.
* Giá trị tối đa của hàm đối ngẫu $$g(u)$$ trùng khớp chính xác với giá trị $$f^*$$.
