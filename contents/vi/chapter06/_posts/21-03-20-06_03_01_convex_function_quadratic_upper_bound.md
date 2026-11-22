---
layout: post
title: 06-03-01 Cận trên bậc hai của hàm lồi
chapter: '06'
order: 10
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

## Giới thiệu

**Cận trên bậc hai** là một tính chất nền tảng của các hàm lồi trơn, đóng vai trò công cụ cốt lõi trong việc phân tích và thiết kế thuật toán tối ưu hóa. Tính chất này khẳng định rằng mọi hàm lồi có gradient liên tục Lipschitz đều có thể được chặn trên bởi một hàm bậc hai, tạo cơ sở trực tiếp cho việc phân tích hội tụ của các phương pháp dựa trên gradient.

## Vai trò và Ý nghĩa

Vì sao cận trên bậc hai lại quan trọng trong tối ưu hóa?

1. **Thiết kế thuật toán**: Nhiều thuật toán tối ưu (như gradient descent) xây dựng bước cập nhật dựa trên xấp xỉ cục bộ của hàm mục tiêu. Cận trên bậc hai cung cấp một khuôn khổ nhất quán để thiết lập các xấp xỉ này.

2. **Phân tích hội tụ**: Bất đẳng thức cận trên bậc hai giúp chặn mức thay đổi giá trị hàm sau mỗi bước lặp, từ đó chứng minh tốc độ hội tụ của thuật toán.

3. **Lựa chọn kích thước bước**: Hằng số Lipschitz $$L$$ trong cận trên trực tiếp xác định ngưỡng kích thước bước an toàn cho gradient descent.

## Tính chất Cận trên Bậc hai

<div class="textbook-theorem" markdown="1">
**Định lý**: Nếu $$f$$ là hàm lồi và $$\nabla f$$ liên tục Lipschitz với hằng số $$L$$, thì $$f$$ thỏa mãn cận trên bậc hai:

> $$ \begin{align}
f(y) & \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \| y - x \|^2_2 \quad \forall x, y
\end{align} $$
</div>

### Diễn giải Hình học

Bất đẳng thức trên cho thấy:
- **Xấp xỉ tuyến tính** $$f(x) + \nabla f(x)^T (y-x)$$ (khai triển Taylor bậc nhất) luôn nằm dưới $$f(y)$$ nhờ tính lồi.
- **Cận trên bậc hai** $$f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \| y - x \|^2_2$$ luôn nằm trên $$f(y)$$.
- Đồ thị của $$f(y)$$ được kẹp giữa hai cận này.

### Đặc trưng Tương đương

<div class="textbook-theorem" markdown="1">
**Hệ quả**: Đối với mọi hàm lồi trơn $$f$$ có gradient $$L$$-Lipschitz, hàm số sau đây là hàm lồi:

> $$ \begin{align}
g(x) & = \frac{L}{2} \| x \|^2_2 - f(x) \quad \text{với } dom(g) = dom(f)
\end{align} $$
</div>

Nói cách khác, $$f(x)$$ có thể biểu diễn dưới dạng hiệu giữa một hàm bậc hai và một hàm lồi.

## Chứng minh

Ta sẽ chứng minh cả cận trên bậc hai lẫn đặc trưng tương đương dựa trên hai tính chất cơ bản của hàm lồi trơn.

### Kiến thức Chuẩn bị

<div class="textbook-definition" markdown="1">
**Định nghĩa 1 (Toán tử đơn điệu)**: Trên không gian vector $$X$$, toán tử $$T : X \to X^*$$ được gọi là đơn điệu nếu:
> $$(Tu - Tv, u-v) \ge 0, \quad \forall u, v \in X$$
</div>

**Tính chất 1 (Tính đơn điệu của gradient)**: Nếu $$f$$ lồi và khả vi thì $$\nabla f$$ là toán tử đơn điệu:
> $$(\nabla f(y) - \nabla f(x))^T (y-x) \ge 0, \quad \forall x, y$$

