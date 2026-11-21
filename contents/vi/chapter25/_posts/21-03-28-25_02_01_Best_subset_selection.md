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

Chọn tập con tốt nhất, một trong những ví dụ tiêu biểu của quy hoạch nguyên, là bài toán chọn $$k$$ phần tử trong $$p$$ phần tử.

## Chọn tập con tốt nhất
Khi $$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n×p}$$ và $$y \in \mathbb{R}^{n}$$, bài toán chọn tập con tốt nhất như sau:

> $$
> \begin{align}
> \min_{\beta} & \quad \frac{1}{2} \parallel y - X\beta \parallel^{2} \\\\
> \text{subject to } & \quad \parallel \beta \parallel_{0}  \  \leq  k
> \end{align}
> $$

Ở đây, $$\parallel \beta \parallel_{0}$$ là số phần tử khác không của $$\beta$$.

Ở các chương trước, ta đã định nghĩa loại bài toán này là bài toán Lasso và làm cho $$\beta$$ thưa bằng chuẩn $$l_1$$. Trong bài toán này, nó được định nghĩa là bài toán ràng buộc số phần tử khác không bằng chuẩn $$l_0$$, nhưng vì điều kiện ràng buộc $$\parallel \beta \parallel_{0}  \  \leq  k$$ không lồi nên bài toán không thể giải bằng các kỹ thuật tối ưu lồi đã học cho đến nay.

### Công thức quy hoạch nguyên
Vậy hãy viết lại bài toán này bằng quy hoạch nguyên.

> $$
> \begin{align}
> \min_{\beta, z} & \quad \frac{1}{2} \parallel y - X\beta \parallel^{2} \\\\
> \text{subject to } & \quad \left\vert  \beta_{i} \right\vert  \leq M_{i} \cdot z_{i} \quad i = 1 \dotsc p \\\\
> & \quad \sum_{i = 1}^{p} z_{i} \leq k \\\\
> & \quad z_{i} \in \lbrace 0, 1 \rbrace \quad i = 1 \dotsc p
> \end{align}
> $$

Bằng cách đưa vào biến nhị phân $$z_i$$ và làm cho tổng các $$z_i$$ nhỏ hơn hoặc bằng $$k$$, ta làm cho bài toán trên tương đương với bài toán gốc. $$M_i$$ là một cận trên đã biết trước của $$\left\vert  \beta_{i} \right\vert$$, là giá trị có thể tính bằng cách tiền xử lý $$X$$ và $$y$$.

Bây giờ vì đã định nghĩa bài toán bằng quy hoạch nguyên, từ đây ta có thể giải bằng các kỹ thuật quy hoạch nguyên.

## Một cách khéo léo để có nghiệm khả thi tốt
Hãy tổng quát hóa bài toán để giải thích thuật toán. Giả sử hàm mục tiêu $$g : \mathbb{R}^{p} \to \mathbb{R}$$ lồi trơn và $$\nabla g$$ là L-Lipschitz.
>
$$\min_{\beta} g(\beta) \quad \text{subject to} \quad \parallel \beta \parallel_{0} \le k$$

Với chọn tập con tốt nhất, $$g(\beta) = \frac{1}{2} \parallel X\beta - y \parallel^2_2$$.

### Quan sát
Nhờ hàm $$H_k(u)$$ được định nghĩa như sau, ta có thể tìm $$k$$ phần tử có giá trị tuyệt đối lớn nhất của $$u \in \mathbb{R}^p$$.
>
$$ H_k(u) = \underset{\beta : \parallel \beta \parallel_{0} \le k}{\text{argmin}} \parallel \beta - u \parallel^2_2$$

Khi đó, hàm $$H_k(u)$$ thực hiện hard thresholding. Cũng có thể xem nó là phép chiếu $$u$$ lên tập $$\beta$$ thỏa $$\parallel \beta \parallel_{0} \le k$$.

### Thuật toán bậc nhất rời rạc (Discrete first-order algorithm)
Bây giờ hãy định nghĩa thuật toán bằng gradient descent và hàm $$H_k(u)$$.

1. Bắt đầu với $$\beta^{(0)}$$
2. với $$i = 0, 1, ...$$ <br>
$$\quad \beta^{(i+1)} = H_k \left(\beta^{(i)} - \frac{1}{L} \nabla g(\beta^{(i)})\right)$$<br>
kết thúc vòng lặp<br>

Lặp lại quá trình trên thì $$\beta^{(i)} \to \bar{\beta}$$ hội tụ. Đây có thể gọi là một nghiệm cục bộ của bài toán cực tiểu hóa ở trên.
>
$$ \bar{\beta} =  H_k \left(\bar{\beta} - \frac{1}{L} \nabla g(\bar{\beta})\right)$$

Về kết quả, thuật toán này có thể xem là thuật toán proximal gradient, vì hàm $$H_k(u)$$ đóng vai trò là toán tử proximal.
## Kết quả tính toán
### Khoảng cách của quy hoạch số nguyên hỗn hợp (Mixed integer programming gap)
Hãy xem kết quả thí nghiệm của bài toán chọn tập con ở hình dưới.

Ở đồ thị bên trái, cận trên đã đạt tối ưu ngay từ sớm nhưng cận dưới tăng chậm và chỉ đến điểm gặp cận trên ta mới biết đó là nghiệm tối ưu. Đó là vì trong quy hoạch tuyến tính không có cách kiểm tra nghiệm có tối ưu hay không, và chỉ khi cận trên và cận dưới bằng nhau ta mới biết nghiệm là tối ưu.
(Tham khảo: hiệu giữa cận trên và cận dưới được gọi là mixed integer programming gap.)

Hình bên phải cho thấy cùng kết quả thí nghiệm đó dưới dạng mixed integer programming gap thu nhỏ dần. Đồ thị màu cam biểu diễn mixed integer programming gap, tức hiệu giữa cận trên và cận dưới, đang giảm dần.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_03_subset_results1.png" alt="[Hình 1] Tập dữ liệu n=350, p = 64, k=6 [3]">
  <figcaption style="text-align: center;">$$[Hình 1] \; Dữ \; liệu \; n=350, p = 64, k=6 \; [3]$$</figcaption>
</p>
</figure>
<br>

### Khởi động nguội và khởi động ấm (Cold and Warm Starts)
Hình tiếp theo cho thấy warm start nhìn chung có hiệu năng vượt trội so với cold start.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_04_subset_results2.png" alt="[Hình 2] Cold start và Warm start [3]">
  <figcaption style="text-align: center;">[Hình 2] Cold start và Warm start [3]</figcaption>
</p>
</figure>
<br>

### Phát hiện tính thưa (Sparsity Detection)
Hình tiếp theo so sánh tính thưa của MIP (Mixed Integer Programming), Lasso, Step regression và Sparsenet. Kết quả cho thấy MIP cho kết quả thưa nhất.


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_05_subset_results3.png" alt="[Hình 3] Phát hiện tính thưa (dữ liệu tổng hợp) [3]">
  <figcaption style="text-align: center;">[Hình 3] Phát hiện tính thưa (dữ liệu tổng hợp) [3]</figcaption>
</p>
</figure>
<br>
