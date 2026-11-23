---
layout: post
title: 03-01-01 Định nghĩa
chapter: '03'
order: 3
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

## Hàm lồi

Một hàm $$f:\mathbb{R}^n \rightarrow \mathbb{R}$$ được gọi là **hàm lồi** nếu miền xác định $$\text{dom}f$$ của nó là một tập lồi và với mọi $$x, y \in \text{dom}f$$ cùng mọi $$0 \le \theta \le 1$$, ta có:

> $$f(\theta x+(1-\theta)y) \le \theta f(x)+(1-\theta)f(y)$$,
>
> với $$0 \le \theta \le 1$$, cho mọi $$x,y \in \text{dom} f$$

Nói cách khác, giá trị của $$f$$ tại tổ hợp lồi của hai điểm $$x, y$$ luôn nhỏ hơn hoặc bằng tổ hợp lồi tương ứng của $$f(x)$$ và $$f(y)$$. Về mặt hình học, đoạn thẳng nối hai điểm $$(x, f(x))$$ và $$(y, f(y))$$ trên đồ thị của $$f$$ luôn nằm phía trên (hoặc trùng với) đồ thị của hàm.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/convex_function2.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Hàm Lồi [2]</figcaption>
</p>
</figure>

## Hàm lồi chặt

Một hàm $$f:\mathbb{R}^n \rightarrow \mathbb{R}$$ được gọi là **lồi chặt** nếu miền xác định $$\text{dom}f$$ lồi và bất đẳng thức nghiêm ngặt sau đúng với mọi hai điểm phân biệt $$x, y \in \text{dom}f$$ và $$0 < \theta < 1$$:

> $$f(\theta x+(1-\theta)y)<\theta f(x)+(1-\theta)f(y)$$,
>
> với $$0<\theta<1$$, $$x \neq y$$, cho mọi $$x, y \in \text{dom}f$$

## Hàm lồi mạnh

Một hàm $$f$$ được gọi là **lồi mạnh** với tham số $$m > 0$$ nếu hàm $$f(x) - \frac{m}{2}\| x \|_{2}^{2}$$ là hàm lồi.

### [Lưu ý] lồi mạnh ⇒ lồi chặt ⇒ lồi

## Hàm lõm

Một hàm $$f$$ được gọi là **hàm lõm** nếu $$-f$$ là hàm lồi.

Mọi hàm affine $$f(x) = a^T x+b$$ đều thỏa mãn đẳng thức:
> $$
\begin{aligned}
f(\theta x+(1-\theta)y) &= a^T (\theta x+(1-\theta)y) +b \\
&= \theta a^T x + (1-\theta) a^T y + \theta b + (1-\theta) b \\
&= \theta f(x)+(1-\theta)f(y) \\
\end{aligned} 
$$
> $$\text{với mọi } x,y \in \text{dom} f, \text{ và } 0 \le \theta \le 1$$

Do đó, mọi hàm affine đều vừa lồi vừa lõm.

### Bốn cách kiểm tra hàm lồi trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/convexity-tests_vi.mp4"></video>
</div>

Dây cung và Jensen trên x² (ví dụ 1 và 3), tiếp tuyến nằm dưới đồ thị, đạo hàm bậc hai và Hessian, epigraph và tập mức dưới, đối chiếu với hàm hình chữ W x⁴ − 3x².
