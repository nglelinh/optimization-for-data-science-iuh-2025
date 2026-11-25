---
layout: post
title: 20-02-01 Phân rã đối ngẫu với ràng buộc đẳng thức
chapter: '20'
order: 5
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

Trong bài toán tối ưu có ràng buộc đẳng thức tuyến tính $$\sum_{i=1}^B A_i x_i = b$$, phân rã đối ngẫu hoạt động theo một nhịp điệu hai pha cực kỳ sạch sẽ: pha song song (từng khối $$i$$ tự tìm $$x_i^{(k)}$$ ứng với mức giá $$u^{(k-1)}$$) và pha tổng hợp (nút trung tâm cộng dồn độ lệch $$\sum_i A_i x_i^{(k)} - b$$ để cập nhật $$u^{(k)}$$). Nhờ chỉ trao đổi vector biến đối ngẫu $$u \in \mathbb{R}^m$$ thay vì trao đổi toàn bộ dữ liệu hay hàm chi phí $$f_i$$, kỹ thuật này bảo toàn quyền riêng tư dữ liệu và mở rộng tự nhiên trên các cụm máy chủ phân tán.

## Bản đồ kiến thức nền: Ba điểm cốt lõi của phân rã đối ngẫu với ràng buộc đẳng thức

Để áp dụng đúng thuật toán phân rã đẳng thức mà không gặp bẫy hội tụ, hãy nắm vững ba điểm sau:

- **Phân hoạch theo khối cột của ma trận $$A = [A_1, \dots, A_B]$$:** Điều kiện tiên quyết để bài toán con tách rời hoàn toàn là hàm mục tiêu phải cộng tính $$\sum_i f_i(x_i)$$ và ràng buộc đẳng thức phải cộng tính $$\sum_i A_i x_i = b$$ (không có số hạng chéo giữa $$x_i$$ và $$x_j$$).
- **Biến đối ngẫu tự do dấu ($$u \in \mathbb{R}^m$$):** Vì ràng buộc là đẳng thức $$Ax = b$$, nhân tử $$u$$ có thể nhận cả giá trị dương lẫn âm — không cần phép chiếu lên góc phần tư không âm.
- **Điều kiện hội tụ của từng biến gốc $$x_i^{(k)}$$:** Dù giá trị đối ngẫu $$g(u^{(k)})$$ hội tụ dưới điều kiện nhẹ, bản thân dãy điểm gốc $$x^{(k)}$$ chỉ chắc chắn hội tụ về nghiệm tối ưu $$x^\star$$ khi mỗi $$f_i$$ lồi chặt (hoặc lồi mạnh); nếu $$f_i$$ tuyến tính, $$x_i^{(k)}$$ có thể nhảy qua lại giữa các đỉnh mà không bao giờ thỏa mãn $$Ax = b$$!

### Khung giải thích (nên đọc chậm): Chạy tay 2 vòng lặp phân rã song song cho 2 khối biến

Xét bài toán tách biến với ràng buộc đẳng thức:

$$\min_{x_1, x_2} \; \underbrace{x_1^2}_{f_1(x_1)} + \underbrace{2x_2^2}_{f_2(x_2)} \qquad \text{với điều kiện} \qquad x_1 + x_2 = 3.$$

Nghiệm tối ưu chính xác là $$x_1^\star = 2, x_2^\star = 1, u^\star = -4$$. Khởi tạo $$u^{(0)} = -2$$ và chọn bước học $$t = 1$$:

1. **Vòng lặp $$k = 1$$:**
   - **Giải song song 2 bài toán con với $$u^{(0)} = -2$$:**
     - Khối 1: $$x_1^{(1)} = \arg\min_{x_1} (x_1^2 - 2x_1) = 1.0$$.
     - Khối 2: $$x_2^{(1)} = \arg\min_{x_2} (2x_2^2 - 2x_2) = 0.5$$.
   - **Cập nhật đối ngẫu tại nút trung tâm:**
     Phần dư $$r^{(1)} = x_1^{(1)} + x_2^{(1)} - 3 = 1.5 - 3 = -1.5$$.
     $$u^{(1)} = -2 + 1(-1.5) = -3.5.$$
