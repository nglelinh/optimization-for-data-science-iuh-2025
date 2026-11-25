---
layout: post
title: 18-07 BFGS Bộ nhớ Hạn chế (LBFGS)
chapter: '18'
order: '8'
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

Khi số biến $$n$$ vượt ngưỡng vài chục nghìn hay vài triệu (như trong hồi quy logistic nhiều đặc trưng, mạng nơ-ron vật lý PINN hay tái tạo ảnh y tế), ngay cả việc lưu trữ một ma trận $$H_k$$ dày đặc kích thước $$n \times n$$ cũng trở nên bất khả thi vì tràn bộ nhớ RAM. **L-BFGS** (Nocedal, 1980) giải quyết triệt để nút thắt này bằng một nhận xét xuất sắc: ta **không bao giờ cần tạo ra ma trận $$H_k$$ tường minh** — ta chỉ cần lưu đúng $$m$$ cặp vector gần nhất $$(s_i, y_i)$$ (thường $$m = 5\text{–}20$$) rồi chạy một **vòng lặp hai chiều (two-loop recursion)** để tính thẳng tích $$H_k \nabla f(x_k)$$ chỉ trong $$O(mn)$$ phép toán!

## Kiến thức cần nhớ: Bốn trụ cột của L-BFGS và thuật toán hai vòng lặp

Để hiểu rõ cách L-BFGS giữ lại gần như trọn vẹn sức mạnh của BFGS với bộ nhớ tí hon, hãy nắm vững bốn ý tưởng sau:

- **Quên có chọn lọc (Sliding Window of Curvature Pairs):** Chỉ giữ lại $$m$$ cặp $$(s_i, y_i)$$ gần nhất và loại bỏ các cặp cũ. Điều này không chỉ giảm bộ nhớ từ $$O(n^2)$$ xuống $$O(mn)$$ mà còn giúp loại bỏ thông tin độ cong đã lỗi thời ở xa điểm lặp hiện tại.
- **Khởi tạo tỉ lệ động $$H_k^0 = \gamma_k I$$:** Ở mỗi vòng lặp, thay vì bắt đầu từ ma trận đơn vị $$I$$, L-BFGS chọn hệ số tỉ lệ $$\gamma_k = \frac{s_{k-1}^T y_{k-1}}{y_{k-1}^T y_{k-1}}$$ phản ánh quy mô độ cong cục bộ gần nhất, giúp bước đơn vị $$t = 1$$ được chấp nhận gần như ngay lập tức.
- **Thuật toán đệ quy hai vòng lặp (Two-Loop Recursion):** Khai triển đệ quy công thức BFGS hai bên $$H^+ = V^T H V + \rho s s^T$$ cho phép tính trực tiếp vector $$r = H_k q$$ qua một vòng lặp đi lùi (từ mới nhất về cũ nhất) và một vòng lặp đi tới (từ cũ nhất lên mới nhất), chỉ dùng tích vô hướng và cộng vector!
- **Hội tụ tuyến tính mạnh (Strong Linear Convergence):** Dù không đạt hội tụ siêu tuyến tính như BFGS đầy đủ (vì bộ nhớ hữu hạn $$m$$ không tích lũy đủ toàn bộ phổ độ cong khi $$n \gg m$$), L-BFGS vẫn hội tụ nhanh vượt trội so với hạ gradient và là thuật toán bậc nhất–giả bậc hai tin cậy bậc nhất cho tối ưu quy mô lớn.

### Giải thích: Chạy tay thuật toán Two-Loop Recursion với $$m = 1$$ và kiểm chứng khớp tuyệt đối

Giả sử ta chỉ lưu $$m = 1$$ cặp lịch sử $$s_0 = (1, 0)^T, y_0 = (2, 1)^T$$ ($$\rho_0 = \frac{1}{y_0^T s_0} = \frac{1}{2} = 0.5$$), và cần tính tích $$r = H_1 q$$ tại vector gradient hiện tại $$q = (4, 2)^T$$:

1. **Vòng lặp 1 (đi lùi — cập nhật $$q$$):**
   - Tính $$\alpha_0 = \rho_0 (s_0^T q) = 0.5 \times [(1)(4) + (0)(2)] = 2.0$$.
   - Cập nhật $$q \leftarrow q - \alpha_0 y_0 = \begin{bmatrix} 4 \\ 2 \end{bmatrix} - 2.0\begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$.
2. **Bước tỉ lệ khởi tạo $$r = H_1^0 q = \gamma_1 q$$:**
   - Hệ số tỉ lệ $$\gamma_1 = \frac{s_0^T y_0}{y_0^T y_0} = \frac{2}{2^2 + 1^2} = 0.4$$.
   - Nhân tỉ lệ: $$r = 0.4 \times (0, 0)^T = (0, 0)^T$$.
3. **Vòng lặp 2 (đi tới — khôi phục $$r$$):**
   - Tính $$\beta_0 = \rho_0 (y_0^T r) = 0.5 \times 0 = 0$$.
   - Cập nhật $$r \leftarrow r + (\alpha_0 - \beta_0) s_0 = \begin{bmatrix} 0 \\ 0 \end{bmatrix} + (2.0 - 0)\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \end{bmatrix}$$.
