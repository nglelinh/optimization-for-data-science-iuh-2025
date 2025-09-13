---
layout: post
title: 06-03-01 Cận trên bậc hai của hàm lồi
chapter: '06'
order: 8
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

## Giới thiệu

**Cận trên bậc hai** là một tính chất cơ bản của các hàm lồi trơn, cung cấp một công cụ quan trọng để phân tích và thiết kế các thuật toán tối ưu hóa. Tính chất này thiết lập rằng bất kỳ hàm lồi trơn nào cũng có thể được chặn trên bởi một hàm bậc hai, điều này có những ý nghĩa quan trọng cho việc phân tích hội tụ của các phương pháp dựa trên gradient.

## Động lực

Tại sao chúng ta quan tâm đến cận trên bậc hai?

1. **Thiết kế thuật toán**: Nhiều thuật toán tối ưu hóa (như gradient descent) dựa vào các xấp xỉ cục bộ của hàm mục tiêu. Cận trên bậc hai cung cấp một cách hệ thống để xây dựng các xấp xỉ này.

2. **Phân tích hội tụ**: Cận trên bậc hai cho phép chúng ta chứng minh tốc độ hội tụ cho các thuật toán tối ưu hóa bằng cách chặn mức độ thay đổi của hàm.

3. **Lựa chọn bước nhảy**: Hằng số Lipschitz $$L$$ trong cận trực tiếp xác định bước nhảy an toàn cho gradient descent.

## Tính chất Cận trên Bậc hai

**Định lý**: Nếu $$f$$ là lồi và $$\nabla f$$ liên tục Lipschitz với hằng số $$L$$, thì $$f$$ thỏa mãn cận trên bậc hai:

> $$ \begin{align}
f(y) & \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \| y - x \|^2_2 \quad \forall x, y
\end{align} $$

### Diễn giải Hình học

Bất đẳng thức này phát biểu rằng:
- **Xấp xỉ tuyến tính** $$f(x) + \nabla f(x)^T (y-x)$$ (khai triển Taylor bậc nhất) ước lượng thấp $$f(y)$$ do tính lồi
- **Cận trên bậc hai** $$f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \| y - x \|^2_2$$ ước lượng cao $$f(y)$$
- Hàm $$f(y)$$ được "kẹp" giữa hai cận này

### Đặc trưng Tương đương

**Hệ quả**: Đối với bất kỳ hàm lồi trơn $$f$$ nào, hàm sau đây là lồi:

> $$ \begin{align}
g(x) & = \frac{L}{2} \| x \|^2_2 - f(x) \quad \text{với } dom(g) = dom(f)
\end{align} $$

Điều này có nghĩa là $$f(x)$$ có thể được viết như hiệu của một hàm bậc hai và một hàm lồi.

## Chứng minh

Chúng ta sẽ chứng minh cả cận trên bậc hai và đặc trưng tương đương. Chứng minh dựa trên hai tính chất chính của các hàm lồi trơn.

### Kiến thức Cần thiết

**Định nghĩa 1 (Toán tử Đơn điệu)**: Trong không gian vector $$X$$, toán tử $$T : X \to X^*$$ là đơn điệu nếu:
> $$(Tu - Tv, u-v) \ge 0, \quad \forall u, v \in X$$

**Tính chất 1 (Tính đơn điệu của Gradient)**: Nếu $$f$$ là lồi và khả vi, thì $$\nabla f$$ là toán tử đơn điệu:
> $$(\nabla f(y) - \nabla f(x))^T (y-x) \ge 0, \quad \forall x, y$$

**Tính chất 2 (Liên tục Lipschitz)**: $$\nabla f$$ liên tục Lipschitz với hằng số $$L$$:
> $$ \| \nabla f(x) - \nabla f(y) \|_2 \le L \| x - y \|_2, \quad \forall x, y$$

### Chứng minh Cận trên Bậc hai

**Bước 1**: Xét hàm $$h(t) = f(x + t(y-x))$$ với $$t \in [0,1]$$. Theo định lý cơ bản của giải tích:

> $$ \begin{align}
f(y) - f(x) &= h(1) - h(0) = \int_0^1 h'(t) dt \\
&= \int_0^1 \nabla f(x + t(y-x))^T (y-x) dt
\end{align} $$

