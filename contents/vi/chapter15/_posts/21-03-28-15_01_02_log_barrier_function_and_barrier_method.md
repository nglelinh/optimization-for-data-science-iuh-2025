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
Trước khi giới thiệu phương pháp chắn, trước hết hãy xem hàm chỉ thị có thể được xấp xỉ bằng hàm chắn như thế nào.

## Xấp xỉ hàm chỉ thị
Trong hình dưới đây, bạn có thể thấy hàm chỉ thị và hàm chắn. Đường nét đứt là hàm chỉ thị $$I_C$$, còn các đường nét liền là hàm chắn $$\phi(x) = -1/t\log(-x)$$ với $$t = 0.5, 1, 2$$. Hàm chắn xấp xỉ hàm chỉ thị một cách trơn tru, và khi $$t=2$$ cho xấp xỉ tốt nhất.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_function_01.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">$$\text{[Hình 1] Hàm chắn }\phi(x) = -1/t\log(-x) [1]$$</figcaption>
</p>
</figure>


## Hàm chắn logarit
Giả sử $$h_1, \cdots , h_m : \mathbb{R}^n \to \mathbb{R}$$ là các hàm lồi và khả vi hai lần. Đối với tập $$ \{x : h_i(x) \lt 0, i = 1, \cdots , m \}$$, hàm sau được gọi là hàm chắn logarit.

>
\begin{align}
\phi(x) = - \sum_{i=1}^{m} \log(-h_i(x))
\end{align}

Ở đây, tập này được giả sử là phần trong của tập khả thi $$C$$ và khác rỗng.

## Phương pháp chắn

Sử dụng hàm chắn, bài toán ban đầu có thể được xấp xỉ như sau. Ở đây $$t\gt 0$$.
>
$$\begin{align}
&\min_{x}           && f(x) + \frac{1}{t} \phi(x) & \qquad      & \min_{x} && tf(x) + \phi(x) \\
&\text{subject to } && Ax = b                     & \iff \qquad & \text{subject to } && Ax = b \\
\end{align}$$

Phương pháp giải bài toán được định nghĩa như vậy bằng phương pháp Newton được gọi là **phương pháp chắn (barrier method)**.
