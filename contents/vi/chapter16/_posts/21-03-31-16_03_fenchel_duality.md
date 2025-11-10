---
layout: post
title: 16-03 Tính đối ngẫu Fenchel
chapter: '16'
order: 4
owner: Minjoo Lee
categories:
- chapter16
lang: vi
published: false
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Trong [13-04 Hàm liên hợp]({% multilang_post_url contents/chapter13/21-04-05-13_04_Conjugate_function %}), chúng ta đã học cách suy ra các bài toán đối ngẫu bằng cách sử dụng các hàm liên hợp. Tính đối ngẫu Fenchel đề cập đến các bài toán đối ngẫu được suy ra từ các hàm liên hợp có dạng sau:

$$
\max_{v} -f^*(A^Tv) - g^*(-v)
$$

Hãy khám phá xem dạng bài toán này được suy ra từ đâu.

### Bài toán nguyên thủy

> $$
> \min_{x} \quad f(x) + g(Ax)
> $$

Bài toán đã cho có thể được định nghĩa lại với một ràng buộc đẳng thức được thêm vào.

### Bài toán nguyên thủy được viết lại
>
$$
 \begin{align}
 &\min_{x,z} \        && f(x) + g(z)\\
 &\text{subject to} \ && Ax = z.
 \end{align}
 $$

Hãy suy ra bài toán đối ngẫu của bài toán nguyên thủy được định nghĩa lại bằng cách sử dụng các hàm liên hợp. <br/>

* **Nhắc lại:** $$f^*(s) \doteq  \max_{x} \big( s^Tx - f(x) \big) = \min_{x} \big( f(x) - s^Tx \big)$$

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

* **Tính chất tốt:** Nếu $$f, g$$ là lồi và đóng, đối ngẫu của đối ngẫu lại trở thành nguyên thủy. (Đối xứng)

## Ví dụ: quy hoạch cônic

### Bài toán nguyên thủy của CP dạng chuẩn
>$$
\begin{align}
    \mathop{\text{minimize}}_x &\quad c^Tx \\\\
    \text{subject to} &\quad Ax = b \\\\
    &\quad x \in K
\end{align}
$$

Bài toán trên có thể được định nghĩa lại bằng cách sử dụng hai hàm $$f(x) = c^Tx + I_K(x)$$ và $$g(z) = I_{\{b\}}(z)$$.<br/>

* **Lưu ý:** $$\begin{equation}
    f(x) + g(Ax) = 
    \begin{cases}
      0, & \text{nếu}\ Ax=b, x \in K \\\\
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

Hãy suy ra bài toán đối ngẫu từ bài toán nguyên thủy CP được định nghĩa lại. Đầu tiên, mở rộng các hàm $$f$$ và $$g$$ cho chúng ta:
> $$
> \begin{align}
> & \min_{x, z} && \; c^Tx + I_K(x) + I_{\{b\}}(z)  \\\
> &\text{subject to} && \;  z   =Ax \\
> \end{align}
> $$

Hãy mở rộng bài toán bằng cách sử dụng các hàm liên hợp từ định nghĩa của bài toán đối ngẫu.

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

$$I_{-K^*}(A^Ty - c)$$ có thể được biểu diễn như một ràng buộc.

> $$
> \begin{align}
> A^Ty - c & = -s, \; -s \in -K^* \\\
> \Leftrightarrow A^Ty + s & = c, \; s \in K^* \\\
> \end{align}
> $$

Vì $$I_{\{b\}}^*(-y) = \max_{b} -b^Ty - I_{\{b\}}(b)$$, bài toán có thể được tổ chức như sau:
> $$
> \begin{align}
> &\max_{y, s} \ && -(-b^Ty - I_{\{b\}}(b)) \\\
> &\text{subject to} \ && y^TA + s = c \\\
> &  \; s \in K^* \\
> \end{align}
> $$

Vì $$I_{\{b\}}(b) = 0$$, nó có thể được loại bỏ khỏi bài toán.

### Bài toán đối ngẫu của CP

> $$
> \begin{align}
> &\max_{y, s} \ &&  \;  b^Ty  \\\
> &\text{subject to} \ && y^TA + s = c \\\
> &  \; s \in K^* \\
> \end{align}
> $$ 

* Nếu bài toán nguyên thủy hoặc bài toán đối ngẫu khả thi nghiêm ngặt, thì tính đối ngẫu mạnh được thỏa mãn.
* Nếu cả bài toán nguyên thủy và bài toán đối ngẫu đều khả thi nghiêm ngặt, thì tính đối ngẫu mạnh được thỏa mãn và tồn tại nghiệm tối ưu nguyên thủy & đối ngẫu.

## Ví dụ: quy hoạch nửa xác định
Hãy xem xét các dạng của bài toán nguyên thủy & đối ngẫu cho SDP và các bài toán nguyên thủy & đối ngẫu cho bài toán barrier của SDP.

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
* **Lưu ý:** Không giống như LP, SDP không luôn thỏa mãn tính đối ngẫu mạnh.

### Bài toán đối ngẫu của SDP
>$$
>\begin{align}
>    &\mathop{\text{maximize}}_{y} &&{b^Ty} \\\\
>    &\text{subject to } &&{\sum_{i=1}^m y_i A_i + S = C} \\\\
>    & &&{S \succeq 0}.\\\\
>\end{align}
>$$

* **Lưu ý:** Nón nửa xác định dương là một nón tự đối ngẫu. ($$(\mathbb{S}_{+}^n)^* = \mathbb{S}_{+}^n$$)

### Bài toán nguyên thủy của bài toán Barrier cho SDP
>$$
>\begin{align}
>    &\mathop{\text{minimize}}_{X} &&{tr(CX) - \tau \log \big( det(X) \big)} \\\\
>    &\text{subject to } &&{tr(A_iX) = b_i, \phantom{5} i=1,\dotsc,p} \\\\
>\end{align}$$
>
>$$\text{trong đó } C, A_1, \dotsc, A_p \in \mathbb{S}^n.$$

### Bài toán đối ngẫu của bài toán Barrier cho SDP
>$$
>\begin{align}
>    &\mathop{\text{maximize}}_{y, S} &&{b^Ty +  \tau \log \big( det(S) \big)} \\\\
>    &\text{subject to } &&{\sum_{i=1}^m y_i A_i + S = C}.
>\end{align}
>$$