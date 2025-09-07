---
layout: post
title: 04-03 Điều kiện tối ưu
chapter: '04'
order: 4
owner: YoungJae Choung
categories:
- chapter04
lang: vi
lesson_type: required
---

## Điều kiện tối ưu bậc nhất

Để tìm hiểu thêm về hàm lồi, xem [Chương 3: Các Tính chất Chính của Hàm Lồi]({% multilang_post_url contents/chapter03/20-02-08-03_01_key_properties_of_convex_functions %}).

>$$
\begin{aligned}
&\min_x &&f(x) \\
&\text{subject to} &&x \in C
\end{aligned}
$$

Đối với một bài toán lồi mà hàm mục tiêu $$f$$ **khả vi**, điều kiện sau là cần và đủ cho một điểm tối ưu $$x$$:

> $$\nabla f(x)^{T}(y-x) \geq 0 \\
> \text{ với mọi } y \in C$$

Đây được gọi là *điều kiện bậc nhất cho tính tối ưu*. 

$$\nabla f(x)^{T}(y-x) = 0$$ định nghĩa một siêu phẳng đi qua $$x$$ trong tập $$C$$, và $$- \nabla f(x)$$ chỉ hướng di chuyển về phía điểm tối ưu $$x$$. <br><br>

Nếu điều kiện trên được thỏa mãn, 
tập $$C$$ nằm trong nửa không gian đối diện với $$- \nabla f(x)$$, 
nên $$x$$ là một điểm tối ưu.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter04/first-order-condition.png" alt="[Fig1] geometric interpretation of first-order condition for optimality [3]">
  <figcaption style="text-align: center;">[Hình 1] Giải thích hình học về điều kiện bậc nhất cho tính tối ưu [3]</figcaption>
</p>
</figure>
<br>

### Trường hợp đặc biệt quan trọng
Khi $$C = \mathbb{R}^n$$ (tối ưu hóa không ràng buộc),
điều kiện tối ưu là:
> $$\nabla f(x) = 0$$

Trong trường hợp này, $$-\nabla f(x)$$ chỉ về phía điểm tối ưu $$x$$, và $$\nabla f(x) = 0$$ có nghĩa là không còn hướng nào để di chuyển để giảm $$f$$ tại $$x$$.

---


## Nền tảng Toán học

Trong khi các điều kiện bậc nhất sờ dụng gradient $$\nabla f(x)$$, các điều kiện bậc hai sử dụng **ma trận Hessian**:

$$H_f(x) = \nabla^2 f(x) = \begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}$$

Ma trận Hessian nắm bắt **độ cong** của hàm tại điểm $$x$$, cung cấp thông tin về hình dạng cục bộ của hàm mục tiêu.

## Điều kiện Tối ưu Bậc Hai

Xem xét bài toán tối ưu hóa không ràng buộc:
$$\min_x f(x)$$

trong đó $$f: \mathbb{R}^n \to \mathbb{R}$$ khả vi liên tục bậc hai.

### Điều kiện Cần (Bậc Hai)

Nếu $$x^*$$ là cực tiểu địa phương của $$f$$, thì:

1. **Điều kiện cần bậc nhất**: $$\nabla f(x^*) = 0$$
2. **Điều kiện cần bậc hai**: $$\nabla^2 f(x^*) \succeq 0$$ (nửa xác định dương)

### Điều kiện Đủ (Bậc Hai)

Nếu tại điểm $$x^*$$:

1. $$\nabla f(x^*) = 0$$ (điều kiện bậc nhất)
2. $$\nabla^2 f(x^*) \succ 0$$ (xác định dương)

Thì $$x^*$$ là **cực tiểu địa phương chặt** của $$f$$.

## Hiểu về Tính Xác Định Dương

Một ma trận đối xứng $$A$$ là:
- **Xác định dương** ($$A \succ 0$$) nếu $$v^T A v > 0$$ với mọi $$v \neq 0$$
- **Nửa xác định dương** ($$A \succeq 0$$) nếu $$v^T A v \geq 0$$ với mọi $$v$$

