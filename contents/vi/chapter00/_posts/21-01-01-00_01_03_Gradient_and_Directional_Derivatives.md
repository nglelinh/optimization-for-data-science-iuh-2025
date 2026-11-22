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
