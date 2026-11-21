---
layout: post
title: 14-07 So sánh với phương pháp bậc nhất
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

Trong bài này, chúng ta so sánh phương pháp Newton và gradient descent từ góc nhìn tổng quát. Giả sử chiều của miền là $$n$$.

| Tiêu chí | Phương pháp Newton | Gradient descent |
| -------- | -------- | -------- |
| Bộ nhớ     | $$O(n^{2})$$ (lưu trữ ma trận Hessian cỡ $$n \times n$$)     | $$O(n)$$ (lưu trữ gradient $$n$$ chiều) |
| Tính toán     | $$O(n^{3})$$ flops (giải hệ tuyến tính cỡ $$n \times n$$)     | $$O(n)$$ flops (cộng vector $$n$$ chiều)     |
| Backtracking     | $$O(n)$$ | $$O(n)$$  |
| Điều kiện (conditioning)     | Bất biến affine, ít bị ảnh hưởng bởi conditioning  | Có thể bị ảnh hưởng mạnh bởi conditioning |
| Độ mong manh     | Nhạy cảm với lỗi lập trình hoặc sai số số học | Bền vững hơn phương pháp Newton |

## Ví dụ

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/gd(1).jpeg" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Hồi quy logistic [3]</figcaption>
</p>
</figure>

Hình 1 ở trên là ví dụ hồi quy logistic đã được thảo luận trong [14-04]({% multilang_post_url contents/chapter14/2021-03-26-14_04_backtracking_line_search %}). Nếu vẽ trục hoành theo thời gian tính toán thực tế, ta thấy kết quả như trên. Trong phân tích hội tụ, phương pháp Newton có hai giai đoạn. Trên thực tế, sau một khoảng thời gian nhất định, ta có thể quan sát sự hội tụ nhanh (hội tụ bậc hai). Ở giai đoạn đầu (giai đoạn có giảm bước) của phương pháp Newton, tốc độ hội tụ tương tự gradient descent. Tuy nhiên, vì cần $$O(n^{3})$$ phép tính, thời gian tính toán thực tế có thể chậm hơn. Sau khi backtracking line search không còn cần thiết, ta quan sát được hội tụ bậc hai và tiến triển rất nhanh.

### Tự tay thử: Newton so với gradient descent

<div class="opx-explainer" data-opx="newton" data-lang="vi"></div>
