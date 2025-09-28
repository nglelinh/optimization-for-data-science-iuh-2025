---
layout: post
title: 06-02-03 Tìm kiếm đường chính xác
chapter: '06'
order: 6
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Một cách khác để thích ứng kích thước bước trong gradient descent là **tìm kiếm đường chính xác**.

### Tìm kiếm Đường chính xác là gì?
Trong tìm kiếm đường chính xác, chúng ta di chuyển theo hướng của gradient âm và chọn kích thước bước tốt nhất có thể.

Đối với biểu thức sau, nếu $$s > 0$$, bước tiếp theo $$x - s \nabla f(x)$$ di chuyển ra khỏi vị trí hiện tại. Bằng cách thay đổi $$s$$, chúng ta tìm kích thước bước $$t$$ làm giảm thiểu $$f$$:

> $$t = \arg\min_{s \ge 0} f(x - s \nabla f(x))$$

## Thuật toán Exact Line Search

Thuật toán exact line search có thể được mô tả như sau:

1. **Bước 1**: Tại điểm hiện tại $$x^{(k)}$$, tính gradient $$\nabla f(x^{(k)})$$
2. **Bước 2**: Định nghĩa hàm một biến $$\phi(t) = f(x^{(k)} - t \nabla f(x^{(k)}))$$ với $$t \geq 0$$
3. **Bước 3**: Tìm $$t^* = \arg\min_{t \geq 0} \phi(t)$$ bằng cách giải $$\phi'(t) = 0$$
4. **Bước 4**: Cập nhật $$x^{(k+1)} = x^{(k)} - t^* \nabla f(x^{(k)})$$

## Các Ví dụ Cụ thể

### Ví dụ 1: Hàm Bậc hai Đơn giản (Dễ)

Xem xét hàm mục tiêu đơn giản:
$$f(x) = \frac{1}{2}x^2 - 3x + 2$$

**Bước 1**: Tính gradient
$$\nabla f(x) = x - 3$$

**Bước 2**: Tại điểm xuất phát $$x^{(0)} = 0$$, ta có $$\nabla f(0) = -3$$

**Bước 3**: Định nghĩa hàm line search
$$\phi(t) = f(0 - t(-3)) = f(3t) = \frac{1}{2}(3t)^2 - 3(3t) + 2 = \frac{9t^2}{2} - 9t + 2$$

**Bước 4**: Tìm minimum bằng cách lấy đạo hàm
$$\phi'(t) = 9t - 9 = 0 \Rightarrow t^* = 1$$

**Bước 5**: Cập nhật
$$x^{(1)} = 0 - 1 \cdot (-3) = 3$$

Kết quả: Chỉ sau một bước, ta đã tìm được nghiệm tối ưu $$x^* = 3$$ (vì $$\nabla f(3) = 0$$).

### Ví dụ 2: Hàm Bậc hai Nhiều biến (Trung bình)

Xem xét hàm mục tiêu:
$$f(x_1, x_2) = x_1^2 + 2x_2^2 - 2x_1 - 4x_2 + 3$$

**Bước 1**: Tính gradient
$$\nabla f(x_1, x_2) = \begin{pmatrix} 2x_1 - 2 \\ 4x_2 - 4 \end{pmatrix}$$

**Bước 2**: Tại điểm xuất phát $$x^{(0)} = (0, 0)$$
$$\nabla f(0, 0) = \begin{pmatrix} -2 \\ -4 \end{pmatrix}$$

**Bước 3**: Định nghĩa hàm line search
$$x^{(0)} - t \nabla f(x^{(0)}) = \begin{pmatrix} 0 \\ 0 \end{pmatrix} - t \begin{pmatrix} -2 \\ -4 \end{pmatrix} = \begin{pmatrix} 2t \\ 4t \end{pmatrix}$$

$$\phi(t) = f(2t, 4t) = (2t)^2 + 2(4t)^2 - 2(2t) - 4(4t) + 3$$
$$= 4t^2 + 32t^2 - 4t - 16t + 3 = 36t^2 - 20t + 3$$

