---
layout: post
title: 06-03-02 Phân Tích Hội Tụ & Chứng Minh
chapter: '06'
order: 11
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Giả sử $$f$$ lồi, khả vi với $$dom(f) = \mathbb{R}^n$$ và $$\nabla f$$ liên tục Lipschitz với hằng số $$L > 0$$:

>$$ \| \nabla f(x) - \nabla f(y) \|_2 \le L \| x - y \|_2 \quad \text{với mọi } x, y$$

Tham khảo: [[Wikipedia: Lipschitz continuity](https://en.wikipedia.org/wiki/Lipschitz_continuity)]

## Định lý Hội tụ

Thuật toán **gradient descent** với kích thước bước cố định $$t \le 1/L$$ thỏa mãn:
>$$
\begin{align}
f(x^{(k)}) - f^* \le \frac{ \| x^{(0)} - x^* \|^2_2 }{2tk}
\end{align}
$$

Với kích thước bước cố định, tốc độ hội tụ là $$O(1/k)$$. Do đó, để đạt sai số $$f(x^{(k)}) - f^* \le \epsilon$$, thuật toán cần $$O(1/\epsilon)$$ vòng lặp.

## Chứng minh (Bổ đề giảm)

Vì $$f$$ lồi và $$\nabla f$$ liên tục Lipschitz với hằng số $$L$$, hàm $$f$$ thỏa mãn cận trên bậc hai (xem [06-03-01]({% multilang_post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %})):

> $$
\begin{align}
f(y) \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \| y - x \|^2_2 \quad \forall x, y
\end{align}
$$

Với bước cập nhật gradient descent $$x^+ = x - t \nabla f(x)$$, thay $$y = x^+$$ vào bất đẳng thức trên, ta được:

>$$
\begin{align}
f(x^+) & \le f(x) - t \left( 1 - \frac{Lt}{2} \right)\| \nabla f(x) \|^2_2 \\
& \le f(x) - \frac{t}{2} \| \nabla f(x) \|^2_2 \quad \text{nếu } t \le 1/L
\end{align}
$$

Do đó $$f(x^+) < f(x)$$ mỗi khi $$\nabla f(x) \neq 0$$, cho thấy giá trị hàm mục tiêu giảm nghiêm ngặt qua từng bước lặp và tiến tới hội tụ.
