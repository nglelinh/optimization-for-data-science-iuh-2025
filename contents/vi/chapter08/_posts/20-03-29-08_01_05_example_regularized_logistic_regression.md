---
layout: post
title: '08-01-05 Ví dụ: Hồi quy Logistic có Điều Chuẩn'
chapter: '08'
order: 7
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
lesson_type: required
---

Giả sử $$(x_i, y_i) \in \mathbb{R}^p \times \{0, 1\}$$ với $$i=1,...,n$$. Hàm mất mát hồi quy logistic được định nghĩa như sau:
>
\begin{align}
f(\beta) = \sum_{i=1}^n\big(-y_ix_i^T\beta + \log(1+\exp(x_i^T\beta))\big)
\end{align}

Hàm này là tổng hữu hạn của một hàm tuyến tính và một hàm log-sum-exp, vì vậy nó là một hàm lồi khả vi.

Bây giờ, bài toán regularization cho $$\beta$$ được công thức hóa như sau:

>
\begin{align}
\min_{\beta} \text{ } f(\beta) + \lambda \cdot P(\beta)
\end{align}

Ở đây, $$P(\beta)$$ có thể được định nghĩa là $$\Vert \beta \Vert _2^2$$ (phạt ridge) hoặc $$\Vert \beta \Vert _1$$ (phạt lasso).

Hàm mất mát với phạt ridge vẫn là một hàm lồi khả vi, nhưng hàm mất mát với phạt lasso trở thành một hàm lồi không khả vi. Đối với hai hàm mất mát này, chúng ta có thể áp dụng gradient descent cho ridge và phương pháp subgradient cho lasso, và bằng cách vẽ đồ thị giá trị hàm mục tiêu tại lần lặp $$k$$, chúng ta có thể quan sát đặc điểm hội tụ của cả hai phương pháp.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter08/08_01_grad_vs_subgrad.png" alt="grad_vs_subgrad" width="90%" height="90%">
</p>
  <figcaption style="text-align: center;">[Fig 1] Gradient descent so với phương pháp Subgradient [3]</figcaption>
</figure>

Thí nghiệm này cho thấy rằng gradient descent hội tụ nhanh hơn nhiều so với phương pháp subgradient.
