---
layout: post
title: '15-03-01 Điều kiện KKT nhiễu (Perturbed KKT conditions)'
chapter: "15"
order: 8
categories:
- chapter16
lang: vi
---

So sánh điều kiện KKT của bài toán chắn và bài toán ban đầu cho thấy mối liên hệ chặt chẽ giữa hai bài toán.

## Điều kiện KKT của bài toán chắn
Số hạng thứ hai trong phương trình dừng của bài toán chắn chính là gradient của hàm chắn logarit:
>
$$\begin{align}
t \nabla f(x^*(t)) - \sum_{i=1}^{m} \frac{1}{h_i(x^*(t))} \nabla h_i(x^*(t)) + A^Tw = 0  \\\ 
 Ax^*(t) = b, \quad h_i(x^*(t)) \lt 0, \quad i = 1, \cdots , m \\\
\end{align}$$

## Điều kiện KKT của bài toán ban đầu
Trong điều kiện KKT của bài toán gốc, điều kiện độ lệch bù (complementary slackness) đòi hỏi $$h_i(x^*) \cdot u_i^* = 0$$, nhưng trong thực tế ta khó xác định trước ràng buộc nào đạt dấu bằng trên biên:
>
$$\begin{align}
\nabla f(x^*) + \sum_{i=1}^{m} u_i^* \nabla h_i(x^*) + A^Tv^* = 0 \\\ 
Ax^* = b, \quad h_i(x^*) \le 0, \quad u_i^* \ge 0,   \\\ 
h_i(x^*) \cdot u_i^* = 0,  \quad i = 1, \cdots , m \\\
\end{align}$$

## Viết lại điều kiện KKT của bài toán chắn
Để thấy rõ mối quan hệ giữa hai hệ điều kiện, ta định nghĩa các biến đối ngẫu $$u_i(t)$$ và $$v$$ như sau:
>
$$\begin{align}
u_i(t) = - \frac{1}{t h_i(x^*(t))}, \quad v = \frac{1}{t}w
\end{align}$$

Chia cả hai vế của phương trình dừng trong bài toán chắn cho $$t$$ và thay $$u_i(t)$$, $$v$$ vào, ta thu được hệ điều kiện tương đương:

>
$$\begin{align}
& \nabla f(x^*(t)) + \sum_{i=1}^{m} u_i(t) \nabla h_i(x^*(t)) + A^Tv = 0  \\\ 
& Ax^*(t) = b, \quad u_i(t) \cdot   h_i(x^*(t)) = - \frac{1}{t}, \quad h_i(x^*(t)) \lt 0, \quad u_i(t) \gt 0 , \quad i = 1, \cdots , m \\\
\end{align}$$

Hệ này gần như trùng khớp với điều kiện KKT của bài toán gốc, ngoại trừ điều kiện độ lệch bù bị nhiễu thành $$u_i(t) \cdot h_i(x^*(t)) = - \frac{1}{t}$$. Khi $$t \to \infty$$, vế phải tiến về $$0$$, khôi phục đúng điều kiện $$h_i(x^*) \cdot u_i^* = 0$$ của bài toán ban đầu.
