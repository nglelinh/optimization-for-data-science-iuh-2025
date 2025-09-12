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

Giả sử chúng ta có bài toán tối ưu hóa lồi sau đây.

>$$
>\begin{align}
>    &\min_{x} &&{- \sum_{i=1}^n \log(\alpha_i + x_i)} \\\\
>    &\text{với điều kiện} &&{x \succeq 0, 1^Tx = 1},\\\\
>&\text{trong đó } \alpha_i > 0.
>\end{align}
>$$

Bài toán này liên quan đến việc phân bổ công suất cho n kênh truyền thông và xuất hiện trong lý thuyết thông tin. Biến $$x_i$$ biểu diễn công suất đầu ra của máy phát được phân bổ cho kênh thứ i, và $$\log(\alpha_i + x_i)$$ biểu diễn dung lượng hoặc tốc độ truyền thông của kênh đó. Tức là, bài toán này là xác định bao nhiêu công suất nên được phân bổ cho mỗi kênh để tối đa hóa tổng tốc độ truyền thông [1].

Gọi các nhân tử Lagrange cho ràng buộc bất đẳng thức $$x^\star \succeq 0$$ và ràng buộc đẳng thức $$1^Tx^\star = 1$$ lần lượt là $$\lambda^\star \in \mathbb{R}^n$$ và $$\nu^\star \in \mathbb{R}$$. Các điều kiện KKT cho bài toán đã cho như sau.
>$$
>\begin{align}
>x^\star \succeq 0, \\\\
>1^Tx^\star = 1, \\\\
>\lambda^\star \succeq 0, \\\\
>\lambda_i^\star x_i^\star = 0, \text{    } i = 1, \dots, n, \\\\
> -1 / (\alpha_i + x_i^\star) - \lambda_i^\star + \nu^\star = 0,  \text{    } i= 1, \dots, n.
>\end{align}
> $$

Sử dụng các phương trình thu được từ các điều kiện KKT, chúng ta có thể tìm $$x^\star, \lambda^\star, \nu^\star$$ một cách giải tích. Đầu tiên, chúng ta loại bỏ $$\lambda^\star$$ khỏi các phương trình bằng cách sử dụng nó như một biến slack.
>$$
>\begin{align}
>x^\star \succeq 0, \\\\
>1^Tx^\star = 1, \\\\
>x_i^\star(\nu^\star - 1 / (\alpha_i + x_i^\star)) = 0, \text{    } i = 1, \dots, n, \\\\
> \nu^\star \ge 1/(\alpha_i + x_i^\star),  \text{    } i= 1, \dots, n.
>\end{align}
> $$

Điều này được sắp xếp như sau bởi tính dừng và bù yếu.
> $$
> x_i^\star = 
> \begin{cases}
> 1 / \nu^\star - \alpha_i &\nu^\star < 1/\alpha_i \ \\\\
> 0 &\nu^\star \ge 1/\alpha_i\\\\
> \end{cases}
> = \max\{0, 1/\nu^\star - \alpha_i \}, \quad i = 1, \dots, n.
> $$

Cũng vậy, theo điều kiện $$1^T x^\star = 1$$, $$x_i^\star, i = 1, \dots, n$$ có tổng bằng 1.
> $$
> \sum_{i=1}^n \max\{0, 1/\nu^\star - \alpha_i \} = 1.
> $$

Vế trái của phương trình là một hàm tuyến tính từng khoảng tăng của $$1/\nu^\star$$, vì vậy phương trình này có một nghiệm duy nhất cho $$\alpha_i$$ cố định.

Phương pháp giải này được gọi là water-filling (đổ nước). Khi $$\alpha_i$$ là mức độ nền cho vùng $$i$$, bài toán này có thể được nghĩ như việc đổ nước vào mỗi vùng sao cho mực nước trở thành $$1/\nu^\star$$ như được hiển thị trong hình dưới đây. Chúng ta đổ nước cho đến khi tổng lượng nước trở thành 1.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl}}/img/chapter_img/chapter12/water-fill.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Minh họa thuật toán water-filling [1]</figcaption>
</p>
</figure>
