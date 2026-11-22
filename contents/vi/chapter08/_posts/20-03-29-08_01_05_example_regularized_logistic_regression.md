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

Cho tập dữ liệu $$(x_i, y_i) \in \mathbb{R}^p \times \{0, 1\}$$ với $$i=1,...,n$$. Hàm mất mát của hồi quy logistic được định nghĩa như sau:
>
\begin{align}
f(\beta) = \sum_{i=1}^n\big(-y_ix_i^T\beta + \log(1+\exp(x_i^T\beta))\big)
\end{align}

Vì đây là tổng hữu hạn của các hàm tuyến tính và hàm log-sum-exp, $$f(\beta)$$ là hàm lồi và khả vi.

Xét bài toán hồi quy logistic có chính quy hóa đối với $$\beta$$:

>
\begin{align}
\min_{\beta} \text{ } f(\beta) + \lambda \cdot P(\beta)
\end{align}

trong đó thành phần phạt $$P(\beta)$$ có thể là $$\Vert \beta \Vert _2^2$$ (chính quy hóa Ridge) hoặc $$\Vert \beta \Vert _1$$ (chính quy hóa Lasso).

Hàm mục tiêu với phạt Ridge vẫn là hàm lồi khả vi, còn hàm mục tiêu với phạt Lasso là hàm lồi không khả vi. Khi áp dụng gradient descent cho bài toán Ridge và phương pháp subgradient cho bài toán Lasso, rồi vẽ giá trị hàm mục tiêu theo số bước lặp $$k$$, ta có thể trực quan hóa sự khác biệt về tốc độ hội tụ giữa hai phương pháp.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter08/08_01_grad_vs_subgrad.png" alt="grad_vs_subgrad" width="90%" height="90%">
</p>
  <figcaption style="text-align: center;">[Fig 1] Gradient descent so với phương pháp Subgradient [3]</figcaption>
</figure>

Kết quả thực nghiệm cho thấy gradient descent hội tụ nhanh hơn đáng kể so với phương pháp subgradient.
