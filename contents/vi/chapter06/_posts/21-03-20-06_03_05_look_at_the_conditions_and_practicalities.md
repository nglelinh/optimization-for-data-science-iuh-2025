---
layout: post
title: 06-03-05 Xem xét điều kiện & Tính thực tiễn
chapter: '06'
order: 14
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Định lý hội tụ trên bảng trắng đẹp như mơ, nhưng khi đem vào thực tế lập trình, hàng loạt câu hỏi "trần trụi" lập tức xuất hiện: *làm sao biết một bài toán thực tế như Hồi quy tuyến tính có $$L$$ và $$m$$ bằng bao nhiêu? Nếu số đặc trưng $$p$$ lớn hơn số mẫu $$n$$ thì tính lồi mạnh có biến mất không? Và vì ta không bao giờ biết trước $$f^\star$$, làm sao biết lúc nào nên dừng vòng lặp?*

Bài học này nối liền lý thuyết hội tụ với kỹ nghệ lập trình tối ưu hóa thực tế: tính cụ thể $$L$$ và $$m$$ từ giá trị kỳ dị (singular values) của ma trận dữ liệu $$X$$, phân tích chi phí mỗi vòng lặp $$O(np)$$, và xây dựng các **tiêu chí dừng (stopping criteria)** đáng tin cậy.

## Bản đồ kiến thức nền: Từ Định lý sang Code thực chiến

Bốn trụ cột dưới đây là hành trang bắt buộc khi triển khai Gradient Descent trên dữ liệu thật:

- **$$L$$ và $$m$$ của Bình phương tối thiểu qua Giá trị kỳ dị:** Với $$f(\beta) = \frac{1}{2}\|y - X\beta\|_2^2$$, ma trận Hessian là hằng số $$\nabla^2 f(\beta) = X^T X$$. Do đó:
  $$L = \lambda_{\max}(X^T X) = \sigma_{\max}^2(X), \qquad m = \lambda_{\min}(X^T X) = \sigma_{\min}^2(X).$$
- **Thảm họa mất tính lồi mạnh khi $$p > n$$:** Nếu số đặc trưng $$p$$ lớn hơn số mẫu $$n$$ (ví dụ dữ liệu gen học có 20.000 gen nhưng chỉ 200 bệnh nhân), ma trận $$X^T X \in \mathbb{R}^{p \times p}$$ có hạng tối đa là $$n < p$$, nên chắc chắn có trị riêng bằng $$0$$ ($$m = 0$$)! Hàm mất tính lồi mạnh — và cách cứu duy nhất là cộng thêm điều chuẩn Ridge $$\frac{\lambda}{2}\|\beta\|_2^2$$ để đẩy $$m$$ lên $$\ge \lambda > 0$$!
- **Tiêu chí dừng thực tế (Stopping Criteria):** Không biết $$f^\star$$, ta dùng độ lớn gradient $$\|\nabla f(x^{(k)})\|_2 \le \epsilon_{\text{grad}}$$ (nhờ bất đẳng thức PL, với hàm lồi mạnh $$m$$ ta biết ngay $$f(x^{(k)}) - f^\star \le \frac{1}{2m}\|\nabla f(x^{(k)})\|_2^2$$!), kết hợp với kiểm tra mức thay đổi tương đối của $$f$$ hoặc $$x$$.
- **Ưu & Nhược điểm cốt lõi của GD:** Mỗi bước cực rẻ (chỉ $$O(np)$$, không cần lập hay nghịch đảo ma trận Hessian $$O(p^3)$$ như Newton), rất dễ cài đặt, nhưng cực nhạy cảm với chỉ số điều kiện $$\kappa = (\sigma_{\max}/\sigma_{\min})^2$$!

### Khung giải thích (nên đọc chậm): Tính $$L, m, \kappa$$ và chứng nhận độ chính xác dừng qua $$\|\nabla f\|_2$$

Cho ma trận dữ liệu 2 mẫu, 2 đặc trưng $$X = \begin{pmatrix} 2 & 0 \\ 0 & 0.5 \end{pmatrix}$$ và bài toán $$f(\beta) = \frac{1}{2}\|y - X\beta\|_2^2$$:

1. **Tính $$L$$, $$m$$ và $$\kappa$$ không có điều chuẩn:**
   - $$X^T X = \begin{pmatrix} 4 & 0 \\ 0 & 0.25 \end{pmatrix} \implies L = 4,\; m = 0.25$$.
   - Chỉ số điều kiện: $$\kappa = \frac{4}{0.25} = 16$$.
