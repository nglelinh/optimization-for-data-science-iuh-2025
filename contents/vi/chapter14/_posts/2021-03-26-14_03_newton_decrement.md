---
layout: post
title: 14-03 Newton decrement
chapter: '14'
order: 9
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

Trong mục này, chúng ta định nghĩa đại lượng giảm Newton (Newton decrement) và phân tích ý nghĩa của nó.

Đối với bài toán tối ưu hóa dưới đây, Newton decrement tại $$x$$ được ký hiệu và định nghĩa là $$\lambda(x)$$:

>\begin{align}
>\min_{x} \quad f(x),\\\\
>\end{align}
>\begin{align}
>\lambda(x) = (\nabla f(x)^{T}(\nabla^{2}f(x))^{-1}\nabla f(x))^{1/2}.
>\end{align}

## Đặc điểm của Newton decrement
Thứ nhất, Newton decrement liên hệ trực tiếp với hiệu giữa giá trị hàm $$f(x)$$ và giá trị nhỏ nhất của xấp xỉ bậc hai của $$f$$ tại $$x$$:
>$$
>\begin{align}
>f(x)-&\min_{y} \big( f(x)+\nabla f(x)^{T}(y-x)+\frac{1}{2}(y-x)^{T}\nabla^{2}f(x)(y-x)\big),\\\\
>f(x)-&\bigg( f(x) + \nabla^{T}f(x)\big( -(\nabla^{2} f(x) )^{-1} \nabla f(x)\big) + \frac{1}{2}\big( -(\nabla^{2}f(x))^{-1} \nabla f(x) \big)^{T} \nabla ^{2}f(x) \big( -(\nabla^{2}f(x))^{-1}\nabla f(x) \big) \bigg) \\\\ 
>&= \frac{1}{2}\nabla f(x)^{T}(\nabla^{2} f(x) )^{-1}\nabla f(x) = \frac{1}{2}\lambda(x)^{2}.
>\end{align}
>$$

Do đó, $$\frac{1}{2}\lambda^{2}(x)$$ có thể được dùng làm ước lượng cho khoảng cách tối ưu $$f(x)-f^{\star}$$.

Thứ hai, với hướng Newton ở mỗi vòng lặp là $$v = -(\nabla^{2}f(x))^{-1}\nabla f(x)$$, Newton decrement chính là độ dài của bước Newton theo chuẩn cảm sinh bởi ma trận Hessian $$\nabla^{2}f(x)$$.

Đại lượng này cũng có thể hiểu như một dạng khoảng cách Mahalanobis [[Wikipedia](https://en.wikipedia.org/wiki/Mahalanobis_distance)], trong đó điểm mới $$y$$ đóng vai trò quan sát, điểm hiện tại $$x$$ là giá trị trung bình, còn ma trận Hessian tại $$x$$ đóng vai trò nghịch đảo của ma trận hiệp phương sai. Khoảng cách Mahalanobis đo khoảng cách từ một điểm đến giá trị trung bình sau khi chuẩn hóa theo độ lệch chuẩn trên hướng tương ứng; tương tự, Newton decrement đo độ lớn của bước Newton tính từ điểm hiện tại trong hệ đo xác định bởi Hessian.

Thứ ba, Newton decrement có thể biểu diễn qua bước cập nhật Newton $$\Delta x_{nt}$$ và ma trận Hessian. Từ công thức cập nhật của phương pháp Newton:
>\begin{align}
>x^{+} &= x-\big(\nabla^{2} f(x) \big)^{-1} \nabla f(x) &\\ 
>\end{align}
>\begin{align}
>\Delta x_{nt} &= -\big(\nabla^{2} f(x) \big)^{-1} \nabla f(x) &\\
>\end{align}
>\begin{align}
>\nabla f(x)^{T} \Delta x_{nt} &= -\lambda (x)^{2}
>\end{align}

Từ các hệ thức trên, ta viết lại Newton decrement dưới dạng:
>\begin{align}
>\lambda(x) = (\Delta x_{nt}^{T}\nabla^{2} f(x) \Delta x_{nt})^{1/2}.
>\end{align}

Cuối cùng, tương tự bước Newton, Newton decrement cũng bất biến affine. Cụ thể, với mọi ma trận không suy biến $$A$$, nếu đặt $$g(y) = f(Ay)$$ thì tại $$x = Ay$$ ta có $$\lambda_{g(y)} = \lambda_{f(x)}$$.

### Newton decrement trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/newton-decrement_vi.mp4"></video>
</div>

½λ² là mức hạ của mô hình bậc hai, so với f − f* trên eˣ − 2x và trên hàm log-sum-exp, rồi so sánh tiêu chuẩn dừng λ với ‖∇f‖ khi đổi biến.
