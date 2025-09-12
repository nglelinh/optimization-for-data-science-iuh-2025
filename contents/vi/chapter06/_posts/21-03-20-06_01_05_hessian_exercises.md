---
layout: post
title: '06-01-05 Bài tập: Hiểu về Kích thước Bước và Độ cong'
chapter: '06'
order: 7
owner: AI Assistant
categories:
- chapter06
lang: vi
lesson_type: exercises
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

## Bài tập 1: Suy luận Xấp xỉ Bậc hai

Xét xấp xỉ bậc hai được sử dụng trong gradient descent:
$$f(y) \approx f(x) + \nabla f(x)^T (y - x) + \frac{1}{2t} \|y - x\|_2^2$$

**Phần A**: Chứng minh rằng tối thiểu hóa xấp xỉ này theo $$y$$ cho cập nhật gradient descent $$y = x - t\nabla f(x)$$.

**Phần B**: Điều gì xảy ra nếu chúng ta thay đổi hệ số thành $$\frac{\alpha}{2t}$$ thay vì $$\frac{1}{2t}$$? Điều này ảnh hưởng như thế nào đến kích thước bước?

**Phần C**: Diễn giải số hạng $$\frac{1}{2t} \|y - x\|_2^2$$ theo hình học. Nó ngăn chặn điều gì?

---

## Bài tập 2: Kích thước Bước và Độ cong Hàm

Xét hai hàm bậc hai:
- $$f_1(x_1, x_2) = \frac{1}{2}(x_1^2 + x_2^2)$$
- $$f_2(x_1, x_2) = \frac{1}{2}(4x_1^2 + x_2^2)$$

**Phần A**: Tính ma trận Hessian (ma trận các đạo hàm riêng bậc hai) cho cả hai hàm.

**Phần B**: Nếu chúng ta xấp xỉ cả hai Hessian bằng $$\frac{1}{t}I$$, giá trị $$t$$ nào cho xấp xỉ tốt nhất cho mỗi hàm?

**Phần C**: Bắt đầu từ điểm $$(2, 2)$$, thực hiện 3 lần lặp gradient descent trên cả hai hàm sử dụng kích thước bước tối ưu của bạn. So sánh hành vi hội tụ.

---

## Bài tập 3: Số Điều kiện và Hội tụ

Với hàm $$f(x_1, x_2) = \frac{1}{2}(ax_1^2 + bx_2^2)$$ với $$a > b > 0$$:

**Phần A**: Số điều kiện $$\kappa = \frac{a}{b}$$ là gì? Điều này liên quan như thế nào đến "hình dạng" của hàm?

**Phần B**: Chứng minh rằng kích thước bước tối ưu cho hội tụ nhanh nhất là $$t^* = \frac{2}{a + b}$$.

**Phần C**: So sánh tốc độ hội tụ cho:
- $$\kappa = 1$$ ($$a = b = 1$$)
- $$\kappa = 4$$ ($$a = 4, b = 1$$)
- $$\kappa = 100$$ ($$a = 100, b = 1$$)

Điều gì xảy ra khi số điều kiện tăng?

---

## Bài tập 4: Kích thước Bước theo Tọa độ

Thay vì sử dụng cùng kích thước bước cho tất cả tọa độ, xét:
$$x_1^{(k+1)} = x_1^{(k)} - t_1 \frac{\partial f}{\partial x_1}$$
$$x_2^{(k+1)} = x_2^{(k)} - t_2 \frac{\partial f}{\partial x_2}$$

**Phần A**: Với $$f(x_1, x_2) = \frac{1}{2}(ax_1^2 + bx_2^2)$$, lựa chọn $$t_1, t_2$$ nào làm cho mỗi tọa độ hội tụ trong đúng một bước?

**Phần B**: Điều này liên quan như thế nào đến việc xấp xỉ Hessian bằng ma trận đường chéo thay vì $$\frac{1}{t}I$$?

**Phần C**: Lập trình cách tiếp cận theo tọa độ này và so sánh với gradient descent chuẩn trên hàm bậc hai điều kiện xấu.

---

## Bài tập 5: Trực quan hóa Chất lượng Xấp xỉ

