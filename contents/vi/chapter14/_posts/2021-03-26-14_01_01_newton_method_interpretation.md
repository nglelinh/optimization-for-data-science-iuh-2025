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

Nhiều sinh viên thuộc lòng công thức $$x^+ = x - (\nabla^2 f(x))^{-1}\nabla f(x)$$ nhưng lại không hiểu *tại sao* biểu thức đó lại có dạng như vậy. Cách hiểu đẹp nhất và tự nhiên nhất chính là đặt phương pháp Newton và Gradient Descent cạnh nhau trên cùng một khung hình: **cả hai đều cực tiểu hóa một mô hình bậc hai cục bộ của $$f$$!**

Sự khác biệt duy nhất nằm ở chất lượng của mô hình xấp xỉ: Gradient Descent thay ma trận độ cong thật $$\nabla^2 f(x)$$ bằng một quả cầu tròn đơn giản $$\frac{1}{2t}\|y - x\|_2^2$$, còn phương pháp Newton giữ nguyên vẹn **khai triển Taylor bậc hai đầy đủ** của $$f$$ tại $$x$$. Nhờ giữ đúng hình dạng hình học thực của hàm, đỉnh của parabol xấp xỉ nằm sát đáy thật hơn rất nhiều.

## Kiến thức cần nhớ: Diễn giải phương pháp Newton như bài toán cực tiểu hóa xấp xỉ bậc hai

- **Khai triển Taylor bậc hai:** Quanh điểm $$x$$, $$\tilde{f}_x(y) = f(x) + \nabla f(x)^T(y-x) + \frac{1}{2}(y-x)^T \nabla^2 f(x)(y-x)$$. Đặt $$\nabla_y \tilde{f}_x(y) = 0$$ cho ra ngay $$\nabla f(x) + \nabla^2 f(x)(y - x) = 0 \implies y = x - (\nabla^2 f(x))^{-1}\nabla f(x)$$.
- **So sánh trực tiếp với Gradient Descent:** Gradient Descent cực tiểu hóa $$f(x) + \nabla f(x)^T(y-x) + \frac{1}{2t}\|y-x\|_2^2$$ — tương đương việc giả vờ rằng $$\nabla^2 f(x) \approx \frac{1}{t}I$$.
- **Diễn giải theo chuẩn Hessian cục bộ:** Bước Newton cũng là hướng giảm dốc nhất nếu ta đo độ dài bước đi bằng **chuẩn Hessian** $$\|v\|_{\nabla^2 f(x)} = \sqrt{v^T \nabla^2 f(x) v}$$ thay vì chuẩn Euclid $$\|v\|_2$$.

### Giải thích: Dựng tường minh parabol Taylor bậc hai và tìm đỉnh của nó

Xét hàm 1 chiều $$f(x) = x^4 - 4x + 5$$ tại điểm xuất phát $$x_0 = 2$$ (nghiệm thật của $$f'(x) = 4x^3 - 4 = 0$$ là $$x^\star = 1$$).

1. **Tính các giá trị đạo hàm tại $$x_0 = 2$$:**
   - $$f(2) = 16 - 8 + 5 = 13$$.
   - $$f'(2) = 4(2)^3 - 4 = 28$$.
   - $$f''(2) = 12(2)^2 = 48$$.
2. **Viết tường minh mô hình parabol Taylor bậc hai quanh $$x_0 = 2$$:**
   $$\tilde{f}_2(y) = 13 + 28(y - 2) + \frac{1}{2}(48)(y - 2)^2 = 13 + 28(y - 2) + 24(y - 2)^2.$$
3. **Tìm điểm cực tiểu của parabol $$\tilde{f}_2(y)$$:**
   Lấy đạo hàm theo $$y$$:
   $$\tilde{f}_2'(y) = 28 + 48(y - 2) = 0 \implies y - 2 = -\frac{28}{48} = -\frac{7}{12} \approx -0.5833.$$
   Vậy điểm tiếp theo là $$x_1 = 2 - \frac{7}{12} = \frac{17}{12} \approx 1.4167$$.
4. **Đối chiếu với bước Gradient Descent dùng mô hình tròn $$\frac{1}{2t}(y-2)^2$$:** Nếu chọn $$t = 1/48$$ (khớp đúng độ cong tại $$x_0$$), GD trong 1 chiều trùng bước Newton; nhưng trong nhiều chiều với các hướng cong khác nhau ($$48$$ và $$1$$), chỉ mô hình Taylor bậc hai đầy đủ mới co giãn đúng cả hai trục cùng lúc!

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

Ta cần tìm $$y$$ để cực tiểu hóa $$f_{approx}(y)$$. Đây là hàm bậc hai theo $$y$$ với Hessian $$\nabla^2 f(x)$$, nên nó lồi khi $$\nabla^2 f(x) \succeq 0$$. Nếu $$\nabla^2 f(x) \succ 0$$ thì $$f_{approx}$$ lồi chặt và có đúng một điểm cực tiểu, chính là điểm làm gradient theo $$y$$ bằng 0. (Nếu Hessian chỉ nửa xác định dương, mô hình có thể không có cực tiểu hoặc có vô số cực tiểu.) Từ đó ta có công thức cập nhật của phương pháp Newton:

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

### Phương pháp Newton: một chiều, hai chiều và khi nào thất bại (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/newton-parabola_vi.mp4"></video>
</div>

Mỗi bước cực tiểu hóa mô hình bậc hai $$f(x_k)+f'(x_k)(x-x_k)+\tfrac12 f''(x_k)(x-x_k)^2$$, dẫn đến công thức cập nhật $$x_{k+1}=x_k-f'(x_k)/f''(x_k)$$.
