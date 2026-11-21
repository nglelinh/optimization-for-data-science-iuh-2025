---
layout: post
title: '08-01-06 Kích thước bước Polyak'
chapter: '08'
order: 8
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

**Kích thước bước Polyak** là một cách để thiết lập kích thước bước khi giá trị tối ưu được biết. Nếu $$f^*$$ được biết, kích thước bước Polyak có thể được định nghĩa như sau.

## Định lý hội tụ cho kích thước bước Polyak
>
$$ \begin{align}
t_k = \frac{f^{(k-1)}-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}}, \quad k = 1,2,3...
\end{align} $$

## Chứng minh định lý hội tụ cho kích thước bước Polyak
Chứng minh có thể được suy ra từ [bất đẳng thức cơ bản]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}) và chuỗi bất đẳng thức được sử dụng ở đó.

>
$$ \begin{align}
 \Vert x^{(k)}-x^* \Vert_2^{2}  \quad \le \quad  \Vert x^{(k-1)}-x^* \Vert_2^{2}-2t_k (f(x^{(k-1)})-f^*)+t_k^{2} \Vert g^{(k-1)} \Vert_2^{2} \\
\end{align} $$

Lấy đạo hàm vế phải ở trên theo $$t_k$$ và cho bằng 0, ta thu được kích thước bước Polyak làm cực tiểu vế phải.
>
$$ \begin{align}
& \frac{\partial}{\partial t_k}  \Vert x^{(k-1)}-x^* \Vert_2^{2}-2t_k (f(x^{(k-1)})-f^*)+t_k^{2} \Vert g^{(k-1)} \Vert_2^{2} = 0 \\
 \Longleftrightarrow & -2(f(x^{(k-1)})-f^*)+2t_k \Vert g^{(k-1)} \Vert_2^{2} = 0 \\
 \Longleftrightarrow & f(x^{(k-1)})-f^* = t_k \Vert g^{(k-1)} \Vert_2^{2} \\
 \Longleftrightarrow & t_k = \frac{f(x^{(k-1)})-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}} \quad \text{(kích thước bước Polyak tại k)}
\end{align} $$

Tốc độ hội tụ của kích thước bước Polyak cũng có thể được suy ra từ [bất đẳng thức cơ bản]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}) và chuỗi bất đẳng thức được sử dụng ở đó.

## Tốc độ hội tụ cho kích thước bước Polyak

Hãy thay kích thước bước Polyak $$t_i$$ vào bất đẳng thức cơ bản đã được suy ra ở phần [bất đẳng thức cơ bản]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}).
>
$$ \begin{align}
& 2\sum_{i=1}^{k}t_i(f(x^{(i)})-f^*) \le R^2 + \sum_{i=1}^kt_i^2 \Vert g^{(i)} \Vert_2^2 \\
 \Longleftrightarrow \quad & 2\sum_{i=1}^{k}\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \le R^2 + \sum_{i=1}^k\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \\
 \Longleftrightarrow \quad & \sum_{i=1}^{k}\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \le R^2 \\
\end{align} $$

Giả sử điều kiện Lipschitz $$ \Vert g^{(i)} \Vert_2 \le G$$ luôn đúng, bất đẳng thức trên có thể được sắp xếp lại như sau:
>
$$ \begin{align}
& \sum_{i=1}^{k}(f(x^{(i)})-f^*)^2 \le R^2G^2 \\
 \Longleftrightarrow \quad & k ⋅ (f(x^{(i)})-f^*)^2 \le R^2G^2 \\
 \Longleftrightarrow \quad & \sqrt{k} ⋅ (f(x^{(i)})-f^*) \le RG \\
 \Longleftrightarrow \quad & (f(x^{(i)})-f^*) \le \frac{RG}{\sqrt{k}} \\
\end{align} $$

(Ở đây $$f(x^{(i)})$$ được hiểu là giá trị tốt nhất trong các vòng lặp đã thực hiện, $$f^{(k)}_{best}$$.)

Nếu đặt $$\frac{RG}{\sqrt{k}}=\epsilon$$ thì $$k=\big(\frac{RG}{\epsilon}\big)^2$$, do đó số vòng lặp cần thiết để đạt một điểm cận tối ưu với độ chính xác $$\epsilon$$ có bậc $$\big(\frac{RG}{\epsilon}\big)^2$$. Nói cách khác, tốc độ hội tụ là $$O(1/\epsilon^{2})$$, giống như các phương pháp subgradient khác.

### Bước Polyak trong 18 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/polyak-step_vi.mp4"></video>
</div>

Bước cố định bị kẹt ở một mức nhất định, bước giảm dần đi rất chậm, còn bước Polyak $$\alpha_k=\dfrac{f(x_k)-f^*}{\|g_k\|_2^2}$$ rơi đúng vào điểm cực tiểu, nhưng cần biết $$f^*$$.

### Tự tay thử: ba quy tắc kích thước bước

<div class="opx-explainer" data-opx="sgm" data-lang="vi"></div>
