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