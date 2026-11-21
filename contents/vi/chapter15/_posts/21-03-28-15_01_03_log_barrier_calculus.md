---
layout: post
title: '15-01-03 Giải tích của hàm chắn logarit'
chapter: "15"
order: 5
owner: "Minjoo Lee"
categories:
- chapter15
lang: vi
---

Gradient và Hessian của hàm chắn logarit như sau.
>
\begin{align}
\phi(x) = - \sum_{i=1}^{m} \log(-h_i(x))
\end{align}

Gradient:
>
\begin{align}
\nabla \phi(x) = - \sum_{i=1}^{m} \frac{1}{h_i(x)} \nabla h_i(x)
\end{align}

Hessian:

>
\begin{align}
\nabla^2 \phi(x) = \sum_{i=1}^{m} \frac{1}{h_i(x)^2} \nabla h_i(x) \nabla h_i(x)^T -  \sum_{i=1}^{m} \frac{1}{h_i(x)} \nabla^2 h_i(x)
\end{align}

## Ví dụ: $$\phi(x) = -\sum_{i=1}^{n} \log(x_i)$$
Nếu tính gradient và Hessian cho hàm chắn $$\phi(x) = -\sum_{i=1}^{n} \log(x_i)$$, ta được kết quả sau.
>
\begin{align}
\phi(x) = -\sum_{i=1}^{n} \log(x_i)
\end{align}
Do đó, $$h_i(x) =  -x_i$$ và $$x_i \ge 0$$.

Gradient:
>
$$
\nabla \phi(x) = - 
\begin{bmatrix}
1/x_1 \\\
\vdots \\\
1/x_n \\\
\end{bmatrix}
 = -X^{-1} \mathbb{1}, \qquad X = \text{diag}(x)$$
 
Hessian:
>
$$
\nabla^2 \phi(x) = 
\begin{bmatrix}
1/x_1^2 & \cdots & \\\
\vdots & \ddots & \vdots  \\\
& \cdots & 1/x_n^2 \\\
\end{bmatrix}
 = X^{-2}$$
