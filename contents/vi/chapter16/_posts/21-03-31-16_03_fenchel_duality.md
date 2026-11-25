---
layout: post
title: 16-03 Tính đối ngẫu Fenchel
chapter: '16'
order: 4
owner: Minjoo Lee
categories:
- chapter16
lang: vi
---

Đối ngẫu Lagrange rất mạnh khi bài toán được viết tường minh dưới dạng hàm mục tiêu kèm các bất đẳng thức vô hướng $$h_i(x) \le 0$$. Nhưng khi bài toán là tổng hai hàm lồi không trơn ghép qua một toán tử tuyến tính $$\min_x f(x) + g(Ax)$$ — hoặc đặc biệt hơn, là **Quy hoạch nón (Conic Programming)** với ràng buộc $$x \in K$$ (nón bậc hai, nón ma trận nửa xác định dương) — thì **Đối ngẫu Fenchel** lại tỏa sáng với vẻ đẹp đối xứng và sức tổng quát vượt trội.

Chỉ bằng đúng hai hàm liên hợp $$f^*$$ và $$g^*$$, định lý đối ngẫu Fenchel biến bài toán nguyên thủy $$\min_x f(x) + g(Ax)$$ thành bài toán đối ngẫu $$\max_y -f^*(A^T y) - g^*(-y)$$ (tùy quy ước dấu). Không cần phân tách từng ràng buộc bất đẳng thức, toàn bộ cấu trúc hình học của nón $$K$$ tự động chuyển thành nón đối ngẫu $$K^*$$ chỉ sau một bước tính liên hợp của hàm chỉ thị!

## Kiến thức cần nhớ: Bốn trụ cột của Đối ngẫu Fenchel và Quy hoạch nón

- **Cặp bài toán Đối ngẫu Fenchel:**
  - Nguyên thủy: $$\min_x f(x) + g(Ax)$$.
  - Đối ngẫu: $$\max_u -f^*(-A^T u) - g^*(u)$$ (hoặc đổi biến $$y = -u$$ thành $$\max_y -f^*(A^T y) - g^*(-y)$$).
- **Điều kiện đối ngẫu mạnh Fenchel–Rockafellar:** Khi $$f, g$$ lồi và tồn tại điểm $$x \in \operatorname{dom} f$$ sao cho $$Ax \in \operatorname{int}(\operatorname{dom} g)$$ (hoặc điều kiện tương đối trong cho tập affine), khoảng cách đối ngẫu Fenchel bằng $$0$$.
- **Hai hàm liên hợp chìa khóa cho Quy hoạch nón:**
  - Liên hợp của hàm chỉ thị không gian affine $$I_{\{Ax = b\}}(x)$$ liên kết trực tiếp với nhân tử $$y$$ qua $$A^T y$$.
  - Liên hợp của hàm chỉ thị nón $$I_K(x)$$ chính là hàm chỉ thị của **nón cực** $$-K^*$$ (tức $$I_K^*(z) = I_{K^*}(-z)$$).
- **Sức mạnh thống nhất LP – SOCP – SDP:** Quy hoạch nón chuẩn $$\min \{c^T x \mid Ax = b, x \in K\}$$ tự động sinh ra đối ngẫu $$\max \{b^T y \mid c - A^T y \in K^*\}$$ — chỉ cần thay $$K = \mathbb{R}_+^n, \mathcal{Q}_n, \mathbb{S}_+^n$$ là có ngay đối ngẫu của LP, SOCP và SDP!

### Giải thích: Áp dụng Đối ngẫu Fenchel suy ra đối ngẫu của một bài toán Quy hoạch Nón Bậc Hai (SOCP) nhỏ

Xét bài toán quy hoạch nón bậc hai trên $$\mathbb{R}^3$$ với biến $$x = (x_1, x_2, x_3)^T$$ thuộc nón bậc hai $$K = \{(x_1, x_2, x_3) : \sqrt{x_1^2 + x_2^2} \le x_3\}$$ (nhớ $$K$$ tự đối ngẫu: $$K^* = K$$):

$$\min_{x \in \mathbb{R}^3} x_1 + 2x_3 \qquad \text{với } x_3 = 1, \;\; x \in K.$$
(Tức $$c = (1, 0, 2)^T$$, $$A = \begin{bmatrix} 0 & 0 & 1 \end{bmatrix}$$, $$b = 1$$).

1. **Giải nhanh trực tiếp bài toán nguyên thủy để kiểm chứng:**
   Vì $$x_3 = 1$$ và $$\sqrt{x_1^2 + x_2^2} \le 1$$, giá trị nhỏ nhất của $$x_1 + 2(1)$$ đạt tại $$x_1^\star = -1, x_2^\star = 0, x_3^\star = 1$$, cho $$p^\star = -1 + 2 = 1$$.
