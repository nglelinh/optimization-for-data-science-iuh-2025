---
layout: post
title: 06-03-05 Xem xét điều kiện & Tính thực tiễn
chapter: '06'
order: 12
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

## Điều kiện liên tục Lipschitz & Tính lồi mạnh
Hãy xem xét các điều kiện cho tính liên tục Lipschitz và tính lồi mạnh sử dụng $$f(β) = \frac{1}{2} \lVert y−Xβ \rVert_2^2$$ làm ví dụ.

### Tính liên tục Lipschitz của $$∇f$$ :
* Điều này có nghĩa là $$\nabla^2f(x) \preceq LI$$. <br>
* Vì $$∇^2f(β) = X^TX$$, chúng ta có $$L = \sigma^2_{max}(X)$$.<br>


### Tính lồi mạnh của $$f$$ :
* Điều này có nghĩa là $$\nabla^2f(x) \succeq mI$$.<br>
* Vì $$\nabla^2f(β) = X^TX$$, chúng ta có $$m = \sigma_{min}^2(X)$$.<br>
* Nếu $$X$$ là ma trận $$n \times p$$ và $$p > n$$, thì $$\sigma_{min}(X) = 0$$, vậy $$f$$ không thể lồi mạnh.<br>
* Ngay cả khi $$\sigma_{min}(X) > 0$$, số điều kiện $$L/m = \sigma_{max}^2(X)/\sigma_{min}^2(X)$$ có thể rất lớn.


Nếu hàm $$f$$ lồi mạnh và có gradient Lipschitz, thì nó thỏa mãn điều sau. Bạn có thể nghĩ về $$f$$ như được kẹp giữa hai hàm bậc hai.

>$$mI \preceq \nabla^2f(x) \preceq LI \text{ với mọi } x ∈ \mathbb{R}^n$$ và $$L > m > 0$$


Thỏa mãn cả hai điều kiện cho mọi $$x$$ có thể rất mạnh. Tuy nhiên, nếu chúng ta suy nghĩ cẩn thận hơn, chúng ta có thể thấy rằng điều kiện này chỉ cần thiết cho tập mức phụ sau đây.

> $$S = \{x : f(x) \leq f(x^{(0)})\}$$

## Tính thực tiễn

### Tiêu chí dừng cho các thuật toán tối ưu hóa

Trong thực tế, các thuật toán tối ưu hóa cần các tiêu chí dừng được định nghĩa rõ ràng để xác định khi nào chấm dứt quá trình lặp. Dưới đây là những điều kiện dừng phổ biến nhất:

#### 1. **Độ lớn Gradient gần bằng Không:**
Đây là điều kiện dừng lý tưởng cho các bài toán tối ưu hóa không ràng buộc, dựa trên thực tế rằng gradient của hàm mục tiêu bằng không tại các cực trị địa phương.
$$
\|\nabla f(\mathbf{x}_k)\| \leq \epsilon_1
$$
trong đó $$\mathbf{x}_k$$ là điểm hiện tại tại lần lặp $$k$$, và $$\epsilon_1$$ là một ngưỡng dương nhỏ.

Nếu $$x^{\star}$$ là nghiệm, thì $$\nabla f(x^{\star}) = 0$$. Nếu $$f$$ lồi mạnh, thì:
> $$\lVert \nabla f(x) \rVert_2 ≤ \sqrt{2m \epsilon} ⇒ f(x)−f^{\star} ≤ \epsilon$$

#### 2. **Thay đổi nhỏ trong giá trị hàm mục tiêu:**
Thuật toán dừng khi giá trị hàm mục tiêu không còn thay đổi đáng kể giữa các lần lặp liên tiếp.
$$
|f(\mathbf{x}_{k+1}) - f(\mathbf{x}_k)| \leq \epsilon_2
$$
trong đó $$\epsilon_2$$ là một ngưỡng dương nhỏ.

