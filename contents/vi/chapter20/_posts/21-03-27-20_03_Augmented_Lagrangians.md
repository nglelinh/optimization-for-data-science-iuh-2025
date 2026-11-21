---
layout: post
title: '20-03 Augmented Lagrangian'
chapter: '20'
order: 7
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

Nhược điểm của dual ascent là cần điều kiện mạnh để đảm bảo hội tụ. (Để đảm bảo hội tụ, $$f$$ phải lồi mạnh.) Nhược điểm này có thể được khắc phục bằng **phương pháp augmented Lagrangian** (còn gọi là **phương pháp nhân tử, method of multipliers**).

Ta biến đổi bài toán gốc như sau.
>\begin{equation}
\min_x f(x) + \frac{\rho}{2} \lVert Ax - b \rVert _2^2 \quad \text{ subject to } \quad Ax = b
\end{equation}

Ở đây $$\rho > 0$$. Nếu $$A$$ có hạng cột đầy đủ thì hàm mục tiêu lồi mạnh. Bài toán mới tương đương chính xác với bài toán ban đầu (số hạng bổ sung $$Ax - b$$ bằng không tại mọi điểm khả thi).

## Phương pháp Augmented Lagrangian
**Dual gradient ascent** trên bài toán này lặp lại các bước sau với $$k=1,2,3,\dots$$
> $$
> \begin{alignat}{1}
> x^{(k)} & \in \arg\min_x f(x) + (u^{(k-1)})^T A x + \frac{\rho}{2} \lVert Ax - b \rVert_2^2  \\
> u^{(k)} & = u^{(k-1)} + \rho (A x^{(k)} - b)
> \end{alignat}
> $$

Trong thuật toán đối ngẫu này, $$\rho$$ đóng vai trò kích thước bước, tức là $$t_k=\rho$$. Để thấy lý do, hãy xét phần sau.

#### Vì sao $$\rho$$ là kích thước bước phù hợp

Vì $$x^{(k)}$$ cực tiểu hóa $$f(x) + (u^{(k-1)})^T Ax + \frac{\rho}{2} \lVert Ax - b\rVert _2^2$$,
điều kiện dừng nói rằng subgradient của hàm mục tiêu tại $$x^{(k)}$$ phải chứa $$0$$:

> $$
> \begin{alignat}{1}
> 0 & \in \partial f(x^{(k)}) + A^T \left( u^{(k-1)} + \rho (A x^{(k)} -b) \right)  \\
>   & = \partial f(x^{(k)}) + A^T u^{(k)}
> \end{alignat}
> $$

Như vậy với cập nhật $$u^{(k)} = u^{(k-1)} + \rho (A x^{(k)} - b)$$, $$x^{(k)}$$ cực tiểu hóa chính xác hàm Lagrange $$f(x) + (u^{(k)})^T A x$$ như điều kiện dừng đối ngẫu yêu cầu. Dưới các điều kiện thích hợp, $$Ax^{(k)}-b$$ tiến về $$0$$, nên các điểm lặp trở nên khả thi, các điều kiện KKT cuối cùng được thỏa mãn, và $$x^{(k)}$$, $$u^{(k)}$$ tiến đến tối ưu.

Ưu điểm của **phương pháp augmented Lagrangian** là hội tụ tốt hơn nhiều; nhược điểm là mất tính phân rã được của bài toán.
