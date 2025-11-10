---
layout: post
title: 16-02 Điều kiện tối ưu
chapter: '16'
order: 3
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

Trong phần này, chúng ta sẽ xem xét các điều kiện tối ưu KKT cho các bài toán nguyên thủy và các bài toán barrier tương ứng, và sau đó so sánh sự khác biệt của chúng.
<br/>

## Điều kiện tối ưu KKT

Hãy xem lại các điều kiện KKT mà chúng ta đã đề cập trong Chương 12. Điều kiện KKT được sử dụng như các điều kiện để xác định tính tối ưu.

### Bài toán nguyên thủy
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad f(x) \\\\
>    \text{subject to} &\quad h_i(x) \leq 0, i = 1, \ldots, m \\\\
>    &\quad l_j(x) = 0, j = 1, \ldots, r
>\end{align}
>$$

Khi bài toán nguyên thủy đã cho là lồi, các điều kiện KKT trở thành điều kiện đủ cho tính tối ưu nguyên thủy & đối ngẫu. Có nghĩa là, khi $$f, h_1, \dots, h_m$$ là lồi và $$l_1, \dots, l_r$$ là affine, nếu $$x^\star, u^\star, v^\star$$ thỏa mãn các điều kiện KKT sau, thì $$x^\star$$ và $$(u^\star, v^\star)$$ là tối ưu nguyên thủy & đối ngẫu với khoảng cách đối ngẫu bằng không. (Chúng ta giả sử rằng $$f, h_1, \dots, h_m, l_1, \dots, l_r$$ có thể vi phân.) <br>

* Tham khảo: [12-01 Điều kiện KKT]({% multilang_post_url contents/chapter12/21-04-02-12_00_KKT_conditions %})

### Điều kiện KKT cho bài toán nguyên thủy đã cho
>$$
>\begin{align}
>l_i &= 0, \quad i=1, \dots, r\\\\
>u_i^\star, -h_i(x^\star) &\ge 0, \quad i=1, \dots, m\\\\
>u_i^\star h_i(x^\star) &= 0, \quad i=1, \dots, m\\\\
>\nabla f(x^\star) + \sum_{i=1}^m \nabla h_i(x^\star) u^\star_i + \sum_{i=1}^r \nabla l_i(x^\star) v_i^\star &= 0.\\\\
>\end{align}
>$$

## Phương trình đường dẫn trung tâm

Hãy cũng xem xét các điều kiện để xác định tính tối ưu của các bài toán barrier.

### Bài toán barrier

>$$
\begin{align}
    \mathop{\text{minimize}}_x &\quad f(x) + \tau \phi(x) \\\\
    &\quad l_j(x) = 0, j = 1, \ldots, r  \\\\
\end{align}$$
>
>$$ \text{trong đó } \phi(x) = - \sum_{i=1}^m \log \big( -h_i(x) \big).$$


Bằng cách tổ chức các điều kiện KKT cho các bài toán barrier, chúng ta có thể suy ra các điều kiện tối ưu sau. Lưu ý sự khác biệt trong ràng buộc bất đẳng thức và các điều kiện bổ sung so với các điều kiện tối ưu KKT cho các bài toán nguyên thủy đã xem xét trước đó. (Tham khảo: [15-03-01 Điều kiện KKT bị nhiễu]({% multilang_post_url contents/chapter15/21-03-28-15_03_01_perturbed_kkt_conditions %}))

### Điều kiện tối ưu cho bài toán barrier (và đối ngẫu của nó)

>$$
\begin{align}
l_i &= 0, \quad i=1, \dots, r\\\\
u_i(t), -h_i(x^\star(t)) &\gt 0, \quad i=1, \dots, m\\\\
u_i(t) h_i(x^\star(t)) &= -\tau, \quad i=1, \dots, m\\\\
\nabla f(x^\star(t)) + \sum_{i=1}^m \nabla h_i(x^\star(t)) u_i(t) + \sum_{i=1}^r \nabla l_i(x^\star(t)) \hat{v}_i^\star &= 0,\\\\
\end{align} \\\\
$$
>
>$$\text{trong đó } \tau = \frac{1}{t}, u_i(t) = - \frac{1}{t h_i(x^\star(t))}, \quad \hat{v} = \frac{1}{t}v.$$

## Trường hợp đặc biệt: quy hoạch tuyến tính

### Nhắc lại: Bài toán nguyên thủy của LP dạng chuẩn
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad c^Tx \\\\
>    \text{subject to} &\quad Ax = b \\\\
>    &\quad x \ge 0
>\end{align}
>$$

### Nhắc lại: Bài toán đối ngẫu của LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty \\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>    &\quad s \ge 0
>\end{align}
>$$

Quy hoạch tuyến tính có tính chất tốt là luôn thỏa mãn tính đối ngẫu mạnh do điều kiện Slater được làm tế, vì các ràng buộc bất đẳng thức là affine. Các điều kiện tối ưu cho LP như sau:

>$$
>\begin{align}
>A^T y^\star + s^\star &= c\\\\
>Ax^\star &= b\\\\
>X S \mathbb{1} &= 0\\\\
>x^\star, s^\star &\ge 0,\\\\
>\end{align}$$
> 
>$$\text{trong đó }X = Diag(x^\star), S = Diag(s^\star)$$

Lưu ý rằng $$X S \mathbb{1} = 0$$ tương đương với $$Xs^\star=(x_1^\star s_1^\star, \dots, x_n^\star s_n^\star)=0$$. Chúng ta sử dụng ký hiệu $$X, S$$ để thuận tiện trong các thuật toán sẽ được giới thiệu sau này.

### Thuật toán cho quy hoạch tuyến tính

Chúng ta giới thiệu hai phương pháp đại diện để giải LP bằng cách sử dụng các điều kiện tối ưu.

1. Simplex: Một phương pháp duy trì các điều kiện 1, 2, và 3 trong khi dần dần thỏa mãn điều kiện 4.
2. Phương pháp điểm trong: Một phương pháp duy trì điều kiện 4 trong khi dần dần thỏa mãn các điều kiện 1, 2, và 3. Điều này sẽ được đề cập trong chương tiếp theo.

## Đường dẫn trung tâm cho quy hoạch tuyến tính

### Nhắc lại: Bài toán barrier cho LP
>$$\begin{align}
    \mathop{\text{minimize}}_x &\quad c^Tx - \tau \sum_{i=1}^n \log(x_i)\\\\
    \text{subject to} &\quad Ax = b, \\\\
    \text{trong đó}  &\quad \tau > 0
\end{align}$$


### Nhắc lại: Bài toán đối ngẫu của bài toán Barrier cho LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty + \tau \sum_{i=1}^n log(s_i)\\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>\end{align}
>$$

Các điều kiện tối ưu cho bài toán barrier của LP như sau:

>$$
\begin{align}
A^T y^\star + s^\star &= c\\\\
Ax^\star &= b\\\\
X S \mathbb{1} &= \tau \mathbb{1}\\\\
x^\star, s^\star &\gt 0,\\\\
\text{trong đó} &\quad X = Diag(x^\star), S = Diag(s^\star)
\end{align}$$

Các điều kiện 3 và 4 cho thấy sự khác biệt so với các điều kiện KKT của LP nguyên thủy.