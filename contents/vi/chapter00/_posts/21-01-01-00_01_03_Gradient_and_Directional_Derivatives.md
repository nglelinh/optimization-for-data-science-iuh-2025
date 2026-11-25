---
layout: post
title: 00-01-03 Gradient và Đạo Hàm Theo Hướng
chapter: '00'
order: 5
owner: GitHub Copilot
lang: vi
categories:
- chapter00
lesson_type: required
---

Đứng giữa sườn đồi, bạn có vô số hướng để bước đi: hướng nào giúp hạ độ cao nhanh nhất, hướng nào giữ nguyên độ cao, và nếu bị một hàng rào ràng buộc chặn hướng dốc nhất thì ta vẫn có thể đi xuống theo một hướng xiên khác không? Câu trả lời trọn vẹn nằm ở mối quan hệ cực kỳ thanh lịch giữa **vector gradient** và **đạo hàm theo hướng**: một phép tích vô hướng duy nhất $$D_u f(x) = \nabla f(x)^T u$$.

Đây là công thức nền tảng đứng sau mọi phương pháp hạ bậc nhất (first-order methods), từ Gradient Descent cổ điển cho đến Conditional Gradient (Frank–Wolfe).

## Bản đồ kiến thức nền: Hình học của hướng đi và độ dốc

- **Đạo hàm theo hướng ($$D_u f(x)$$):** Đo tốc độ thay đổi tức thời của $$f$$ khi ta di chuyển từ $$x$$ dọc theo vector đơn vị $$u$$ ($$\|u\|_2 = 1$$). Với hàm khả vi, $$D_u f(x) = \nabla f(x)^T u = \|\nabla f(x)\|_2 \cos\theta$$.
- **Bất đẳng thức Cauchy–Schwarz và hướng dốc nhất:** Vì $$-1 \le \cos\theta \le 1$$, giá trị lớn nhất của $$D_u f(x)$$ là $$+\|\nabla f(x)\|_2$$ khi $$u$$ cùng hướng $$\nabla f(x)$$, và giá trị nhỏ nhất là $$-\|\nabla f(x)\|_2$$ khi $$u$$ ngược hướng $$\nabla f(x)$$.
- **Hướng giảm (Descent Direction):** Bất kỳ vector $$d$$ nào thỏa mãn $$\nabla f(x)^T d < 0$$ (tạo góc tù với gradient) đều bảo đảm $$f(x + \alpha d) < f(x)$$ với bước $$\alpha > 0$$ đủ nhỏ — nền tảng của mọi thuật toán tìm kiếm đường thẳng (line search).
- **Tính trực giao với đường mức:** Khi $$u$$ tiếp tuyến với đường mức $$f(x) = c$$, hàm không đổi dọc theo $$u$$ nên $$\nabla f(x)^T u = 0$$, tức gradient luôn vuông góc với đường mức.

### Khung giải thích (nên đọc chậm): So sánh tốc độ giảm dọc theo hai hướng khác nhau

Xét hàm $$f(x, y) = x^2 + 2y^2$$ tại điểm $$p = (1, 1)^T$$ (giá trị $$f(1, 1) = 3$$):

1. **Tính gradient tại $$p$$:**
   $$\nabla f(x, y) = \begin{pmatrix}2x \\ 4y\end{pmatrix} \implies \nabla f(1, 1) = \begin{pmatrix}2 \\ 4\end{pmatrix}, \qquad \|\nabla f(1, 1)\|_2 = \sqrt{2^2 + 4^2} = \sqrt{20} = 2\sqrt{5} \approx 4.472.$$
2. **Thử đi theo hướng đơn vị $$u = (3/5, 4/5)^T$$:**
   $$D_u f(1, 1) = \nabla f(1, 1)^T u = 2\left(\frac{3}{5}\right) + 4\left(\frac{4}{5}\right) = \frac{6 + 16}{5} = \frac{22}{5} = 4.4 > 0.$$
   Hàm tăng rất nhanh gần sát mức tối đa $$4.472$$ vì $$u$$ gần trùng hướng gradient.
