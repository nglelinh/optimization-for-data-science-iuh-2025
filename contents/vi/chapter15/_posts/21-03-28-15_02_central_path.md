---
layout: post
title: 15-02 Đường trung tâm
chapter: '15'
order: 6
owner: Minjoo Lee
categories:
- chapter15
lang: vi
---

Ký hiệu $$x^*(t)$$ là nghiệm của bài toán chắn ứng với tham số $$t > 0$$:

>$$
>\begin{align}
> &\min_{x} \ &&  tf(x) + \phi(x) \\
> &\text{thỏa mãn } \ && Ax = b \\
> \end{align}
>$$

Khi đó, tập hợp $$\{x^*(t) \mid t > 0 \}$$ được gọi là **đường trung tâm (central path)**.

Dưới các điều kiện phù hợp, đường trung tâm tạo thành một đường cong trơn trong $$\mathbb{R}^n$$ và hội tụ về nghiệm tối ưu $$x^*$$ của bài toán gốc khi $$t \to \infty$$.

Nói cách khác, thay vì tìm trực tiếp nghiệm tối ưu nằm trên biên, ta giải một chuỗi bài toán chắn với các giá trị $$t$$ tăng dần để đi dọc theo đường trung tâm từ bên trong miền khả thi tiến dần ra biên.

## Ví dụ: đường trung tâm của một bài toán LP
Xét bài toán quy hoạch tuyến tính (LP):
>$$
>\begin{align*}
>&\min_{x} \ && c^Tx \\
>&\text{thỏa mãn } \ && a_i^Tx \le b_i, \quad i = 1, \cdots , 6 \\
>\end{align*}
>$$

Trong hình dưới đây, các đường nét đứt biểu diễn đường đồng mức của hàm chắn logarit $$\phi$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_central_path_02.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Đường trung tâm [1]</figcaption>
</p>
</figure>

Khi $$t \to \infty$$, đường trung tâm hội tụ về đỉnh tối ưu $$x^*$$. Tại mỗi điểm $$x^*(t)$$ trên đường trung tâm, siêu phẳng $$c^Tx = c^Tx^*(t)$$ tiếp xúc với đường đồng mức của $$\phi$$ đi qua $$x^*(t)$$.

### Đường trung tâm trong 10 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/central-path_vi.mp4"></video>
</div>

Khi $$t$$ tăng dần, nghiệm $$x^*(t)$$ của bài toán chắn trượt dọc theo đường trung tâm tiến về đỉnh tối ưu.

### Tự tay thử: trượt dọc đường trung tâm

<div class="opx-explainer" data-opx="barrier" data-lang="vi"></div>
