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

Với bài toán lasso được cho dưới đây,
>
\begin{equation}
\min_{\beta} \frac{1}{2}  \| y-X\beta \|_2^2 + \lambda \| \beta \|_1
\end{equation}

trong đó $$y \in \mathbb{R}^n$$, $$X \in \mathbb{R}^{n \times p}$$, $$\lambda \geq 0$$.

Điều kiện tối ưu gradient dưới cho bài toán này có thể được biểu diễn như sau:
>
$$
\eqalign{
0 \in \partial\left(\frac{1}{2} \| y-X\beta \|_2^2 + \lambda \| \beta \|_1\right)
&\quad \Longleftrightarrow \quad 0 \in - X^T (y-X\beta) + \lambda \partial  \| \beta \|_1 \\
&\quad \Longleftrightarrow \quad X^T (y-X\beta)  = \lambda v \\
& \quad \text{với } v \in \partial  \| \beta \|_1 \text{ nào đó}
}\\
$$

Ở đây, đối với một điểm $$\beta=(\beta_1,\beta_2,\dots,\beta_p )$$, gradient dưới $$v=(v_1,v_2,\dots,v_p)$$ được cho bởi:

$$
v_i = 
\begin{cases}
 1   &\text{nếu } \beta_i > 0 \\
-1   &\text{nếu } \beta_i < 0 \\
[-1,1]   &\text{nếu } \beta_i = 0
\end{cases}
, i \in \{1,2,\dots,p \}
$$

Bất kỳ $$\beta$$ nào thỏa mãn điều kiện sau là tối ưu:
>
\begin{equation}
X^T(y-X\beta) = \lambda v 
\end{equation}

Tức là, đối với $$\beta$$ tối ưu, các điều kiện sau được thỏa mãn:
>
$$
\begin{cases}
X_i^T(y-X\beta) = \lambda \cdot \text{sign}(\beta_i) &\text{nếu } \beta_i \neq 0 \\
 |X_i^T(y-X\beta)|  \leq \lambda &\text{nếu } \beta_i = 0 
\end{cases}$$

Ở đây, $$X_i, i \in \{1,2,\dots, p \}$$ ký hiệu cột thứ $$i$$ của ma trận $$X$$.
