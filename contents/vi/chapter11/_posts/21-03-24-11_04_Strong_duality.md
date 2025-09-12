---
layout: post
title: 11-4 Tính đối ngẫu mạnh
chapter: '11'
order: 5
owner: Wontak Ryu
categories:
- chapter11
lang: vi
lesson_type: required
---

Khi một bài toán thỏa mãn $$f^* = g^*$$, điều này được gọi là **tính đối ngẫu mạnh**. **Điều kiện Slater** là một điều kiện đủ cho tính đối ngẫu mạnh.

## Điều kiện Slater: 
Nếu bài toán gốc là lồi và tồn tại ít nhất một $$x \in \mathbb{R}^n$$ khả thi nghiêm ngặt, thì tính đối ngẫu mạnh xảy ra.
>
$$
\begin{equation}
h_1(x)<0,\dots,h_m(x)<0, \text{ and } l_1(x) = 0,\dots,l_r(x) = 0,
\end{equation}
$$

Lưu ý quan trọng: Bất đẳng thức nghiêm ngặt không cần được thỏa mãn khi hàm là affine.
## Ví dụ: Bài toán đối ngẫu Support Vector Machine 
Cho $$y \in \{-1,1\}^n$$, $$X \in \mathbb{R}^{n \times p}$$ (các cột của $$X$$ là $$x_1, ..., x_n$$), bài toán SVM(Support Vector Machine) được định nghĩa như sau:

>
$$
\begin{alignat}{1}
\min_{\beta, \beta_0, \xi} & \quad \frac{1}{2}\parallel\beta\parallel_2^2 + C \sum_{i=1}^n \xi_i   \\\\
                                  s.t. & \quad \xi_i \geq 0, i=1,\dots,n   \\\\
                                       & \quad y_i(x_i^T \beta + \beta_o) \geq 1 - \xi_i, i=1,\dots,n
\end{alignat}
$$

Sử dụng các biến đối ngẫu $$v, w \geq 0$$, hãy định nghĩa hàm Lagrangian:
>
\begin{equation}
L(\beta,\beta_0,\xi,v,w) = \frac{1}{2} \parallel\beta\parallel\_2^2 + C\sum_{i=1}^n \xi_i - \sum_{i=1}^n v_i \xi_i +  \sum_{i=1}^n w_i (1-\xi_i - y_i(x_i^T\beta + \beta_o))
\end{equation}


Tối thiểu hóa theo $$\beta, \beta_0, \xi$$, ta có thể tìm được hàm đối ngẫu Lagrangian như sau:
>
$$
g(v,w) = 
\begin{cases}
-\frac{1}{2} w^T\tilde{X}\tilde{X}^T w +  1^Tw, &\text{if $w=C1-v, w^Ty=0$} \\\\
-\infty, &\text{otherwise}
\end{cases}
$$

Ở đây $$\tilde{X}=\text{diag}(y) X$$. Do đó, bài toán đối ngẫu SVM (sau khi loại bỏ biến slack $$v$$) trở thành: 
>
$$
\begin{alignat}{1}
\max_{w}  & \quad -\frac{1}{2} w^T\tilde{X}\tilde{X}^T w +  1^Tw \\\\
     s.t. &  \quad 0 \leq w \leq C1, w^Ty = 0
\end{alignat}
$$

Vì bài toán gốc thỏa mãn điều kiện Slater, tính đối ngẫu mạnh xảy ra. (Đó là, hàm mục tiêu là lồi và các ràng buộc bất đẳng thức là affine theo $$\beta, \beta_0, \xi$$.)



