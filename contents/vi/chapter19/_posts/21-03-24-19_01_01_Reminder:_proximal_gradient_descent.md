---
layout: post
title: '19-01-01 Nhắc lại: proximal gradient descent'
chapter: '19'
order: 3
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

Trước khi leo lên bậc thang của phương pháp bậc hai, ta cần đứng thật vững trên bậc thang bậc nhất. Proximal gradient descent (PGD) không chỉ là một công thức mẹo vặt ghép bước gradient với toán tử $$\operatorname{prox}_t$$ — đằng sau nó là một diễn giải hình học tuyệt đẹp: ở mỗi bước, ta thay thế hàm trơn $$g$$ bằng xấp xỉ bậc hai cầu (isotropic quadratic approximation) có độ cong $$\frac{1}{t}I$$, giữ nguyên hàm không trơn $$h$$, rồi tìm cực tiểu chính xác của mô hình đó. Chính diễn giải "xấp xỉ bậc hai cộng $$h$$" này là cầu nối tự nhiên nhất sang Newton proximal.

## Bản đồ kiến thức nền: Ba trụ cột của Proximal Gradient Descent

Ôn lại nhanh ba khái niệm cốt lõi từ Chương 9 dưới góc nhìn mở đường cho Chương 19:

- **Toán tử proximal $$\operatorname{prox}_t(x)$$:** Định nghĩa là $$\arg\min_z \left(\frac{1}{2t}\|x - z\|_2^2 + h(z)\right)$$, dung hòa giữa việc giữ $$z$$ gần điểm tham chiếu $$x$$ và việc làm nhỏ hàm không trơn $$h(z)$$. Với $$h(z) = \lambda\|z\|_1$$, nó là phép ngưỡng mềm (soft-thresholding); với $$h(z) = I_C(z)$$, nó là phép chiếu Euclid lên tập lồi $$C$$.
- **Diễn giải cực tiểu hóa mô hình thay thế (Majorization–Minimization):** Nếu $$\nabla g$$ liên tục Lipschitz với hằng số $$L$$ và chọn $$t \le 1/L$$, mô hình $$g(x) + \nabla g(x)^T(y-x) + \frac{1}{2t}\|y-x\|_2^2 + h(y)$$ luôn nằm phía trên hàm thực $$g(y) + h(y)$$, nên mỗi bước PGD chắc chắn làm giảm giá trị hàm mục tiêu.
- **Giới hạn của độ cong đẳng hướng $$\frac{1}{t}I$$:** Dùng chung một vô hướng $$1/t$$ cho mọi chiều buộc thuật toán phải thu nhỏ bước đi theo chiều cong gắt nhất ($$L$$), gây chậm trễ nghiêm trọng trên các chiều thoải hơn — tạo ra khoảng trống để Newton proximal thay $$\frac{1}{t}I$$ bằng $$\nabla^2 g(x)$$.

### Khung giải thích (nên đọc chậm): Tính tay bước PGD với ngưỡng mềm (Soft-Thresholding)

Xét bài toán Lasso 1 chiều:

$$\min_{x \in \mathbb{R}} \; f(x) = \underbrace{\frac{1}{2}(x - 3)^2}_{g(x)} + \underbrace{1.5 |x|}_{h(x)}.$$

Ta có $$\nabla g(x) = x - 3$$ (hằng số Lipschitz $$L = 1$$). Nghiệm tối ưu chính xác thỏa mãn $$0 \in (x^\star - 3) + 1.5\,\partial|x^\star| \implies x^\star = 1.5$$. Hãy chạy tay PGD từ $$x^{(0)} = 0$$ với hai lựa chọn bước học:

1. **Với bước học $$t = 0.5$$ (nhỏ hơn $$1/L = 1$$):**
   - Gradient tại $$x^{(0)} = 0$$ là $$\nabla g(0) = -3$$.
   - Bước gradient trơn: $$u = x^{(0)} - t\nabla g(0) = 0 - 0.5(-3) = 1.5$$.
   - Áp dụng toán tử proximal với ngưỡng $$\lambda t = 1.5 \times 0.5 = 0.75$$:
     $$x^{(1)} = S_{0.75}(1.5) = \operatorname{sign}(1.5)\max(|1.5| - 0.75, \; 0) = 0.75.$$
   - Kiểm tra giá trị hàm: $$f(0) = 4.5$$ giảm mạnh xuống $$f(0.75) = \frac{1}{2}(-2.25)^2 + 1.5(0.75) = 2.53125 + 1.125 = 3.65625$$.