**Bước 4**: Tìm minimum
$$\phi'(t) = 72t - 20 = 0 \Rightarrow t^* = \frac{20}{72} = \frac{5}{18}$$

**Bước 5**: Cập nhật
$$x^{(1)} = \begin{pmatrix} 2 \cdot \frac{5}{18} \\ 4 \cdot \frac{5}{18} \end{pmatrix} = \begin{pmatrix} \frac{5}{9} \\ \frac{10}{9} \end{pmatrix}$$

### Ví dụ 3: Hàm Rosenbrock 2D (Khó)

Xem xét hàm Rosenbrock nổi tiếng:
$$f(x_1, x_2) = 100(x_2 - x_1^2)^2 + (1 - x_1)^2$$

**Bước 1**: Tính gradient
$$\nabla f(x_1, x_2) = \begin{pmatrix} -400x_1(x_2 - x_1^2) - 2(1 - x_1) \\ 200(x_2 - x_1^2) \end{pmatrix}$$

**Bước 2**: Tại điểm xuất phát $$x^{(0)} = (-1, 1)$$
$$\nabla f(-1, 1) = \begin{pmatrix} -400(-1)(1 - 1) - 2(1 - (-1)) \\ 200(1 - 1) \end{pmatrix} = \begin{pmatrix} -4 \\ 0 \end{pmatrix}$$

**Bước 3**: Định nghĩa hàm line search
$$x^{(0)} - t \nabla f(x^{(0)}) = \begin{pmatrix} -1 \\ 1 \end{pmatrix} - t \begin{pmatrix} -4 \\ 0 \end{pmatrix} = \begin{pmatrix} -1 + 4t \\ 1 \end{pmatrix}$$

$$\phi(t) = f(-1 + 4t, 1) = 100(1 - (-1 + 4t)^2)^2 + (1 - (-1 + 4t))^2$$

Đây là một hàm phức tạp hơn, cần sử dụng phương pháp số để tìm minimum.

**Phân tích**: Với hàm Rosenbrock, exact line search trở nên phức tạp vì:
- Hàm không có dạng bậc hai đơn giản
- Cần sử dụng phương pháp số như Newton-Raphson để giải $$\phi'(t) = 0$$
- Có thể có nhiều điểm dừng cục bộ

### Ví dụ 4: Hàm Với Ràng buộc Miền (Rất khó)

Xem xét bài toán:
$$\min f(x) = x_1^2 + x_2^2 - 2x_1x_2$$
với ràng buộc $$x_1, x_2 \geq 0$$

Trong trường hợp này, exact line search phải xem xét:
$$t^* = \arg\min_{t \geq 0} f(x^{(k)} - t \nabla f(x^{(k)}))$$
sao cho $$x^{(k)} - t \nabla f(x^{(k)}) \geq 0$$

Điều này dẫn đến bài toán tối ưu có ràng buộc phức tạp hơn.

## Ưu điểm và Nhược điểm

### Ưu điểm:
1. **Tối ưu lý thuyết**: Mỗi bước đảm bảo giảm tối đa hàm mục tiêu theo hướng gradient
2. **Hội tụ nhanh**: Đối với hàm bậc hai, có thể hội tụ trong một bước
3. **Không cần điều chỉnh tham số**: Không cần chọn learning rate

### Nhược điểm:
1. **Chi phí tính toán cao**: Mỗi bước cần giải một bài toán tối ưu một biến
2. **Phức tạp với hàm phi tuyến**: Cần phương pháp số để tìm minimum
3. **Không thực tế cho bài toán lớn**: Thời gian tính toán quá lâu

## Khi nào sử dụng Exact Line Search?

Exact line search phù hợp khi:
- **Hàm mục tiêu đơn giản** (ví dụ: bậc hai)
- **Số chiều nhỏ** (thường ≤ 10 biến)
- **Cần độ chính xác cao** và có thể chấp nhận chi phí tính toán
- **Hàm mục tiêu có cấu trúc đặc biệt** cho phép giải tích

Trong thực tế, **backtracking line search** hiệu quả hơn và được sử dụng phổ biến hơn cho hầu hết các ứng dụng.
