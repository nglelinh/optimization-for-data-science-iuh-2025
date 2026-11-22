---
layout: post
title: 06-02-01 Kích thước bước cố định
chapter: '06'
order: 6
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Cách đơn giản nhất để chọn kích thước bước trong gradient descent là giữ nguyên một giá trị cố định cho mọi lần lặp: $$t_k = t$$ với $$k = 1, 2, 3, ...$$. Tuy nhiên, tốc độ và khả năng hội tụ của thuật toán phụ thuộc rất lớn vào việc lựa chọn $$t$$.

Ví dụ, hình dưới đây minh họa gradient descent áp dụng cho hàm $$f(x) = (10 x_1^2 + x_2^2) / 2$$ với ba kích thước bước khác nhau:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_02_01_gradientdescent4.png" alt="gradientdescent4" width="100%" height="100%">
  <figcaption style="text-align: center;">[Hình 1] Các trường hợp lựa chọn kích thước bước [3]</figcaption>
</p>
</figure>

* Trong trường hợp A, kích thước bước $$t$$ quá lớn, khiến thuật toán phân kỳ sau 8 bước và không thể tiến tới điểm cực tiểu.
* Trong trường hợp B, kích thước bước $$t$$ quá nhỏ, khiến tốc độ hội tụ rất chậm và chưa đạt được điểm cực tiểu ngay cả sau 100 bước.
* Trong trường hợp C, kích thước bước có độ lớn phù hợp, giúp thuật toán hội tụ trong khoảng 40 bước. (Cách xác định khoảng giá trị phù hợp này sẽ được phân tích ở các mục sau trong chương.)

### Kích thước bước: ba quy tắc trong 20 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/gd-step-sizes_vi.mp4"></video>
</div>

Trên mặt hàm có đường đồng mức kéo dài, bước quá lớn gây dao động zig-zag hoặc phân kỳ, còn bước quá nhỏ khiến thuật toán tiến rất chậm. Backtracking line search và exact line search giúp tự động chọn kích thước bước phù hợp.

### Tự tay thử: kích thước bước

<div class="opx-explainer" data-opx="gd" data-lang="vi"></div>
