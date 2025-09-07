---
layout: post
title: 00-01-03 Gradient và Đạo hàm Hướng
chapter: '00'
order: 5
owner: GitHub Copilot
lang: vi
categories:
- chapter00
lesson_type: required
---

Bài học này khám phá vector gradient và đạo hàm hướng, những khái niệm trung tâm trong tối ưu hóa để hiểu cách các hàm số thay đổi theo các hướng khác nhau.

---

## Vector Gradient

Gradient $$\nabla f$$ là một vector gồm các đạo hàm riêng của hàm số $$f$$ theo từng biến của nó. Nó chỉ ra hướng tăng dốc nhất của hàm số tại một điểm cho trước.

### Định nghĩa và Tính toán

Với hàm hai biến $$f(x, y)$$, gradient của nó là:

$$ \nabla f = \begin{pmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{pmatrix} $$

Với hàm $$n$$ biến $$f(x_1, x_2, \ldots, x_n)$$:

$$ \nabla f = \begin{pmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{pmatrix} $$

### Ví dụ: Tính Gradient

Với $$f(x, y) = x^2 + 3xy + y^2$$:

$$\frac{\partial f}{\partial x} = 2x + 3y$$
$$\frac{\partial f}{\partial y} = 3x + 2y$$

Do đó: $$\nabla f = \begin{pmatrix} 2x + 3y \\ 3x + 2y \end{pmatrix}$$

Tại điểm $$(1, 2)$$: $$\nabla f(1, 2) = \begin{pmatrix} 2(1) + 3(2) \\ 3(1) + 2(2) \end{pmatrix} = \begin{pmatrix} 8 \\ 7 \end{pmatrix}$$

---

## Đạo hàm Hướng

**Đạo hàm hướng** đo tốc độ thay đổi của $$f$$ khi chúng ta di chuyển theo bất kỳ hướng nào được chọn $$\mathbf{u}$$. Ở đây $$\mathbf{u}$$ phải là vector đơn vị (có độ dài bằng 1).

### Định nghĩa

Với hàm số $$f(\mathbf{x})$$ và vector đơn vị $$\mathbf{u} = \langle u_1, u_2, \ldots, u_n \rangle$$:

$$D_{\mathbf{u}}f(\mathbf{x}) = \nabla f(\mathbf{x}) \cdot \mathbf{u} = \sum_{i=1}^{n} \frac{\partial f}{\partial x_i} u_i$$

### Giải thích Hình học

Đạo hàm hướng có thể được viết như:

$$D_{\mathbf{u}}f = \lvert \nabla f \rvert \cos \theta$$

nơi $$\theta$$ là góc giữa $$\nabla f$$ và $$\mathbf{u}$$, và $$\lvert \nabla f \rvert$$ là độ lớn của gradient.

### Ví dụ: Tính Đạo hàm Hướng

Sử dụng ví dụ trước $$f(x, y) = x^2 + 3xy + y^2$$ tại điểm $$(1, 2)$$ nơi $$\nabla f(1, 2) = \begin{pmatrix} 8 \\ 7 \end{pmatrix}$$:

**Hướng 1:** $$\mathbf{u}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$ (hướng x dương)
$$D_{\mathbf{u}_1}f(1, 2) = 8 \cdot 1 + 7 \cdot 0 = 8$$

**Hướng 2:** $$\mathbf{u}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$ (hướng y dương)
$$D_{\mathbf{u}_2}f(1, 2) = 8 \cdot 0 + 7 \cdot 1 = 7$$

**Hướng 3:** $$\mathbf{u}_3 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$$ (đường chéo 45°)
$$D_{\mathbf{u}_3}f(1, 2) = 8 \cdot \frac{1}{\sqrt{2}} + 7 \cdot \frac{1}{\sqrt{2}} = \frac{15}{\sqrt{2}} \approx 10.61$$

---

## Tốc độ Thay đổi Tối đa và Tối thiểu

### Các Tính chất Chính

Từ công thức $$D_{\mathbf{u}}f = \lvert \nabla f \rvert \cos \theta$$, chúng ta có thể xác định:

1. **Tốc độ Thay đổi Tối đa**: Xảy ra khi $$\cos \theta = 1$$ (tức là $$\theta = 0°$$)
   - Hướng: $$\mathbf{u} = \frac{\nabla f}{\lvert \nabla f \rvert}$$ (cùng hướng với gradient)
   - Tốc độ tối đa: $$D_{\max}f = \lvert \nabla f \rvert$$

2. **Tốc độ Thay đổi Tối thiểu**: Xảy ra khi $$\cos \theta = -1$$ (tức là $$\theta = 180°$$)
   - Hướng: $$\mathbf{u} = -\frac{\nabla f}{\lvert \nabla f \rvert}$$ (ngược với gradient)
   - Tốc độ tối thiểu: $$D_{\min}f = -\lvert \nabla f \rvert$$

3. **Tốc độ Thay đổi Bằng Không**: Xảy ra khi $$\cos \theta = 0$$ (tức là $$\theta = 90°$$)
   - Hướng: Bất kỳ vector nào vuông góc với $$\nabla f$$

### Tóm tắt Các Tính chất của Gradient

- Gradient $$\nabla f$$ chỉ theo hướng **tăng dốc nhất**
- Hướng $$-\nabla f$$ chỉ theo hướng **giảm dốc nhất**
- Độ lớn $$\lvert \nabla f \rvert$$ cho **tốc độ thay đổi tối đa**
- Khi $$\nabla f = \mathbf{0}$$, điểm đó là **điểm tới hạn** (tối ưu tiềm năng)

---

## Mối quan hệ với Đường đồng mức

Tại bất kỳ điểm nào trên đường mức $$f(x, y) = c$$, vector gradient $$\nabla f$$ **trực giao (vuông góc)** với đường tiếp tuyến của đường mức tại điểm đó.

### Tại sao Điều này Quan trọng

Tính chất trực giao này rất cơ bản vì:

1. **Đường mức biểu diễn giá trị hàm hằng số**: Di chuyển dọc theo đường mức không thay đổi giá trị hàm, nên đạo hàm hướng bằng không.

2. **Gradient chỉ hướng tăng dốc nhất**: Hướng tăng giá trị hàm nhanh nhất phải vuông góc với hướng không thay đổi giá trị chút nào.

3. **Thông đạt tối ưu hóa**: Để tìm cực trị, chúng ta tìm các điểm nơi gradient bằng không (điểm tới hạn) hoặc nơi gradient vuông góc với biên ràng buộc.

### Ứng dụng trong Tối ưu hóa

Hiểu gradient và đạo hàm hướng rất quan trọng cho:

1. **Gradient Descent**: Di chuyển theo hướng $$-\nabla f$$ để tối thiểu hóa $$f$$
2. **Gradient Ascent**: Di chuyển theo hướng $$+\nabla f$$ để tối đa hóa $$f$$
3. **Tối ưu hóa có Ràng buộc**: Sử dụng mối quan hệ giữa gradient và đường mức
4. **Phân tích Hội tụ**: Hiểu khi nào thuật toán sẽ hội tụ đến nghiệm tối ưu
5. **Lựa chọn Kích thước Bước**: Xác định di chuyển bao xa theo hướng gradient

Gradient cung cấp cả hướng di chuyển và thông tin về tốc độ thay đổi của hàm, làm cho nó trở thành nền tảng cho hầu hết các thuật toán tối ưu hóa.