#### 3. **Thay đổi nhỏ trong biến (tham số):**
Thuật toán dừng khi các tham số mô hình không còn thay đổi đáng kể giữa các lần lặp.
$$
\|\mathbf{x}_{k+1} - \mathbf{x}_k\| \leq \epsilon_3
$$
trong đó $$\epsilon_3$$ là một ngưỡng dương nhỏ.

#### 4. **Số lần lặp tối đa:**
Để ngăn thuật toán chạy vô hạn hoặc quá lâu, một giới hạn trên về số lần lặp được đặt.
$$
k \geq \text{MaxIterations}
$$
Đây là điều kiện dừng an toàn đảm bảo thuật toán sẽ chấm dứt trong thời gian hợp lý, ngay cả khi nó chưa đạt được sự hội tụ hoàn hảo.

#### 5. **Thời gian chạy tối đa:**
Tương tự như giới hạn lần lặp tối đa, thuật toán có thể được dừng nếu nó đã chạy quá thời gian cho phép.
$$
\text{ElapsedTime} \geq \text{MaxTime}
$$

#### 6. **Điều kiện kết hợp:**
Trong thực tế, nhiều điều kiện dừng thường được sử dụng kết hợp. Ví dụ, thuật toán dừng nếu *bất kỳ* điều kiện nào ở trên được thỏa mãn. Điều này giúp cân bằng giữa độ chính xác và hiệu quả tính toán.

### [Tham khảo] Quá trình suy dẫn
Quá trình suy dẫn cho phương trình trên như sau.
Vì $$f$$ thỏa mãn tính lồi mạnh, tồn tại hằng số $$m \ge 0$$ sao cho:
> $$ \begin{align}
\nabla^2 f(x) \succeq mI \\
\end{align} $$

Hãy mở rộng hàm $$f$$ bằng chuỗi Taylor bậc hai.
> $$ \begin{align}
f(y) = f(x) + \nabla f(x)^T(y−x) + \frac{1}{2} (y−x)^T \nabla^2 f(x) (y−x), \space \forall x, y
\end{align} $$

Sau đó, theo $$\nabla f(x) \succeq mI$$ ở trên, chúng ta có thể sắp xếp số hạng cuối như một điều kiện cận dưới.
> $$ \begin{align}
f(y) &  \ge f(x) + \nabla f(x)^T(y−x) + \frac{m}{2} \lVert y−x \rVert_2^2, \space \forall x, y
\end{align} $$

Lấy đạo hàm $$f(y)$$ theo $$y$$ cho $$\tilde{y} = x - (1/m) \nabla f(x)$$. Thay $$\tilde{y}$$ vào khai triển Taylor:

> $$ \begin{align}
f(y) &  \ge f(x) + \nabla f(x)^T(\tilde{y}−x) + \frac{m}{2} \lVert \tilde{y}−x \rVert_2^2 \\
&  = f(x) - \frac{1}{2m} \lVert \nabla f(x) \rVert_2^2
\end{align} $$

Do đó, thay $$f(y)$$ bằng $$f^{*}$$ cho:
> $$ \begin{align}
 f^{*}  \ge f(x) - \frac{1}{2m} \lVert \nabla f(x) \rVert_2^2
\end{align} $$

Quy tắc dừng trên được suy dẫn như sau:

> $$ \begin{align}
f(x) - f^{*} \le \frac{1}{2m} \lVert \nabla f(x) \rVert^2_2 & \le \epsilon \\
\lVert \nabla f(x) \rVert^2_2 & \le 2m\epsilon \\
\lVert \nabla f(x) \rVert_2 & \le \sqrt{2m\epsilon} \\
\end{align} $$


### Ưu điểm và nhược điểm của Gradient Descent

### Ưu điểm
* Thuật toán đơn giản và chi phí mỗi lần lặp thấp.
* Rất nhanh cho các bài toán lồi mạnh, có điều kiện tốt.

### Nhược điểm
* Nói chung chậm vì nhiều bài toán không lồi mạnh hoặc có điều kiện tốt.
* Không thể xử lý các hàm không khả vi.