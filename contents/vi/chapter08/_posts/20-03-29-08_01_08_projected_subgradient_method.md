---
layout: post
title: '08-01-08 Phương pháp Subgradient có Chiếu'
chapter: '08'
order: 10
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Phương pháp được mô tả trong ví dụ trước được gọi là phương pháp subgradient có chiếu. Thuật toán này có thể được sử dụng cho các bài toán lồi có ràng buộc.

Nếu chúng ta ký hiệu miền thỏa mãn các ràng buộc là tập $$C$$, thì bài toán lồi có ràng buộc được định nghĩa như sau:

>
$$ \begin{align}
\min_x \text{ }f(x) \quad \text{với điều kiện } x \in C
\end{align} $$

Bằng cách sử dụng phương pháp subgradient có chiếu, các bài toán như vậy có thể được giải tương đối dễ dàng. Phương pháp subgradient có chiếu tương tự như phương pháp subgradient chuẩn, nhưng ở mỗi lần lặp, kết quả được chiếu lên tập $$C$$.

>
$$ \begin{align}
x^{(k)} = P_c(x^{(k-1)} - t_k \cdot g^{(k-1)}), \quad k = 1,2,3,...
\end{align} $$

Nếu phép chiếu có thể thực hiện được, phương pháp này có cùng tính chất hội tụ và tốc độ như phương pháp subgradient.

Một điều cần lưu ý về phương pháp subgradient có chiếu là ngay cả khi $$C$$ là một tập lồi đơn giản, nếu phép toán chiếu $$P_c$$ khó thực hiện, thì bài toán tổng thể cũng trở nên khó giải. Thông thường, các tập $$C$$ sau đây tương đối dễ chiếu lên:

- Ảnh affine: {$$Ax=b : x \in \mathbb{R}^{n}$$}
- Tập nghiệm của hệ tuyến tính: {$$x: Ax=b$$}
- Trực giao không âm: $$\mathbb{R}_+^{n} =  $${$$x: x\ge 0$$}
- Một số quả cầu chuẩn: {$$x: \lVert x \rVert _p \le 1 $$} với $$p=1,2,\infty$$
- Một số đa diện đơn giản và hình nón đơn giản
