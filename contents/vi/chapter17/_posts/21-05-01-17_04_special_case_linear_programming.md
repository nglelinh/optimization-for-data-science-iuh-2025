---
layout: post
title: '17-04 Trường hợp đặc biệt: quy hoạch tuyến tính'
chapter: '17'
order: 8
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---

Trong phần này, hãy xem một ví dụ về phương pháp gốc-đối ngẫu cho bài toán LP (quy hoạch tuyến tính).

## Quy hoạch tuyến tính
Xét bài toán LP gốc sau.
>$$
>\begin{align}
>    &\min_{x} && {c^Tx} \\\\
>    &\text{subject to } && {Ax = b} \\\\
>    & &&{x ≥ 0} \\\
>\end{align}
>$$
>
> $$\text{với } c ∈R^n, A ∈R^{m×n}, b ∈R^m$$


Bài toán đối ngẫu của bài toán LP gốc ở trên như sau.
>$$
>\begin{align}
>    &\max_{y,s}  && {b^Ty} \\\\
>    &\text{subject to } && {A^Ty + s = c} \\\\
>    & &&{s ≥ 0} \\\
>\end{align}
>$$


## Điều kiện tối ưu và phương trình đường trung tâm
Sau đây là các điều kiện tối ưu (điều kiện KKT) cho bài toán gốc-đối ngẫu của LP ở trên.
> $$
> \begin{array}{rcl}
> A^Ty + s & = & c \\\
> Ax & = & b \\\
> XS\mathbb{1} & = & 0 \\\
> x,s  & \succeq & 0
> \end{array}
> $$


Phương trình đường trung tâm
> $$
> \begin{array}{rcl}
> A^Ty + s & = & c \\\
> Ax & = & b \\\
> XS\mathbb{1} & = & τ\mathbb{1} \\\
> x,s  & > & 0
> \end{array}
> $$


## Phương pháp gốc-đối ngẫu so với phương pháp chắn
### Các bước Newton của phương pháp gốc-đối ngẫu
Sau đây là phương trình Newton của phương pháp gốc-đối ngẫu cho bài toán LP.

> $$\begin{bmatrix}
0 & A^T & I \\\
A & 0 & 0 \\\
S & 0 & X 
\end{bmatrix}
\begin{bmatrix}
∆x \\\
∆y \\\
∆s 
\end{bmatrix}= −
\begin{bmatrix}
A^Ty + s−c \\\
Ax−b \\\
XS\mathbb{1}−τ\mathbb{1} 
\end{bmatrix}$$

Từ điều kiện tối ưu, ta biết được quan hệ sau.

$$XS\mathbb{1} = \tau \mathbb{1} \iff s = \tau X^{−1}\mathbb{1} \iff x = \tau S^{−1}\mathbb{1}$$

Theo đó, ta có thể thu được điều kiện tối ưu của bài toán chắn gốc bằng cách khử $$s$$, hoặc thu được điều kiện tối ưu của bài toán chắn đối ngẫu bằng cách khử $$x$$.

### Các bước Newton cho các bài toán chắn
Sau đây là các phương trình đường trung tâm gốc và đối ngẫu cho bài toán chắn. (Bên trái là gốc, bên phải là đối ngẫu)
> $$
> \begin{array}{rcr}
> A^Ty + τX^{−1}1 & = & c & \qquad \qquad & A^Ty + s & = & c \\\
> Ax & = & b & \qquad \qquad & τAS^{−1}\mathbb{1} & = & b\\\
> x & > & 0 & \qquad \qquad & s & > & 0
> \end{array}
> $$
> 

Sử dụng các phương trình đường trung tâm ở trên, các bước Newton cho bài toán gốc và đối ngẫu như sau.

**Bước Newton gốc**
> $$\begin{bmatrix}
τX^{−2} & A^T \\\
A & 0
\end{bmatrix}
\begin{bmatrix}
∆x \\\
∆y
\end{bmatrix}= −
\begin{bmatrix}
A^Ty + τX^{−1}\mathbb{1}−c \\\
Ax−b 
\end{bmatrix}$$ 

**Bước Newton đối ngẫu**
> $$\begin{bmatrix}
A^T & I \\\
0 & τAS^{−2}
\end{bmatrix}
\begin{bmatrix}
∆y \\\
∆s
\end{bmatrix}= −
\begin{bmatrix}
A^Ty + s −c \\\
τAS^{−1}\mathbb{1}−b
\end{bmatrix}$$ 


## Ví dụ: phương pháp chắn so với phương pháp gốc-đối ngẫu
### LP chuẩn: $$n = 50$$, $$m = 100$$
Để kiểm chứng hiệu năng của phương pháp gốc-đối ngẫu, hãy xem ví dụ về một bài toán LP chuẩn với $$n = 50$$ biến và $$m = 100$$ ràng buộc đẳng thức. (Ví dụ từ B & V 11.3.2 và 11.7.4)

Phương pháp chắn dùng nhiều giá trị $$\mu$$ khác nhau (2, 50, 150) trong khi phương pháp gốc-đối ngẫu cố định $$\mu$$ bằng 10.
Cả hai phương pháp đều dùng $$\alpha = 0.01, \beta = 0.5$$.


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter17/barrier_vs_primal_dual.png">
  <figcaption style="text-align: center;">[Hình 1] Khoảng cách đối ngẫu (phương pháp chắn so với gốc-đối ngẫu) [1]</figcaption>
</p>
</figure>

Như có thể thấy từ đồ thị, phương pháp gốc-đối ngẫu hội tụ nhanh đồng thời cho độ chính xác cao.

### Chuỗi bài toán: $$n = 2m$$ với $$n$$ tăng dần
Bây giờ hãy xem hiệu năng đối với một dãy bài toán có $$n = 2m$$ và $$n$$ tăng dần.

* Phương pháp chắn dùng $$\mu = 100$$ và vòng lặp ngoài chỉ thực hiện khoảng 2 lần. (Khoảng cách đối ngẫu được giảm xuống $$10^4$$)
* Phương pháp gốc-đối ngẫu dùng $$\mu = 10$$ và dừng khi khoảng cách đối ngẫu và khoảng cách khả thi xấp xỉ $$10^{-8}$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter17/barrier_vs_primal_dual2.png">
  <figcaption style="text-align: center;">[Hình 2] Số vòng lặp Newton (phương pháp chắn so với gốc-đối ngẫu) [1]</figcaption>
</p>
</figure>

Như có thể thấy từ hình trên, phương pháp gốc-đối ngẫu tìm nghiệm với độ chính xác cao hơn nhưng cần thêm một số vòng lặp.

### Gốc - đối ngẫu trong 18 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/primal-dual-ipm_vi.mp4"></video>
</div>

Phương pháp rào cản định tâm lại sau mỗi lần cập nhật $$t$$; phương pháp gốc - đối ngẫu chỉ thực hiện một bước Newton trên các điều kiện KKT nhiễu theo $$(x,\lambda)$$ và thu hẹp khoảng cách đối ngẫu với ít bước hơn nhiều.

### Tự tay thử: gốc - đối ngẫu so với rào cản

<div class="opx-explainer" data-opx="pdipm" data-lang="vi"></div>
