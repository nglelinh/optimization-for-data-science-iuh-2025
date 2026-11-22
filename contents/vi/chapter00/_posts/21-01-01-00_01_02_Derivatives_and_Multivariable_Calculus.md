---
layout: post
title: 00-01-02 Đạo hàm và Giải tích đa biến
chapter: '00'
order: 4
owner: GitHub Copilot
lang: vi
categories:
- chapter00
lesson_type: required
---

Bài học này trình bày đạo hàm và các khái niệm cốt lõi của giải tích đa biến — nền tảng của lý thuyết và thuật toán tối ưu hóa.

---

## Đạo hàm và tốc độ thay đổi

Đạo hàm của một hàm một biến biểu thị tốc độ thay đổi tức thời của hàm đó, giúp ta nắm bắt hành vi cục bộ của hàm số.

### Các khái niệm đạo hàm cơ bản

**Độ dốc giữa hai điểm:**

$$\text{Độ dốc} = \frac{y_2 - y_1}{x_2 - x_1}$$

**Đạo hàm (tốc độ thay đổi tức thời):**

$$f'(x_0) = \lim_{x_1 \to x_0} \frac{f(x_1) - f(x_0)}{x_1 - x_0} = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$$

Đạo hàm cho biết hàm số thay đổi nhanh đến mức nào tại một điểm cho trước. Trong tối ưu hóa, khái niệm này đặc biệt quan trọng để xác định các điểm dừng — nơi tốc độ thay đổi bằng không.

### Đường mức của hàm số

Đường mức là công cụ cơ bản trong giải tích đa biến để trực quan hóa các hàm hai biến $$f(x, y)$$, cho phép biểu diễn một mặt cong trong không gian 3 chiều trên mặt phẳng 2 chiều.

Một **đường mức** của hàm số $$f(x, y)$$ là tập hợp tất cả các điểm $$(x, y)$$ thuộc miền xác định của $$f$$ mà tại đó hàm số nhận cùng một giá trị hằng số:

$$f(x, y) = c$$

**Ví dụ:**
- Với $$f(x, y) = x^2 + y^2$$, các đường mức là các đường tròn đồng tâm: $$x^2 + y^2 = c$$ (với $$c > 0$$).
- Với $$f(x, y) = x + y$$, các đường mức là các đường thẳng song song: $$x + y = c$$.

Đường mức giúp ta quan sát:
1. Hình dạng bề mặt (địa hình) của hàm số.
2. Hướng tăng nhanh nhất và hướng giảm nhanh nhất.
3. Vị trí của các điểm cực trị tiềm năng.

---

## Các khái niệm chính của giải tích đa biến

### Đạo hàm riêng

Với hàm nhiều biến $$f(x_1, x_2, \ldots, x_n)$$, **đạo hàm riêng** theo biến $$x_i$$ được định nghĩa là:

$$\frac{\partial f}{\partial x_i} = \lim_{h \to 0} \frac{f(x_1, \ldots, x_i + h, \ldots, x_n) - f(x_1, \ldots, x_i, \ldots, x_n)}{h}$$

Đạo hàm riêng đo tốc độ thay đổi của $$f$$ khi chỉ có $$x_i$$ biến thiên trong khi tất cả các biến còn lại được giữ cố định.

### Vector gradient

**Gradient** là vector tập hợp toàn bộ các đạo hàm riêng bậc nhất của hàm số:

$$\nabla f(\mathbf{x}) = \begin{pmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{pmatrix}$$

Gradient chỉ theo hướng tăng nhanh nhất của hàm số và luôn vuông góc với các đường mức.

### Ma trận Hessian

**Ma trận Hessian** chứa toàn bộ các đạo hàm riêng bậc hai của hàm số:

$$\nabla^2 f(\mathbf{x}) = \mathbf{H} = \begin{pmatrix} 
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{pmatrix}$$

Ma trận Hessian phản ánh độ cong của hàm số và được dùng để:
- Phân loại các điểm tới hạn (cực tiểu, cực đại hoặc điểm yên ngựa).
- Xây dựng các thuật toán tối ưu hóa bậc hai như phương pháp Newton.

---

## Quy tắc dây chuyền cho hàm đa biến

Quy tắc dây chuyền là công cụ thiết yếu để tính đạo hàm của hàm hợp — dạng hàm xuất hiện rất phổ biến trong các bài toán tối ưu hóa.

### Quy tắc dây chuyền cơ bản

Với hàm $$z = f(x, y)$$, trong đó $$x = g(t)$$ và $$y = h(t)$$:

$$ \frac{dz}{dt} = \frac{\partial f}{\partial x} \frac{dx}{dt} + \frac{\partial f}{\partial y} \frac{dy}{dt} $$

### Quy tắc dây chuyền tổng quát

Với hàm $$z = f(x_1, x_2, \ldots, x_n)$$, trong đó mỗi $$x_i = x_i(t_1, t_2, \ldots, t_m)$$:

$$ \frac{\partial z}{\partial t_j} = \sum_{i=1}^{n} \frac{\partial f}{\partial x_i} \frac{\partial x_i}{\partial t_j} $$

### Ứng dụng trong tối ưu hóa

Quy tắc dây chuyền giữ vai trò nền tảng trong:

1. **Tính gradient**: tính đạo hàm của các hàm mục tiêu có cấu trúc hàm hợp.
2. **Xử lý ràng buộc**: xử lý các ràng buộc phụ thuộc vào các biến trung gian.
3. **Cài đặt thuật toán**: thuật toán lan truyền ngược (backpropagation) trong mạng nơ-ron và vi phân tự động.
4. **Phân tích độ nhạy**: đánh giá mức độ ảnh hưởng của sự thay đổi tham số tới nghiệm tối ưu.

### Ví dụ: Tối ưu hóa có ràng buộc

Xét bài toán cực tiểu hóa $$f(x, y) = x^2 + y^2$$ với ràng buộc $$g(x, y) = x + y - 1 = 0$$.

Từ ràng buộc, ta rút $$y = 1 - x$$ để đưa về bài toán một biến:

$$h(x) = f(x, 1-x) = x^2 + (1-x)^2$$

Áp dụng quy tắc dây chuyền:

$$h'(x) = \frac{\partial f}{\partial x} \cdot 1 + \frac{\partial f}{\partial y} \cdot \frac{d(1-x)}{dx} = 2x + 2(1-x)(-1) = 4x - 2$$

Giải phương trình $$h'(x) = 0$$ ta được $$x = 1/2$$, suy ra điểm tối ưu là $$(1/2, 1/2)$$.

Ví dụ này minh họa cách các công cụ giải tích đa biến phối hợp với nhau để giải bài toán tối ưu hóa một cách có hệ thống.
