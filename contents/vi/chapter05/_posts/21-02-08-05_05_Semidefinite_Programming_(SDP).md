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

Trong Quy hoạch Tuyến tính, ta yêu cầu một vector $$x \in \mathbb{R}^n$$ không âm theo từng thành phần: $$x_i \ge 0$$. Bây giờ hãy nâng cấp trí tưởng tượng lên một chiều sâu hoàn toàn mới: thay vector $$x$$ bằng một **ma trận đối xứng** $$X \in \mathbb{S}^n$$, và thay điều kiện "không âm từng phần tử" bằng điều kiện "mọi trị riêng đều không âm" — tức ma trận **nửa xác định dương** $$X \succeq 0$$!

Bước nhảy vọt tưởng chừng trừu tượng ấy sinh ra **Quy hoạch Nửa xác định (Semidefinite Programming - SDP)** — một trong những phát kiến rực rỡ nhất của tối ưu hóa lồi cuối thế kỷ 20. Nhờ SDP, Goemans và Williamson (1995) đã phá vỡ kỷ lục xấp xỉ bài toán NP-khó Max-Cut với tỷ lệ đảm bảo $$0.878$$, các kỹ sư điều khiển chứng minh được tính ổn định của hệ phi tuyến qua hàm Lyapunov, và các nhà nghiên cứu AI kiểm chứng được độ vững chắc của mạng nơ-ron sâu.

## Kiến thức cần nhớ: Tư duy tối ưu trên không gian ma trận

Bốn trụ cột sau mở khóa trực giác về SDP và Bất đẳng thức Ma trận Tuyến tính (LMI):

- **Nón Ma trận Nửa xác định dương $$\mathbb{S}_+^n$$:** Tập tất cả ma trận đối xứng $$X$$ thỏa $$v^T X v \ge 0 \; \forall v$$ là một nón lồi đóng, tự đối ngẫu (với tích trong Frobenius $$\langle A, B \rangle = \operatorname{tr}(AB)$$). Khác với góc phần tư không âm có các mặt phẳng, biên của $$\mathbb{S}_+^n$$ vừa cong trơn vừa có những đường gờ sắc (tại nơi trị riêng giảm hạng).
- **Bất đẳng thức Ma trận Tuyến tính (LMI):** Ràng buộc $$F(x) = F_0 + x_1 F_1 + \dots + x_m F_m \succeq 0$$ yêu cầu một tổ hợp affine của các ma trận đối xứng phải nửa xác định dương. Nếu mọi $$F_i$$ đều là ma trận đường chéo, LMI thu gọn về đúng một hệ bất đẳng thức tuyến tính LP!
- **Bổ đề Phần bù Schur (Schur Complement):** Đây là "cây đũa thần" chuyển mọi ràng buộc bậc hai và SOCP thành LMI:
  $$\|u\|_2 \le t \iff \begin{pmatrix} t I & u \\ u^T & t \end{pmatrix} \succeq 0.$$
  Nhờ đó ta chứng minh được ngay $$\text{LP} \subset \text{QP} \subset \text{QCQP} \subset \text{SOCP} \subset \text{SDP}$$.
- **Nới lỏng SDP cho bài toán tổ hợp & Ma trận hạng thấp:** Khi gặp biến $$x_i \in \{-1, +1\}$$, ta đặt ma trận $$X = x x^T$$ thỏa $$X_{ii} = 1,\; X \succeq 0,\; \operatorname{rank}(X) = 1$$. Chỉ cần bỏ ràng buộc phi lồi $$\operatorname{rank}(X) = 1$$, ta thu được ngay một bài SDP lồi cực chặt!

### Giải thích: Chuyển bài toán tìm trị riêng lớn nhất và ràng buộc SOCP thành LMI 2×2

**Ví dụ 1 — Tối thiểu hóa trị riêng lớn nhất $$\lambda_{\max}(A(x))$$:**
Cho $$A(x) = \begin{pmatrix} 1 + x & 2 \\ 2 & 3 - x \end{pmatrix}$$. Tìm $$x \in \mathbb{R}$$ để $$\lambda_{\max}(A(x))$$ nhỏ nhất.

1. **Chuyển thành SDP:** Bất đẳng thức $$\lambda_{\max}(A(x)) \le t$$ tương đương với mọi trị riêng của $$tI - A(x)$$ đều $$\ge 0$$, tức là LMI:
   $$\min_{x, t} \; t \quad \text{s.t.} \quad \begin{pmatrix} t - 1 - x & -2 \\ -2 & t - 3 + x \end{pmatrix} \succeq 0.$$
2. **Giải bằng tiêu chuẩn Sylvester cho ma trận 2×2 nửa xác định dương:**
   Cần hai phần tử đường chéo $$\ge 0$$ và định thức $$\ge 0$$:
   $$(t - 1 - x)(t - 3 + x) - 4 \ge 0 \iff (t - 2)^2 - (x - 1)^2 \ge 4.$$
3. **Tìm giá trị nhỏ nhất của $$t$$:**
   Ta có $$(t - 2)^2 \ge 4 + (x - 1)^2 \ge 4$$. Muốn $$t$$ nhỏ nhất, chọn $$x^\star = 1$$ để triệt tiêu $$(x-1)^2$$, cho $$(t - 2)^2 = 4 \implies t^\star = 4$$ (vì cần $$t - 1 - x = t - 2 \ge 0$$).
4. **Kiểm tra trực tiếp:** Tại $$x^\star = 1$$, $$A(1) = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}$$ có hai trị riêng là $$4$$ và $$0$$, vậy $$\lambda_{\max}(A(1)) = 4$$ đúng bằng $$t^\star$$!

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