**Tính chất 2 (Tính liên tục Lipschitz)**: $$\nabla f$$ liên tục Lipschitz với hằng số $$L$$:
> $$ \| \nabla f(x) - \nabla f(y) \|_2 \le L \| x - y \|_2, \quad \forall x, y$$

### Chứng minh Cận trên Bậc hai

**Bước 1**: Xét hàm một biến $$h(t) = f(x + t(y-x))$$ trên $$t \in [0,1]$$. Theo định lý cơ bản của giải tích:

> $$ \begin{align}
f(y) - f(x) &= h(1) - h(0) = \int_0^1 h'(t) dt \\
&= \int_0^1 \nabla f(x + t(y-x))^T (y-x) dt
\end{align} $$

**Bước 2**: Tách số hạng $$\nabla f(x)^T (y-x)$$ ra ngoài dấu tích phân:
> $$ \begin{align}
f(y) - f(x) &= \nabla f(x)^T (y-x) + \int_0^1 [\nabla f(x + t(y-x)) - \nabla f(x)]^T (y-x) dt
\end{align} $$

**Bước 3**: Áp dụng bất đẳng thức Cauchy–Schwarz và tính liên tục Lipschitz của $$\nabla f$$:
> $$ \begin{align}
&[\nabla f(x + t(y-x)) - \nabla f(x)]^T (y-x) \\
&\le \|\nabla f(x + t(y-x)) - \nabla f(x)\| \cdot \|y-x\| \\
&\le L \cdot t\|y-x\| \cdot \|y-x\| = Lt\|y-x\|^2
\end{align} $$

**Bước 4**: Lấy tích phân trên $$t \in [0,1]$$:
> $$ \begin{align}
f(y) - f(x) &\le \nabla f(x)^T (y-x) + \int_0^1 Lt\|y-x\|^2 dt \\
&= \nabla f(x)^T (y-x) + L\|y-x\|^2 \int_0^1 t dt \\
&= \nabla f(x)^T (y-x) + \frac{L}{2}\|y-x\|^2
\end{align} $$

Suy ra $$f(y) \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2}\|y-x\|^2$$.

### Chứng minh Đặc trưng Tương đương

<div class="textbook-theorem" markdown="1">
**Định lý**: Hàm $$g(x) = \frac{L}{2} \| x \|^2_2 - f(x)$$ là hàm lồi.
</div>

**Chứng minh**: Ta cần chứng minh $$\nabla^2 g(x) \succeq 0$$ (nửa xác định dương).

Từ $$g(x) = \frac{L}{2} \| x \|^2_2 - f(x)$$, ta có:
- $$\nabla g(x) = Lx - \nabla f(x)$$
- $$\nabla^2 g(x) = LI - \nabla^2 f(x)$$

Với mọi vector $$v$$, xét dạng toàn phương $$v^T \nabla^2 g(x) v$$:

> $$ \begin{align}
v^T \nabla^2 g(x) v &= v^T (LI - \nabla^2 f(x)) v \\
&= L\|v\|^2 - v^T \nabla^2 f(x) v
\end{align} $$

Do $$\nabla f$$ liên tục Lipschitz với hằng số $$L$$, ta có $$\nabla^2 f(x) \preceq LI$$, nghĩa là:
$$v^T \nabla^2 f(x) v \le L\|v\|^2$$

Từ đó suy ra $$v^T \nabla^2 g(x) v = L\|v\|^2 - v^T \nabla^2 f(x) v \ge 0$$.

Vậy $$g$$ là hàm lồi. $$\square$$

## Các Ví dụ

### Ví dụ 1: Hàm Bậc hai

Xét $$f(x) = \frac{1}{2}x^T A x + b^T x + c$$ với $$A \succeq 0$$ (nửa xác định dương).

- $$\nabla f(x) = Ax + b$$
- $$\nabla^2 f(x) = A$$
- Với $$\lambda_{max}(A) = L$$, ta có $$\|\nabla f(x) - \nabla f(y)\| = \|A(x-y)\| \le L\|x-y\|$$.

