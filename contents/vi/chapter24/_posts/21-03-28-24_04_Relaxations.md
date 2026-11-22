---
layout: post
title: 24-04 Nới Lỏng
chapter: '24'
order: 5
owner: YoungJae Choung
categories:
- chapter24
lang: vi
---

Mục này trình bày định nghĩa tổng quát của phép nới lỏng (relaxation) cùng hai phương pháp phổ biến để tạo cận dưới cho quy hoạch nguyên: nới lỏng lồi (convex relaxation) và nới lỏng Lagrange (Lagrangian relaxation).

## Điều kiện của phép nới lỏng

Xét bài toán tối ưu gốc:
> $$\min_{x \in X} f(x)$$

Một bài toán tối ưu khác có dạng sau được gọi là một *nới lỏng* của bài toán gốc:

> $$\begin{align}
> &\min_{x \in Y} \: g(x)\\\\
> &\text{sao cho}\\\\
> &\text{① } X \subseteq Y \quad \text{và}\\\\ 
> &\text{② } g(x) \leq f(x) \text{ với mọi } x \in X 
> \end{align}$$ 

Nếu hàm mục tiêu $$g(x)$$ trùng với $$f(x)$$ thì chỉ cần thỏa mãn điều kiện ①; nếu $$g(x)$$ khác $$f(x)$$ thì phải thỏa mãn cả hai điều kiện. Từ hai điều kiện này, giá trị tối ưu của bài toán nới lỏng luôn là một cận dưới của giá trị tối ưu của bài toán gốc.

## Nới lỏng lồi

Với bài toán quy hoạch nguyên hỗn hợp:
> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } && x \in C \\\\
> &&&x_j \in \mathbb{Z}, \quad j \in J
> \end{align} $$
> $$\begin{align}
> \text{trong đó } f \text{ lồi, } f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \subseteq \mathbb{R}^n 
> \quad \text{và} \quad J \subseteq \lbrace 1, \dotsc, n \rbrace
> \end{align}
> $$

bài toán nới lỏng lồi thu được bằng cách bỏ các ràng buộc nguyên $$x_j \in \mathbb{Z}$$:
> $$
> \begin{align}
> &\min_{x} && f(x) \\\\
> &\text{subject to } && x \in C
> \end{align} $$
> $$\begin{align}
> \text{trong đó } f \text{ lồi, } f: \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \subseteq \mathbb{R}^n.
> \end{align}
> $$

## Nới lỏng Lagrange

Xét bài toán có thêm ràng buộc tuyến tính $$Ax \leq b$$ bên cạnh tập ràng buộc $$X$$ (có thể chứa cả các ràng buộc nguyên):

> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } &&Ax \leq b \\\\
> &&& x_{j} \in \mathbb{Z}, \quad x \in X 
> \end{align}
> $$

Đưa ràng buộc $$Ax \leq b$$ lên hàm mục tiêu với nhân tử Lagrange $$u \geq 0$$, ta thu được hàm đối ngẫu Lagrange:

> $$
> \begin{align}
> L(u) = &\min_{x} &&f(x) + u^{\top}(Ax-b) \\\\
> &\text{subject to } &&x \in X
> \end{align}
> $$

Phép nới lỏng này mở rộng tập khả thi, và với mọi $$x$$ thỏa mãn $$Ax \leq b$$ cùng $$u \geq 0$$, ta luôn có $$f(x) + u^{\top}(Ax - b) \leq f(x)$$. Vì vậy $$L(u)$$ là một cận dưới hợp lệ với mọi $$u \geq 0$$. Cận dưới chặt nhất thu được bằng cách giải bài toán đối ngẫu Lagrange $$\max_{u \geq 0} L(u)$$. Do $$L(u)$$ là cận dưới theo từng điểm của một họ hàm affine theo $$u$$, $$L(u)$$ luôn là hàm lõm, nên bài toán đối ngẫu là bài toán cực đại hóa hàm lõm (tương đương tối ưu lồi).

Áp dụng nới lỏng Lagrange cho bài toán đặt cơ sở ở mục 24-02 bằng cách nới lỏng ràng buộc đẳng thức $$\sum_j x_{ij} = 1$$ với nhân tử không ràng buộc dấu $$v$$:

> $$
> \begin{align}
> L(v) = &\min_{x, y} && \sum_{j = 1}^{n} f_{j}y_{j} + \sum_{i = 1}^{m}\sum_{j = 1}^{n}(c_{ij} - v_{i})x_{ij} + \sum_{i = 1}^{m} v_{i} \\\\
> &\text{subject to } && x_{ij} \leq y_{j}, \quad i = 1, \dotsc, m, \quad j = 1, \dotsc, n \\\\
> &&& x_{ij}, y_{j} \in \lbrace 0, 1 \rbrace, \quad i = 1, \dotsc, m, \quad j = 1, \dotsc, n 
> \end{align}
> $$

Với mỗi vector $$v$$ cố định, bài toán con $$L(v)$$ có nghiệm dạng đóng rất dễ tính:
> $$ x_{ij}(v) =\begin{cases}1 & \text{nếu } c_{ij} - v_{i} < 0 \text{ và } \sum_{l} (c_{lj} - v_{l})^{-} + f_{j} < 0 \\\\
> 0 & \text{ngược lại,} \end{cases}$$
> $$ y_{j}(v) =\begin{cases}1 & \text{nếu } \sum_{l} (c_{lj} - v_{l})^{-} + f_{j} < 0 \\\\
> 0 & \text{ngược lại.} \end{cases} $$

Cách giải này vừa cung cấp cận dưới $$L(v)$$ vừa gợi ý nghiệm gốc heuristic. Để tìm cận dưới tốt nhất, ta có thể chuyển $$\max_{v} L(v)$$ thành $$\min_{v} -L(v)$$ và giải bằng phương pháp dưới đạo hàm (subgradient method).
