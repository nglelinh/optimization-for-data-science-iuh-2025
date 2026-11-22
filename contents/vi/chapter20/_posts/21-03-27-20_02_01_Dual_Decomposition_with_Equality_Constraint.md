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

### Phân rã đối ngẫu trong 18 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/dual-decomposition_vi.mp4"></video>
</div>

Mỗi tác tử tự giải bài toán con của riêng mình theo mức giá $$\nu$$, sau đó bước tăng đối ngẫu (dual ascent) điều chỉnh tăng hoặc giảm $$\nu$$ tùy theo mức độ vi phạm ràng buộc $$\sum_i x_i - c$$.

### Tự tay thử: đặt mức giá

<div class="opx-explainer" data-opx="dd" data-lang="vi"></div>
