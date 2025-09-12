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

Cho $$c \in \mathbb{R}^n$$, $$A \in \mathbb{R}^{m \times n}$$, $$b \in \mathbb{R}^m$$, $$G \in \mathbb{R}^{r \times n}$$, $$h \in \mathbb{R}^r$$, 

#### Bài toán gốc (Primal LP): 
>
$$
\begin{alignat}{1}
\min_{x} & \quad c^T x   \\\\ 
  s.t.   & \quad Ax = b  \\\\
         & \quad Gx \leq h 
\end{alignat}
$$


#### Bài toán đối ngẫu (Dual LP): 
>
$$
\begin{alignat}{1}
\max_{u,v} & \quad -b^T u - h^T v   \\\\
         s.t. & \quad - A^T u - G^T v = c  \\\\
             & \quad v \geq 0 
\end{alignat}
$$

### Giải thích 1: 

Với mọi $$u$$ và $$v \geq 0$$, và với bất kỳ $$x$$ khả thi của bài toán gốc nào, ta có: 
>
$$
\begin{equation}
u^T (Ax-b) + v^T(Gx-h) \leq 0
\end{equation}
$$

Tức là,

>
$$
\begin{equation}
(-A^Tu - G^Tv)^T x \geq -b^Tu - h^T v
\end{equation}
$$

Từ mối quan hệ này, nếu $$c=-A^Tu - G^Tv$$, ta thu được một cận dưới cho giá trị tối ưu của bài toán gốc. 


### Giải thích 2: 

Với mọi $$u$$ và $$v \geq 0$$, và với bất kỳ $$x$$ khả thi của bài toán gốc nào,

>
$$
\begin{equation}
c^T x \geq c^T x + u^T (Ax-b) + v^T (Gx -h) := L(x,u,v)
\end{equation}
$$

Do đó, nếu $$C$$ là tập khả thi của bài toán gốc và $$f^*$$ là giá trị tối ưu của bài toán gốc, thì 

>
$$
\begin{equation}
f^* \geq \min_{x \in C} L(x,u,v) \geq \min_x L(x,u,v) := g(u,v)
\end{equation}
$$

Nói cách khác, $$g(u,v)$$ là một cận dưới của $$f^*$$. 

>
$$
g(u,v) =
\begin{cases}
-b^T u - h^T v & \text{nếu $c=-A^Tu - G^T v$} \\\\
-\infty            & \text{trường hợp khác} 
\end{cases}
$$

Giải thích thứ hai cho ra cùng một bài toán đối ngẫu như giải thích thứ nhất, nhưng nó hoàn toàn tổng quát và áp dụng được cho các bài toán tối ưu bất kỳ (bao gồm cả những bài toán không lồi).