2. **Vòng lặp $$k = 2$$:**
   - **Giải song song với $$u^{(1)} = -3.5$$:**
     - Khối 1: $$x_1^{(2)} = \arg\min_{x_1} (x_1^2 - 3.5x_1) = 1.75$$.
     - Khối 2: $$x_2^{(2)} = \arg\min_{x_2} (2x_2^2 - 3.5x_2) = 0.875$$.
   - **Cập nhật đối ngẫu:**
     Phần dư $$r^{(2)} = 1.75 + 0.875 - 3 = -0.375$$ (giảm **4 lần** chỉ sau 1 vòng!).
     $$u^{(2)} = -3.5 + 1(-0.375) = -3.875$$ — tiến sát $$u^\star = -4$$ cực nhanh!

---

Xét bài toán tối ưu có hàm mục tiêu tách biến kèm ràng buộc đẳng thức tuyến tính:
>$$\begin{equation}
>\min_x \sum_{i=1}^B f_i(x_i) \quad \text{ subject to } \quad Ax = b
>\end{equation}$$

Giả sử biến $$x$$ được phân hoạch thành $$B$$ khối $$x = (x_1, \dots, x_B) \in \mathbb{R}^n$$ với $$x_i \in \mathbb{R}^{n_i}$$, và ma trận $$A$$ được chia tương ứng thành $$B$$ khối cột $$A = [A_1, \dots, A_B]$$ với $$A_i \in \mathbb{R}^{m \times n_i}$$. Khi cố định biến đối ngẫu $$u$$, bài toán cực tiểu hóa theo $$x$$ tách hoàn toàn thành $$B$$ bài toán con độc lập:
> $$
> \begin{alignat}{1}
> & \quad x^+ \in \arg\min_x \sum_{i=1}^B f_i(x_i) + u^T Ax  \\
> \Longleftrightarrow & \quad x_i^+ \in \arg\min_{x_i} f_i(x_i) + u^T A_ix_i, \quad i=1,\dots, B
> \end{alignat}
> $$

### Thuật toán phân rã đối ngẫu

> $$
> \begin{alignat}{1}
> x_i^{(k)} & \in \arg \min_{x_i} f_i(x_i) + (u^{(k-1)})^T A_i x_i, \quad i=1,\dots,B  \\
> u^{(k)}   & = u^{(k-1)} + t_k \left(\sum_{i=1}^B A_i x_i^{(k)} - b \right)
> \end{alignat}
> $$

Thuật toán lặp lại hai bước sau với $$k = 1, 2, 3, \dots$$:
* **Bước phát (broadcast):** Giá trị đối ngẫu $$u^{(k-1)}$$ hiện tại được gửi tới cả $$B$$ bộ xử lý; mỗi bộ xử lý giải song song bài toán con để tìm $$x_i^{(k)}$$.
* **Bước thu (gather):** Thu thập các kết quả $$A_i x_i^{(k)}$$ từ các bộ xử lý để cập nhật biến đối ngẫu toàn cục $$u^{(k)}$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter20/decomposition.png" alt="[Hình 1] Broadcast and Gather" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Broadcast and Gather</figcaption>
</p>
</figure>

### Phân rã đối ngẫu: giá và các tác tử (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/dual-decomposition_vi.mp4"></video>
</div>

Mỗi tác tử tự giải bài toán con của riêng mình theo mức giá $$\nu$$, sau đó bước tăng đối ngẫu (dual ascent) điều chỉnh tăng hoặc giảm $$\nu$$ tùy theo mức độ vi phạm ràng buộc $$\sum_i x_i - c$$.

### Tự tay thử: đặt mức giá

<div class="opx-explainer" data-opx="dd" data-lang="vi"></div>
