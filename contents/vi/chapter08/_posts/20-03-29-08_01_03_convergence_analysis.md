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

Trong gradient descent, ta giả thiết $$\nabla f$$ liên tục Lipschitz; còn trong phương pháp subgradient, ta giả thiết chính hàm $$f$$ liên tục Lipschitz (xem thêm định lý hội tụ của gradient descent tại [06-03-01]({% multilang_post_url contents/chapter06/21-03-20-06_03_01_convergence_analysis_and_proof %})).

Giả sử $$f$$ là hàm lồi với $$\text{dom } f = \mathbb{R}^n$$ và thỏa mãn điều kiện Lipschitz:

>\begin{align}
> | f(x) - f(y) | \le G \lVert x - y \rVert_2 \text{ với mọi } x, y
\end{align}

Dưới các giả thiết này, ta có hai kết quả hội tụ tương ứng với kích thước bước cố định và kích thước bước giảm dần.

## Định lý hội tụ cho kích thước bước cố định

Với kích thước bước cố định $$t_k = t$$:
>\begin{align}
> \lim_{k\to\infty} f(x^{(k)}_{best}) \le f^* + \frac{G^{2}t}{2}
\end{align}

## Định lý hội tụ cho kích thước bước giảm dần

Với kích thước bước giảm dần thỏa mãn điều kiện chuẩn:

>\begin{align}
\lim_{k\to\infty}f(x^{(k)}_{best}) = f^*
\end{align}

## Chứng minh

### Trường hợp kích thước bước cố định

Với kích thước bước cố định, ta có $$\sum_{i=1}^{k}t_{i} = kt$$ và $$\sum_{i=1}^{k}t_{i}^{2} = kt^2$$. Thay vào bất đẳng thức cơ bản:

>$$\begin{align}
& f_{best}^{(k)} - f^* \le \frac{R^{2}+G^{2}\sum_{i=1}^{k}t_{i}^{2}}{2\sum_{i=1}^{k}t_{i}} = \frac{R^{2}+G^{2}k t^{2}}{2kt}  = \frac{R^{2}}{2tk} + \frac{G^{2}t}{2} \\
& \lim_{k→\infty}(f^{(k)}_{best} - f^*) \le 0 + \frac{G^{2}t}{2} = \frac{G^{2}t}{2} \\
& \lim_{k→\infty}(f^{(k)}_{best}) \le f^* + \frac{G^{2}t}{2}
\end{align}
$$

### Trường hợp kích thước bước giảm dần

Chứng minh sử dụng hai điều kiện (1) và (2) của dãy kích thước bước giảm dần:

>$$
\begin{align}
\text{(1)} \sum_{i=1}^{\infty} t_i = \infty, \quad \text{(2)}  \sum_{i=1}^{\infty} t_i^{2} = \beta < \infty
\end{align}
$$

Thay vào bất đẳng thức cơ bản và cho $$k \to \infty$$:

>$$
\begin{align}
& f_{best}^{(k)} - f^* \le \frac{R^{2}+G^{2}\sum_{i=1}^{k}t_{i}^{2}}{2\sum_{i=1}^{k}t_{i}} \\
& \lim_{k→\infty}(f^{(k)}_{best} - f^* ) \le \frac{R^{2}+G^{2}\beta}{2\infty} = 0 \\
& \lim_{k→\infty}(f^{(k)}_{best}) =  f^* \\
\end{align}
$$