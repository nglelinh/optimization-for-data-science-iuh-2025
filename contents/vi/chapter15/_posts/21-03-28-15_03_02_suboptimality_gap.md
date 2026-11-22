---
layout: post
title: '15-03-02 Khoảng cách dưới tối ưu (Suboptimality gap)'
chapter: '15'
order: 9
owner: Minjoo Lee
categories:
- chapter15
lang: vi
---

Khoảng cách dưới tối ưu giữa giá trị $$f(x^*(t))$$ tại điểm đường trung tâm và giá trị tối ưu $$f(x^*)$$ của bài toán gốc là bao nhiêu?

Trước hết, từ tính lồi của $$f$$ và $$h_i$$ (đồ thị hàm lồi luôn nằm trên tiếp tuyến khai triển Taylor bậc nhất của nó), ta có hai bất đẳng thức:

>$$
>\begin{align}
>f(x^*) &\ge f(x^*(t)) + \nabla f(x^*(t))^T (x^* - x^*(t)) \\\\
>h_i(x^*) &\ge h_i(x^*(t)) + \nabla h_i(x^*(t))^T (x^* - x^*(t)), \quad i = 1, \cdots, m
>\end{align}
>$$

Từ bất đẳng thức thứ hai, chuyển vế ta thu được:

$$
h_i(x^*(t)) - h_i(x^*) \le \nabla h_i(x^*(t))^T (x^*(t) - x^*), \quad i = 1, \cdots, m
$$

## Dẫn xuất khoảng cách dưới tối ưu

Kết hợp hai bất đẳng thức trên với điều kiện KKT nhiễu ở mục trước (với $$u_i(t) > 0$$), ta có:

$$
\begin{align}
f(x^*(t)) - f(x^*) + \sum_{i=1}^{m} u_i(t) (h_i(x^*(t)) - h_i(x^*) ) &\le \left\langle \nabla f(x^*(t)) + \sum_{i=1}^{m} u_i(t) \nabla h_i(x^*(t)), \quad x^*(t) - x^* \right\rangle \\\\
&= \left\langle -A^Tv, \quad x^*(t) - x^* \right\rangle \\\\
\end{align}
$$

Vì $$Ax^*(t) = b$$ và $$Ax^* = b$$, nên $$\langle -A^Tv, x^*(t) - x^* \rangle = -v^T A(x^*(t) - x^*) = 0$$.

Chuyển tổng ở vế trái sang vế phải và rút gọn:

$$
\begin{align}
f(x^*(t)) - f(x^*) &\le - \sum_{i=1}^{m} u_i(t) (h_i(x^*(t)) - h_i(x^*) ) \\\\
&= \frac{m}{t} + \sum_{i=1}^{m} u_i(t) h_i(x^*) \\\\
&\le \frac{m}{t}
\end{align}
$$

Ở dòng thứ hai, ta thay $$u_i(t) \cdot h_i(x^*(t)) = - \frac{1}{t}$$ từ điều kiện KKT nhiễu để thu được $$\frac{m}{t}$$. Ở dòng cuối, tổng $$\sum_{i=1}^{m} u_i(t) h_i(x^*) \le 0$$ vì $$u_i(t) > 0$$ và $$h_i(x^*) \le 0$$.

Như vậy, ta thu được cận trên cho khoảng cách dưới tối ưu, đồng thời là tiêu chí dừng hữu ích cho phương pháp chắn (mối liên hệ với khoảng cách đối ngẫu cũng sẽ được phân tích thêm ở các chương sau):

>$$
>\begin{align}
>f(x^*(t)) - f(x^*) \le \frac{m}{t}
>\end{align}
>$$
