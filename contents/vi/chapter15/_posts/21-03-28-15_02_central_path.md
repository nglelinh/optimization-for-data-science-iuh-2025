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

Nếu ta ký hiệu nghiệm của bài toán rào cản sau ($$t > 0$$) là $$x^*(t)$$, thì **đường trung tâm** (central path) là tập $$\{x^*(t) | t > 0 \}$$.

>$$\begin{align}
> &\min_{x} \ &&  tf(x) + \phi(x) \\
> &\text{thỏa mãn } \ && Ax = b \\
> \end{align}$$

Với các điều kiện phù hợp, tập **đường trung tâm** tạo thành một đường cong trơn trong $$\mathbb{R}^n$$, và khi $$t \to \infty$$ thì $$x^*(t) \to x^*$$, trong đó $$x^*$$ là nghiệm của bài toán gốc.

**Đường trung tâm** là tập các nghiệm thu được bằng cách định nghĩa lại bài toán dần dần với các giá trị $$t$$ mới, di chuyển từ bên trong tiến ra biên, khi việc tìm trực tiếp nghiệm tối ưu trên biên là khó.

## Ví dụ: đường trung tâm của một bài LP
Hãy tìm đường trung tâm của bài toán LP sau.
>$$\begin{align*}
>&\min_{x} \ && c^Tx \\
>&\text{thỏa mãn } \ && a_i^Tx \le b_i, \quad i = 1, \cdots , 6 \\
>\end{align*}$$

Trong hình dưới đây, đường nét đứt biểu diễn hàm rào logarit $$\phi$$. <br>

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_central_path_02.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Đường trung tâm [1]</figcaption>
</p>
</figure>

Ta thấy rằng khi $$t \to \infty$$, đường trung tâm hội tụ về nghiệm tối ưu $$x^*$$. Tại điểm đó, siêu phẳng $$c^Tx = c^Tx(t)$$ là tiếp tuyến của đường mức của $$\phi$$ đi qua $$c^Tx(t)$$.

### Đường trung tâm trong 10 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/central-path_vi.mp4"></video>
</div>

Khi $$t$$ tăng, nghiệm $$x^*(t)$$ của bài toán rào cản trượt dọc đường trung tâm tới đỉnh tối ưu.

### Tự tay thử: trượt dọc đường trung tâm

<div class="opx-explainer" data-opx="barrier" data-lang="vi"></div>
