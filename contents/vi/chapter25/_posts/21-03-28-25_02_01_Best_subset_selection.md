---
layout: post
title: '25-02-01 Chọn tập con tốt nhất (Best subset selection)'
chapter: '25'
order: 8
owner: YoungJae Choung
categories:
- chapter25
lang: vi
---

Chọn tập con tốt nhất là một bài toán tiêu biểu của quy hoạch nguyên hỗn hợp trong thống kê, nhằm lựa chọn tối đa $$k$$ đặc trưng quan trọng nhất trong số $$p$$ đặc trưng sẵn có.

## Phát biểu bài toán

Cho ma trận đặc trưng $$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n \times p}$$ và vector phản hồi $$y \in \mathbb{R}^{n}$$, bài toán chọn tập con tốt nhất có dạng:

> $$
> \begin{align}
> \min_{\beta} & \quad \frac{1}{2} \parallel y - X\beta \parallel^{2} \\\\
> \text{subject to } & \quad \parallel \beta \parallel_{0} \leq k
> \end{align}
> $$

trong đó $$\parallel \beta \parallel_{0}$$ là số phần tử khác không của $$\beta$$.

Ở các chương trước, bài toán Lasso tạo tính thưa một cách xấp xỉ thông qua chuẩn $$l_1$$. Ở đây, ràng buộc chuẩn giả $$l_0$$ ($$\parallel \beta \parallel_{0} \leq k$$) giới hạn trực tiếp số biến được chọn nhưng lại không lồi, nên không thể giải trực tiếp bằng các phương pháp tối ưu lồi thông thường.

### Mô hình quy hoạch nguyên hỗn hợp

Ta biểu diễn lại bài toán trên dưới dạng quy hoạch nguyên hỗn hợp:

> $$
> \begin{align}
> \min_{\beta, z} & \quad \frac{1}{2} \parallel y - X\beta \parallel^{2} \\\\
> \text{subject to } & \quad \left\vert \beta_{i} \right\vert \leq M_{i} \cdot z_{i}, \quad i = 1, \dotsc, p \\\\
> & \quad \sum_{i = 1}^{p} z_{i} \leq k \\\\
> & \quad z_{i} \in \lbrace 0, 1 \rbrace, \quad i = 1, \dotsc, p
> \end{align}
> $$

Các biến nhị phân $$z_i$$ kèm ràng buộc $$\sum_{i=1}^{p} z_i \leq k$$ đảm bảo tối đa $$k$$ hệ số $$\beta_i$$ khác không. Các hằng số $$M_i$$ là cận trên của $$\left\vert \beta_{i} \right\vert$$ tại nghiệm tối ưu và có thể ước lượng trước bằng cách tiền xử lý $$X$$ và $$y$$. Khi đã viết ở dạng này, ta có thể giải bài toán bằng các bộ giải quy hoạch nguyên hỗn hợp.

## Cách tạo điểm khởi động khả thi tốt

Để trình bày thuật toán tìm nghiệm khả thi ban đầu (warm start), ta xét bài toán tổng quát với hàm mục tiêu $$g : \mathbb{R}^{p} \to \mathbb{R}$$ lồi, trơn và có gradient $$\nabla g$$ liên tục $$L$$-Lipschitz:

> $$\min_{\beta} g(\beta) \quad \text{subject to} \quad \parallel \beta \parallel_{0} \le k$$

Với bài toán chọn tập con tốt nhất, $$g(\beta) = \frac{1}{2} \parallel X\beta - y \parallel^2_2$$.

### Nhận xét

Định nghĩa toán tử $$H_k(u)$$ giữ lại đúng $$k$$ phần tử có trị tuyệt đối lớn nhất của vector $$u \in \mathbb{R}^p$$ và gán các phần tử còn lại bằng 0:

> $$ H_k(u) = \underset{\beta : \parallel \beta \parallel_{0} \le k}{\text{argmin}} \parallel \beta - u \parallel^2_2 $$

Toán tử $$H_k(u)$$ chính là phép co ngưỡng cứng (hard thresholding), hay phép chiếu Euclid của $$u$$ lên tập $$\{\beta : \parallel \beta \parallel_{0} \le k\}$$.

### Thuật toán bậc nhất rời rạc (Discrete first-order algorithm)

Kết hợp bước hạ gradient với toán tử $$H_k$$:

1. Khởi tạo $$\beta^{(0)}$$.
2. Với $$i = 0, 1, \dots$$: <br>
$$\quad \beta^{(i+1)} = H_k \left(\beta^{(i)} - \frac{1}{L} \nabla g(\beta^{(i)})\right)$$ <br>
Kết thúc vòng lặp.

Quá trình lặp này hội tụ về một điểm $$\bar{\beta}$$ thỏa mãn điều kiện điểm bất động (tương ứng một nghiệm cục bộ tốt để làm điểm khởi động nóng cho MIP):

> $$ \bar{\beta} = H_k \left(\bar{\beta} - \frac{1}{L} \nabla g(\bar{\beta})\right) $$

Về cấu trúc, thuật toán này có dạng tương tự proximal gradient descent với $$H_k$$ đóng vai trò toán tử proximal trên tập ràng buộc $$l_0$$.

## Kết quả thực nghiệm

### Khoảng cách tối ưu trong quy hoạch nguyên hỗn hợp (MIP gap)

Hình 1 trình bày kết quả thực nghiệm cho bài toán chọn tập con tốt nhất.

Ở đồ thị bên trái, cận trên sớm đạt tới giá trị tối ưu nhưng cận dưới tăng chậm hơn; chỉ khi cận dưới gặp cận trên ta mới chứng nhận được nghiệm hiện tại là tối ưu toàn cục. Điều này phản ánh đặc thù của quy hoạch nguyên: không có điều kiện tối ưu đơn giản để kiểm tra trực tiếp mà phải dựa vào việc thu hẹp hiệu giữa cận trên và cận dưới (gọi là *MIP gap*).

Đồ thị bên phải minh họa quá trình MIP gap (đường màu cam) giảm dần theo thời gian.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_03_subset_results1.png" alt="[Hình 1] Tập dữ liệu n=350, p = 64, k=6 [3]">
  <figcaption style="text-align: center;">$$[Hình 1] \; Dữ \; liệu \; n=350, p = 64, k=6 \; [3]$$</figcaption>
</p>
</figure>
<br>

### Khởi động nguội và khởi động nóng (Cold và Warm Starts)

Hình 2 cho thấy việc dùng nghiệm từ thuật toán bậc nhất rời rạc làm điểm khởi động nóng (warm start) mang lại hiệu năng vượt trội so với khởi động nguội (cold start).

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_04_subset_results2.png" alt="[Hình 2] Cold start và Warm start [3]">
  <figcaption style="text-align: center;">[Hình 2] Cold start và Warm start [3]</figcaption>
</p>
</figure>
<br>

### Khả năng phát hiện tính thưa (Sparsity Detection)

Hình 3 so sánh độ thưa của nghiệm thu được giữa MIP, Lasso, hồi quy từng bước (Stepwise regression) và SparseNet trên dữ liệu tổng hợp; kết quả cho thấy MIP đạt độ thưa chính xác nhất.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_05_subset_results3.png" alt="[Hình 3] Phát hiện tính thưa (dữ liệu tổng hợp) [3]">
  <figcaption style="text-align: center;">[Hình 3] Phát hiện tính thưa (dữ liệu tổng hợp) [3]</figcaption>
</p>
</figure>
<br>
