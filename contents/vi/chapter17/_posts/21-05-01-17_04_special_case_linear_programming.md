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

Trong phần này, chúng ta xét áp dụng phương pháp gốc-đối ngẫu cho trường hợp đặc biệt là bài toán quy hoạch tuyến tính (LP).

## Quy hoạch tuyến tính
Xét bài toán LP gốc dạng chuẩn:
>$$
>\begin{align}
>    &\min_{x} && {c^Tx} \\\\
>    &\text{subject to } && {Ax = b} \\\\
>    & &&{x \ge 0} \\\
>\end{align}
>$$
>
> $$\text{với } c \in \mathbb{R}^n, A \in \mathbb{R}^{m\times n}, b \in \mathbb{R}^m$$


Bài toán đối ngẫu tương ứng là:
>$$
>\begin{align}
>    &\max_{y,s}  && {b^Ty} \\\\
>    &\text{subject to } && {A^Ty + s = c} \\\\
>    & &&{s \ge 0} \\\
>\end{align}
>$$


## Điều kiện tối ưu và phương trình đường trung tâm
Hệ điều kiện tối ưu (KKT) cho cặp bài toán LP gốc – đối ngẫu trên là:
> $$
> \begin{array}{rcl}
> A^Ty + s & = & c \\\
> Ax & = & b \\\
> XS\mathbb{1} & = & 0 \\\
> x,s  & \succeq & 0
> \end{array}
> $$


Hệ phương trình đường trung tâm:
> $$
> \begin{array}{rcl}
> A^Ty + s & = & c \\\
> Ax & = & b \\\
> XS\mathbb{1} & = & \tau\mathbb{1} \\\
> x,s  & > & 0
> \end{array}
> $$


## Phương pháp gốc-đối ngẫu so với phương pháp chắn
### Bước Newton của phương pháp gốc-đối ngẫu
Hệ phương trình Newton cho bài toán LP trong phương pháp gốc-đối ngẫu có dạng:

> $$\begin{bmatrix}
0 & A^T & I \\\
A & 0 & 0 \\\
S & 0 & X 
\end{bmatrix}
\begin{bmatrix}
\Delta x \\\
\Delta y \\\
\Delta s 
\end{bmatrix}= -
\begin{bmatrix}
A^Ty + s-c \\\
Ax-b \\\
XS\mathbb{1}-\tau\mathbb{1} 
\end{bmatrix}$$

Từ điều kiện bù nhiễu, ta có quan hệ tương đương:

$$XS\mathbb{1} = \tau \mathbb{1} \iff s = \tau X^{-1}\mathbb{1} \iff x = \tau S^{-1}\mathbb{1}$$

Nhờ đó, ta có thể khử $$s$$ để thu về hệ điều kiện tối ưu của bài toán chắn gốc, hoặc khử $$x$$ để thu về hệ điều kiện tối ưu của bài toán chắn đối ngẫu.

### Bước Newton của phương pháp chắn
Hệ phương trình đường trung tâm cho bài toán chắn gốc (bên trái) và bài toán chắn đối ngẫu (bên phải):
> $$
> \begin{array}{rcr}
> A^Ty + \tau X^{-1}\mathbb{1} & = & c & \qquad \qquad & A^Ty + s & = & c \\\
> Ax & = & b & \qquad \qquad & \tau AS^{-1}\mathbb{1} & = & b\\\
> x & > & 0 & \qquad \qquad & s & > & 0
> \end{array}
> $$
> 

Tuyến tính hóa các phương trình đường trung tâm trên, ta thu được hệ bước Newton cho bài toán gốc và bài toán đối ngẫu:

**Bước Newton gốc**
> $$\begin{bmatrix}
-\tau X^{-2} & A^T \\\
A & 0
\end{bmatrix}
\begin{bmatrix}
\Delta x \\\
\Delta y
\end{bmatrix}= -
\begin{bmatrix}
A^Ty + \tau X^{-1}\mathbb{1}-c \\\
Ax-b 
\end{bmatrix}$$ 

**Bước Newton đối ngẫu**
> $$\begin{bmatrix}
A^T & I \\\
0 & -\tau AS^{-2}
\end{bmatrix}
\begin{bmatrix}
\Delta y \\\
\Delta s
\end{bmatrix}= -
\begin{bmatrix}
A^Ty + s -c \\\
\tau AS^{-1}\mathbb{1}-b
\end{bmatrix}$$ 


## Ví dụ: so sánh phương pháp chắn và phương pháp gốc-đối ngẫu
### Bài toán LP chuẩn: $$n = 50$$, $$m = 100$$
Để so sánh hiệu năng, ta xét ví dụ một bài toán LP chuẩn với $$n = 50$$ biến và $$m = 100$$ ràng buộc (ví dụ từ Boyd & Vandenberghe, mục 11.3.2 và 11.7.4).

Phương pháp chắn được thử với nhiều giá trị $$\mu$$ khác nhau ($$2, 50, 150$$), trong khi phương pháp gốc-đối ngẫu cố định $$\mu = 10$$. Cả hai phương pháp đều sử dụng $$\alpha = 0.01, \beta = 0.5$$.


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter17/barrier_vs_primal_dual.png">
  <figcaption style="text-align: center;">[Hình 1] Khoảng cách đối ngẫu (phương pháp chắn so với gốc-đối ngẫu) [1]</figcaption>
</p>
</figure>

Đồ thị cho thấy phương pháp gốc-đối ngẫu hội tụ nhanh hơn đồng thời đạt độ chính xác cao hơn.

### Chuỗi bài toán: $$n = 2m$$ với $$n$$ tăng dần
Tiếp theo, xét hiệu năng trên một dãy bài toán LP với $$n = 2m$$ khi kích thước $$n$$ tăng dần:

* Phương pháp chắn dùng $$\mu = 100$$ và thực hiện khoảng 2 vòng lặp ngoài (khoảng cách đối ngẫu giảm xuống $$10^{-4}$$).
* Phương pháp gốc-đối ngẫu dùng $$\mu = 10$$ và dừng khi khoảng cách đối ngẫu và sai số khả thi đạt xấp xỉ $$10^{-8}$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter17/barrier_vs_primal_dual2.png">
  <figcaption style="text-align: center;">[Hình 2] Số vòng lặp Newton (phương pháp chắn so với gốc-đối ngẫu) [1]</figcaption>
</p>
</figure>

Như hình trên cho thấy, phương pháp gốc-đối ngẫu đạt độ chính xác cao hơn nhiều dù chỉ cần thêm một lượng nhỏ vòng lặp Newton.

### Gốc - đối ngẫu trong 18 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/primal-dual-ipm_vi.mp4"></video>
</div>

Phương pháp rào cản phải định tâm lại sau mỗi lần cập nhật $$t$$; trong khi đó, phương pháp gốc – đối ngẫu chỉ thực hiện một bước Newton trên hệ điều kiện KKT bị nhiễu theo $$(x,\lambda)$$ và thu hẹp khoảng cách đối ngẫu với ít bước hơn đáng kể.

### Tự tay thử: gốc - đối ngẫu so với rào cản

<div class="opx-explainer" data-opx="pdipm" data-lang="vi"></div>