2. **Suy dẫn bài toán đối ngẫu bằng công thức đối ngẫu nón Fenchel:**
   $$\max_{y \in \mathbb{R}} b^T y \qquad \text{với } s = c - A^T y \in K^* = K.$$
   Ta tính $$s = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix} - \begin{bmatrix} 0 \\ 0 \\ y \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \\ 2 - y \end{bmatrix}$$.
3. **Áp dụng điều kiện $$s \in K$$ (nón bậc hai):**
   $$\sqrt{1^2 + 0^2} \le 2 - y \iff 1 \le 2 - y \iff y \le 1.$$
   Vậy bài toán đối ngẫu là $$\max_{y \le 1} y$$, đạt cực đại tại $$y^\star = 1$$ với $$d^\star = 1 = p^\star$$!
   Kiểm tra thêm tính trực giao nón (bù yếu nón): $$x^{\star T} s^\star = (-1)(1) + 0(0) + (1)(1) = 0$$ — khớp hoàn hảo!

---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Trong bài [13-04 Hàm liên hợp]({% multilang_post_url contents/chapter13/21-04-05-13_04_Conjugate_function %}), chúng ta đã biết cách suy ra bài toán đối ngẫu bằng hàm liên hợp (conjugate function). Tính đối ngẫu Fenchel đề cập đến các bài toán đối ngẫu được xây dựng từ hàm liên hợp theo dạng tổng quát sau:

$$
\max_{v} -f^*(A^Tv) - g^*(-v)
$$

Hãy xem dạng đối ngẫu này xuất phát từ đâu.

### Bài toán nguyên thủy

> $$
> \min_{x} \quad f(x) + g(Ax)
> $$

Bài toán này có thể viết lại tương đương bằng cách đưa thêm biến phụ $$z$$ và ràng buộc đẳng thức:

### Bài toán nguyên thủy được viết lại
>
$$
 \begin{align}
 &\min_{x,z} \        && f(x) + g(z)\\
 &\text{subject to} \ && Ax = z.
 \end{align}
 $$

Ta suy ra bài toán đối ngẫu của dạng viết lại bằng hàm liên hợp. <br/>

* **Nhắc lại:** $$f^*(s) \doteq  \max_{x} \big( s^Tx - f(x) \big) = -\min_{x} \big( f(x) - s^Tx \big)$$

<br/>
$$
\begin{align}
&\max_{v} \min_{x, z} \quad L(x,z,v)\\\\
= &\max_{v} \min_{x, z} \quad f(x) + g(z) + v^T (z - Ax) \\\\
= &\max_{v} \min_{x, z} \quad v^Tz + g(z) - (A^Tv)^Tx + f(x)\\\\
= &\max_{v} \quad  -f^*(A^Tv) - g^*(-v)\\\\
\end{align}
$$

### Tính đối ngẫu Fenchel
> $$
> \max_{v} -f^*(A^Tv) - g^*(-v)
> $$

* **Tính chất quan trọng:** Nếu $$f, g$$ là các hàm lồi và đóng, thì bài toán đối ngẫu của bài toán đối ngẫu quay trở lại chính bài toán nguyên thủy (tính đối xứng).

## Ví dụ: quy hoạch nón (Conic Programming)

### Bài toán nguyên thủy của CP dạng chuẩn
>$$
\begin{align}
    \mathop{\text{minimize}}_x &\quad c^Tx \\\\
    \text{subject to} &\quad Ax = b \\\\
    &\quad x \in K
\end{align}
$$

Bài toán trên có thể viết lại thông qua hai hàm $$f(x) = c^Tx + I_K(x)$$ và $$g(z) = I_{\{b\}}(z)$$.<br/>

* **Lưu ý:** $$\begin{equation}
    f(x) + g(Ax) = 
    \begin{cases}
      c^Tx, & \text{nếu}\ Ax=b, x \in K \\\\
      \infty, & \text{trường hợp khác}
    \end{cases}
  \end{equation}$$

### Bài toán nguyên thủy của CP được viết lại
> $$
> \begin{align}
> &\min_{x, z}       \ &&  f(x) + g(z)\\\
> &\text{subject to} \ && z  =Ax \\\
> \end{align}
> $$

### Suy ra bài toán đối ngẫu của CP

Từ dạng viết lại ở trên, triển khai tường minh hai hàm $$f$$ và $$g$$, ta có:
> $$
> \begin{align}
> & \min_{x, z} && \; c^Tx + I_K(x) + I_{\{b\}}(z)  \\\
> &\text{subject to} && \;  z   =Ax \\
> \end{align}
> $$

Áp dụng định nghĩa bài toán đối ngẫu và biến đổi bằng hàm liên hợp:

