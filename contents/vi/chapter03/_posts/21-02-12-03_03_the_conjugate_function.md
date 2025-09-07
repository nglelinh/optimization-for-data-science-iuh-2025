---
layout: post
title: 03-03 Hàm liên hợp
chapter: '03'
order: 7
owner: Minjoo Lee
categories:
- chapter03
lang: vi
lesson_type: required
---

Phần này giới thiệu hàm liên hợp (còn gọi là liên hợp lồi hoặc liên hợp Fenchel), một khái niệm cơ bản trong giải tích lồi và lý thuyết đối ngẫu, cung cấp một công cụ mạnh mẽ để biến đổi các bài toán tối ưu.

## Định nghĩa và Nền tảng Toán học

Với một hàm $$f: \mathbb{R}^n \to \mathbb{R}$$, **hàm liên hợp** $$f^*: \mathbb{R}^n \to \mathbb{R}$$ được định nghĩa là:

$$f^*(y) = \sup_{x \in \text{dom}(f)} \{y^T x - f(x)\}$$

trong đó $$\sup$$ biểu thị supremum (cận trên nhỏ nhất) trên tất cả $$x$$ trong miền xác định của $$f$$.

### Giải thích Hình học

Hàm liên hợp có một giải thích hình học đẹp:
- $$f^*(y)$$ biểu thị **khoảng cách tối đa** giữa hàm tuyến tính $$y^T x$$ và hàm gốc $$f(x)$$
- Về mặt hình học, nó đo lường mức độ siêu phẳng với độ dốc $$y$$ có thể được "nâng lên trên" đồ thị của $$f$$
- Liên hợp biến đổi hàm từ "không gian nguyên thủy" sang "không gian đối ngẫu" của các độ dốc

### Tại sao nó quan trọng?

Hàm liên hợp được sử dụng để:
1. Biến đổi các bài toán tối ưu thành các **bài toán đối ngẫu** tương ứng
2. Cung cấp các công cụ phân tích cho **lý thuyết đối ngẫu** (được đề cập trong Chương 11)
3. Cho phép thế trực tiếp trong **Đối ngẫu Lagrange** mà không cần lấy đạo hàm rõ ràng
4. Thiết lập kết nối giữa các nghiệm tối ưu nguyên thủy và đối ngẫu

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/conjugate_function.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Hàm liên hợp [2]</figcaption>
</p>
</figure>

## Các Tính chất Cơ bản

Hàm liên hợp có nhiều tính chất đáng chú ý khiến nó trở thành một công cụ phân tích mạnh mẽ:

### 1. Tính chất Lồi
- **$$f^*$$ luôn lồi**, bất kể $$f$$ có lồi hay không
- Điều này là do $$f^*(y)$$ là supremum theo điểm của các hàm affine $$y^T x - f(x)$$
- Supremum của bất kỳ tập hợp nào các hàm lồi (affine) đều lồi

### 2. Bất đẳng thức Fenchel
Với bất kỳ $$x$$ và $$y$$:
$$f(x) + f^*(y) \geq x^T y$$

Bất đẳng thức cơ bản này thiết lập mối quan hệ cận dưới giữa một hàm và liên hợp của nó.

### 3. Liên hợp của Liên hợp (Liên hợp kép)
- Nói chung: $$f^{**} \leq f$$ (liên hợp kép là một cận dưới)
- **Nếu $$f$$ đóng và lồi**: $$f^{**} = f$$ (phục hồi hoàn hảo)
- Tính chất này rất quan trọng cho lý thuyết đối ngẫu

### 4. Mối quan hệ Dưới vi phân
Nếu $$f$$ đóng và lồi, thì với bất kỳ $$x, y$$:
$$y \in \partial f(x) \iff x \in \partial f^*(y) \iff f(x) + f^*(y) = x^T y$$

Điều này thiết lập một sự đối xứng đẹp giữa không gian nguyên thủy và đối ngẫu.

## Các Ví dụ Chi tiết

### Ví dụ 1: Logarithm Âm
Xem xét $$f(x) = -\log x$$ với $$x > 0$$.

**Tính toán từng bước:**
$$f^*(y) = \sup_{x>0} \{xy + \log x\}$$

Để tìm supremum, chúng ta lấy đạo hàm theo $$x$$:
$$\frac{d}{dx}(xy + \log x) = y + \frac{1}{x} = 0$$

Điều này cho ta $$x^* = -\frac{1}{y}$$ (chỉ hợp lệ khi $$y < 0$$).

**Kết quả:**
$$f^*(y) = \begin{cases}
-1 - \log(-y), & \text{nếu } y < 0 \\
+\infty, & \text{nếu } y \geq 0
\end{cases}$$

### Ví dụ 2: Hàm Bậc hai
Xem xét $$f(x) = \frac{1}{2}x^T Q x$$ trong đó $$Q \succ 0$$ (xác định dương).

**Tính toán từng bước:**
$$f^*(y) = \sup_{x} \{y^T x - \frac{1}{2}x^T Q x\}$$

