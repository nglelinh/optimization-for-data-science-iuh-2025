---
layout: post
title: 13-04-01 Ví dụ đối ngẫu lasso
chapter: '13'
order: 6
owner: Wontak Ryu
categories:
- chapter13
lang: vi
---

Nếu bạn áp dụng máy móc công thức hàm Lagrange cho bài toán Lasso $$\min_\beta \frac{1}{2}\|y - X\beta\|_2^2 + \lambda \|\beta\|_1$$, bạn sẽ lập tức gặp một bất ngờ dở khóc dở cười: vì bài toán gốc **không có ràng buộc nào cả**, hàm đối ngẫu chỉ là một hằng số bằng đúng $$f^\star$$ — hoàn toàn vô dụng!

Bí quyết của các chuyên gia tối ưu nằm ở một bước "tách biến nghệ thuật": đặt biến phụ $$z = X\beta$$ để tách rời phần bình phương sai số khỏi phần phạt $$\ell_1$$. Chỉ cần một phương trình ràng buộc nhân tạo đó thôi, bài toán đối ngẫu của Lasso lập tức hiện ra với vẻ đẹp hình học kinh ngạc: **tìm hình chiếu Euclid của vectơ dữ liệu $$y$$ lên một khối đa diện lồi $$\{u : \|X^T u\|_\infty \le \lambda\}$$**. Từ đây, ta không chỉ hiểu sâu cấu trúc hình học của Lasso mà còn mở ra các kỹ thuật sàng lọc biến (safe screening) loại bỏ hàng nghìn đặc trưng thừa ngay trước khi giải.

## Bản đồ kiến thức nền: Từ Lasso nguyên thủy sang bài toán chiếu hình học đối ngẫu

- **Kỹ thuật đưa biến phụ (Variable Splitting):** Khi bài toán không ràng buộc gồm tổng hai hàm có cấu trúc khác nhau, đặt $$z = X\beta$$ tạo ra ràng buộc đẳng thức để tách phép lấy cực tiểu thành hai bài toán con dễ giải đóng.
- **Liên hợp của hàm bình phương và chuẩn $$\ell_1$$:** Phần $$\frac{1}{2}\|y - z\|_2^2$$ sinh ra dạng bậc hai $$\frac{1}{2}\|y - u\|_2^2$$ trên biến đối ngẫu $$u$$, còn phần $$\lambda \|\beta\|_1$$ biến thành điều kiện ràng buộc hộp $$\|X^T u\|_\infty \le \lambda$$ (chính là quả cầu chuẩn đối ngẫu $$\ell_\infty$$!).
- **Quan hệ nguyên thủy – đối ngẫu (KKT):** Tại nghiệm tối ưu, phần dư $$r^\star = y - X\beta^\star$$ trùng đúng với nghiệm đối ngẫu $$u^\star$$ (hoặc tỷ lệ trực tiếp tùy quy ước dấu), cho thấy mọi đặc trưng không được chọn ($$\beta_j^\star = 0$$) đều có tương quan chặt $$\vert X_j^T u^\star \vert < \lambda$$.

### Khung giải thích (nên đọc chậm): Tính tay đối ngẫu Lasso trên một ví dụ 2 đặc trưng

Xét bài toán Lasso với $$n = 2, p = 2$$, ma trận thiết kế đơn giản $$X = I_2$$ (hai cột trực chuẩn), dữ liệu $$y = (3, 0.5)^T$$ và tham số phạt $$\lambda = 1$$:

$$\min_{\beta \in \mathbb{R}^2} \frac{1}{2}\bigl((3 - \beta_1)^2 + (0.5 - \beta_2)^2\bigr) + (\vert \beta_1 \vert + \vert \beta_2 \vert).$$

