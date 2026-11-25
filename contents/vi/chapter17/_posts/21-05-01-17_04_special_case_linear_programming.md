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

Trong toàn bộ thế giới tối ưu hóa, quy hoạch tuyến tính (LP) là nơi phương pháp điểm trong gốc–đối ngẫu phô diễn vẻ đẹp đại số thuần khiết nhất. Vì hàm mục tiêu tuyến tính có Hessian bằng không ($$\nabla^2 f(x) = 0$$) và ràng buộc bất đẳng thức chỉ đơn giản là $$x \ge 0$$, hệ phương trình Newton khổng lồ với $$2n + m$$ ẩn số có thể được khử gọn thành một hệ phương trình đối xứng xác định dương kích thước chỉ $$m \times m$$ — gọi là **hệ phương trình chuẩn (normal equations)**.

## Bản đồ kiến thức nền: Từ LP dạng chuẩn đến hệ phương trình chuẩn $$AD^2A^T$$

Bốn ý tưởng cốt lõi dưới đây cho thấy vì sao giải LP bằng PD-IPM lại vừa gọn gàng vừa cực nhanh:

- **Đối ngẫu LP dạng chuẩn và biến bù $$s$$:** Viết bài toán gốc $$\min c^T x \text{ s.t. } Ax = b, x \ge 0$$ song song với bài toán đối ngẫu $$\max b^T y \text{ s.t. } A^T y + s = c, s \ge 0$$ giúp điều kiện bù chặt có dạng cực kỳ đối xứng $$x_i s_i = 0$$ (và đường trung tâm là $$XS\mathbf{1} = \tau\mathbf{1}$$).
- **Hệ tuyến tính KKT của LP:** Vì không có số hạng bậc hai từ $$f$$ hay $$h$$, ma trận Jacobi của hệ LP chỉ gồm $$A, A^T, X = \operatorname{diag}(x), S = \operatorname{diag}(s)$$.
- **Khử khối về hệ phương trình chuẩn:** Khử $$\Delta s$$ rồi khử $$\Delta x$$ bằng ma trận tỉ lệ đường chéo $$D^2 = X S^{-1} = \operatorname{diag}(x_i/s_i)$$, ta chỉ cần giải duy nhất một hệ tuyến tính đối xứng xác định dương $$(A D^2 A^T)\Delta y = \text{rhs}$$ bằng phân tích Cholesky thưa!
- **Khác biệt bản chất với phương pháp chắn trên LP:** Khi so sánh hai bước Newton trên cùng một điểm đường trung tâm, bước của phương pháp chắn chỉ cân nhắc đường đi của biến gốc $$x$$, trong khi bước gốc–đối ngẫu tự động cân bằng cả $$x$$ và $$s$$ thông qua tỉ số $$x_i/s_i$$.

### Khung giải thích (nên đọc chậm): Giải tay một bước PD-IPM cho LP bằng hệ phương trình chuẩn $$AD^2A^T$$

Xét bài toán LP 2 biến với $$m = 1$$ ràng buộc đẳng thức:

$$\min_{x_1, x_2} \; 2x_1 + 3x_2 \qquad \text{với điều kiện} \qquad x_1 + x_2 = 1, \; x_1, x_2 \ge 0.$$

Ở đây $$c = (2, 3)^T$$, $$A = [1, \; 1]$$, $$b = 1$$. Nghiệm tối ưu là $$x^\star = (1, 0)^T, y^\star = 2, s^\star = (0, 1)^T$$. Xét điểm trong khả thi ban đầu $$x = (0.5, 0.5)^T$$, $$y = 0$$, $$s = c - A^T y = (2, 3)^T$$ (nên $$r_p = Ax - b = 0$$ và $$r_d = A^T y + s - c = 0$$). Chọn $$\tau = 0.25$$:

1. **Tính phần dư trung tâm:**
   $$r_c = XS\mathbf{1} - \tau\mathbf{1} = \begin{bmatrix} (0.5)(2) - 0.25 \\ (0.5)(3) - 0.25 \end{bmatrix} = \begin{bmatrix} 0.75 \\ 1.25 \end{bmatrix}.$$
2. **Lập ma trận tỉ lệ đường chéo $$D^2 = X S^{-1}$$:**
   $$D^2 = \operatorname{diag}\!\left(\frac{0.5}{2}, \; \frac{0.5}{3}\right) = \operatorname{diag}\!\left(\frac{1}{4}, \; \frac{1}{6}\right).$$
3. **Giải hệ phương trình chuẩn $$1 \times 1$$ tìm $$\Delta y$$:**
   - Vế trái: $$A D^2 A^T = [1, 1] \begin{bmatrix} 1/4 & 0 \\ 0 & 1/6 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \end{bmatrix} = \frac{1}{4} + \frac{1}{6} = \frac{5}{12}$$.
   - Với $$r_p = 0, r_d = 0$$, vế phải của hệ chuẩn là $$A S^{-1} r_c = \frac{0.75}{2} + \frac{1.25}{3} = \frac{3}{8} + \frac{5}{12} = \frac{19}{24}$$.
   - Suy ra $$\Delta y = \frac{19/24}{5/12} = \frac{19}{10} = 1.9$$.
4. **Thế ngược tìm $$\Delta s$$ và $$\Delta x$$:**
   - $$\Delta s = -A^T \Delta y = (-1.9, \; -1.9)^T \implies s + \Delta s = (0.1, \; 1.1)^T > 0$$!
   - $$\Delta x = -S^{-1}(r_c + X\Delta s) = -\begin{bmatrix} (0.75 - 0.95)/2 \\ (1.25 - 0.95)/3 \end{bmatrix} = \begin{bmatrix} +0.1 \\ -0.1 \end{bmatrix} \implies x + \Delta x = (0.6, \; 0.4)^T > 0$$!
   Kiểm tra lại: $$x_1^+ + x_2^+ = 1.0$$, $$A^T y^+ + s^+ = (2, 3)^T = c$$, và khoảng cách đối ngẫu $$x^T s$$ sụt ngay từ $$2.5$$ xuống còn $$(0.6)(0.1) + (0.4)(1.1) = 0.50$$ chỉ sau 1 bước duy nhất!

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

### Gốc - đối ngẫu so với phương pháp rào cản (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/primal-dual-ipm_vi.mp4"></video>
</div>

Phương pháp rào cản phải định tâm lại sau mỗi lần cập nhật $$t$$; trong khi đó, phương pháp gốc – đối ngẫu chỉ thực hiện một bước Newton trên hệ điều kiện KKT bị nhiễu theo $$(x,\lambda)$$ và thu hẹp khoảng cách đối ngẫu với ít bước hơn đáng kể.

### Tự tay thử: gốc - đối ngẫu so với rào cản

<div class="opx-explainer" data-opx="pdipm" data-lang="vi"></div>
