---
layout: post
title: 18-07 BFGS Bộ nhớ Hạn chế (LBFGS)
chapter: '18'
order: '8'
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

# Giới thiệu

L-BFGS (Limited-memory BFGS) là đại diện tiêu biểu của lớp phương pháp Quasi-Newton bộ nhớ hạn chế, đặc biệt hữu ích khi chi phí tính toán hoặc lưu trữ ma trận Hessian dày đặc kích thước $$n \times n$$ quá lớn. Thay vì lưu toàn bộ ma trận $$n \times n$$, L-BFGS chỉ lưu một số ít vector $$n$$-chiều để biểu diễn ngầm xấp xỉ nghịch đảo Hessian.

Như tên gọi, L-BFGS được xây dựng trực tiếp từ BFGS. Ý tưởng cốt lõi là chỉ sử dụng thông tin độ cong từ $$m$$ vòng lặp gần nhất để xấp xỉ Hessian nghịch đảo, đồng thời loại bỏ thông tin từ các vòng lặp quá cũ — vừa tiết kiệm bộ nhớ, vừa tránh dùng thông tin độ cong đã không còn phản ánh đúng tính chất cục bộ tại điểm lặp hiện tại.

Ngoài ra, phiên bản bộ nhớ hạn chế của các thuật toán Quasi-Newton khác (chẳng hạn SR1) cũng có thể được xây dựng theo cùng nguyên lý [14].

# L-BFGS

Để hiểu L-BFGS, trước hết nhắc lại phép cập nhật của BFGS ở mỗi vòng lặp:

>$$
>x^+ = x - t H \nabla f, \\\\
>\text{trong đó } t \text{ là độ dài bước và } H \text{ được cập nhật theo công thức:}\\\\
>\text{ }\\\\
>H^+ = \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big) + \frac{ss^T}{y^Ts}. \\\\
>$$

Với cấu trúc trên, tích ma trận–vector $$H^+q$$ (với $$q \in \mathbb{R}^n$$) có thể được tính chỉ bằng các phép tích vô hướng tạo thành các đại lượng vô hướng $$\alpha, \beta \in \mathbb{R}$$ và các phép cộng vector theo $$p, s \in \mathbb{R}^n$$:

>$$
>\begin{align}
>H^+q &= \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big)q + \frac{ss^Tq}{y^Ts}\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) \underbrace{H \big( q - \frac{s^T q}{y^Ts} y \big)}_{p} + \underbrace{\frac{s^Tq}{y^Ts}}_{\alpha} s\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) p + \alpha s\\\\
> &= p - \underbrace{\frac{y^Tp}{y^Ts}}_{\beta}s + \alpha s \\\\
> &= p + (\alpha - \beta) s, \\\\
>& \text{trong đó } \alpha = \frac{s^Tq}{y^Ts}, \ q^+ = q - \alpha y, \ p = Hq^+, \ \beta = \frac{y^Tp}{y^Ts}.
>\end{align} \\\\
>$$

Nếu $$H$$ được hình thành sau $$k$$ bước cập nhật BFGS, thì hướng bước $$-H\nabla f(x)$$ có thể được tính trực tiếp với độ phức tạp $$O(kn)$$ mà không cần tạo tường minh ma trận $$H$$ (xem thuật toán đệ quy hai vòng bên dưới). Để tiết kiệm bộ nhớ khi $$k$$ lớn, L-BFGS chỉ giữ lại thông tin độ cong từ $$m$$ vòng lặp gần nhất (với $$k \ge m$$), đưa chi phí mỗi bước xuống $$O(mn)$$.

# Thuật toán

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter18/algorithm_quasi-newton.png" alt="[Fig1] Thuật toán LBFGS [3]" width="90%">
  <figcaption style="text-align: center;">[Fig1] Thuật toán LBFGS [3]</figcaption>
</p>
</figure>

Ma trận xấp xỉ nghịch đảo Hessian $$H_k$$ nhìn chung là ma trận dày đặc nên phép nhân ma trận trực tiếp rất tốn kém khi số biến lớn. L-BFGS tính trực tiếp tích $$H_k \nabla f_k$$ thông qua chuỗi các tích vô hướng và phép cộng vector, khắc phục hoàn toàn nút thắt bộ nhớ và tính toán của $$H_k$$.

Trong thực hành, xấp xỉ khởi đầu $$H^{0, k}$$ ở mỗi vòng lặp thường được chọn là bội số của ma trận đơn vị $$H^{0, k} = \gamma_k I$$ — lựa chọn đơn giản nhưng đã được chứng minh rất hiệu quả ([14] mục 7.2):

>$$
H^{0, k} = \gamma_k I, \\\\
>\text{trong đó } \: \gamma_k = \frac{s^T_{k-1}y_{k-1}}{y^T_{k-1}y_{k-1}}.
>$$

* **Lưu ý:** Hệ số co giãn $$\gamma_k$$ (và do đó $$H^{0, k}$$) được cập nhật lại ở mỗi vòng lặp.