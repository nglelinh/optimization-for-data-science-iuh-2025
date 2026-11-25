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

Trước khi cải tiến một cỗ máy, người kỹ sư giỏi luôn tháo nó ra xem từng bánh răng hoạt động ra sao. Phương pháp chắn (barrier method) ở Chương 15 thực ra đã ẩn chứa sẵn một bộ biến đối ngẫu cực kỳ đẹp mắt ngay tại mỗi điểm trên đường trung tâm $$x^\star(t)$$. Khi viết lại điều kiện tối ưu của bài toán chắn dưới góc nhìn đối ngẫu, ta sẽ bất ngờ nhận ra rằng khoảng cách tối ưu đúng bằng $$m/t$$ không phải là một ước lượng ngẫu nhiên, mà là hệ quả trực tiếp của điều kiện KKT bị nhiễu.

## Bản đồ kiến thức nền: Cầu nối từ hàm chắn sang điều kiện KKT bị nhiễu

Bài ôn tập này móc nối bốn khái niệm then chốt từ các chương trước thành một khung thống nhất duy nhất:

- **Hàm chắn logarit (Logarithmic Barrier):** Thay vì ép cứng ràng buộc $$h_i(x) \le 0$$, ta cộng thêm $$-\frac{1}{t}\sum_{i=1}^m \log(-h_i(x))$$ để dựng một "bức tường vô hạn" dọc theo biên miền khả thi, biến bài toán có bất đẳng thức thành chuỗi bài toán chỉ có ràng buộc đẳng thức.
- **Điều kiện dừng của bài toán chắn:** Đạo hàm của $$tf(x) - \sum_{i=1}^m \log(-h_i(x))$$ bằng không tạo ra trọng số tự nhiên $$u_i^\star(t) = -\frac{1}{t h_i(x^\star(t))} > 0$$. Đây chính là cách biến đối ngẫu "tự lộ diện" từ bài toán gốc.
- **Hàm đối ngẫu Lagrange và chứng chỉ tối ưu:** Thay cặp $$(u^\star(t), v^\star(t))$$ vào hàm đối ngẫu $$g(u, v)$$ cho phép chứng minh chính xác $$f(x^\star(t)) - p^\star \le f(x^\star(t)) - g(u^\star(t), v^\star(t)) = m/t$$.
- **Diễn giải KKT bị nhiễu:** Nhân hai vế công thức định nghĩa $$u_i^\star(t)$$ với $$-h_i(x^\star(t))$$ cho ra $$-u_i^\star(t) h_i(x^\star(t)) = 1/t$$ — phiên bản làm trơn của điều kiện bù chặt $$u_i h_i(x) = 0$$.

### Khung giải thích (nên đọc chậm): Tính tay điểm đường trung tâm và kiểm chứng khoảng cách đối ngẫu $$m/t$$

Xét bài toán lồi 1 biến với $$m = 1$$ ràng buộc bất đẳng thức:

$$\min_{x} f(x) = x^2 \qquad \text{với điều kiện} \qquad h(x) = 1 - x \le 0 \quad (\text{tức } x \ge 1).$$

Nghiệm chính xác dễ thấy là $$x^\star = 1$$, giá trị tối ưu $$p^\star = 1$$. Bây giờ hãy giải bài toán chắn $$\min_{x > 1} \; t x^2 - \log(x - 1)$$ bằng tay:

