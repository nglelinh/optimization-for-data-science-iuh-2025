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


Xét bài toán hồi quy Lasso dưới dạng tổng của một hàm lồi khả vi và một hàm không trơn tách được theo từng tọa độ:

> $$
> \min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2 + \lambda \|\beta\|_1
> $$

**Lưu ý:** $$\|\beta\|_1 = \sum_{i=1}^p | \beta_i |$$.

Giữ cố định các thành phần $$\beta_j$$ ($$j \neq i$$), ta tìm $$\beta_i$$ cực tiểu hóa hàm mục tiêu từ điều kiện tối ưu bậc nhất với dưới đạo hàm:

$$\begin{align}
&0 \in \partial_i f(\beta) \;\Longleftrightarrow\; 0 = X_i^T X_i \beta_i + X_i^T(X_{-i} \beta_{-i} - y) + \lambda s_i,\\\\
&\text{với } s_i \in \partial |\beta_i|
\;\Rightarrow\;
\beta_i = S_{\lambda / \|X_i\|_2^2} \big( \frac{X_i^T(y-X_{-i} \beta_{-i})}{X_i^TX_i} \big)
\end{align}$$

Nghiệm cập nhật có dạng toán tử co ngưỡng mềm (soft-thresholding) với ngưỡng $$\lambda / \|X_i\|_2^2$$. Thuật toán coordinate descent lặp lại bước cập nhật $$\beta_i$$ này lần lượt cho $$i=1,2,\dots,p,1,2,\dots$$.

## Thí nghiệm: so sánh tốc độ hội tụ giữa PG, AGD và CD

Đồ thị dưới đây so sánh tốc độ hội tụ của proximal gradient descent (PG), accelerated proximal gradient descent (AGD) và coordinate descent (CD) trên bài toán hồi quy Lasso với $$n=100, p=20$$. Giá trị $$k$$ trên trục hoành biểu diễn một bước lặp (đối với PG, AGD) hoặc một chu trình duyệt đủ $$p$$ tọa độ (đối với CD).

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/pd_vs_agd_vs_cd.png" alt="[Hình 1] PG, AGD và CD [3]">
  <figcaption style="text-align: center;">[Hình 1] PG, AGD và CD [3]</figcaption>
</p>
</figure>
<br><br>

Tương tự [ví dụ hồi quy tuyến tính]({% multilang_post_url contents/chapter23/21-03-28-23_02_Example_linear_regression %}), coordinate descent tiếp tục hội tụ nhanh hơn đáng kể so với PG và AGD nhờ sử dụng ngay thông tin cập nhật mới nhất của từng tọa độ trong mỗi chu trình.

* **Lưu ý:** Cả ba phương pháp trong thí nghiệm trên đều có chi phí tính toán $$O(np)$$ flops cho mỗi vòng lặp/chu trình.
