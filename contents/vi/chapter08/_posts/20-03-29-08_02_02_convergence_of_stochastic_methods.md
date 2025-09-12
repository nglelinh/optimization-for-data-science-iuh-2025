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

Giả sử mỗi hàm $$f_i, i = 1,...,m$$ là lồi và liên tục Lipschitz với hằng số G.

Đối với phương pháp subgradient ngẫu nhiên, các tính chất sau đây đúng cho kích thước bước cố định và giảm dần:

- **Kích thước bước cố định** với $$t_k = t$$, $$k = 1, 2, 3, ...$$

>$$\text{Đối với phương pháp tuần hoàn và ngẫu nhiên với kích thước bước cố định, điều sau đây đúng:} \\
\begin{align}
\lim_{k\to\infty} f(x_{best}^{(k)}) \le f^{*} + 5m^{2}G^{2}t/2
\end{align}
$$

Ở đây, $$mG$$ là hằng số Lipschitz của $$\sum_{i=1}^{m} f_i$$.

- **Kích thước bước giảm dần**

>$$\text{Đối với phương pháp tuần hoàn và ngẫu nhiên với kích thước bước giảm dần, điều sau đây đúng:} \\
\begin{align}
\lim_{k\to\infty} f(x_{best}^{(k)}) = f^{*}
\end{align}
$$