> $$
> \begin{align}
> & \max_{y} \; \min_{x, z} \;  L(x, z, y) \\\
> = \; & \max_{y} \; \min_{x, z} \;  c^Tx + I_K(x) + I_{\{b\}}(z) + y^T(z-Ax) \\\
> = \; & \max_{y}  \;\min_{x, z} \; (c - A^Ty)^Tx  + I_K(x) \;+ \;  y^Tz + I_{\{b\}}(z) \\\
> = \; & \max_{y} \;  \min_{x, z} \; -( (A^Ty - c)^Tx  - I_K(x)) \;  - \; ( - y^Tz - I_{\{b\}}(z) ) \\\
> = \; & \max_{y} \; - I_K^*(A^Ty - c)  -  I_{\{b\}}^*(-y)  \\\
> = \; & \max_{y} \; - I_{-K^*}(A^Ty - c)  - I_{\{b\}}^*(-y)  \\
> \end{align}
> $$

Số hạng $$I_{-K^*}(A^Ty - c)$$ có thể được chuyển thành ràng buộc tường minh:

> $$
> \begin{align}
> A^Ty - c & = -s, \; -s \in -K^* \\\
> \Leftrightarrow A^Ty + s & = c, \; s \in K^* \\\
> \end{align}
> $$

Do $$I_{\{b\}}^*(-y) = \max_{z} (-y^Tz - I_{\{b\}}(z)) = -b^Ty - I_{\{b\}}(b)$$, bài toán có thể được viết lại như sau:
> $$
> \begin{align}
> &\max_{y, s} \ && -(-b^Ty - I_{\{b\}}(b)) \\\
> &\text{subject to} \ && A^Ty + s = c \\\
> &  \; s \in K^* \\
> \end{align}
> $$

Vì $$I_{\{b\}}(b) = 0$$, ta rút gọn được:

### Bài toán đối ngẫu của CP

> $$
> \begin{align}
> &\max_{y, s} \ &&  \;  b^Ty  \\\
> &\text{subject to} \ && A^Ty + s = c \\\
> &  \; s \in K^* \\
> \end{align}
> $$ 

* Nếu bài toán nguyên thủy hoặc bài toán đối ngẫu khả thi ngặt, thì tính đối ngẫu mạnh được thỏa mãn.
* Nếu cả bài toán nguyên thủy và bài toán đối ngẫu đều khả thi ngặt, thì tính đối ngẫu mạnh được thỏa mãn và cả hai bài toán đều đạt nghiệm tối ưu.

## Ví dụ: quy hoạch nửa xác định (SDP)
Dưới đây là dạng nguyên thủy – đối ngẫu của quy hoạch nửa xác định (SDP) cùng cặp nguyên thủy – đối ngẫu cho bài toán rào cản tương ứng.

### Bài toán nguyên thủy của SDP
>$$
>\begin{align}
>    &\mathop{\text{minimize}}_{X} &&{tr(CX)} \\\\
>    &\text{subject to } &&{tr(A_iX) = b_i, \phantom{5} i=1,\dotsc,p} \\\\
>    & &&{X \succeq 0},\\\\
>\end{align}$$
>
> $$\text{trong đó } C, A_1, \dotsc, A_p \in \mathbb{S}^n.$$

* **Nhắc lại:** $$tr(CX) = \sum_{i,j=1}^n C_{ij}X_{ij}$$
* **Lưu ý:** Khác với LP, SDP không phải lúc nào cũng thỏa mãn tính đối ngẫu mạnh.

### Bài toán đối ngẫu của SDP
>$$
>\begin{align}
>    &\mathop{\text{maximize}}_{y} &&{b^Ty} \\\\
>    &\text{subject to } &&{\sum_{i=1}^p y_i A_i + S = C} \\\\
>    & &&{S \succeq 0}.\\\\
>\end{align}
>$$

* **Lưu ý:** Nón ma trận nửa xác định dương là một nón tự đối ngẫu: $$(\mathbb{S}_{+}^n)^* = \mathbb{S}_{+}^n$$.

### Bài toán nguyên thủy của bài toán rào cản cho SDP
>$$
>\begin{align}
>    &\mathop{\text{minimize}}_{X} &&{tr(CX) - \tau \log \big( det(X) \big)} \\\\
>    &\text{subject to } &&{tr(A_iX) = b_i, \phantom{5} i=1,\dotsc,p} \\\\
>\end{align}$$
>
>$$\text{trong đó } C, A_1, \dotsc, A_p \in \mathbb{S}^n.$$

### Bài toán đối ngẫu của bài toán rào cản cho SDP
>$$
>\begin{align}
>    &\mathop{\text{maximize}}_{y, S} &&{b^Ty +  \tau \log \big( det(S) \big)} \\\\
>    &\text{subject to } &&{\sum_{i=1}^p y_i A_i + S = C}.
>\end{align}
>$$