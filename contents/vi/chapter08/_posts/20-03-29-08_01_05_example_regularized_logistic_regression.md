---
layout: post
title: '08-01-05 Ví dụ: Hồi quy Logistic có Điều Chuẩn'
chapter: '08'
order: 7
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
lesson_type: required
---

Hồi quy logistic là "ngựa thồ" kinh điển của học máy thống kê — hàm mất mát log-loss của nó trơn vô hạn lần, lồi đẹp đẽ và có gradient tính trong chớp mắt. Thế nhưng chỉ cần thêm vào một số hạng điều chuẩn chuẩn $$\ell_1$$ nhỏ bé $$\lambda \|\beta\|_1$$ để tự động loại bỏ các đặc trưng nhiễu và tạo mô hình thưa (sparse), toàn bộ các siêu phẳng tọa độ $$\beta_j = 0$$ lập tức biến thành những đường gãy sắc cạnh!

Ngay tại thời điểm mô hình đạt độ thưa mong muốn (nhiều trọng số $$\beta_j = 0$$), đạo hàm cổ điển lại biến mất đúng ở những tọa độ đó. Bài học này cho thấy cách phương pháp subgradient bước vào giải quyết trọn vẹn bài toán hồi quy logistic có điều chuẩn $$\ell_1$$ (và so sánh với điều chuẩn $$\ell_2$$ trơn), đồng thời làm lộ ra một tinh tế quan trọng: khi một trọng số bằng $$0$$, ta được quyền chọn bất kỳ giá trị nào trong đoạn $$[-\lambda, \lambda]$$ cho thành phần subgradient tương ứng.

## Bản đồ kiến thức nền: Ba trụ cột của hồi quy logistic có điều chuẩn

- **Hàm mất mát log-loss và tính lồi trơn:** Với xác suất dự đoán $$p_i(\beta) = \sigma(x_i^T\beta) = \frac{1}{1 + e^{-x_i^T\beta}}$$, đạo hàm của $$-\sum (y_i x_i^T\beta - \log(1 + e^{x_i^T\beta}))$$ có dạng cực kỳ trực quan: $$\nabla \ell(\beta) = \sum_{i=1}^n (p_i(\beta) - y_i) x_i$$ — chính là tổng các vector đặc trưng có trọng số bằng sai số dự đoán!
- **Điều chuẩn $$\ell_1$$ vs $$\ell_2$$ và hình học tạo thưa:** Số hạng $$\frac{\lambda}{2}\|\beta\|_2^2$$ trơn khắp nơi và chỉ co nhỏ trọng số về gần $$0$$; trong khi $$\lambda\|\beta\|_1$$ có góc nhọn dọc các trục tọa độ, tạo ra dưới vi phân $$\partial(\lambda|\beta_j|)\big|_0 = [-\lambda, \lambda]$$ đủ rộng để hấp thụ gradient nhỏ của hàm mất mát và giữ chặt $$\beta_j = 0$$.
- **Quy tắc cộng dưới vi phân (Moreau–Rockafellar):** Vì cả hàm mất mát log-loss lẫn hàm phạt $$\lambda\|\beta\|_1$$ đều lồi và xác định trên toàn $$\mathbb{R}^p$$, dưới vi phân của tổng bằng tổng các dưới vi phân: $$\partial f(\beta) = \nabla \ell(\beta) + \lambda \partial \|\beta\|_1$$. Ta chỉ cần tính từng phần rồi cộng lại theo từng tọa độ.

### Khung giải thích (nên đọc chậm): Tính tay một bước subgradient cho hồi quy logistic $$\ell_1$$

Xét tập dữ liệu 1 chiều cực gọn gồm 2 mẫu: $$(x_1, y_1) = (1, 1)$$ và $$(x_2, y_2) = (-1, 0)$$, hệ số điều chuẩn $$\lambda = 0.5$$:
$$f(\beta) = \sum_{i=1}^2 \big(-y_i x_i \beta + \log(1 + e^{x_i \beta})\big) + 0.5|\beta|.$$

