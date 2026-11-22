---
layout: post
title: '08-02-02 Hội tụ của các Phương pháp Ngẫu nhiên'
chapter: '08'
order: 13
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Giả sử mỗi hàm thành phần $$f_i$$ ($$i = 1,...,m$$) là hàm lồi và liên tục Lipschitz với hằng số $$G$$.

Đối với phương pháp subgradient ngẫu nhiên, ta có hai kết quả hội tụ tương ứng với kích thước bước cố định và kích thước bước giảm dần:

- **Kích thước bước cố định** $$t_k = t$$ ($$k = 1, 2, 3, ...$$):

>$$\text{Đối với cả hai biến thể tuần hoàn và ngẫu nhiên với kích thước bước cố định, ta có:} \\
\begin{align}
\lim_{k\to\infty} f(x_{best}^{(k)}) \le f^{*} + 5m^{2}G^{2}t/2
\end{align}
$$

Trong đó, $$mG$$ là hằng số Lipschitz của hàm tổng $$\sum_{i=1}^{m} f_i$$.

- **Kích thước bước giảm dần**:

>$$\text{Đối với cả hai biến thể tuần hoàn và ngẫu nhiên với kích thước bước giảm dần, ta có:} \\
\begin{align}
\lim_{k\to\infty} f(x_{best}^{(k)}) = f^{*}
\end{align}
$$
