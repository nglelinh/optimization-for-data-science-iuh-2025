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

Trong mục này, ta so sánh tổng quát giữa phương pháp Newton và gradient descent trên miền xác định có số chiều $$n$$.

| Tiêu chí | Phương pháp Newton | Gradient descent |
| -------- | -------- | -------- |
| Bộ nhớ | $$O(n^{2})$$ (lưu trữ ma trận Hessian cỡ $$n \times n$$) | $$O(n)$$ (lưu trữ vector gradient $$n$$ chiều) |
| Chi phí tính toán mỗi bước | $$O(n^{3})$$ phép tính (giải hệ tuyến tính cỡ $$n \times n$$) | $$O(n)$$ phép tính (cộng vector $$n$$ chiều) |
| Tìm kiếm đường backtracking | $$O(n)$$ | $$O(n)$$ |
| Độ nhạy với số điều kiện (conditioning) | Bất biến affine, không phụ thuộc số điều kiện của hệ tọa độ | Chịu ảnh hưởng mạnh bởi số điều kiện |
| Độ ổn định triển khai | Nhạy cảm hơn với lỗi cài đặt và sai số số học | Ổn định hơn phương pháp Newton |

## Ví dụ

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/gd(1).jpeg" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Hồi quy logistic [3]</figcaption>
</p>
</figure>

Hình 1 biểu diễn lại ví dụ hồi quy logistic ở mục [14-04]({% multilang_post_url contents/chapter14/2021-03-26-14_04_backtracking_line_search %}) nhưng với trục hoành là thời gian tính toán thực tế. Theo phân tích lý thuyết, phương pháp Newton gồm hai giai đoạn: ở giai đoạn giảm chấn ban đầu, mức giảm sai số theo từng bước tương đương gradient descent nhưng chi phí mỗi bước là $$O(n^{3})$$ nên thời gian chạy thực tế có thể chậm hơn; khi bước vào giai đoạn thuần túy (backtracking không còn cần thu nhỏ bước), phương pháp đạt hội tụ bậc hai và giảm sai số rất nhanh.

### Tự tay thử: Newton so với gradient descent

<div class="opx-explainer" data-opx="newton" data-lang="vi"></div>