1. **Điều kiện dừng:** Đạo hàm theo $$x$$ bằng $$0$$ cho phương trình $$2tx - \frac{1}{x - 1} = 0 \iff 2tx^2 - 2tx - 1 = 0$$.
2. **Tại $$t = 1$$:** Phương trình là $$2x^2 - 2x - 1 = 0$$, nghiệm lớn hơn $$1$$ là $$x^\star(1) = \frac{1 + \sqrt{3}}{2} \approx 1.3660$$. Khi đó $$f(x^\star(1)) \approx 1.8660$$.
3. **Suy ra biến đối ngẫu từ điểm chắn:** $$u^\star(1) = -\frac{1}{t h(x^\star(1))} = \frac{1}{1 \cdot (1.3660 - 1)} \approx 2.7321 > 0$$.
4. **Kiểm chứng hàm đối ngẫu và khoảng cách $$m/t$$:** Với $$u > 0$$, hàm đối ngẫu là $$g(u) = \min_x (x^2 + u(1 - x)) = u - \frac{u^2}{4}$$. Tại $$u^\star(1) \approx 2.7321$$, ta có $$g(u^\star(1)) = 2.7321 - \frac{2.7321^2}{4} \approx 0.8660$$. Hiệu số $$f(x^\star(1)) - g(u^\star(1)) = 1.8660 - 0.8660 = 1.0000 = \frac{1}{t}$$ — khớp tuyệt đối với công thức $$m/t$$!
5. **Tăng lên $$t = 10$$:** Giải $$20x^2 - 20x - 1 = 0$$ được $$x^\star(10) = \frac{20 + \sqrt{480}}{40} \approx 1.0477$$, lúc này $$f(x^\star(10)) - g(u^\star(10)) = \frac{1}{10} = 0.1$$, và điểm $$x^\star(t)$$ tiến sát nghiệm $$x^\star = 1$$.

---

Ở Chương 15 chúng ta đã tìm hiểu phương pháp chắn (barrier method), còn ở Chương 13 và Chương 16 chúng ta đã xét lý thuyết đối ngẫu. Trước khi đi sâu vào nội dung chương này, ta ôn lại ngắn gọn các khái niệm cốt lõi đó.

## Phương pháp chắn
Xét bài toán gốc (primal) lồi với các hàm $$f, h_i \ (i = 1, \dots, m)$$ khả vi:
> $$\begin{align}
> &\min_{x} && f(x) \\
> &\text{subject to } &&h_{i}(x) \leq 0, i = 1, \dotsc, m \\
> &&& Ax = b \\
> \end{align}$$

Sử dụng hàm chắn logarit, ta chuyển bài toán gốc sang bài toán chắn tương ứng:

> $$\begin{align}
> & \min_{x} && f(x) + \frac{1}{t} \phi(x) & \qquad & \min_{x} && tf(x) + \phi(x) \\
> & \text{subject to } && Ax = b & \iff \qquad & \text{subject to } && Ax = b \\
> & \text{where } && \phi(x) = - \sum_{i=1}^{m} \log(-h_i(x))
> \end{align}$$

Thuật toán khởi tạo với $$t = t^{(0)} > 0$$ và tăng dần $$t$$ cho đến khi $$\frac{m}{t} \le \epsilon$$. Tại mỗi vòng lặp $$k = 0, 1, 2, \dots$$, phương pháp Newton được dùng để giải bài toán chắn nhằm tìm $$x^{\star}(t)$$ với điểm khởi tạo $$x^{(k)}$$, rồi gán $$x^{(k+1)} = x^{\star}(t)$$.

Thuật toán có thể được tóm tắt như sau:

1. Chọn $$t^{(0)} \gt 0$$ và đặt $$k := 0$$.
2. Giải bài toán chắn tại $$t = t^{(0)}$$ để tìm $$x^{(0)} = x^{\star}(t^{(0)})$$.
3. Khi $$m/t^{(k)} \gt \epsilon$$, lặp:<br>
  3-1. Cập nhật $$t^{(k+1)} = \mu t^{(k)}$$ với $$\mu > 1$$.<br>
  3-2. Khởi tạo phương pháp Newton từ $$x^{(k)}$$ (khởi động ấm — warm start) và giải bài toán chắn tại $$t = t^{(k+1)}$$ để tìm $$x^{(k+1)} = x^{\star}(t^{(k+1)})$$.<br>
  3-3. Tăng $$k := k + 1$$.<br>