**Phần A**: Với hàm $$f(x_1, x_2) = \frac{1}{2}(4x_1^2 + x_2^2)$$, vẽ đường đồng mức hàm thực và đường đồng mức của xấp xỉ bậc hai $$f(x) + \nabla f(x)^T (y - x) + \frac{1}{2t} \|y - x\|_2^2$$ quanh điểm $$x = (1, 1)$$.

**Phần B**: Thử các giá trị $$t$$ khác nhau và quan sát cách chất lượng xấp xỉ thay đổi.

**Phần C**: Giá trị $$t$$ nào làm cho đường đồng mức xấp xỉ giống nhất với đường đồng mức hàm thực?

---

## Bài tập 6: Chiến lược Chọn Kích thước Bước

So sánh ba chiến lược chọn kích thước bước trên hàm $$f(x) = \frac{1}{2}x^T A x$$ với:
$$A = \begin{bmatrix} 10 & 2 \\ 2 & 1 \end{bmatrix}$$

1. **Bước cố định nhỏ**: $$t = 0.1$$
2. **Bước cố định lớn**: $$t = 0.5$$
3. **Bước thích ứng**: $$t = \frac{2}{\lambda_{\max} + \lambda_{\min}}$$ với $$\lambda_{\max}, \lambda_{\min}$$ là trị riêng lớn nhất và nhỏ nhất của $$A$$

**Phần A**: Tính các trị riêng của $$A$$ và xác định kích thước bước thích ứng.

**Phần B**: Bắt đầu từ $$(5, 5)$$, chạy gradient descent với mỗi chiến lược trong 20 lần lặp.

**Phần C**: Vẽ đường cong hội tụ và quỹ đạo. Chiến lược nào hoạt động tốt nhất và tại sao?

---

## Bài tập 7: Hàm Thực vs Xấp xỉ Bậc hai

Xét hàm không bậc hai $$f(x) = e^{x_1} + x_2^2$$.

**Phần A**: Tính gradient và Hessian của hàm này.

**Phần B**: Tại điểm $$x = (0, 1)$$, so sánh:
- Một bước gradient descent với kích thước bước $$t = 0.1$$
- Một bước sử dụng xấp xỉ bậc hai với Hessian thực
- Một bước sử dụng xấp xỉ bậc hai với $$\frac{1}{t}I$$ với $$t = 0.1$$

**Phần C**: Xấp xỉ nào cho kết quả gần với hướng tối thiểu thực hơn?

---

## Bài tập Lập trình

### Bài tập 8: Lập trình và So sánh

Lập trình và so sánh hiệu suất của chúng:

```python
import numpy as np
import matplotlib.pyplot as plt

def quadratic_function(x, A):
    """Tính f(x) = 0.5 * x^T A x"""
    return 0.5 * x.T @ A @ x

def gradient(x, A):
    """Tính gradient của f(x) = 0.5 * x^T A x"""
    return A @ x

def standard_gd(A, x0, step_size, max_iter=100):
    """Gradient descent chuẩn"""
    x = x0.copy()
    history = [x.copy()]
    
    for i in range(max_iter):
        grad = gradient(x, A)
        x = x - step_size * grad
        history.append(x.copy())
        
        if np.linalg.norm(grad) < 1e-8:
            break
    
    return np.array(history)

def coordinate_wise_gd(A, x0, step_sizes, max_iter=100):
    """Gradient descent theo tọa độ"""
    x = x0.copy()
    history = [x.copy()]
    
    for i in range(max_iter):
        grad = gradient(x, A)
        # Áp dụng kích thước bước khác nhau cho mỗi tọa độ
        x = x - step_sizes * grad
        history.append(x.copy())
        
        if np.linalg.norm(grad) < 1e-8:
            break
    
    return np.array(history)

# Kiểm tra trên các số điều kiện khác nhau
condition_numbers = [1, 4, 16, 64]
x0 = np.array([2.0, 2.0])

for kappa in condition_numbers:
    A = np.array([[kappa, 0], [0, 1]])
    
    # Kích thước bước tối ưu cho GD chuẩn
    eigenvals = np.linalg.eigvals(A)
    t_optimal = 2 / (eigenvals.max() + eigenvals.min())
    
    # Kích thước bước tối ưu theo tọa độ
    t_coord = 2 / np.diag(A)
    
    # Chạy cả hai phương pháp
    history_std = standard_gd(A, x0, t_optimal)
    history_coord = coordinate_wise_gd(A, x0, t_coord)
    
    # Vẽ kết quả
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.semilogy([quadratic_function(x, A) for x in history_std], 'b-', label='GD Chuẩn')
    plt.semilogy([quadratic_function(x, A) for x in history_coord], 'r--', label='GD Theo tọa độ')
    plt.xlabel('Lần lặp')
    plt.ylabel('Giá trị Hàm')
    plt.legend()
    plt.title(f'Hội tụ (κ = {kappa})')
    
    plt.subplot(1, 2, 2)
    plt.plot(history_std[:, 0], history_std[:, 1], 'b-o', label='GD Chuẩn', markersize=3)
    plt.plot(history_coord[:, 0], history_coord[:, 1], 'r--s', label='GD Theo tọa độ', markersize=3)
    plt.xlabel('x₁')
    plt.ylabel('x₂')
    plt.legend()
    plt.title(f'Quỹ đạo (κ = {kappa})')
    plt.axis('equal')
    
    plt.tight_layout()
    plt.show()
```

