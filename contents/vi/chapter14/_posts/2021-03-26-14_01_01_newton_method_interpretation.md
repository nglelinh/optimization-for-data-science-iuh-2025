---
layout: post
title: 14-01-01 Giải thích phương pháp Newton
chapter: '14'
order: 3
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
});
</script>

Trang này trình bày cách dẫn xuất bước cập nhật Newton từ xấp xỉ bậc hai của hàm gốc $$f$$, đồng thời so sánh với bước cập nhật của gradient descent trong [Chương 6]({% multilang_post_url contents/chapter06/21-03-20-06_00_gradient_descent %}).

## Bước cập nhật của phương pháp Newton
Xấp xỉ Taylor bậc hai của hàm $$f$$ quanh điểm $$x$$ có dạng:

>$$
>\begin{align}
>f(y)	\approx f(x) + \nabla f(x)^{T}(y-x) +\frac{1}{2}(y-x)^{T}\nabla^{2}f(x)(y-x),\\\\
>f_{approx}(y)	= f(x) + \nabla f(x)^{T}(y-x) +\frac{1}{2}(y-x)^{T}\nabla^{2}f(x)(y-x).
>\end{align}
>$$

Trong đó, $$y$$ đại diện cho điểm ở bước tiếp theo ($$x^{+}$$), còn $$f_{approx}$$ là hàm xấp xỉ bậc hai của $$f$$.

Ta cần tìm $$y$$ để cực tiểu hóa $$f_{approx}(y)$$. Vì $$f_{approx}$$ là hàm lồi, điểm $$y$$ làm triệt tiêu gradient theo biến $$y$$ chính là điểm cực tiểu và cho ta công thức cập nhật của phương pháp Newton:

>$$
>\begin{align}
>\nabla f_{approx}(y)	&= \nabla f(x) +\frac{1}{2} \Big((\nabla^{2} f(x))^{T}(y-x)+(y-x)^{T}\nabla^{2}f(x)\Big)\\\\
>&=\nabla f(x) +\nabla^{2} f(x)(y-x)\\\\
>& = 0,\\\\
>\Leftrightarrow y &= x-(\nabla^{2}f(x))^{-1}\nabla f(x).
>\end{align}
>$$

## Bước cập nhật của gradient descent
Trong gradient descent, ta cũng dùng khai triển bậc hai của $$f$$, nhưng thay ma trận Hessian bằng ma trận đơn vị chia cho $$t$$:

>$$
>\begin{align}
>f(y)	\approx f(x) + \nabla f(x)^{T}(y-x) +\frac{1}{2t}\|{y-x}\|_{2}^{2},\\\\
>f_{approx}(y)	= f(x) + \nabla f(x)^{T}(y-x) +\frac{1}{2t}\|{y-x}\|_{2}^{2}.\\\\
>\end{align}
>$$

Tương tự phương pháp Newton, cho gradient của $$f_{approx}(y)$$ theo $$y$$ bằng không, ta tìm được điểm cập nhật $$x^{+}$$:

>$$
>\begin{align}
>\nabla f_{approx}(y) &= \nabla f(x) + \frac{1}{t}(y-x), \\\\
> &= 0,\\\\
>y &= x-t\nabla f(x).
>\end{align}
>$$

Kết quả này trùng khớp với công thức cập nhật của gradient descent. Xem thêm chi tiết tại [chương gradient descent]({% multilang_post_url contents/chapter06/21-03-20-06_00_gradient_descent %}).

## Ví dụ
Xét hàm $$f = (10x_{1}^{2}+x_{2}^{2})/2+5\log(1+e^{-x_{1}-x_{2}})$$. Giả sử tại mỗi vòng lặp, ta chọn kích thước bước của gradient descent sao cho độ dài bước đi xấp xỉ bằng độ dài bước cập nhật của phương pháp Newton, rồi so sánh hướng hội tụ của gradient descent (màu đen) và phương pháp Newton (màu xanh).

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/gd.jpeg" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] So sánh giữa gradient descent (màu đen) và phương pháp Newton (màu xanh)[3]</figcaption>
</p>
</figure>

Như minh họa trong Hình 1, vì thay đạo hàm bậc hai bằng một hằng số nhân ma trận đơn vị, gradient descent luôn di chuyển vuông góc với tiếp tuyến của các đường đồng mức và hội tụ chậm hơn phương pháp Newton. Các mục tiếp theo sẽ trình bày tính chất, đặc điểm, phân tích hội tụ và các ví dụ của phương pháp Newton.

### Phương pháp Newton trong một chiều

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/newton-parabola_vi.mp4"></video>
</div>

Mỗi bước cực tiểu hóa mô hình bậc hai $$f(x_k)+f'(x_k)(x-x_k)+\tfrac12 f''(x_k)(x-x_k)^2$$, dẫn đến công thức cập nhật $$x_{k+1}=x_k-f'(x_k)/f''(x_k)$$.
