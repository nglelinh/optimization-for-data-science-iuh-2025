---
layout: post
title: 14-02-02 Tính bất biến affine của phương pháp Newton
chapter: '14'
order: 7
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

Một tính chất quan trọng của phương pháp Newton là tính bất biến affine: hướng cập nhật không phụ thuộc vào các phép biến đổi affine của hệ tọa độ. Ngược lại, gradient descent không có tính chất này nên tốc độ hội tụ thay đổi tùy theo hệ tọa độ được chọn.

Trang này chứng minh tính chất bất biến affine của phương pháp Newton.

## Chứng minh tính bất biến affine
Cho $$f:\mathbb{R}^{n}\rightarrow \mathbb{R}$$ khả vi hai lần và ma trận không suy biến $$A\in \mathbb{R}^{n\times n}$$. Định nghĩa hàm $$g(y) := f(Ay)$$, tức là hàm $$g$$ tại $$y$$ có cùng giá trị với hàm $$f$$ tại điểm biến đổi affine $$Ay$$. Để tránh nhầm lẫn về ký hiệu và đối số của gradient, ta đặt $$x := Ay$$.

Áp dụng quy tắc chuỗi để lấy đạo hàm bậc nhất và bậc hai của $$g$$, ta thu được:

>$$
>\begin{align}
>\nabla g(y) &= A^{T} \nabla f(x)\\\\
>\nabla^{2} g(y) &= A^{T}\nabla^{2}f(x)A,
>\end{align}
>$$

Bước Newton của $$g$$ theo biến $$y$$ là:

>$$
>\begin{align}
>y^{+}  = y-(\nabla^{2}g(y))^{-1}\nabla g(y).
>\end{align}
>$$

Biểu diễn bước cập nhật này theo $$f$$ và $$x$$, ta suy ra bước Newton cho $$f$$ tại $$x$$:

>$$
>\begin{align}
>y^{+} &= y-(A^{T}\nabla^{2}f(x)A)^{-1}A^{T} \nabla f(x)\\\\
>\Leftrightarrow y^{+} &= y-A^{-1}(\nabla^{2}f(x))^{-1}(A^{T})^{-1}A^{T} \nabla f(x)\\\\
>\Leftrightarrow Ay^{+} &= Ay-(\nabla^{2}f(x))^{-1}\nabla f(x)\\\\
>\Leftrightarrow x^{+} &= x - \nabla^{2}f(x)^{-1}\nabla f(x).
>\end{align}
>$$

Kết quả này cho thấy bước Newton bất biến affine: các bước cập nhật trong hệ tọa độ đã biến đổi bởi ma trận không suy biến $$A$$ hoàn toàn tương đương với các bước cập nhật trong hệ tọa độ gốc.

Thực hiện kiểm tra tương tự cho gradient descent, ta thu được:

>$$
>\begin{align}
>y^{+} &= y-t_{k}\cdot \nabla g(y)\\\\
>\Leftrightarrow y^{+} &= y-t_{k}\cdot A^{T}\nabla f(x)\\\\
>\Leftrightarrow x^{+} &= x - t_{k}\cdot AA^{T}\nabla f(x). 
>\end{align}
>$$

Với gradient descent, do ma trận Hessian được xấp xỉ bởi $$\frac{1}{t}I$$, hướng cập nhật bị thay đổi khi áp dụng phép biến đổi affine lên hệ tọa độ (trừ trường hợp đặc biệt $$AA^T$$ tỉ lệ với ma trận đơn vị).