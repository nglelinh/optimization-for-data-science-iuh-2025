---
layout: post
title: 04-06 Loại bỏ ràng buộc đẳng thức
chapter: '04'
order: 7
owner: YoungJae Choung
categories:
- chapter04
lang: vi
---
Phần này trình bày kỹ thuật loại bỏ các ràng buộc đẳng thức tuyến tính trong bài toán tối ưu hóa lồi nhằm đơn giản hóa tập khả thi hoặc cấu trúc bài toán.

Xét bài toán tối ưu hóa lồi có dạng:

>$$
\begin{aligned}
&\min_{x} &&f(x)\\
&\text{subject to } &&g_{i}(x) \leq 0, \quad i = 1, \dotsc, m\\
&&&{Ax = b}.\\
\end{aligned}
$$

Giả sử $$x_{0}$$ là một nghiệm riêng bất kỳ thỏa mãn $$Ax_{0} = b$$ và $$M$$ là ma trận sao cho không gian cột của nó trùng với không gian hạch của $$A$$, tức là $$\text{col}(M) = \text{null}(A)$$. Khi đó, mọi điểm $$x$$ thỏa mãn ràng buộc đẳng thức $$Ax = b$$ đều có thể biểu diễn dưới dạng:
>$$x = My + x_{0}$$

Thật vậy, $$Ax = A(My + x_{0}) = AMy + Ax_{0} = 0 + b = b$$. Do đó, bằng cách thay thế $$x = My + x_{0}$$ vào bài toán gốc, ta loại bỏ hoàn toàn ràng buộc đẳng thức và thu được bài toán tương đương:

>$$
\begin{aligned}
&\min_y &&f(My+x_0)\\
&\text{subject to} &&g_{i}(My+x_{0}) \leq 0, \quad i = 1, \dotsc, m.\\
\end{aligned}
$$

Tuy nhiên, trong thực tế cần cân nhắc kỹ trước khi áp dụng phương pháp này vì hai hạn chế chính:
1. Việc tìm ma trận $$M$$ (chẳng hạn qua phân tích QR hoặc SVD) thường tốn kém về mặt tính toán khi kích thước bài toán lớn.
2. Nếu ma trận bài toán theo biến gốc $$x$$ có cấu trúc thưa, việc chuyển sang biến $$y$$ qua ma trận dày đặc $$M$$ có thể phá vỡ tính thưa và làm tăng chi phí tính toán.
