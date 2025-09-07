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

Phần này thảo luận các tính chất và đặc trưng của các hàm giả lồi khả vi.

## Điều kiện bậc nhất
Gọi $$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ là một hàm khả vi. Nếu $$\text{dom}f$$ lồi và điều kiện sau được thỏa mãn, thì $$f$$ là giả lồi.
>$$f$$ là giả lồi $$\iff$$ $$f(y) \leq f(x) \Rightarrow \nabla f(x)^T(y-x) \leq 0$$ với mọi $$x, y \in \text{dom}f$$

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/3.12_Three_level_curves_OV6vtPq.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1]</figcaption>
</p>
</figure>
**Ba đường mức của một hàm giả lồi $$f$$. $$\nabla f(x)$$ là vector pháp tuyến định nghĩa siêu phẳng hỗ trợ của tập mức dưới $$\{z \mid f(z) \leq f(x)\}$$ tại $$x$$.**


Điều kiện bậc nhất cho tính giả lồi có vẻ tương tự như đặc trưng bậc nhất của tính lồi (xem [03-01-03]({% multilang_post_url contents/chapter03/21-02-12-03_01_03_key_properties_of_convex_functions %})), nhưng có những khác biệt quan trọng. Ví dụ, nếu $$f$$ lồi và $$\nabla f(x) = 0$$, thì $$x$$ là điểm cực tiểu toàn cục của $$f$$, nhưng điều này không luôn đúng cho các hàm giả lồi.

<br>
## Điều kiện bậc hai

Khi $$f$$ khả vi hai lần, các điều kiện bậc hai được áp dụng. Nếu $$f$$ là giả lồi, thì với mọi $$x \in \text{dom}f$$ và mọi $$y \in \mathbb{R}^n$$, điều sau đây đúng:
>$$f$$ là giả lồi, $$y^T \nabla f(x) = 0 \Longrightarrow y^T \nabla^2 f(x)y \geq 0$$ với mọi $$x \in \text{dom} f$$, mọi $$y \in \mathbb{R}^n$$ <br>

Với các hàm giả lồi trên $$\mathbb{R}$$:

>$$f$$ là giả lồi, $$f'(x) = 0 \Rightarrow f''(x) \geq 0$$

Tức là, nếu tồn tại bất kỳ điểm nào có độ dốc bằng không, giá trị đạo hàm bậc hai là không âm. Quay lại với $$\mathbb{R}^n$$, điều kiện bậc hai cũng thỏa mãn các tính chất sau:

1) Khi $$\nabla f(x) = 0$$, chúng ta phải luôn có $$\nabla^2f(x) \succeq 0$$.
2) Nếu $$\nabla f(x) \neq 0$$, thì $$y^T \nabla f(x) = 0 \Rightarrow y^T \nabla^2 f(x)y \geq 0$$, trong đó $$\nabla^2 f(x)$$ hoạt động như ma trận Hessian và là nửa xác định dương trên không gian con $$(n-1)$$ chiều $$\nabla f(x)^\perp$$.

(Không gian con $$(n-1)$$ chiều $$\nabla f(x)^\perp$$ có nghĩa là không gian con $$(n-1)$$ chiều vuông góc với $$\nabla f(x)$$. Nó có $$(n-1)$$ chiều vì $$\nabla f(x)$$ là gradient của hàm $$n$$ chiều $$f$$, làm giảm chiều đi một.)
