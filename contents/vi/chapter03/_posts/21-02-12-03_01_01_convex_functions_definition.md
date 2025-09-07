---
layout: post
title: 03-01-01 Định nghĩa
chapter: '03'
order: 3
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---
## Hàm lồi

Một hàm $$f:\mathbb{R}^n \rightarrow \mathbb{R}$$ được gọi là lồi nếu miền xác định của nó là một tập lồi và với bất kỳ hai điểm $$x, y \in \text{dom}f$$, hàm thỏa mãn:

> $$f(\theta x+(1-\theta)y) \le \theta f(x)+(1-\theta)f(y)$$,
>
> với $$0 \le \theta \le 1$$, cho mọi $$x,y \in \text{dom} f$$

Điều này có nghĩa là với bất kỳ hai điểm $$x, y$$, giá trị của $$f$$ tại tổ hợp lồi của chúng nhỏ hơn hoặc bằng tổ hợp lồi của các giá trị hàm tương ứng. Về mặt hình học, đồ thị của $$f$$ nằm dưới đoạn thẳng nối $$f(x)$$ và $$f(y)$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/convex_function2.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Hàm Lồi [2]</figcaption>
</p>
</figure>


## Hàm lồi chặt
Một hàm $$f:\mathbb{R}^n \rightarrow \mathbb{R}$$ được gọi là lồi chặt nếu với bất kỳ hai điểm phân biệt $$x, y \in \text{dom}f$$ và $$0 < \theta < 1$$:

> $$f(\theta x+(1-\theta)y)<\theta f(x)+(1-\theta)f(y)$$,
>
> với $$0<\theta<1$$, $$x \neq y$$, cho mọi $$x, y \in \text{dom}f$$

## Hàm lồi mạnh
Một hàm $$f$$ được gọi là lồi mạnh nếu $$f - \frac{m}{2}\| x \|_{2}^{2}$$, với $$m > 0$$, là hàm lồi.

### [Lưu ý] lồi mạnh ⇒ lồi chặt ⇒ lồi

## Hàm lõm
Một hàm $$f$$ được gọi là lõm nếu $$-f$$ là hàm lồi.

Tất cả các hàm affine $$f(x) = a^T x+b$$ đều thỏa mãn:
> $$
\begin{aligned}
f(\theta x+(1-\theta)y) &= a^T (\theta x+(1-\theta)y) +b \\
&= \theta a^T x + (1-\theta) a^T y + \theta b + (1-\theta) b \\
&= \theta f(x)+(1-\theta)f(y) \\
\end{aligned} 
$$
> $$\text{với mọi } x,y \in \text{dom} f, \text{và } 0 \le \theta \le 1$$

Tức là, các hàm affine luôn vừa lồi vừa lõm.
