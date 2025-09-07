---
layout: post
title: 04-05 Biến đổi và thay đổi biến
chapter: '04'
order: 6
owner: YoungJae Choung
categories:
- chapter04
lang: vi
---
Phần này thảo luận về các biến đổi và thay đổi biến trong các bài toán tối ưu hóa lồi, hữu ích cho việc đơn giản hóa hoặc tái công thức hóa bài toán.

Hàm mục tiêu hoặc các hàm ràng buộc có thể được sửa đổi trong khi vẫn bảo toàn bài toán tối ưu hóa đã cho, và đôi khi điều này có thể được sử dụng để khám phá "tính lồi ẩn" của bài toán.

### Định lý 1
Khi hàm $$h : \mathbb{R} \rightarrow \mathbb{R}$$ là một biến đổi đơn điệu tăng, mối quan hệ sau được thỏa mãn:

>$$
>\begin{align}
>   &\text{min}_{x} f(x) \text{ subject to } x \in C \\
>   \Longleftrightarrow \quad &\text{min}_{x} h(f(x)) \text{ subject to } x \in C
>\end{align}
>$$

### Định lý 2
Nếu hàm $$\phi: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$$ là hàm tương ứng một-một và ảnh của $$\phi$$ bao phủ tập khả thi $$C$$, thì các biến của bài toán tối ưu hóa có thể được thay đổi như sau:   

>$$
>\begin{align}
>    &\min_{x} f(x) \text{ subject to } x \in C \\\\ 
>    \Longleftrightarrow \quad &\min_{y} f(\phi(y)) \text{ subject to } \phi(y) \in C
>\end{align}
>$$

### Ví dụ: quy hoạch hình học

Một hàm $$f: \mathbb{R}_{++}^n \rightarrow \mathbb{R}$$ có dạng sau được gọi là **đơn thức** (monomial):
> $$f(x) = \gamma x_{1}^{a_{1}} x_{2}^{a_{2}} \dotsb x_{n}^{a_{n}} \text{ với } \gamma > 0, a_{1}, \dotsc, a_{n} \in \mathbb{R}.$$


Ngoài ra, tổng của các đơn thức được gọi là **đa thức dương** (posynomial):
> $$g(x) = \sum_{k=1}^{p} \gamma_{k} x_{1}^{a_{k1}} x_{2}^{a_{k2}} \dotsb x_{n}^{a_{kn}} \text{ với } \gamma > 0, a\_1, \dotsc, a_{n} \in \mathbb{R}.$$


Một **chương trình hình học** được định nghĩa dưới dạng sau và là một bài toán không lồi:
>$$
\begin{align}
&\min_{x} &&f(x) \\
&\text{subject to } &&g_{i}(x) \leq 1, i = 1, \dotsc, m\\
&&&h_{j}(x) = 1, j = 1, \dotsc, r,\\\\
\end{align}\\
$$

>trong đó $$f$$, $$g_{i}, i=1, \dotsc, m$$ là các đa thức dương và $$h_{j}, j=1, \dotsc, r$$ là các đơn thức.

Hãy chứng minh rằng một chương trình hình học tương đương với một bài toán lồi nào đó.

### Chứng minh:
>Đối với $$f(x) = \gamma x_{1}^{a_{1}} x_{2}^{a_{2}} \dotsb x_{n}^{a_{n}}$$, nếu chúng ta đặt $$y_{i} = \log x_{i}$$ và $$b = \log \gamma$$, thì $$f$$ có thể được biến đổi như sau, và theo **Định lý 2**, điều này bảo toàn bài toán tối ưu hóa đã cho một cách tương đương:
>$$\gamma (e^{y_{1}})^{a_{1}} (e^{y_{2}})^{a_{2}} \dotsb (e^{y_{n}})^{a_{n}} = e^{a^Ty + b}$$
>
>Ngoài ra, một đa thức dương có thể được biểu diễn như $$\sum_{k=1}^{p} e^{a_{k}^{Ty} + b_{k}}$$.
>
>Tại thời điểm này, theo **Định lý 1**, dạng logarit $$\log \big( \sum_{k=1}^{p} e^{a_{k}^{Ty} + b_{k}} \big)$$ cũng có thể bảo toàn bài toán tối ưu hóa một cách tương đương.
>
>Tức là, chương trình hình học tương đương với bài toán sau, đây là một bài toán lồi:
>
>$$
>\begin{align}
&\min_{x} \quad &&{log \big( \sum_{k=1}^{p_{0}} e^{a_{0k}^{Ty} + b_{0k}} \big)} \\
&\text{subject to} &&{
         log \big( \sum_{k=1}^{p_{i}} e^{a_{ik}^{Ty} + b_{ik}} \big)
         \leq 0
         , \quad i = 1, \dotsc, m
}\\
&&&c_{j}^{Ty} + d_{j} = 0, \quad j = 1, \dotsc, r\\\\
\end{align}
$$
