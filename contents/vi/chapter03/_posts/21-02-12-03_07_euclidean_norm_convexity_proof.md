---
layout: post
title: 03-07 Chuẩn Euclidean - L2 - là Lồi
chapter: '03'
order: 15
owner: AI Assistant
categories:
- chapter03
lang: vi
---


**Chuẩn Euclidean** (còn gọi là chuẩn $$\ell_2$$) của một vector $$x \in \mathbb{R}^n$$ được định nghĩa là:

$$\|x\|_2 = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2} = \sqrt{x^T x}$$

Chúng ta sẽ chứng minh rằng hàm này là lồi sử dụng ba phương pháp khác nhau:
1. **Chứng minh dựa trên định nghĩa** sử dụng bất đẳng thức Jensen
2. **Kiểm tra đạo hàm bậc hai** (phân tích Hessian)
3. **Phương pháp bất đẳng thức tam giác**

## Phương pháp 1: Chứng minh Dựa trên Định nghĩa

**Định lý**: Chuẩn Euclidean $$f(x) = \|x\|_2$$ là lồi trên $$\mathbb{R}^n$$.

**Chứng minh**: 
Để chứng minh tính lồi, chúng ta cần chỉ ra rằng với bất kỳ $$x, y \in \mathbb{R}^n$$ và $$\theta \in [0,1]$$:

$$\|\theta x + (1-\theta) y\|_2 \leq \theta \|x\|_2 + (1-\theta) \|y\|_2$$

Đặt $$z = \theta x + (1-\theta) y$$. Khi đó:

$$\begin{align}
\|z\|_2^2 &= \|\theta x + (1-\theta) y\|_2^2 \\
&= (\theta x + (1-\theta) y)^T (\theta x + (1-\theta) y) \\
&= \theta^2 x^T x + 2\theta(1-\theta) x^T y + (1-\theta)^2 y^T y \\
&= \theta^2 \|x\|_2^2 + 2\theta(1-\theta) x^T y + (1-\theta)^2 \|y\|_2^2
\end{align}$$

Theo **bất đẳng thức Cauchy-Schwarz**: $$x^T y \leq \|x\|_2 \|y\|_2$$

Do đó:
$$\|z\|_2^2 \leq \theta^2 \|x\|_2^2 + 2\theta(1-\theta) \|x\|_2 \|y\|_2 + (1-\theta)^2 \|y\|_2^2$$

Vế phải có thể phân tích thành nhân tử:
$$\theta^2 \|x\|_2^2 + 2\theta(1-\theta) \|x\|_2 \|y\|_2 + (1-\theta)^2 \|y\|_2^2 = (\theta \|x\|_2 + (1-\theta) \|y\|_2)^2$$

Lấy căn bậc hai hai vế:
$$\|\theta x + (1-\theta) y\|_2 \leq \theta \|x\|_2 + (1-\theta) \|y\|_2$$

Điều này chứng minh chuẩn Euclidean là lồi. $$\square$$

## Phương pháp 2: Kiểm tra đạo hàm bậc hai (phân tích Hessian)

Với các hàm khả vi hai lần, ta có thể dùng **kiểm tra đạo hàm bậc hai**: một hàm là lồi nếu ma trận Hessian của nó nửa xác định dương.

**Phân tích**: 
Chuẩn Euclidean $$f(x) = \|x\|_2 = \sqrt{x^T x}$$ không khả vi tại $$x = 0$$. Tuy nhiên, với $$x \neq 0$$, ta có thể tính:

$$\frac{\partial f}{\partial x_i} = \frac{x_i}{\|x\|_2}$$

$$\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{1}{\|x\|_2} \delta_{ij} - \frac{x_i x_j}{\|x\|_2^3}$$

Ma trận Hessian là:
$$H = \frac{1}{\|x\|_2} I - \frac{1}{\|x\|_2^3} x x^T = \frac{1}{\|x\|_2} \left( I - \frac{x x^T}{\|x\|_2^2} \right)$$

