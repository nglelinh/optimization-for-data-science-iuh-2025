---
layout: post
title: 14-06-01 Định nghĩa các hàm tự hài hòa
chapter: '14'
order: 11
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
## Tự hài hòa trên $$R$$
Một hàm lồi $$f : R \rightarrow R$$ được định nghĩa là tự hài hòa khi nó thỏa mãn phương trình sau:
>$$\begin{align}
>\|f^{'''}(x)\| \leq 2f^{''}(x)^{3/2} \qquad \text{for all }x\in \text{dom }f.
>\end{align}$$

Làm ví dụ đơn giản, các hàm tuyến tính ($$ax+b$$) và các hàm bậc hai (lồi) là tự hài hòa vì giá trị đạo hàm bậc ba của chúng là 0.

## Tự hài hòa trên $$R^{n}$$
Một hàm $$f : R^{n}\rightarrow R$$ được định nghĩa là tự hài hòa khi nó tự hài hòa cho bất kỳ đoạn thẳng nào trong miền, tức là, cho tất cả các đoạn thẳng được bao gồm trong miền. Ví dụ, đối với tất cả $$x\in dom\, f$$ và tất cả $$v$$, khi $$g(t) = f(x+tv)$$ được định nghĩa, nếu $$g(t)$$ là tự hài hòa, thì f được định nghĩa là một hàm tự hài hòa trong miền của $$\mathbb{R}^{n}$$.

## Ví dụ về hàm tự hài hòa

1) $$f : \mathbb{R}^{n}_{++}\rightarrow \mathbb{R}$$, $$f(x) = -\sum^{n}_{i=1}log(x_{i})$$.

Có thể dễ dàng xác minh rằng $$f(t) = -\log{t}$$. Hơn nữa, tổng của các hàm tự hài hòa cũng là tự hài hòa. Khi có các hàm tự hài hòa $$f_{1}, f_{2} : R\rightarrow R$$, tổng của các hàm tự hài hòa cũng là tự hài hòa như được hiển thị dưới đây.[3]
>$$\begin{align}
>|f_{1}^{'''}(x)+f_{2}^{'''}(x)|  \leq & |f^{'''}_{1}(x)|+|f^{'''}_{2}(x)|\\\\
> \leq &2\big( f^{''}_{1}(x)^{3/2}+f^{''}_{2}(x)^{3/2}\big)\\\\
>\leq &2\big( f^{''}_{1}(x)+f^{''}_{2}(x) \big)^{3/2}.
>\end{align}$$

Bước cuối sử dụng tính chất sau:
>$$\begin{align}
>(u^{3/2}+v^{3/2})^{2/3} \leq u+v, \qquad u, v \geq 0.
>\end{align}$$