**Bước 2**: Chúng ta có thể viết lại như sau:
> $$ \begin{align}
f(y) - f(x) &= \nabla f(x)^T (y-x) + \int_0^1 [\nabla f(x + t(y-x)) - \nabla f(x)]^T (y-x) dt
\end{align} $$

**Bước 3**: Sử dụng bất đẳng thức Cauchy-Schwarz và tính liên tục Lipschitz:
> $$ \begin{align}
&[\nabla f(x + t(y-x)) - \nabla f(x)]^T (y-x) \\
&\le \|\nabla f(x + t(y-x)) - \nabla f(x)\| \cdot \|y-x\| \\
&\le L \cdot t\|y-x\| \cdot \|y-x\| = Lt\|y-x\|^2
\end{align} $$

**Bước 4**: Tích phân trên $$t \in [0,1]$$:
> $$ \begin{align}
f(y) - f(x) &\le \nabla f(x)^T (y-x) + \int_0^1 Lt\|y-x\|^2 dt \\
&= \nabla f(x)^T (y-x) + L\|y-x\|^2 \int_0^1 t dt \\
&= \nabla f(x)^T (y-x) + \frac{L}{2}\|y-x\|^2
\end{align} $$

Do đó: $$f(y) \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2}\|y-x\|^2$$

### Chứng minh Đặc trưng Tương đương

**Định lý**: Hàm $$g(x) = \frac{L}{2} \| x \|^2_2 - f(x)$$ là lồi.

**Chứng minh**: Chúng ta cần chỉ ra rằng $$\nabla^2 g(x) \succeq 0$$ (nửa xác định dương).

Vì $$g(x) = \frac{L}{2} \| x \|^2_2 - f(x)$$, ta có:
- $$\nabla g(x) = Lx - \nabla f(x)$$
- $$\nabla^2 g(x) = LI - \nabla^2 f(x)$$

Với bất kỳ vector $$v$$ nào, chúng ta cần chỉ ra $$v^T \nabla^2 g(x) v \ge 0$$:

> $$ \begin{align}
v^T \nabla^2 g(x) v &= v^T (LI - \nabla^2 f(x)) v \\
&= L\|v\|^2 - v^T \nabla^2 f(x) v
\end{align} $$

Từ tính liên tục Lipschitz của $$\nabla f$$, chúng ta có thể chỉ ra rằng $$\nabla^2 f(x) \preceq LI$$, có nghĩa là:
$$v^T \nabla^2 f(x) v \le L\|v\|^2$$

Do đó: $$v^T \nabla^2 g(x) v = L\|v\|^2 - v^T \nabla^2 f(x) v \ge 0$$

Điều này chứng minh rằng $$g$$ là lồi. $$\square$$

## Ví dụ

### Ví dụ 1: Hàm Bậc hai

Xét $$f(x) = \frac{1}{2}x^T A x + b^T x + c$$ với $$A \succeq 0$$ (nửa xác định dương).

- $$\nabla f(x) = Ax + b$$
- $$\nabla^2 f(x) = A$$
- Nếu $$\lambda_{max}(A) = L$$, thì $$\|\nabla f(x) - \nabla f(y)\| = \|A(x-y)\| \le L\|x-y\|$$

Cận trên bậc hai trở thành:
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

### Ví dụ 3: Bình phương Tối thiểu

Với $$f(x) = \frac{1}{2}\|Ax - b\|^2$$ trong đó $$A \in \mathbb{R}^{m \times n}$$:

- $$\nabla f(x) = A^T(Ax - b)$$
- $$\nabla^2 f(x) = A^T A$$
- $$L = \lambda_{max}(A^T A) = \sigma_{max}^2(A)$$ (bình phương giá trị kỳ dị lớn nhất)

Cận trên bậc hai là:
$$f(y) \le f(x) + (A^T(Ax - b))^T(y-x) + \frac{\sigma_{max}^2(A)}{2}\|y-x\|^2$$

## Ứng dụng trong Tối ưu hóa

### 1. Kích thước Bước nhảy của Gradient Descent

Cận trên bậc hai trực tiếp xác định **kích thước bước nhảy an toàn tối đa** cho gradient descent. Nếu chúng ta sử dụng kích thước bước $$\alpha \le \frac{1}{L}$$, thì:

