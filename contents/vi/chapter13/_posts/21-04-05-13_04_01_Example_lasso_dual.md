---
layout: post
title: 13-04-01 Ví dỡ đối ngẫu lasso
chapter: '13'
order: 6
owner: Wontak Ryu
categories:
- chapter13
lang: vi
---

Hãy xem xét bài toán lasso với $$y \in \mathbb{R}^n, X \in \mathbb{R}^{n\times p}$$:

> $$ \min_\beta \frac{1}{2} \| y-X\beta \|^2_2 + \lambda\| \beta \|_1$$
> 
> $$f(\beta) = \frac{1}{2} \| y - X\beta \|^2_2 +  \lambda\| \beta \|_1$$
> 
> $$L(\beta) = f(\beta)$$
> 
>  $$ \min_\beta L(\beta) = f^{\star}$$

Hàm đối ngẫu của bài toán trên là hằng số (= $$f^*$$). Do đó, chúng ta có thể biến đổi bài toán nguyên thủy như sau:

> $$ \min_{\beta,z} \frac{1}{2} \| y-z \|^2_2 + \lambda \| \beta \|_1 \text{ với điều kiện } z = X\beta$$

Hàm đối ngẫu của bài toán đã biến đổi là:
> $$\begin{align}
> g(u) &= \min_{\beta,z} \frac{1}{2} \| y-z \|^2_2 + \lambda \| \beta \|_1 + u^T(z-X\beta) \\
> &= \frac{1}{2} \| y \|^2_2 - \frac{1}{2} \| y-u \|^2_2 - I_{\{ v : \| v \|_\infty \leq 1 \}}(X^Tu/\lambda) \\
> \end{align}$$
> 

#### [Chứng minh]
> $$\begin{align}
> g(u) &= \min_{\beta,z} \frac{1}{2} \| y-z \|^2_2 + \lambda \| \beta \|_1 + u^T(z-X\beta) \\
> &= \underbrace{ \left( \min_z \frac{1}{2} \| y - z \|^2_2 + u^Tz \right)}_{(1)} + \underbrace{\left( \min_\beta  \lambda \| \beta \|_1 + u^TX\beta \right)}_{(2)} \\
> \end{align}$$
> 
> $$ z^{\star} = y - u$$
> 
> $$\begin{align}
> (1) \cdots \left( \min_z \frac{1}{2} \| y - z \|^2_2 + u^Tz \right)
> &= \frac{1}{2} \| u \|^2_2 + u^T(y - u) \\
> &= -\frac{1}{2} \| y - u \|^2_2 + \frac{1}{2} \| y \|^2_2 \\
> \end{align}$$
> $$\begin{align}
> (2) \cdots \left( \min_\beta  \lambda \| \beta \|_1 + u^TX\beta \right) 
> &= - \lambda \max_\beta \frac{u^Tx}{\lambda} \beta - \| \beta \|_2 \\
> &= - \lambda \left( \| \frac{u^Tx}{\lambda} \|_\infty \leq 1 \right) \\
> &= - \lambda \left( \| u^Tx \|_\infty \leq \lambda \right) \\
> \end{align}$$
> \therefore g(u) = -\frac{1}{2} \| y - u \|^2_2 + \frac{1}{2} \| y \|^2_2 + - \lambda \left( \| u^Tx \|_\infty \leq \lambda \right)
> = \frac{1}{2} \| y \|^2_2 - \frac{1}{2} \| y-u \|^2_2 - I_{\{ v : \| v \|_\infty \leq 1 \}}(X^Tu/\lambda)

Do đó, bài toán đối ngẫu lasso là:

> $$ \max_u \frac{1}{2} ( \| y \|^2_2 - \| y-u \|^2_2 ) \text{ với điều kiện } \| X^Tu \|_\infty \leq \lambda$$

Điều này tương đương với:

> $$ \min_u \| y-u \|^2_2 \text{ với điều kiện } \| X^Tu \|_\infty \leq \lambda$$

### [Kiểm tra]
Điều kiện Slater được thỏa mãn, do đó đối ngẫu mạnh đúng.
> $$ \text{đối ngẫu mạnh } \implies (\beta^{\star}, z^{\star})$$
> 
> $$ \text{ phải tối thiểu hóa  } L( \beta, z, u^{\star} ) \text{ trên } -u, \beta, z$$

### [Lưu ý]
Giá trị tối ưu trong bài toán trước không phải là giá trị mục tiêu lasso tối ưu.
Tuy nhiên, nghiệm đối ngẫu $$u$$ và nghiệm lasso $$\beta$$ thỏa mãn $$X\beta = y-u$$.

Điều này được thỏa mãn bởi điều kiện dừng KKT $$z$$ (tức là, $$z-y + \beta = 0$$).

Do đó, lasso thỏa mãn phần dư đối ngẫu.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter13/Conjugate_LassoDual_Example.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig2] Lasso Dual [1]</figcaption>
</p>
</figure>