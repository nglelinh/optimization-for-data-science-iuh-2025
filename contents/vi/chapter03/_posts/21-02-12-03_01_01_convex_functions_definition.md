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

Không phải mọi hàm lồi đều "đẹp" như nhau dưới góc độ thuật toán. Hàm giá trị tuyệt đối $$|x|$$ lồi nhưng có đáy nhọn và có thể tạo ra cả một đoạn nghiệm tối ưu không duy nhất; hàm mũ $$e^x$$ lồi chặt nhưng càng đi về $$-\infty$$ càng dẹt phẳng dần khiến Gradient Descent bò chậm; chỉ đến **hàm lồi mạnh** (strongly convex) ta mới có bảo đảm đáy cong chặt toàn cục, nghiệm duy nhất và tốc độ hội tụ tuyến tính thần tốc!

Bài học này phân biệt rạch ròi chuỗi bao hàm quan trọng bậc nhất của tối ưu hóa: **lồi mạnh $$\implies$$ lồi chặt $$\implies$$ lồi**, cùng khái niệm hàm lõm đối xứng.

## Kiến thức cần nhớ: Bốn cấp độ của độ cong lồi

![Định nghĩa hình học hàm lồi qua dây cung]({{ site.baseurl }}/img/chapter_img/chapter03/convex_function01.png)

- **Hàm lồi (Convex):** Miền xác định $$\operatorname{dom} f$$ lồi và $$f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y)$$. Bảo đảm cực tiểu địa phương = cực tiểu toàn cục, nhưng cực tiểu có thể không duy nhất.
- **Hàm lồi chặt (Strictly Convex):** Bất đẳng thức chặt $$<$$ với mọi $$x \ne y,\ \theta \in (0, 1)$$. Bảo đảm nếu cực tiểu tồn tại thì nó là **duy nhất**, nhưng độ cong vẫn có thể tiến về $$0$$ ở vô cực.
- **Hàm $$m$$-lồi mạnh ($$m$$-Strongly Convex):** $$f(x) - \frac{m}{2}\|x\|_2^2$$ vẫn còn lồi (với $$m > 0$$), tương đương $$\nabla^2 f(x) \succeq m I$$. Đồ thị bị chặn dưới toàn cục bởi một chiếc bát parabol có độ cong tối thiểu $$m$$, bảo đảm tốc độ hội tụ hình học (tuyến tính) cho Gradient Descent!
- **Hàm lõm (Concave):** $$-f$$ là hàm lồi; cực đại hóa hàm lõm tương đương cực tiểu hóa hàm lồi $$-f$$.

### Giải thích: So sánh 3 hàm đại diện cho 3 nấc lồi trên $$\mathbb{R}$$

Hãy kiểm tra trực tiếp từng nấc trên ba hàm cụ thể:

1. **Lồi nhưng KHÔNG lồi chặt — $$f_1(x) = |x|$$:**
   Chọn $$x = 1,\ y = 3,\ \theta = 0.5$$ (trung điểm $$2$$):
   $$f_1(2) = 2 = 0.5\cdot f_1(1) + 0.5\cdot f_1(3) = 0.5(1) + 0.5(3) = 2.$$
   Dấu bằng xảy ra dù $$x \ne y$$, nên $$|x|$$ không lồi chặt.
2. **Lồi chặt nhưng KHÔNG lồi mạnh — $$f_2(x) = e^x$$ trên $$\mathbb{R}$$:**
   Đạo hàm bậc hai $$f_2''(x) = e^x > 0\ \forall x \in \mathbb{R} \implies$$ **lồi chặt**.
   Tuy nhiên, với mọi hằng số $$m > 0$$ bất kỳ, khi chọn $$x < \ln m$$ ta có $$f_2''(x) = e^x < m$$, nên không tồn tại $$m > 0$$ chặn dưới $$e^x$$ trên toàn $$\mathbb{R}$$!
3. **Lồi mạnh — $$f_3(x) = x^2 + e^x$$ trên $$\mathbb{R}$$:**
   Đạo hàm bậc hai $$f_3''(x) = 2 + e^x > 2\ \forall x \in \mathbb{R}$$. Do đó $$f_3(x) - \frac{2}{2}x^2 = e^x$$ vẫn lồi, chứng tỏ $$f_3$$ là **2-lồi mạnh** trên toàn $$\mathbb{R}$$!

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
