---
layout: post
title: '21-03 Ví dụ: Hồi quy Lasso và hồi quy group lasso'
chapter: '21'
order: 4
owner: Hooncheol Shin
categories:
- chapter21
lang: vi
---

Trong thống kê hiện đại, **Lasso** chọn từng đặc trưng đơn lẻ bằng phạt $$\ell_1$$, còn **Group Lasso** (Yuan & Lin, 2006) chọn hoặc loại bỏ **cả một nhóm đặc trưng cùng lúc** (ví dụ toàn bộ các biến giả one-hot của một biến phân loại, hay cả một cụm gen cùng chức năng) bằng phạt tổng chuẩn Euclid $$\sum_{g} \sqrt{p_g}\|\beta_g\|_2$$. Điều tuyệt vời khi giải cả hai bài toán này bằng ADMM là: **bước giải hệ tuyến tính cho $$\beta$$ giống hệt nhau**, ta chỉ cần đổi đúng một dòng ở bước cập nhật $$\alpha$$ — từ ngưỡng mềm từng phần tử (elementwise soft-thresholding) sang **ngưỡng mềm theo khối (block soft-thresholding)**!

## Bản đồ kiến thức nền: Bốn trụ cột của ADMM cho Lasso và Group Lasso

Để áp dụng linh hoạt ADMM cho các biến thể hồi quy có điều chuẩn thưa, hãy nắm chắc bốn điểm sau:

- **Tách biến $$\beta = \alpha$$ để cô lập cấu trúc không trơn:** Toàn bộ dữ liệu $$(X, y)$$ nằm gọn trong bước $$\beta$$ (một bài toán bình phương tối thiểu có điều chuẩn Ridge $$\frac{\rho}{2}\|\beta - (\alpha - w)\|_2^2$$ luôn khả nghịch), còn toàn bộ cấu trúc thưa nằm gọn trong bước $$\alpha$$.
- **Định lý đảo ma trận Woodbury khi $$n \ll p$$:** Nếu số đặc trưng $$p$$ lớn hơn nhiều so với số mẫu $$n$$, thay vì phân tích Cholesky ma trận $$p \times p$$ là $$X^T X + \rho I$$, ta dùng công thức Woodbury chỉ cần phân tích Cholesky ma trận nhỏ $$n \times n$$ là $$I_n + \frac{1}{\rho} X X^T$$!
- **Toán tử ngưỡng mềm theo khối cho Group Lasso:** Với mỗi nhóm biến $$g$$, $$\operatorname{prox}_{\tau\|\cdot\|_2}(v_g) = \left(1 - \frac{\tau}{\|v_g\|_2}\right)_+ v_g$$. Nếu chuẩn nhóm $$\|v_g\|_2 \le \tau$$, toàn bộ vector $$\alpha_g$$ bị ép về $$0$$ đồng thời; ngược lại, nó bị co tỉ lệ mà vẫn giữ nguyên hướng!
- **Tối ưu hóa tốc độ nhờ tái sử dụng phân tích Cholesky:** Giữ nguyên $$\rho$$ (hoặc chỉ đổi $$\rho$$ vài lần đầu) giúp chi phí mỗi vòng lặp sau đó chỉ còn $$O(p^2)$$ (hoặc $$O(np)$$ khi $$n \ll p$$).

### Khung giải thích (nên đọc chậm): So sánh trực tiếp ngưỡng mềm Lasso và ngưỡng mềm khối Group Lasso trên cùng vector

Giả sử trong một bước cập nhật $$\alpha^{(k)}$$ của ADMM, ta nhận được vector đầu vào $$v = \beta^{(k)} + w^{(k-1)} = (3, \; 4)^T$$ (thuộc cùng một nhóm $$g$$ kích thước 2) với ngưỡng hiệu dụng $$\tau = \lambda / \rho = 2$$:

1. **Nếu dùng Lasso (phạt $$\lambda(|v_1| + |v_2|)$$ — xử lý độc lập từng tọa độ):**
   - $$\alpha_1 = S_2(3) = \max(3 - 2, 0) = 1.0$$.
   - $$\alpha_2 = S_2(4) = \max(4 - 2, 0) = 2.0$$.
   - Kết quả: $$\alpha_{\text{Lasso}} = (1.0, \; 2.0)^T$$. Nếu tăng ngưỡng lên $$\tau = 3.5$$, tọa độ 1 bị triệt tiêu ($$0$$) nhưng tọa độ 2 vẫn sống sót ($$0.5$$).