1. **Giải bài toán đối ngẫu (chiếu $$y$$ lên khối hộp $$\|X^T u\|_\infty \le 1$$):**
   Vì $$X = I_2$$, bài toán đối ngẫu tương đương với:
   $$\min_{u \in \mathbb{R}^2} \frac{1}{2}\|y - u\|_2^2 \qquad \text{với } \vert u_1 \vert \le 1, \;\; \vert u_2 \vert \le 1.$$
   Chiếu từng tọa độ của $$y = (3, 0.5)^T$$ lên đoạn $$[-1, 1]$$ ta nhận ngay:
   $$u_1^\star = \operatorname{clip}(3, -1, 1) = 1, \qquad u_2^\star = \operatorname{clip}(0.5, -1, 1) = 0.5.$$
2. **Khôi phục nghiệm nguyên thủy Lasso từ $$u^\star$$:**
   Từ điều kiện $$X\beta^\star = y - u^\star$$ (khi $$X = I_2$$), ta có ngay nghiệm thưa:
   $$\beta_1^\star = 3 - 1 = 2, \qquad \beta_2^\star = 0.5 - 0.5 = 0.$$
   (Khớp hoàn toàn với công thức ngưỡng mềm *soft-thresholding*!)
3. **Kiểm tra đối ngẫu mạnh:**
   - Giá trị nguyên thủy: $$f(\beta^\star) = \frac{1}{2}\bigl((3-2)^2 + (0.5-0)^2\bigr) + (\vert 2\vert + 0) = \frac{1}{2}(1 + 0.25) + 2 = 2.625$$.
   - Giá trị đối ngẫu: $$\frac{1}{2}\|y\|_2^2 - \frac{1}{2}\|y - u^\star\|_2^2 = \frac{1}{2}(9.25) - \frac{1}{2}(4 + 0) = 4.625 - 2 = 2.625$$.
   Khoảng cách đối ngẫu bằng đúng $$0$$!

---

Xét bài toán lasso với $$y \in \mathbb{R}^n$$ và $$X \in \mathbb{R}^{n\times p}$$:

> $$ \min_\beta \frac{1}{2} \| y-X\beta \|^2_2 + \lambda\| \beta \|_1$$
> 
> $$f(\beta) = \frac{1}{2} \| y - X\beta \|^2_2 +  \lambda\| \beta \|_1$$
> 
> $$L(\beta) = f(\beta)$$
> 
> $$ \min_\beta L(\beta) = f^{\star}$$

Vì bài toán gốc không có ràng buộc nên hàm đối ngẫu chỉ là hằng số bằng $$f^{\star}$$. Để xây dựng bài toán đối ngẫu hữu ích hơn, ta đưa thêm biến phụ $$z = X\beta$$ và viết lại bài toán nguyên thủy tương đương:

> $$ \min_{\beta,z} \frac{1}{2} \| y-z \|^2_2 + \lambda \| \beta \|_1 \text{ với điều kiện } z = X\beta$$

Hàm đối ngẫu Lagrange của bài toán đã biến đổi là:

> $$\begin{align}
> g(u) &= \min_{\beta,z} \frac{1}{2} \| y-z \|^2_2 + \lambda \| \beta \|_1 + u^T(z-X\beta) \\
> &= \frac{1}{2} \| y \|^2_2 - \frac{1}{2} \| y-u \|^2_2 - I_{\{ v : \| v \|_\infty \leq 1 \}}(X^Tu/\lambda) \\
> \end{align}$$

