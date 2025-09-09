---
layout: post
title: 14-04 Tìm kiếm đường backtracking
chapter: '14'
order: 8
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

Cho đến nay, chúng ta đã xem xét phương pháp Newton thuần túy. Tuy nhiên, phương pháp này không đảm bảo hội tụ, vì vậy chúng ta sử dụng tìm kiếm đường backtracking để đảm bảo hội tụ trong phương pháp Newton có giảm chấn.

## Phương pháp Newton có giảm chấn
Phương pháp Newton thuần túy áp dụng lặp đi lặp lại cập nhật sau (ở đây $$t=1$$):

>\begin{align}
>x^{+} = x -t(\nabla^{2}f(x))^{-1}\nabla f(x).
>\end{align}

Phương pháp Newton có giảm chấn sử dụng tìm kiếm đường backtracking. Nếu giá trị hàm tại vị trí được cập nhật lớn hơn xấp xỉ bậc hai, chúng ta thu nhỏ kích thước bước $$t$$:

>$$\begin{align}
>&\text{với các tham số }0<\alpha \leq \frac{1}{2}, 0<\beta<1, \\
>&\text{trong khi } f(x+tv)>f(x)+\alpha t \nabla f(x)^{T}v\\
>&\text{thu nhỏ }t=\beta t
>\end{align}$$

Here, $$v=-(\nabla^{2}f(x))^{-1}\nabla f(x)$$ and $$\nabla f(x)^{T}v = -\lambda^{2}(x)$$.

## Ví dụ: hồi quy logistic
Làm ví dụ, đối với hồi quy logistic với n = 500, p = 100, chúng ta so sánh tốc độ hội tụ của gradient descent và phương pháp Newton với tìm kiếm đường backtracking.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/2.jpeg" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Hồi quy logistic [3]</figcaption>
</p>
</figure>


Phương pháp Newton cho thấy tốc độ hội tụ nhanh hơn nhiều so với gradient descent. Từ chương tiếp theo, chúng ta sẽ xem xét tốc độ hội tụ này.