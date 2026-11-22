---
layout: post
title: 05-05 Quy Hoạch Bán Xác Định (SDP)
chapter: '05'
order: 11
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
---

Nếu ràng buộc bất đẳng thức tuyến tính trong một bài toán LP tổng quát được thay bằng một **bất đẳng thức ma trận tuyến tính** (Linear Matrix Inequality - LMI), ta thu được **bài toán quy hoạch nửa xác định** (hay *quy hoạch bán xác định*, Semidefinite Programming - SDP).

### Bài toán Quy hoạch Nửa xác định (dạng bất đẳng thức)
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{x_1 F_1 + \dotsb + x_n F_n + G \preceq 0} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&G, F_1, \dotsb, F_n \in \mathbb{S}^{k} \text{ và } A \in \mathbb{R}^{p \times n}.
>\end{align}$$

* Nếu $$G, F_1, \dotsb, F_n$$ đều là các ma trận đường chéo kích thước $$k \times k$$, ràng buộc LMI trên tương đương với $$k$$ bất đẳng thức tuyến tính, và bài toán SDP rút gọn thành một bài toán LP.
* Nhiều ràng buộc LMI có thể gộp thành một LMI duy nhất bằng cách ghép thành các ma trận đường chéo khối:
> $$
> x_1\hat{F_1} + \dotsb + x_n\hat{F_n} + \hat{G} \preceq 0, \quad x_1\tilde{F_1} + \dotsb + x_n\tilde{F_n} + \tilde{G} \preceq 0
> $$
> tương đương với một LMI duy nhất:
> $$
> x_1
> \begin{bmatrix}
>     \hat{F_1} & 0 \\\\
>     0 & \tilde{F_1} \\\\
> \end{bmatrix} + 
> x_2
> \begin{bmatrix}
>     \hat{F_2} & 0 \\\\
>     0 & \tilde{F_2} \\\\
> \end{bmatrix} + 
> \dotsb
> +
> x_n
> \begin{bmatrix}
>     \hat{F_n} & 0 \\\\
>     0 & \tilde{F_n} \\\\
> \end{bmatrix} + 
> \begin{bmatrix}
>     \hat{G} & 0 \\\\
>     0 & \tilde{G} \\\\
> \end{bmatrix}
> \preceq 0
> $$

## SDP ở dạng chuẩn
Bài toán quy hoạch nửa xác định ở dạng chuẩn được biểu diễn theo biến ma trận $$X \in \mathbb{S}^n$$ như sau:

### Bài toán SDP dạng chuẩn
>$$
>\begin{align}
>    &\text{minimize}_{X} &&{\mathrm{tr}(CX)} \\\\
>    &\text{subject to } &&{\mathrm{tr}(A_i X) = b_i, \quad i = 1, \dotsc, m} \\\\
>    & &&{X \succeq 0},\\\\
>    & \text{where } &&C, A_i \in \mathbb{S}^n, \; X \in \mathbb{S}^n.
>\end{align}$$

* Nhắc lại: tích vô hướng Frobenius giữa hai ma trận đối xứng là $$\mathrm{tr}(CX) = \sum_{i,j=1}^n C_{ij}X_{ij}$$.

Mọi bài toán SDP ở dạng bất đẳng thức đều có thể chuyển về SDP dạng chuẩn theo các bước sau:

### Chuyển đổi SDP về dạng chuẩn

**Bước 1.** Đưa thêm ma trận biến phụ $$S \succeq 0$$ để chuyển ràng buộc bất đẳng thức LMI thành ràng buộc đẳng thức:
>$$
>\begin{align}
>    &\text{minimize}_{x, S} &&{c^T x + d} \\\\
>    &\text{subject to } &&{\sum_{l=1}^n F_l x_l+ S = -G} \\\\
>    & &&{Ax = b}\\\\
>    & &&{S \succeq 0}
>\end{align}
>$$

**Bước 2.** Viết lại ràng buộc đẳng thức ma trận ở Bước 1 theo từng phần tử $$(i, j)$$:
>$$
>\begin{align}
>    &\text{minimize}_{x, S} &&{c^T x + d} \\\\
>    &\text{subject to } &&{\sum_{l=1}^n (F_l x_l)_{ij} + S_{ij} = -G_{ij}, \quad i,j = 1, \dotsc, k} \\\\
>    & &&{Ax = b}\\\\
>    & &&{S \succeq 0}
>\end{align}
>$$

