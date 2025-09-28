---
layout: post
title: '08-01-03 Phân tích hội tụ'
chapter: '08'
order: 5
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
lesson_type: required
---

Trong gradient descent, ta giả định rằng $$\nabla f$$ liên tục Lipschitz, nhưng trong phương pháp subgradient, ta giả định rằng chính $$f$$ là liên tục Lipschitz. (Xem định lý hội tụ cho gradient descent [06-03-01]({% multilang_post_url contents/chapter06/21-03-20-06_03_01_convergence_analysis_and_proof %}) để tham khảo.)

Giả sử $$f$$ là lồi, dom $$f = \mathbb{R}^n$$, và $$f$$ thỏa mãn điều kiện Lipschitz:

>\begin{align}
> | f(x) - f(y) | \le G \lVert x - y \rVert_2 \text{ với mọi } x, y
\end{align}

Dựa trên các giả định này, công thức hội tụ cho kích thước bước cố định và giảm dần như sau:

## Định lý hội tụ cho kích thước bước cố định

Kích thước bước cố định có tính chất hội tụ sau:
>\begin{align}
> \lim_{k\to\infty} f(x^{(k)}_{best}) \le f^* + \frac{G^{2}t}{2}
\end{align}

## Định lý hội tụ cho kích thước bước giảm dần

Phương pháp kích thước bước giảm dần có tính chất hội tụ sau:

>\begin{align}
\lim_{k\to\infty}f(x^{(k)}_{best}) = f^*
\end{align}

## Chứng minh

Chứng minh cho kích thước bước cố định và giảm dần như sau.

## Chứng minh định lý hội tụ cho kích thước bước cố định

Phương pháp kích thước bước cố định sử dụng $$\sum_{i=1}^{k}t_{i} = kt$$ trong chứng minh.

>$$\begin{align}
& f_{best}^{(k)} - f^* \le \frac{R^{2}+G^{2}\sum_{i=1}^{k}t_{i}^{2}}{2\sum_{i=1}^{k}t_{i}} = \frac{R^{2}+G^{2}k t^{2}}{2kt}  = \frac{R^{2}}{2tk} + \frac{G^{2}t}{2} \\
& \lim_{k→\infty}(f^{(k)}_{best} - f^*) \le 0 + \frac{G^{2}t}{2} = \frac{G^{2}t}{2} \\
& \lim_{k→\infty}(f^{(k)}_{best}) \le f^* + \frac{G^{2}t}{2}
\end{align}
$$


## Chứng minh định lý hội tụ cho kích thước bước giảm dần

Chứng minh cho kích thước bước giảm dần sử dụng các tính chất (1) và (2) sau:

>$$
\begin{align}
\text{(1)} \sum_{i=1}^{\infty} t_i = \infty, \quad \text{(2)}  \sum_{i=1}^{\infty} t_i^{2} = \beta < \infty
\end{align}
$$

>$$
\begin{align}
& f_{best}^{(k)} - f^* \le \frac{R^{2}+G^{2}\sum_{i=1}^{k}t_{i}^{2}}{2\sum_{i=1}^{k}t_{i}} \\
& \lim_{k→\infty}(f^{(k)}_{best} - f^* ) \le \frac{R^{2}+G^{2}\beta}{2\infty} = 0 \\
& \lim_{k→\infty}(f^{(k)}_{best}) =  f^* \\
\end{align}
$$