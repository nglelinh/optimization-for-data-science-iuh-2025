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

LBFGS là một ví dụ của các phương pháp quasi-Newton bộ nhớ hạn chế, và rất hữu ích khi chi phí tính toán hoặc lưu trữ ma trận Hessian là không hợp lý. Phương pháp này ước lượng (xấp xỉ) ma trận Hessian bằng cách chỉ duy trì một vài vector $$n$$-chiều thay vì lưu trữ một ma trận Hessian dày đặc $$n \times n$$.

Thuật toán LBFGS dựa trên BFGS, như tên gọi của nó. Ý tưởng chính là sử dụng thông tin độ cong từ các vòng lặp gần nhất để ước lượng Hessian. Mặt khác, thông tin độ cong từ các vòng lặp cũ hơn không được sử dụng để tiết kiệm không gian lưu trữ, vì nó có thể khá xa với hành vi được thể hiện bởi Hessian của vòng lặp hiện tại.

Lưu ý phụ, các phiên bản bộ nhớ hạn chế của các thuật toán quasi-Newton khác (ví dụ: SR1) cũng có thể được suy ra bằng cách sử dụng cùng kỹ thuật [14].

# LBFGS

Để giải thích LBFGS, trước tiên hãy xem xét phương pháp BFGS. Tại mỗi bước, BFGS cập nhật $$x$$ như sau:

>$$
>x^+ = x - t H \nabla f, \\\\
>\text{trong đó } t \text{ là độ dài bước và } H \text{ được cập nhật tại mỗi vòng lặp bằng công thức, }\\\\
>\text{ }\\\\
>H^+ = \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big) + \frac{ss^T}{y^Ts}. \\\\
>$$

Với $$H$$ như trên, $$H^+q, q \in \mathbb{R}^n$$ có thể được biểu diễn bằng các số vô hướng $$\alpha, \beta \in \mathbb{R}$$ và các vector $$p, s \in \mathbb{R}^n$$.

>$$
>\begin{align}
>H^+q &= \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big)q + \frac{ss^Tq}{y^Ts}\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) \underbrace{H \big( q - \frac{s^T q}{y^Ts} y \big)}_{p} + \underbrace{\frac{s^Tq}{y^Ts}}_{\alpha} s\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) p + \alpha s\\\\
> &= p - \underbrace{\frac{y^Tp}{y^Ts}}_{\beta}s + \alpha s \\\\
> &= p + (\alpha - \beta) s, \\\\
>& \text{trong đó } \alpha = \frac{s^Tq}{y^Ts}, q^+ = q - \alpha y, p = Hq^+, \beta = \frac{y^Tp}{y^Ts}.
>\end{align} \\\\
>$$

Khi $$H$$ được cập nhật qua k lần cập nhật BFGS, thì $$Hq= -H\nabla f(x)$$ có thể được tính toán trong độ phức tạp $$O(kn)$$ (xem thuật toán bên dưới). Để sử dụng bộ nhớ hiệu quả, chúng ta chỉ sử dụng thông tin độ cong từ $$m$$ vòng lặp gần nhất. (với $$k \ge m$$)

# Thuật toán

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter18/algorithm_quasi-newton.png" alt="[Fig1] Thuật toán LBFGS [3]" width="90%">
  <figcaption style="text-align: center;">[Fig1] Thuật toán LBFGS [3]</figcaption>
</p>
</figure>

Thông thường, xấp xỉ Hessian nghịch đảo $$H_k$$ là dày đặc, và trong trường hợp có nhiều biến, phép toán trở nên rất nặng. LBFGS thu được $$H_k \nabla f_k$$ bằng tổng và tích của các vector liên tiếp, giải quyết vấn đề tính toán của $$H_k$$.

Trong tính toán, xấp xỉ Hessian ban đầu $$H^{0, k}$$ thường (và đã được xác minh là rất hiệu quả) là tích của ma trận đơn vị với một số hằng số ($$H^{0, k} = \gamma_k I$$), do đó việc tính toán không quá lớn ([14] mục 7.2).

>$$
H^{0, k} = \gamma_k I, \\\\
>\text{trong đó } \: \gamma_k = \frac{s^T_{k-1}y_{k-1}}{y^T_{k-1}y_{k-1}}.
>$$

* **Lưu ý:** $$H^{0, k}$$ thay đổi theo mỗi vòng lặp.