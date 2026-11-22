---
layout: post
title: 16-01 Tính đối ngẫu Lagrangian - nhìn lại
chapter: '16'
order: 2
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

Trong phần này, chúng ta sẽ chỉ ra cách biểu diễn bài toán nguyên thủy và bài toán đối ngẫu thông qua hàm Lagrange (Lagrangian), rồi dùng cách biểu diễn này để suy ra bài toán đối ngẫu cho quy hoạch tuyến tính (LP) dạng chuẩn và quy hoạch bậc hai (QP). Tiếp đó, chúng ta sẽ tìm bài toán đối ngẫu của bài toán rào cản (barrier) cho quy hoạch tuyến tính, và thấy rằng dạng của nó trùng khớp với bài toán rào cản thiết lập cho bài toán đối ngẫu của quy hoạch tuyến tính.

<br/>
Trước hết, xét bài toán nguyên thủy và hàm Lagrange tương ứng như sau.

### Bài toán nguyên thủy
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad f(x) \\\\
>    \text{subject to} &\quad h_i(x) \leq 0, i = 1, \ldots, m \\\\
>    &\quad l_j(x) = 0, j = 1, \ldots, r
>\end{align}
>$$

### Hàm Lagrange (Lagrangian)
>$$
>L(x,u,v) = f(x) + \sum_{i=1}^m u_i h_i (x) + \sum_{j=1}^r v_j l_j (x)
>$$

<br/>
Khi đó, bài toán nguyên thủy và bài toán đối ngẫu có thể được viết lại dưới dạng các bài toán minimax/maximin liên quan trực tiếp đến hàm Lagrange.

### Bài toán nguyên thủy được viết lại
>$$
>\min_x \mathop{\max_{u,v}}_{u \geq 0} L(x,u,v)
>$$

Dạng viết lại này không liệt kê tường minh các ràng buộc, nhưng phần cực đại hóa theo $$u, v$$ đóng vai trò như một hàm chỉ thị (indicator function) đối với mọi điểm $$x$$ không khả thi:

1. Nếu tồn tại $$i \in [1, m]$$ sao cho $$h_i(\hat{x}) \gt 0$$, thì $$\hat{x}$$ là điểm không khả thi. Khi đó, số hạng $$u_i h_i(\hat{x})$$ phân kỳ ra $$\infty$$ khi lấy $$\max_{u,v}$$ với $$u \geq 0$$, do đó đóng vai trò như hàm chỉ thị phạt vô hạn mọi điểm $$\hat{x}$$ vi phạm ràng buộc bất đẳng thức.
2. Nếu tồn tại $$i \in [1, r]$$ sao cho $$l_i(\hat{x}) \neq 0$$, thì $$\hat{x}$$ là điểm không khả thi. Khi đó, số hạng $$v_i l_i(\hat{x})$$ phân kỳ ra $$\infty$$ khi lấy $$\max_{u,v}$$, do đó đóng vai trò như hàm chỉ thị đối với mọi điểm $$\hat{x}$$ vi phạm ràng buộc đẳng thức.

### Bài toán đối ngẫu được viết lại
>$$
>\mathop{\max_{u,v}}_{u \geq 0} \min_x L(x,u,v)
>$$

Trong bài toán đối ngẫu, miền ràng buộc được nới lỏng nên hàm mục tiêu bên trong không còn đóng vai trò hàm chỉ thị cho các ràng buộc nguyên thủy. Vì phép lấy $$\min_x$$ với $$u, v$$ cố định không áp đặt các ràng buộc của bài toán nguyên thủy, bài toán đối ngẫu viết lại cũng thể hiện rõ cơ chế nới lỏng miền này. (Tham khảo: [11-02 Hàm đối ngẫu Lagrange]({% multilang_post_url contents/chapter11/21-03-24-11_02_Lagrange_dual_function %}))

## Tính đối ngẫu yếu và mạnh
Chúng ta ôn lại hai định lý cơ bản về tính đối ngẫu yếu và tính đối ngẫu mạnh.

### Định lý: tính đối ngẫu yếu
Gọi $$p$$ và $$d$$ lần lượt là giá trị tối ưu của bài toán nguyên thủy và bài toán đối ngẫu. Khi đó, bất đẳng thức sau luôn đúng:

$$
p \ge d
$$

### Định lý: tính đối ngẫu mạnh (điều kiện Slater tinh chỉnh)
Trên miền xác định $$D$$, giả sử $$f, h_1, \dots, h_p$$ là các hàm lồi và $$h_{p+1}, \dots, h_m, l_1, \dots, l_r$$ là các hàm affine. Nếu tồn tại điểm $$\hat{x} \in \text{relint}(D)$$ thỏa mãn:
> $$\begin{align}
>h_i(\hat{x}) \ & \lt 0, \ && i=1, \dots, p \\
>h_i(\hat{x}) \ & \le 0, \ && i=p+1, \dots, m \\
>l_j(\hat{x}) \ & = 0, \ && j = 1, \dots, r
\end{align}$$

thì $$p = d$$ được đảm bảo cho các giá trị tối ưu $$p, d$$ của bài toán nguyên thủy và bài toán đối ngẫu.

## Ví dụ: quy hoạch tuyến tính
Ta suy ra bài toán đối ngẫu của quy hoạch tuyến tính (LP) từ dạng định nghĩa ở trên.

### Bài toán nguyên thủy của LP dạng chuẩn
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad c^Tx \\\\
>    \text{subject to} &\quad Ax = b \\\\
>    &\quad x \ge 0
>\end{align}
>$$

Theo định nghĩa đã nêu, bài toán đối ngẫu tương ứng là:

$$\mathop{\max_{s,y}}_{s\ge0} \min_{x} \: L(x,s,y) = \mathop{\max_{s,y}}_{s\ge0} \min_{x} \: c^Tx - s^Tx + (b-Ax)^T y$$