Cận trên bậc hai có dạng:
$$f(y) \le f(x) + (Ax + b)^T(y-x) + \frac{L}{2}\|y-x\|^2$$

Đối với hàm bậc hai, cận này là **chặt** khi $$L = \lambda_{max}(A)$$.

### Ví dụ 2: Hàm Mất mát Logistic

Xét hàm mất mát logistic $$f(x) = \log(1 + e^{a^T x})$$ với $$a \in \mathbb{R}^n$$.

- $$\nabla f(x) = \frac{e^{a^T x}}{1 + e^{a^T x}} a = \sigma(a^T x) a$$
- $$\nabla^2 f(x) = \sigma(a^T x)(1 - \sigma(a^T x)) aa^T$$

Vì $$\sigma(t)(1-\sigma(t)) \le \frac{1}{4}$$ với mọi $$t$$, ta có:
$$\nabla^2 f(x) \preceq \frac{1}{4} aa^T \preceq \frac{\|a\|^2}{4} I$$

Do đó, $$L = \frac{\|a\|^2}{4}$$ và cận trên bậc hai là:
$$f(y) \le f(x) + \sigma(a^T x) a^T(y-x) + \frac{\|a\|^2}{8}\|y-x\|^2$$

### Ví dụ 3: Bài toán Bình phương Tối thiểu

Với $$f(x) = \frac{1}{2}\|Ax - b\|^2$$ trong đó $$A \in \mathbb{R}^{m \times n}$$:

- $$\nabla f(x) = A^T(Ax - b)$$
- $$\nabla^2 f(x) = A^T A$$
- $$L = \lambda_{max}(A^T A) = \sigma_{max}^2(A)$$ (bình phương giá trị kỳ dị lớn nhất của $$A$$).

Cận trên bậc hai có dạng:
$$f(y) \le f(x) + (A^T(Ax - b))^T(y-x) + \frac{\sigma_{max}^2(A)}{2}\|y-x\|^2$$

## Ứng dụng trong Tối ưu hóa

### 1. Chọn Kích thước Bước cho Gradient Descent

Cận trên bậc hai cho phép xác định trực tiếp ngưỡng kích thước bước an toàn. Nếu chọn $$\alpha \le \frac{1}{L}$$, ta có:

$$f(x - \alpha \nabla f(x)) \le f(x) - \alpha \|\nabla f(x)\|^2 + \frac{L\alpha^2}{2}\|\nabla f(x)\|^2$$

Khi $$\alpha \le \frac{1}{L}$$, vế phải được thu gọn thành:
$$f(x - \alpha \nabla f(x)) \le f(x) - \frac{\alpha}{2}\|\nabla f(x)\|^2$$

Bất đẳng thức này đảm bảo hàm mục tiêu **giảm đủ** sau mỗi lần lặp.

### 2. Phân tích Tốc độ Hội tụ

Với gradient descent dùng bước $$\alpha = \frac{1}{L}$$ trên hàm $$\mu$$-lồi mạnh, cận trên bậc hai giúp chứng minh:

$$f(x_{k+1}) - f^* \le \left(1 - \frac{\mu}{L}\right)(f(x_k) - f^*)$$

trong đó $$\mu$$ là hằng số lồi mạnh. Kết quả này cho thấy thuật toán đạt **hội tụ tuyến tính** với hệ số co $$\left(1 - \frac{\mu}{L}\right)$$.

### 3. Phương pháp Gradient Gần kề (Proximal Gradient)

Đối với bài toán tối ưu hợp $$\min_x f(x) + g(x)$$ gồm phần trơn $$f$$ và phần không trơn $$g$$, cận trên bậc hai của $$f$$ dẫn đến bước cập nhật gradient gần kề:

$$x_{k+1} = \text{prox}_{\alpha g}\left(x_k - \alpha \nabla f(x_k)\right)$$

trong đó điều kiện $$\alpha \le \frac{1}{L}$$ đảm bảo hội tụ.

### 4. Các Phương pháp Tăng tốc

