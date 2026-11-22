---
layout: post
title: 12-03 Ví dụ thuật toán water-filling
chapter: '12'
order: 4
owner: Wontak Ryu
categories:
- chapter12
lang: vi
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Xét bài toán tối ưu hóa lồi sau:

>$$
>\begin{align}
>    &\min_{x} &&{- \sum_{i=1}^n \log(\alpha_i + x_i)} \\\\
>    &\text{với điều kiện} &&{x \succeq 0, 1^Tx = 1},\\\\
>&\text{trong đó } \alpha_i > 0.
>\end{align}
>$$

Bài toán này xuất hiện trong lý thuyết thông tin, gắn với việc phân bổ công suất cho $$n$$ kênh truyền thông. Biến $$x_i$$ biểu diễn công suất phát phân bổ cho kênh thứ $$i$$, còn $$\log(\alpha_i + x_i)$$ biểu diễn dung lượng hay tốc độ truyền của kênh đó. Như vậy, mục tiêu là phân bổ tổng công suất cố định vào các kênh sao cho tổng tốc độ truyền đạt cực đại [1].

Gọi $$\lambda^\star \in \mathbb{R}^n$$ và $$\nu^\star \in \mathbb{R}$$ lần lượt là các nhân tử Lagrange ứng với ràng buộc bất đẳng thức $$x^\star \succeq 0$$ và ràng buộc đẳng thức $$1^Tx^\star = 1$$. Các điều kiện KKT của bài toán là:

>$$
>\begin{align}
>x^\star \succeq 0, \\\\
>1^Tx^\star = 1, \\\\
>\lambda^\star \succeq 0, \\\\
>\lambda_i^\star x_i^\star = 0, \text{    } i = 1, \dots, n, \\\\
> -1 / (\alpha_i + x_i^\star) - \lambda_i^\star + \nu^\star = 0,  \text{    } i= 1, \dots, n.
>\end{align}
> $$

Từ hệ điều kiện KKT trên, ta có thể tìm $$x^\star, \lambda^\star, \nu^\star$$ theo dạng giải tích. Trước hết, khử $$\lambda^\star$$ bằng cách coi nó như biến phụ không âm ($$\lambda_i^\star = \nu^\star - 1/(\alpha_i + x_i^\star) \ge 0$$):

>$$
>\begin{align}
>x^\star \succeq 0, \\\\
>1^Tx^\star = 1, \\\\
>x_i^\star(\nu^\star - 1 / (\alpha_i + x_i^\star)) = 0, \text{    } i = 1, \dots, n, \\\\
> \nu^\star \ge 1/(\alpha_i + x_i^\star),  \text{    } i= 1, \dots, n.
>\end{align}
> $$

Kết hợp điều kiện dừng và điều kiện bù yếu, ta thu được biểu thức nghiệm:

> $$
> x_i^\star = 
> \begin{cases}
> 1 / \nu^\star - \alpha_i &\nu^\star < 1/\alpha_i \ \\\\
> 0 &\nu^\star \ge 1/\alpha_i\\\\
> \end{cases}
> = \max\{0, 1/\nu^\star - \alpha_i \}, \quad i = 1, \dots, n.
> $$

Theo ràng buộc $$1^T x^\star = 1$$, tổng các thành phần $$x_i^\star$$ ($$i = 1, \dots, n$$) bằng $$1$$:

> $$
> \sum_{i=1}^n \max\{0, 1/\nu^\star - \alpha_i \} = 1.
> $$

Vế trái là một hàm tuyến tính từng khúc và tăng theo $$1/\nu^\star$$, nên với các giá trị $$\alpha_i$$ cố định, phương trình trên có nghiệm duy nhất cho $$1/\nu^\star$$.

Phương pháp giải này được gọi là **water-filling (đổ nước)**. Nếu xem $$\alpha_i$$ là độ cao đáy của ngăn thứ $$i$$, bài toán tương đương với việc đổ nước vào các ngăn cho đến khi mực nước chung đạt mức $$1/\nu^\star$$ và tổng lượng nước đổ vào bằng $$1$$, như minh họa trong hình dưới đây.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl}}/img/chapter_img/chapter12/water-fill.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Minh họa thuật toán water-filling [1]</figcaption>
</p>
</figure>
