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

Hãy định nghĩa bài toán hồi quy tuyến tính như sau.

> $$\min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2,$$
> $$\text{với } y \in \mathbb{R}^n \text{ và } X \in \mathbb{R}^{n \times p} \text{ có các cột } X_1, \dots, X_p.$$

Khi các $$\beta_j,\: j \neq i$$ là giá trị cố định, hãy tìm $$\beta_i$$ cực tiểu hóa hàm mục tiêu đã cho.
($$-i$$ nghĩa là các thành phần còn lại trừ $$i$$. Với $$X$$ thì đó là các cột còn lại trừ cột thứ $$i$$.)

$$\begin{align}
0 &= \nabla_i f(\beta)\\\\
&= X_i^T (X\beta - y)\\\\
&= X_i^T (X_i \beta_i + X_{-i} \beta_{-i} - y)\\\\
\Rightarrow\\\\
&\beta_i = \frac{X_i^T (y - X_{-i} \beta_{-i})}{X_i^T X_i}
\end{align}$$

Với coordinate descent, ta lặp lại và cập nhật $$\beta_i$$ với $$i=1,2,\dots,p,1,2,\dots$$.

## Thí nghiệm: so sánh tốc độ hội tụ - GD, AGD và CD

Đồ thị dưới đây cho thấy tốc độ hội tụ của coordinate descent, gradient descent và accelerated gradient descent cho bài toán hồi quy tuyến tính với $$n=100, p=20$$. (Giá trị k trên trục hoành biểu diễn một bước (GD, AGD) hoặc một chu trình (CD).)

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/gd_vs_agd_vs_cd.png" alt="[Hình 1] GD, AGD và CD [3]">
  <figcaption style="text-align: center;">[Hình 1] GD, AGD và CD [3]</figcaption>
</p>
</figure>
<br/>

Theo các kết quả trên, coordinate descent cho tốc độ hội tụ tốt hơn đáng kể so với AGD, vốn tối ưu trong các phương pháp bậc nhất. Vì sao hiện tượng này có thể xảy ra? Kết luận là coordinate descent có thể đạt hiệu năng vượt xa AGD vì nó dùng nhiều thông tin hơn các phương pháp bậc nhất. Đó là vì coordinate descent, ở mỗi bước trong một chu trình, dùng thông tin mới nhất vừa được cập nhật ở bước trước. (Nghĩa là CD không phải là phương pháp bậc nhất.)

### Q. Vậy so sánh một chu trình của CD với một bước của GD trong thí nghiệm trên có công bằng không?

**A. Có.** Công thức cập nhật CD giới thiệu ở trên có thể được biến đổi để có độ phức tạp thời gian $$O(n)$$ mỗi bước. Khi đó, độ phức tạp thời gian của một chu trình CD là $$O(np)$$, bằng với độ phức tạp thời gian của một bước GD.

* **Cập nhật gradient descent:** $$\beta \leftarrow \beta + tX^T(y-X\beta)$$, độ phức tạp thời gian của phép tính $$X\beta$$ là $$O(np)$$ flops.
* **Cập nhật coordinate descent:** nếu giữ sẵn phần dư $$r = y - X\beta$$, thì $$\beta_i \leftarrow \beta_i + \frac{X_i^T r}{X_i^T X_i}$$ và sau đó cập nhật $$r \leftarrow r - X_i (\beta_i^{\text{new}} - \beta_i^{\text{old}})$$, mỗi bước tốn $$O(n)$$ flops.

### Coordinate descent trong 18 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/coordinate-descent_vi.mp4"></video>
</div>

Coordinate descent cực tiểu hóa chính xác theo từng tọa độ một, vẽ nên đường bậc thang; các tọa độ tương quan làm các bậc thang trở nên nhỏ.

### Tự tay thử: coordinate descent so với gradient descent

<div class="opx-explainer" data-opx="cd" data-lang="vi"></div>
