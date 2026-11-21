---
layout: post
title: '22-04 Tính chất và các biến thể'
chapter: '22'
order: 5
owner: YoungJae Choung
categories:
- chapter22
lang: vi
---

## Một số biến thể
Hãy xem một số biến thể của phương pháp gradient có điều kiện:<br>
• **Line search**: Thay vì cố định $$γ_k=2/(k+1),k=1,2,3,...$$, ta dùng exact line search cho kích thước bước ở mỗi $$k = 1, 2, 3, . . .$$.
> $$γ_k = \arg\min_{γ∈[0,1]} f\Bigl( x^{(k−1)} + γ\bigl(s^{(k−1)} − x^{(k−1)} \bigr) \Bigr)$$

Cũng có thể dùng backtracking.

• **Fully corrective**: Cập nhật trực tiếp theo phương trình sau.
> $$x^{(k)} = \arg\min_y f(y) \: \text{ subject to } y ∈ conv\{ x^{(0)}, s^{(0)}, . . . s^{(k−1)} \}$$

Phương pháp này có thể đạt tiến bộ tốt hơn nhiều, nhưng chi phí cao.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter22/away_steps.png" alt="[Hình 3] Động lực của away step [3]">
  <figcaption style="text-align: center;">[Hình 3] Động lực của away step [3]</figcaption>
</p>
</figure>
<br>


## Một biến thể khác: away steps
Để có lời giải nhanh hơn, hãy xem bài toán cực tiểu hóa ở [Hình 3]. Ở đây, nghiệm tối ưu là (0,0). Phương pháp gradient có điều kiện khó di chuyển ra khỏi điểm khởi đầu (0,1). Tuy nhiên, nhờ chuyển động away step, gradient có điều kiện không chỉ di chuyển đến các điểm triển vọng mà còn di chuyển ra xa các điểm không triển vọng.



Giả sử bao lồi $$C = conv(A)$$ với tập nguyên tử (atom) $$A$$.

Ta có thể biểu diễn tường minh $$x∈C$$ như một tổ hợp lồi của các phần tử thuộc $$A$$.
> $$x = \sum_{a∈A} λ_a(x)a$$

Gradient có điều kiện với away steps: \\
$$\text{1. chọn } x^{(0)} = a^{(0)} ∈ A$$ \\
$$\text{2. với } k = 1, 2, 3, . . .$$ \\
$$\qquad s^{(k−1)} ∈ \arg\min_{a∈A} ∇f(x^{(k−1)})^Ta,$$
$$\qquad a^{(k−1)} ∈ \arg\max_{a∈A, λa(x(k−1))>0} ∇f(x^{(k−1)})^Ta$$
$$\qquad \text{chọn } v = s^{(k−1)} − x^{(k−1)} \text{ hoặc } v = x^{(k−1)} − a^{(k−1)}$$
$$\qquad x^{(k)} = x^{(k−1)} + γ_kv$$ \\
$$\text{3. kết thúc}$$


## Hội tụ tuyến tính
Xét bài toán không ràng buộc sau.
> $$\min_x f(x) \: \text{ subject to } x ∈ \mathbb{R}^n$$

Ở đây, $$f$$ là µ-lồi mạnh và $$∇f$$ là L-Lipschitz.

Lặp gradient descent $$x^{(k+1)} = x^{(k)} − t_k∇f(x^{(k)})$$ với $$t_k = 1/L$$, ta có bất đẳng thức sau.
> $$f(x^{(k)}) − f^{\star} ≤ \Bigl( 1 −\frac{µ}{L} \Bigr)^k \bigl( f(x^{(0)}) − f^{\star} \bigr)$$

Bây giờ hãy xét thêm bài toán có ràng buộc sau.
> $$\min_x f(x) \: \text{ subject to } x ∈ conv(A) ⊆ \mathbb{R}^n$$

### [Định lý (Lacoste-Julien & Jaggi 2013)]
Giả sử $$f$$ là µ-lồi mạnh, $$∇f$$ là L-Lipschitz, và $$A ⊆ \mathbb{R}^n$$ hữu hạn.

Với $$γ_k$$ thích hợp, các vòng lặp do thuật toán gradient có điều kiện sinh ra luôn thỏa mãn:
> $$f(x^{(k)}) − f^{\star} ≤ (1 − r)^{k/2}(f(x^{(0)}) − f^{\star}) \text { for } r = \frac{µ}{L}·\frac{Φ(A)^2}{4\text{diam}(A)^2}$$
> $$\text{trong đó }Φ(A) = \min_{F ∈faces(conv(A))} dist(F, conv(A \setminus F))$$
 
Nếu đa diện là phẳng (planar) thì $$Φ$$ nhỏ và thuật toán hội tụ chậm.


## Path following
Hãy xét bài toán ràng buộc theo chuẩn sau
> $$\min_x f(x) \: \text{ subject to } \| x \| ≤ t$$

Thuật toán Frank-Wolfe có thể được dùng cho **path following** (bám theo đường nghiệm), nghĩa là nó có thể sinh ra một đường nghiệm (xấp xỉ) $$\hat{x}(t), t ≥ 0$$.

Bắt đầu với $$t_0 = 0$$ và $$x^{\star}(0) = 0$$, cố định các tham số $$\epsilon, m > 0$$ rồi lặp với $$k=1,2,3,...$$.

* Tính $$t_k = t_{k−1} + \frac{(1 − 1/m)\epsilon}{\| ∇f(\hat{x}(t_{k−1}))\|_{∗}}$$ và đặt $$\hat{x}(t) = \hat{x}(t_{k−1})$$ cho mọi $$t ∈ (t_{k−1}, t_k)$$.

* Tại $$t = t_k$$, chạy Frank-Wolfe để tính $$\hat{x}(t_k)$$ và dừng khi khoảng cách đối ngẫu $$≤ \frac{\epsilon}{m}$$.

Đây là phương pháp đơn giản hóa các chiến lược hiện có. [Giesen et al. (2012)]

Nhờ chiến lược **path following** này, ta có thể đảm bảo điều sau với mọi $$t$$ được ghé qua:
> $$f(\hat{x}(t)) − f(x^{\star}(t)) ≤ \epsilon$$

Nghĩa là, nó sinh ra khoảng cách dưới tối ưu (suboptimality gap) bị chặn đều bởi $$\epsilon$$ với mọi $$t$$.

Như thấy ở phương trình dưới đây, khoảng cách đối ngẫu Frank-Wolfe có thể được định nghĩa lại như sau:
> $$g_t(x) = \max_{\|s\|≤t} ∇f(x)^T(x − s) = ∇f(x)^Tx + t\|∇f(x)\|_{∗}$$

Đây là một hàm tuyến tính theo $$t$$. Do đó, nếu $$g_t(x) ≤ \frac{\epsilon}{m}$$, ta có thể tăng $$t$$ lên $$t^+ = t + (1 − 1/m)\epsilon/\|∇f(x)\|_{∗}$$ và có phương trình sau.

> $$g_t+ (x) = ∇f(x)^Tx + t\|∇f(x)\|_{∗} + \epsilon − \epsilon/m ≤ \epsilon$$

Nghĩa là, khoảng cách đối ngẫu được duy trì $$≤ \epsilon$$ giữa $$t$$ và $$t^+$$ với cùng $$x$$.