$$f(x - \alpha \nabla f(x)) \le f(x) - \alpha \|\nabla f(x)\|^2 + \frac{L\alpha^2}{2}\|\nabla f(x)\|^2$$

Khi $$\alpha \le \frac{1}{L}$$, vế phải đơn giản hóa thành:
$$f(x - \alpha \nabla f(x)) \le f(x) - \frac{\alpha}{2}\|\nabla f(x)\|^2$$

Điều này đảm bảo **giảm đủ** tại mỗi lần lặp.

### 2. Phân tích Tốc độ Hội tụ

Đối với gradient descent với kích thước bước $$\alpha = \frac{1}{L}$$, cận trên bậc hai cho phép chúng ta chứng minh:

$$f(x_{k+1}) - f^* \le \left(1 - \frac{\mu}{L}\right)(f(x_k) - f^*)$$

trong đó $$\mu$$ là tham số lồi mạnh. Điều này cho **hội tụ tuyến tính** với tốc độ $$\left(1 - \frac{\mu}{L}\right)$$.

### 3. Phương pháp Gradient Gần kề

Trong tối ưu hóa tổng hợp $$\min_x f(x) + g(x)$$ với $$f$$ trơn và $$g$$ không trơn, cận trên bậc hai của $$f$$ dẫn đến cập nhật gradient gần kề:

$$x_{k+1} = \text{prox}_{\alpha g}\left(x_k - \alpha \nabla f(x_k)\right)$$

trong đó $$\alpha \le \frac{1}{L}$$ đảm bảo hội tụ.

### 4. Phương pháp Tăng tốc

Các phương pháp tiên tiến như **gradient tăng tốc Nesterov** và **FISTA** cũng dựa vào cận trên bậc hai để đạt được tốc độ hội tụ tối ưu $$O(1/k^2)$$ cho các hàm lồi trơn.

## Những Điểm Chính

1. **Tính chất Cơ bản**: Cận trên bậc hai là nền tảng của lý thuyết tối ưu hóa lồi trơn.

2. **Thiết kế Thuật toán**: Nó cung cấp cơ sở lý thuyết để chọn kích thước bước trong các phương pháp dựa trên gradient.

3. **Phân tích Hội tụ**: Nó cho phép chứng minh nghiêm ngặt tốc độ hội tụ của các thuật toán tối ưu hóa.

4. **Tác động Thực tế**: Hiểu biết về $$L$$ giúp các nhà thực hành điều chỉnh thuật toán hiệu quả.

5. **Trực giác Hình học**: Nó hình thức hóa ý tưởng rằng các hàm lồi trơn không "cong quá mức" - chúng được chặn trên bởi các parabola.

## Trực quan Tương tác

Sơ đồ sau minh họa tính chất cận trên bậc hai:

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

**Những Quan sát Chính**:
- **Xấp xỉ tuyến tính** (đường tiếp tuyến) nằm dưới $$f(y)$$ do tính lồi
- **Cận trên bậc hai** nằm trên $$f(y)$$ 
- **Hàm thực** $$f(y)$$ được kẹp giữa hai cận này
- Khoảng cách giữa các cận phụ thuộc vào $$L$$ (hằng số Lipschitz) và $$\|y-x\|^2$$

## Cân nhắc Tính toán

### Ước lượng Hằng số Lipschitz

Trong thực tế, việc tìm hằng số Lipschitz chính xác $$L$$ có thể khó khăn. Các phương pháp phổ biến:

1. **Phân tích Lý thuyết**: Đối với các lớp hàm cụ thể (bậc hai, logistic, v.v.)
2. **Phương pháp Phổ**: $$L = \lambda_{max}(\nabla^2 f)$$ khi có Hessian
3. **Phương pháp Thích ứng**: Bắt đầu với ước lượng và điều chỉnh dựa trên điều kiện giảm đủ
4. **Tìm kiếm Đường**: Sử dụng backtracking để tìm kích thước bước phù hợp

### Triển khai Thuật toán Thực tế

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

Phương pháp thích ứng này đảm bảo hội tụ trong khi tự động điều chỉnh ước lượng hằng số Lipschitz.