3. **Thử hướng giảm nhanh nhất $$u^* = -\frac{\nabla f(1,1)}{\|\nabla f(1,1)\|_2} = \left(-\frac{1}{\sqrt{5}}, -\frac{2}{\sqrt{5}}\right)^T$$:**
   $$D_{u^*} f(1, 1) = 2\left(-\frac{1}{\sqrt{5}}\right) + 4\left(-\frac{2}{\sqrt{5}}\right) = -\frac{10}{\sqrt{5}} = -2\sqrt{5} \approx -4.472.$$
4. **Thử hướng tiếp tuyến đường mức $$v = (-2/\sqrt{5}, 1/\sqrt{5})^T$$:**
   $$D_v f(1, 1) = 2\left(-\frac{2}{\sqrt{5}}\right) + 4\left(\frac{1}{\sqrt{5}}\right) = 0.$$
   Đi dọc theo $$v$$ giữ nguyên độ cao tức thời (tiếp tuyến với elip $$x^2 + 2y^2 = 3$$ tại $$(1,1)$$).

---

Bài học này trình bày vector gradient và đạo hàm theo hướng — hai khái niệm trung tâm trong tối ưu hóa giúp phân tích cách hàm số biến thiên theo từng hướng di chuyển.

---

## Vector gradient

Gradient $$\nabla f$$ là vector gồm tất cả các đạo hàm riêng bậc nhất của hàm $$f$$ theo từng biến. Tại một điểm cho trước, gradient chỉ theo hướng hàm số tăng nhanh nhất.

### Định nghĩa và cách tính

Với hàm hai biến $$f(x, y)$$, gradient của hàm là:

