---
layout: post
title: 06-02-01 Kích thước bước cố định
chapter: '06'
order: 4
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Cách đơn giản nhất để chọn kích thước bước trong gradient descent là sử dụng một giá trị cố định cho tất cả các lần lặp: $$t_k = t$$ với $$k = 1, 2, 3, ...$$. Tuy nhiên, sự hội tụ và hành vi phụ thuộc rất nhiều vào việc lựa chọn $$t$$.

Ví dụ, trong hình dưới đây, gradient descent được áp dụng cho $$f(x) = (10 x_1^2 + x_2^2) / 2$$ với các kích thước bước khác nhau:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_02_01_gradientdescent4.png" alt="gradientdescent4" width="100%" height="100%">
  <figcaption style="text-align: center;">[Hình 1] Các kịch bản kích thước bước [3]</figcaption>
</p>
</figure>

* Trong trường hợp A, kích thước bước $$t$$ quá lớn, gây ra phân kỳ sau 8 bước. Không thể đạt được cực tiểu.
* Trong trường hợp B, kích thước bước $$t$$ quá nhỏ, vì vậy sự hội tụ rất chậm và cực tiểu không được đạt được ngay cả sau 100 bước.
* Trong trường hợp C, kích thước bước là "phù hợp", và sự hội tụ đạt được trong khoảng 40 bước. (Cách tìm giá trị "phù hợp" này được thảo luận sau trong chương này.)
