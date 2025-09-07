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
Mục tiêu của khóa học này là phát triển các khả năng sau:

* Nhận biết khi nào một bài toán cho trước là bài toán tối ưu hóa lồi
* Xây dựng một tình huống cho trước thành bài toán tối ưu hóa lồi
* Lựa chọn thuật toán phù hợp nhất để giải một bài toán tối ưu hóa lồi đã định nghĩa

## Chủ đề
Để đạt được những mục tiêu này, các chủ đề sau sẽ được đề cập:

* Tập lồi, hàm số, bài toán tối ưu hóa
* Ví dụ và ứng dụng
* Thuật toán

Đặc biệt, trọng tâm chính sẽ là thuật toán.

## Thuật toán
Có nhiều phương pháp khác nhau để giải bài toán tối ưu hóa. Hiệu suất của mỗi phương pháp phụ thuộc vào tính chất của bài toán được giải. Để chọn thuật toán hiệu quả nhất, cần có hiểu biết sâu sắc về cả bài toán và thuật toán. Hãy xem một ví dụ: khử nhiễu total variation.

### Ví dụ: Khử nhiễu Total variation

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/2d_fused_lasso.png" alt="2D Fused Lasso" width="70%">
  <figcaption style="text-align: center;">[Hình1] Khử nhiễu Total Variation [3]</figcaption>
</p>
</figure>

Giả sử bạn nhận được một hình ảnh nhiễu (giữa), và bạn muốn loại bỏ nhiễu để có được nghiệm (phải) gần với hình ảnh thật (trái). Nếu mỗi giá trị pixel là $$y_i, i = 1, ..., n$$, bài toán này có thể được xây dựng thành bài toán tối ưu hóa sau, thường được gọi là bài toán 2D fused lasso hoặc khử nhiễu 2D total variation:

>$$\min_{\theta} \frac{1}{2} \sum_{i=1}^n (y_i - \theta_{i})^2 + \lambda \sum_{(i,j) \in E} \vert \theta_i - \theta_j \vert$$

* E: tập hợp các cạnh giữa tất cả các $$\theta$$ lân cận
* $$\frac{1}{2} \sum_{i=1}^n (y_i - \theta_{i})^2$$: Mất mát bình phương tối thiểu. Buộc $$\theta$$ gần với $$y$$
* $$\sum_{(i,j) \in E} \vert \theta_i - \theta_j \vert$$: Làm mịn total variation. Được sử dụng khi sự thay đổi giữa các pixel lân cận không lớn (từng phần hằng số). Việc chọn phương pháp làm mịn phù hợp đòi hỏi xem xét cẩn thận đặc điểm của bài toán. (Để biết thêm chi tiết về làm mịn total variation, xem Chương 6.1.2 và 6.3 trong Tài liệu tham khảo 1.)

Bài toán tối ưu hóa lồi ở trên có thể được giải bằng thuật toán [Specialized ADMM](http://stanford.edu/~boyd/admm.html), mang lại nghiệm bên phải sau 20 lần lặp.

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

### Coordinate descent, 10K chu kỳ
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/result3.png" alt="Result3" width="50%">
  <figcaption style="text-align: center;">[Hình4] Kết quả Coordinate Descent [3]</figcaption>
</p>
</figure>

Như được chỉ ra ở trên, đối với bài toán 2D fused lasso, Specialized ADMM hoạt động tốt nhất trong ba phương pháp. Tuy nhiên, đối với các bài toán khác, hai phương pháp còn lại có thể vượt trội hơn Specialized ADMM. Trong các chương sau, chúng ta sẽ phân tích các thuật toán và bài toán khác nhau để học cách lựa chọn thuật toán phù hợp nhất.
