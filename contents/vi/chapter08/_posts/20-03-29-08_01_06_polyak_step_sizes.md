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

**Kích thước bước Polyak** là quy tắc chọn kích thước bước khi đã biết trước giá trị tối ưu $$f^*$$. Công thức kích thước bước Polyak được định nghĩa như sau:

## Định nghĩa kích thước bước Polyak
>
$$ \begin{align}
t_k = \frac{f^{(k-1)}-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}}, \quad k = 1,2,3...
\end{align} $$

## Cách suy ra kích thước bước Polyak
Ta xuất phát từ bất đẳng thức trung gian trong phần [bất đẳng thức cơ bản]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}):

>
$$ \begin{align}
 \Vert x^{(k)}-x^* \Vert_2^{2}  \quad \le \quad  \Vert x^{(k-1)}-x^* \Vert_2^{2}-2t_k (f(x^{(k-1)})-f^*)+t_k^{2} \Vert g^{(k-1)} \Vert_2^{2} \\
\end{align} $$

Lấy đạo hàm vế phải theo $$t_k$$ và cho bằng 0 để cực tiểu hóa cận trên của khoảng cách $$\Vert x^{(k)}-x^* \Vert_2^2$$, ta thu được kích thước bước Polyak:
>
$$ \begin{align}
& \frac{\partial}{\partial t_k}  \Vert x^{(k-1)}-x^* \Vert_2^{2}-2t_k (f(x^{(k-1)})-f^*)+t_k^{2} \Vert g^{(k-1)} \Vert_2^{2} = 0 \\
 \Longleftrightarrow & -2(f(x^{(k-1)})-f^*)+2t_k \Vert g^{(k-1)} \Vert_2^{2} = 0 \\
 \Longleftrightarrow & f(x^{(k-1)})-f^* = t_k \Vert g^{(k-1)} \Vert_2^{2} \\
 \Longleftrightarrow & t_k = \frac{f(x^{(k-1)})-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}} \quad \text{(kích thước bước Polyak tại bước k)}
\end{align} $$

## Tốc độ hội tụ của kích thước bước Polyak

Thay kích thước bước Polyak $$t_i$$ vào bất đẳng thức tổng quát từ phần [bất đẳng thức cơ bản]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}):
>
$$ \begin{align}
& 2\sum_{i=1}^{k}t_i(f(x^{(i)})-f^*) \le R^2 + \sum_{i=1}^kt_i^2 \Vert g^{(i)} \Vert_2^2 \\
 \Longleftrightarrow \quad & 2\sum_{i=1}^{k}\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \le R^2 + \sum_{i=1}^k\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \\
 \Longleftrightarrow \quad & \sum_{i=1}^{k}\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \le R^2 \\
\end{align} $$

Với giả thiết Lipschitz $$ \Vert g^{(i)} \Vert_2 \le G$$, bất đẳng thức trên dẫn đến:
>
$$ \begin{align}
& \sum_{i=1}^{k}(f(x^{(i)})-f^*)^2 \le R^2G^2 \\
 \Longleftrightarrow \quad & k ⋅ (f(x^{(i)})-f^*)^2 \le R^2G^2 \\
 \Longleftrightarrow \quad & \sqrt{k} ⋅ (f(x^{(i)})-f^*) \le RG \\
 \Longleftrightarrow \quad & (f(x^{(i)})-f^*) \le \frac{RG}{\sqrt{k}} \\
\end{align} $$

(Trong các dòng suy ra cuối, $$f(x^{(i)})$$ được hiểu là giá trị tốt nhất qua $$k$$ bước lặp, tức $$f^{(k)}_{best}$$.)

Đặt $$\frac{RG}{\sqrt{k}}=\epsilon$$, ta thu được $$k=\big(\frac{RG}{\epsilon}\big)^2$$. Như vậy, số bước lặp cần thiết để đạt sai số $$\epsilon$$ có bậc $$\big(\frac{RG}{\epsilon}\big)^2$$, tức tốc độ hội tụ là $$O(1/\epsilon^{2})$$ — cùng bậc với các quy tắc chọn bước khác của phương pháp subgradient.

### Bước Polyak: chọn độ dài bước từ f* (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/polyak-step_vi.mp4"></video>
</div>

Bước cố định dừng lại ở một lân cận quanh nghiệm tối ưu, bước giảm dần tiến rất chậm, còn bước Polyak $$\alpha_k=\dfrac{f(x_k)-f^*}{\|g_k\|_2^2}$$ hướng thẳng về điểm cực tiểu nhưng đòi hỏi phải biết trước $$f^*$$.

### Tự tay thử: ba quy tắc kích thước bước

<div class="opx-explainer" data-opx="sgm" data-lang="vi"></div>
