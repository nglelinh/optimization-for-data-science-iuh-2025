---
layout: post
title: 01-03 Mục tiêu và Chủ đề
chapter: '01'
order: 4
owner: Kyeongmin Woo
categories:
- chapter01
lang: vi
lesson_type: required
---

## Mục tiêu

Khóa học này hướng tới việc rèn luyện ba năng lực chính:

* Nhận biết khi nào một bài toán cho trước là bài toán tối ưu hóa lồi.
* Mô hình hóa một bài toán thực tế thành bài toán tối ưu hóa lồi.
* Lựa chọn thuật toán phù hợp nhất để giải một bài toán tối ưu hóa lồi cụ thể.

## Chủ đề

Để đạt được các mục tiêu trên, khóa học sẽ đi qua các nội dung:

* Tập lồi, hàm lồi và bài toán tối ưu hóa lồi.
* Các ví dụ và ứng dụng điển hình.
* Các lớp thuật toán tối ưu (gradient, proximal, Newton, điểm trong, ADMM, …).
* Lộ trình hiện đại 2026 trên trang này: SGD / Adam / AdamW (Chương 26), vi phân tự động (Chương 27), bề mặt hàm mục tiêu không lồi (Chương 28), SGD song song dữ liệu và FedAvg (Chương 29).

Trong đó, trọng tâm xuyên suốt của khóa học là thuật toán.

## Thuật toán

Có nhiều phương pháp khác nhau để giải cùng một bài toán tối ưu hóa, và hiệu quả của từng phương pháp phụ thuộc chặt chẽ vào cấu trúc của bài toán. Để chọn được thuật toán phù hợp nhất, cần hiểu rõ cả đặc điểm của bài toán lẫn cơ chế hoạt động của thuật toán. Ta minh họa điều này qua ví dụ khử nhiễu toàn biến phân (total variation denoising).

### Ví dụ: Khử nhiễu Total Variation

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/2d_fused_lasso.png" alt="2D Fused Lasso" width="70%">
  <figcaption style="text-align: center;">[Hình1] Khử nhiễu Total Variation [3]</figcaption>
</p>
</figure>

Giả sử bạn có một bức ảnh bị nhiễu (hình giữa) và muốn khử nhiễu để khôi phục ảnh (hình phải) gần với ảnh gốc (hình trái). Nếu ký hiệu giá trị từng điểm ảnh là $$y_i, i = 1, ..., n$$, ta có thể mô hình hóa yêu cầu này thành bài toán tối ưu hóa sau — thường gọi là bài toán **2D fused lasso** hay **khử nhiễu 2D total variation**:

>$$\min_{\theta} \frac{1}{2} \sum_{i=1}^n (y_i - \theta_{i})^2 + \lambda \sum_{(i,j) \in E} \vert \theta_i - \theta_j \vert$$

* $$E$$: tập hợp các cạnh nối giữa các điểm ảnh lân cận.
* $$\frac{1}{2} \sum_{i=1}^n (y_i - \theta_{i})^2$$: hàm mất mát bình phương tối thiểu, giữ cho ảnh khôi phục $$\theta$$ bám sát ảnh quan sát $$y$$.
* $$\sum_{(i,j) \in E} \vert \theta_i - \theta_j \vert$$: thành phần làm mịn toàn biến phân (total variation), phù hợp khi giá trị các điểm ảnh lân cận ít thay đổi (dạng hằng số từng khúc). Việc chọn thành phần điều chuẩn thích hợp đòi hỏi cân nhắc kỹ đặc thù của bài toán (xem thêm Chương 6.1.2 và 6.3 trong Tài liệu tham khảo 1).

Bài toán tối ưu hóa lồi trên có thể được giải bằng thuật toán [Specialized ADMM](http://stanford.edu/~boyd/admm.html), cho kết quả như hình bên phải chỉ sau 20 lần lặp.

### Specialized ADMM, 20 lần lặp
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/result1.png" alt="Result1" width="50%">
  <figcaption style="text-align: center;">[Hình2] Kết quả Specialized ADMM [3]</figcaption>
</p>
</figure>

### Proximal gradient descent, 1000 lần lặp
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/result2.png" alt="Result2" width="50%">
  <figcaption style="text-align: center;">[Hình3] Kết quả Proximal Gradient Descent [3]</figcaption>
</p>
</figure>

### Coordinate descent, 10.000 chu kỳ
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/result3.png" alt="Result3" width="50%">
  <figcaption style="text-align: center;">[Hình4] Kết quả Coordinate Descent [3]</figcaption>
</p>
</figure>

Như kết quả minh họa ở trên, với bài toán 2D fused lasso, Specialized ADMM vượt trội hơn hai phương pháp còn lại. Tuy nhiên, trên những bài toán khác, proximal gradient descent hoặc coordinate descent có thể lại hiệu quả hơn. Trong các chương tiếp theo, chúng ta sẽ phân tích sâu từng lớp thuật toán và lớp bài toán để biết cách lựa chọn phương pháp thích hợp nhất.
