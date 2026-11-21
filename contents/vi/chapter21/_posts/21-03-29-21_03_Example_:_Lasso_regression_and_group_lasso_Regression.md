---
layout: post
title: '21-03 Ví dụ: Hồi quy Lasso và hồi quy group lasso'
chapter: '21'
order: 4
owner: Hooncheol Shin
categories:
- chapter21
lang: vi
---

## Hồi quy Lasso
Hãy giải bài toán hồi quy Lasso bằng ADMM.

Cho $$y\in \mathbb{R}^{n}, X\in \mathbb{R}^{n\times p}$$, bài toán Lasso là:
>$$
>\begin{align}
>\min_{\beta}\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda||\beta||_{1}
>\end{align}
>$$

Ở các chương trước, chúng ta đã giải bài toán Lasso bằng nhiều phương pháp, gồm [proximal gradient descent (ISTA)]({% multilang_post_url contents/chapter09/20-01-08-09_01_proximal_gradient_descent %}), [accelerated proximal gradient descent (FISTA)]({% multilang_post_url contents/chapter09/20-01-08-09_05_03_example_FISTA %}), [phương pháp barrier]({% multilang_post_url contents/chapter15/21-03-28-15_barrier_method %}) và [phương pháp điểm trong gốc-đối ngẫu]({% multilang_post_url contents/chapter17/21-05-01-17_primal_dual_interior_point_method %}).

Cũng như khi suy ra dạng đối ngẫu, hiệu năng của thuật toán ADMM phụ thuộc vào cách ta thiết lập các biến phụ. Trong nhiều cách thiết lập biến phụ, dạng sau được biết là một trong những dạng hiệu quả nhất:
>$$
>\begin{align}
>&\min_{\beta, \alpha} &&\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda||\alpha||_{1}\\\\
>&\text{subject to} &&\beta-\alpha= 0.
>\end{align}
>$$

## Các cập nhật ADMM

Các cập nhật ADMM cho dạng này được suy ra như sau. Cập nhật $$\beta$$ là một hàm bậc hai nên ta có thể tìm cực tiểu bằng cách lấy đạo hàm. Cập nhật $$\alpha$$ tương tự bài toán đã xét ở [Chương 7 (07-03-04)]({% multilang_post_url contents/chapter07/21-03-25-07_03_04_example_soft-thresholding %}), có nghiệm dạng soft-thresholding.
>$$
>\begin{align}
>\beta^{+} &= \underset{\beta}{\operatorname{argmin}}\frac{1}{2}||y-X\beta||^{2}_{2}+\frac{\rho}{2}||\beta-\alpha+w||^{2}_{2}\\\\
>&= (X^{T}X+\rho I)^{-1}(X^{T}y+\rho (\alpha-w))\\\\
>\alpha^{+} &= \underset{\alpha}{\operatorname{argmin}}\lambda||\alpha||_{1}+\frac{\rho}{2}||\beta^{+}-\alpha+w||^{2}_{2}\\\\
>&= S_{\frac{\lambda}{\rho}}(\beta^{+}+w)\\\\
>w^{+} &=w+\beta^{+}-\alpha^{+}
>\end{align}
>$$

## Các tính chất chính

Kết quả này có các đặc điểm sau:

* Ma trận $$X^{T}X+\rho I$$ luôn khả nghịch với mọi $$X$$ vì $$\rho>0$$.
* Nếu tính trước phân rã (thường là phân rã Cholesky) trong $$O(p^{3})$$ flops thì cập nhật $$\beta$$ tốn $$O(p^{2})$$ flops.
* Cập nhật $$\alpha$$ áp dụng toán tử soft-thresholding $$S_{t}$$, giống hệt nội dung ở [07-03-04]({% multilang_post_url contents/chapter07/21-03-25-07_03_04_example_soft-thresholding %}).
* Các bước ADMM "gần như" tương đương với việc lặp lại soft-thresholding các hệ số của hồi quy ridge.
* Các giá trị $$\rho$$ khác nhau cho kết quả khác nhau.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/lasso.png" alt="[Hình 1] So sánh các thuật toán cho hồi quy lasso (50 trường hợp với n = 100, p = 20) [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] So sánh các thuật toán cho hồi quy lasso (50 trường hợp với n = 100, p = 20) [3]</figcaption>
</p>
</figure>