2. **Với bước học tối ưu $$t = 1/L = 1$$:**
   - Bước gradient trơn: $$u = 0 - 1(-3) = 3$$.
   - Ngưỡng mềm với $$\lambda t = 1.5$$: $$x^{(1)} = S_{1.5}(3) = 3 - 1.5 = 1.5 = x^\star$$!
   Lưu ý: khi $$g(x)$$ là hàm bậc hai 1 chiều, chọn $$t = 1/g''(x)$$ khiến mô hình bậc hai của PGD trùng khớp hoàn toàn với Newton proximal!

---

Trước khi đi vào **phương pháp Newton proximal (proximal Newton method)**, hãy ôn lại ngắn gọn **proximal gradient descent**.

Xem chi tiết tại [09 Proximal Gradient Descent and Acceleration]({% multilang_post_url contents/chapter09/20-01-08-09_proximal_gradient_descent_and_acceleration %}).

## Proximal gradient descent
**Proximal gradient descent** áp dụng cho bài toán tối ưu hàm tổng hợp có dạng:

>$$f(x) = g(x) + h(x)$$

* $$g$$ lồi và khả vi với $$\operatorname{dom}(g) = \mathbb{R}^n$$.
* $$h$$ lồi, có thể không khả vi nhưng có cấu trúc "đơn giản".


#### Thuật toán
Bắt đầu từ điểm khởi tạo $$x^{(0)}$$, thuật toán lặp lại phép cập nhật:

>$$x^{(k)} = \text{prox}_{t_k}(x^{(k-1)} - t_k \nabla g(x^{(k-1)}) ),\quad k=1,2,3,\dots$$

trong đó $$\text{prox}_{t}(\cdot)$$ là toán tử proximal ứng với hàm $$h$$:

> \begin{align}
\text{prox}_{t}(x) = \underset{z}{\text{argmin}} \ \frac{1}{2t} \parallel x - z \parallel_2^2 + h(z)
\end{align}

Phép cập nhật này cũng có thể được viết lại dưới dạng tương tự gradient descent nhờ ánh xạ gradient tổng quát $$G_{t}$$:

> \begin{align}
> x^{(k)} = x^{(k-1)} - t_k \cdot G_{t_k}(x^{(k-1)}), \space \space \text{với} \space G_{t}(x) = \frac{x-\text{prox}_{t} (x - t \nabla g(x))}{t} \\\\
> \end{align}

#### Hiệu năng
* Hiệu năng của **proximal gradient descent** phụ thuộc trực tiếp vào $$h$$. Nếu $$h$$ phức tạp — đặc biệt khi toán tử prox không có nghiệm dạng đóng — thì mỗi vòng lặp sẽ tốn kém và thuật toán chạy chậm.

* Thuật toán có cùng tốc độ hội tụ theo số vòng lặp với gradient descent trên $$g$$, nhưng chỉ thực sự hiệu quả khi toán tử prox được tính nhanh ở mỗi bước.

## Động lực
Trong **proximal gradient descent**, ở mỗi bước ta xấp xỉ hàm khả vi $$g$$ bằng mô hình bậc hai cục bộ, giữ nguyên phần không khả vi $$h$$ và cực tiểu hóa tổng hai thành phần đó (xem chi tiết tại [09-01 Proximal gradient descent]({% multilang_post_url contents/chapter09/20-01-08-09_01_proximal_gradient_descent %})):

> $$
> \begin{align}
x^+ & = \underset{z}{\text{argmin}}  \, \frac{1}{2t} \parallel x - t \nabla g(x) - z \parallel_2 ^2 + h(z) \\\\
> & = \underset{z}{\text{argmin}} \ \nabla g(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2 + h(z) \\\\
> \end{align}
> $$

Hai số hạng đầu tiên của biểu thức thứ hai xuất phát từ khai triển Taylor bậc hai của $$g$$ (bỏ hằng số $$g(x)$$), trong đó ma trận Hessian $$\nabla^2 g(x)$$ được thay đơn giản bằng $$\frac{1}{t} I$$ (độ cong đẳng hướng — spherical curvature).

Hình dưới đây minh họa cách xấp xỉ bậc hai được dùng để cập nhật nghiệm trong proximal gradient descent.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.01_01_proximal_gradient_descent.png" alt="[Hình 1] Các bước cập nhật của proximal gradient descent [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Các bước cập nhật của proximal gradient descent [3]</figcaption>
</p>
</figure>

Điểm khác biệt cốt lõi giữa gradient descent và phương pháp Newton là việc sử dụng Hessian cục bộ $$\nabla^2 g(x)$$ trong mô hình bậc hai. Nếu thay $$\frac{1}{t} I$$ bằng đúng ma trận Hessian $$\nabla^2 g(x)$$ trong bài toán con ở trên, ta thu được **phương pháp Newton proximal**, sẽ được trình bày ở phần tiếp theo.
