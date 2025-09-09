---
layout: post
title: 14-09 Các phương pháp Quasi-Newton
chapter: '14'
order: 15
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

Nếu việc tính toán Hessian quá đắt hoặc Hessian là suy biến, chúng ta sử dụng các phương pháp quasi-Newton để xấp xỉ ma trận Hessian, tức là, $$\nabla^{2}f(x)$$ được thay thế bởi $$H>0$$, và chúng ta sử dụng $$H$$ cho cập nhật:

>\begin{align}
>x^{+} = x - tH^{-1}\nabla f(x)
>\end{align}

Một số đặc điểm của các phương pháp quasi-Newton như sau. Để biết thêm chi tiết, xem [Chương 18]({% multilang_post_url contents/chapter18/21-03-23-18_00_Quasi_Newton_methods %}).

* Hessian xấp xỉ $$H$$ được cập nhật ở mỗi bước. Mục tiêu là sử dụng tính toán tương đối rẻ cho $$H^{-1}$$.
* Tốc độ hội tụ là siêu tuyến tính, nhưng không nhanh bằng phương pháp Newton. Thông thường, $$n$$ bước của quasi-Newton tương đương với một bước của Newton về tiến bộ.
* Nhiều phương pháp quasi-Newton cập nhật $$H$$ ở mỗi lần lặp sử dụng các kỹ thuật truyền.