Từ điều kiện dừng $$\nabla_x L = 0$$, ta thu được quan hệ $$c = A^Ty + s$$. Thay quan hệ này vào bài toán đối ngẫu:

$$\mathop{\max_{s,y}}_{s\ge0} \: (A^Ty + s)^Tx - s^Tx + (b-Ax)^Ty \quad \text{ s.t. } c=A^Ty +s$$

Rút gọn biểu thức trên, ta thu được:

### Bài toán đối ngẫu của LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty \\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>    &\quad s \ge 0
>\end{align}
>$$


## Ví dụ: quy hoạch bậc hai lồi
Tiếp theo, ta áp dụng cùng cách tiếp cận để suy ra bài toán đối ngẫu của quy hoạch bậc hai lồi (QP).

### Bài toán nguyên thủy của QP dạng chuẩn
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad \frac{1}{2} x^T Q x + c^Tx \\
>    \text{subject to} &\quad Ax = b \\
>    &\quad x \ge 0, \\
>
>\end{align}$$
>
>$$\text{trong đó } Q \text{ là ma trận đối xứng và nửa xác định dương.}$$


Bài toán đối ngẫu tương ứng có dạng:

$$\mathop{\max_{s,y}}_{s\ge0} \min_{x} \: L(x,s,y) = \mathop{\max_{s,y}}_{s\ge0} \min_{x} \:  \frac{1}{2} x^T Q x + c^Tx - s^Tx + (b-Ax)^T y$$


Giải điều kiện dừng $$\nabla_x L = 0$$ cho ta quan hệ $$Qx = A^Ty + s - c$$. Thay vào bài toán đối ngẫu:

$$
\begin{align}
&\mathop{\max_{s,y,x}}_{s\ge0} \: \frac{1}{2} x^T (A^Ty +s - c) + c^Tx - s^Tx + (b-Ax)^T y \quad \text{ s.t. } Qx = A^Ty +s - c\\\\
&= \mathop{\max_{s,y,x}}_{s\ge0} \: x^T (A^Ty +s - c) + c^Tx - s^Tx + (b-Ax)^T y -  \frac{1}{2} x^T (A^Ty +s - c) \quad \text{ s.t. } Qx = A^Ty +s - c\\\\
&= \mathop{\max_{s,y,x}}_{s\ge0}  \: b^Ty - \frac{1}{2} x^T (A^Ty +s - c) \quad  \text{ s.t. } Qx = A^Ty +s - c\\\\
&= \mathop{\max_{s,y,x}}_{s\ge0}  \: b^Ty - \frac{1}{2} x^T Q x \quad \text{ s.t. } Qx = A^Ty +s - c
\end{align}
$$

Viết gọn lại, ta thu được:

### Bài toán đối ngẫu của QP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y,x} &\quad b^Ty - \frac{1}{2} x^T Q x\\\\
>    \text{subject to} &\quad A^Ty +  s - c = Qx \\\\
>    &\quad s \ge 0
>\end{align}
>$$

Như vậy, bài toán đối ngẫu của một bài toán quy hoạch bậc hai cũng là một bài toán quy hoạch bậc hai.

## Ví dụ: bài toán rào cản cho quy hoạch tuyến tính
Bài toán rào cản (barrier) cho quy hoạch tuyến tính được định nghĩa như sau:

### Bài toán rào cản cho LP
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad c^Tx - \tau \sum_{i=1}^n \log(x_i)\\
>    \text{subject to} &\quad Ax = b, \\
>\end{align}$$
>
>$$\text{trong đó }\tau > 0.$$


Bài toán đối ngẫu tương ứng là:
$$
\begin{align}
\max_{y} \min_{x} \: L(x,y) &= \max_{y} \min_{x} \:  c^Tx - \tau \sum_{i=1}^n \log(x_i) + (b-Ax)^T y\\\\
&=  \max_{y} \min_{x} \:  \underbrace{(c-A^Ty)^T}_{s^T \doteq (c-A^Ty)^T}x - \tau \sum_{i=1}^n \log(x_i) + b^Ty\\\\
&= \max_{y} \min_{x} \: \sum_{i=1}^n \big( s_i x_i - \tau  \log(x_i) \big) + b^Ty  \quad \text{ s.t. } A^Ty +s = c
\end{align}
$$

Biểu thức $$\sum_{i=1}^n \big( s_i x_i - \tau \log(x_i) \big) + b^Ty$$ đạt giá trị nhỏ nhất khi $$x_i = \frac{\tau}{s_i}$$ (với $$s_i > 0$$). Thay $$x_i = \frac{\tau}{s_i}$$ vào bài toán đối ngẫu:

$$
\begin{align}
&\max_{s,y} \: b^Ty + n\tau - \tau \sum_{i=1}^n \log\left(\frac{\tau}{s_i}\right) \quad \text{ s.t. } A^Ty +s = c\\\\
&= \max_{s,y} \: b^Ty + \tau \sum_{i=1}^n \log(s_i) + n\tau - n\tau\log(\tau) \quad \text{ s.t. } A^Ty +s = c\\\\
\end{align}
$$

Vì hằng số $$n\tau - n\tau\log(\tau)$$ không ảnh hưởng đến nghiệm tối ưu, ta có thể bỏ qua hằng số này và viết gọn bài toán đối ngẫu như sau:

### Bài toán đối ngẫu của bài toán rào cản cho LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty + \tau \sum_{i=1}^n \log(s_i)\\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>\end{align}
>$$

Có thể thấy bài toán này trùng khớp hoàn toàn với bài toán rào cản thiết lập trực tiếp cho bài toán đối ngẫu của quy hoạch tuyến tính.
