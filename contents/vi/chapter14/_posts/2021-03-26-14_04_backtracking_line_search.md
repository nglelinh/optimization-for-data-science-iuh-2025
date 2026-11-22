---
layout: post
title: 14-04 Tìm kiếm đường backtracking
chapter: '14'
order: 10
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Đến đây, chúng ta mới xét phương pháp Newton thuần túy. Vì phương pháp này không đảm bảo hội tụ toàn cục, ta kết hợp thêm tìm kiếm đường backtracking để thu được phương pháp Newton có giảm chấn (damped Newton method).

## Phương pháp Newton có giảm chấn
Phương pháp Newton thuần túy lặp lại công thức cập nhật sau với $$t = 1$$:

>\begin{align}
>x^{+} = x -t(\nabla^{2}f(x))^{-1}\nabla f(x).
>\end{align}

Phương pháp Newton có giảm chấn sử dụng tìm kiếm đường backtracking: nếu giá trị hàm tại điểm cập nhật lớn hơn cận trên từ xấp xỉ tuyến tính có hệ số $$\alpha$$ (điều kiện giảm đủ Armijo), ta thu nhỏ kích thước bước $$t$$:

>$$
>\begin{align}
>&\text{với các tham số }0<\alpha \leq \frac{1}{2}, 0<\beta<1, \\
>&\text{trong khi } f(x+tv)>f(x)+\alpha t \nabla f(x)^{T}v\\
>&\text{thu nhỏ }t=\beta t
>\end{align}
>$$

Ở đây, $$v=-(\nabla^{2}f(x))^{-1}\nabla f(x)$$ và $$\nabla f(x)^{T}v = -\lambda^{2}(x)$$.

## Ví dụ: hồi quy logistic
Xét bài toán hồi quy logistic với $$n = 500$$ và $$p = 100$$ để so sánh tốc độ hội tụ giữa gradient descent và phương pháp Newton kết hợp tìm kiếm đường backtracking.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/2.jpeg" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Hồi quy logistic [3]</figcaption>
</p>
</figure>

Phương pháp Newton hội tụ nhanh hơn đáng kể so với gradient descent. Mục tiếp theo sẽ phân tích lý thuyết tốc độ hội tụ này.