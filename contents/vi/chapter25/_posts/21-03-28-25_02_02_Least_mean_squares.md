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

Nếu dữ liệu thực tế chứa những lỗi nhập liệu khổng lồ hoặc các cảm biến bị hỏng đột ngột, hồi quy bình phương tối thiểu (LS) có thể sụp đổ chỉ vì **một điểm ngoại lai duy nhất** (điểm sụp đổ $$0\%$$). Peter Rousseeuw (1984) đề xuất một ý tưởng cực kỳ táo bạo: thay vì cực tiểu hóa *tổng* bình phương phần dư, hãy cực tiểu hóa **trung vị** của các phần dư tuyệt đối (**Least Median of Squares — LMS**), đạt điểm sụp đổ lý thuyết cao nhất có thể là gần $$50\%$$!

Thách thức duy nhất khiến LMS ít được dùng chính xác trong suốt 30 năm là tính NP-khó của nó. Bài học này trình bày cách Bertsimas và Mazumder (2014) viết lại bài toán tổng quát **Least Quantile Regression (LQS)** thành một quy hoạch nguyên hỗn hợp (MILP) gọn gàng, kết hợp khởi động nóng bằng thuật toán bậc nhất để giải chính xác và chứng nhận nghiệm.

## Kiến thức cần nhớ: Bốn trụ cột của Hồi quy phân vị nhỏ nhất (LQS) bằng MIP

Để hiểu trọn vẹn công thức MILP của bài toán LQS, hãy nắm chắc bốn trụ cột sau:

- **Điểm sụp đổ (Breakdown Point) và Độ bền vững:** LS (chuẩn $$\ell_2$$) bị kéo lệch vô hạn bởi 1 điểm ngoại lai; LAD (chuẩn $$\ell_1$$) bền vững với ngoại lai ở nhãn $$y$$ nhưng vẫn dễ bị phá bởi điểm đòn bẩy cao ở $$X$$; LMS/LQS chỉ quan tâm tới phần dư nhỏ thứ $$q$$ nên miễn nhiễm ngay cả khi gần một nửa mẫu vừa hỏng $$X$$ vừa hỏng $$y$$.
- **Mã hóa thống kê thứ tự $$|r_{(q)}|$$ bằng biến nhị phân:** Muốn giá trị $$\gamma$$ lớn hơn hoặc bằng ít nhất $$q$$ phần dư tuyệt đối, ta gắn biến nhị phân $$z_i \in \{0, 1\}$$ cho mỗi mẫu $$i$$ với ràng buộc $$\sum_{i=1}^n z_i \ge q$$ và $$|r_i| \le \gamma + M(1 - z_i)$$. Khi $$z_i = 1$$ (mẫu sạch được chọn), phần dư bị ép $$|r_i| \le \gamma$$; khi $$z_i = 0$$ (mẫu ngoại lai), ràng buộc được nới lỏng bởi hằng số lớn $$M$$.
- **Tối ưu phân rã hàm hiệu hai hàm lồi (Difference-of-Convex / First-Order Heuristic):** Vì tổng $$q$$ phần dư nhỏ nhất có thể viết dưới dạng hiệu của hai hàm lồi, thuật toán bậc nhất lặp luân phiên giữa tuyến tính hóa phần lõm (chọn tập $$q$$ mẫu có phần dư nhỏ nhất) và giải bài toán lồi con để tạo điểm khởi động nóng cực tốt.
- **Chứng nhận toàn cục qua MIP Gap:** Khác với các thuật toán chọn ngẫu nhiên cổ điển (như `lqs` trong R chỉ lấy mẫu vài tổ hợp và không biết mình cách tối ưu bao xa), khung MILP cho biết chính xác khoảng cách tới nghiệm toàn cục.

### Giải thích: Tính tay mô hình MILP của LQS trên dữ liệu có ngoại lai cực đoan

Xét bài toán ước lượng hằng số vị trí $$\beta \in \mathbb{R}$$ (tức mô hình $$r_i = y_i - \beta$$) cho 3 quan sát $$y = (1,\; 2,\; 100)^T$$, với phân vị trung vị $$q = 2$$ (tối thiểu hóa phần dư nhỏ thứ 2, tức $$|r_{(2)}|$$).

1. **Thiết lập bài toán MILP với $$M = 200$$:**
   Ta cần tìm $$\beta \in \mathbb{R}$$, $$\gamma \ge 0$$ và $$z_1, z_2, z_3 \in \{0, 1\}$$ sao cho:
   $$\min\ \gamma \qquad \text{s.t. } |y_i - \beta| \le \gamma + 200(1 - z_i) \; (i = 1, 2, 3), \quad z_1 + z_2 + z_3 \ge 2.$$
2. **Xét tổ hợp chọn 2 điểm sạch $$z = (1, 1, 0)$$:**
   - Ràng buộc hiệu lực cho $$i = 1, 2$$: $$|1 - \beta| \le \gamma$$ và $$|2 - \beta| \le \gamma$$.
   - Ràng buộc cho điểm ngoại lai $$i = 3$$ ($$z_3 = 0$$): $$|100 - \beta| \le \gamma + 200$$ (tự động thỏa mãn thoải mái!).
   - Để cực tiểu hóa $$\gamma = \max(|1 - \beta|,\; |2 - \beta|)$$, ta chọn $$\beta$$ nằm chính giữa $$1$$ và $$2$$: $$\beta^\star = 1.5$$, cho ra $$\gamma^\star = 0.5$$!
3. **So sánh với hai tổ hợp còn lại và các chuẩn khác:**
   - Nếu chọn $$z = (1, 0, 1)$$ (gồm $$1$$ và $$100$$): $$\gamma = \frac{100 - 1}{2} = 49.5 \gg 0.5$$.
   - Nếu chọn $$z = (0, 1, 1)$$ (gồm $$2$$ và $$100$$): $$\gamma = \frac{100 - 2}{2} = 49.0 \gg 0.5$$.
   - Trong khi đó, Bình phương tối thiểu (LS) cho $$\hat{\beta}_{\text{LS}} = \frac{1 + 2 + 100}{3} = 34.33$$ — hoàn toàn vô dụng!
   Ví dụ nhỏ này cho thấy rõ ràng cách biến nhị phân $$z_i$$ tự động "gạt" điểm ngoại lai $$100$$ ra khỏi mục tiêu cực tiểu hóa $$\gamma$$!

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
