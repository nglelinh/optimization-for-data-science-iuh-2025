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

Để nới lỏng, cần thỏa mãn các điều kiện cụ thể, và có thể dùng các phương pháp nới lỏng lồi (convex relaxation) và nới lỏng Lagrange (Lagrangian relaxation). Hãy xem nội dung chi tiết.

## Điều kiện của nới lỏng
Nếu một bài toán tối ưu tổng quát được định nghĩa như sau:
> $$\min_{x \in X} f(x)$$

Nới lỏng của bài toán này được định nghĩa như sau khi biểu diễn dưới dạng một bài toán tối ưu bất kỳ:

> $$\begin{align}
> &\min_{x \in Y} \: g(x)\\\\
> &\text{sao cho}\\\\
> &\text{① } X \subset Y \quad \text{ and}\\\\ 
> &\text{② } g(x) \leq f(x) \text{ với mọi } x \in X 
> \end{align}$$ 

Nếu các hàm mục tiêu $$f(x)$$ và $$g(x)$$ khác nhau thì phải thỏa mãn cả hai điều kiện, còn nếu chúng giống nhau thì chỉ cần thỏa mãn điều kiện ①.
Nhờ hai điều kiện này, giá trị tối ưu của bài toán nới lỏng trở thành cận dưới của giá trị tối ưu của bài toán gốc.

## Nới lỏng lồi
Khi bài toán đã cho như sau:
> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } && x \in C \\\\
> &&&x_j \in \mathbb{Z}, \quad j \in J \\\\
>\end{align} $$
>$$\begin{align}
> \text{trong đó } f \text{ lồi, } f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \subseteq \mathbb{R}^n 
> \quad \text{và} \quad J \subseteq \lbrace 1 \dotsc n \rbrace \\\\
> \end{align}
> $$

nới lỏng lồi có thể biểu diễn như sau:
> $$
> \begin{align}
> &\min_{x} && f(x) \\\\
> &\text{subject to } && x \in C \\\\
>\end{align} $$
>$$\begin{align}
>\text{trong đó } f \text{ lồi, } f: \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \subseteq \mathbb{R}^n 
>\quad \text{và} \quad J \subseteq \lbrace 1 \dotsc n \rbrace \\\\
>\end{align}
>$$


## Nới lỏng Lagrange
Khi $$X$$ lồi và bao gồm cả các ràng buộc nguyên, ta có thể định nghĩa bài toán như sau.

> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } &&Ax \leq b \\\\
> &&& x_{j} \in \mathbb{Z} \quad x \in X 
> \end{align}
> $$

Khi đó, đưa các ràng buộc vào hàm mục tiêu và thực hiện nới lỏng Lagrange với $$u \geq 0$$ nào đó, ta được:

> $$
> \begin{align}
> L(u) = &\min_{x} &&f(x) + u^{\top}(Ax-b) \\\\
> &\text{subject to } &&x \in X
> \end{align}
> $$

Qua dạng Lagrange, tập ràng buộc được mở rộng, và với $$x$$ khả thi thỏa mãn $$Ax \leq b$$, luôn có $$f(x) + u^{\top}(Ax - b) \leq f(x)$$ với $$u \geq 0$$. Do đó $$L(u)$$ là một cận dưới với mọi $$u \geq 0$$, và cận dưới tốt nhất có thể thu được bằng cách giải bài toán đối ngẫu $$\max_{u \geq 0} L(u)$$. Hãy nhớ rằng $$L(u)$$ là cực tiểu theo từng điểm của các hàm affine theo $$u$$ nên là hàm lõm, do đó bài toán đối ngẫu là bài toán tối ưu lõm (cực đại hóa hàm lõm).

Áp dụng nới lỏng Lagrange vào bài toán đặt cơ sở đã nhắc ở trên, với $$v$$ không ràng buộc, bài toán biến đổi thành việc giải biểu thức sau.

> $$
> \begin{align}
> L(v) = &\min_{x, y} && \sum_{j = 1}^{n} f_{j}y_{j} + \sum_{i = 1}^{m}\sum_{j = 1}^{n}(c_{ij} - v_{i})x_{ij} + \sum_{i = 1}^{m} v_{i} \\\\
> &\text{subject to } && x_{ij} \leq y_{j} \quad i = 1 \dotsc m, \quad j = 1 \dotsc n \\\\
> &&& x_{ij}, y_{j} \in \lbrace 0, 1 \rbrace \quad  i = 1 \dotsc m, \quad j = 1 \dotsc n 
> \end{align}
> $$

Với mỗi $$v$$, nới lỏng Lagrange $$L(v)$$ có thể giải dễ dàng:
> $$ x_{ij}(v) =\begin{cases}1 & \text{if} \quad c_{ij} - v_{i} < 0 \quad \text{and}  \quad \sum_{l} (c_{lj} - v_{l})^{-} + f_{j} < 0 \\\\
> 0 & \text{otherwise.} \end{cases}$$
> $$ y_{j}(v) =\begin{cases}1 & \text{if } \quad \sum_{l} (c_{lj} - v_{l})^{-} + f_{j} < 0 \\\\
> 0 & \text{otherwise.} \end{cases} $$

Điều này cho phép ta thu được cận dưới $$L(v)$$ và một nghiệm gốc heuristic. Ngoài ra, nếu dùng dưới vi phân (subdifferential) của $$-L(v)$$ thì việc tính toán cũng dễ hơn. Dùng phương pháp subgradient, ta có thể giải bằng cách chuyển $$\max_{v} L(v)$$ thành $$\min_{v} -L(v)$$.
