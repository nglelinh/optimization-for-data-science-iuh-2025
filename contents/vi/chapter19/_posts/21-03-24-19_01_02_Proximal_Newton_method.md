---
layout: post
title: '19-01-02 Phương pháp Newton proximal'
chapter: '19'
order: 4
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

Ở bài 19-01-01, ta thấy proximal gradient descent chỉ đơn giản là cực tiểu hóa xấp xỉ bậc hai đẳng hướng của $$g$$ cộng với $$h$$. Bây giờ hãy thực hiện một cú nâng cấp trực diện: giữ nguyên hoàn toàn triết lý đó, nhưng thay ma trận đơn vị tỉ lệ $$\frac{1}{t}I$$ bằng **ma trận Hessian thực** $$H^{(k-1)} = \nabla^2 g(x^{(k-1)})$$! Kết quả là **phương pháp Newton proximal**: một thuật toán từng xuất hiện sớm trong thống kê dưới tên gọi *local score*, nay trở thành trụ cột của tối ưu hóa tổng hợp bậc hai.

## Kiến thức cần nhớ: Bốn mảnh ghép cấu thành thuật toán Newton proximal

Để hiểu thấu đáo cấu trúc hai bước (tìm hướng $$v^{(k)}$$ rồi chọn bước $$t_k$$) của thuật toán trong bài, hãy tách riêng bốn yếu tố:

- **Bài toán con tìm hướng $$v^{(k)}$$:** Thay vì cộng $$v^{(k)}$$ trực tiếp từ một công thức đóng như Newton cổ điển $$-H^{-1}\nabla g$$, ta giải $$\min_v \nabla g(x)^T v + \frac{1}{2}v^T H v + h(x + v)$$. Lưu ý phần không trơn $$h(x + v)$$ được giữ nguyên không hề xấp xỉ!
- **Tính hướng giảm (Descent Direction):** Khi $$H \succ 0$$, hướng $$v^{(k)}$$ thu được luôn thỏa mãn $$\nabla g(x)^T v + h(x + v) - h(x) \le -v^T H v < 0$$ (nếu $$x$$ chưa tối ưu). Nhờ vậy, chắc chắn tồn tại độ dài bước $$t_k > 0$$ làm giảm chặt hàm tổng hợp $$f = g + h$$.
- **Độ dài bước $$t_k \in (0, 1]$$:** Ta cập nhật $$x^{(k)} = x^{(k-1)} + t_k v^{(k)}$$. Vì $$h$$ lồi, phép tổ hợp lồi $$x + t_k v = (1 - t_k)x + t_k(x + v)$$ luôn bảo toàn miền xác định của $$h$$ (ví dụ luôn giữ nghiệm khả thi nếu $$h = I_C$$).
- **Khi $$h \equiv 0$$:** Bài toán con rút gọn về $$\min_v \nabla g(x)^T v + \frac{1}{2}v^T H v \implies v = -H^{-1}\nabla g(x)$$, quay về chính xác phương pháp Newton cổ điển!

### Giải thích: Tính tay 1 bước Newton proximal cho hồi quy Logistic có phạt $$\ell_1$$

Xét bài toán 1 chiều mô phỏng hồi quy logistic có điều chuẩn Lasso:

$$\min_{x \in \mathbb{R}} \; \underbrace{\log(1 + e^{-x})}_{g(x)} + \underbrace{0.2 |x|}_{h(x)}.$$

Ta có $$g'(x) = \frac{-e^{-x}}{1 + e^{-x}} = -\frac{1}{1 + e^x}$$ và $$g''(x) = \frac{e^x}{(1 + e^x)^2}$$. Hãy tính một bước Newton proximal xuất phát từ $$x^{(0)} = 0$$:

1. **Tính đạo hàm bậc nhất và bậc hai của $$g$$ tại $$x^{(0)} = 0$$:**
   $$g'(0) = -\frac{1}{2} = -0.5, \qquad H^{(0)} = g''(0) = \frac{1}{4} = 0.25.$$
2. **Thiết lập bài toán con tìm hướng $$v^{(1)}$$:**
   $$v^{(1)} = \arg\min_{v} \left\{ -0.5 v + \frac{1}{2}(0.25) v^2 + 0.2 |0 + v| \right\} = \arg\min_{v} \left\{ 0.125(v - 2)^2 + 0.2|v| \right\}.$$