**Kiểm tra tính nửa xác định dương**:
Với mọi vector $$v \in \mathbb{R}^n$$:
$$v^T H v = \frac{1}{\|x\|_2} \left( \|v\|_2^2 - \frac{(x^T v)^2}{\|x\|_2^2} \right)$$

Theo bất đẳng thức Cauchy-Schwarz: $$(x^T v)^2 \leq \|x\|_2^2 \|v\|_2^2$$

Do đó: $$\|v\|_2^2 - \frac{(x^T v)^2}{\|x\|_2^2} \geq 0$$

Điều này cho thấy $$H \succeq 0$$, xác nhận tính lồi với $$x \neq 0$$. (Tại $$x = 0$$ tính lồi suy ra từ phương pháp 1 hoặc 3.)

## Phương pháp 3: Phương pháp bất đẳng thức tam giác

**Chứng minh thay thế bằng bất đẳng thức Minkowski**:

Chuẩn Euclidean thỏa mãn **bất đẳng thức tam giác**:
$$\|x + y\|_2 \leq \|x\|_2 + \|y\|_2$$

Để chứng minh tính lồi, đặt $$u = \theta x$$ và $$v = (1-\theta) y$$ với $$\theta \in [0,1]$$:
$$\|\theta x + (1-\theta) y\|_2 = \|u + v\|_2 \leq \|u\|_2 + \|v\|_2 = \theta \|x\|_2 + (1-\theta) \|y\|_2$$

Điều này trực tiếp thiết lập điều kiện lồi (đồng nhất bậc một của chuẩn được dùng ở đẳng thức cuối).


## Các tính chất và ứng dụng chính

### Các tính chất của tính lồi của chuẩn Euclidean

1. **Lồi chặt dọc theo đường**: Chuẩn Euclidean thực ra là **lồi chặt** dọc theo mọi đường thẳng không đi qua gốc tọa độ.

2. **Tính thuần nhất**: $$\|\alpha x\|_2 = \lvert\alpha\rvert \|x\|_2$$ với mọi vô hướng $$\alpha$$.

3. **Tính dưới cộng**: $$\|x + y\|_2 \leq \|x\|_2 + \|y\|_2$$ (bất đẳng thức tam giác).

### Ứng dụng trong tối ưu hóa

Tính lồi của chuẩn Euclidean có những hệ quả quan trọng:

1. **Bài toán bình phương tối thiểu**: Hàm mục tiêu $$\|Ax - b\|_2^2$$ là lồi.

2. **Chính quy hóa**: Các số hạng chính quy hóa $$\ell_2$$ như $$\lambda \|x\|_2$$ (với $$\lambda \ge 0$$) bảo toàn tính lồi.

3. **Tối ưu có ràng buộc**: Các ràng buộc chuẩn $$\|x\|_2 \leq r$$ xác định các tập khả thi lồi.

## Kết luận

Chúng ta đã chứng minh chuẩn Euclidean là lồi bằng ba cách tiếp cận khác nhau:

1. **Định nghĩa trực tiếp**: Dùng bất đẳng thức Jensen và Cauchy-Schwarz
2. **Kiểm tra đạo hàm bậc hai**: Chỉ ra Hessian nửa xác định dương  
3. **Bất đẳng thức tam giác**: Tận dụng tính chất cơ bản của chuẩn
2. **Second derivative test**: Showing the Hessian is positive semidefinite  
3. **Triangle inequality**: Leveraging the fundamental norm property

Tính chất lồi này là nền tảng của lý thuyết tối ưu và có nhiều ứng dụng trong học máy, xử lý tín hiệu và giải tích số.

Phần minh họa tương tác ở trên cho thấy điều kiện lồi $$\|\theta x + (1-\theta) y\|_2 \leq \theta \|x\|_2 + (1-\theta) \|y\|_2$$ đúng với mọi lựa chọn các điểm và tham số tổ hợp lồi $$\theta$$.
