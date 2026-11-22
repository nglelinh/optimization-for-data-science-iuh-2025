---
layout: post
title: '08-02-04 So sánh Phương pháp Batch và Ngẫu nhiên'
chapter: '08'
order: 15
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Đặc điểm hội tụ của phương pháp batch và phương pháp ngẫu nhiên có thể tóm tắt như sau:

Nhìn chung, phương pháp ngẫu nhiên tiến nhanh về vùng lân cận nghiệm tối ưu trong giai đoạn đầu, nhưng thường dao động và khó hội tụ chính xác khi đã đến gần nghiệm tối ưu. Ngược lại, phương pháp batch tiến chậm hơn ở giai đoạn đầu nhưng hội tụ ổn định và chính xác hơn về điểm tối ưu.

Hình dưới đây so sánh quá trình hội tụ của hai phương pháp trên bài toán [hồi quy logistic](https://en.wikipedia.org/wiki/Logistic_regression) không có chính quy hóa:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter08/08_02_stochastic_vs_batch.png" alt="stochastic_vs_batch" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">[Fig 3] So sánh Batch vs Stochastic Gradient Descent [2]</figcaption>
</figure>

Khi mỗi hàm thành phần $$f_i$$ đều trơn, phần dao động còn lại của đường ngẫu nhiên quanh điểm tối ưu chính là sàn nhiễu mà các phương pháp giảm phương sai trong [26-05 SVRG và SAGA]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %}) loại bỏ — mà không cần tính lại toàn bộ gradient batch ở mỗi bước.
