---
layout: post
title: '23-03 Ví dụ: hồi quy lasso'
chapter: '23'
order: 4
owner: YoungJae Choung
categories:
- chapter23
lang: vi
---

Khi Robert Tibshirani giới thiệu hồi quy **Lasso** năm 1996, bài toán này từng bị xem là khá chậm để giải vì hàm phạt $$\lambda\|\beta\|_1$$ không khả vi tại gốc tọa độ, buộc người dùng thời đó phải chuyển sang quy hoạch bậc hai (QP) với số ràng buộc tăng gấp đôi. Nhưng hơn một thập kỷ sau, cộng đồng thống kê phát hiện ra một sự thật đẹp đến khó tin: vì chuẩn $$\ell_1$$ tách hoàn toàn theo từng tọa độ, **hạ theo tọa độ (Coordinate Descent)** biến bài toán Lasso không trơn thành một chuỗi phép co ngưỡng mềm 1 chiều đơn giản đến mức có thể tính nhẩm!

Chính phát hiện này đã đưa Lasso từ một khái niệm học thuật thành công cụ phân tích dữ liệu tiêu chuẩn trong y sinh, tài chính và học máy quy mô lớn, thường nhanh hơn cả Proximal Gradient và Accelerated Proximal Gradient hàng bậc độ lớn.

## Kiến thức cần nhớ: Ba trụ cột của Coordinate Descent cho Lasso

Để hiểu trọn vẹn công thức cập nhật chỉ vỏn vẹn một dòng của bài học này, hãy nắm vững ba trụ cột sau:

- **Dưới đạo hàm của giá trị tuyệt đối (Subdifferential of $$|\beta_i|$$):** Tại $$\beta_i \neq 0$$, đạo hàm là $$\operatorname{sign}(\beta_i)$$; còn tại điểm gấp khúc $$\beta_i = 0$$, dưới vi phân là cả đoạn $$[-1, 1]$$. Chính đoạn $$[-1, 1]$$ này tạo ra "vùng chết" (*dead zone*): nếu tương quan giữa cột $$X_i$$ và phần dư đủ nhỏ ($$\le \lambda$$), hệ số $$\beta_i$$ bị kéo hẳn về $$0$$.
- **Toán tử co ngưỡng mềm (Soft-Thresholding Operator):** Định nghĩa $$S_\tau(z) = \operatorname{sign}(z)\max(|z| - \tau, 0)$$. Nghiệm tối ưu theo từng tọa độ của Lasso chỉ gồm hai thao tác liên tiếp: (1) tính nghiệm hồi quy bình phương tối thiểu 1 biến trên phần dư riêng, rồi (2) kéo nó về phía $$0$$ một đoạn bằng đúng $$\tau_i = \lambda / \|X_i\|_2^2$$.
- **Định lý Tseng và Tính thưa tức thì:** Nhờ $$\sum_{i=1}^p |\beta_i|$$ tách được hoàn toàn theo từng biến, Coordinate Descent được đảm bảo hội tụ tới nghiệm tối ưu toàn cục của Lasso. Hơn thế, nhiều hệ số lập tức bằng $$0$$ ngay từ các vòng đầu, mở đường cho kỹ thuật bỏ qua biến không hoạt động (*active set*) ở bài sau.

### Giải thích: Tính tay 1 chu trình CD cho Lasso và quan sát ngưỡng sinh tính thưa

Ta giữ nguyên ma trận $$X$$ và vector $$y$$ từ bài trước để so sánh trực tiếp hồi quy tuyến tính thường với Lasso:

$$
X = \begin{pmatrix} 1 & 1 \\ 1 & -1 \\ 0 & 1 \end{pmatrix}, \qquad y = \begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix}, \qquad \|X_1\|_2^2 = 2,\; \|X_2\|_2^2 = 3.
$$

Chọn hệ số phạt $$\lambda = 2$$, khởi tạo $$\beta^{(0)} = (0, 0)$$ và phần dư $$r = (3, 1, 1)^T$$:

1. **Cập nhật tọa độ $$i = 1$$:**
   - Nghiệm hồi quy thường 1 biến: $$z_1 = \frac{X_1^T r}{\|X_1\|_2^2} = \frac{3 + 1 + 0}{2} = 2$$.
   - Ngưỡng co riêng cho cột 1: $$\tau_1 = \frac{\lambda}{\|X_1\|_2^2} = \frac{2}{2} = 1$$.
   - Áp dụng co ngưỡng mềm: $$\beta_1^{(1)} = S_1(2) = \operatorname{sign}(2)\max(2 - 1, 0) = 1$$.
   - Cập nhật phần dư: $$r \leftarrow (3, 1, 1)^T - 1 \cdot (1, 1, 0)^T = (2, 0, 1)^T$$.
