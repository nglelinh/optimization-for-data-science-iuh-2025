---
layout: post
title: '06-01-06 Bài tập: Hiểu về Kích thước Bước và Độ cong'
chapter: '06'
order: 4
owner: AI Assistant
categories:
- chapter06
lang: vi
lesson_type: exercises
redirect_from:
  - /contents/vi/chapter06/06_01_05_hessian_exercises/
---

Hiểu bằng mắt rằng $$1/t$$ đóng vai trò xấp xỉ Hessian là một chuyện, nhưng tự tay đạo hàm mô hình bậc hai, tính chỉ số điều kiện $$\kappa = \lambda_{\max}/\lambda_{\min}$$ và thấy tận mắt vì sao đổi tỷ lệ trục (preconditioning) làm tốc độ hội tụ tăng gấp hàng trăm lần lại là một trải nghiệm khai sáng hoàn toàn khác.

Bộ bài tập chuyên sâu này dẫn bạn đi từng bước từ chứng minh đại số quy tắc cập nhật GD, phân tích ảnh hưởng của độ cong địa phương đến từng tọa độ, cho đến việc thiết kế bước thích ứng theo đường chéo Hessian — tiền đề trực tiếp cho các thuật toán AdaGrad và Adam trong học sâu!

## Bản đồ kiến thức nền: Bốn công cụ cần dùng để giải trọn bộ bài tập độ cong

Trước khi bắt tay vào 5 bài tập bên dưới, hãy đặt sẵn bốn công thức trụ cột lên bàn:

- **Đạo hàm dạng toàn phương:** Với $$q(y) = f(x) + g^T(y - x) + \frac{1}{2t}\|y - x\|_2^2$$, lấy gradient theo $$y$$ cho $$\nabla q(y) = g + \frac{1}{t}(y - x) = 0 \implies y^\star = x - tg$$.
- **Điều kiện ổn định & Bước tối ưu cho hàm bậc hai:** Với $$f(x) = \frac{1}{2} x^T Q x$$ có các trị riêng $$0 < m = \lambda_{\min} \le \dots \le \lambda_{\max} = L$$, bước cố định tốt nhất cho bài toán bậc hai là $$t^\star = \frac{2}{L + m}$$, cho hệ số co tối ưu là $$\rho^\star = \frac{\kappa - 1}{\kappa + 1}$$ với $$\kappa = \frac{L}{m}$$.
- **Tách biến theo từng tọa độ (Diagonal Preconditioning):** Nếu thay $$\frac{1}{t} I$$ bằng ma trận đường chéo $$D = \operatorname{diag}(1/t_1, \dots, 1/t_n)$$ khớp với từng phần tử đường chéo $$H_{ii}$$ của Hessian, ta thu được bước cập nhật riêng cho từng tọa độ $$x_i^+ = x_i - \frac{1}{H_{ii}} \frac{\partial f}{\partial x_i}$$.
- **Liên hệ trực tiếp với Chuẩn hóa đặc trưng (Feature Scaling):** Trong học máy, chuẩn hóa các cột dữ liệu về cùng phương sai chính là cách giảm chỉ số điều kiện $$\kappa(X^T X)$$ từ hàng triệu xuống gần $$1$$, biến đường đồng mức ellipsoid dẹt thành hình tròn để GD đi thẳng vào tâm!

### Khung giải thích (nên đọc chậm): Tính bước tối ưu và số vòng lặp theo chỉ số điều kiện $$\kappa$$

Xét hàm bậc hai $$f(x_1, x_2) = \frac{1}{2}(x_1^2 + 9x_2^2)$$ với $$Q = \operatorname{diag}(1, 9)$$.

1. **Bước 1 — Xác định trị riêng và chỉ số điều kiện:**
   $$m = \lambda_{\min} = 1, \qquad L = \lambda_{\max} = 9, \qquad \kappa = \frac{L}{m} = 9.$$
2. **Bước 2 — Tính bước tối ưu $$t^\star = \frac{2}{L + m}$$ và hệ số co $$\rho^\star$$:**
   $$t^\star = \frac{2}{9 + 1} = 0.2.$$
   Kiểm tra hai hệ số co theo từng trục tại $$t^\star = 0.2$$:
   - Trục $$x_1$$: $$1 - 0.2(1) = +0.8$$.
   - Trục $$x_2$$: $$1 - 0.2(9) = -0.8$$.
   Cả hai đều có trị tuyệt đối bằng $$\rho^\star = \frac{9 - 1}{9 + 1} = 0.8$$!
