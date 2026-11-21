---
layout: post
title: '17-01 Ôn lại phương pháp chắn, đối ngẫu và điều kiện tối ưu'
chapter: '17'
order: 2
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---

Ở Chương 15 chúng ta đã xem xét phương pháp chắn, và ở Chương 13 và 16 chúng ta đã tìm hiểu về đối ngẫu.
Trước khi đi vào nội dung của chương này, chúng ta muốn ôn lại ngắn gọn phương pháp chắn và đối ngẫu.



## Phương pháp chắn
Khi bài toán gốc (primal) sau là lồi và $$f, h_i , i = 1, . . . m$$ khả vi,
> $$\begin{align}
> &\min_{x} && f(x) \\
> &\text{subject to } &&h_{i}(x) \leq 0, i = 1, \dotsc, m \\
> &&& Ax = b \\
> \end{align}$$

Sử dụng hàm chắn logarit, bài toán gốc có thể được chuyển thành bài toán chắn như sau:

> $$\begin{align}
> & \min_{x} && f(x) + \frac{1}{t} \phi(x) & \qquad & \min_{x} && tf(x) + \phi(x) \\
> & \text{subject to } && Ax = b & \iff \qquad & \text{subject to } && Ax = b \\
> & \text{where } && \phi(x) = - \sum_{i=1}^{m} \log(-h_i(x))
> \end{align}$$

Thuật toán bắt đầu với $$t = t^{(0)}$$ thỏa mãn $$t > 0$$ và tăng $$t$$ cho đến khi $$\frac{m}{t}$$ nhỏ hơn hoặc bằng $$\epsilon$$. Khi đó, phương pháp Newton được dùng để tìm $$x^{\star}(t)$$ với giá trị khởi tạo $$x^{(0)}$$, và quá trình tìm $$x^{(k+1)} = x^{\star}(t)$$ ở mỗi bước với $$k = 1, 2, 3, . . .$$ được lặp lại.

Thuật toán có thể được tóm tắt ngắn gọn như sau:

1. Chọn $$t^{(0)} \gt 0$$ và $$k := 0$$.
2. Giải bài toán chắn tại $$t = t^{(0)}$$ để tìm $$x^{(0)} = x^{\star}(t)$$.
3. Trong khi $$m/t \gt \epsilon$$ <br>
  3-1. Cập nhật $$t^{(k+1)} = µt$$ với $$(µ > 1)$$ <br>
  3-2. Khởi tạo phương pháp Newton với $$x^{(k)}$$ (warm start)<br>
        Giải bài toán chắn tại $$t = t^{(k+1)}$$ để tìm $$x^{(k+1)} = x^{\star}(t)$$.<br>
  kết thúc vòng lặp<br>

* Thông tin chi tiết xem [15-01-02 Hàm chắn logarit và phương pháp chắn]({% multilang_post_url contents/chapter15/21-03-28-15_01_02_log_barrier_function_and_barrier_method %})


## Đối ngẫu
Cho bài toán gốc sau: 
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad f(x) \\\\
>    \text{subject to} &\quad Ax = b \\\\
>    &\quad h(x) \le 0
>\end{align}
>$$

Bài toán này có thể được chuyển sang dạng Lagrange như sau:
>$$
>L(x,u,v) = f(x) + u^Th(x) + v^T(Ax - b)
>$$

Sử dụng hàm Lagrange được định nghĩa như vậy, bài toán gốc và bài toán đối ngẫu có thể được định nghĩa lại dưới dạng sau. Thông tin chi tiết xem Chương 16.<br>
### Bài toán gốc
>$$
>\min_x \mathop{\max_{u,v}}_{u \geq 0} L(x,u,v)
>$$

### Bài toán đối ngẫu
>$$
>\mathop{\max_{u,v}}_{u \geq 0} \min_x L(x,u,v)
>$$

## Điều kiện tối ưu

Khi $$f,h_1,...h_m$$ lồi và khả vi, và bài toán đã cho thỏa mãn đối ngẫu mạnh, các điều kiện tối ưu KKT của bài toán này như sau:

> $$
> \begin{array}{rcl}
> ∇f(x) +∇h(x)u + A^Tv & = & 0 & \text{(Tính dừng)}\\\
>  Uh(x) & = & 0 & \text{(Độ lệch bù)} \\\
> Ax & = & b & \text{(Khả thi gốc)}\\\
> u,−h(x)  & ≥ & 0 & \text{(Khả thi đối ngẫu)}
> \end{array}
> $$

Ở đây, $$U$$ nghĩa là $$\text{diag}(u)$$, và $$∇h(x)$$ nghĩa là $$ [ ∇h_1(x) ··· ∇h_m(x) ]$$.

* Thông tin chi tiết xem [Chương 12 Điều kiện KKT]({% multilang_post_url contents/chapter12/21-04-02-12_00_KKT_conditions %})

## Phương trình đường trung tâm
Hàm $$f(x)$$ có thể được định nghĩa lại thành bài toán chắn như sau.<br>
Trong phương trình dưới đây, $$τ$$ là $$\frac{1}{t}$$, và bằng cách cho $$τ$$ dần tiến về 0 và tìm nghiệm lặp đi lặp lại, cuối cùng ta thu được nghiệm của bài toán ban đầu.

>$$
>\begin{align}
>&\min_{x} && {f(x) + τ\phi(x)} \\\\
>& &&{Ax = b} \\\
>& \text{where } && \phi(x) = −\sum_{i=1}^m \log(−h_i(x)).
>\end{align}
>$$

Nghĩa là, trong phương trình trên, sự khác biệt so với bài toán gốc xuất hiện tùy theo $$τ$$, và quỹ đạo được tạo ra theo $$τ$$, tức là tập nghiệm của bài toán chắn, được gọi là đường trung tâm (central path).

Và các điều kiện tối ưu cho bài toán chắn này như sau:
> $$
> \begin{array}{rcl}
> ∇f(x) +∇h(x)u + A^Tv  & = & 0 \\\
> Uh(x) & = & −τ\mathbb{1} \\\
> Ax & = & b \\\
> u,−h(x)  & > & 0
> \end{array}
> $$
 
* Thông tin chi tiết xem [16-02 Điều kiện tối ưu]({% multilang_post_url contents/chapter16/21-03-31-16_02_optimality_conditions %})

**Phương pháp điểm trong gốc-đối ngẫu (Primal-Dual interior point method)** được giới thiệu trong chương này là phương pháp định nghĩa ba phương trình đầu tiên ở trên là các phần dư (residual) và tìm nghiệm bằng cách đưa chúng về $$0$$.

#### Một sự thật hữu ích
Nghiệm $$(x(τ),u(τ),v(τ))$$ có khoảng cách đối ngẫu (duality gap) bằng $$mτ$$, tức là $$\frac{m}{t}$$, như sau:
> $$f(x(τ))−\min_x L(x,u(τ),v(τ)) = mτ= \frac{m}{t}$$