$$ \nabla f = \begin{pmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{pmatrix} $$

Với hàm $$n$$ biến $$f(x_1, x_2, \ldots, x_n)$$:

$$ \nabla f = \begin{pmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{pmatrix} $$

### Ví dụ: Tính gradient

Xét hàm $$f(x, y) = x^2 + 3xy + y^2$$:

$$\frac{\partial f}{\partial x} = 2x + 3y$$
$$\frac{\partial f}{\partial y} = 3x + 2y$$

Do đó: $$\nabla f = \begin{pmatrix} 2x + 3y \\ 3x + 2y \end{pmatrix}$$

Tại điểm $$(1, 2)$$: $$\nabla f(1, 2) = \begin{pmatrix} 2(1) + 3(2) \\ 3(1) + 2(2) \end{pmatrix} = \begin{pmatrix} 8 \\ 7 \end{pmatrix}$$

---

## Đạo hàm theo hướng

**Đạo hàm theo hướng** đo tốc độ thay đổi của hàm $$f$$ khi di chuyển theo một hướng $$\mathbf{u}$$ bất kỳ, trong đó $$\mathbf{u}$$ là vector đơn vị (có độ dài bằng 1).

### Định nghĩa

Với hàm $$f(\mathbf{x})$$ và vector đơn vị $$\mathbf{u} = \langle u_1, u_2, \ldots, u_n \rangle$$:

$$D_{\mathbf{u}}f(\mathbf{x}) = \nabla f(\mathbf{x}) \cdot \mathbf{u} = \sum_{i=1}^{n} \frac{\partial f}{\partial x_i} u_i$$

### Diễn giải hình học

Đạo hàm theo hướng có thể biểu diễn dưới dạng:

$$D_{\mathbf{u}}f = \lvert \nabla f \rvert \cos \theta$$

trong đó $$\theta$$ là góc giữa $$\nabla f$$ và $$\mathbf{u}$$, còn $$\lvert \nabla f \rvert$$ là độ lớn (chuẩn Euclid) của gradient.

### Ví dụ: Tính đạo hàm theo hướng

Xét lại hàm $$f(x, y) = x^2 + 3xy + y^2$$ tại điểm $$(1, 2)$$ với $$\nabla f(1, 2) = \begin{pmatrix} 8 \\ 7 \end{pmatrix}$$:

**Hướng 1:** $$\mathbf{u}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$ (hướng dương của trục $$x$$)
$$D_{\mathbf{u}_1}f(1, 2) = 8 \cdot 1 + 7 \cdot 0 = 8$$

**Hướng 2:** $$\mathbf{u}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$ (hướng dương của trục $$y$$)
$$D_{\mathbf{u}_2}f(1, 2) = 8 \cdot 0 + 7 \cdot 1 = 7$$

**Hướng 3:** $$\mathbf{u}_3 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$$ (hướng đường chéo 45°)
$$D_{\mathbf{u}_3}f(1, 2) = 8 \cdot \frac{1}{\sqrt{2}} + 7 \cdot \frac{1}{\sqrt{2}} = \frac{15}{\sqrt{2}} \approx 10.61$$

---

## Tốc độ thay đổi lớn nhất và nhỏ nhất

### Các tính chất chính

Từ công thức $$D_{\mathbf{u}}f = \lvert \nabla f \rvert \cos \theta$$, ta suy ra:

1. **Tốc độ thay đổi lớn nhất**: đạt được khi $$\cos \theta = 1$$ (tức $$\theta = 0°$$)
   - Hướng: $$\mathbf{u} = \frac{\nabla f}{\lvert \nabla f \rvert}$$ (cùng hướng với gradient)
   - Giá trị lớn nhất: $$D_{\max}f = \lvert \nabla f \rvert$$

2. **Tốc độ thay đổi nhỏ nhất**: đạt được khi $$\cos \theta = -1$$ (tức $$\theta = 180°$$)
   - Hướng: $$\mathbf{u} = -\frac{\nabla f}{\lvert \nabla f \rvert}$$ (ngược hướng với gradient)
   - Giá trị nhỏ nhất: $$D_{\min}f = -\lvert \nabla f \rvert$$

3. **Tốc độ thay đổi bằng không**: xảy ra khi $$\cos \theta = 0$$ (tức $$\theta = 90°$$)
   - Hướng: mọi vector đơn vị vuông góc với $$\nabla f$$

### Tóm tắt các tính chất của gradient

- Gradient $$\nabla f$$ chỉ theo hướng **tăng nhanh nhất**.
- Vector $$-\nabla f$$ chỉ theo hướng **giảm nhanh nhất**.
- Độ lớn $$\lvert \nabla f \rvert$$ bằng **tốc độ thay đổi lớn nhất**.
- Tại điểm thỏa mãn $$\nabla f = \mathbf{0}$$, ta có **điểm tới hạn** (critical point) — ứng viên cho cực trị của hàm số.

---

## Quan hệ với đường mức

Tại mọi điểm trên một đường mức $$f(x, y) = c$$, vector gradient $$\nabla f$$ luôn **trực giao (vuông góc)** với tiếp tuyến của đường mức tại điểm đó.

### Ý nghĩa của tính trực giao

Tính trực giao giữa gradient và đường mức có ý nghĩa quan trọng vì:

1. **Đường mức ứng với giá trị hàm không đổi**: di chuyển dọc theo tiếp tuyến của đường mức không làm thay đổi giá trị hàm ở bậc nhất, nên đạo hàm theo hướng đó bằng không.
2. **Gradient chỉ theo hướng tăng nhanh nhất**: hướng làm hàm số tăng nhanh nhất phải vuông góc với hướng không làm thay đổi giá trị hàm.
3. **Ứng dụng trong tối ưu hóa**: để tìm cực trị, ta tìm các điểm mà gradient bằng không (điểm tới hạn) hoặc — trong bài toán có ràng buộc — điểm mà gradient vuông góc với biên của tập ràng buộc.

### Ứng dụng trong tối ưu hóa

Hiểu rõ về gradient và đạo hàm theo hướng là cơ sở cho nhiều nội dung trong tối ưu hóa:

1. **Gradient Descent**: di chuyển theo hướng $$-\nabla f$$ để cực tiểu hóa $$f$$.
2. **Gradient Ascent**: di chuyển theo hướng $$+\nabla f$$ để cực đại hóa $$f$$.
3. **Tối ưu hóa có ràng buộc**: khai thác mối quan hệ hình học giữa gradient và đường mức.
4. **Phân tích hội tụ**: đánh giá điều kiện để thuật toán hội tụ về nghiệm tối ưu.
5. **Chọn kích thước bước**: xác định độ dài bước đi hợp lý dọc theo hướng tìm kiếm.

Nhờ cung cấp đồng thời hướng di chuyển và tốc độ thay đổi cục bộ của hàm số, gradient đóng vai trò nền tảng trong phần lớn các thuật toán tối ưu hóa.
