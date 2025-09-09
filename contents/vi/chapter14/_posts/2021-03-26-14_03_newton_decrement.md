---
layout: post
title: 14-03 Newton decrement
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

Trong chương này, chúng ta định nghĩa Newton decrement và xem xét ý nghĩa của nó.

Đối với bài toán tối ưu hóa dưới đây, Newton decrement tại $$x$$ được định nghĩa là $$\lambda(x)$$:

>\begin{align}
>\min_{x} \quad f(x),\\\\
>\end{align}
>\begin{align}
>\lambda(x) = (\nabla f(x)^{T}(\nabla^{2}f(x))^{-1}\nabla f(x))^{1/2}.
>\end{align}

## Đặc điểm của Newton decrement
Thứ nhất, Newton decrement liên quan đến sự khác biệt giữa hàm $$f(x)$$ và giá trị tối thiểu của xấp xỉ bậc hai của nó. Tính toán sự khác biệt này cho:
>$$\begin{align}
>f(x)-&\min_{y} \big( f(x)+\nabla f(x)^{T}(y-x)+\frac{1}{2}(y-x)^{T}\nabla^{2}f(x)(y-x)\big),\\\\
>f(x)-&\bigg( f(x) + \nabla^{T}f(x)\big( -(\nabla^{2} f(x) )^{-1} \nabla f(x)\big) + \frac{1}{2}\big( -(\nabla^{2}f(x))^{-1} \nabla f(x) \big)^{T} \nabla ^{2}f(x) \big( -(\nabla^{2}f(x))^{-1}\nabla f(x) \big) \bigg) \\\\ 
>&= \frac{1}{2}\nabla f(x)^{T}(\nabla^{2} f(x) )^{-1}\nabla f(x) = \frac{1}{2}\lambda(x)^{2}.
>\end{align}$$

Do đó, $$\frac{1}{2}\lambda^{2}(x)$$ có thể được coi là một cận xấp xỉ cho khoảng cách tối ưu $$f(x)-f^{\star}$$.

Thứ hai, hướng Newton trong phương pháp Newton cho mỗi lần lặp là $$v = -(\nabla^{2}f(x))^{-1}\nabla f(x)$$, và Newton decrement là độ dài của bước Newton trong chuẩn được định nghĩa bởi Hessian $$\nabla^{2}f(x)$$.

Ngoài ra, điều này có thể được xem là một loại khoảng cách Mahalanobis [[Wikipedia](https://en.wikipedia.org/wiki/Mahalanobis_distance)], trong đó bước mới $$y$$ là quan sát, vị trí hiện tại $$x$$ là giá trị trung bình, và Hessian của $$f(x)$$ là hiệp phương sai. Khoảng cách Mahalanobis đo khoảng cách từ một điểm đến giá trị trung bình theo hướng của hiệp phương sai của phân phối.

Nếu chúng ta xem xét định nghĩa khoảng cách Mahalanobis là khoảng cách giữa một điểm và giá trị trung bình của một phân phối chia cho độ lệch chuẩn theo hướng đó, Newton decrement biểu diễn khoảng cách của bước mới từ vị trí hiện tại, với Hessian đóng vai trò là hiệp phương sai của phân phối.

Thứ ba, Newton decrement có thể được biểu diễn theo số gia và Hessian. Bắt đầu từ cập nhật bước trong phương pháp Newton, chúng ta có:
>\begin{align}
>x^{+} &= x-\big(\nabla^{2} f(x) \big)^{-1} \nabla f(x) &\\ 
>\end{align}
>\begin{align}
>\Delta x_{nt} &= -\big(\nabla^{2} f(x) \big)^{-1} \nabla f(x) &\\
>\end{align}
>\begin{align}
>\nabla f(x)^{T} \Delta x_{nt} &= -\lambda (x)^{2}
>\end{align}

Sử dụng các mối quan hệ này, Newton decrement cũng có thể được biểu diễn là:
>\begin{align}
>\lambda(x) = (\Delta x_{nt}^{T}\nabla^{2} f(x) \Delta x_{nt})^{1/2}.
>\end{align}


Cuối cùng, giống như bước Newton, Newton decrement cũng bất biến affine. Nói cách khác, đối với bất kỳ ma trận không suy biến nào, nếu hàm $$g(y) = f(Ay)$$ được định nghĩa, thì tại $$x = Ay$$, ta có $$\lambda_{g(y)} = \lambda_{f(x)}$$.