2. **Nếu dùng Group Lasso (phạt $$\lambda\|v\|_2$$ — xử lý cả nhóm):**
   - Tính chuẩn Euclid của cả nhóm: $$\|v\|_2 = \sqrt{3^2 + 4^2} = 5$$.
   - Hệ số co chung: $$\left(1 - \frac{\tau}{\|v\|_2}\right)_+ = \left(1 - \frac{2}{5}\right)_+ = 0.6$$.
   - Kết quả: $$\alpha_{\text{Group}} = 0.6 \times (3, \; 4)^T = (1.8, \; 2.4)^T$$ (giữ nguyên tỉ lệ $$3:4$$ giữa hai biến trong nhóm!).
   - Nếu tăng ngưỡng lên $$\tau = 5.5 > \|v\|_2 = 5$$, hệ số co bằng $$0$$ và **toàn bộ nhóm** bị loại về $$(0, 0)^T$$ cùng một lúc!

---

## Hồi quy Lasso

Hãy xét cách giải bài toán hồi quy Lasso bằng ADMM.

Cho $$y\in \mathbb{R}^{n}$$ và $$X\in \mathbb{R}^{n\times p}$$, bài toán Lasso được phát biểu là:
>$$
>\begin{align}
>\min_{\beta}\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda||\beta||_{1}
>\end{align}
>$$

Ở các chương trước, chúng ta đã giải bài toán này bằng nhiều phương pháp khác nhau, bao gồm [proximal gradient descent (ISTA)]({% multilang_post_url contents/chapter09/20-01-08-09_01_proximal_gradient_descent %}), [accelerated proximal gradient descent (FISTA)]({% multilang_post_url contents/chapter09/20-01-08-09_05_03_example_FISTA %}), [phương pháp rào (barrier method)]({% multilang_post_url contents/chapter15/21-03-28-15_barrier_method %}) và [phương pháp điểm trong gốc–đối ngẫu]({% multilang_post_url contents/chapter17/21-05-01-17_primal_dual_interior_point_method %}).

Tương tự như khi xây dựng bài toán đối ngẫu, hiệu năng của ADMM phụ thuộc đáng kể vào cách chọn biến phụ. Trong các cách tách biến có thể dùng, dạng sau thường mang lại hiệu quả tính toán tốt nhất:
>$$
>\begin{align}
>&\min_{\beta, \alpha} &&\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda||\alpha||_{1}\\\\
>&\text{subject to} &&\beta-\alpha= 0.
>\end{align}
>$$

## Các bước cập nhật ADMM

Với cách tách biến trên, bước cập nhật $$\beta$$ là bài toán cực tiểu hóa hàm bậc hai trơn nên có thể giải trực tiếp bằng điều kiện đạo hàm bằng không. Bước cập nhật $$\alpha$$ tương tự bài toán ở [Chương 7 (07-03-04)]({% multilang_post_url contents/chapter07/21-03-25-07_03_04_example_soft-thresholding %}), cho nghiệm đóng dưới dạng toán tử co ngưỡng mềm (soft-thresholding):
>$$
>\begin{align}
>\beta^{+} &= \underset{\beta}{\operatorname{argmin}}\frac{1}{2}||y-X\beta||^{2}_{2}+\frac{\rho}{2}||\beta-\alpha+w||^{2}_{2}\\\\
>&= (X^{T}X+\rho I)^{-1}(X^{T}y+\rho (\alpha-w))\\\\
>\alpha^{+} &= \underset{\alpha}{\operatorname{argmin}}\lambda||\alpha||_{1}+\frac{\rho}{2}||\beta^{+}-\alpha+w||^{2}_{2}\\\\
>&= S_{\frac{\lambda}{\rho}}(\beta^{+}+w)\\\\
>w^{+} &=w+\beta^{+}-\alpha^{+}
>\end{align}
>$$

## Các tính chất chính

Thuật toán trên có những đặc điểm đáng chú ý sau:

* Ma trận $$X^{T}X+\rho I$$ luôn khả nghịch với mọi $$X$$ vì $$\rho>0$$.
* Nếu tính trước phân rã ma trận (thường là phân rã Cholesky) với chi phí $$O(p^{3})$$ phép toán dấu phẩy động (flops), thì mỗi bước cập nhật $$\beta$$ sau đó chỉ tốn $$O(p^{2})$$ flops.
* Bước cập nhật $$\alpha$$ áp dụng toán tử co ngưỡng mềm $$S_{t}$$ đã trình bày ở [07-03-04]({% multilang_post_url contents/chapter07/21-03-25-07_03_04_example_soft-thresholding %}).
* Về trực giác, mỗi vòng lặp ADMM gần như lặp lại việc giải một bài toán hồi quy ridge rồi áp dụng co ngưỡng mềm lên các hệ số.
* Các giá trị $$\rho$$ khác nhau dẫn đến tốc độ hội tụ khác nhau.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/lasso.png" alt="[Hình 1] So sánh các thuật toán cho hồi quy lasso (50 trường hợp với n = 100, p = 20) [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] So sánh các thuật toán cho hồi quy lasso (50 trường hợp với n = 100, p = 20) [3]</figcaption>
</p>
</figure>