* Xem chi tiết tại [15-01-02 Hàm chắn logarit và phương pháp chắn]({% multilang_post_url contents/chapter15/21-03-28-15_01_02_log_barrier_function_and_barrier_method %}).

## Đối ngẫu
Xét bài toán gốc:
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad f(x) \\\\
>    \text{subject to} &\quad Ax = b \\\\
>    &\quad h(x) \le 0
>\end{align}
>$$

Hàm Lagrange tương ứng là:
>$$
>L(x,u,v) = f(x) + u^Th(x) + v^T(Ax - b)
>$$

Từ hàm Lagrange này, bài toán gốc và bài toán đối ngẫu có thể được viết lại như sau (xem chi tiết tại Chương 16):<br>
### Bài toán gốc
>$$
>\min_x \mathop{\max_{u,v}}_{u \geq 0} L(x,u,v)
>$$

### Bài toán đối ngẫu
>$$
>\mathop{\max_{u,v}}_{u \geq 0} \min_x L(x,u,v)
>$$

## Điều kiện tối ưu

Khi $$f, h_1, \dots, h_m$$ lồi, khả vi và bài toán thỏa mãn tính đối ngẫu mạnh, các điều kiện tối ưu KKT có dạng:

> $$
> \begin{array}{rcl}
> \nabla f(x) +\nabla h(x)u + A^Tv & = & 0 & \text{(Tính dừng)}\\\
>  Uh(x) & = & 0 & \text{(Bù chặt)} \\\
> Ax & = & b & \text{(Khả thi gốc)}\\\
> u,-h(x)  & \ge & 0 & \text{(Khả thi gốc và đối ngẫu)}
> \end{array}
> $$

Trong đó, $$U = \text{diag}(u)$$ và $$\nabla h(x) = [ \nabla h_1(x) \ \cdots \ \nabla h_m(x) ]$$.

* Xem chi tiết tại [Chương 12 Điều kiện KKT]({% multilang_post_url contents/chapter12/21-04-02-12_00_KKT_conditions %}).

## Phương trình đường trung tâm
Ta có thể viết lại bài toán chắn theo tham số $$\tau = \frac{1}{t}$$. Khi cho $$\tau$$ tiến dần về $$0$$ và giải lặp lại bài toán chắn, ta thu được nghiệm hội tụ về nghiệm tối ưu của bài toán gốc:

>$$
>\begin{align}
>&\min_{x} && {f(x) + \tau\phi(x)} \\\\
>& &&{Ax = b} \\\
>& \text{where } && \phi(x) = -\sum_{i=1}^m \log(-h_i(x)).
>\end{align}
>$$

Như vậy, mức sai khác so với bài toán gốc phụ thuộc vào $$\tau$$, và tập hợp các nghiệm tương ứng theo tham số $$\tau > 0$$ tạo thành quỹ đạo gọi là **đường trung tâm (central path)**.

Các điều kiện tối ưu cho bài toán chắn là:
> $$
> \begin{array}{rcl}
> \nabla f(x) +\nabla h(x)u + A^Tv  & = & 0 \\\
> Uh(x) & = & -\tau\mathbb{1} \\\
> Ax & = & b \\\
> u,-h(x)  & > & 0
> \end{array}
> $$
 
* Xem chi tiết tại [16-02 Điều kiện tối ưu]({% multilang_post_url contents/chapter16/21-03-31-16_02_optimality_conditions %}).

**Phương pháp điểm trong gốc-đối ngẫu (Primal-Dual interior-point method)** trong chương này định nghĩa ba phương trình đầu tiên ở trên thành các phần dư (residual) và tìm nghiệm bằng cách đưa chúng tiến về $$0$$.

#### Một tính chất hữu ích
Nghiệm $$(x(\tau), u(\tau), v(\tau))$$ trên đường trung tâm có khoảng cách đối ngẫu (duality gap) đúng bằng $$m\tau = \frac{m}{t}$$:
> $$f(x(\tau))-\min_x L(x,u(\tau),v(\tau)) = m\tau= \frac{m}{t}$$
