---
layout: post
title: '07-03-03 Ví dụ: Điều kiện tối ưu Lasso'
chapter: '07'
order: 9
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
---

Xét bài toán Lasso sau:
>
\begin{equation}
\min_{\beta} \frac{1}{2}  \| y-X\beta \|_2^2 + \lambda \| \beta \|_1
\end{equation}

trong đó $$y \in \mathbb{R}^n$$, $$X \in \mathbb{R}^{n \times p}$$ và $$\lambda \geq 0$$.

Điều kiện tối ưu theo gradient dưới của bài toán này được viết như sau:
>
$$
\eqalign{
0 \in \partial\left(\frac{1}{2} \| y-X\beta \|_2^2 + \lambda \| \beta \|_1\right)
&\quad \Longleftrightarrow \quad 0 \in - X^T (y-X\beta) + \lambda \partial  \| \beta \|_1 \\
&\quad \Longleftrightarrow \quad X^T (y-X\beta)  = \lambda v \\
& \quad \text{với } v \in \partial  \| \beta \|_1 \text{ nào đó}
}\\
$$

Với $$\beta=(\beta_1,\beta_2,\dots,\beta_p )$$, các thành phần của gradient dưới $$v=(v_1,v_2,\dots,v_p)$$ thỏa mãn:

$$
v_i = 
\begin{cases}
 1   &\text{nếu } \beta_i > 0 \\
-1   &\text{nếu } \beta_i < 0 \\
[-1,1]   &\text{nếu } \beta_i = 0
\end{cases}
, i \in \{1,2,\dots,p \}
$$

Bất kỳ $$\beta$$ nào thỏa mãn phương trình sau đều là nghiệm tối ưu:
>
\begin{equation}
X^T(y-X\beta) = \lambda v 
\end{equation}

Viết theo từng tọa độ, $$\beta$$ là nghiệm tối ưu khi và chỉ khi:
>
$$
\begin{cases}
X_i^T(y-X\beta) = \lambda \cdot \text{sign}(\beta_i) &\text{nếu } \beta_i \neq 0 \\
 |X_i^T(y-X\beta)|  \leq \lambda &\text{nếu } \beta_i = 0 
\end{cases}$$

trong đó $$X_i$$ ($$i \in \{1,2,\dots, p \}$$) ký hiệu cột thứ $$i$$ của ma trận $$X$$.