Những thuật toán tăng tốc như **gradient tăng tốc Nesterov** và **FISTA** cũng dựa trên cận trên bậc hai để đạt tốc độ hội tụ tối ưu $$O(1/k^2)$$ trên lớp hàm lồi trơn.

## Tóm tắt Các Điểm Chính

1. **Tính chất nền tảng**: Cận trên bậc hai là trụ cột của lý thuyết tối ưu hóa lồi trơn.
2. **Thiết kế thuật toán**: Cung cấp cơ sở lý thuyết để chọn kích thước bước trong các phương pháp bậc nhất.
3. **Phân tích hội tụ**: Cho phép chứng minh chặt chẽ tốc độ hội tụ của nhiều thuật toán tối ưu.
4. **Ý nghĩa thực hành**: Ước lượng hằng số $$L$$ giúp điều chỉnh siêu tham số hiệu quả hơn.
5. **Trực giác hình học**: Hình thức hóa nhận định rằng hàm lồi trơn có độ cong bị chặn trên và luôn nằm dưới một parabol bậc hai.

## Minh họa Hình học

Sơ đồ dưới đây minh họa quan hệ giữa hàm thực, xấp xỉ tuyến tính và cận trên bậc hai:

```
      f(y)
        |
        |     Cận Trên Bậc Hai
        |    f(x) + ∇f(x)ᵀ(y-x) + (L/2)||y-x||²
        |   /
        |  /
        | /     Hàm thực f(y)
        |/     /
       /|     /
      / |    /
     /  |   /    Xấp xỉ Tuyến tính
    /   |  /     f(x) + ∇f(x)ᵀ(y-x)
   /    | /
  /     |/
 /      x        y
/       |         →
        |
```

**Nhận xét chính**:
- **Xấp xỉ tuyến tính** (đường tiếp tuyến) luôn nằm dưới $$f(y)$$ do tính lồi.
- **Cận trên bậc hai** luôn nằm trên $$f(y)$$.
- **Hàm thực** $$f(y)$$ nằm kẹp giữa hai cận này.
- Khoảng cách giữa hai cận phụ thuộc vào hằng số Lipschitz $$L$$ và bình phương khoảng cách $$\|y-x\|^2$$.

## Cân nhắc khi Triển khai

### Ước lượng Hằng số Lipschitz

Trong thực tế, việc xác định chính xác hằng số Lipschitz $$L$$ thường không đơn giản. Các cách tiếp cận phổ biến gồm:

1. **Tính giải tích**: Áp dụng cho các lớp hàm cụ thể (bậc hai, logistic, bình phương tối thiểu...).
2. **Phương pháp phổ**: Tính $$L = \lambda_{max}(\nabla^2 f)$$ khi có thể tính ma trận Hessian.
3. **Ước lượng thích ứng**: Khởi tạo một ước lượng ban đầu rồi điều chỉnh dần dựa trên điều kiện giảm đủ.
4. **Tìm kiếm đường**: Dùng tìm kiếm đường lùi (backtracking) để tự động tìm bước nhảy phù hợp.

### Cài đặt Minh họa

```python
def gradient_descent_with_lipschitz(f, grad_f, x0, L_estimate=1.0, max_iter=1000):
    """
    Gradient descent với ước lượng hằng số Lipschitz thích ứng
    """
    x = x0
    L = L_estimate
    
    for k in range(max_iter):
        grad = grad_f(x)
        
        # Thử bước với ước lượng L hiện tại
        alpha = 1.0 / L
        x_new = x - alpha * grad
        
        # Kiểm tra điều kiện giảm đủ
        if f(x_new) <= f(x) - 0.5 * alpha * np.linalg.norm(grad)**2:
            x = x_new  # Chấp nhận bước
        else:
            L *= 2  # Tăng ước lượng L và thử lại
            continue
            
        # Tùy chọn: giảm L nếu bước quá bảo thủ
        if k % 10 == 0:
            L *= 0.9
            
    return x
```

Cách tiếp cận thích ứng này đảm bảo hàm mục tiêu giảm ổn định đồng thời tự động hiệu chỉnh ước lượng hằng số Lipschitz $$L$$.