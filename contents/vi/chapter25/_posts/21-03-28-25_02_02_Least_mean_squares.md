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

Cho đến nay, ta đã giải các bài toán hồi quy bằng cách cực tiểu hóa chuẩn $$l_2$$ hoặc chuẩn $$l_1$$ của phần dư. Có phương pháp nào bền vững (robust) hơn các phương pháp này không?

Khi thực hiện hồi quy để cực tiểu hóa trung vị của phần dư, ta có thể đạt hồi quy bền vững hơn. Phương pháp này gọi là **Least Median of Squares**, và nó đủ bền vững để ước lượng không bị hỏng ngay cả khi khoảng 50% dữ liệu bị hỏng. Tuy nhiên, bài toán này cũng là bài toán NP-khó!

Phần này giới thiệu cách giải bài toán **Least Quantile of Squares**, tổng quát hóa bài toán Least Median of Squares, bằng quy hoạch nguyên.
## Least median of squares
Cho $$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n×p}$$ và $$y \in \mathbb{R}^{n}$$. Và khi $$\beta \in \mathbb{R}^{p}$$, đặt $$r : = y - X\beta$$.

### Quan sát
* Least squares (LS) : $$\beta_{LS} : = \underset{\beta}{\text{argmin}} \sum_{i} r^2_i$$
* Least absolute deviation (LAD) : $$\beta_{LAD} : = \underset{\beta}{\text{argmin}} \sum_{i} \lvert r_{i} \rvert$$
### Least Median of Squares (LMS)
>$$\beta_{LMS} : = \underset{\beta}{\text{argmin}} (\text{median} \lvert r_{i} \rvert )$$

## Hồi quy phân vị nhỏ nhất (Least quantile regression)
Bài toán Least Quantile of Squares, tổng quát hóa bài toán Least Median of Squares, có thể định nghĩa như sau. Ở đây $$r_{(q)}$$ là phần dư tuyệt đối được sắp thứ tự thứ $$q$$.
### Least Quantile of Squares (LQS)
>$$\beta_{LQS} : = \underset{\beta}{\text{argmin}} (\lvert r_{(q)} \rvert ), \quad 1 \le q \le n, \quad \lvert r_{(1)} \rvert \le \lvert r_{(2)} \rvert \le \cdots \le \lvert r_{(n)} \rvert$$

### Bước then chốt trong việc lập công thức
Bây giờ hãy viết lại bài toán Least Quantile of Squares bằng quy hoạch nguyên. Khi đó, với mỗi phần tử $$i$$ của $$r$$, ta dùng một biến nhị phân để phân biệt hai trường hợp sau.

>$$ \lvert r_{i} \rvert \le \lvert r_{(q)} \rvert \quad \text{hoặc} \quad \lvert r_{i} \rvert \ge \lvert r_{(q)} \rvert $$

### Công thức quy hoạch nguyên
$$\bar{\mu_{i}}$$ và $$\mu_{i}$$ là các biến độ chùng (slack) theo ngưỡng; $$z_i = 1$$ cho $$q$$ phần dư có giá trị tuyệt đối nhỏ nhất và $$z_i = 0$$ cho $$n-q$$ phần dư còn lại.

> $$
> \begin{align}
>   \min_{\beta, \mu, \bar{\mu}, z, \gamma} & \quad {\gamma} \\
>   \text{subject to} & \quad  \gamma \ge \lvert r_{i} \rvert - \bar{\mu_{i}}, \quad i = 1, ..., n \\\\
>   & \quad  \gamma \le \lvert r_{i} \rvert + \mu_{i}, \quad i = 1, ..., n \\\\
>   & \quad \bar{\mu_{i}} \le M \cdot (1-z_{i}), \quad i = 1, ..., n \\\\
>   & \quad \mu_{i} \le M \cdot z_{i}, \quad i = 1, ..., n \\\\
>   & \quad \sum^{n}_{i=1} z_{i} = q \\\\
>   & \quad \mu_{i}, \bar{\mu_{i}} \ge 0, \quad i = 1, ..., n \\\\
>   & \quad z_{i} \in \{0, 1\},  \quad i = 1, ..., n
> \end{align}
> $$

Ở bài toán này, hai ràng buộc đầu chứa giá trị tuyệt đối của phần dư $$\lvert r_{i} \rvert$$ nên không thể giải bằng nới lỏng lồi. Do đó, cần chuyển hai ràng buộc đầu thành hàm lồi.


## Thuật toán bậc nhất
$$\lvert r_{i} \rvert$$ có thể được định nghĩa lại dưới dạng hàm lồi $$H_{q}(\beta)$$ như sau.
>
$$ \lvert r_{(q)} \rvert = \lvert y_{(q)} - x^{T}_{(q)} \beta \rvert = H_{q}(\beta) - H_{q+1}(\beta)$$

Khi đó $$H_{q}(\beta)$$ được định nghĩa như sau.

> $$
> \begin{align}
> H_{q}(\beta) = \sum^{n}_{i=q} \lvert y_{(i)} - x^{T}_{(i)} \beta \rvert  = &
> \max_{w} \sum^{n}_{i=1} w_i \lvert y_{(i)} - x^{T}_{(i)} \beta \rvert \\\\
> & \text{subject to} \quad \sum^{n}_{i=1}  w_i  = n − q + 1 \\\\
> &0 \le w_i \le 1, \quad i = 1, ..., n
> \end{align}
> $$

$$H_{q}(\beta)$$ là tổng của tất cả các phần dư từ thứ $$q$$ trở lên, khi các $$\lvert r_{i} \rvert$$ đã định nghĩa ở trên được sắp xếp từ nhỏ đến lớn. Do đó, lấy tổng các phần dư từ thứ $$q$$ trở lên trừ đi tổng các phần dư từ thứ $$q+1$$ trở lên thì được phần dư thứ $$q$$.

Bằng thuật toán subgradient, ta có thể tìm cực tiểu địa phương của $$H_{q}(\beta) - H_{q+1}(\beta)$$.

* Thông tin chi tiết xem bài báo [LEAST QUANTILE REGRESSION VIA MODERN OPTIMIZATION](https://arxiv.org/pdf/1310.8625.pdf).
## Kết quả tính toán
Kết quả thí nghiệm bài toán Least Quantile of Squares trong bài báo trên có thể xem ở các đồ thị sau.

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
