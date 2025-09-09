---
layout: post
title: 14-01-01 Giải thích phương pháp Newton
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

Trang này xem xét cách bước cập nhật đã thảo luận trước đó được dẫn xuất từ xấp xỉ bậc hai của hàm số gốc $$f$$. Chúng ta cũng so sánh nó với bước cập nhật gradient descent được đề cập trong [Chương 6]({% multilang_post_url contents/chapter06/21-03-20-06_00_gradient_descent %}).

## Bước cập nhật phương pháp Newton
Xấp xỉ Taylor bậc hai (xấp xỉ bậc hai) của hàm số $$f$$ như sau:

>$$
>\begin{align}
>f(y)	\approx f(x) + \nabla f(x)^{T}(y-x) +\frac{1}{2}(y-x)^{T}\nabla^{2}f(x)(y-x),\\\\
>f_{approx}(y)	= f(x) + \nabla f(x)^{T}(y-x) +\frac{1}{2}(y-x)^{T}\nabla^{2}f(x)(y-x).
>\end{align}
>$$

Ở đây, $$y$$ là giá trị $$x$$ của bước tiếp theo, tức là $$x^{+}$$. Chúng ta cũng định nghĩa xấp xỉ bậc hai là $$f_{approx}$$.

Chúng ta muốn tìm đầu vào $$y$$ để tối thiểu hóa $$f_{approx}$$ này, tức là xấp xỉ bậc hai. Vì $$f_{approx}$$ là lồi, đầu vào $$y$$ làm cho gradient của phương trình trên bằng không sẽ tối thiểu hóa $$f_{approx}$$. Kết quả này trở thành công thức cập nhật bước trong phương pháp Newton. Hãy nhớ rằng việc lấy đạo hàm trong phương trình dưới đây là theo y.

>$$
>\begin{align}
>\nabla f_{approx}(y)	&= \nabla f(x) +\frac{1}{2} \Big((\nabla^{2} f(x))^{T}(y-x)+(y-x)^{T}\nabla^{2}f(x)\Big)\\\\
>&=\nabla f(x) +\nabla^{2} f(x)(y-x)\\\\
>& = 0,\\\\
>\Leftrightarrow y &= x-(\nabla^{2}f(x))^{-1}\nabla f(x).
>\end{align}
>$$

## Bước cập nhật gradient descent
Trong gradient descent, chúng ta sử dụng các số hạng xấp xỉ Taylor bậc hai của hàm số $$f$$, nhưng đối với số hạng bậc hai, chúng ta giả sử nó là ma trận đơn vị chia cho $$t$$, thay vì kết quả đạo hàm bậc hai thực tế.

>$$
>\begin{align}
>f(y)	\approx f(x) + \nabla f(x)^{T}(y-x) +\frac{1}{2t}\|{y-x}\|_{2}^{2},\\\\
>f_{approx}(y)	= f(x) + \nabla f(x)^{T}(y-x) +\frac{1}{2t}\|{y-x}\|_{2}^{2}.\\\\
>\end{align}
>$$

Tương tự như phương pháp Newton, chúng ta có thể xác định giá trị $$y$$ mà tại đó gradient của xấp xỉ trên bằng không, tức là $$x^{+}$$.
>$$
>\begin{align}
>\nabla f(y) &= \nabla f(x) + \frac{1}{t}(y-x), \\\\
> &= 0,\\\\
>y &= x-t\nabla f(x).
>\end{align}
>$$

Kết quả này giống hệt với bước cập nhật của gradient descent.

Để biết thông tin chi tiết về gradient descent, hãy tham khảo [chương gradient descent]({% multilang_post_url contents/chapter06/21-03-20-06_00_gradient_descent %}).

## Ví dụ
Làm ví dụ, đối với hàm số $$f = (10x_{1}^{2}+x_{2}^{2})/2+5log(1+e^{-x_{1}-x_{2}})$$, chúng ta giả sử thực hiện các bước có độ dài gần bằng nhau. Tức là, chúng ta đặt kích thước bước trong gradient descent để khớp với độ lớn cập nhật của phương pháp Newton tại mỗi lần lặp, và so sánh hướng hội tụ của gradient descent (màu đen) và phương pháp Newton (màu xanh) theo các bước của chúng.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/gd.jpeg" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] So sánh giữa gradient descent (màu đen) và phương pháp Newton (màu xanh)[3]</figcaption>
</p>
</figure>

Như có thể thấy trong Hình 1, gradient descent giả sử số hạng đạo hàm bậc hai là một hằng số nhân với ma trận đơn vị khi tính toán gradient, do đó nó hội tụ vuông góc với hướng tiếp tuyến của các đường đồng mức, và cho thấy tốc độ hội tụ chậm hơn so với phương pháp Newton. Các chương còn lại sẽ đề cập đến các tính chất, đặc điểm, sự hội tụ, ví dụ, v.v. của phương pháp Newton.
