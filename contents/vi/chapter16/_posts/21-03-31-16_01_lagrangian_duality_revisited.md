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

Trong phần này, chúng ta sẽ cho thấy rằng các bài toán nguyên thủy và đối ngẫu có thể được định nghĩa bằng cách sử dụng Lagrangian, và sử dụng định nghĩa này để suy ra các bài toán đối ngẫu cho quy hoạch tuyến tính dạng chuẩn và quy hoạch bậc hai. Hơn nữa, chúng ta sẽ suy ra bài toán đối ngẫu cho quy hoạch tuyến tính với bài toán barrier được áp dụng, cho thấy rằng dạng của nó giống với bài toán barrier cho bài toán đối ngẫu của quy hoạch tuyến tính.

<br/>
Đầu tiên, hãy định nghĩa bài toán nguyên thủy và Lagrangian như sau.

### Bài toán nguyên thủy
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad f(x) \\\\
>    \text{subject to} &\quad h_i(x) \leq 0, i = 1, \ldots, m \\\\
>    &\quad l_j(x) = 0, j = 1, \ldots, r
>\end{align}
>$$

### Lagrangian
>$$
>L(x,u,v) = f(x) + \sum_{i=1}^m u_i h_i (x) + \sum_{j=1}^r v_j l_j (x)
>$$

<br/>
Tại thời điểm này, bài toán nguyên thủy và bài toán đối ngẫu có thể được định nghĩa lại thành các bài toán liên quan đến Lagrangian.

### Bài toán nguyên thủy được viết lại
>$$
>\min_x \mathop{\max_{u,v}}_{u \geq 0} L(x,u,v)
>$$

Bài toán nguyên thủy được định nghĩa lại không nêu rõ ràng các ràng buộc, nhưng nó có tác dụng như một hàm chỉ thị cho bất kỳ $$x$$ không khả thi nào vi phạm các ràng buộc.

1. Nếu $$h_i(\hat{x}) \gt 0$$ cho một số $$i \in [1, m]$$, thì $$\hat{x}$$ là một điểm không khả thi. Trong trường hợp này, $$u_i h_i(\hat{x})$$ phân kỳ về $$\infty$$ do $$\max_{u,v}$$, vì vậy nó hoạt động như một hàm chỉ thị cho bất kỳ $$\hat{x}$$ nào vi phạm ràng buộc bất đẳng thức.
2. Nếu $$l_i(\hat{x}) \neq 0$$ cho một số $$i \in [1, r]$$, thì $$\hat{x}$$ là một điểm không khả thi. Trong trường hợp này, $$v_i l_i(\hat{x})$$ phân kỳ về $$\infty$$ do $$\max_{u,v}$$, vì vậy nó hoạt động như một hàm chỉ thị cho bất kỳ $$\hat{x}$$ nào vi phạm ràng buộc đẳng thức.

### Bài toán đối ngẫu được viết lại
>$$
>\mathop{\max_{u,v}}_{u \geq 0} \min_x L(x,u,v)
>$$

Trong bài toán đối ngẫu, việc nới lỏng miền là cần thiết, vì vậy nó không nên hoạt động như một hàm chỉ thị cho các ràng buộc của bài toán nguyên thủy. Vì việc lấy $$\min_x$$ cho $$u, v$$ cố định không thể thực thi các ràng buộc của bài toán nguyên thủy, bài toán đối ngẫu được định nghĩa lại cũng có tác dụng nới lỏng miền. (Tham khảo: [11-02 Hàm đối ngẫu Lagrange]({% multilang_post_url contents/chapter11/21-03-24-11_02_Lagrange_dual_function %}))

## Tính đối ngẫu yếu và mạnh
Hãy xem xét lại tính đối ngẫu yếu và tính đối ngẫu mạnh.

### Định lý: tính đối ngẫu yếu
Khi $$p$$ và $$d$$ là các giá trị tối ưu cho bài toán nguyên thủy và bài toán đối ngẫu tương ứng, điều sau luôn được thỏa mãn:


$$
p \ge d
$$

### Định lý: tính đối ngẫu mạnh (điều kiện Slater được làm tế)
Đối với tập miền $$D$$, giả sử rằng $$f, h_1, \dots, h_p$$ là lồi và $$h_{p+1}, \dots, h_m, l_1, \dots, l_r$$ là affine. Nếu tồn tại $$\hat{x} \in \text{relint}(D)$$ thỏa mãn điều sau:
> $$\begin{align}
>h_i(\hat{x}) \ & \lt 0, \ && i=1, \dots, p \\
>h_i(\hat{x}) \ & \le 0, \ && i=p+1, \dots, m \\
>l_j(\hat{x}) \ & = 0, \ && j = 1, \dots, r
\end{align}$$

thì $$p = d$$ được đảm bảo cho các giá trị tối ưu $$p, d$$ của bài toán nguyên thủy và bài toán đối ngẫu.

## Ví dụ: quy hoạch tuyến tính
Hãy suy ra bài toán đối ngẫu của quy hoạch tuyến tính bằng cách sử dụng bài toán đối ngẫu đã định nghĩa trước đó.

### Bài toán nguyên thủy của LP dạng chuẩn
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad c^Tx \\\\
>    \text{subject to} &\quad Ax = b \\\\
>    &\quad x \ge 0
>\end{align}
>$$

Theo định nghĩa trước đó, bài toán đối ngẫu của bài toán trên như sau:

$$\mathop{\max_{s,y}}_{s\ge0} \min_{x} \: L(x,s,y) = \mathop{\max_{s,y}}_{s\ge0} \min_{x} \: c^Tx - s^Tx + (b-Ax)^T y$$

