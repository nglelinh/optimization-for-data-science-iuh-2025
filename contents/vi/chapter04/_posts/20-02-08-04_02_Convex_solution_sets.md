---
layout: post
title: 04-02 Tập nghiệm lồi
chapter: '04'
order: 3
owner: YoungJae Choung
categories:
- chapter04
lang: vi
lesson_type: required
---
Phần này trình bày các tính chất cơ bản của tập nghiệm trong một bài toán tối ưu hóa lồi. <br>
Gọi $$X_{opt}$$ là tập nghiệm tối ưu của một bài toán lồi:

>$$
\begin{aligned}
X_{opt} =
&\text{arg}\min_x &&f(x) \\
&\text{subject to} &&g_{i}(x) \leq 0, \quad i = 1, \dotsc, m \\
&&&h_{j}(x) = 0, \quad j = 1, \dotsc, r  \\\\
\end{aligned}
$$

## Tính chất chính 1
> $$X_{opt}$$ là một tập lồi.

### Chứng minh
> Giả sử $$x$$ và $$y$$ đều là nghiệm tối ưu của bài toán:
> 1. Vì miền xác định $$D$$ là tập lồi nên với mọi $$0 \le t \le 1$$, ta có $$tx + (1-t)y \in D$$.
> 2. Vì $$g_i$$ ($$i=1,\dotsc,m$$) là các hàm lồi và $$h_j$$ ($$j=1, \dotsc,r$$) là các hàm affine, nên điểm $$tx + (1-t)y$$ cũng thỏa mãn mọi ràng buộc:
    $$
    \begin{aligned}
       g_{i}(tx + (1-t)y) &\leq tg_i(x) + (1-t)g_i(y) \leq 0, \\
       h_{j}(tx + (1-t)y) &= th_j(x) + (1-t)h_j(y) = 0.
    \end{aligned}
    $$
> 3. Vì $$f$$ là hàm lồi, ta có:
    $$
    \begin{aligned}
      f(tx+(1-t)y) &\leq tf(x) + (1-t)f(y) \\
      &= tf^{\star} + (1-t) f^{\star} \\
      &= f^{\star},
    \end{aligned}
    $$
    trong đó $$f^{\star}$$ là giá trị tối ưu của bài toán. Do $$tx + (1-t)y$$ là điểm khả thi nên $$f(tx+(1-t)y) \ge f^{\star}$$, suy ra $$f(tx+(1-t)y) = f^{\star}$$. Vậy $$tx + (1-t)y$$ cũng là một nghiệm tối ưu.

### Giải thích hình học
Với một bài toán tối ưu hóa lồi, mọi cực tiểu địa phương đều là cực tiểu toàn cục. <br>
Nếu tập nghiệm chứa nhiều hơn một phần tử, thì mọi tổ hợp lồi của các nghiệm cũng là nghiệm, nên tập nghiệm có dạng phẳng ở đáy như minh họa dưới đây:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter04/multiple-optima.png" alt="[Fig1] geometric interpretation of convexity of the solution set">
  <figcaption style="text-align: center;">[Hình 1] Minh họa hình học về tính lồi của tập nghiệm</figcaption>
</p>
</figure>
<br>

## Tính chất chính 2
> Nếu $$f$$ là hàm lồi chặt, thì nghiệm tối ưu (nếu tồn tại) là duy nhất, tức là $$X_{opt}$$ chứa tối đa một phần tử.

Hàm $$f$$ được gọi là lồi chặt nếu với mọi $$x \neq y \in \text{dom } f$$ và mọi $$0 < t < 1$$, ta luôn có:
>$$f(tx + (1-t)y) < tf(x) + (1-t)f(y).$$

Về mặt hình học, đồ thị của hàm lồi chặt cong hướng lên và không chứa bất kỳ đoạn thẳng phẳng nào, do đó bài toán không thể có hai điểm cực tiểu phân biệt.
