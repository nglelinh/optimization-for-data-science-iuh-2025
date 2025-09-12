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

Hãy xem xét bài toán tối thiểu hóa tổng các hàm như sau:

>$$
\begin{equation}
\min_x \sum_{i=1}^m f_i(x)
\end{equation}
$$

Nếu chúng ta áp dụng phương pháp subgradient cho bài toán này, chúng ta cần tính subgradient cho mỗi hàm $$f_i$$ và cộng chúng lại. (Điều này tương tự như phương pháp được giới thiệu trong [stochastic gradient descent]({% multilang_post_url contents/chapter06/21-03-20-06_05_stochastic_gradient_descent %})).

Tóm lại, phương pháp subgradient ngẫu nhiên có dạng như sau:

>$$
\begin{align}
x^{(k)} = x^{(k-1)} - t_k \cdot g_{i_k}^{(k-1)}, \quad k = 1, 2, 3, . . . 
\end{align}
$$

Ở đây, $$i_k \in \{1,...,m\}$$ là chỉ số được chọn tại lần lặp thứ $$k$$. Như sẽ được thảo luận trong phần tiếp theo về tốc độ hội tụ của phương pháp subgradient ngẫu nhiên, việc lựa chọn phương pháp tuần hoàn hoặc ngẫu nhiên ảnh hưởng đến kết quả. $$g_{i}^{(k-1)} \in \partial f_{i}(x^{k-1})$$, và hướng cập nhật này khác với [phương pháp subgradient]({% multilang_post_url contents/chapter08/20-03-29-08_01_subgradient_method %}) thông thường (còn được gọi là phương pháp subgradient batch hoặc phương pháp subgradient full batch), nơi sử dụng $$\sum_{i=1}^{m} g_i^{(k-1)}$$.

Nếu mỗi $$f_i, i = 1,...,m$$ khả vi, thuật toán này trở thành stochastic gradient descent. (Phương pháp subgradient ngẫu nhiên là một dạng tổng quát hơn)