Chúng ta thay thế mối quan hệ $$c=A^Ty +s$$ thu được bằng cách giải $$\nabla_x L = 0$$ vào bài toán đối ngẫu.

$$\mathop{\max_{s,y}}_{s\ge0} \: (A^Ty + s)^Tx - s^Tx + (b-Ax)^Ty \quad \text{ s.t. } c=A^Ty +s$$

Điều này có thể được tổ chức như sau:

### Bài toán đối ngẫu của LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty \\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>    &\quad s \ge 0
>\end{align}
>$$


## Ví dụ: quy hoạch bậc hai lồi
Bây giờ hãy suy ra bài toán đối ngẫu của quy hoạch bậc hai bằng cách sử dụng bài toán đối ngẫu đã định nghĩa trước đó.

### Bài toán nguyên thủy của QP dạng chuẩn
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad \frac{1}{2} x^T Q x + c^Tx \\
>    \text{subject to} &\quad Ax = b \\
>    &\quad x \ge 0, \\
>
>\end{align}$$
>
>$$\text{trong đó } Q \text{ là đối xứng và nửa xác định dương.}$$


Theo định nghĩa trước đó, bài toán đối ngẫu của bài toán trên như sau:

$$\mathop{\max_{s,y}}_{s\ge0} \min_{x} \: L(x,s,y) = \mathop{\max_{s,y}}_{s\ge0} \min_{x} \:  \frac{1}{2} x^T Q x + c^Tx - s^Tx + (b-Ax)^T y$$


Chúng ta thay thế mối quan hệ $$Qx = A^Ty +s - c$$ thu được bằng cách giải $$\nabla_x L = 0$$ vào bài toán đối ngẫu.

$$
\begin{align}
&\mathop{\max_{s,y,x}}_{s\ge0} \: \frac{1}{2} x^T (A^Ty +s - c) + c^Tx - s^Tx + (b-Ax)^T y \quad \text{ s.t. } Qx = A^Ty +s - c\\\\
&= \mathop{\max_{s,y,x}}_{s\ge0} \: x^T (A^Ty +s - c) + c^Tx - s^Tx + (b-Ax)^T y -  \frac{1}{2} x^T (A^Ty +s - c) \quad \text{ s.t. } Qx = A^Ty +s - c\\\\
&= \mathop{\max_{s,y,x}}_{s\ge0}  \: b^Ty - \frac{1}{2} x^T (A^Ty +s - c) \quad  \text{ s.t. } Qx = A^Ty +s - c\\\\
&= \mathop{\max_{s,y,x}}_{s\ge0}  \: b^Ty - \frac{1}{2} x^T Q x \quad \text{ s.t. } Qx = A^Ty +s - c
\end{align}
$$

Điều này có thể được tổ chức như sau:

### Bài toán đối ngẫu của QP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y,x} &\quad b^Ty - \frac{1}{2} x^T Q x\\\\
>    \text{subject to} &\quad A^Ty +  s - c = Qx \\\\
>    &\quad s \ge 0
>\end{align}
>$$

Bài toán đối ngẫu của một bài toán bậc hai cũng là một bài toán bậc hai.

## Ví dụ: bài toán barrier cho quy hoạch tuyến tính
Bài toán barrier cho quy hoạch tuyến tính được định nghĩa như sau:

### Bài toán barrier cho LP
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad c^Tx - \tau \sum_{i=1}^n \log(x_i)\\
>    \text{subject to} &\quad Ax = b, \\
>\end{align}$$
>
>$$\text{trong đó }\tau > 0.$$


Theo định nghĩa trước đó, bài toán đối ngẫu của bài toán trên như sau:
$$
\begin{align}
\max_{y} \min_{x} \: L(x,y) &= \max_{y} \min_{x} \:  c^Tx - \tau \sum_{i=1}^n \log(x_i) + (b-Ax)^T y\\\\
&=  \max_{y} \min_{x} \:  \underbrace{(c-A^Ty)}_{s \doteq c-A^Ty}x - \tau \sum_{i=1}^n \log(x_i) + b^Ty\\\\
&= \max_{y} \min_{x} \: \sum_{i=1}^n \big( s_i^Tx_i - \tau  \log(x_i) \big) + b^Ty  \quad \text{ s.t. } A^Ty +s = c
\end{align}
$$

Ở đây, $$\sum_{i=1}^n \big( s_i^Tx_i - \tau  \log(x_i) \big) + b^Ty$$ sẽ được tối thiểu hóa khi $$x_i = \frac{\tau}{s_i}$$. Do đó, hãy thay thế $$\frac{\tau}{s_i}$$ cho $$x_i$$ trong bài toán đối ngẫu.

$$
\begin{align}
&\max_{s,y} \: b^Ty + n\tau - \tau \sum_{i=1}^n log(\frac{\tau}{s_i}) \quad \text{ s.t. } A^Ty +s = c\\\\
&= \max_{s,y} \: b^Ty + \tau \sum_{i=1}^n log(s_i) + n\tau - n\tau\log(\tau) \quad \text{ s.t. } A^Ty +s = c\\\\
\end{align}
$$

Vì $$n\tau - n\tau\log(\tau)$$ có thể được bỏ qua khỏi bài toán, bài toán đối ngẫu có thể được tổ chức như sau:

### Bài toán đối ngẫu của bài toán Barrier cho LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty + \tau \sum_{i=1}^n log(s_i)\\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>\end{align}
>$$

Chúng ta có thể thấy rằng bài toán này giống hệt với bài toán barrier cho bài toán đối ngẫu của quy hoạch tuyến tính.
