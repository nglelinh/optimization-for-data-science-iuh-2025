---
layout: post
title: '17-02-03 Thuật toán gốc-đối ngẫu (Primal-Dual Algorithm)'
chapter: '17'
order: 6
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---

Để định nghĩa thuật toán gốc-đối ngẫu, trước hết ta định nghĩa $$\tau(x,u)$$ như sau.
> $$\tau(x,u) := -\frac{h(x)^Tu}{m} \quad \text{với} \quad h (x) \le 0, u \ge 0$$

Lưu ý rằng $$t$$ và $$\mu$$ của phương pháp chắn được viết lại thành $$\tau$$ và $$\sigma$$ trong thuật toán gốc-đối ngẫu.
> $$\tau = \frac{1}{t}, \quad \sigma = \frac{1}{\mu}$$

## Thuật toán gốc-đối ngẫu
Thuật toán gốc-đối ngẫu như sau.
> 1. Chọn $$\sigma \in (0,1)$$.<br>
> 2. Chọn $$(x^0,u^0,v^0)$$ với $$h(x^0) < 0$$ và $$u^0 > 0$$.<br>
> 3. Lặp lại các bước sau ($$k = 0,1,... $$):<br>
> $$\quad$$ * Tính bước Newton:<br>
> $$\qquad \quad (x,u,v) = (x^k,u^k,v^k)$$ <br>
> $$\qquad \quad$$ tính $$\tau := \sigma \tau(x^k,u^k)$$<br>
> $$\qquad \quad$$ tính $$(\Delta x,\Delta u,\Delta v)$$ ứng với $$\tau$$ này<br>
> $$\quad$$ * Chọn độ dài bước $$\theta_k$$ bằng backtracking.<br>
> $$\quad$$ * Cập nhật gốc-đối ngẫu:<br>
> $$\qquad \quad (x^{k+1},u^{k+1},v^{k+1}) := (x^k,u^k,v^k) + \theta_k(\Delta x,\Delta u,\Delta v)$$<br>
> 4. Dừng khi $$-h(x^{k+1})^Tu \le \epsilon$$ và $$(\parallel r_{prim} \parallel^2_2 + \parallel r_{dual} \parallel^2_2)^{1/2} \le \epsilon $$.<br>

Ở mỗi bước, thuật toán thực hiện một bước Newton để tính $$(\Delta x,\Delta u,\Delta v)$$ rồi cập nhật gốc-đối ngẫu để thu được $$(x^{k+1},u^{k+1},v^{k+1})$$. Độ dài bước $$\theta_k$$ được chọn bằng backtracking line search để các biến gốc-đối ngẫu vẫn khả thi. Thuật toán dừng khi khoảng cách đối ngẫu thay thế và các phần dư gốc, đối ngẫu nhỏ hơn $$\epsilon$$.


## Backtracking line search
Vì thuật toán gốc-đối ngẫu chỉ thực hiện một bước Newton mỗi vòng lặp, nên bước này nên được xem là cho một hướng đi về phía nghiệm hơn là một nghiệm chính xác. Do đó, ta cần chọn độ dài bước phù hợp để khi di chuyển theo hướng đó, điểm lặp vẫn nằm trong tập khả thi.

Nghĩa là, ở mỗi bước của thuật toán ta tìm $$\theta$$ và cập nhật các biến gốc-đối ngẫu.

> $$x^+ = x + \theta \Delta x, \quad  u^+ = u + \theta \Delta u, \quad v^+ = v + \theta \Delta v$$

Quá trình này có hai mục tiêu chính.

* Duy trì $$h(x) < 0, u > 0$$.
* Giảm $$\parallel r(x,u,v) \parallel$$.

Để làm điều này, ta dùng **backtracking line search nhiều giai đoạn (multi-stage backtracking line search)**.

#### Giai đoạn 1: khả thi đối ngẫu $$u \gt 0$$
Ta bắt đầu với bước lớn nhất $$\theta_{max} \le 1$$ thỏa mãn $$u + \theta \Delta u \ge 0$$.

> $$\theta_{\max} = \min \Biggl\{1,\  \min \Bigl\{ -\frac{u_i}{\Delta u_i} : \Delta u_i < 0 \Bigr\} \Biggr\}$$

Công thức này được suy ra như sau.

> $$\begin{align}
&u + \theta \Delta u && \ge 0  \\\\
\Leftrightarrow \quad &u && \ge -\theta \Delta u \\\\
\Leftrightarrow \quad &- u/\Delta u && \ge \theta \quad  \text{ với các thành phần có }\Delta u \lt 0  \\\\
\end{align}$$

Bước này làm cho $$u$$ khả thi.

#### Giai đoạn 2: khả thi gốc $$h(x) \lt 0$$
Tiếp theo, chọn các tham số $$\alpha, \beta \in (0,1)$$, đặt $$\theta = 0.99\theta_{max}$$, rồi thực hiện như sau.

* Cập nhật $$\theta = \beta\theta$$ cho đến khi $$h_i(x^+) < 0, i = 1,...,m$$.

Bước này làm cho $$x$$ khả thi.

#### Giai đoạn 3: giảm $$\parallel r(x,u,v) \parallel$$
* Cập nhật $$\theta = \beta \theta$$ cho đến khi $$\| r(x^+,u^+,v^+) \| \le (1-\alpha \theta) \| r(x,u,v) \|$$.

Cập nhật ở Giai đoạn 3 giống với thuật toán backtracking line search chuẩn.

Vế phải của điều kiện có thể được suy ra như sau. Trước hết, từ phương pháp Newton ta có
> $$\begin{align}
\Delta w = (\Delta x, \Delta u, \Delta v) &\approx -r^{\prime}(w)^{-1} r(w) \\\\
\Leftrightarrow r(w)  &\approx  -r^{\prime}(w) \Delta w \\\\
\end{align}$$

Vì $$r^{\prime}(w) \Delta w \approx -r(w)$$, thay vào khai triển Taylor bậc nhất ta được
> $$\begin{align}
r(w + \theta \Delta w) & \approx r(w) +  r^{\prime}(w) (\theta \Delta w) \\\\
&\approx (1-\theta) r(w) \\\\
\end{align}$$

Do đó, $$r(w + \alpha \theta \Delta w) \approx (1-\alpha  \theta) r(w)$$.
