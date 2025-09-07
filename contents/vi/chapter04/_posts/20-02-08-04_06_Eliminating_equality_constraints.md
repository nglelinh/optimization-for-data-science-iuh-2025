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
Phần này giải thích các kỹ thuật loại bỏ ràng buộc đẳng thức trong các bài toán tối ưu hóa lồi để đơn giản hóa tập khả thi hoặc cấu trúc bài toán.

>$$
\begin{aligned}
&\min_{x} &&f(x)\\
&\text{subject to } &&g_{i}(x) \leq 0, i = 1, .., m\\
&&&{Ax = b}.\\
\end{aligned}
$$

Đối với một nghiệm tùy ý $$x_{0}$$ thỏa mãn $$Ax_{0} = b$$ và $$\text{col}(M) = \text{null}(A)$$, bất kỳ $$x$$ nào thỏa mãn ràng buộc đẳng thức có thể được biểu diễn như sau:
>$$x = My + x_{0}$$

Tức là, $$Ax = A(My + x_{0}) = AMy + Ax_{0} = 0 + b = b$$. Do đó, bằng cách thay thế $$My+x_{0}$$ cho $$x$$ trong bài toán đã cho, chúng ta có thể loại bỏ ràng buộc đẳng thức.

Vậy, bài toán sau tương đương với bài toán gốc:

>$$
\begin{aligned}
&\min_y &&f(My+x_0)\\
&\text{subject to} &&g_{i}(My+x_{0}) \leq 0, i = 1, .., m.\\
\end{aligned}
$$

Tuy nhiên, cần thận trọng khi sử dụng phương pháp này vì các lý do sau:
1. Việc tính toán $$M$$ nói chung rất đắt đỏ.
2. Nếu $$x$$ thưa hơn $$y$$, chi phí tính toán sử dụng $$y$$ có thể cao hơn.