2. **Cập nhật tọa độ $$i = 2$$:**
   - Nghiệm hồi quy thường 1 biến: $$z_2 = \frac{X_2^T r}{\|X_2\|_2^2} = \frac{2 + 0 + 1}{3} = 1$$.
   - Ngưỡng co riêng cho cột 2: $$\tau_2 = \frac{\lambda}{\|X_2\|_2^2} = \frac{2}{3}$$.
   - Áp dụng co ngưỡng mềm: $$\beta_2^{(1)} = S_{2/3}(1) = 1 - \frac{2}{3} = \frac{1}{3}$$.
3. **Thử tăng phạt lên $$\lambda = 4$$ để thấy tính thưa tuyệt đối:**
   - Với cột 1, ngưỡng mới là $$\tau_1 = \frac{4}{2} = 2$$, nên $$\beta_1 = S_2(2) = 0$$!
   - Phần dư vẫn là $$(3, 1, 1)^T$$; với cột 2, $$z_2 = \frac{3 - 1 + 1}{3} = 1$$ còn ngưỡng $$\tau_2 = \frac{4}{3} > 1$$, nên $$\beta_2 = S_{4/3}(1) = 0$$!
   Chỉ cần quan sát một phép trừ nhỏ, bạn đã thấy tận mắt cơ chế cắt hệ số về đúng $$0$$ của Lasso!

Xét bài toán hồi quy Lasso dưới dạng tổng của một hàm lồi khả vi và một hàm không trơn tách được theo từng tọa độ:

> $$
> \min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2 + \lambda \|\beta\|_1
> $$

**Lưu ý:** $$\|\beta\|_1 = \sum_{i=1}^p | \beta_i |$$.

Giữ cố định các thành phần $$\beta_j$$ ($$j \neq i$$), ta tìm $$\beta_i$$ cực tiểu hóa hàm mục tiêu từ điều kiện tối ưu bậc nhất với dưới đạo hàm:

$$\begin{align}
&0 \in \partial_i f(\beta) \;\Longleftrightarrow\; 0 = X_i^T X_i \beta_i + X_i^T(X_{-i} \beta_{-i} - y) + \lambda s_i,\\\\
&\text{với } s_i \in \partial |\beta_i|
\;\Rightarrow\;
\beta_i = S_{\lambda / \|X_i\|_2^2} \big( \frac{X_i^T(y-X_{-i} \beta_{-i})}{X_i^TX_i} \big)
\end{align}$$

Nghiệm cập nhật có dạng toán tử co ngưỡng mềm (soft-thresholding) với ngưỡng $$\lambda / \|X_i\|_2^2$$. Thuật toán coordinate descent lặp lại bước cập nhật $$\beta_i$$ này lần lượt cho $$i=1,2,\dots,p,1,2,\dots$$.

## Thí nghiệm: so sánh tốc độ hội tụ giữa PG, AGD và CD

Đồ thị dưới đây so sánh tốc độ hội tụ của proximal gradient descent (PG), accelerated proximal gradient descent (AGD) và coordinate descent (CD) trên bài toán hồi quy Lasso với $$n=100, p=20$$. Giá trị $$k$$ trên trục hoành biểu diễn một bước lặp (đối với PG, AGD) hoặc một chu trình duyệt đủ $$p$$ tọa độ (đối với CD).

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/pd_vs_agd_vs_cd.png" alt="[Hình 1] PG, AGD và CD [3]">
  <figcaption style="text-align: center;">[Hình 1] PG, AGD và CD [3]</figcaption>
</p>
</figure>
<br><br>

Tương tự [ví dụ hồi quy tuyến tính]({% multilang_post_url contents/chapter23/21-03-28-23_02_Example_linear_regression %}), coordinate descent tiếp tục hội tụ nhanh hơn đáng kể so với PG và AGD nhờ sử dụng ngay thông tin cập nhật mới nhất của từng tọa độ trong mỗi chu trình.

* **Lưu ý:** Cả ba phương pháp trong thí nghiệm trên đều có chi phí tính toán $$O(np)$$ flops cho mỗi vòng lặp/chu trình.
