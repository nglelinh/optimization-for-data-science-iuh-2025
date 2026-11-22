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
[Nhắc lại:]({% multilang_post_url contents/chapter03/21-02-12-03_02_operations_that_preserve_convexity %})
Nếu $$C$$ là tập lồi và $$f$$ là hàm lồi đồng thời theo $$(x, y)$$, thì hàm $$g(x) = \min_{y \in C} f(x, y)$$ là hàm lồi theo $$x$$.

Do đó, phép tối ưu hóa từng phần trên một tập con các biến trong bài toán tối ưu hóa lồi vẫn bảo toàn tính lồi.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter04/partial-optimization.png" alt="[Fig1] partial optimization of a convex problem [3]">
  <figcaption style="text-align: center;">[Hình 1] Tối ưu hóa từng phần của một bài toán lồi [3]</figcaption>
</p>
</figure>
<br>

### Ví dụ: Dạng hàm mất mát hinge của SVM
Đối với tập dữ liệu không tách tuyến tính được, bài toán máy vectơ hỗ trợ (SVM) biên mềm được phát biểu như sau:
>$$
\begin{aligned}
&\min_{\beta, \beta_{0}, \xi} &&\frac{1}{2}\|\beta\|_2^2 + C \sum_{i=1}^{n} \xi_{i} \\
&\text{subject to} &&{\xi}_{i} \ge 0, \\ 
&&&y_{i}(x_{i}^T \beta + \beta_{0}) \ge 1 - {\xi}_{i}, \\
&&&i = 1, \dotsc, n. \\
\end{aligned}
$$

Hai nhóm ràng buộc trên có thể gộp lại thành một ràng buộc duy nhất theo $$\xi_i$$:
> $$
\begin{aligned}
{\xi}_{i} \ge \max\{0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})\} \\
\end{aligned}
$$

Với mỗi cặp $$(\beta, \beta_0)$$ cố định, giá trị nhỏ nhất có thể của $$\xi_{i}$$ chính là $$\max\{0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})\}$$. Khi tối ưu hóa riêng theo biến $$\xi$$, ta định nghĩa hàm mục tiêu rút gọn $$\tilde{f}$$ như sau:

> $$
\begin{aligned}
\frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} {\xi}_{i} &\ge \frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} \max({0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})})\\
&= \min\left\{\frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} \xi_{i} \;\middle|\; \xi_{i} \ge 0, \ y_{i}(x_{i}^T \beta + \beta_{0}) \ge 1 - \xi_{i}, \ i = 1, \dotsc, n\right\} \\
&= \tilde{f}(\beta, \beta_{0}). \\
\end{aligned}
$$

Sử dụng hàm mục tiêu rút gọn $$\tilde{f}$$ giúp loại bỏ hoàn toàn các biến phụ $$\xi$$, đồng thời chuyển bài toán ban đầu từ dạng có ràng buộc sang bài toán tối ưu hóa lồi không ràng buộc tương đương:

>$$
\begin{aligned}
\min_{\beta, \beta_0} \frac{1}{2} \|\beta\|_2^2 + C \sum_{i=1}^{n} \max\{0, 1 - y_{i} (x_{i}^{T} \beta + \beta_{0}) \}
\end{aligned}
$$
