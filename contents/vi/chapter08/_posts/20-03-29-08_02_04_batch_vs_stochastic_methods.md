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

Tính chất hội tụ của phương pháp batch và ngẫu nhiên như sau:

Nói chung, phương pháp ngẫu nhiên tiếp cận điểm tối ưu nhanh chóng trong giai đoạn đầu, nhưng có thể không hội tụ tốt gần điểm tối ưu. Ngược lại, phương pháp batch hội tụ chậm hơn nhưng tiếp cận điểm tối ưu chính xác hơn.

Hình dưới đây so sánh sự hội tụ của phương pháp batch và ngẫu nhiên cho [hồi quy logistic](https://en.wikipedia.org/wiki/Logistic_regression) (không có regularization):

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter08/08_02_stochastic_vs_batch.png" alt="stochastic_vs_batch" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">[Fig 3] So sánh Batch vs Stochastic Gradient Descent [2]</figcaption>
</figure>