3. **Giải chính xác bài toán con bằng ngưỡng mềm:** Chia hàm mục tiêu con cho $$H^{(0)} = 0.25$$ cho dạng chuẩn $$\frac{1}{2}(v - 2)^2 + \frac{0.2}{0.25}|v| = \frac{1}{2}(v - 2)^2 + 0.8|v|$$. Suy ra:
   $$v^{(1)} = S_{0.8}(2) = 2 - 0.8 = 1.2.$$
4. **Kiểm tra độ giảm hàm mục tiêu với bước đơn vị $$t_1 = 1$$ ($$x^{(1)} = 1.2$$):**
   - Tại $$x^{(0)} = 0$$: $$f(0) = \log(2) + 0 \approx 0.6931$$.
   - Tại $$x^{(1)} = 1.2$$: $$f(1.2) = \log(1 + e^{-1.2}) + 0.2(1.2) \approx 0.2633 + 0.2400 = 0.5033$$ (giảm rất mạnh!).
   - Kiểm tra độ gần nghiệm tối ưu thực $$x^\star = \ln(4) \approx 1.3863$$ (nơi $$g'(x^\star) = -0.2$$): chỉ sau **1 bước**, ta đã nhảy từ $$0$$ lên $$1.2$$, sát nghiệm thực $$1.3863$$!

---

Ở phần trước, ta đã thấy **phương pháp Newton proximal** thay thế độ cong đẳng hướng $$\frac{1}{t} I$$ trong **proximal gradient descent** bằng ma trận Hessian cục bộ $$\nabla^2 g(x)$$. Ý tưởng này từng được nghiên cứu sớm trong thống kê dưới tên gọi "local score".

Dưới đây là cách xây dựng tường minh thuật toán **Newton proximal**.

## Thuật toán
Mỗi vòng lặp của phương pháp Newton proximal gồm hai bước: tìm hướng cập nhật $$v$$ và chọn độ dài bước $$t_k$$.

* **Bước 1:** Khởi tạo từ điểm ban đầu $$x^{(0)}$$ và lặp với $$k = 1, 2, 3, \dots$$

* **Bước 2:** Tìm hướng bước $$v^{(k)}$$ bằng cách giải bài toán con bậc hai có điều chuẩn:

> \begin{align}
v^{(k)} & = \underset{v}{\text{argmin}} \ \nabla g(x^{(k-1)})^T v + \frac{1}{2} v^T H^{(k-1)} v + h(x^{(k-1)} + v)
\end{align}

trong đó $$H^{(k-1)} = \nabla^2 g(x^{(k-1)})$$ là ma trận Hessian của $$g$$ tại $$x^{(k-1)}$$.

* **Bước 3:** Cập nhật điểm lặp theo hướng $$v^{(k)}$$ với độ dài bước $$t_k$$:

> \begin{align}
x^{(k)} & =x^{(k-1)} + t_k v^{(k)}
\end{align}

Khi chọn cố định $$t_k = 1$$, ta thu được phương pháp Newton proximal thuần túy. Trong thực tế, độ dài bước $$t_k$$ thường được xác định qua tìm kiếm theo đường lui (backtracking line search).

#### Cách viết theo điểm đích $$z$$
Nếu biểu diễn bài toán con theo điểm đích $$z = x^{(k-1)} + v$$ thay vì hướng $$v$$, công thức cập nhật trở thành:

> $$
> \begin{align}
> z^{(k)} & = \underset{z}{\text{argmin}} \ \nabla g(x^{(k-1)})^T (z - x^{(k-1)}) + \frac{1}{2} (z - x^{(k-1)})^T H^{(k-1)} (z - x^{(k-1)}) + h(z) \\\\
> x^{(k)} & =x^{(k-1)} + t_k (z^{(k)} - x^{(k-1)} )
> \end{align}
> $$

Về mặt trực giác, ở bước đầu ta tìm điểm trung gian $$z^{(k)}$$ cực tiểu hóa mô hình bậc hai của $$g$$ cộng với $$h$$, sau đó di chuyển từ $$x^{(k-1)}$$ về phía $$z^{(k)}$$ theo tỷ lệ $$t_k \in (0, 1]$$ (không nhất thiết đi trọn bước tới $$z^{(k)}$$).
