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

**Phương pháp điểm trong gốc-đối ngẫu (Primal-dual interior-point method)** là phương pháp tìm nghiệm bằng cách đi theo đường trung tâm, tương tự phương pháp chắn. Để làm điều này, nó định nghĩa các điều kiện KKT nhiễu (perturbed KKT conditions) như các hàm phần dư và tìm nghiệm làm chúng bằng không. Phần này nhằm giải thích cách tiếp cận đó.

## Phương trình đường trung tâm
Chuyển vế phải sang vế trái trong các phương trình đường trung tâm đã giải thích ở phần trước [17-01 Điều kiện tối ưu]({% multilang_post_url contents/chapter17/21-05-01-17_01_barrier_method_duality_optimality_revisited %}), ta có thể sắp xếp chúng như sau. (Các điều kiện tối ưu của phương trình đường trung tâm còn được gọi là các điều kiện KKT nhiễu.)
> $$
> \begin{array}{rcl}
> ∇f(x) +∇h(x)u + A^Tv & = & 0 \\\
>  Uh(x) + \tau\mathbb{1}  & = & 0 \\\
> Ax−b & = & 0 \\\
> u,−h(x)  & > & 0
> \end{array}
> $$

Lưu ý rằng độ lệch bù và các ràng buộc bất đẳng thức trong điều kiện KKT của bài toán ban đầu khác với trong các điều kiện KKT nhiễu. Với bài toán ban đầu, $$Uh(x) = 0$$ và $$u,−h(x)  \ge 0$$, nhưng trong các điều kiện KKT nhiễu, $$Uh(x) = - \tau\mathbb{1}$$ và $$u,−h(x)  \gt 0$$.

Các phương trình phi tuyến đã được sắp xếp này, tức các điều kiện KKT nhiễu, có thể được giải bằng cách xấp xỉ chúng thành các phương trình tuyến tính bằng phiên bản tìm nghiệm (root finding) của phương pháp Newton.

## Bước Newton
Bây giờ hãy tìm hiểu phương pháp tìm nghiệm bằng cách xấp xỉ tuyến tính các điều kiện KKT nhiễu. Phương trình điều kiện KKT nhiễu có thể được định nghĩa là hàm phần dư $$r(x, u, v) = 0$$. (Lý do gọi là phần dư là vì các giá trị này phải bằng 0 để đạt tối ưu.)

> $$r(x,u,v) :=
> \begin{bmatrix}
> ∇f(x) +∇h(x)u + A^Tv \\\
> Uh(x) + τ\mathbb{1} \\\
> Ax−b
> \end{bmatrix}, H(x) = \text{Diag}(h(x))$$

Để tìm nghiệm của hàm, xấp xỉ $$r(x, u, v)$$ bằng khai triển Taylor bậc nhất cho ta kết quả sau. (Quá trình này xấp xỉ các phương trình phi tuyến thành phương trình tuyến tính. Thông tin chi tiết xem [14-02-01 Tìm nghiệm]({% multilang_post_url contents/chapter14/2021-03-26-14_01_newton_method %}))
>$$\begin{align}
0 & = r(x + \Delta x, u + \Delta u, v + \Delta v)  \\\\
  & \approx r(x, u, v) + \nabla r(x, u, v) 
\begin{pmatrix}
\Delta x \\\\
\Delta u \\\\
\Delta v \\\\
\end{pmatrix} \\\\
\end{align}$$

Theo đó, hàm $$r(x, u, v)$$ có thể được sắp xếp như sau.

>$$\begin{align}
\nabla r(x, u, v) 
\begin{pmatrix}
\Delta x \\\\
\Delta u \\\\
\Delta v \\\\
\end{pmatrix} = -r(x, u, v) \\\\
\end{align}$$

Lấy đạo hàm $$r(x, u, v)$$ theo $$x, u, v$$ để thu được ma trận Jacobi $$\nabla r(x, u, v)$$ và thay vào phương trình trên, ta được kết quả sau.
> $$\begin{bmatrix}
> \nabla^2f(x) + \sum_i u_i \nabla^2h_i(x) & \nabla h(x) & A^T \\\
>  U \nabla  h(x)^T & H(x) & 0 \\\
> A & 0 & 0
> \end{bmatrix}
> \begin{bmatrix}
> \Delta x \\\
> \Delta u \\\
> \Delta v
> \end{bmatrix} = −r(x,u,v)$$
> trong đó
> $$r(x,u,v) :=
> \begin{bmatrix}
> \nabla f(x) +\nabla h(x)u + A^Tv \\\
> Uh(x) + τ\mathbb{1} \\\
> Ax−b
> \end{bmatrix}, H(x) = \text{Diag}(h(x))$$

Nghiệm $$(\Delta x, \Delta u, \Delta v)$$ của phương trình này là hướng cập nhật cho các biến gốc và đối ngẫu. Lý do phương pháp được giới thiệu trong chương này được gọi là phương pháp điểm trong **gốc-đối ngẫu (Primal-Dual)** là vì nó cập nhật đồng thời các biến gốc và đối ngẫu bằng cách sử dụng các hàm phần dư.
