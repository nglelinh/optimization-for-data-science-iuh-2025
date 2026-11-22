---
layout: post
title: '25-02-02 Least median of squares và least quantile regression'
chapter: '25'
order: 9
owner: YoungJae Choung
categories:
- chapter25
lang: vi
---

Ở các chương trước, bài toán hồi quy thường được giải bằng cách cực tiểu hóa chuẩn $$l_2$$ hoặc chuẩn $$l_1$$ của vector phần dư. Để đạt độ bền vững (robustness) cao hơn trước các điểm ngoại lai, ta có thể cực tiểu hóa *trung vị* của phần dư — phương pháp mang tên **Least Median of Squares (LMS)**. Ước lượng này có điểm sụp đổ gần 50%, tức vẫn giữ được độ ổn định ngay cả khi gần một nửa dữ liệu bị nhiễu nặng. Tuy nhiên, bài toán LMS lại thuộc lớp NP-khó.

Mục này giới thiệu cách mô hình hóa và giải bài toán tổng quát hơn là **Least Quantile of Squares (LQS)** bằng quy hoạch nguyên hỗn hợp.

## Bình phương trung vị nhỏ nhất (Least Median of Squares)

Cho ma trận đặc trưng $$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n \times p}$$, vector phản hồi $$y \in \mathbb{R}^{n}$$ và hệ số $$\beta \in \mathbb{R}^{p}$$, đặt vector phần dư $$r := y - X\beta$$.

### So sánh với các chuẩn hồi quy quen thuộc

* Bình phương tối thiểu (Least Squares — LS): $$\beta_{LS} := \underset{\beta}{\text{argmin}} \sum_{i} r^2_i$$
* Độ lệch tuyệt đối nhỏ nhất (Least Absolute Deviation — LAD): $$\beta_{LAD} := \underset{\beta}{\text{argmin}} \sum_{i} \lvert r_{i} \rvert$$

### Least Median of Squares (LMS)

>$$\beta_{LMS} := \underset{\beta}{\text{argmin}} (\text{median} \lvert r_{i} \rvert )$$

## Hồi quy phân vị nhỏ nhất (Least Quantile Regression)

Tổng quát hóa từ trung vị sang phân vị thứ $$q$$, bài toán **Least Quantile of Squares (LQS)** cực tiểu hóa phần dư tuyệt đối nhỏ thứ $$q$$ (ký hiệu $$\lvert r_{(q)} \rvert$$):

>$$\beta_{LQS} := \underset{\beta}{\text{argmin}} (\lvert r_{(q)} \rvert ), \quad 1 \le q \le n, \quad \lvert r_{(1)} \rvert \le \lvert r_{(2)} \rvert \le \cdots \le \lvert r_{(n)} \rvert$$

### Ý tưởng lập mô hình

Để biểu diễn bài toán này bằng quy hoạch nguyên hỗn hợp, với mỗi quan sát $$i$$ ta dùng một biến nhị phân nhằm phân tách hai nhóm phần dư:

>$$ \lvert r_{i} \rvert \le \lvert r_{(q)} \rvert \quad \text{hoặc} \quad \lvert r_{i} \rvert \ge \lvert r_{(q)} \rvert $$

### Công thức quy hoạch nguyên hỗn hợp

Đưa vào các biến phụ (slack) không âm $$\bar{\mu_{i}}$$, $$\mu_{i}$$ và các biến nhị phân $$z_i$$ sao cho $$z_i = 1$$ ứng với $$q$$ phần dư có trị tuyệt đối nhỏ nhất và $$z_i = 0$$ ứng với $$n-q$$ phần dư còn lại:

> $$
> \begin{align}
>   \min_{\beta, \mu, \bar{\mu}, z, \gamma} & \quad {\gamma} \\
>   \text{subject to} & \quad  \gamma \ge \lvert r_{i} \rvert - \bar{\mu_{i}}, \quad i = 1, \dots, n \\\\
>   & \quad  \gamma \le \lvert r_{i} \rvert + \mu_{i}, \quad i = 1, \dots, n \\\\
>   & \quad \bar{\mu_{i}} \le M \cdot (1-z_{i}), \quad i = 1, \dots, n \\\\
>   & \quad \mu_{i} \le M \cdot z_{i}, \quad i = 1, \dots, n \\\\
>   & \quad \sum^{n}_{i=1} z_{i} = q \\\\
>   & \quad \mu_{i}, \bar{\mu_{i}} \ge 0, \quad i = 1, \dots, n \\\\
>   & \quad z_{i} \in \{0, 1\},  \quad i = 1, \dots, n
> \end{align}
> $$

Trong công thức trên, hai nhóm ràng buộc đầu chứa giá trị tuyệt đối $$\lvert r_{i} \rvert$$ (đặc biệt ràng buộc $$\gamma \le \lvert r_i \rvert + \mu_i$$ là không lồi), nên cần biểu diễn lại các ràng buộc chứa giá trị tuyệt đối về dạng tuyến tính hóa/lồi thích hợp trước khi giải bằng nới lỏng lồi.

## Thuật toán bậc nhất

Ta có thể biểu diễn phần dư thứ $$q$$ dưới dạng hiệu của hai hàm lồi $$H_{q}(\beta)$$ và $$H_{q+1}(\beta)$$:

> $$ \lvert r_{(q)} \rvert = \lvert y_{(q)} - x^{T}_{(q)} \beta \rvert = H_{q}(\beta) - H_{q+1}(\beta)$$

trong đó $$H_{q}(\beta)$$ là tổng của $$n - q + 1$$ phần dư tuyệt đối lớn nhất:

> $$
> \begin{align}
> H_{q}(\beta) = \sum^{n}_{i=q} \lvert y_{(i)} - x^{T}_{(i)} \beta \rvert  = &
> \max_{w} \sum^{n}_{i=1} w_i \lvert y_{(i)} - x^{T}_{(i)} \beta \rvert \\\\
> & \text{subject to} \quad \sum^{n}_{i=1}  w_i  = n − q + 1 \\\\
> &0 \le w_i \le 1, \quad i = 1, \dots, n
> \end{align}
> $$

Khi các phần dư tuyệt đối được sắp theo thứ tự tăng dần, lấy tổng từ phần tử thứ $$q$$ trở đi trừ đi tổng từ phần tử thứ $$q+1$$ trở đi sẽ thu được đúng $$\lvert r_{(q)} \rvert$$.

Nhờ biểu diễn hiệu hai hàm lồi này, ta có thể dùng thuật toán dưới đạo hàm (subgradient) để tìm một cực tiểu địa phương của $$H_{q}(\beta) - H_{q+1}(\beta)$$ làm điểm khởi động nóng cho bộ giải MIP.

* Xem chi tiết trong bài báo [LEAST QUANTILE REGRESSION VIA MODERN OPTIMIZATION](https://arxiv.org/pdf/1310.8625.pdf).

## Kết quả thực nghiệm

Các đồ thị dưới đây minh họa kết quả thực nghiệm của bài toán Least Quantile of Squares từ bài báo trên.

### Mixed integer programming gap
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_06_LQS_results1.png" alt="[Hình 1] Mixed integer programming gap [3]">
  <figcaption style="text-align: center;">[Hình 1] Mixed integer programming gap [3]</figcaption>
</p>
</figure>
<br>

### Cold start và Warm start
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_07_LQS_results2.png" alt="[Hình 2] Cold start và Warm start [3]">
  <figcaption style="text-align: center;">[Hình 2] Cold start và Warm start [3]</figcaption>
</p>
</figure>
<br>
