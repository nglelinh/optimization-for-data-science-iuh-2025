---
layout: post
title: '07-03-04 Ví dụ: Ngưỡng mềm (Soft-Thresholding)'
chapter: '07'
order: 10
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
---

Xét trường hợp đơn giản hơn của bài toán Lasso khi $$X=I$$:
>
\begin{equation}
\min_{\beta} \frac{1}{2} \| y-\beta \|_2^2 + \lambda \| \beta \|_1
\end{equation}

Từ ví dụ trước, điều kiện tối ưu theo gradient dưới của bài toán này là:
>
$$
\begin{cases}
y_i-\beta_i = \lambda \cdot \text{sign}(\beta_i) &\text{nếu } \beta_i \neq 0 \\
 |y_i-\beta_i| \leq \lambda &\text{nếu } \beta_i = 0
\end{cases}
$$

Giải điều kiện trên cho từng tọa độ, ta thu được nghiệm dạng đóng $$\beta = S_{\lambda}(y)$$, với:
>
$$
[S_{\lambda}(y)]_{i} = 
\begin{cases}
y_i - \lambda &\text{nếu }y_i > \lambda \\
0             &\text{nếu }-\lambda \leq y_i \leq \lambda, \quad \quad i \in \{1,2,\dots,n \} \\
y_i + \lambda &\text{nếu } y_i < -\lambda
\end{cases}
$$

Toán tử $$S_{\lambda}$$ được gọi là **toán tử ngưỡng mềm (soft-thresholding operator)**.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_03_subgrad-6.png" alt="connection_to_convexity_geometry" width="80%" height="80%">
</p>
 <figcaption style="text-align: center;">$$\text{[Hình 1] Ngưỡng mềm, y (trục x), } \beta \text{ (trục y), } \lambda=1/2 \text{ [3]}$$ </figcaption>
</figure>