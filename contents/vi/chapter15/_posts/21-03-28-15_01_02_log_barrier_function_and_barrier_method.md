---
layout: post
title: '15-01-02 Hàm chắn logarit và phương pháp chắn'
chapter: '15'
order: 4
owner: Minjoo Lee
categories:
- chapter15
lang: vi
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Trước khi phát biểu phương pháp chắn, ta xem xét cách xấp xỉ hàm chỉ thị bằng hàm chắn trơn.

## Xấp xỉ hàm chỉ thị
Hình dưới đây minh họa hàm chỉ thị và các hàm chắn tương ứng. Đường nét đứt là hàm chỉ thị $$I_C$$, còn các đường nét liền là hàm chắn $$\phi(x) = -1/t\log(-x)$$ ứng với $$t = 0.5, 1, 2$$. Hàm chắn xấp xỉ hàm chỉ thị một cách trơn tru, và khi $$t$$ tăng (chẳng hạn $$t = 2$$ trong hình), xấp xỉ càng sát hàm chỉ thị.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_function_01.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">$$\text{[Hình 1] Hàm chắn }\phi(x) = -1/t\log(-x) [1]$$</figcaption>
</p>
</figure>

## Hàm chắn logarit
Giả sử $$h_1, \cdots , h_m : \mathbb{R}^n \to \mathbb{R}$$ là các hàm lồi và khả vi hai lần. Trên tập $$\{x : h_i(x) \lt 0, i = 1, \cdots , m \}$$, **hàm chắn logarit (logarithmic barrier function)** được định nghĩa là:

>
\begin{align}
\phi(x) = - \sum_{i=1}^{m} \log(-h_i(x))
\end{align}

Tập xác định trên được giả sử là phần trong khác rỗng của tập khả thi $$C$$.

## Phương pháp chắn
Sử dụng hàm chắn logarit với tham số $$t \gt 0$$, bài toán tối ưu ban đầu được xấp xỉ bởi bài toán có ràng buộc đẳng thức sau:
>
$$\begin{align}
&\min_{x}           && f(x) + \frac{1}{t} \phi(x) & \qquad      & \min_{x} && tf(x) + \phi(x) \\
&\text{subject to } && Ax = b                     & \iff \qquad & \text{subject to } && Ax = b \\
\end{align}$$

Phương pháp giải bài toán xấp xỉ này bằng phương pháp Newton được gọi là **phương pháp chắn (barrier method)**.
