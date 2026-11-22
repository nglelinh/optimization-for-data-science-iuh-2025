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
Phần này trình bày các kỹ thuật biến đổi hàm và đổi biến trong tối ưu hóa, giúp đơn giản hóa hoặc viết lại bài toán về dạng tương đương thuận lợi hơn.

Bằng cách biến đổi hàm mục tiêu hoặc các hàm ràng buộc mà vẫn giữ nguyên tập nghiệm tương ứng, đôi khi ta có thể phát hiện "tính lồi ẩn" của những bài toán ban đầu trông có vẻ không lồi.

### Định lý 1
Nếu $$h : \mathbb{R} \rightarrow \mathbb{R}$$ là một hàm đơn điệu tăng chặt, thì hai bài toán sau là tương đương:

>$$
>\begin{align}
>   &\min_{x} f(x) \text{ subject to } x \in C \\
>   \Longleftrightarrow \quad &\min_{x} h(f(x)) \text{ subject to } x \in C
>\end{align}
>$$

### Định lý 2
Nếu ánh xạ $$\phi: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$$ là một song ánh (hoặc đơn ánh có ảnh bao phủ tập khả thi $$C$$), thì có thể đổi biến bài toán tối ưu hóa như sau:

>$$
>\begin{align}
>    &\min_{x} f(x) \text{ subject to } x \in C \\\\ 
>    \Longleftrightarrow \quad &\min_{y} f(\phi(y)) \text{ subject to } \phi(y) \in C
>\end{align}
>$$

### Ví dụ: Quy hoạch hình học

Một hàm $$f: \mathbb{R}_{++}^n \rightarrow \mathbb{R}$$ có dạng sau được gọi là **đơn thức dương** (monomial):
> $$f(x) = \gamma x_{1}^{a_{1}} x_{2}^{a_{2}} \dotsb x_{n}^{a_{n}} \text{ với } \gamma > 0, \; a_{1}, \dotsc, a_{n} \in \mathbb{R}.$$

Tổng của các đơn thức dương được gọi là **đa thức dương** (posynomial):
> $$g(x) = \sum_{k=1}^{p} \gamma_{k} x_{1}^{a_{k1}} x_{2}^{a_{k2}} \dotsb x_{n}^{a_{kn}} \text{ với } \gamma_{k} > 0, \; a_{k1}, \dotsc, a_{kn} \in \mathbb{R}.$$

Một **bài toán quy hoạch hình học** (geometric program) được phát biểu như sau (dạng gốc không phải là bài toán lồi):
>$$
\begin{align}
&\min_{x} &&f(x) \\
&\text{subject to } &&g_{i}(x) \leq 1, \quad i = 1, \dotsc, m\\
&&&h_{j}(x) = 1, \quad j = 1, \dotsc, r,\\\\
\end{align}
$$

>trong đó $$f$$ và $$g_{i}$$ ($$i=1, \dotsc, m$$) là các đa thức dương, còn $$h_{j}$$ ($$j=1, \dotsc, r$$) là các đơn thức dương.

Hãy chứng minh rằng mọi bài toán quy hoạch hình học đều tương đương với một bài toán tối ưu hóa lồi.

### Chứng minh
> Với một đơn thức dương $$f(x) = \gamma x_{1}^{a_{1}} x_{2}^{a_{2}} \dotsb x_{n}^{a_{n}}$$, đặt phép đổi biến $$y_{i} = \log x_{i}$$ (tức $$x_i = e^{y_i}$$) và $$b = \log \gamma$$. Theo **Định lý 2**, phép đổi biến này bảo toàn tính tương đương của bài toán và đưa $$f$$ về dạng:
> $$\gamma (e^{y_{1}})^{a_{1}} (e^{y_{2}})^{a_{2}} \dotsb (e^{y_{n}})^{a_{n}} = e^{a^Ty + b}.$$
>
> Tương tự, mỗi đa thức dương trở thành $$\sum_{k=1}^{p} e^{a_{k}^{T}y + b_{k}}$$.
>
> Tiếp theo, áp dụng phép biến đổi đơn điệu tăng chặt $$\log(\cdot)$$ theo **Định lý 1**, ta thu được dạng $$\log \big( \sum_{k=1}^{p} e^{a_{k}^{T}y + b_{k}} \big)$$ mà vẫn giữ nguyên tính tương đương của bài toán.
>
> Như vậy, bài toán quy hoạch hình học ban đầu tương đương với bài toán sau, vốn là một bài toán tối ưu hóa lồi (vì hàm log-sum-exp là hàm lồi và ràng buộc đẳng thức là affine):
>
>$$
\begin{align}
&\min_{y} \quad &&{\log \big( \sum_{k=1}^{p_{0}} e^{a_{0k}^{T}y + b_{0k}} \big)} \\
&\text{subject to} &&{
         \log \big( \sum_{k=1}^{p_{i}} e^{a_{ik}^{T}y + b_{ik}} \big)
         \leq 0
         , \quad i = 1, \dotsc, m
}\\
&&&c_{j}^{T}y + d_{j} = 0, \quad j = 1, \dotsc, r.\\\\
\end{align}
$$