## So sánh hiệu năng

[Hình 1] so sánh đường hội tụ của nhiều thuật toán trên bài toán hồi quy Lasso, trong đó các thuật toán đều có độ phức tạp mỗi vòng lặp tương đương nhau. Trên đồ thị, ADMM đạt tốc độ hội tụ gần tương đương với proximal gradient descent (đường đen). Accelerated proximal gradient descent (đường đỏ) xuất hiện các dao động dạng "gợn Nesterov" nhưng hội tụ nhanh hơn một chút. Ngoài ra, tốc độ hội tụ của ADMM thay đổi rõ rệt tùy theo giá trị $$\rho$$. Phương pháp coordinate descent (đường xanh lá), sẽ được trình bày ở [Chương 23]({% multilang_post_url contents/chapter23/21-03-28-23_Coordinate_Descent %}), khai thác sâu hơn cấu trúc bài toán nên hội tụ nhanh hơn các phương pháp còn lại, dù đòi hỏi các điều kiện áp dụng riêng.

Nếu đặt $$\rho$$ quá lớn, trọng số tương đối của hàm mục tiêu $$f+g$$ giảm đi; ngược lại, nếu $$\rho$$ quá nhỏ, tốc độ tiến về miền khả thi sẽ chậm. Do đó, việc chọn $$\rho$$ phù hợp đóng vai trò quan trọng. Chi tiết hơn có thể xem trong [BPCPE] tại [danh mục bài báo tham khảo của Chương 21]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %}).

## Hồi quy Group Lasso

Tương tự, ta áp dụng ADMM cho bài toán hồi quy Group Lasso với $$y\in \mathbb{R}^{n}$$ và $$X\in \mathbb{R}^{n \times p}$$:

>$$
>\begin{align}
>\min_{\beta}\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda\sum^{G}_{g=1} c_{g}||\beta_{(g)}||_{2}.
>\end{align}
>$$

Tách biến tương tự như trường hợp Lasso, ta viết lại bài toán thành:
>$$
>\begin{align}
>&\min_{\beta,\alpha} &&\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda\sum^{G}_{g=1} c_{g}||\alpha_{(g)}||_{2}\\\\
>&\text{subject to} &&\beta-\alpha=0.
>\end{align}
>$$

Các bước cập nhật ADMM thu được là:
>$$
>\begin{align}
>\beta^{+} &= (X^{T}X+\rho I)^{-1}(X^{T}y+\rho (\alpha-w))\\\\
>\alpha^{+}_{(g)} &= R_{c_{g}\frac{\lambda}{\rho}}(\beta^{+}_{(g)}+w_{(g)})\qquad g = 1,\ldots,G\\\\
>w^{+} &=w+\beta^{+}-\alpha^{+}
>\end{align}
>$$

## Các tính chất của ADMM cho Group Lasso

Thuật toán này có các đặc điểm sau:

* Ma trận $$X^{T}X+\rho I$$ luôn khả nghịch với mọi $$X$$ vì $$\rho>0$$.
* Nếu tính trước phân rã Cholesky với chi phí $$O(p^{3})$$ flops, mỗi bước cập nhật $$\beta$$ chỉ tốn $$O(p^{2})$$ flops.
* Bước cập nhật $$\alpha$$ sử dụng toán tử co ngưỡng mềm theo nhóm (group soft-thresholding) $$R_{t}$$, định nghĩa như sau:

>$$
>\begin{align}
>R_{t}(x) = \left(1-\frac{t}{\lVert x \rVert_{2}}\right)_{+}x
>\end{align}
>$$

### ADMM cho lasso (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/admm-lasso_vi.mp4"></video>
</div>

ADMM thực hiện luân phiên một bước cập nhật $$x$$ kiểu hồi quy ridge, một bước cập nhật $$z$$ bằng co ngưỡng mềm, và một bước cập nhật biến đối ngẫu $$u$$ nhằm kéo $$x$$ và $$z$$ tiến lại gần nhau.

Video dùng ký hiệu chung của ADMM: $$x$$ ứng với $$\beta$$, $$z$$ ứng với $$\alpha$$, $$u$$ ứng với $$w$$ (biến đối ngẫu đã chia cho $$\rho$$); ma trận $$X$$ và vectơ $$y$$ của bài được viết là $$A$$ và $$b$$. Trong video, $$y$$ là nhân tử Lagrange chứ không phải vectơ đáp ứng.

### Tự tay thử: ADMM trên bài toán Lasso

<div class="opx-explainer" data-opx="admm" data-lang="vi"></div>
