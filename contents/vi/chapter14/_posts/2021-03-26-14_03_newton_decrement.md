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

Khi chạy Gradient Descent, ta thường kiểm tra độ lớn gradient $$\|\nabla f(x)\|_2 \le \epsilon$$ để biết mình đã gần đáy hay chưa. Nhưng trong thế giới của phương pháp Newton, chuẩn Euclid $$\|\nabla f(x)\|_2$$ lại có một nhược điểm chí mạng: **nó không bất biến affine!** Chỉ cần đổi đơn vị đo của một biến, $$\|\nabla f(x)\|_2$$ có thể phình to gấp 1.000 lần dù bạn đang đứng ngay sát nghiệm tối ưu.

Để giải quyết triệt để vấn đề này, các nhà toán học đã sáng chế ra một thước đo tự nhiên riêng cho phương pháp Newton: **đại lượng giảm Newton (Newton decrement)** $$\lambda(x) = \sqrt{\nabla f(x)^T (\nabla^2 f(x))^{-1} \nabla f(x)}$$. Không chỉ hoàn toàn bất biến affine, $$\frac{1}{2}\lambda(x)^2$$ còn cho bạn biết ngay **khoảng cách dự kiến từ vị trí hiện tại tới đáy của parabol xấp xỉ**, trở thành tiêu chí dừng tiêu chuẩn vàng cho mọi bộ giải Newton và phương pháp điểm trong.

## Bản đồ kiến thức nền: Bốn ý nghĩa đồng thời của Newton Decrement $$\lambda(x)$$

- **Ước lượng khoảng cách tới giá trị tối ưu:** Nếu thay $$f$$ bằng xấp xỉ Taylor bậc hai $$\tilde{f}_x$$, mức giảm cực đại có thể đạt được chính xác bằng:
  $$f(x) - \min_y \tilde{f}_x(y) = \frac{1}{2}\lambda(x)^2.$$
  Vì vậy, tiêu chí dừng $$\frac{1}{2}\lambda(x)^2 \le \epsilon$$ có ý nghĩa trực tiếp là "còn cách đáy xấp xỉ không quá $$\epsilon$$".
- **Độ dài bước Newton theo chuẩn Hessian:** Với bước Newton $$v = -(\nabla^2 f(x))^{-1}\nabla f(x)$$, ta có $$\lambda(x) = \sqrt{v^T \nabla^2 f(x) v} = \|v\|_{\nabla^2 f(x)}$$ — chuẩn tự nhiên gắn với độ cong tại $$x$$.
- **Đạo hàm theo hướng Newton:** Đạo hàm của $$f$$ dọc theo hướng bước Newton $$v$$ bằng đúng $$-\lambda(x)^2$$: $$\nabla f(x)^T v = -\lambda(x)^2 < 0$$. Đại lượng này dùng trực tiếp trong điều kiện dừng của tìm kiếm đường backtracking!
- **Tính bất biến affine tuyệt đối:** Dưới mọi phép đổi tọa độ khả nghịch $$x = Ay$$, giá trị $$\lambda(x)$$ giữ nguyên không đổi, biến nó thành tiêu chí dừng đáng tin cậy bất kể bài toán có bị kéo giãn trục mạnh đến đâu.

### Khung giải thích (nên đọc chậm): Tính tay $$\lambda(x)$$ và kiểm chứng ước lượng mức giảm $$\frac{1}{2}\lambda(x)^2$$

Xét hàm bậc hai 2 chiều $$f(x_1, x_2) = 2x_1^2 + 8x_2^2 - 4x_1 - 16x_2 + 12$$ tại điểm $$x = (2, 2)^T$$.

1. **Tính giá trị hàm, gradient và Hessian tại $$x = (2, 2)^T$$:**
   - $$f(2, 2) = 2(4) + 8(4) - 8 - 32 + 12 = 12$$.
   - $$\nabla f(x) = \begin{bmatrix} 4x_1 - 4 \\ 16x_2 - 16 \end{bmatrix} \implies \nabla f(2, 2) = \begin{bmatrix} 4 \\ 16 \end{bmatrix}$$.
   - $$\nabla^2 f(x) = \begin{bmatrix} 4 & 0 \\ 0 & 16 \end{bmatrix} \implies (\nabla^2 f)^{-1} = \begin{bmatrix} 1/4 & 0 \\ 0 & 1/16 \end{bmatrix}$$.
2. **Tính bước Newton $$v$$ và Newton decrement $$\lambda(x)$$:**
   - $$v = -(\nabla^2 f)^{-1}\nabla f = \begin{bmatrix} -1 \\ -1 \end{bmatrix}$$.
   - $$\lambda(x)^2 = \nabla f^T (\nabla^2 f)^{-1} \nabla f = 4\left(\frac{1}{4}\right)4 + 16\left(\frac{1}{16}\right)16 = 4 + 16 = 20 \implies \lambda(x) = \sqrt{20} \approx 4.472$$.
3. **Kiểm chứng đồng thời hai hệ thức vàng:**
   - Đạo hàm theo hướng $$v$$: $$\nabla f^T v = 4(-1) + 16(-1) = -20 = -\lambda(x)^2$$.
   - Mức giảm tới đáy thật $$x^\star = (1, 1)^T$$: ta có $$f(1, 1) = 2 + 8 - 4 - 16 + 12 = 2$$, nên $$f(2, 2) - f(1, 1) = 12 - 2 = 10$$. Đối chiếu với $$\frac{1}{2}\lambda(x)^2 = \frac{1}{2}(20) = 10$$ — **chính xác tuyệt đối!** (Với hàm phi tuyến tổng quát, $$\frac{1}{2}\lambda(x)^2$$ là xấp xỉ cực sát của $$f(x) - f^\star$$ khi gần nghiệm).

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
>f(x)-&\bigg( f(x) + \nabla f(x)^{T}\big( -(\nabla^{2} f(x) )^{-1} \nabla f(x)\big) + \frac{1}{2}\big( -(\nabla^{2}f(x))^{-1} \nabla f(x) \big)^{T} \nabla ^{2}f(x) \big( -(\nabla^{2}f(x))^{-1}\nabla f(x) \big) \bigg) \\\\ 
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
