---
layout: post
title: '08-02-01 Phương pháp Subgradient Ngẫu nhiên'
chapter: '08'
order: 12
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Xét bài toán cực tiểu hóa tổng của $$m$$ hàm lồi sau:

>$$
\begin{equation}
\min_x \sum_{i=1}^m f_i(x)
\end{equation}
$$

Nếu áp dụng phương pháp subgradient tiêu chuẩn, ở mỗi bước lặp ta phải tính subgradient cho toàn bộ $$m$$ hàm $$f_i$$ rồi cộng lại (tương tự như động cơ dẫn đến [stochastic gradient descent]({% multilang_post_url contents/chapter06/21-03-20-06_05_stochastic_gradient_descent %})).

Thay vì tính trên toàn bộ tổng, phương pháp subgradient ngẫu nhiên chỉ cập nhật theo một hàm thành phần tại mỗi bước:

>$$
\begin{align}
x^{(k)} = x^{(k-1)} - t_k \cdot g_{i_k}^{(k-1)}, \quad k = 1, 2, 3, . . . 
\end{align}
$$

Trong đó, $$i_k \in \{1,...,m\}$$ là chỉ số được chọn tại bước lặp thứ $$k$$, và $$g_{i}^{(k-1)} \in \partial f_{i}(x^{k-1})$$. Cách chọn chỉ số $$i_k$$ — theo thứ tự tuần hoàn (cyclic) hay chọn ngẫu nhiên (randomized) — sẽ ảnh hưởng đến tốc độ hội tụ, như sẽ phân tích ở bài tiếp theo. Hướng cập nhật này khác với [phương pháp subgradient]({% multilang_post_url contents/chapter08/20-03-29-08_01_subgradient_method %}) thông thường (còn gọi là phương pháp subgradient batch hoặc full batch), vốn dùng tổng $$\sum_{i=1}^{m} g_i^{(k-1)}$$.

Khi mọi hàm $$f_i$$ ($$i = 1,...,m$$) đều khả vi, thuật toán này trở về đúng stochastic gradient descent; do đó, phương pháp subgradient ngẫu nhiên là một dạng tổng quát hơn.