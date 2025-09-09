---
layout: post
title: 14-02-02 Tính bất biến affine của phương pháp Newton
chapter: '14'
order: 6
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

Một trong những tính chất quan trọng của phương pháp Newton là nó bất biến affine. Điều này có nghĩa là hướng của việc cập nhật không phụ thuộc vào các phép biến đổi affine của hệ tọa độ. Ví dụ, gradient descent biến thiên theo các phép biến đổi affine, do đó tốc độ hội tụ khác nhau tùy thuộc vào không gian tọa độ.

Trang này dẫn xuất tính chất bất biến affine.

## Tính bất biến affine : chứng minh
Cho $$f:\mathbb{R}^{n}\rightarrow \mathbb{R}$$ khả vi hai lần, và cho $$A\in \mathbb{R}^{n\times n}$$ không suy biến. Cũng định nghĩa $$g(y)$$ là $$f(Ay)$$. $$g(y):=f(Ay)$$. Điều này có nghĩa là một hàm $$g$$ nào đó nhận $$y$$ làm đầu vào có cùng đầu ra như hàm $$f$$ nhận $$Ay$$ (biến đổi affine bởi $$A$$ đối với $$y$$) làm đầu vào. Để giảm thiểu sự nhầm lẫn về ký hiệu và đối số gradient, chúng ta định nghĩa $$x:=Ay$$.

Sử dụng quy tắc chuỗi để lấy đạo hàm cả hai vế một lần và hai lần, chúng ta nhận được các kết quả sau:

>$$
>\begin{align}
>\nabla g(y) &= A^{T} \nabla f(x)\\\\
>\nabla^{2} g(y) &= A^{T}\nabla^{2}f(x)A,
>\end{align}
>$$

Bước Newton của $$g$$ đối với $$y$$ như sau:

>$$
>\begin{align}
>y^{+}  = y-(\nabla^{2}g(y))^{-1}\nabla g(y).
>\end{align}
>$$

Ở đây, thay vì hàm $$g$$, nếu chúng ta biến đổi và sắp xếp nó theo hàm $$f$$ đối với $$x$$, chúng ta có thể dẫn xuất bước Newton cho $$x$$ và $$f$$.

>$$
>\begin{align}
>y^{+} &= y-(A^{T}\nabla^{2}f(x)A)^{-1}A^{T} \nabla f(x)\\\\
>\Leftrightarrow y^{+} &= y-A^{-1}(\nabla^{2}f(x))^{-1}(A^{T})^{-1}A^{T} \nabla f(x)\\\\
>\Leftrightarrow Ay^{+} &= Ay-(\nabla^{2}f(x))^{-1}\nabla f(x)\\\\
>\Leftrightarrow x^{+} &= x - \nabla^{2}f(x)^{-1}\nabla f(x).
>\end{align}
>$$

Điều này có nghĩa là bước Newton là bất biến affine, tức là, các cập nhật trong các hệ tọa độ được biến đổi bởi các phép biến đổi affine được biểu diễn bởi các ma trận không suy biến là giống hệt nhau.

Sử dụng cùng phương pháp để kiểm tra tính bất biến affine của gradient descent bằng cách dẫn xuất cập nhật bước, chúng ta có thể thu được kết quả sau:

>$$
>\begin{align}
>y^{+} &= y-t_{k}\cdot \nabla g(y)\\\\
>\Leftrightarrow y^{+} &= y-t_{k}\cdot \nabla f(x)A^{T}\\\\
>\Leftrightarrow x^{+} &= x - t_{k}\cdot A\nabla f(x)A^{T}. 
>\end{align}
>$$

Trong trường hợp của gradient descent, vì ma trận Hessian được xấp xỉ là $$\frac{1}{t}I$$ cho các cập nhật, chúng ta có thể thấy rằng hướng của cập nhật thay đổi đối với các tọa độ được biến đổi affine.