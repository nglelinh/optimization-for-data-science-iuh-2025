---
layout: post
title: 14-06-01 Định nghĩa các hàm tự hài hòa
chapter: '14'
order: 13
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
    });
</script>
## Tự hài hòa trên $$\mathbb{R}$$
Một hàm lồi $$f : \mathbb{R} \rightarrow \mathbb{R}$$ được gọi là **tự hài hòa (self-concordant)** nếu nó thỏa mãn bất đẳng thức:
>$$
>\begin{align}
>|f^{'''}(x)| \leq 2f^{''}(x)^{3/2} \qquad \text{for all }x\in \text{dom }f.
>\end{align}
>$$

Ví dụ đơn giản: mọi hàm tuyến tính ($$ax+b$$) và hàm bậc hai lồi đều là hàm tự hài hòa vì đạo hàm bậc ba của chúng bằng $$0$$.

## Tự hài hòa trên $$\mathbb{R}^{n}$$
Một hàm $$f : \mathbb{R}^{n}\rightarrow \mathbb{R}$$ được gọi là tự hài hòa nếu nó tự hài hòa dọc theo mọi đường thẳng cắt miền xác định của nó. Cụ thể, với mọi $$x\in \text{dom}\, f$$ và mọi vector $$v$$, nếu hàm một biến $$g(t) = f(x+tv)$$ là tự hài hòa thì $$f$$ là hàm tự hài hòa trên $$\mathbb{R}^{n}$$.

## Ví dụ về hàm tự hài hòa

1) $$f : \mathbb{R}^{n}_{++}\rightarrow \mathbb{R}$$, $$f(x) = -\sum^{n}_{i=1}\log(x_{i})$$.

Ta có thể dễ dàng kiểm tra rằng hàm một biến $$f(t) = -\log{t}$$ là tự hài hòa. Hơn nữa, tổng của các hàm tự hài hòa cũng là hàm tự hài hòa: với hai hàm tự hài hòa $$f_{1}, f_{2} : \mathbb{R}\rightarrow \mathbb{R}$$, ta có [3]:
>$$
>\begin{align}
>|f_{1}^{'''}(x)+f_{2}^{'''}(x)|  \leq & |f^{'''}_{1}(x)|+|f^{'''}_{2}(x)|\\\\
> \leq &2\big( f^{''}_{1}(x)^{3/2}+f^{''}_{2}(x)^{3/2}\big)\\\\
>\leq &2\big( f^{''}_{1}(x)+f^{''}_{2}(x) \big)^{3/2}.
>\end{align}
>$$

Bước cuối sử dụng bất đẳng thức:
>$$
>\begin{align}
>(u^{3/2}+v^{3/2})^{2/3} \leq u+v, \qquad u, v \geq 0.
>\end{align}
>$$
