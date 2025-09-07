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
Hãy cùng tìm hiểu các tính chất của tập nghiệm lồi. <br>
Gọi $$X_{opt}$$ là tập nghiệm của một bài toán lồi:

>$$
\begin{aligned}
X_{opt} =
&\text{arg}\min_x &&f(x) \\
&\text{subject to} &&g_{i}(x) \leq 0, i = 1, .., m \\
&&&h_{j}(x) = 0, j = 1, .., r  \\\\
\end{aligned}
$$

## Tính chất chính 1
> $$X_{opt}$$ là một tập lồi.

### Chứng minh
> Nếu $$x$$ và $$y$$ là các nghiệm:
> 1. Tập miền $$D$$ là lồi, nên với $$0 \le t \le 1$$, $$tx+ (1-t)y \in D$$.
> 2. $$g_i, i=1,\dotsc,m$$ và $$h_j, j=1, \dotsc,r$$ là các hàm lồi và affine, nên các điều kiện sau được thỏa mãn:
    $$
    \begin{aligned}
       g_{i}(tx + (1-t)y) \leq tg_i(x) + (1-t)g_i(y) \leq 0, \\
       h_{j}(tx + (1-t)y) = th_j(x) + (1-t)h_j(y) = 0 \\
    \end{aligned}
    $$
> 3. $$f$$ là hàm lồi, nên:
    >
    >\begin{aligned}
    >  f(tx+(1-t)y) &\leq tf(x) + (1-t)f(y) \\
    >  = tf^{\star} + (1-t) f^{\star} \\
    >  = f^{\star}
    >\end{aligned}
    >trong đó $$f^{\star}$$ là giá trị nhỏ nhất.
    >Vậy, $$tx + (1-t)y$$ cũng là một nghiệm.

### Giải thích hình học
Trong một hàm lồi, bất kỳ cực trị địa phương nào cũng là cực trị toàn cục. <br>
Nếu tập nghiệm chứa nhiều phần tử, nó phải có dạng như sau:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter04/multiple-optima.png" alt="[Fig1] geometric interpretation of convexity of the solution set">
  <figcaption style="text-align: center;">[Hình 1] Giải thích hình học về tính lồi của tập nghiệm</figcaption>
</p>
</figure>
<br>

## Tính chất chính 2
>Nếu $$f$$ là hàm lồi chặt, thì nghiệm là duy nhất. Tức là, $$X_{opt}$$ chỉ chứa một phần tử.

$$f$$ là hàm lồi chặt có nghĩa là $$f$$ luôn thỏa mãn tính chất sau:
>$$f(tx + (1-t)y) < tf(x) + (1-t)f(y),$$
>
>$$\text{trong đó } 0 < t < 1, x \neq y, \text{ và } x, y \in \text{dom } f.$$

Tức là, $$f$$ là hàm lồi hướng xuống không có đoạn phẳng, và nghiệm của $$f$$ là duy nhất.