3. **Bước 3 — So sánh nếu dùng bước riêng theo từng tọa độ $$t_1 = 1/1 = 1,\; t_2 = 1/9$$:**
   - Trục $$x_1$$: $$1 - 1(1) = 0$$.
   - Trục $$x_2$$: $$1 - \frac{1}{9}(9) = 0$$.
   Chỉ cần đúng **1 bước duy nhất** thay vì $$\approx 31$$ bước (để $$0.8^k < 10^{-3}$$) để chạm nghiệm $$x^\star = (0, 0)$$! Đó là sức mạnh thực sự của việc ước lượng đúng độ cong!

---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

## Bài tập 1: Suy ra Quy tắc Cập nhật từ Xấp xỉ Bậc hai

Xét xấp xỉ bậc hai được sử dụng trong gradient descent:
$$f(y) \approx f(x) + \nabla f(x)^T (y - x) + \frac{1}{2t} \|y - x\|_2^2$$

**Phần A**: Chứng minh rằng việc cực tiểu hóa xấp xỉ này theo $$y$$ cho ta quy tắc cập nhật gradient descent $$y = x - t\nabla f(x)$$.

**Phần B**: Điều gì xảy ra nếu ta thay hệ số $$\frac{1}{2t}$$ bằng $$\frac{\alpha}{2t}$$ (với $$\alpha > 0$$)? Thay đổi này ảnh hưởng như thế nào đến kích thước bước hiệu dụng?

**Phần C**: Hãy diễn giải ý nghĩa hình học của số hạng $$\frac{1}{2t} \|y - x\|_2^2$$. Số hạng này giúp ngăn chặn hiện tượng gì?

---

## Bài tập 2: Kích thước Bước và Độ cong Hàm số

Xét hai hàm bậc hai:
- $$f_1(x_1, x_2) = \frac{1}{2}(x_1^2 + x_2^2)$$
- $$f_2(x_1, x_2) = \frac{1}{2}(4x_1^2 + x_2^2)$$

**Phần A**: Tính ma trận Hessian (ma trận các đạo hàm riêng bậc hai) của cả hai hàm số.

**Phần B**: Nếu xấp xỉ mỗi ma trận Hessian bằng $$\frac{1}{t}I$$, giá trị $$t$$ nào cho xấp xỉ tốt nhất đối với từng hàm?

**Phần C**: Xuất phát từ điểm $$(2, 2)$$, thực hiện 3 bước lặp gradient descent trên cả hai hàm với kích thước bước vừa tìm được và so sánh hành vi hội tụ.

---

## Bài tập 3: Chỉ số Điều kiện và Tốc độ Hội tụ

Xét hàm số $$f(x_1, x_2) = \frac{1}{2}(ax_1^2 + bx_2^2)$$ với $$a > b > 0$$:

**Phần A**: Chỉ số điều kiện $$\kappa = \frac{a}{b}$$ đo lường đại lượng nào và liên quan ra sao đến hình dạng đường đồng mức của hàm số?

**Phần B**: Chứng minh rằng kích thước bước cố định tối ưu cho tốc độ hội tụ nhanh nhất là $$t^* = \frac{2}{a + b}$$.

**Phần C**: So sánh tốc độ hội tụ trong ba trường hợp:
- $$\kappa = 1$$ ($$a = b = 1$$)
- $$\kappa = 4$$ ($$a = 4, b = 1$$)
- $$\kappa = 100$$ ($$a = 100, b = 1$$)

Điều gì xảy ra khi chỉ số điều kiện tăng lên?

---

## Bài tập 4: Kích thước Bước theo Từng Tọa độ

Thay vì dùng chung một kích thước bước cho mọi tọa độ, xét quy tắc cập nhật:
$$x_1^{(k+1)} = x_1^{(k)} - t_1 \frac{\partial f}{\partial x_1}$$
$$x_2^{(k+1)} = x_2^{(k)} - t_2 \frac{\partial f}{\partial x_2}$$

