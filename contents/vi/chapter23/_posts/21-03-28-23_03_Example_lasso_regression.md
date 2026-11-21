---
layout: post
title: '23-03 Ví dụ: hồi quy lasso'
chapter: '23'
order: 4
owner: YoungJae Choung
categories:
- chapter23
lang: vi
---


Ta viết bài toán hồi quy lasso dưới dạng hàm mục tiêu có phần không trơn tách được như sau.

> $$
> \min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2 + \lambda \|\beta\|_1
> $$

**Note:**
$$\|\beta\|_1 = \sum_{i=1}^p | \beta_i |$$

Khi các $$\beta_j, j \neq i$$ là giá trị cố định, hãy tìm $$\beta_i$$ cực tiểu hóa hàm mục tiêu đã cho.

$$\begin{align}
&0 = \nabla_i f(\beta) = X_i^T X_i \beta_i + X_i^T(X_{-i} \beta_{-i} - y) + \lambda s_i,\\\\
&\text{where } s_i \in \partial |\beta_i|
\Rightarrow 
\beta_i = S_{\lambda / \|X_i\|_2^2} \big( \frac{X_i^T(y-X_{-i} \beta_{-i})}{X_i^TX_i} \big)
\end{align}$$

Nghiệm có dạng hàm soft-thresholding với ngưỡng $$\lambda / \|X_i\|_2^2$$. Với coordinate descent, ta lặp và cập nhật $$\beta_i$$ với $$i=1,2,\dots,p,1,2,\dots$$.

## Thí nghiệm: so sánh tốc độ hội tụ - PG, AGD và CD

Đồ thị dưới đây so sánh tốc độ hội tụ của proximal gradient descent, accelerated gradient descent và coordinate descent cho bài toán hồi quy lasso với $$n=100, p=20$$. (Giá trị k trên trục hoành biểu diễn một bước (PG, AGD) hoặc một chu trình (CD).)

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/pd_vs_agd_vs_cd.png" alt="[Hình 1] PG, AGD và CD [3]">
  <figcaption style="text-align: center;">[Hình 1] PG, AGD và CD [3]</figcaption>
</p>
</figure>
<br><br>

Cũng như ở [ví dụ hồi quy tuyến tính]({% multilang_post_url contents/chapter23/21-03-28-23_02_Example_linear_regression %}), ở bài toán hồi quy lasso coordinate descent cũng cho tốc độ hội tụ vượt trội. (Nó dùng nhiều thông tin hơn các phương pháp bậc nhất.)

* **Lưu ý:** Mọi phương pháp trong thí nghiệm trên đều có độ phức tạp thời gian $$O(np)$$ flops mỗi vòng lặp.