2. **Xem hiệu ứng khi thêm điều chuẩn Ridge $$\frac{1}{2}\lambda\|\beta\|_2^2$$ với $$\lambda = 0.75$$:**
   - Hessian mới: $$X^T X + 0.75 I = \operatorname{diag}(4.75,\; 1.0)$$.
   - $$L_{\text{new}} = 4.75,\; m_{\text{new}} = 1.0 \implies \kappa_{\text{new}} = 4.75$$ (giảm hơn **3.3 lần**!).
3. **Dùng tiêu chí dừng $$\|\nabla f(\beta^{(k)})\|_2 \le 0.02$$ để chứng nhận sai số hàm mục tiêu:**
   Nhờ bất đẳng thức PL với $$m_{\text{new}} = 1.0$$:
   $$f(\beta^{(k)}) - f^\star \le \frac{1}{2 m_{\text{new}}} \|\nabla f(\beta^{(k)})\|_2^2 \le \frac{1}{2(1.0)} (0.02)^2 = 0.0002.$$
   Dù không hề biết $$f^\star$$ bằng bao nhiêu, chỉ cần nhìn norm gradient xuống dưới $$0.02$$ là ta có **chứng chỉ toán học** rằng mình đang cách đáy toàn cục không quá $$0.0002$$!

---

## Điều kiện Liên tục Lipschitz & Tính Lồi mạnh

Xét bài toán hồi quy bình phương tối thiểu $$f(\beta) = \frac{1}{2} \lVert y - X\beta \rVert_2^2$$ để minh họa các điều kiện liên tục Lipschitz và tính lồi mạnh.

### Tính liên tục Lipschitz của $$\nabla f$$:
* Điều kiện này tương đương với $$\nabla^2 f(x) \preceq LI$$.<br>
* Vì $$\nabla^2 f(\beta) = X^TX$$, ta có $$L = \sigma^2_{\max}(X)$$.<br>

### Tính lồi mạnh của $$f$$:
* Điều kiện này tương đương với $$\nabla^2 f(x) \succeq mI$$.<br>
* Vì $$\nabla^2 f(\beta) = X^TX$$, ta có $$m = \sigma_{\min}^2(X)$$.<br>
* Nếu $$X$$ có kích thước $$n \times p$$ với $$p > n$$, thì $$\sigma_{\min}(X) = 0$$, nên $$f$$ không thể lồi mạnh.<br>
* Ngay cả khi $$\sigma_{\min}(X) > 0$$, chỉ số điều kiện $$L/m = \sigma_{\max}^2(X)/\sigma_{\min}^2(X)$$ vẫn có thể rất lớn.

Khi $$f$$ vừa lồi mạnh vừa có gradient liên tục Lipschitz, hàm số thỏa mãn điều kiện kẹp sau (tức đồ thị của $$f$$ nằm giữa hai hàm bậc hai):

>$$mI \preceq \nabla^2 f(x) \preceq LI \quad \text{với mọi } x \in \mathbb{R}^n \text{ và } L > m > 0$$

Việc đòi hỏi cả hai điều kiện đúng với mọi $$x \in \mathbb{R}^n$$ khá chặt. Tuy nhiên, trên thực tế các điều kiện này chỉ cần thỏa mãn trên tập mức dưới (sublevel set):

> $$S = \{x : f(x) \leq f(x^{(0)})\}$$

## Tính Thực tiễn

### Tiêu chí Dừng cho Thuật toán Tối ưu hóa

Trong thực tế, thuật toán tối ưu cần các tiêu chí dừng rõ ràng để quyết định thời điểm kết thúc quá trình lặp. Dưới đây là những điều kiện dừng thường dùng nhất:

#### 1. **Độ lớn Gradient gần bằng không:**
Đây là tiêu chí dừng tự nhiên cho bài toán tối ưu không ràng buộc, dựa trên điều kiện tối ưu bậc nhất $$\nabla f(x^{\star}) = 0$$ tại điểm cực trị:
$$
\|\nabla f(\mathbf{x}_k)\| \leq \epsilon_1
$$
trong đó $$\mathbf{x}_k$$ là điểm tại lần lặp $$k$$ và $$\epsilon_1 > 0$$ là ngưỡng sai số nhỏ.

Nếu $$f$$ lồi mạnh với hằng số $$m > 0$$, ta có đảm bảo trực tiếp về sai số giá trị hàm:
> $$\lVert \nabla f(x) \rVert_2 \leq \sqrt{2m \epsilon} \Rightarrow f(x) - f^{\star} \leq \epsilon$$