**Phần A**: Với $$f(x_1, x_2) = \frac{1}{2}(ax_1^2 + bx_2^2)$$, cần chọn $$t_1, t_2$$ bằng bao nhiêu để mỗi tọa độ hội tụ sau đúng một bước?

**Phần B**: Cách chọn này liên hệ như thế nào với việc xấp xỉ Hessian bằng một ma trận đường chéo thay vì $$\frac{1}{t}I$$?

**Phần C**: Cài đặt phương pháp cập nhật theo tọa độ này và so sánh với gradient descent chuẩn trên một hàm bậc hai có chỉ số điều kiện lớn.

---

## Bài tập 5: Trực quan hóa Chất lượng Xấp xỉ

**Phần A**: Với hàm $$f(x_1, x_2) = \frac{1}{2}(4x_1^2 + x_2^2)$$, vẽ đường đồng mức của hàm thực và đường đồng mức của xấp xỉ bậc hai $$f(x) + \nabla f(x)^T (y - x) + \frac{1}{2t} \|y - x\|_2^2$$ quanh điểm $$x = (1, 1)$$.

**Phần B**: Thử nghiệm nhiều giá trị $$t$$ khác nhau và quan sát sự thay đổi về chất lượng xấp xỉ.

**Phần C**: Giá trị $$t$$ nào làm cho đường đồng mức của hàm xấp xỉ bám sát đường đồng mức hàm thực nhất?

---

## Bài tập 6: So sánh Chiến lược Chọn Kích thước Bước

So sánh ba chiến lược chọn kích thước bước trên hàm $$f(x) = \frac{1}{2}x^T A x$$ với:
$$A = \begin{bmatrix} 10 & 2 \\ 2 & 1 \end{bmatrix}$$

1. **Bước cố định nhỏ**: $$t = 0.1$$
2. **Bước cố định lớn**: $$t = 0.5$$
3. **Bước tối ưu theo trị riêng**: $$t = \frac{2}{\lambda_{\max} + \lambda_{\min}}$$, trong đó $$\lambda_{\max}, \lambda_{\min}$$ lần lượt là trị riêng lớn nhất và nhỏ nhất của $$A$$.

**Phần A**: Tính các trị riêng của $$A$$ và xác định kích thước bước tối ưu ở chiến lược 3.

**Phần B**: Xuất phát từ điểm $$(5, 5)$$, chạy gradient descent với từng chiến lược trong 20 lần lặp.

**Phần C**: Vẽ đường cong hội tụ và quỹ đạo di chuyển. Chiến lược nào đạt hiệu quả tốt nhất và vì sao?

---

## Bài tập 7: Hàm Phi tuyến và Xấp xỉ Bậc hai

Xét hàm không phải bậc hai $$f(x) = e^{x_1} + x_2^2$$.

**Phần A**: Tính gradient và ma trận Hessian của hàm số.

**Phần B**: Tại điểm $$x = (0, 1)$$, hãy so sánh kết quả sau một bước của ba cách cập nhật:
- Một bước gradient descent với $$t = 0.1$$.
- Một bước cực tiểu hóa xấp xỉ bậc hai sử dụng Hessian thực.
- Một bước cực tiểu hóa xấp xỉ bậc hai sử dụng $$\frac{1}{t}I$$ với $$t = 0.1$$.

**Phần C**: Xấp xỉ nào đưa điểm lặp lại gần hướng cực tiểu thực hơn?

---

## Bài tập Lập trình

### Bài tập 8: Cài đặt và So sánh

Cài đặt và so sánh hiệu năng của hai biến thể gradient descent bằng đoạn mã sau:

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
    t_coord = 1 / np.diag(A)
    
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

Xây dựng một biểu đồ tương tác hiển thị:
1. Đường đồng mức của hàm thực.
2. Đường đồng mức của xấp xỉ bậc hai.
3. Quỹ đạo của gradient descent.
4. Thanh trượt cho phép điều chỉnh kích thước bước để quan sát tác động lên quá trình hội tụ.

**Yêu cầu**:
- Sử dụng `matplotlib` widgets hoặc `plotly` để tạo tương tác.
- Minh họa cả trường hợp điều kiện tốt và điều kiện xấu.
- Hiển thị sai số xấp xỉ khi thay đổi kích thước bước.

