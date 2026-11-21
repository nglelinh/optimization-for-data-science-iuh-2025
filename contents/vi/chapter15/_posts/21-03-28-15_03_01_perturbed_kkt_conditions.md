---
layout: post
title: '15-03-01 Điều kiện KKT nhiễu (Perturbed KKT conditions)'
chapter: "15"
order: 8
categories:
- chapter16
lang: vi
---

Nếu suy ra điều kiện KKT từ bài toán chắn và từ bài toán ban đầu, ta được các kết quả sau.
## Điều kiện KKT cho bài toán chắn
Số hạng thứ hai trong điều kiện KKT của bài toán chắn được suy ra từ gradient của hàm chắn logarit.
>
$$\begin{align}
t \nabla f(x^*(t)) - \sum_{i=1}^{m} \frac{1}{h_i(x^*(t))} \nabla h_i(x^*(t)) + A^Tw = 0  \\\ 
 Ax^*(t) = b, \quad h_i(x^*(t)) \lt 0, \quad i = 1, \cdots , m \\\
\end{align}$$

##  Điều kiện KKT cho bài toán ban đầu
Trong điều kiện KKT của bài toán ban đầu, độ lệch bù (complementary slackness) cho $$h_i(x^*) \cdot u_i^* = 0$$, nhưng trên thực tế rất khó biết điều kiện biên này.
>
$$\begin{align}
\nabla f(x^*) + \sum_{i=1}^{m} u_i^* \nabla h_i(x^*) + A^Tv^* = 0 \\\ 
Ax^* = b, \quad h_i(x^*) \le 0, \quad u_i^* \ge 0,   \\\ 
h_i(x^*) \cdot u_i^* = 0,  \quad i = 1, \cdots , m \\\
\end{align}$$


## Định nghĩa lại điều kiện KKT cho bài toán chắn
Vậy mối quan hệ giữa hai bộ điều kiện KKT này là gì?

Trước hết, định nghĩa $$u_i(t)$$ và $$v$$ như sau:
>
$$\begin{align}
u_i(t) = - \frac{1}{t h_i(x^*(t))}, \quad v = \frac{1}{t}w
\end{align}$$

Hãy viết lại các điều kiện KKT cho bài toán chắn.

Nhìn vào bài toán được định nghĩa lại, ta thấy các điều kiện KKT gần như giống hệt với bài toán ban đầu. Trong đó, $$u_i(t) \cdot   h_i(x^*(t)) = - \frac{1}{t}$$ tiến về 0 khi $$t \to \infty$$, khớp với $$h_i(x^*) \cdot u_i^* = 0$$ trong bài toán ban đầu.

>
$$\begin{align}
& \nabla f(x^*(t)) + \sum_{i=1}^{m} u_i(t) \nabla h_i(x^*(t)) + tA^Tv = 0  \\\ 
& Ax^*(t) = b, \quad u_i(t) \cdot   h_i(x^*(t)) = - \frac{1}{t}, \quad h_i(x^*(t)) \lt 0, \quad u_i(t) \gt 0 , \quad i = 1, \cdots , m \\\
\end{align}$$