Lấy gradient và đặt bằng không:
$$\nabla_x (y^T x - \frac{1}{2}x^T Q x) = y - Qx = 0$$

Điều này cho ta $$x^* = Q^{-1}y$$.

Thế ngược lại:
$$f^*(y) = y^T Q^{-1} y - \frac{1}{2}(Q^{-1}y)^T Q (Q^{-1}y) = \frac{1}{2}y^T Q^{-1} y$$

### Ví dụ 3: Giá trị Tuyệt đối (trường hợp 1D)
Xem xét $$f(x) = \lvert x \rvert$$ với $$x \in \mathbb{R}$$.

$$f^*(y) = \sup_{x} \{yx - \lvert x \rvert\}$$

**Phân tích theo trường hợp:**
- Nếu $$\lvert y \rvert \leq 1$$: Supremum là hữu hạn và bằng 0
- Nếu $$\lvert y \rvert > 1$$: Supremum là $$+\infty$$

**Kết quả:**
$$f^*(y) = \begin{cases}
0, & \text{nếu } \lvert y \rvert \leq 1 \\
+\infty, & \text{nếu } \lvert y \rvert > 1
\end{cases}$$

Đây là **hàm chỉ thị** của khoảng $$[-1, 1]$$.

### Ví dụ 4: Hàm Mũ
Xem xét $$f(x) = e^x$$ với $$x \in \mathbb{R}$$.

$$f^*(y) = \sup_{x} \{yx - e^x\}$$

Đặt đạo hàm bằng không: $$y - e^x = 0$$, vậy $$x^* = \log y$$ (hợp lệ với $$y > 0$$).

**Kết quả:**
$$f^*(y) = \begin{cases}
y \log y - y, & \text{nếu } y > 0 \\
0, & \text{nếu } y = 0 \\
+\infty, & \text{nếu } y < 0
\end{cases}$$

## Ứng dụng trong Tối ưu hóa

Hàm liên hợp đóng vai trò quan trọng trong:

1. **Đối ngẫu Lagrange**: Chuyển đổi các bài toán nguyên thủy thành bài toán đối ngẫu
2. **Đối ngẫu Fenchel**: Một khung tổng quát cho đối ngẫu tối ưu lồi
3. **Toán tử Gần kề**: Được sử dụng trong các thuật toán tối ưu hiện đại
4. **Phân tích Biến phân**: Nghiên cứu các bài toán tối ưu thông qua các cặp liên hợp

Các ứng dụng này sẽ được khám phá chi tiết trong Chương 11 và 13.

## Trực quan Hóa Tương tác

Để hiểu rõ hơn cách hàm liên hợp hoạt động, hãy khám phá trực quan hóa tương tác của chúng tôi:

<div style="text-align: center; margin: 20px 0;">
    <a href="../conjugate_function_interactive.html" target="_blank" 
       style="display: inline-block; padding: 12px 24px; background-color: #3498db; color: white; text-decoration: none; border-radius: 6px; font-weight: bold; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
        🎯 Khởi động Công cụ Khám phá Hàm Liên hợp Tương tác
    </a>
</div>

Công cụ tương tác cho phép bạn:
- **Trực quan hóa các loại hàm khác nhau** và liên hợp của chúng cạnh nhau
- **Điều chỉnh tham số** để xem chúng ảnh hưởng đến liên hợp như thế nào
- **Khám phá các đường tiếp tuyến** để hiểu giải thích hình học
- **So sánh nhiều ví dụ** với giải thích toán học chi tiết

## Tóm tắt và Những Điểm Chính

Hàm liên hợp là một công cụ toán học mạnh mẽ:

1. **Biến đổi hàm** từ không gian nguyên thủy sang không gian đối ngẫu thông qua phép toán $$f^*(y) = \sup_x \{y^T x - f(x)\}$$
2. **Luôn tạo ra các hàm lồi**, bất kể tính lồi của hàm gốc
3. **Thiết lập các bất đẳng thức cơ bản** như bất đẳng thức Fenchel: $$f(x) + f^*(y) \geq x^T y$$
4. **Kích hoạt lý thuyết đối ngẫu** bằng cách kết nối các bài toán tối ưu nguyên thủy và đối ngẫu
5. **Cung cấp các công cụ phân tích** để giải các bài toán tối ưu phức tạp

Hiểu biết về hàm liên hợp là thiết yếu cho:
- **Lý thuyết tối ưu lồi** và phát triển thuật toán
- **Đối ngẫu Lagrange** và xây dựng bài toán đối ngẫu  
- **Các phương pháp tối ưu hiện đại** như thuật toán gần kề
- **Phân tích biến phân** và kinh tế toán học

Trực giác hình học về "khoảng cách tối đa giữa hàm tuyến tính và phi tuyến" cung cấp sự hiểu biết trực quan bổ sung cho định nghĩa phân tích, làm cho khái niệm trừu tượng này dễ tiếp cận hơn cho người học.