**Các kiểm tra thực tế cho tính xác định dương:**
1. **Kiểm tra giá trị riêng**: Tất cả giá trị riêng đều dương
2. **Thứ định thức chính**: Tất cả thứ định thức chính đều dương
3. **Phân tích Cholesky**: $$A = L L^T$$ tồn tại với $$L$$ tam giác dưới

## Giải thích Hình học

Các điều kiện bậc hai cung cấp thông tin về **độ cong** tại điểm tới hạn:

- **$$\nabla^2 f(x^*) \succ 0$$**: Hàm cong lên trên theo mọi hướng → **cực tiểu địa phương chặt**
- **$$\nabla^2 f(x^*) \prec 0$$**: Hàm cong xuống dưới theo mọi hướng → **cực đại địa phương chặt**  
- **$$\nabla^2 f(x^*) \succeq 0$$**: Độ cong không âm → **có thể là cực tiểu**
- **Hessian bất định**: Độ cong hỗn hợp → **điểm yên ngựa**

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter04/second-order-conditions.png" alt="Second-order optimality conditions visualization" width="80%" height="80%">
 <figcaption style="text-align: center;">[Hình 1] Giải thích hình học về các điều kiện bậc hai</figcaption>
</p>
</figure>

## Các Ví dụ Chi tiết

### Ví dụ 1: Hàm Bậc Hai
Xem xét $$f(x_1, x_2) = x_1^2 + 2x_2^2 + x_1 x_2$$

**Bước 1: Tìm điểm tới hạn**
$$\nabla f(x) = \begin{bmatrix} 2x_1 + x_2 \\ 4x_2 + x_1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

Giải: $$x^* = (0, 0)$$

**Bước 2: Tính Hessian**
$$\nabla^2 f(x) = \begin{bmatrix} 2 & 1 \\ 1 & 4 \end{bmatrix}$$

**Bước 3: Kiểm tra tính xác định dương**
- Giá trị riêng: $$\lambda_1 = \frac{6 + \sqrt{12}}{2} > 0$$, $$\lambda_2 = \frac{6 - \sqrt{12}}{2} > 0$$
- Thứ định thức chính: $$2 > 0$$, $$\det = 8 - 1 = 7 > 0$$

**Kết luận**: $$\nabla^2 f(0,0) \succ 0$$ → $$(0,0)$$ là cực tiểu địa phương chặt.

### Example 2: Non-Convex Function
Consider $$f(x_1, x_2) = x_1^4 + x_2^4 - 2x_1^2 - 2x_2^2$$

**Step 1: Find critical points**
$$\nabla f(x) = \begin{bmatrix} 4x_1^3 - 4x_1 \\ 4x_2^3 - 4x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

Critical points: $$(0,0)$$, $$(\pm 1, 0)$$, $$(0, \pm 1)$$, $$(\pm 1, \pm 1)$$

**Step 2: Analyze $$(0,0)$$**
$$\nabla^2 f(0,0) = \begin{bmatrix} -4 & 0 \\ 0 & -4 \end{bmatrix} \prec 0$$

**Conclusion**: $$(0,0)$$ is a strict local maximum.

**Step 3: Analyze $$(1,1)$$**
$$\nabla^2 f(1,1) = \begin{bmatrix} 8 & 0 \\ 0 & 8 \end{bmatrix} \succ 0$$

**Conclusion**: $$(1,1)$$ is a strict local minimum.

### Example 3: Saddle Point
Consider $$f(x_1, x_2) = x_1^2 - x_2^2$$

**Analysis at $$(0,0)$$:**
- $$\nabla f(0,0) = (0,0)$$ ✓
- $$\nabla^2 f(0,0) = \begin{bmatrix} 2 & 0 \\ 0 & -2 \end{bmatrix}$$ (indefinite)