1. **Tính gradient phần log-loss tại điểm khởi tạo $$\beta^{(0)} = 0$$:**
   Tại $$\beta = 0$$, xác suất dự đoán cho cả hai mẫu đều là $$p_1(0) = p_2(0) = \frac{1}{1 + e^0} = 0.5$$.
   - Đóng góp mẫu 1: $$(p_1 - y_1) x_1 = (0.5 - 1)(1) = -0.5$$.
   - Đóng góp mẫu 2: $$(p_2 - y_2) x_2 = (0.5 - 0)(-1) = -0.5$$.
   - Tổng gradient phần trơn: $$\nabla \ell(0) = -0.5 + (-0.5) = -1.0$$.
2. **Xác định tập dưới vi phân $$\partial f(0)$$ và kiểm tra xem $$\beta = 0$$ có tối ưu không:**
   Vì $$\partial (0.5|\beta|)\big|_0 = [-0.5, 0.5]$$, ta có:
   $$\partial f(0) = -1.0 + [-0.5, 0.5] = [-1.5, -0.5].$$
   Vì $$0 \notin [-1.5, -0.5]$$, điểm $$\beta = 0$$ **chưa tối ưu** (tín hiệu dữ liệu mạnh hơn lực phạt $$\lambda = 0.5$$). Ngược lại, nếu ta tăng $$\lambda = 1.2$$, thì $$\partial f(0) = [-2.2, 0.2] \ni 0$$ và $$\beta^* = 0$$ lập tức là nghiệm tối ưu!
3. **Thực hiện một bước cập nhật subgradient với $$t_1 = 0.5$$:**
   Chọn $$s^{(0)} = 0 \in [-1, 1]$$ cho $$\partial |\beta|\big|_0$$ (quy ước phổ biến nhất trong code), ta có $$g^{(0)} = -1.0 + 0.5(0) = -1.0$$.
   $$\beta^{(1)} = 0 - 0.5(-1.0) = 0.5.$$
   Khi $$\beta^{(1)} = 0.5 > 0$$, ta kiểm tra: $$f(0) = 2\ln 2 \approx 1.386$$, còn $$f(0.5) = -0.5 + \ln(1+e^{0.5}) + \ln(1+e^{-0.5}) + 0.25 = -0.5 + 0.974 + 0.474 + 0.25 = 1.198 < 1.386$$!

Cho tập dữ liệu $$(x_i, y_i) \in \mathbb{R}^p \times \{0, 1\}$$ với $$i=1,...,n$$. Hàm mất mát của hồi quy logistic được định nghĩa như sau:
>
\begin{align}
f(\beta) = \sum_{i=1}^n\big(-y_ix_i^T\beta + \log(1+\exp(x_i^T\beta))\big)
\end{align}

Vì đây là tổng hữu hạn của các hàm tuyến tính và hàm log-sum-exp, $$f(\beta)$$ là hàm lồi và khả vi.

Xét bài toán hồi quy logistic có chính quy hóa đối với $$\beta$$:

>
\begin{align}
\min_{\beta} \text{ } f(\beta) + \lambda \cdot P(\beta)
\end{align}

trong đó thành phần phạt $$P(\beta)$$ có thể là $$\Vert \beta \Vert _2^2$$ (chính quy hóa Ridge) hoặc $$\Vert \beta \Vert _1$$ (chính quy hóa Lasso).

Hàm mục tiêu với phạt Ridge vẫn là hàm lồi khả vi, còn hàm mục tiêu với phạt Lasso là hàm lồi không khả vi. Khi áp dụng gradient descent cho bài toán Ridge và phương pháp subgradient cho bài toán Lasso, rồi vẽ giá trị hàm mục tiêu theo số bước lặp $$k$$, ta có thể trực quan hóa sự khác biệt về tốc độ hội tụ giữa hai phương pháp.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter08/08_01_grad_vs_subgrad.png" alt="grad_vs_subgrad" width="90%" height="90%">
</p>
  <figcaption style="text-align: center;">[Fig 1] Gradient descent so với phương pháp Subgradient [3]</figcaption>
</figure>

Kết quả thực nghiệm cho thấy gradient descent hội tụ nhanh hơn đáng kể so với phương pháp subgradient.
