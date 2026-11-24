---
layout: post
title: '23-02 Ví dụ: hồi quy tuyến tính'
chapter: '23'
order: 3
owner: Jinwoo Park
categories:
- chapter23
lang: vi
---

Xét bài toán hồi quy tuyến tính:

> $$\min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2,$$
> $$\text{với } y \in \mathbb{R}^n \text{ và } X \in \mathbb{R}^{n \times p} \text{ có các cột } X_1, \dots, X_p.$$

Giữ cố định tất cả các thành phần $$\beta_j$$ ($$j \neq i$$), ta tìm $$\beta_i$$ cực tiểu hóa hàm mục tiêu (ký hiệu $$-i$$ chỉ tập các thành phần còn lại trừ $$i$$; tương ứng $$X_{-i}$$ là ma trận gồm các cột của $$X$$ trừ cột thứ $$i$$):

$$\begin{align}
0 &= \nabla_i f(\beta)\\\\
&= X_i^T (X\beta - y)\\\\
&= X_i^T (X_i \beta_i + X_{-i} \beta_{-i} - y)\\\\
\Rightarrow\\\\
&\beta_i = \frac{X_i^T (y - X_{-i} \beta_{-i})}{X_i^T X_i}
\end{align}$$

Thuật toán coordinate descent lặp lại việc cập nhật $$\beta_i$$ theo công thức trên với $$i = 1, 2, \dots, p, 1, 2, \dots$$.

## Thí nghiệm: so sánh tốc độ hội tụ giữa GD, AGD và CD

Đồ thị dưới đây so sánh tốc độ hội tụ của coordinate descent (CD), gradient descent (GD) và accelerated gradient descent (AGD) trên bài toán hồi quy tuyến tính với $$n=100, p=20$$. Trên trục hoành, giá trị $$k$$ biểu diễn một bước lặp (đối với GD, AGD) hoặc một chu trình duyệt đủ $$p$$ tọa độ (đối với CD).

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/gd_vs_agd_vs_cd.png" alt="[Hình 1] GD, AGD và CD [3]">
  <figcaption style="text-align: center;">[Hình 1] GD, AGD và CD [3]</figcaption>
</p>
</figure>
<br/>

Kết quả cho thấy coordinate descent hội tụ nhanh hơn đáng kể so với AGD — vốn đạt tốc độ tối ưu trong lớp các phương pháp bậc nhất. Lý do là CD không thuộc lớp phương pháp bậc nhất thuần túy: ở mỗi bước con bên trong một chu trình, nó tận dụng ngay giá trị tọa độ vừa được cập nhật ở bước trước đó.

### Câu hỏi: So sánh một chu trình CD với một bước GD như trên có công bằng không?

**Trả lời: Có.** Công thức cập nhật CD có thể cài đặt với độ phức tạp $$O(n)$$ cho mỗi tọa độ, do đó một chu trình gồm $$p$$ tọa độ tốn $$O(np)$$ phép tính — tương đương chi phí một bước GD:

* **Cập nhật gradient descent:** $$\beta \leftarrow \beta + tX^T(y-X\beta)$$, tốn $$O(np)$$ flops để tính $$X\beta$$ và $$X^T r$$.
* **Cập nhật coordinate descent:** duy trì sẵn vector phần dư $$r = y - X\beta$$; khi đó mỗi bước chỉ cần cập nhật $$\beta_i \leftarrow \beta_i + \frac{X_i^T r}{X_i^T X_i}$$ rồi cập nhật phần dư $$r \leftarrow r - X_i (\beta_i^{\text{new}} - \beta_i^{\text{old}})$$, tốn $$O(n)$$ flops mỗi tọa độ.

### Coordinate descent: mỗi lần một tọa độ (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/coordinate-descent_vi.mp4"></video>
</div>

Coordinate descent cực tiểu hóa chính xác theo từng trục tọa độ, tạo nên quỹ đạo dạng bậc thang; khi các biến có tương quan cao, kích thước mỗi bước đi sẽ thu hẹp lại.

### Tự tay thử: coordinate descent so với gradient descent

<div class="opx-explainer" data-opx="cd" data-lang="vi"></div>
