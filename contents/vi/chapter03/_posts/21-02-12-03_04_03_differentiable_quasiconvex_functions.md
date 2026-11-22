---
layout: post
title: 03-04-03 Hàm giả lồi khả vi
chapter: '03'
order: 11
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

Phần này trình bày các điều kiện đặc trưng bậc nhất và bậc hai cho hàm giả lồi khả vi.

## Điều kiện bậc nhất

Cho hàm khả vi $$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ có miền xác định $$\text{dom}f$$ lồi. Khi đó $$f$$ là hàm giả lồi khi và chỉ khi:
>$$f$$ là giả lồi $$\iff$$ $$f(y) \leq f(x) \Rightarrow \nabla f(x)^T(y-x) \leq 0$$ với mọi $$x, y \in \text{dom}f$$

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/3.12_Three_level_curves_OV6vtPq.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1]</figcaption>
</p>
</figure>
**Ba đường mức của một hàm giả lồi $$f$$: gradient $$\nabla f(x)$$ là vector pháp tuyến của một siêu phẳng hỗ trợ tập mức dưới $$\{z \mid f(z) \leq f(x)\}$$ tại $$x$$.**

Điều kiện bậc nhất của hàm giả lồi có dạng khá giống đặc trưng bậc nhất của hàm lồi (xem bài [03-01-03]({% multilang_post_url contents/chapter03/21-02-12-03_01_03_key_properties_of_convex_functions %})), nhưng vẫn có khác biệt quan trọng: với hàm lồi, $$\nabla f(x) = 0$$ suy ra $$x$$ là điểm cực tiểu toàn cục, còn với hàm giả lồi thì điều này không nhất thiết đúng.

<br>

## Điều kiện bậc hai

Khi $$f$$ khả vi hai lần và là hàm giả lồi, với mọi $$x \in \text{dom}f$$ và mọi $$y \in \mathbb{R}^n$$ ta có:
>$$f$$ là giả lồi, $$y^T \nabla f(x) = 0 \Longrightarrow y^T \nabla^2 f(x)y \geq 0$$ với mọi $$x \in \text{dom} f$$, mọi $$y \in \mathbb{R}^n$$ <br>

Trong trường hợp một biến trên $$\mathbb{R}$$, điều kiện này rút gọn thành:

>$$f$$ là giả lồi, $$f'(x) = 0 \Rightarrow f''(x) \geq 0$$

Nghĩa là tại mọi điểm dừng (đạo hàm bậc nhất bằng 0), đạo hàm bậc hai phải không âm. Trong không gian $$\mathbb{R}^n$$, điều kiện bậc hai kéo theo hai hệ quả sau:

1. Nếu $$\nabla f(x) = 0$$ thì ma trận Hessian phải nửa xác định dương: $$\nabla^2f(x) \succeq 0$$.
2. Nếu $$\nabla f(x) \neq 0$$ thì $$y^T \nabla f(x) = 0 \Rightarrow y^T \nabla^2 f(x)y \geq 0$$, tức là ma trận Hessian $$\nabla^2 f(x)$$ nửa xác định dương trên không gian con $$(n-1)$$ chiều $$\nabla f(x)^\perp$$ (tập các vector vuông góc với $$\nabla f(x)$$).