**Conclusion**: $$(0,0)$$ is a saddle point (neither minimum nor maximum).

## Constrained Optimization: Second-Order Conditions

For constrained problems:
$$\min_x f(x) \text{ subject to } h_i(x) = 0, \, i = 1,\ldots,m$$

The **bordered Hessian** of the Lagrangian is used:
$$\mathcal{L}(x,\lambda) = f(x) + \sum_{i=1}^m \lambda_i h_i(x)$$

**Second-order sufficient condition**: The bordered Hessian has the correct inertia (number of negative eigenvalues equals the number of constraints).

## Comparison: First vs Second-Order Conditions

| Aspect | First-Order | Second-Order |
|--------|-------------|--------------|
| **Information** | Gradient (slope) | Hessian (curvature) |
| **Necessary condition** | $$\nabla f(x^*) = 0$$ | $$\nabla f(x^*) = 0$$ and $$\nabla^2 f(x^*) \succeq 0$$ |
| **Sufficient condition** | Not available for unconstrained | $$\nabla f(x^*) = 0$$ and $$\nabla^2 f(x^*) \succ 0$$ |
| **Strength** | Weaker | Stronger |
| **Computational cost** | $$O(n)$$ | $$O(n^2)$$ |
| **Distinguishes** | Critical points | Minima, maxima, saddle points |

## Interactive Visualization

Explore how second-order conditions work in practice:

<div style="text-align: center; margin: 20px 0;">
    <a href="../second_order_conditions_interactive.html" target="_blank" 
       style="display: inline-block; padding: 12px 24px; background-color: #e74c3c; color: white; text-decoration: none; border-radius: 6px; font-weight: bold; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
        🎯 Khởi động Công cụ Khám phá Điều kiện Bậc Hai
    </a>
</div>

Công cụ tương tác minh họa:
- **Phân tích giá trị riêng Hessian** cho các loại hàm khác nhau
- **Phân loại trực quan** các điểm tới hạn (cực tiểu, cực đại, yên ngựa)
- **Đồ thị đường đẳng mức** hiển thị hành vi độ cong cục bộ
- **Tính toán từng bước** cho các kiểm tra bậc hai

## Tóm tắt và Các Điểm Chính

Các điều kiện tối ưu bậc hai cung cấp **đặc trưng mạnh hơn** cho các điểm tối ưu:

### **Kết quả Chính:**
1. **Điều kiện cần**: $$\nabla f(x^*) = 0$$ và $$\nabla^2 f(x^*) \succeq 0$$
2. **Điều kiện đủ**: $$\nabla f(x^*) = 0$$ và $$\nabla^2 f(x^*) \succ 0$$
3. **Khả năng phân loại**: Có thể phân biệt giữa cực tiểu, cực đại và điểm yên ngựa

### **Tầm quan trọng Thực tế:**
- **Thiết kế thuật toán**: Nền tảng cho các phương pháp kiểu Newton
- **Phân tích tính lồi**: Thiết yếu cho việc xác minh hàm lồi
- **Tính bền vững**: Đảm bảo mạnh hơn so với chỉ các điều kiện bậc nhất
- **Lý thuyết tối ưu hóa**: Cầu nối giữa tính tối ưu địa phương và toàn cục

### **Cân nhắc Tính toán:**
- **Chi phí**: Lưu trữ và tính toán $$O(n^2)$$ cho Hessian
- **Xấp xỉ**: Các phương pháp Quasi-Newton giảm gánh nặng tính toán
- **Ổn định số**: Tính toán giá trị riêng yêu cầu triển khai cẩn thận

Hiểu về các điều kiện bậc hai là thiết yếu cho lý thuyết tối ưu hóa nâng cao và phát triển các thuật toán số hiệu quả. Chúng cung cấp nền tảng toán học cho nhiều phương pháp tối ưu hóa hiện đại và đưa ra các hiểu biết sâu sắc hơn về cấu trúc của các bài toán tối ưu hóa.
