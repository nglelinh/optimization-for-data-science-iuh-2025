---
layout: post
title: 04-04 Tối ưu hóa từng phần
chapter: '04'
order: 5
owner: YoungJae Choung
categories:
- chapter04
lang: vi
---
[Nhắc lại: ]({% multilang_post_url contents/chapter03/21-02-12-03_02_operations_that_preserve_convexity %})
Nếu $$C$$ là tập lồi và $$f$$ lồi theo $$(x,y)$$, thì $$g(x) = \min_{y \in C} f(x, y)$$ lồi theo $$x$$.

Vậy, tối ưu hóa từng phần trong một bài toán lồi được xây dựng với các hàm nhiều biến bảo toàn tính lồi.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter04/partial-optimization.png" alt="[Fig1] partial optimization of a convex problem [3]">
  <figcaption style="text-align: center;">[Hình 1] Tối ưu hóa từng phần của một bài toán lồi [3]</figcaption>
</p>
</figure>
<br>

### Ví dụ: Dạng hinge của SVM
Đối với tập không tách được, bài toán SVM được định nghĩa như:
>$$
\begin{aligned}
&\min_{\beta, \beta_{0}, \xi} &&\frac{1}{2}\|\beta\|_2^2 + C \sum_{i=1}^{n} \xi_{i} \\
&\text{subject to} &&{\xi}_{i} \ge 0, \\ 
&&&y_{i}(x_{i}^T \beta + \beta_{0}) \ge 1 - {\xi}_{i}, \\
&&&i = 1, .., n \\
\end{aligned}
$$

Các ràng buộc trên có thể được biểu diễn thành một ràng buộc duy nhất:
> $$
\begin{aligned}
{\xi}_{i} \ge \max\{0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})\} \\
\end{aligned}
$$

Trong trường hợp này, $$\max\{0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})\}$$ là giá trị nhỏ nhất cho $$\xi_{i}$$, và chúng ta có thể định nghĩa $$\tilde{f}$$ như:

> $$
\begin{aligned}
\frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} {\xi}_{i} &\ge \frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} \max({0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})})\\
&= \min\{\frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} \xi_{i} \quad | \quad \xi_{i} \ge 0, \ y_{i}(x_{i}^T \beta + \beta_{0}) \ge 1 - \xi_{i}, \ i = 1, .., n\} \\
&= \tilde{f}(\beta, \beta_{0}) \\
\end{aligned}
$$


Bằng cách sử dụng $$\tilde{f}$$ được đơn giản hóa làm hàm mục tiêu, một nghiệm đơn giản hơn có thể được thu được. Trong bài toán đã cho, $$\xi$$ đã bị loại bỏ, và nó cũng đã được chuyển đổi từ bài toán có ràng buộc thành bài toán không ràng buộc.

>$$
\begin{aligned}
\min_{\beta, \beta_0} \frac{1}{2} \|\beta\|_2^2 + C \sum_{i=1}^{n} \max\{0, 1 - y_{i} (x_{i}^{T} \beta + \beta_{0}) \}
\end{aligned}
$$
