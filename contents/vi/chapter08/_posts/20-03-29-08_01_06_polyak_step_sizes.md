---
layout: post
title: '08-01-06 Kích thước bước Polyak'
chapter: '08'
order: 8
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

**Kích thước bước Polyak** là một cách để thiết lập kích thước bước khi giá trị tối ưu được biết. Nếu $$f^*$$ được biết, kích thước bước Polyak có thể được định nghĩa như sau.

## Định lý hội tụ cho kích thước bước Polyak
>
$$ \begin{align}
t_k = \frac{f^{(k-1)}-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}}, \quad k = 1,2,3...
\end{align} $$

## Chứng minh định lý hội tụ cho kích thước bước Polyak
Chứng minh có thể được suy ra từ [bất đẳng thức cơ bản]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}) và chuỗi bất đẳng thức được sử dụng ở đó.

>
$$ \begin{align}
 \Vert x^{(k)}-x^* \Vert_2^{2}  \quad \le \quad  \Vert x^{(k-1)}-x^* \Vert_2^{2}-2t_k (f(x^{(k-1)})-f^*)+t_k^{2} \Vert g^{(k-1)} \Vert_2^{2} \\
\end{align} $$

By differentiating the right-hand side above with respect to $$t_k$$ and setting it to zero, we obtain the Polyak step size that minimizes the right-hand side.
>
$$ \begin{align}
& \frac{\partial}{\partial t_k}  \Vert x^{(k-1)}-x^* \Vert_2^{2}-2t_k (f(x^{(k-1)})-f^*)+t_k^{2} \Vert g^{(k-1)} \Vert_2^{2} = 0 \\
 \Longleftrightarrow & -2(f(x^{(k-1)})-f^*)+2t_k \Vert g^{(k-1)} \Vert_2^{2} = 0 \\
 \Longleftrightarrow & f(x^{(k-1)})-f^* = t_k \Vert g^{(k-1)} \Vert_2^{2} \\
 \Longleftrightarrow & t_k = \frac{f(x^{(k-1)})-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}} \quad \text{(Polyak step size at k)}
\end{align} $$

The convergence rate of the Polyak step size can also be derived from the [basic inequality]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}) and the sequence of inequalities used there.

## Convergence rate for Polyak step-sizes

Let’s substitute the Polyak step size $$t_i$$ into the basic inequality derived in the [basic inequality]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}).
>
$$ \begin{align}
& 2\sum_{i=1}^{k}t_i(f(x^{(i)})-f^*) \le R^2 + \sum_{i=1}^kt_i^2 \Vert g^{(i)} \Vert_2^2 \\
 \Longleftrightarrow \quad & 2\sum_{i=1}^{k}\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \le R^2 + \sum_{i=1}^k\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \\
 \Longleftrightarrow \quad & \sum_{i=1}^{k}\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \le R^2 \\
\end{align} $$

Assuming that the Lipschitz condition $$ \Vert g^{(i)} \Vert_2 \le G$$ always holds, the above inequality can be rearranged as follows:
>
$$ \begin{align}
& \sum_{i=1}^{k}(f(x^{(i)})-f^*)^2 \le R^2G^2 \\
 \Longleftrightarrow \quad & k ⋅ (f(x^{(i)})-f^*)^2 \le R^2G^2 \\
 \Longleftrightarrow \quad & \sqrt{k} ⋅ (f(x^{(i)})-f^*) \le RG \\
 \Longleftrightarrow \quad & (f(x^{(i)})-f^*) \le \frac{RG}{\sqrt{k}} \\
\end{align} $$

If we let $$\frac{RG}{\sqrt{k}}=\epsilon$$, then $$k=\big(\frac{RG}{\epsilon}\big)^2$$, so the number of trials required to reach a suboptimal point with respect to $$\epsilon$$ is on the order of $$\big(\frac{RG}{\epsilon}\big)^2$$. In other words, the convergence rate is $$O(1/\epsilon^{2})$$, which is the same as other subgradient methods.