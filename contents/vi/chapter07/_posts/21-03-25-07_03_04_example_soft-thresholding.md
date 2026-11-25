---
layout: post
title: '07-03-04 Ví dụ: Ngưỡng mềm (Soft-Thresholding)'
chapter: '07'
order: 10
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
---

Nếu bạn từng nghe đến các thuật toán tối ưu không trơn nổi tiếng như **ISTA / FISTA (Proximal Gradient)** hay **ADMM** dùng để giải Lasso hàng triệu biến trong chớp mắt, thì trái tim của tất cả các thuật toán đó nằm gọn trong một toán tử 1 dòng cực kỳ duyên dáng: **Ngưỡng mềm (Soft-Thresholding)**!

Toán tử này xuất hiện ngay khi ta giải trường hợp đơn giản nhất của Lasso với ma trận trực giao $$X = I$$: $$\min_\beta \frac{1}{2}\|y - \beta\|_2^2 + \lambda\|\beta\|_1$$. Nhờ bài toán tách hoàn toàn thành $$p$$ bài toán 1 chiều độc lập, điều kiện subgradient $$0 \in \partial f(\beta^\star)$$ cho ta một **công thức nghiệm đóng tuyệt đẹp**!

## Bản đồ kiến thức nền: Giải phẫu Toán tử Ngưỡng mềm $$S_\lambda(y)$$

Ba trụ cột sau làm rõ cấu trúc và ứng dụng rộng lớn của Soft-Thresholding:

- **Công thức tách tọa độ (Separability):** Vì $$\frac{1}{2}\|y - \beta\|_2^2 + \lambda\|\beta\|_1 = \sum_{i=1}^p \left(\frac{1}{2}(y_i - \beta_i)^2 + \lambda|\beta_i|\right)$$, ta tối ưu độc lập từng tọa độ $$\beta_i$$!
- **Nghiệm đóng Ngưỡng mềm (Soft-Thresholding Operator):** Giải điều kiện $$y_i - \beta_i \in \lambda \partial|\beta_i|$$ cho đúng ba miền:
  $$\beta_i^\star = S_\lambda(y_i) = \begin{cases} y_i - \lambda & \text{nếu } y_i > \lambda \\ 0 & \text{nếu } |y_i| \le \lambda \\ y_i + \lambda & \text{nếu } y_i < -\lambda \end{cases} = \operatorname{sign}(y_i)\max(|y_i| - \lambda,\; 0).$$
- **Ngưỡng mềm (Soft) vs. Ngưỡng cứng (Hard) & Toán tử Proximal:** Khác với ngưỡng cứng (giữ nguyên $$y_i$$ khi $$|y_i| > \lambda$$ nên bị nhảy gián đoạn tại $$\pm \lambda$$), ngưỡng mềm là hàm **liên tục** kéo mọi giá trị về gần 0 một khoảng $$\lambda$$ và dập tắt hoàn toàn mọi nhiễu nằm trong "vùng chết" $$[-\lambda, \lambda]$$. Đây chính là **toán tử proximal** $$\operatorname{prox}_{\lambda\|\cdot\|_1}(y)$$ dùng trong xử lý ảnh wavelet và thuật toán ISTA!

### Khung giải thích (nên đọc chậm): Áp dụng Soft-Thresholding bằng tay lên một vector tín hiệu có nhiễu

Giả sử ta đo được vector tín hiệu lẫn nhiễu $$y = (4.5,\; -0.8,\; 0.3,\; -3.2,\; 1.0)^T$$ và áp dụng ngưỡng mềm với $$\lambda = 1.0$$:

1. **Tọa độ 1 ($$y_1 = 4.5 > 1.0$$):** $$\beta_1^\star = 4.5 - 1.0 = 3.5$$.
2. **Tọa độ 2 ($$y_2 = -0.8 \in [-1, 1]$$):** $$\beta_2^\star = 0$$ (nhiễu âm nhỏ bị dập tắt!).
3. **Tọa độ 3 ($$y_3 = 0.3 \in [-1, 1]$$):** $$\beta_3^\star = 0$$ (nhiễu dương nhỏ bị dập tắt!).
4. **Tọa độ 4 ($$y_4 = -3.2 < -1.0$$):** $$\beta_4^\star = -3.2 + 1.0 = -2.2$$.
5. **Tọa độ 5 ($$y_5 = 1.0$$ nằm đúng biên ngưỡng):** $$\beta_5^\star = 1.0 - 1.0 = 0$$.
6. **Kết quả cuối cùng:** $$\beta^\star = (3.5,\; 0,\; 0,\; -2.2,\; 0)^T$$.
   **Kiểm tra điều kiện subgradient tại tọa độ 4:** $$y_4 - \beta_4^\star = -3.2 - (-2.2) = -1.0 = \lambda \cdot \operatorname{sign}(-2.2)$$ — khớp tuyệt đối! Từ một vector dày đặc 5 phần tử khác 0, chỉ một phép tính tuyến tính $$O(p)$$ đã lọc ra đúng 2 thành phần tín hiệu thưa thực sự!

---

Xét trường hợp đơn giản hơn của bài toán Lasso khi $$X=I$$:
>
\begin{equation}
\min_{\beta} \frac{1}{2} \| y-\beta \|_2^2 + \lambda \| \beta \|_1
\end{equation}

Từ ví dụ trước, điều kiện tối ưu theo gradient dưới của bài toán này là:
>
$$
\begin{cases}
y_i-\beta_i = \lambda \cdot \text{sign}(\beta_i) &\text{nếu } \beta_i \neq 0 \\
 |y_i-\beta_i| \leq \lambda &\text{nếu } \beta_i = 0
\end{cases}
$$

Giải điều kiện trên cho từng tọa độ, ta thu được nghiệm dạng đóng $$\beta = S_{\lambda}(y)$$, với:
>
$$
[S_{\lambda}(y)]_{i} = 
\begin{cases}
y_i - \lambda &\text{nếu }y_i > \lambda \\
0             &\text{nếu }-\lambda \leq y_i \leq \lambda, \quad \quad i \in \{1,2,\dots,n \} \\
y_i + \lambda &\text{nếu } y_i < -\lambda
\end{cases}
$$

Toán tử $$S_{\lambda}$$ được gọi là **toán tử ngưỡng mềm (soft-thresholding operator)**.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_03_subgrad-6.png" alt="connection_to_convexity_geometry" width="80%" height="80%">
</p>
 <figcaption style="text-align: center;">$$\text{[Hình 1] Ngưỡng mềm, y (trục x), } \beta \text{ (trục y), } \lambda=1/2 \text{ [3]}$$ </figcaption>
</figure>