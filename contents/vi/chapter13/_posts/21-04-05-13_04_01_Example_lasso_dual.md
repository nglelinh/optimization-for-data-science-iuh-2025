---
layout: post
title: 13-04-01 Ví dụ đối ngẫu lasso
chapter: '13'
order: 6
owner: Wontak Ryu
categories:
- chapter13
lang: vi
---

Xét bài toán lasso với $$y \in \mathbb{R}^n$$ và $$X \in \mathbb{R}^{n\times p}$$:

> $$ \min_\beta \frac{1}{2} \| y-X\beta \|^2_2 + \lambda\| \beta \|_1$$
> 
> $$f(\beta) = \frac{1}{2} \| y - X\beta \|^2_2 +  \lambda\| \beta \|_1$$
> 
> $$L(\beta) = f(\beta)$$
> 
> $$ \min_\beta L(\beta) = f^{\star}$$

Vì bài toán gốc không có ràng buộc nên hàm đối ngẫu chỉ là hằng số bằng $$f^{\star}$$. Để xây dựng bài toán đối ngẫu hữu ích hơn, ta đưa thêm biến phụ $$z = X\beta$$ và viết lại bài toán nguyên thủy tương đương:

> $$ \min_{\beta,z} \frac{1}{2} \| y-z \|^2_2 + \lambda \| \beta \|_1 \text{ với điều kiện } z = X\beta$$

Hàm đối ngẫu Lagrange của bài toán đã biến đổi là:

> $$\begin{align}
> g(u) &= \min_{\beta,z} \frac{1}{2} \| y-z \|^2_2 + \lambda \| \beta \|_1 + u^T(z-X\beta) \\
> &= \frac{1}{2} \| y \|^2_2 - \frac{1}{2} \| y-u \|^2_2 - I_{\{ v : \| v \|_\infty \leq 1 \}}(X^Tu/\lambda) \\
> \end{align}$$

#### Chứng minh
> $$\begin{align}
> g(u) &= \min_{\beta,z} \frac{1}{2} \| y-z \|^2_2 + \lambda \| \beta \|_1 + u^T(z-X\beta) \\
> &= \underbrace{ \left( \min_z \frac{1}{2} \| y - z \|^2_2 + u^Tz \right)}_{(1)} + \underbrace{\left( \min_\beta \left(\lambda \| \beta \|_1 - u^TX\beta\right) \right)}_{(2)} \\
> \end{align}$$
> 
> Ở phần (1), lấy đạo hàm theo $$z$$ bằng $$0$$ cho $$z^{\star} = y - u$$, nên:
> 
> $$\begin{align}
> (1) \cdots \left( \min_z \frac{1}{2} \| y - z \|^2_2 + u^Tz \right)
> &= \frac{1}{2} \| u \|^2_2 + u^T(y - u) \\
> &= -\frac{1}{2} \| y - u \|^2_2 + \frac{1}{2} \| y \|^2_2 \\
> \end{align}$$
> 
> Ở phần (2), dùng hàm liên hợp của chuẩn $$\ell_1$$:
> 
> $$\begin{align}
> (2) \cdots \left( \min_\beta \left(\lambda \| \beta \|_1 - u^TX\beta\right) \right) 
> &= - \lambda \max_\beta \left( \left(\frac{X^Tu}{\lambda}\right)^T \beta - \| \beta \|_1 \right) \\
> &= - I_{\{ v : \| v \|_\infty \leq 1 \}}(X^Tu/\lambda) \\
> &= - I_{\{ w : \| w \|_\infty \leq \lambda \}}(X^Tu) \\
> \end{align}$$
> 
> Suy ra:
> 
> $$g(u) = \frac{1}{2} \| y \|^2_2 - \frac{1}{2} \| y-u \|^2_2 - I_{\{ v : \| v \|_\infty \leq 1 \}}(X^Tu/\lambda)$$

Do đó, bài toán đối ngẫu của lasso là:

> $$ \max_u \frac{1}{2} ( \| y \|^2_2 - \| y-u \|^2_2 ) \text{ với điều kiện } \| X^Tu \|_\infty \leq \lambda$$

Bỏ hằng số $$\frac{1}{2}\|y\|_2^2$$ và đổi dấu, bài toán đối ngẫu tương đương với bài toán chiếu Euclidean lên đa diện:

> $$ \min_u \| y-u \|^2_2 \text{ với điều kiện } \| X^Tu \|_\infty \leq \lambda$$

### Kiểm tra tính đối ngẫu mạnh

Bài toán nguyên thủy là bài toán lồi chỉ có ràng buộc đẳng thức tuyến tính nên thỏa mãn điều kiện Slater; do đó tính đối ngẫu mạnh được đảm bảo:

> $$ \text{Đối ngẫu mạnh } \implies (\beta^{\star}, z^{\star}) \text{ phải cực tiểu hóa } L( \beta, z, u^{\star} ) \text{ theo } \beta, z$$

### Lưu ý

Giá trị tối ưu của bài toán rút gọn $$\min_u \|y - u\|_2^2$$ không bằng giá trị mục tiêu tối ưu của bài toán lasso gốc (vì đã bỏ hằng số và hệ số $$\frac{1}{2}$$). Tuy nhiên, nghiệm đối ngẫu $$u^{\star}$$ và nghiệm lasso $$\beta^{\star}$$ liên hệ trực tiếp qua đẳng thức $$X\beta^{\star} = y - u^{\star}$$.

Hệ thức này suy ra từ điều kiện dừng KKT theo $$z$$ là $$z - y + u = 0$$ kết hợp với ràng buộc $$z = X\beta$$. Do đó, nghiệm đối ngẫu $$u^{\star}$$ chính là phần dư $$y - X\beta^{\star}$$ của bài toán lasso.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter13/Conjugate_LassoDual_Example.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig2] Đối ngẫu của bài toán Lasso [1]</figcaption>
</p>
</figure>

### Đối ngẫu của lasso nhìn như một phép chiếu (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/lasso-dual_vi.mp4"></video>
</div>

Bài toán đối ngẫu tìm $$u$$ thỏa $$\|A^Tu\|_\infty\le\lambda$$. Các tọa độ mà ràng buộc này chạm biên (đạt dấu bằng) tương ứng với các thành phần có thể khác $$0$$ của nghiệm bài toán gốc.

### Tự tay thử: lasso gốc và đối ngẫu

<div class="opx-explainer" data-opx="ld" data-lang="vi"></div>
