---
layout: post
title: '17-02-01 Phương trình đường trung tâm và bước Newton'
chapter: '17'
order: 4
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---

**Phương pháp điểm trong gốc-đối ngẫu (Primal-dual interior-point method)** tìm nghiệm tối ưu bằng cách bám theo đường trung tâm tương tự phương pháp chắn. Để làm điều này, thuật toán biểu diễn các điều kiện KKT bị nhiễu (perturbed KKT conditions) dưới dạng hàm phần dư và tìm nghiệm làm triệt tiêu các phần dư đó. Phần này trình bày chi tiết cách tiếp cận này.

## Phương trình đường trung tâm
Chuyển toàn bộ vế phải sang vế trái trong hệ phương trình đường trung tâm đã nêu ở [17-01 Điều kiện tối ưu]({% multilang_post_url contents/chapter17/21-05-01-17_01_barrier_method_duality_optimality_revisited %}), ta thu được hệ điều kiện KKT bị nhiễu:
> $$
> \begin{array}{rcl}
> \nabla f(x) +\nabla h(x)u + A^Tv & = & 0 \\\
>  Uh(x) + \tau\mathbb{1}  & = & 0 \\\
> Ax-b & = & 0 \\\
> u,-h(x)  & > & 0
> \end{array}
> $$

Lưu ý sự khác biệt giữa điều kiện KKT của bài toán gốc và điều kiện KKT bị nhiễu: ở bài toán gốc ta có điều kiện bù chặt $$Uh(x) = 0$$ và $$u, -h(x) \ge 0$$, còn ở điều kiện KKT bị nhiễu ta có $$Uh(x) = -\tau\mathbb{1}$$ và $$u, -h(x) \gt 0$$.

Hệ phương trình phi tuyến này có thể được giải xấp xỉ ở mỗi bước bằng cách tuyến tính hóa nó thông qua phiên bản tìm nghiệm (root-finding) của phương pháp Newton.

## Bước Newton
Ta định nghĩa hệ ba phương trình đầu tiên là hàm phần dư $$r(x, u, v) = 0$$ (gọi là phần dư vì các đại lượng này cần tiến về $$0$$ tại nghiệm tối ưu):

> $$r(x,u,v) :=
> \begin{bmatrix}
> \nabla f(x) +\nabla h(x)u + A^Tv \\\
> Uh(x) + \tau\mathbb{1} \\\
> Ax-b
> \end{bmatrix}, H(x) = \text{Diag}(h(x))$$

Áp dụng khai triển Taylor bậc nhất để xấp xỉ tuyến tính phương trình $$r(x + \Delta x, u + \Delta u, v + \Delta v) = 0$$ (xem chi tiết tại [14-02-01 Tìm nghiệm]({% multilang_post_url contents/chapter14/2021-03-26-14_01_newton_method %})):
>$$\begin{align}
0 & = r(x + \Delta x, u + \Delta u, v + \Delta v)  \\\\
  & \approx r(x, u, v) + \nabla r(x, u, v) 
\begin{pmatrix}
\Delta x \\\\
\Delta u \\\\
\Delta v \\\\
\end{pmatrix} \\\\
\end{align}$$

Suy ra hệ phương trình tuyến tính xác định bước Newton:

>$$\begin{align}
\nabla r(x, u, v) 
\begin{pmatrix}
\Delta x \\\\
\Delta u \\\\
\Delta v \\\\
\end{pmatrix} = -r(x, u, v) \\\\
\end{align}$$

Tính ma trận Jacobi $$\nabla r(x, u, v)$$ bằng cách lấy đạo hàm riêng của $$r(x, u, v)$$ theo $$x, u, v$$ rồi thay vào hệ trên, ta thu được:
> $$\begin{bmatrix}
> \nabla^2f(x) + \sum_i u_i \nabla^2h_i(x) & \nabla h(x) & A^T \\\
>  U \nabla  h(x)^T & H(x) & 0 \\\
> A & 0 & 0
> \end{bmatrix}
> \begin{bmatrix}
> \Delta x \\\
> \Delta u \\\
> \Delta v
> \end{bmatrix} = -r(x,u,v)$$
> trong đó
> $$r(x,u,v) :=
> \begin{bmatrix}
> \nabla f(x) +\nabla h(x)u + A^Tv \\\
> Uh(x) + \tau\mathbb{1} \\\
> Ax-b
> \end{bmatrix}, H(x) = \text{Diag}(h(x))$$

Nghiệm $$(\Delta x, \Delta u, \Delta v)$$ của hệ tuyến tính này chính là hướng cập nhật cho cả biến gốc và biến đối ngẫu. Chính vì thuật toán cập nhật đồng thời biến gốc và biến đối ngẫu thông qua hàm phần dư nên nó được gọi là phương pháp điểm trong **gốc-đối ngẫu (Primal-Dual)**.
