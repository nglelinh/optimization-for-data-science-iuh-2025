---
layout: post
title: 11 Tính đối ngẫu trong chương trình tổng quát
chapter: '11'
order: 1
owner: Wontak Ryu
categories:
- chapter11
lang: vi
lesson_type: required
---

### Ôn tập: Tính đối ngẫu trong quy hoạch tuyến tính

Cho $$c \in \mathbb{R}^n$$, $$A \in \mathbb{R}^{m \times n}$$, $$b \in \mathbb{R}^m$$, $$G \in \mathbb{R}^{r \times n}$$, $$h \in \mathbb{R}^r$$.

#### Bài toán gốc (Primal LP)
>
$$
\begin{alignat}{1}
\min_{x} & \quad c^T x   \\\\ 
  s.t.   & \quad Ax = b  \\\\
         & \quad Gx \leq h 
\end{alignat}
$$

#### Bài toán đối ngẫu (Dual LP)
>
$$
\begin{alignat}{1}
\max_{u,v} & \quad -b^T u - h^T v   \\\\
         s.t. & \quad - A^T u - G^T v = c  \\\\
             & \quad v \geq 0 
\end{alignat}
$$

### Cách giải thích 1

Với mọi $$u$$, mọi $$v \geq 0$$ và mọi $$x$$ khả thi của bài toán gốc, ta có:

>
$$
\begin{equation}
u^T (Ax-b) + v^T(Gx-h) \leq 0
\end{equation}
$$

Biến đổi bất đẳng thức này, ta thu được:

>
$$
\begin{equation}
(-A^Tu - G^Tv)^T x \geq -b^Tu - h^T v
\end{equation}
$$

Do đó, nếu $$c = -A^Tu - G^Tv$$, thì $$-b^Tu - h^Tv$$ là một cận dưới cho giá trị tối ưu của bài toán gốc.

### Cách giải thích 2

Với mọi $$u$$, mọi $$v \geq 0$$ và mọi $$x$$ khả thi của bài toán gốc, ta có:

>
$$
\begin{equation}
c^T x \geq c^T x + u^T (Ax-b) + v^T (Gx -h) := L(x,u,v)
\end{equation}
$$

Gọi $$C$$ là tập khả thi của bài toán gốc và $$f^*$$ là giá trị tối ưu gốc, khi đó:

>
$$
\begin{equation}
f^* \geq \min_{x \in C} L(x,u,v) \geq \min_x L(x,u,v) := g(u,v)
\end{equation}
$$

Nói cách khác, $$g(u,v)$$ luôn là một cận dưới của $$f^*$$, với biểu thức tường minh:

>
$$
g(u,v) =
\begin{cases}
-b^T u - h^T v & \text{nếu $c=-A^Tu - G^T v$} \\\\
-\infty            & \text{trường hợp khác} 
\end{cases}
$$

Cách giải thích thứ hai cho ra cùng bài toán đối ngẫu như cách thứ nhất, nhưng hoàn toàn tổng quát và áp dụng được cho mọi bài toán tối ưu bất kỳ (kể cả các bài toán không lồi).

## Ứng dụng hiện đại (2022–2026)

Bài đọc tùy chọn đi kèm trình bày cách sử dụng đối ngẫu Lagrange như tín hiệu huấn luyện hoặc chứng chỉ trong tối ưu bền vững theo phân phối (DRO), mạng nơ-ron giải AC-OPF (DC3 / OPF-DNN), phương pháp quy giảm công bằng của Fairlearn và SVM nhân (kernel SVM). Xem [11-08 Ứng dụng hiện đại của đối ngẫu Lagrange]({% multilang_post_url contents/chapter11/2026-09-16-11_08_modern_applications %}).