**Bước 3.** Tách biến tự do $$x$$ thành hiệu của hai biến không âm:
$$x = x^{+} - x^{-}$$, với $$x^{+} \succeq 0$$ và $$x^{-} \succeq 0$$.
>$$
>\begin{align}
>    &\text{minimize}_{x^{+}, x^{-}, S} &&{c^T (x^{+} - x^{-}) + d} \\\\
>    &\text{subject to } &&{\sum_{l=1}^n (F_l x^{+}_l)_{ij} - \sum_{l=1}^n (F_l x^{-}_l)_{ij} + S_{ij} = -G_{ij}, \quad i,j = 1, \dotsc, k} \\\\
>    & &&{Ax^{+} - Ax^{-} = b}\\\\
>    & &&{S \succeq 0}\\\\
>    & &&{x^{+}, \; x^{-} \succeq 0}.
>\end{align}
>$$

**Bước 4.** Định nghĩa các ma trận đường chéo khối $$X, C, \tilde{A}, \tilde{b}$$ (các ô để trống đều bằng 0):

> $$
> X = 
> \begin{bmatrix}
> \operatorname{diag}(x^{+})\\\\
>  & \operatorname{diag}(x^{-})\\\\
> && S \\\\
> \end{bmatrix}
> , \quad
> C = 
> \begin{bmatrix}
> \operatorname{diag}(c)\\\\
> & -\operatorname{diag}(c) &\\\\
> & & O_{k \times k}\\\\
> \end{bmatrix}
> ,$$
> với các ma trận ràng buộc đối xứng $$P_{ij}$$ (có khối ứng với $$S$$ đặt $$1$$ ở vị trí $$(i,i)$$ nếu $$i=j$$ hoặc $$1/2$$ ở hai vị trí $$(i,j), (j,i)$$ nếu $$i \neq j$$) và
> $$
> Q_{i}= 
> \begin{bmatrix}
> \operatorname{diag}(A_i)\\\\
> &-\operatorname{diag}(A_i)\\\\
> &&O_{k \times k}\\\\
> \end{bmatrix}
> $$
> (trong đó $$A_i$$ là hàng thứ $$i$$ của ma trận $$A$$), sao cho
> $$
> \mathrm{tr}(P_{ij}X) = -G_{ij}, \qquad \mathrm{tr}(Q_i X) = b_i.
> $$
> Gom tất cả các ma trận $$P_{ij}$$ và $$Q_i$$ thành danh sách $$\tilde{A}_1, \dotsc, \tilde{A}_m$$ cùng vectơ vế phải $$\tilde{b}$$ tương ứng.

**Bước 5.** Thay các biểu thức trên vào bài toán ở Bước 3 (bỏ qua hằng số $$d$$), ta thu được dạng chuẩn của SDP:

>$$
>\begin{align}
>    &\text{minimize}_{X} &&{\mathrm{tr}(CX)} \\\\
>    &\text{subject to } &&{\mathrm{tr}(\tilde{A}_i X) = \tilde{b}_i, \quad i = 1, \dotsc, m} \\\\
>    & &&{X \succeq 0}.
>\end{align}
>$$

## Mối quan hệ giữa SOCP và SDP
Nhờ sử dụng **bù Schur** ([[8](https://en.wikipedia.org/wiki/Schur_complement)]), mọi ràng buộc nón bậc hai của SOCP đều có thể viết tương đương dưới dạng một LMI. Do đó, SOCP là một trường hợp đặc biệt của SDP, tức là $$SOCP \subseteq SDP$$.

### Nhắc lại: Bài toán Quy hoạch Nón Bậc hai
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{f^T x} \\\\
>    &\text{subject to } &&{\| A_i x + b_i \|_2 \leq c_i^T x + d_i, \quad i = 1, \dotsc, m}\\\\
>    & &&{Fx = g}.
>\end{align}
>$$

### Chuyển đổi SOCP sang SDP bằng bù Schur
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{f^T x} \\\\
>    &\text{subject to } 
>    &&
>    \begin{bmatrix}
>    (c_i^T x + d_i)I    & A_i x + b_i \\\\
>    (A_i x + b_i)^T & c_i^T x + d_i \\\\
>    \end{bmatrix} \succeq 0, \quad i = 1, \dotsc, m\\\\
>    & &&{Fx = g}.
>\end{align}
>$$