### Bài tập 9: Trực quan hóa Tương tác

Tạo một biểu đồ tương tác hiển thị:
1. Đường đồng mức hàm thực
2. Đường đồng mức xấp xỉ bậc hai
3. Quỹ đạo gradient descent
4. Thanh trượt để điều chỉnh kích thước bước và xem nó ảnh hưởng như thế nào đến hội tụ

**Yêu cầu**:
- Sử dụng matplotlib widgets hoặc plotly cho tính tương tác
- Hiển thị cả ví dụ điều kiện tốt và điều kiện xấu
- Hiển thị lỗi xấp xỉ khi kích thước bước thay đổi

---

## Đề cương Lời giải

### Lời giải Bài tập 1:
**A**: Lấy $$\frac{\partial}{\partial y}[f(x) + \nabla f(x)^T (y - x) + \frac{1}{2t} \|y - x\|_2^2] = \nabla f(x) + \frac{1}{t}(y-x) = 0$$
Giải: $$y = x - t\nabla f(x)$$

**B**: Kích thước bước hiệu quả trở thành $$\frac{t}{\alpha}$$

**C**: Số hạng hoạt động như "phạt gần" - nó ngăn không cho thực hiện bước quá xa từ điểm hiện tại

### Lời giải Bài tập 2:
**A**: 
- $$\nabla^2 f_1 = I$$
- $$\nabla^2 f_2 = \begin{bmatrix} 4 & 0 \\ 0 & 1 \end{bmatrix}$$

**B**: 
- Với $$f_1$$: $$t = 1$$
- Với $$f_2$$: $$t = 0.4$$ (tối thiểu hóa $$\|(4-\frac{1}{t})^2 + (1-\frac{1}{t})^2\|$$)

### Lời giải Bài tập 3:
**A**: $$\kappa = \frac{a}{b}$$ đo lường mức độ "kéo dài" của đường đồng mức ellip

**B**: Tối thiểu hóa hệ số hội tụ $$\frac{\kappa-1}{\kappa+1}$$

**C**: Số điều kiện cao hơn → hội tụ chậm hơn, hành vi dao động nhiều hơn

### Kết quả Học tập Chính:

1. **Hiểu biết trực quan**: Kích thước bước liên quan đến độ cong giả định
2. **Kỹ năng thực tế**: Cách chọn kích thước bước cho các bài toán khác nhau
3. **Hiểu biết lý thuyết**: Kết nối giữa tính chất hàm và hành vi tối ưu hóa
4. **Kinh nghiệm lập trình**: Coding và so sánh các cách tiếp cận khác nhau

Các bài tập này xây dựng hiểu biết mà không yêu cầu các khái niệm nâng cao như phương pháp Newton, thay vào đó tập trung vào mối quan hệ cơ bản giữa kích thước bước, độ cong và hành vi hội tụ.