## So sánh hiệu năng

[Hình 1] so sánh sự hội tụ của nhiều thuật toán cho bài toán hồi quy Lasso. Tất cả các thuật toán có cùng độ phức tạp tính toán trên mỗi vòng lặp. Như thấy từ tốc độ hội tụ trên đồ thị, ADMM có tốc độ hội tụ tương tự proximal gradient descent (đen). Accelerated proximal gradient descent (đỏ) có các "gợn Nesterov" nhưng cho tốc độ hội tụ nhanh hơn một chút. Ta cũng thấy ADMM có tốc độ hội tụ khác nhau tùy theo giá trị $$\rho$$. Coordinate descent (xanh lá), sẽ được thảo luận sau ở [Chương 23]({% multilang_post_url contents/chapter23/21-03-28-23_Coordinate_Descent %}), dùng nhiều thông tin hơn về bài toán nên có tốc độ hội tụ nhanh hơn các phương pháp khác. Nhược điểm của coordinate descent là việc áp dụng cần những điều kiện nhất định.

Nếu giá trị $$\rho$$ đặt quá lớn thì trọng số của việc cực tiểu hóa hàm mục tiêu $$f+g$$ trở nên nhỏ, còn nếu $$\rho$$ đặt quá nhỏ thì tính khả thi giảm. Vì vậy, việc đặt giá trị $$\rho$$ phù hợp là quan trọng. Thông tin chi tiết xem [BPCPE] được thảo luận trong [các bài báo tham khảo của Chương 21]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %}).

## Hồi quy Group Lasso

Tương tự, hãy xem cách giải bài toán hồi quy Group Lasso bằng ADMM. Bài toán hồi quy Group Lasso được định nghĩa như sau với $$y\in \mathbb{R}^{n}, X\in \mathbb{R}^{n \times p}$$:

>$$
>\begin{align}
>\min_{\beta}\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda\sum^{G}_{g=1} c_{g}||\beta_{(g)}||_{2}.
>\end{align}
>$$

Như với hồi quy Lasso, ta có thể viết lại bài toán:
>$$
>\begin{align}
>&\min_{\beta,\alpha} &&\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda\sum^{G}_{g=1} c_{g}||\alpha_{(g)}||_{2}\\\\
>&\text{subject to} &&\beta-\alpha=0.
>\end{align}
>$$

Các bước ADMM như sau:
>$$
>\begin{align}
>\beta^{+} &= (X^{T}X+\rho I)^{-1}(X^{T}y+\rho (\alpha-w))\\\\
>\alpha^{+} &= R_{c_{g}\frac{\lambda}{\rho}}(\beta^{+}_{(g)}+w_{(g)})\qquad \text{g = 1,...G}\\\\
>w^{+} &=w+\beta^{+}-\alpha^{+}
>\end{align}
>$$

## Các tính chất của ADMM cho Group Lasso

Kết quả này có các đặc điểm sau:

* Ma trận $$X^{T}X+\rho I$$ luôn khả nghịch với mọi $$X$$ vì $$\rho>0$$.
* Nếu tính trước phân rã (thường là phân rã Cholesky) trong $$O(p^{3})$$ flops thì cập nhật $$\beta$$ tốn $$O(p^{2})$$ flops.
* Cập nhật $$\alpha$$ áp dụng toán tử group soft-thresholding $$R_{t}$$, được định nghĩa như sau:

>\begin{align}
>R_{t}(x) = \left(1-\frac{t}{\lVert x \rVert_{2}}\right)_{+}x
>\end{align}

### ADMM trong 18 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/admm-lasso_vi.mp4"></video>
</div>

ADMM luân phiên một bước cập nhật $$x$$ kiểu ridge, một bước cập nhật $$z$$ bằng co ngưỡng mềm và một bước cập nhật đối ngẫu $$u$$, kéo $$x$$ và $$z$$ lại gần nhau.

### Tự tay thử: ADMM trên bài lasso

<div class="opx-explainer" data-opx="admm" data-lang="vi"></div>