4. **Kiểm chứng độc lập không cần thuật toán hai vòng lặp:** Để ý rằng $$q = (4, 2)^T = 2 y_0$$! Vì mọi ma trận BFGS $$H_1$$ đều phải thỏa mãn phương trình secant $$H_1 y_0 = s_0$$, ta chắc chắn phải có $$H_1 q = 2 H_1 y_0 = 2 s_0 = (2, 0)^T$$ — trùng khớp hoàn toàn với kết quả two-loop recursion mà không hề phải lập ma trận $$H_1$$!

---

# Giới thiệu

L-BFGS (Limited-memory BFGS) là đại diện tiêu biểu của lớp phương pháp Quasi-Newton bộ nhớ hạn chế, đặc biệt hữu ích khi chi phí tính toán hoặc lưu trữ ma trận Hessian dày đặc kích thước $$n \times n$$ quá lớn. Thay vì lưu toàn bộ ma trận $$n \times n$$, L-BFGS chỉ lưu một số ít vector $$n$$-chiều để biểu diễn ngầm xấp xỉ nghịch đảo Hessian.

Như tên gọi, L-BFGS được xây dựng trực tiếp từ BFGS. Ý tưởng cốt lõi là chỉ sử dụng thông tin độ cong từ $$m$$ vòng lặp gần nhất để xấp xỉ Hessian nghịch đảo, đồng thời loại bỏ thông tin từ các vòng lặp quá cũ — vừa tiết kiệm bộ nhớ, vừa tránh dùng thông tin độ cong đã không còn phản ánh đúng tính chất cục bộ tại điểm lặp hiện tại.

Ngoài ra, phiên bản bộ nhớ hạn chế của các thuật toán Quasi-Newton khác (chẳng hạn SR1) cũng có thể được xây dựng theo cùng nguyên lý [14].

# L-BFGS

Để hiểu L-BFGS, trước hết nhắc lại phép cập nhật của BFGS ở mỗi vòng lặp:

>$$
>x^+ = x - t H \nabla f, \\\\
>\text{trong đó } t \text{ là độ dài bước và } H \text{ được cập nhật theo công thức:}\\\\
>\text{ }\\\\
>H^+ = \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big) + \frac{ss^T}{y^Ts}. \\\\
>$$

Với cấu trúc trên, tích ma trận–vector $$H^+q$$ (với $$q \in \mathbb{R}^n$$) có thể được tính chỉ bằng các phép tích vô hướng tạo thành các đại lượng vô hướng $$\alpha, \beta \in \mathbb{R}$$ và các phép cộng vector theo $$p, s \in \mathbb{R}^n$$:

>$$
>\begin{align}
>H^+q &= \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big)q + \frac{ss^Tq}{y^Ts}\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) \underbrace{H \big( q - \frac{s^T q}{y^Ts} y \big)}_{p} + \underbrace{\frac{s^Tq}{y^Ts}}_{\alpha} s\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) p + \alpha s\\\\
> &= p - \underbrace{\frac{y^Tp}{y^Ts}}_{\beta}s + \alpha s \\\\
> &= p + (\alpha - \beta) s, \\\\
>& \text{trong đó } \alpha = \frac{s^Tq}{y^Ts}, \ q^+ = q - \alpha y, \ p = Hq^+, \ \beta = \frac{y^Tp}{y^Ts}.
>\end{align} \\\\
>$$

Nếu $$H$$ được hình thành sau $$k$$ bước cập nhật BFGS, thì hướng bước $$-H\nabla f(x)$$ có thể được tính trực tiếp với độ phức tạp $$O(kn)$$ mà không cần tạo tường minh ma trận $$H$$ (xem thuật toán đệ quy hai vòng bên dưới). Để tiết kiệm bộ nhớ khi $$k$$ lớn, L-BFGS chỉ giữ lại thông tin độ cong từ $$m$$ vòng lặp gần nhất (với $$k \ge m$$), đưa chi phí mỗi bước xuống $$O(mn)$$.

# Thuật toán

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter18/algorithm_quasi-newton.png" alt="[Fig1] Thuật toán LBFGS [3]" width="90%">
  <figcaption style="text-align: center;">[Fig1] Thuật toán LBFGS [3]</figcaption>
</p>
</figure>

Ma trận xấp xỉ nghịch đảo Hessian $$H_k$$ nhìn chung là ma trận dày đặc nên phép nhân ma trận trực tiếp rất tốn kém khi số biến lớn. L-BFGS tính trực tiếp tích $$H_k \nabla f_k$$ thông qua chuỗi các tích vô hướng và phép cộng vector, khắc phục hoàn toàn nút thắt bộ nhớ và tính toán của $$H_k$$.

Trong thực hành, xấp xỉ khởi đầu $$H^{0, k}$$ ở mỗi vòng lặp thường được chọn là bội số của ma trận đơn vị $$H^{0, k} = \gamma_k I$$ — lựa chọn đơn giản nhưng đã được chứng minh rất hiệu quả ([14] mục 7.2):

>$$
H^{0, k} = \gamma_k I, \\\\
>\text{trong đó } \: \gamma_k = \frac{s^T_{k-1}y_{k-1}}{y^T_{k-1}y_{k-1}}.
>$$

* **Lưu ý:** Hệ số co giãn $$\gamma_k$$ (và do đó $$H^{0, k}$$) được cập nhật lại ở mỗi vòng lặp.

### L-BFGS trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/l-bfgs_vi.mp4"></video>
</div>

Vì sao BFGS tốn n² bộ nhớ, m cặp (s, y) và H₀ = γI, làm tay đệ quy hai vòng trong 2 chiều, rồi so sánh số bước trên hồi quy logistic.
