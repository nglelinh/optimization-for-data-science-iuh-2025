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

Khoảng cách dưới tối ưu giữa $$f(x^*(t))$$ (nghiệm của bài toán chắn thu được ở phần trước) và $$f(x^*)$$ (nghiệm của bài toán ban đầu) là bao nhiêu?

Trước hết, ta có hai bất đẳng thức sau.

>$$
>\begin{align}
>f(x^*) &\ge f(x^*(t)) + \nabla f(x^*(t))^T (x^* - x^*(t)) \\\\
>h_i(x^*) &\ge h_i(x^*(t)) + \nabla h_i(x^*(t))^T (x^* - x^*(t)), \quad i = 1, \cdots, m
>\end{align}
>$$

Nếu tính lồi được đảm bảo thì hàm luôn nằm trên tiếp tuyến của nó, nên $$f(x^*) \ge f(x^*(t)) + \nabla f(x^*(t))^T (x^* - x^*(t))$$ đúng. (Tiếp tuyến là xấp xỉ Taylor bậc nhất.)

Tương tự, vì $$h_i(x^*) \ge h_i(x^*(t)) + \nabla h_i(x^*(t))^T (x^* - x^*(t))$$ đúng, ta suy ra:

$$
h_i(x^*(t)) - h_i(x^*) \le \nabla h_i(x^*(t))^T (x^*(t) - x^*), \quad i = 1, \cdots, m
$$

## Suy ra khoảng cách dưới tối ưu

Hãy dùng hai bất đẳng thức này để suy ra khoảng cách dưới tối ưu. Vế phải được suy ra từ hai điều kiện lồi ở trên.

$$
\begin{align}
f(x^*(t)) - f(x^*) + \sum_{i=1}^{m} u_i(t) (h_i(x^*(t)) - h_i(x^*) ) &\le \left\langle \nabla f(x^*(t)) + \sum_{i=1}^{m} u_i(t) \nabla h_i(x^*(t)), \quad x^*(t) - x^* \right\rangle \\\\
&= \left\langle -tA^Tv, \quad x^*(t) - x^* \right\rangle \\\\
\end{align}
$$

Nếu xem vế phải của bất đẳng thức này như một tích vô hướng, vì $$Ax^*(t) = b$$ và $$Ax^* = b$$ nên toàn bộ số hạng này bằng 0.

Do đó, chuyển số hạng thứ ba của vế trái sang vế phải và rút gọn, ta được kết quả sau:

$$
\begin{align}
f(x^*(t)) - f(x^*) &\le - \sum_{i=1}^{m} u_i(t) (h_i(x^*(t)) - h_i(x^*) ) \\\\
&= \frac{m}{t} + \sum_{i=1}^{m} u_i(t) h_i(x^*) \\\\
&\le \frac{m}{t}
\end{align}
$$

Số hạng thứ nhất ở dòng thứ hai bằng $$\frac{m}{t}$$ vì từ điều kiện KKT ta có $$u_i(t) \cdot h_i(x^*(t)) = - \frac{1}{t}$$.

Số hạng thứ hai có thể bỏ đi vì từ điều kiện KKT ta có $$\sum_{i=1}^{m} u_i(t) h_i(x^*) \le 0$$.

Kết quả là ta thu được khoảng cách dưới tối ưu sau đây, và nó là một tiêu chí dừng hữu ích cho bài toán này. Lưu ý rằng khoảng cách đối ngẫu (duality gap) cũng có thể được suy ra ở chương sau.

>$$
>\begin{align}
>f(x^*(t)) - f(x^*) \le \frac{m}{t}
>\end{align}
>$$