---

## Gợi ý Lời giải

### Lời giải Bài tập 1:
**A**: Lấy đạo hàm theo $$y$$: $$\frac{\partial}{\partial y}\left[f(x) + \nabla f(x)^T (y - x) + \frac{1}{2t} \|y - x\|_2^2\right] = \nabla f(x) + \frac{1}{t}(y-x) = 0$$. Giải phương trình thu được $$y = x - t\nabla f(x)$$.

**B**: Kích thước bước hiệu dụng trở thành $$\frac{t}{\alpha}$$.

**C**: Số hạng này đóng vai trò là số hạng phạt gần kề (proximal penalty), giúp hạn chế việc thực hiện bước nhảy quá xa khỏi điểm hiện tại.

### Lời giải Bài tập 2:
**A**:
- $$\nabla^2 f_1 = I$$
- $$\nabla^2 f_2 = \begin{bmatrix} 4 & 0 \\ 0 & 1 \end{bmatrix}$$

**B**:
- Với $$f_1$$: $$t = 1$$.
- Với $$f_2$$: $$t = 0.4$$ (cực tiểu hóa sai số xấp xỉ $$(4-\frac{1}{t})^2 + (1-\frac{1}{t})^2$$ theo $$\frac{1}{t}$$, thu được $$\frac{1}{t} = \frac{4+1}{2} = 2.5$$).

### Lời giải Bài tập 3:
**A**: $$\kappa = \frac{a}{b}$$ đo lường mức độ kéo dài (dẹt) của các đường đồng mức hình elip.

**B**: Cực tiểu hóa hệ số co tối đa theo hai trục cho ta hệ số hội tụ tối ưu $$\frac{\kappa-1}{\kappa+1}$$ tại $$t^* = \frac{2}{a+b}$$.

**C**: Chỉ số điều kiện càng lớn thì hội tụ càng chậm và quỹ đạo càng dễ dao động.

### Lời giải Bài tập 4:
**A**: Chọn $$t_1 = \frac{1}{a}$$, $$t_2 = \frac{1}{b}$$; khi đó $$x_1^{+} = x_1 - \frac{1}{a}\cdot a x_1 = 0$$ và $$x_2^{+} = 0$$, tức hội tụ sau đúng một bước.

**B**: Cách làm này tương ứng với việc xấp xỉ Hessian bằng ma trận đường chéo $$\text{diag}(a, b)$$ (chính xác với hàm bậc hai tách biến này), thay vì dùng ma trận đẳng hướng $$\frac{1}{t}I$$.

**C**: Cần dùng $$t_i = 1/A_{ii}$$ (không dùng $$2/A_{ii}$$, vì kích thước bước $$2/A_{ii}$$ chỉ làm tọa độ đổi dấu và dao động mà không giảm về 0).

### Lời giải Bài tập 6:
**A**: $$\lambda_{\max} \approx 10.424$$, $$\lambda_{\min} \approx 0.576$$, nên $$t = \frac{2}{11} \approx 0.182$$.

**B–C**: Vì $$t = 0.5 > \frac{2}{\lambda_{\max}} \approx 0.192$$ nên gradient descent với bước cố định lớn bị **phân kỳ**; $$t = 0.1$$ hội tụ nhưng chậm theo phương có độ cong nhỏ; $$t = \frac{2}{11}$$ cho tốc độ hội tụ tốt nhất trong ba chiến lược.

### Mục tiêu Học tập Chính:

1. **Hiểu biết trực quan**: Mối liên hệ giữa kích thước bước và độ cong giả định của hàm số.
2. **Kỹ năng thực hành**: Lựa chọn kích thước bước phù hợp cho các dạng bài toán khác nhau.
3. **Nền tảng lý thuyết**: Liên kết tính chất hình học của hàm mục tiêu với hành vi hội tụ.
4. **Thực hành lập trình**: Cài đặt và so sánh trực tiếp các chiến lược cập nhật.

Các bài tập trên giúp xây dựng nền tảng vững chắc về mối quan hệ giữa kích thước bước, độ cong và tốc độ hội tụ mà chưa cần sử dụng các phương pháp bậc hai nâng cao như phương pháp Newton.