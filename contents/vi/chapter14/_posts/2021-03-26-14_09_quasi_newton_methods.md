---
layout: post
title: 14-09 Các phương pháp Quasi-Newton
chapter: '14'
order: 17
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

Khi chi phí tính ma trận Hessian quá lớn hoặc ma trận Hessian bị suy biến, ta có thể dùng các phương pháp tựa Newton (quasi-Newton) để thay $$\nabla^{2}f(x)$$ bằng một ma trận xấp xỉ xác định dương $$H \succ 0$$:

>\begin{align}
>x^{+} = x - tH^{-1}\nabla f(x)
>\end{align}

Một số đặc điểm chính của các phương pháp quasi-Newton (xem chi tiết tại [Chương 18]({% multilang_post_url contents/chapter18/21-03-23-18_00_Quasi_Newton_methods %})):

* Ma trận xấp xỉ Hessian $$H$$ (hoặc nghịch đảo $$H^{-1}$$) được cập nhật sau mỗi bước với mục tiêu tính $$H^{-1}\nabla f(x)$$ với chi phí thấp.
* Tốc độ hội tụ là siêu tuyến tính, chậm hơn tốc độ bậc hai của phương pháp Newton đầy đủ; thông thường, khoảng $$n$$ bước quasi-Newton mang lại mức tiến triển tương đương một bước Newton.
* Nhiều phương pháp quasi-Newton cập nhật $$H$$ ở mỗi vòng lặp bằng các công thức cập nhật bậc thấp dựa trên thông tin gradient thu được từ các bước trước.