#### 2. **Thay đổi nhỏ ở giá trị hàm mục tiêu:**
Dừng thuật toán khi giá trị hàm mục tiêu không còn thay đổi đáng kể giữa hai lần lặp liên tiếp:
$$
|f(\mathbf{x}_{k+1}) - f(\mathbf{x}_k)| \leq \epsilon_2
$$
trong đó $$\epsilon_2 > 0$$ là một ngưỡng nhỏ.

#### 3. **Thay đổi nhỏ ở biến tối ưu:**
Dừng thuật toán khi các tham số không còn dịch chuyển đáng kể giữa các lần lặp:
$$
\|\mathbf{x}_{k+1} - \mathbf{x}_k\| \leq \epsilon_3
$$
trong đó $$\epsilon_3 > 0$$ là một ngưỡng nhỏ.

#### 4. **Số lần lặp tối đa:**
Đặt giới hạn trên cho tổng số vòng lặp để tránh vòng lặp vô hạn hoặc chạy quá lâu:
$$
k \geq \text{MaxIterations}
$$
Đây là điều kiện dừng an toàn, đảm bảo thuật toán kết thúc trong thời gian hữu hạn ngay cả khi chưa đạt độ chính xác mong muốn.

#### 5. **Thời gian chạy tối đa:**
Tương tự giới hạn số lần lặp, thuật toán sẽ dừng nếu vượt quá ngân sách thời gian cho phép:
$$
\text{ElapsedTime} \geq \text{MaxTime}
$$

#### 6. **Điều kiện dừng kết hợp:**
Trong thực tế, nhiều tiêu chí dừng thường được kết hợp với nhau (ví dụ: dừng ngay khi *một trong các* điều kiện trên được thỏa mãn) nhằm cân bằng giữa độ chính xác và chi phí tính toán.

### [Tham khảo] Chứng minh Điều kiện Dừng dưới Tính Lồi mạnh

Cách suy ra tiêu chí dừng theo chuẩn gradient ở mục 1 như sau.

Vì $$f$$ lồi mạnh với hằng số $$m > 0$$, ma trận Hessian thỏa mãn:
> $$ \begin{align}
\nabla^2 f(x) \succeq mI
\end{align} $$

Từ định nghĩa tính lồi mạnh (hay khai triển Taylor bậc hai với $$\nabla^2 f(\xi) \succeq mI$$), ta có cận dưới bậc hai:
> $$ \begin{align}
f(y) & \ge f(x) + \nabla f(x)^T(y-x) + \frac{m}{2} \lVert y-x \rVert_2^2, \quad \forall x, y
\end{align} $$

Lấy đạo hàm vế phải theo $$y$$ và đặt bằng 0, ta thu được điểm cực tiểu của cận dưới bậc hai là $$\tilde{y} = x - (1/m) \nabla f(x)$$. Thay $$\tilde{y}$$ vào vế phải của bất đẳng thức trên:

> $$ \begin{align}
f(y) & \ge f(x) + \nabla f(x)^T(\tilde{y}-x) + \frac{m}{2} \lVert \tilde{y}-x \rVert_2^2 \\
& = f(x) - \frac{1}{2m} \lVert \nabla f(x) \rVert_2^2
\end{align} $$

Lấy cực tiểu theo $$y$$ ở vế trái (thay $$f(y)$$ bằng $$f^{*}$$), ta được:
> $$ \begin{align}
f^{*} \ge f(x) - \frac{1}{2m} \lVert \nabla f(x) \rVert_2^2
\end{align} $$

Từ đó suy ra tiêu chí dừng:

> $$ \begin{align}
f(x) - f^{*} \le \frac{1}{2m} \lVert \nabla f(x) \rVert^2_2 & \le \epsilon \\
\lVert \nabla f(x) \rVert^2_2 & \le 2m\epsilon \\
\lVert \nabla f(x) \rVert_2 & \le \sqrt{2m\epsilon}
\end{align} $$

### Ưu điểm và Nhược điểm của Gradient Descent

### Ưu điểm
* Thuật toán đơn giản, dễ cài đặt và chi phí tính toán trên mỗi vòng lặp thấp.
* Hội tụ nhanh đối với các bài toán lồi mạnh và có chỉ số điều kiện tốt.

### Nhược điểm
* Hội tụ chậm trong trường hợp tổng quát vì nhiều bài toán thực tế không lồi mạnh hoặc có chỉ số điều kiện xấu.
* Không áp dụng trực tiếp được cho các hàm mục tiêu không khả vi.