#### Chứng minh
> $$\begin{align}
> g(u) &= \min_{\beta,z} \frac{1}{2} \| y-z \|^2_2 + \lambda \| \beta \|_1 + u^T(z-X\beta) \\
> &= \underbrace{ \left( \min_z \frac{1}{2} \| y - z \|^2_2 + u^Tz \right)}_{(1)} + \underbrace{\left( \min_\beta \left(\lambda \| \beta \|_1 - u^TX\beta\right) \right)}_{(2)} \\
> \end{align}$$
> 
> Ở phần (1), lấy đạo hàm theo $$z$$ bằng $$0$$ cho $$z^{\star} = y - u$$, nên:
> 
> $$\begin{align}
> (1) \cdots \left( \min_z \frac{1}{2} \| y - z \|^2_2 + u^Tz \right)
> &= \frac{1}{2} \| u \|^2_2 + u^T(y - u) \\
> &= -\frac{1}{2} \| y - u \|^2_2 + \frac{1}{2} \| y \|^2_2 \\
> \end{align}$$
> 
> Ở phần (2), dùng hàm liên hợp của chuẩn $$\ell_1$$:
> 
> $$\begin{align}
> (2) \cdots \left( \min_\beta \left(\lambda \| \beta \|_1 - u^TX\beta\right) \right) 
> &= - \lambda \max_\beta \left( \left(\frac{X^Tu}{\lambda}\right)^T \beta - \| \beta \|_1 \right) \\
> &= - I_{\{ v : \| v \|_\infty \leq 1 \}}(X^Tu/\lambda) \\
> &= - I_{\{ w : \| w \|_\infty \leq \lambda \}}(X^Tu) \\
> \end{align}$$
> 
> Suy ra:
> 
> $$g(u) = \frac{1}{2} \| y \|^2_2 - \frac{1}{2} \| y-u \|^2_2 - I_{\{ v : \| v \|_\infty \leq 1 \}}(X^Tu/\lambda)$$

Do đó, bài toán đối ngẫu của lasso là:

> $$ \max_u \frac{1}{2} ( \| y \|^2_2 - \| y-u \|^2_2 ) \text{ với điều kiện } \| X^Tu \|_\infty \leq \lambda$$

Bỏ hằng số $$\frac{1}{2}\|y\|_2^2$$ và đổi dấu, bài toán đối ngẫu tương đương với bài toán chiếu Euclidean lên đa diện:

> $$ \min_u \| y-u \|^2_2 \text{ với điều kiện } \| X^Tu \|_\infty \leq \lambda$$

### Kiểm tra tính đối ngẫu mạnh

Bài toán nguyên thủy là bài toán lồi chỉ có ràng buộc đẳng thức tuyến tính nên thỏa mãn điều kiện Slater; do đó tính đối ngẫu mạnh được đảm bảo:

> $$ \text{Đối ngẫu mạnh } \implies (\beta^{\star}, z^{\star}) \text{ phải cực tiểu hóa } L( \beta, z, u^{\star} ) \text{ theo } \beta, z$$

### Lưu ý

Giá trị tối ưu của bài toán rút gọn $$\min_u \|y - u\|_2^2$$ không bằng giá trị mục tiêu tối ưu của bài toán lasso gốc (vì đã bỏ hằng số và hệ số $$\frac{1}{2}$$). Tuy nhiên, nghiệm đối ngẫu $$u^{\star}$$ và nghiệm lasso $$\beta^{\star}$$ liên hệ trực tiếp qua đẳng thức $$X\beta^{\star} = y - u^{\star}$$.

Hệ thức này suy ra từ điều kiện dừng KKT theo $$z$$ là $$z - y + u = 0$$ kết hợp với ràng buộc $$z = X\beta$$. Do đó, nghiệm đối ngẫu $$u^{\star}$$ chính là phần dư $$y - X\beta^{\star}$$ của bài toán lasso.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter13/Conjugate_LassoDual_Example.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig2] Đối ngẫu của bài toán Lasso [1]</figcaption>
</p>
</figure>

### Đối ngẫu của lasso nhìn như một phép chiếu (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/lasso-dual_vi.mp4"></video>
</div>

Bài toán đối ngẫu tìm $$u$$ thỏa $$\|A^Tu\|_\infty\le\lambda$$. Các tọa độ mà ràng buộc này chạm biên (đạt dấu bằng) tương ứng với các thành phần có thể khác $$0$$ của nghiệm bài toán gốc.

### Tự tay thử: lasso gốc và đối ngẫu

<div class="opx-explainer" data-opx="ld" data-lang="vi"></div>
