---
layout: post
title: 03-01-03 Các tính chất chính của hàm lồi
chapter: '03'
order: 5
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

## Đặc trưng epigraph

Như đã nêu ở [bài 01-02]({% multilang_post_url contents/chapter01/21-01-28-01_02_convex_optimization_problem %}), hàm $$f$$ lồi khi và chỉ khi epigraph (tập trên đồ thị) của nó là một tập lồi:

> $$f$$ lồi $$\iff \text{epi}(f) = \{(x,t) \in \mathbb{R}^{n+1} \mid x \in \text{dom} f, f(x) \le t \}$$ là một tập lồi

## Tập mức dưới lồi

Nếu $$f$$ là hàm lồi thì mọi tập mức dưới của nó đều là tập lồi:

> $$\{x \in \text{dom } f: f(x) \leq t\}$$, với mọi $$t \in \mathbb{R}$$

### [Lưu ý] Tập mức dưới
Với một hàm $$f:\mathbb{R}^n \mapsto \mathbb{R}$$, tập $$C_\alpha = \{x \in \text{dom} f \mid f(x) \leq \alpha\}$$ được gọi là *tập mức dưới mức $$\alpha$$*.

## Đặc trưng bậc nhất

Giả sử $$f$$ là hàm **khả vi**. Khi đó $$f$$ lồi khi và chỉ khi miền xác định $$\text{dom} f$$ lồi và với mọi $$x, y \in \text{dom} f$$, ta có $$f(y) \geq f(x) +\nabla f(x)^T(y-x)$$:

> $$f$$ lồi $$\iff \text{dom}f$$ lồi, và $$f(y) \geq f(x) +\nabla f(x)^T(y-x)$$ với mọi $$x,y \in \text{dom} f$$

Hình dưới đây minh họa điều kiện bậc nhất cho một hàm lồi khả vi $$f$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/1st_order_condition.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Hàm Lồi [1]</figcaption>
</p>
</figure>

Điều kiện này còn gọi là **điều kiện tiếp tuyến** (hoặc siêu phẳng tiếp tuyến trong không gian nhiều chiều): xấp xỉ tuyến tính bậc nhất của $$f$$ tại bất kỳ điểm $$x$$ nào luôn là một chặn dưới toàn cục của $$f$$. Nói cách khác, đồ thị của hàm lồi luôn nằm phía trên (hoặc trùng với) mọi tiếp tuyến của nó.

### Ví dụ

Xét hàm $$f(x) = x^2$$ với đạo hàm $$f'(x) = 2x$$. Tại một điểm bất kỳ $$x_0$$, phương trình tiếp tuyến với đồ thị $$f$$ là:
$$L(x) = f(x_0) + f'(x_0)(x - x_0) = x_0^2 + 2x_0(x - x_0)$$

Điều kiện bậc nhất đòi hỏi với mọi $$x \in \mathbb{R}$$:
$$f(x) \geq L(x) \iff x^2 \geq x_0^2 + 2x_0(x - x_0)$$

Rút gọn vế phải và chuyển vế, ta được:
$$x^2 - 2x_0x + x_0^2 \geq 0 \iff (x - x_0)^2 \geq 0$$

Bất đẳng thức này luôn đúng với mọi số thực $$x$$ và $$x_0$$, khẳng định $$f(x) = x^2$$ thỏa mãn điều kiện bậc nhất và là hàm lồi.

## Đặc trưng bậc hai

Nếu $$f$$ khả vi hai lần với miền xác định $$\text{dom} f$$ lồi, ta có các tiêu chuẩn sau:

- $$f$$ lồi khi và chỉ khi ma trận Hessian $$\nabla^2 f(x)$$ nửa xác định dương với mọi $$x \in \text{dom} f$$:
> $$f$$ lồi $$\iff \nabla^2f(x) \succeq 0$$ với mọi $$x \in \text{dom} f$$, $$\text{dom} f$$ lồi

- Nếu $$\nabla^2 f(x)$$ xác định dương với mọi $$x \in \text{dom} f$$ thì $$f$$ lồi chặt:
> nếu $$\nabla^2f(x) \succ 0$$ với mọi $$x \in \text{dom} f$$, thì $$f$$ lồi chặt

Nói cách khác, độ cong của hàm theo mọi phương đều không âm.

## Bất đẳng thức Jensen

Cho $$f$$ là hàm lồi và $$w_1, \dots, w_n \ge 0$$ là các trọng số không âm thỏa mãn $$\sum_{i=1}^{n} w_i = 1$$. Khi đó, với mọi $$x_1, \dots, x_n \in \text{dom} f$$:

$$\sum_{i=1}^{n} w_i f(x_i) \geq f \left ( \sum_{i=1}^{n} w_i x_i \right )$$

Trong trường hợp hai điểm, bất đẳng thức này trở về dạng quen thuộc:
>$$f(tx_1 + (1 - t)x_2) \le tf(x_1) + (1 - t)f(x_2) \text{ với } 0 \le t \le 1 $$

>*Mở rộng xác suất:*<br>
>Nếu $$X$$ là biến ngẫu nhiên nhận giá trị trong $$\text{dom } f$$ thì $$f(E[X]) \le E[f(X)]$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/jensen_inequality.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 2] Bất đẳng thức Jensen [2]</figcaption>
</p>
</figure>

### **Bất đẳng thức Jensen có trùng với định nghĩa hàm lồi không?**

Không hoàn toàn — bất đẳng thức Jensen là hệ quả và là dạng tổng quát hóa của định nghĩa hàm lồi:

- Định nghĩa hàm lồi chỉ xét tổ hợp lồi của hai điểm ($$n=2$$), còn bất đẳng thức Jensen mở rộng cho số điểm hữu hạn bất kỳ và sang dạng tích phân / kỳ vọng đối với độ đo xác suất.
- Với $$n=2$$, bất đẳng thức Jensen trùng khớp với định nghĩa hàm lồi; với $$n \ge 3$$, ta suy ra nó bằng quy nạp từ trường hợp hai điểm.

---

### Ví dụ minh họa

Xét hàm lồi $$f(x) = x^2$$ với hai điểm $$x_1 = 1$$ và $$x_2 = 3$$. Ta so sánh $$f\left(\frac{x_1+x_2}{2}\right)$$ và $$\frac{f(x_1)+f(x_2)}{2}$$:

1. **Giá trị hàm tại trung bình cộng:**
   Trung bình cộng là $$\frac{1+3}{2} = 2$$, nên $$f(2) = 2^2 = 4$$.

2. **Trung bình cộng của các giá trị hàm:**
   Ta có $$f(1) = 1$$ và $$f(3) = 9$$, nên trung bình cộng là $$\frac{1+9}{2} = 5$$.

So sánh hai giá trị cho thấy $$4 \le 5$$, đúng với bất đẳng thức Jensen: $$f\left(\frac{1+3}{2}\right) \le \frac{f(1)+f(3)}{2}$$.

### Bốn cách kiểm tra hàm lồi trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/convexity-tests_vi.mp4"></video>
</div>

Dây cung và Jensen trên x² (ví dụ 1 và 3), tiếp tuyến nằm dưới đồ thị, đạo hàm bậc hai và Hessian, epigraph và tập mức dưới, đối chiếu với hàm hình chữ W x⁴ − 3x².
